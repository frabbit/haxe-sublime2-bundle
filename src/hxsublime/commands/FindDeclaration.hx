package hxsublime.commands;

import hxsublime.build.Build;
import hxsublime.panel.Base.Panels;
import hxsublime.Plugin;
import hxsublime.project.Base.Projects;
import hxsublime.project.Project;
import hxsublime.Temp;
import hxsublime.tools.HxSrcTools;
import hxsublime.tools.PathTools;
import hxsublime.tools.ViewTools;
import python.lib.Codecs;
import python.lib.Json;
import python.lib.os.Path;
import python.lib.Re;
import sublime.Edit;
import sublime.EventListener;
import sublime.Region;
import sublime.Sublime;
import sublime.TextCommand;
import sublime.View;
import python.lib.Types;

import hxsublime.tools.HxSrcTools.Regex in HxRegex;

using python.lib.StringTools;

@:keep class HaxeFindDeclarationCommand extends TextCommand 
{
    override public function run( edit:Edit, ?_:KwArgs ) 
    {

        this.run1(true);
    }

    public function helper_method()
    {
        return "hxsublime.FindDeclaration.__sublimeFindDecl";
    }


    public function run1 (use_display:Bool, order:Int = 1)
    {
        trace("run HaxeFindDeclarationCommand");
        var view = this.view;

        var file_name = view.file_name();

        if (file_name == null)
        {
            return;
        }

        var project = Projects.current_project(view);
        

        if (!project.has_build())
        {
            project.extract_build_args(view, false);
        }

        if (!project.has_build())
        {
            project.extract_build_args(view, true);
            return;
        }



        var helper_method = this.helper_method();
        
        var src = ViewTools.getContent(view);

        var file_name = Path.basename(view.file_name());

        var package_match = Re.match(HxRegex.package_line, src);

        var using_pos = if (package_match == null) 0 else package_match.end(0);

        var using_insert = "using hxsublime.FindDeclaration;";

        var src_before_using = src.substring(0, using_pos);
        var src_after_using = src.substr(using_pos);

        
        var sel = view.sel()[0];
        var pos = sel.begin();

        var expr_end = null;
        var expr_start = null;

        if (sel.end() == pos) 
        {

            var r = Helper.get_word_at(view, src, pos);
            var word_str = r._1, word_start = r._2, word_end = r._3;

            var chars = ["{", "+", "-", "(", "[", "*", "/", "=", ";", ":"];
            var res = HxSrcTools.reverse_search_next_char_on_same_nesting_level(src, chars, word_end-1);
            
            res = HxSrcTools.skip_whitespace_or_comments(src, res._1+1);



            expr_end = word_end;
            expr_start = res._1;
        }
        else 
        {
            expr_start = pos;
            expr_end = sel.end();
        }
        
        var src_before_expr = src.substring(using_pos,expr_start);

        var src_after_expr = src.substr(expr_end);

        var expr_string = src.substring(expr_start,expr_end);


        var display_str = if (use_display) ".|" else "";

        var insert_before = helper_method + "(";


        var order_str = Std.string(order);
        var insert_after = ", " + order_str + ")" + display_str;


        var new_src = src_before_using + using_insert + src_before_expr + insert_before +  expr_string + insert_after + src_after_expr;
        
        trace(new_src);

       var r = Helper.prepare_build(view, project, use_display, new_src);
        var build = r._1, temp_path = r._2, temp_file = r._3;

        function cb (out:String, err:String)
        {
            Temp.remove_path(temp_path);

            var file_pos = Re.compile("\\|\\|\\|\\|\\|([^|]+)\\|\\|\\|\\|\\|", Re.I);

            var res = Re.search(file_pos, out);
            if (res != null) 
            {
                //we've got a proper response
                var json_str = res.group(1);
                var json_res = Json.loads(json_str);

                if (json_res.hasKey("error")) 
                {
                    var error = json_res.get("error", null);
                    trace("nothing found (1), cannot find declaration");
                    if (order == 1 && use_display)
                    {
                        this.run1(true, 2);   
                    }
                    else if (order == 2 && use_display)
                    {
                        this.run1(true, 3);
                    }
                }    
                else
                {
                    this.handle_successfull_result(view, json_res, using_insert, insert_before, insert_after, expr_end, build, temp_path, temp_file);
                }
            }
            else
            {
                if (order == 1 && use_display)
                {
                    this.run1(true, 2);
                }
                else if (order == 2 && use_display) 
                {
                    this.run1(true, 3);
                }
                else if (use_display)
                {
                    trace("nothing found yet (2), try again without display (workaround)");
                    this.run1(false);
                }
                else 
                {
                    Panels.default_panel().writeln("Cannot find declaration for expression " + expr_string.strip());
                    trace("nothing found (3), cannot find declaration");
                }
            }
        }

        build.run(project, view, false, cb);
    }

    public function handle_successfull_result(view:View, json_res:Dict<String, Dynamic>, using_insert:String, insert_before:String, insert_after:String, expr_end:Int, build:Build, temp_path:String, temp_file:String)
    {
        var file = json_res.get("file", null);
        var min = json_res.get("min", 0);
        var max = json_res.get("max", 0);

        // abs_path = abs_path.replace(build.get_relative_path(temp_file), build.get_relative_path(view.file_name())
        
        var abs_path = PathTools.joinNorm(build.get_build_folder(), file);
        var abs_path_temp = PathTools.joinNorm(build.get_build_folder(), build.get_relative_path(Path.join(temp_path, temp_file)));


        if (abs_path == temp_file)
        {
            if (min > expr_end)
            {
                min -= insert_after.length;
                min -= insert_before.length;
            }
            min -= using_insert.length;
            // we have manually stored a temp file with only \n line endings
            // so we don't have to adjust the real file position and the sublime
            // text position
        }
        else 
        {
            var f = Codecs.open(abs_path, "r", "utf-8");
            var real_source = f.read();
            f.close();
            // line endings could be \r\n, but sublime text has only \n after
            // opening a file, so we have to calculate the offset betweet the
            // returned position and the real position by counting all \r before min
            // should be moved to a utility function
            var offset = 0;
            for (i in 0...min) 
            {
                if (real_source.charAt(i) == "\r") 
                {
                    offset += 1;
                }
            }
            trace("offset: " + Std.string(offset));

            min -= offset;
        }

        if (abs_path == temp_file)
        {
            // file is active view
            //abs_path = view.file_name();
            var target_view = view;


            trace("line ending: " + Std.string(view.settings().get("line_ending")));

            target_view.sel().clear();
            target_view.sel().add(new Region(min));

            target_view.show(new Region(min));
        }
        else 
        {
            //global find_decl_pos, find_decl_file
            State.find_decl_file = abs_path;
            State.find_decl_pos = min;
            // open file and listen => HaxeFindDeclarationListener
            view.window().open_file(abs_path);
        }
    }
}
//shared between FindDelaration Command and Listener
private class State 
{
    public static var find_decl_file:Null<String> = null;
    public static var find_decl_pos:Null<Int> = null;
}

private class Helper 
{


    static var plugin_path = Plugin.plugin_base_dir();
    public static function get_word_at(view:View, src:String, pos:Int)
    {
        var word = view.word(pos);

        var word_start = word.a;
        var word_end = word.b;

        var word_str = src.substring(word_start,word_end);

        return Tup3.create(word_str, word_start, word_end);
    }

    public static function prepare_build(view:View, project:Project, use_display:Bool, new_src:String)
    {
        var build = project.get_build(view).copy();
        build.add_arg(Tup2.create("-D", "no-inline"));

        var r = Temp.create_temp_path_and_file(build, view.file_name(), new_src);
        var temp_path = r._1, temp_file = r._2;

        build.add_classpath(temp_path);

        build.add_classpath(Path.join(plugin_path, "haxetools"));
        

        trace(build.classpaths);

        build.add_arg(Tup2.create("-dce", "no"));

        if (use_display)
        {
            build.set_auto_completion(temp_file + "@0", false);
        }

        return Tup3.create(build, temp_path, temp_file);
    }
}

@:keep class HaxeFindDeclarationListener extends EventListener
{
    override public function on_activated(view:View) 
    {
        //global find_decl_pos, find_decl_file
        if (view != null && view.file_name() != null) 
        {
            if (view.file_name() == State.find_decl_file)
            {
                view.sel().clear();

                var min = State.find_decl_pos;

                view.sel().add(new Region(min));
                // move to line is delayed, seems to work better
                // without delay the animation to the region does not work properly sometimes
                function show () 
                {
                    view.show_at_center(new Region(min));
                }
                Sublime.set_timeout(show, 70);
            }
            State.find_decl_file = null;
            State.find_decl_pos = null;
        }
    }
}


/*
import sublime, sublime_plugin
import os
import re
import json
import codecs


from haxe import temp as hxtemp
from haxe import project as hxproject

from haxe.plugin import plugin_base_dir

from haxe.tools import viewtools
from haxe.tools import pathtools
from haxe.tools import 

tools

from haxe import panel

from haxe.trace import trace



# TODO cleanup this module





*/