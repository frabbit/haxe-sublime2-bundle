package hxsublime.completion.hx;

import hxsublime.build.Build;
import hxsublime.compiler.Output;
import hxsublime.completion.hx.Constants;
import hxsublime.completion.hx.Toplevel.TopLevel;
import hxsublime.completion.hx.Types.CompletionBuild;
import hxsublime.completion.hx.Types.CompletionContext;
import hxsublime.completion.hx.Types.CompletionOptions;
import hxsublime.completion.hx.Types.CompletionResult;
import hxsublime.completion.hx.Types.CompletionSettings;
import hxsublime.panel.Base.Panels;
import hxsublime.project.Base.Projects;
import hxsublime.project.CompletionState.CompletionCache;
import hxsublime.project.Project;
import hxsublime.Settings;
import hxsublime.Temp;
import hxsublime.tools.ViewTools;
import python.lib.Re;
import python.lib.Time;
import python.lib.Types.Dict;
import python.lib.Types.Tup2;
import sublime.Region;
import sublime.Sublime;
import sublime.View;

using python.lib.ArrayTools;

using python.lib.StringTools;

class Base {
    public static function trigger_completion (view:View, options:CompletionOptions, show_top_level_snippets = false) {


        function run() 
        {
            var project = Projects.current_project(view);
            

            if (!project.has_build()) {
                project.extract_build_args(view, false);
            }


            if (project.has_build()) {
                project.completion_context.set_trigger(view, options);

                
                view.run_command( "auto_complete" , Dict.fromObject({
                    "api_completions_only" : !show_top_level_snippets,
                    "disable_auto_insert" : true,
                    "next_completion_if_showing" : true,
                    'auto_complete_commit_on_tab': true
                }));
            }
            else {

                project.extract_build_args(view, true);
            }
        }

        view.run_command('hide_auto_complete');

        Sublime.set_timeout(run, 0);
    }

    public static function get_available_async_completions(comp_result:CompletionResult, view:View) {

        var ctx = comp_result.ctx;

        var has_results = comp_result.has_results();

        var discard_results = !has_results && ctx.options.types().has_hint();

        return if (discard_results) cancel_completion(view)  else combine_hints_and_comps(comp_result);
    }


    public static function completion_result_with_smart_snippets (view:View, comps:Array<Tup2<String, String>>, result:CompletionResult, options:CompletionOptions) 
    {

        var use_snippets = Settings.smart_snippets(view);
        var prefix_is_whitespace = hxsublime.tools.StringTools.isWhitespaceOrEmpty(result.ctx.prefix);
        var has_one_hint = options.types().has_hint() && result.hints.length == 1;
        var same_cursor_pos = ViewTools.getFirstCursorPos(view) == result.ctx.view_pos;
        
        
        // we don't want to insert the snippet if there is already an argument
        // in that case only the hint should be shown
        var line_after_offset = result.ctx.line_after_offset().strip();
        var really_insert = line_after_offset.length == 0 || "),".indexOf(line_after_offset.charAt(0)) > -1;
      
        if (really_insert && prefix_is_whitespace && use_snippets && has_one_hint && same_cursor_pos) {
            var only_hint = comps[0];
            ViewTools.insertSnippet(view, only_hint._2);
            comps = cancel_completion(view);
        }
        return comps;
    }

    public static function auto_complete(project:Project, view:View, offset:Int, prefix:String) {

        trace("run auto_complete");
        // if completion is triggered by a background completion process
        // completion return the result

        var options = project.completion_context.get_and_delete_trigger(view);
        var res = null;
        if (options != null && options.async_trigger()) {
            trace("run auto_complete 1");
            var async_result = project.completion_context.get_and_delete_async(view);
            
            var use_async_results = async_result != null && async_result.has_results();
            if (use_async_results) {
                trace("run auto_complete 2");
                res = get_available_async_completions(async_result, view);
                res = completion_result_with_smart_snippets(view, res, async_result, options);
                trace(res);
            }
                
            else {
                trace("run auto_complete 3");
                res = cancel_completion(view);
            }
        }
        else {
            trace("create comps");
            res = create_new_completions(project, view, offset, options, prefix);
            //trace("res:" + res);
            trace("after create comps");
        }

        
        return res;
    }


    public static function create_new_completions(project:Project, view:View, offset:Int, options:CompletionOptions, prefix:String) {

        var cache = project.completion_context.current;

        trace("------- COMPLETION START -----------");

        var ctx = create_completion_context(project, view, offset, options, prefix);

        var res = null;
        
        trace("MANUAL COMPLETION: " + Std.string(ctx.options.manual_completion));

        // autocompletion is triggered, but its already 
        // running as a background process, starting it
        // again would result in multiple queries for
        // the same view && src position
        if (is_equivalent_completion_already_running(ctx)) {
            trace("create_new_completions9");
            trace("cancel completion, same is running");
            res = cancel_completion(ctx.view);
        }
        else if (!ctx.options.manual_completion()) {
            trace("create_new_completions7");
            trigger_manual_completion(ctx.view, ctx.options.copy_as_manual() );
            res = cancel_completion(ctx.view);
        }
        else if (is_after_int_iterator(ctx.src(), ctx.offset)) {
            trace("create_new_completions8");
            res = cancel_completion(ctx.view);
        }
        else if (is_iterator_completion(ctx.src(), ctx.offset)) {
            trace("create_new_completions10");
            trace("iterator completion");
            res = [Tup2.create(".\tint iterator", "..")];
        }
        else {
            trace("create_new_completions11");
            if (is_hint_completion(ctx)) {
                trace("ADD HINT");
                ctx.options.types().add_hint();
            }
        
            var is_directly_after_control_struct = ctx.complete_char_is_after_control_struct();

            var only_top_level = ctx.is_new() || is_directly_after_control_struct;


            trace("only_top_level: " + Std.string(only_top_level));
            

            if (only_top_level) {
                res = get_toplevel_completions(ctx);
            }
            else {

                var last_ctx = cache.input;

                if (use_completion_cache(ctx,last_ctx)) 
                {
                    trace("USE COMPLETION CACHE");
                    var out = cache.output;
                    update_completion_cache(cache, out);
                    project.completion_context.add_completion_result(out);
                    res = cancel_completion(view);
                    trigger_async_completion(view, ctx.options, out.show_top_level_snippets());
                    //res = combine_hints_and_comps(out)
                    //res = completion_result_with_smart_snippets(view, res, out, ctx.options)
                }
                else if (supported_compiler_completion_char(ctx.complete_char())) 
                {
                    trace("supported char");
                    var comp_build = create_completion_build(ctx);
                    if (comp_build != null) {
                        run_compiler_completion(comp_build, function (out, err) completion_finished(ctx, comp_build,  out, err));
                    }
                    else {
                        trace("couldn't create temp path && files which are neccessary for completion");
                    }
                    // we don't show any completions at this point
                    
                    res = cancel_completion(view, true);
                }
                else {
                    trace("whatever");
                    var comp_result = CompletionResult.empty_result(ctx, function () return get_toplevel_completions(ctx));
                    update_completion_cache(cache, comp_result);
                    project.completion_context.add_completion_result(comp_result);
                    res = cancel_completion(view);
                    trigger_async_completion(view, ctx.options, comp_result.show_top_level_snippets());
                    //res = combine_hints_and_comps(comp_result)
                }
            }
        }
        return res;
    }

    public static function create_completion_build (ctx:CompletionContext) {
        var tmp_src = ctx.temp_completion_src();

        var r = Temp.create_temp_path_and_file(ctx.build(), ctx.orig_file(), tmp_src);
        var temp_path = r._1, temp_file = r._2;

        var temp_creation_success = temp_path != null && temp_file != null;

       function mk_build() 
       {
            var comp_build = new CompletionBuild(ctx, temp_path, temp_file);
            var build =comp_build.build;
            var display = comp_build.display();
            var macro_completion = ctx.options.macro_completion();
            // prepare build options
            build.set_auto_completion(display, macro_completion);
            if (ctx.settings.show_completion_times(comp_build.ctx.view)) 
            {
                build.set_times();
            }
            return comp_build;
        }


        return if (temp_creation_success) mk_build() else null;
    }


    public static function run_compiler_completion(comp_build:CompletionBuild, callback) {
        
        var start_time = Time.time();
        var ctx = comp_build.ctx;
        var project = ctx.project;
        var build = comp_build.build;
        var view = ctx.view;

        var async = ctx.settings.is_async_completion();

        function in_main (out, err) {
            
            function run () {
                var run_time = Time.time() - start_time;
                trace("completion time: " + Std.string(run_time));
                Temp.remove_path(comp_build.temp_path);
                callback(out, err);
            }
                
            // because of async completion, the current completion could be 
            // out of date, because a newer completion was triggered, so run should
            // only be called if this completion is still up to date
            project.completion_context.run_if_still_up_to_date(ctx.id, run);
        }   
        function on_result(out, err) {
            Sublime.set_timeout(function () in_main(out, err), 2);
        }

        // store the data of the currently running completion operation in cache to fetch it later
        project.completion_context.set_new_completion(ctx);
        
        build.run(project, view, async, on_result);
    }

    public static function completion_finished(ctx:CompletionContext, comp_build:CompletionBuild, out:String, err:String) {
        
        var ctx = comp_build.ctx;
        var temp_file = comp_build.temp_file;
        
        var cache = comp_build.cache;

        var project = ctx.project;
        var view = ctx.view;
        

        var comp_result = output_to_result(ctx, temp_file, err, out, function () return get_toplevel_completions(ctx));

        var has_results = comp_result.has_results();
        
        if (has_results) {
            update_completion_cache(cache, comp_result);
            project.completion_context.add_completion_result(comp_result);
            var show_top_level_snippets = comp_result.show_top_level_snippets();
            trigger_async_completion(view, ctx.options, show_top_level_snippets);
        }
        else {
            trace("ignore background completion on finished")  ;
        }
    }  


    public static function hints_to_sublime_completions(hints:Array<Array<String>>) 
    {
        function make_hint_comp (h:Array<String>) 
        {
            var hint_is_only_type = h.length == 1;
            
            var res = null;
            
            if (hint_is_only_type) {
                res = Tup2.create(h[0] + " - No Completion", "${}");
            }
            else {
                var function_has_no_params = (h.length) == 2 && h[0] == "Void";
                
                var insert = null;
                var show = null;
                if (function_has_no_params) 
                {
                    insert = ")";
                    show = "Void";
                }
                else {

                    function param_escape(p:String) {
                        return p.split("}").join("\\}");
                    }

                    var last_index = h.length-1;
                    var params = h.slice(0, last_index);
                    
                    show = params.join(", ");

                    if (Settings.smart_snippets_just_current()) 
                    {
                        // insert only the snippet for the current parameter
                        var first = param_escape(params[0]);
                        
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
                        function get_snippet_index(list_index) {
                            return Std.string(list_index+1);
                        }

                        function param_snippet(param, index) {
                            return "${" + get_snippet_index(index) + ":" + param_escape(param) + "}";
                        }

                        var snippet_list = [for (index in 0...params.length) param_snippet(params[index], index)];

                        insert = snippet_list.join(",") + ")${0}";
                    }
                }
                
                res = Tup2.create(show, insert);
            }
            return res;
        }

        return [for (h in hints) make_hint_comp(h)];
    }



    public static function combine_hints_and_comps (comp_result:CompletionResult) 
    {
        var all_comps = hints_to_sublime_completions(comp_result.hints);



        if (!comp_result.ctx.options.types().has_hint() || comp_result.hints.length == 0) {
            trace("TAKE TOP LEVEL COMPS");
            all_comps.extend(comp_result.all_comps());
        }
        else {
            if (comp_result.hints.length == 1) {
                Sublime.status_message("signature: " + comp_result.hints[0].join("->"));
            }
        }
            // insert hint directly


        //if len(comp_result.hints) == 1:
        //    hxpanel.default_panel().writeln(comp_result.doc);
        return all_comps;
    }



    public static function is_iterator_completion(src:String, offset:Int) {
        var o = offset;
        var s = src;
        return o > 3 && s.charAt(o) == "\n" && s.charAt(o-1) == "." && s.charAt(o-2) == "." && s.charAt(o-3) != ".";
    }

    public static function is_after_int_iterator(src:String, offset:Int) {
        var o = offset;
        var s = src;
        return o > 3 && s.charAt(o) == "\n" && s.charAt(o-1) == "." && s.charAt(o-2) == "." && s.charAt(o-3) == ".";
    }

    public static function is_hint_completion(ctx:CompletionContext) {
        var whitespace_re = Re.compile("^\\s*$");
        return "(,".indexOf(ctx.complete_char()) > -1 && Re.match(whitespace_re, ctx.prefix) != null;
    }


    public static function is_equivalent_completion_already_running(ctx:CompletionContext) {
        return ctx.project.completion_context.is_equivalent_completion_already_running(ctx);
    }

    public static function should_include_top_level_completion(ctx:CompletionContext) 
    {
        
        trace("complete Char: '" + ctx.complete_char() + "'");
        var toplevel_complete = ":(,{;})".indexOf(ctx.complete_char()) > -1 || ctx.in_control_struct() || ctx.is_new();
        
        trace("should include: " + toplevel_complete);


        return toplevel_complete;
    }


    public static function get_toplevel_completions(ctx:CompletionContext) {
        trace("get top level completions");
        var comps = null;
        if (should_include_top_level_completion( ctx )) {
            comps = TopLevel.get_toplevel_completion_filtered( ctx );
        }
        else {
            trace("should not");
            comps = [];
        }

        return comps;
    }


    public static function create_completion_context(project:Project, view:View, offset:Int, options:CompletionOptions, prefix:String) {

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

    public static function update_completion_cache(cache:CompletionCache, comp_result:CompletionResult) {
        cache.output = comp_result;
        cache.input = comp_result.ctx;
    }


    public static function log_completion_status(status, comps, hints) {
        if (status != "") {
            if (comps.length > 0 || hints.length > 0) {
                trace(status);
            }
            else {
                Panels.default_panel().writeln( status );
            }
        }
    }


    public static function output_to_result (ctx:CompletionContext, temp_file, err, ret, retrieve_tl_comps) {
        var r = Output.get_completion_output(temp_file, ctx.orig_file(), err, ctx.commas());
        var hints = r._1, comps1 = r._2, status = r._3, errors = r._4;
        // we don't need doc here
        var comps2 = [for (t in comps1) Tup2.create(t.hint, t.insert)];
        ctx.project.completion_context.set_errors(errors);
        highlight_errors( errors, ctx.view );
        // top level completions are empty until they are really required
        return new CompletionResult(ret, comps2, status, hints, ctx, retrieve_tl_comps );
    }

    public static function use_completion_cache (last_input:CompletionContext, current_input:CompletionContext) 
    {
        return last_input.eq(current_input);
    }

    public static function supported_compiler_completion_char (char:String) {
        return "(.,".indexOf(char) > -1;
    }



    public static function highlight_errors( errors:Array<CompilerError> , view:View ):Void  {
        var regions = [];
        
        for (e in errors) {
            var l = e.line;
            var left = e.from;
            var right = e.to;
            var a = view.text_point(l,left);
            var b = view.text_point(l,right);
            regions.append( new Region(a,b));
            
            Panels.default_panel().status( "Error" , e.file + ":" + Std.string(l) + ": characters " + Std.string(left) + "-" + Std.string(right) + ": " + e.message);
        }
                
        view.add_regions("haxe-error" , regions , "invalid" , "dot" );
    }

    public static function cancel_completion(view:View, hide_complete = true):Array<Tup2<String,String>> {
        if (hide_complete) {
            // this seems to work fine, it cancels the sublime
            // triggered completion without poping up a completion
            // view
            view.run_command('hide_auto_complete');
        }
        return [Tup2.create("  ...  ", "")];
    }


    public static function trigger_async_completion(view:View, options:CompletionOptions, show_top_level_snippets = false) {

        var async_options = options.copy_as_async();
        
        function run_complete() {
            trigger_completion(view, async_options, show_top_level_snippets);
        }

        Sublime.set_timeout(run_complete, 2);
    }

    public static function trigger_manual_completion(view:View, options:CompletionOptions) 
    {

        var hint = options.types().has_hint();
        var macroComp = options.macro_completion();

        function run_complete() {
            if (hint && macroComp) 
            {
                view.run_command("haxe_hint_display_macro_completion");
            }
            else if (hint) 
            {
                view.run_command("haxe_hint_display_completion");
            }
            else if (macroComp) 
            {
                view.run_command("haxe_display_macro_completion");
            }
            else 
            {
                view.run_command("haxe_display_completion");
            }
        }

        Sublime.set_timeout(run_complete, 2);
    }
}
/*
# -*- coding: utf-8 -*-
import time
import sublime
import re

import haxe.settings as hxsettings
import haxe.panel as hxpanel
from haxe.completion.hx import toplevel
import haxe.temp as hxtemp
import haxe.project as hxproject
from haxe.completion.hx.types import CompletionOptions, CompletionSettings, CompletionContext, CompletionResult, CompletionBuild
from haxe.completion.hx import constants as hxconst
from haxe.compiler.output import get_completion_output
from haxe.log import log
from haxe.tools import viewtools
from haxe.tools import stringtools


# ------------------- FUNCTIONS ----------------------------------




*/