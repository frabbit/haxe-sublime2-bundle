package hxsublime.completion.hx;

import haxe.ds.Option;
import hxsublime.build.Build;
import hxsublime.compiler.Output;
import hxsublime.completion.Completion.CompletionListener;
import hxsublime.completion.hx.Toplevel.TopLevel;
import hxsublime.completion.hx.CompletionBuild;
import hxsublime.completion.hx.CompletionContext;
import hxsublime.completion.hx.CompletionOptions;
import hxsublime.completion.hx.CompletionResult;
import hxsublime.completion.hx.CompletionSettings;
import hxsublime.panel.Panels;
import hxsublime.project.Projects;
import hxsublime.project.CompletionState.CompletionCache;
import hxsublime.project.Project;
import hxsublime.Settings;
import hxsublime.Temp;
import hxsublime.tools.ViewTools;
import python.lib.Re;
import python.lib.Time;
import python.Dict;
import python.Tuple;
import sublime.Region;
import sublime.Sublime;
import sublime.View;

using hxsublime.support.ArrayTools;

using hxsublime.support.StringTools;

class HxCompletion
{
	public static function eventTriggeredAutoComplete(project:Project, view:View, offset:Int, prefix:String)
	{
		trace("------- EVENT TRIGGERED COMPLETION -----------");
		var options = new CompletionOptions(false);
		var ctx = createCompletionContext(project, view, offset, options, prefix);
		return autoComplete(ctx);
	}

	public static function commandTriggeredAutoComplete(project:Project, view:View, offset:Int, options:CompletionOptions, prefix:String)
	{
		trace("------- COMMAND TRIGGERED COMPLETION -----------");
		var ctx = createCompletionContext(project, view, offset, options, prefix);
		return autoComplete(ctx);
	}

	
	static function createCompletionContext(project:Project, view:View, offset:Int, options:CompletionOptions, prefix:String)
	{
		var settings = new CompletionSettings(Settings);
		return new CompletionContext(view, project, offset, options, settings, prefix);
	}

	static function autoComplete(ctx:CompletionContext)
	{
		var project = ctx.project;
		var view = ctx.view;
		
		var cache = project.completionContext.current;

		// cancel current completion because we trigger it later after asynchronously collecting entries
		cancelCompletion(view);

		if (isEquivalentCompletionAlreadyRunning(ctx))
		{
			trace("cancel completion, same is running");
		}
		else if (useCompletionCache(ctx, cache.input))
		{
			trace("use completion cache");
			var out = cache.output;

			updateCompletionCache(cache, out);
			triggerAsyncCompletion(ctx, out, out.showTopLevelSnippets());
		}
		else if (supportedCompilerCompletionChar(ctx.completeChar()))
		{
			trace("call compiler for completion");
			var compBuild = createCompletionBuild(ctx);
			if (compBuild != null) {
				function cb (out, err) completionFinished(ctx, compBuild,  out, err);
				runCompilerCompletion(compBuild, cb);
			}
		}
		else
		{
			trace("only toplevel + snippets");
			var compResult = CompletionResult.emptyResult(ctx, function () return getToplevelCompletions(ctx));
			updateCompletionCache(cache, compResult);
			triggerAsyncCompletion(ctx, compResult, compResult.showTopLevelSnippets());
		}
		return [];
	}

	static function createCompletionBuild (ctx:CompletionContext)
	{
		var tmp_src = ctx.tempCompletionSrc();

		var r = Temp.createTempPathAndFile(ctx.build(), ctx.orig_file(), tmp_src);
		var tempPath = r._1, tempFile = r._2;

		var temp_creation_success = tempPath != null && tempFile != null;

	   	function mkBuild()
	   	{
			var compBuild = new CompletionBuild(ctx, tempPath, tempFile);
			var build = compBuild.build;
			var display = compBuild.display();
			
			// prepare build options
			build.setAutoCompletion(display, false);
			if (ctx.settings.showCompletionTimes(compBuild.ctx.view))
			{
				build.setTimes();
			}
			return compBuild;
		}
		return if (temp_creation_success) mkBuild() else null;
	}


	static function runCompilerCompletion(compBuild:CompletionBuild, callback:String->String->Void)
	{
		var startTime = Time.time();
		var ctx = compBuild.ctx;
		var project = ctx.project;
		var build = compBuild.build;
		var view = ctx.view;

		function inMainThread (out, err)
		{
			function run ()
			{
				var runTime = Time.time() - startTime;
				trace("completion time: " + Std.string(runTime));
				Temp.removePath(compBuild.tempPath);
				callback(out, err);
			}

			// because of async completion, the current completion could be
			// out of date, because a newer completion was triggered, so run should
			// only be called if this completion is still up to date
			project.completionContext.runIfStillUpToDate(ctx.id, run);
		}
		function onResult(out:String, err:String)
		{
			Sublime.set_timeout(inMainThread.bind(out, err), 2);
		}

		// store the data of the currently running completion operation in cache to fetch it later
		project.completionContext.setNewCompletion(ctx);

		build.run(project, view, true, onResult);
	}

	static function completionFinished(ctx:CompletionContext, compBuild:CompletionBuild, out:String, err:String)
	{
		var ctx = compBuild.ctx;
		var tempFile = compBuild.tempFile;

		var cache = compBuild.cache;

		var project = ctx.project;
		var view = ctx.view;


		var compResult = outputToResult(ctx, tempFile, err, out, function () return getToplevelCompletions(ctx));

		var hasResults = compResult.hasResults();

		if (hasResults)
		{
			updateCompletionCache(cache, compResult);
			var showTopLevelSnippets = compResult.showTopLevelSnippets();
			triggerAsyncCompletion(ctx, compResult, showTopLevelSnippets);
		}
		else
		{
			trace("ignore background completion on finished")  ;
		}
	}


	static function hintsToSublimeCompletions(hints:Array<Array<String>>)
	{
		function makeHintComp (h:Array<String>)
		{
			var hintIsJustAType = h.length == 1;

			var res = null;

			if (hintIsJustAType) {
				res = Tuple2.make(h[0] + " - No Completion", "${}");
			}
			else {
				var isFunctionWithoutParams = (h.length) == 2 && h[0] == "Void";

				var insert = null;
				var show = null;

				if (isFunctionWithoutParams)
				{
					insert = ")";
					show = "Void";
				}
				else {

					function escapeParam(p:String) {
						return p.split("}").join("\\}");
					}
					var last_index = h.length-1;
					var params = h.slice(0, last_index);

					show = params.join(", ");

					if (Settings.smartSnippetsJustCurrent())
					{
						// insert only the snippet for the current parameter
						var first = escapeParam(params[0]);

						insert = 
							if (params.length == 1)
								"${1:" + first + "})${0}"
							else
								"${0:" + first + "}";
					}
					else {
						// the last param gets index 0, which is the exit mark for snippets
						function getSnippetIndex(listIndex:Int)
						{
							return Std.string(listIndex+1);
						}

						function paramSnippet(param:String, index:Int)
						{
							return "${" + getSnippetIndex(index) + ":" + escapeParam(param) + "}";
						}

						var snippetList = [for (index in 0...params.length) paramSnippet(params[index], index)];

						insert = snippetList.join(",") + ")${0}";
					}
				}

				res = Tuple2.make(show, insert);
			}
			return res;
		}
		return [for (h in hints) makeHintComp(h)];
	}

	static function combineHintsAndComps (compResult:CompletionResult)
	{
		var hints = compResult.hints;

		var all_comps = hintsToSublimeCompletions(hints);

		if (!compResult.ctx.isHint() || hints.length == 0)
		{
			trace("TAKE TOP LEVEL COMPS");
			all_comps.extend(compResult.allComps());
		}
		else if (hints.length == 1)
		{
			Sublime.status_message("signature: " + hints[0].join("->"));
		}

		return all_comps;
	}

	static function isEquivalentCompletionAlreadyRunning(ctx:CompletionContext)
	{
		return ctx.project.completionContext.isEquivalentCompletionAlreadyRunning(ctx);
	}

	static function shouldIncludeTopLevelCompletion(ctx:CompletionContext)
	{
		trace("complete Char: '" + ctx.completeChar() + "'");

		var validChar = ":(,{;})".indexOf(ctx.completeChar()) > -1;

		var toplevel_complete = validChar || ctx.inControlStruct() || ctx.is_new();

		return toplevel_complete;
	}

	static function getToplevelCompletions(ctx:CompletionContext)
	{
		var user = ctx.options.userActivated;

		var settingsValid = !Settings.topLevelCompletionsOnDemand();
		var prefixValid = ctx.prefix != "";

		var userOrValid = user || (prefixValid && settingsValid);

		var toplevelInclude = userOrValid && shouldIncludeTopLevelCompletion( ctx );

		var comps = 
			if (toplevelInclude)
				TopLevel.getToplevelCompletionFiltered( ctx );
			else [];

		return comps;
	}

	static function updateCompletionCache(cache:CompletionCache, compResult:CompletionResult)
	{
		cache.output = compResult;
		cache.input = compResult.ctx;
	}

	static function outputToResult (ctx:CompletionContext, temp_file, err, ret, retrieve_tl_comps)
	{
		var r = Output.getCompletionOutput(temp_file, ctx.orig_file(), err, ctx.commas());
		var hints = r._1, comps1 = r._2, status = r._3, errors = r._4;
		
		// we don't need doc here
		var comps2 = [for (t in comps1) Tuple2.make(t.hint, t.insert)];
		ctx.project.completionContext.setErrors(errors);
		if (ctx.options.userActivated) {
			trace("do highlight");
			highlightErrors( errors, ctx.view );
		}
		// top level completions are empty until they are really required
		return new CompletionResult(ret, comps2, status, hints, ctx, retrieve_tl_comps );
	}

	static function useCompletionCache (lastInput:CompletionContext, current_input:CompletionContext)
	{
		return lastInput.eq(current_input);
	}

	static function supportedCompilerCompletionChar (char:String)
	{
		return "(.,".indexOf(char) > -1;
	}

	static function highlightErrors( errors:Array<CompilerError> , view:View ):Void
	{
		var regions = [];

		for (e in errors)
		{
			var l = e.line;
			var left = e.from;
			var right = e.to;
			var a = view.text_point(l,left);
			var b = view.text_point(l,right);
			regions.append( new Region(a,b));

			Panels.defaultPanel().status( "Error" , e.file + ":" + Std.string(l) + ": characters " + Std.string(left) + "-" + Std.string(right) + ": " + e.message);
		}

		view.add_regions("haxe-error" , regions , "invalid" , "dot" );
	}

	static function cancelCompletion(view:View)
	{
		view.run_command('hide_auto_complete');
	}

	static function shouldOnlyInsertHint (ctx:CompletionContext, result:CompletionResult)
	{
		var view = ctx.view;
		var use_snippets = Settings.smartSnippets(view);
		var prefix_is_whitespace = hxsublime.tools.StringTools.isWhitespaceOrEmpty(result.ctx.prefix);
		var has_one_hint = ctx.isHint() && result.hints.length == 1;
		var same_cursor_pos = ViewTools.getFirstCursorPos(view) == result.ctx.view_pos;

		// we don't want to insert the snippet if there is already an argument
		// in that case only the hint should be shown
		var lineAfterOffset = result.ctx.lineAfterOffset().strip();
		var really_insert = lineAfterOffset.length == 0 || "),".indexOf(lineAfterOffset.charAt(0)) > -1;

		return really_insert && prefix_is_whitespace && use_snippets && has_one_hint && same_cursor_pos;
		
	}    
		
	static function autoCompleteAsync (ctx:CompletionContext, res:CompletionResult ) 
	{
		var view = ctx.view;
		var ctx = res.ctx;
		var use_async_results = res != null && res.hasResults();
		return if (use_async_results)
		{
			var comps = combineHintsAndComps(res);
			if (shouldOnlyInsertHint(ctx, res)) {
				var onlyHint = comps[0];
				ViewTools.insertSnippet(view, onlyHint._2);
				None;
			} else {
				Some(comps);
			}
		}
		else None;
	}

	static function triggerAsyncCompletion(ctx:CompletionContext, res:CompletionResult, showTopLevelSnippets = false)
	{
		var cb = function (_) return switch autoCompleteAsync(ctx, res) {
			case Some(x): x;
			case None: cancelCompletion(ctx.view); [];
		};
		trace("trigger with " + showTopLevelSnippets);
		CompletionListener.trigger(ctx.view, showTopLevelSnippets, cb);
	}

	
}
