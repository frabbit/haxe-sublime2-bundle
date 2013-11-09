package hxsublime.completion.hx;

import hxsublime.completion.hx.Types.CompletionContext;
import hxsublime.completion.hx.Types.CompletionResult;

class Base {
    public static function trigger_completion (view, options, show_top_level_snippets = false) {

        trace("show_top_level_snippets: " + Std.string(show_top_level_snippets))
        public static function run() {
            project = hxproject.current_project(view)
            
            if (!project.has_build()) {
                project.extract_build_args(view, false)
            }

            if project.has_build() {
                project.completion_context.set_trigger(view, options)
                
                view.run_command( "auto_complete" , {
                    "api_completions_only" : !show_top_level_snippets,
                    "disable_auto_insert" : true,
                    "next_completion_if_showing" : true,
                    'auto_complete_commit_on_tab': true
                } )
            }
            else {
                project.extract_build_args(view, true)
            }
        }

        view.run_command('hide_auto_complete')

        sublime.set_timeout(run, 0)
    }

    public static function get_available_async_completions(comp_result, view) {

        ctx = comp_result.ctx

        has_results = comp_result.has_results()

        discard_results = !has_results && ctx.options.types.has_hint()

        return cancel_completion(view) if discard_results else combine_hints_and_comps(comp_result)
    }


    public static function completion_result_with_smart_snippets (view, comps, result, options) {

        use_snippets = hxsettings.smart_snippets(view)
        prefix_is_whitespace = stringtools.is_whitespace_or_empty(result.ctx.prefix)
        has_one_hint = options.types.has_hint() && len(result.hints) == 1
        same_cursor_pos = viewtools.get_first_cursor_pos(view) == result.ctx.view_pos
        
        
        // we don't want to insert the snippet if there is already an argument
        // in that case only the hint should be shown
        line_after_offset = result.ctx.line_after_offset.strip();
        really_insert = len(line_after_offset) == 0 || line_after_offset[0] in "),";
      
        if (really_insert && prefix_is_whitespace && use_snippets && has_one_hint && same_cursor_pos) {
            only_hint = comps[0];
            viewtools.insert_snippet(view, only_hint[1]);
            comps = cancel_completion(view);
        }
        return comps;
    }

    public static function auto_complete(project, view, offset, prefix) {

        // if completion is triggered by a background completion process
        // completion return the result

        options = project.completion_context.get_and_delete_trigger(view)

        if (options != null && options.async_trigger) {
            async_result = project.completion_context.get_and_delete_async(view)
            use_async_results = async_result != null && async_result.has_results()
            if (use_async_results) {
                res = get_available_async_completions(async_result, view)
                res = completion_result_with_smart_snippets(view, res, async_result, options)

            }
                
            else {
                res = cancel_completion(view)
            }
        }
        else {
            res = create_new_completions(project, view, offset, options, prefix)
        }
        return res
    }


    public static function create_new_completions(project, view, offset, options, prefix) {

        cache = project.completion_context.current

        trace("------- COMPLETION START -----------")

        ctx = create_completion_context(project, view, offset, options, prefix)

        res = null
        
        trace("MANUAL COMPLETION: " + Std.string(ctx.options.manual_completion))

        // autocompletion is triggered, but its already 
        // running as a background process, starting it
        // again would result in multiple queries for
        // the same view && src position
        if (is_equivalent_completion_already_running(ctx)) {
            trace("cancel completion, same is running")
            res = cancel_completion(ctx.view)
        }
        else if (!ctx.options.manual_completion) {
            trigger_manual_completion(ctx.view, ctx.options.copy_as_manual() )
            res = cancel_completion(ctx.view)
        }
        else if (is_after_int_iterator(ctx.src, ctx.offset)) {
            res = cancel_completion(ctx.view)
        }
        else if (is_iterator_completion(ctx.src, ctx.offset)) {
            trace("iterator completion")
            res = [(".\tint iterator", "..")]
        }
        else {

            if (is_hint_completion(ctx)) {
                trace("ADD HINT")
                ctx.options.types.add_hint()
            }
        
            is_directly_after_control_struct = ctx.complete_char_is_after_control_struct

            only_top_level = ctx.is_new || is_directly_after_control_struct


            trace("only_top_level: " + Std.string(only_top_level))
            

            if (only_top_level) {
                res = get_toplevel_completions(ctx)
            }
            else {

                last_ctx = cache["input"]

                if use_completion_cache(ctx,last_ctx) :
                    trace("USE COMPLETION CACHE")
                    out = cache["output"]
                    update_completion_cache(cache, out)
                    project.completion_context.add_completion_result(out)
                    res = cancel_completion(view)
                    trigger_async_completion(view, ctx.options, out.show_top_level_snippets())
                    //res = combine_hints_and_comps(out)
                    //res = completion_result_with_smart_snippets(view, res, out, ctx.options)
                else if (supported_compiler_completion_char(ctx.complete_char)) {
                    
                    comp_build = create_completion_build(ctx)
                    if (comp_build != null) {
                        run_compiler_completion(comp_build, lambda out, err: completion_finished(ctx, comp_build,  out, err))
                    }
                    else {
                        trace("couldn't create temp path && files which are neccessary for completion")
                    }
                    // we don't show any completions at this point
                    
                    res = cancel_completion(view, true)
                }
                else {

                    comp_result = CompletionResult.empty_result(ctx, lambda:get_toplevel_completions(ctx))
                    update_completion_cache(cache, comp_result)
                    project.completion_context.add_completion_result(comp_result)
                    res = cancel_completion(view)
                    trigger_async_completion(view, ctx.options, comp_result.show_top_level_snippets())
                    //res = combine_hints_and_comps(comp_result)
                }
            }
        }
        return res
    }

    public static function create_completion_build (ctx) {
        tmp_src = ctx.temp_completion_src

        temp_path, temp_file = hxtemp.create_temp_path_and_file(ctx.build, ctx.orig_file, tmp_src)

        temp_creation_success = temp_path != null && temp_file != null

        public static function mk_build() {
            comp_build = CompletionBuild(ctx, temp_path, temp_file)
            build =comp_build.build
            display = comp_build.display
            macro_completion = ctx.options.macro_completion
            // prepare build options
            build.set_auto_completion(display, macro_completion)
            if (ctx.settings.show_completion_times(comp_build.ctx.view)) {
                build.set_times()
            }
            return comp_build
        }


        return mk_build() if temp_creation_success else null
    }


    public static function run_compiler_completion(comp_build, callback) {
        
        start_time = time.time()
        ctx = comp_build.ctx
        project = ctx.project
        build = comp_build.build
        view = ctx.view

        async = ctx.settings.is_async_completion

        function in_main (out, err) {
            
            function run () {
                run_time = time.time() - start_time;
                trace("completion time: " + Std.string(run_time))
                hxtemp.remove_path(comp_build.temp_path)
                callback(out, err)
            }
                
            // because of async completion, the current completion could be 
            // out of date, because a newer completion was triggered, so run should
            // only be called if this completion is still up to date
            project.completion_context.run_if_still_up_to_date(ctx.id, run)
        }   
        function on_result(out, err) {
            sublime.set_timeout(function () in_main(out, err), 2)
        }

        // store the data of the currently running completion operation in cache to fetch it later
        project.completion_context.set_new_completion(ctx);
        
        build.run(project, view, async, on_result)
    }

    public static function completion_finished(ctx, comp_build, out, err) {
        
        ctx = comp_build.ctx
        temp_file = comp_build.temp_file
        
        cache = comp_build.cache

        project = ctx.project
        view = ctx.view
        

        comp_result = output_to_result(ctx, temp_file, err, out, lambda:get_toplevel_completions(ctx))

        has_results = comp_result.has_results()
        
        if (has_results) {
            update_completion_cache(cache, comp_result)
            project.completion_context.add_completion_result(comp_result)
            show_top_level_snippets = comp_result.show_top_level_snippets()
            trigger_async_completion(view, ctx.options, show_top_level_snippets)
        }
        else {
            trace("ignore background completion on finished")  
        }
    }  


    public static function hints_to_sublime_completions(hints) {
        public static function make_hint_comp (h) {
            hint_is_only_type = len(h) == 1
            
            res = null
            
            if (hint_is_only_type) {
                res = (h[0] + " - No Completion", "${}")
            }
            else {
                function_has_no_params = (len(h)) == 2 && h[0] == "Void"
                
                if (function_has_no_params) {
                    insert = ")"
                    show = "Void"
                }
                else {

                    function param_escape(p) {
                        return "\\}".join(p.split("}"));
                    }

                    last_index = len(h)-1
                    params = h[0:last_index];
                    
                    show = ", ".join(params)

                    if (hxsettings.smart_snippets_just_current()) {
                        // insert only the snippet for the current parameter
                        first = param_escape(params[0])
                        
                        if len(params) == 1:
                            insert = "${1:" + first + "})${0}"
                        else:
                            insert = "${0:" + first + "}"
                    }
                    else {
                        // the last param gets index 0, which is the exit mark for snippets
                        function get_snippet_index(list_index) {
                            return Std.string(list_index+1)

                        function param_snippet(param, index) {
                            return "${" + get_snippet_index(index) + ":" + param_escape(param) + "}"

                        snippet_list = [param_snippet(param, index) for index, param in enumerate(params)]

                        insert = ",".join(snippet_list) + ")${0}"
                    }
                }
                
                res = (show, insert)
            }
            return res

        return [make_hint_comp(h) for h in hints]
    }



    public static function combine_hints_and_comps (comp_result:CompletionResult) {
        all_comps = hints_to_sublime_completions(comp_result.hints)



        if (!comp_result.ctx.options.types.has_hint() || len(comp_result.hints) == 0) {
            trace("TAKE TOP LEVEL COMPS");
            all_comps.extend(comp_result.all_comps());
        }
        else {
            if (len(comp_result.hints) == 1) {
                sublime.status_message("signature: " + "->".join(comp_result.hints[0]));
            }
        }
            // insert hint directly


        //if len(comp_result.hints) == 1:
        //    hxpanel.default_panel().writeln(comp_result.doc);
        return all_comps
    }



    public static function is_iterator_completion(src:String, offset:Int) {
        var o = offset;
        var s = src;
        return o > 3 && s.charAt(o) == "\n" && s.charAt(o-1) == "." && s.charAt(o-2) == "." && s.charAt(o-3) != ".";
    }

    public static function is_after_int_iterator(src:String, offset:Int) {
        o = offset
        s = src
        return o > 3 && s[o] == "\n" && s[o-1] == "." && s[o-2] == "." && s[o-3] == "."
    }

    public static function is_hint_completion(ctx:CompletionContext) {
        var whitespace_re = Re.compile("^\\s*$");
        return ctx.complete_char in "(," && (
            re.match(whitespace_re, ctx.prefix)
            )
    }


    public static function is_equivalent_completion_already_running(ctx:CompletionContext) {
        return ctx.project.completion_context.is_equivalent_completion_already_running(ctx)
    }

    public static function should_include_top_level_completion(ctx:CompletionContext) {
        
        toplevel_complete = ctx.complete_char in ":(,{;})" || ctx.in_control_struct || ctx.is_new
        



        return toplevel_complete
    }


    public static function get_toplevel_completions(ctx:CompletionContext) {
        var comps = null;
        if (should_include_top_level_completion( ctx )) {
            comps = TopLevel.get_toplevel_completion_filtered( ctx );
        }
        else {
            comps = [];
        }
        return comps;
    }


    public static function create_completion_context(project, view, offset, options, prefix) {

        // if options are null, it's a completion progress initialized by sublime, 
        // !by the user or by key trigger

        trace("OPTIONS:" + Std.string(options))

        if (options == null) {
            options = CompletionOptions(hxconst.COMPLETION_TRIGGER_AUTO)
        }
            
        
        var settings = new CompletionSettings(hxsettings);
        var ctx = new CompletionContext(view, project, offset, options, settings, prefix);
        return ctx;
    }

    public static function update_completion_cache(cache, comp_result) {
        cache["output"] = comp_result;
        cache["input"] = comp_result.ctx;
    }


    public static function log_completion_status(status, comps, hints) {
        if (status != "") {
            if (comps.length > 0 || hints.length > 0) {
                trace(status);
            }
            else {
                hxpanel.default_panel().writeln( status );
            }
        }
    }


    public static function output_to_result (ctx:CompletionContext, temp_file, err, ret, retrieve_tl_comps) {
        hints, comps1, status, errors = get_completion_output(temp_file, ctx.orig_file, err, ctx.commas)
        // we don't need doc here
        comps1 = [for (t in comps1) Tup2.create(t.hint, t.insert)];
        ctx.project.completion_context.set_errors(errors)
        highlight_errors( errors, ctx.view )
        // top level completions are empty until they are really required
        return CompletionResult(ret, comps1, status, hints, ctx, retrieve_tl_comps )
    }

    public static function use_completion_cache (last_input:CompletionContext, current_input:CompletionContext) {
        return last_input.eq(current_input)
    }

    public static function supported_compiler_completion_char (char:String) {
        return "(.,".indexOf(char) > -1;
    }

    

    public static function highlight_errors( errors , view:View ):Void  {
        regions = []
        
        for (e in errors) {
            l = e["line"]
            left = e["from"]
            right = e["to"]
            a = view.text_point(l,left)
            b = view.text_point(l,right)
            regions.append( sublime.Region(a,b))
            
            hxpanel.default_panel().status( "Error" , e["file"] + ":" + Std.string(l) + ": characters " + Std.string(left) + "-" + Std.string(right) + ": " + e["message"])
        }
                
        view.add_regions("haxe-error" , regions , "invalid" , "dot" )
    }

    public static function cancel_completion(view, hide_complete = true):Array<Tup2<String,String>> {
        if (hide_complete) {
            // this seems to work fine, it cancels the sublime
            // triggered completion without poping up a completion
            // view
            view.run_command('hide_auto_complete')
        }
        return [Tup2.create("  ...  ", "")];
    }


    public static function trigger_async_completion(view, options, show_top_level_snippets = false) {

        var async_options = options.copy_as_async();
        
        function run_complete() {
            trigger_completion(view, async_options, show_top_level_snippets);
        }

        Sublime.set_timeout(run_complete, 2);
    }

    public static function trigger_manual_completion(view, options) 
    {

        hint = options.types.has_hint()
        macroComp = options.macro_completion

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