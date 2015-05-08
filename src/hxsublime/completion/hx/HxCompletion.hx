package hxsublime.completion.hx;

import hxsublime.build.Build;
import hxsublime.compiler.Output;
import hxsublime.completion.hx.Constants;
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
    public static function triggerCompletion (view:View, options:CompletionOptions, show_top_level_snippets = false)
    {
        function run()
        {
            var project = Projects.currentProject(view);


            if (!project.hasBuild()) {
                project.extractBuildArgs(view, false);
            }


            if (project.hasBuild()) {
                project.completionContext.setTrigger(view, options);


                view.run_command( "auto_complete" , python.Lib.anonToDict({
                    "api_completions_only" : !show_top_level_snippets,
                    "disable_auto_insert" : true,
                    "next_completion_if_showing" : true,
                    'auto_complete_commit_on_tab': true
                }));
            }
            else {

                project.extractBuildArgs(view, true);
            }
        }

        view.run_command('hide_auto_complete');

        Sublime.set_timeout(run, 0);
    }

    public static function autoComplete(project:Project, view:View, offset:Int, prefix:String)
    {

        trace("run auto_complete");
        // if completion is triggered by a background completion process
        // completion return the result

        var options = project.completionContext.getAndDeleteTrigger(view);
        var res = null;
        if (options != null && options.asyncTrigger())
        {
            trace("run auto_complete 1");
            var async_result = project.completionContext.getAndDeleteAsync(view);

            var use_async_results = async_result != null && async_result.hasResults();
            if (use_async_results)
            {
                trace("run auto_complete 2");
                res = getAvailableAsyncCompletions(async_result, view);
                res = completionResultWithSmartSnippets(view, res, async_result, options);
                trace(res);
            }
            else
            {
                trace("run auto_complete 3");
                res = cancelCompletion(view);
            }
        }
        else
        {
            trace("create comps");
            res = createNewCompletions(project, view, offset, options, prefix);
            //trace("res:" + res);
            trace("after create comps");
        }


        return res;
    }

    static function getAvailableAsyncCompletions(compResult:CompletionResult, view:View)
    {

        var ctx = compResult.ctx;

        var has_results = compResult.hasResults();

        var discard_results = !has_results && ctx.options.types().hasHint();

        return if (discard_results) cancelCompletion(view)  else combineHintsAndComps(compResult);
    }


    static function completionResultWithSmartSnippets (view:View, comps:Array<Tuple2<String, String>>, result:CompletionResult, options:CompletionOptions)
    {

        var use_snippets = Settings.smartSnippets(view);
        var prefix_is_whitespace = hxsublime.tools.StringTools.isWhitespaceOrEmpty(result.ctx.prefix);
        var has_one_hint = options.types().hasHint() && result.hints.length == 1;
        var same_cursor_pos = ViewTools.getFirstCursorPos(view) == result.ctx.view_pos;


        // we don't want to insert the snippet if there is already an argument
        // in that case only the hint should be shown
        var lineAfterOffset = result.ctx.lineAfterOffset().strip();
        var really_insert = lineAfterOffset.length == 0 || "),".indexOf(lineAfterOffset.charAt(0)) > -1;

        if (really_insert && prefix_is_whitespace && use_snippets && has_one_hint && same_cursor_pos)
        {
            var onlyHint = comps[0];
            ViewTools.insertSnippet(view, onlyHint._2);
            comps = cancelCompletion(view);
        }
        return comps;
    }




    static function createNewCompletions(project:Project, view:View, offset:Int, options:CompletionOptions, prefix:String)
    {
        var cache = project.completionContext.current;

        trace("------- COMPLETION START -----------");

        var ctx = createCompletionContext(project, view, offset, options, prefix);

        var res = null;

        trace("MANUAL COMPLETION: " + Std.string(ctx.options.manualCompletion()));

        // autocompletion is triggered, but its already
        // running as a background process, starting it
        // again would result in multiple queries for
        // the same view && src position
        if (isEquivalentCompletionAlreadyRunning(ctx))
        {
            trace("cancel completion, same is running");
            res = cancelCompletion(ctx.view);
        }
        else if (!ctx.options.manualCompletion())
        {
            triggerManualCompletion(ctx.view, ctx.options.copyAsManual() );
            res = cancelCompletion(ctx.view);
        }
        else if (isAfterIntIterator(ctx.src(), ctx.offset))
        {
            res = cancelCompletion(ctx.view);
        }
        else if (isIntIteratorCompletion(ctx.src(), ctx.offset))
        {
            trace("iterator completion");
            res = [Tuple2.make(".\tint iterator", "..")];
        }
        else
        {
            if (isHintCompletion(ctx))
            {
                trace("ADD HINT");
                ctx.options.types().addHint();
            }

            var isDirectlyAfterControlStruct = ctx.completeCharIsAfterControlStruct();

            var onlyTopLevel = ctx.is_new() || isDirectlyAfterControlStruct;


            trace("onlyTopLevel: " + Std.string(onlyTopLevel));


            if (onlyTopLevel)
            {
                res = getToplevelCompletions(ctx);
            }
            else
            {

                var last_ctx = cache.input;

                if (useCompletionCache(ctx,last_ctx))
                {
                    trace("USE COMPLETION CACHE");
                    var out = cache.output;
                    updateCompletionCache(cache, out);
                    project.completionContext.addCompletionResult(out);
                    res = cancelCompletion(view);
                    triggerAsyncCompletion(view, ctx.options, out.showTopLevelSnippets());
                }
                else if (supportedCompilerCompletionChar(ctx.completeChar()))
                {
                    trace("supported char");
                    var compBuild = createCompletionBuild(ctx);
                    if (compBuild != null) {
                        runCompilerCompletion(compBuild, function (out, err) completionFinished(ctx, compBuild,  out, err));
                    }
                    else {
                        trace("couldn't create temp path && files which are neccessary for completion");
                    }
                    // we don't show any completions at this point

                    res = cancelCompletion(view, true);
                }
                else
                {
                    var compResult = CompletionResult.emptyResult(ctx, function () return getToplevelCompletions(ctx));
                    updateCompletionCache(cache, compResult);
                    project.completionContext.addCompletionResult(compResult);
                    res = cancelCompletion(view);
                    triggerAsyncCompletion(view, ctx.options, compResult.showTopLevelSnippets());
                }
            }
        }
        return res;
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
            var build =compBuild.build;
            var display = compBuild.display();
            var macroCompletion = ctx.options.macroCompletion();
            // prepare build options
            build.setAutoCompletion(display, macroCompletion);
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

        var async = ctx.settings.isAsyncCompletion();

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

        trace("ASYNC: " + async);

        build.run(project, view, async, onResult);
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
            project.completionContext.addCompletionResult(compResult);
            var showTopLevelSnippets = compResult.showTopLevelSnippets();
            triggerAsyncCompletion(view, ctx.options, showTopLevelSnippets);
        }
        else
        {
            trace("ignore background completion on finished")  ;
        }
    }


    static function hintsToSublimeCompletions(hints:Array<Array<String>>)
    {
        function make_hint_comp (h:Array<String>)
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

                        if (params.length == 1)
                        {
                            insert = "${1:" + first + "})${0}";
                        }
                        else
                        {
                            insert = "${0:" + first + "}";
                        }
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

        return [for (h in hints) make_hint_comp(h)];
    }



    static function combineHintsAndComps (compResult:CompletionResult)
    {
        var all_comps = hintsToSublimeCompletions(compResult.hints);



        if (!compResult.ctx.options.types().hasHint() || compResult.hints.length == 0)
        {
            trace("TAKE TOP LEVEL COMPS");
            all_comps.extend(compResult.allComps());
        }
        else
        {
            if (compResult.hints.length == 1)
            {
                Sublime.status_message("signature: " + compResult.hints[0].join("->"));
            }
        }
            // insert hint directly


        //if len(compResult.hints) == 1:
        //    hxpanel.default_panel().writeln(compResult.doc);
        return all_comps;
    }



    static function isIntIteratorCompletion(src:String, offset:Int)
    {
        var o = offset;
        var s = src;
        return o > 3 && s.charAt(o) == "\n" && s.charAt(o-1) == "." && s.charAt(o-2) == "." && s.charAt(o-3) != ".";
    }

    static function isAfterIntIterator(src:String, offset:Int)
    {
        var o = offset;
        var s = src;
        return o > 3 && s.charAt(o) == "\n" && s.charAt(o-1) == "." && s.charAt(o-2) == "." && s.charAt(o-3) == ".";
    }

    static function isHintCompletion(ctx:CompletionContext)
    {
        var whitespace_re = Re.compile("^\\s*$");
        return "(,".indexOf(ctx.completeChar()) > -1 && Re.match(whitespace_re, ctx.prefix) != null;
    }


    static function isEquivalentCompletionAlreadyRunning(ctx:CompletionContext)
    {
        return ctx.project.completionContext.isEquivalentCompletionAlreadyRunning(ctx);
    }

    static function shouldIncludeTopLevelCompletion(ctx:CompletionContext)
    {

        trace("complete Char: '" + ctx.completeChar() + "'");
        var toplevel_complete = ":(,{;})".indexOf(ctx.completeChar()) > -1 || ctx.inControlStruct() || ctx.is_new();

        trace("should include: " + toplevel_complete);


        return toplevel_complete;
    }


    static function getToplevelCompletions(ctx:CompletionContext)
    {
        trace("get top level completions");

        var comps = if (shouldIncludeTopLevelCompletion( ctx ))
        {
            TopLevel.getToplevelCompletionFiltered( ctx );
        }
        else
        {
            [];
        }

        return comps;
    }


    static function createCompletionContext(project:Project, view:View, offset:Int, options:CompletionOptions, prefix:String)
    {

        // if options are null, it's a completion progress initialized by sublime,
        // !by the user or by key trigger

        trace("OPTIONS:" + Std.string(options));

        if (options == null) {
            options = new CompletionOptions(Constants.COMPLETION_TRIGGER_AUTO);
        }

        trace(options);


        var settings = new CompletionSettings(Settings);
        var ctx = new CompletionContext(view, project, offset, options, settings, prefix);
        return ctx;
    }

    static function updateCompletionCache(cache:CompletionCache, compResult:CompletionResult)
    {
        cache.output = compResult;
        cache.input = compResult.ctx;
    }


    static function log_completion_status(status, comps, hints)
    {
        if (status != "") {
            if (comps.length > 0 || hints.length > 0) {
                trace(status);
            }
            else {
                Panels.defaultPanel().writeln( status );
            }
        }
    }


    static function outputToResult (ctx:CompletionContext, temp_file, err, ret, retrieve_tl_comps)
    {
        var r = Output.getCompletionOutput(temp_file, ctx.orig_file(), err, ctx.commas());
        var hints = r._1, comps1 = r._2, status = r._3, errors = r._4;
        // we don't need doc here
        var comps2 = [for (t in comps1) Tuple2.make(t.hint, t.insert)];
        ctx.project.completionContext.setErrors(errors);
        highlightErrors( errors, ctx.view );
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

    static function cancelCompletion(view:View, hideComplete = true):Array<Tuple2<String,String>>
    {
        if (hideComplete)
        {
            // this seems to work fine, it cancels the sublime
            // triggered completion without poping up a completion
            // view
            view.run_command('hide_auto_complete');
        }
        return [Tuple2.make("  ...  ", "")];
    }


    static function triggerAsyncCompletion(view:View, options:CompletionOptions, showTopLevelSnippets = false)
    {
        var asyncOptions = options.copyAsAsync();

        function runComplete()
        {
            triggerCompletion(view, asyncOptions, showTopLevelSnippets);
        }

        Sublime.set_timeout(runComplete, 2);
    }

    static function triggerManualCompletion(view:View, options:CompletionOptions)
    {

        var hint = options.types().hasHint();
        var macroComp = options.macroCompletion();

        function runComplete()
        {
            if (hint && macroComp)
            {
                view.run_command("hxsublime_commands__haxe_hint_display_macro_completion");
            }
            else if (hint)
            {
                view.run_command("hxsublime_commands__haxe_hint_display_completion");
            }
            else if (macroComp)
            {
                view.run_command("hxsublime_commands__haxe_display_macro_completion");
            }
            else
            {
                view.run_command("hxsublime_commands__haxe_display_completion");
            }
        }

        Sublime.set_timeout(runComplete, 2);
    }
}
