package hxsublime.commands;

import haxe.ds.StringMap;
import hxsublime.project.Base.Projects;
import hxsublime.tools.HxSrcTools.HaxeType;
import hxsublime.tools.ViewTools;
import python.lib.Types.Tup2;
import sublime.Edit;
import sublime.EventListener;
import sublime.Region;
import sublime.Sublime;
import sublime.TextCommand;
import python.lib.Types;
import sublime.View;

private class State 
{
    public static var _find_decl_file = null;
    public static var _find_decl_pos = null;
    public static var _init_text = "";
    public static var _is_open = false;
}

@:keep class HaxeGotoBaseCommand<T> extends TextCommand
{
    var selecting_build:Bool = false;

    public function get_entries (types:StringMap<HaxeType>):Array<Array<String>>
    {
        return throw "abstract method";
    }
    public function get_data (types:StringMap<HaxeType>):Array<Tup2<String, T>>
    {
        return throw "abstract method";
    }

    public function get_file(data_entry:T):String
    {
        return throw "abstract method";
    }

    public function get_src_pos(data_entry:T):Int
    {
        return throw "abstract method";
    }

    override public function run( edit:Edit, ?kwArgs:KwArgs ) 
    {
        

        trace("run HaxeListBuildFieldsCommand");

        var view = this.view;

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

        var build = project.get_build(view);

        var bundle = build.get_types().merge(build.std_bundle);



        var bundle_types = bundle.all_types_and_enum_constructors_with_info();

        var filtered_types = new StringMap();
        
        for (k in bundle_types.keys())
        {
            var t = bundle_types.get(k);
            if (build.is_type_available(t)) 
            {
                filtered_types.set(k, t);
            }
        }


        var function_list = this.get_entries(filtered_types);
        var function_list_data = this.get_data(filtered_types);
        

        trace(Std.string(function_list));

        trace(Std.string(function_list.length));

        
        this.selecting_build = true;
        Sublime.status_message("Please select a type");
        
        var win = view.window();

        var sel = view.sel();

        if (sel.length == 1 && sel[0].begin() != sel[0].end()) 
        {
            State._init_text = ViewTools.getContent(view).substring(sel[0].begin(), sel[0].end());
        }
        else if (sel.length == 1)
        {
            var reg = view.word(sel[0].begin());
            State._init_text = ViewTools.getContent(view).substring(reg.begin(), reg.end());
        }
        else
        {
            State._init_text = "";
        }
        
        function on_selected (i:Int)
        {
            
            State._is_open = false;
            State._init_text = "";
            if (i >= 0)
            {
                var selected_type = function_list_data[i];
                trace("selected field: " + Std.string(selected_type._1));
                
                var src_pos = this.get_src_pos(selected_type._2);

                var goto_file = this.get_file(selected_type._2);

                State._find_decl_file = goto_file;

                trace("find_decl_file: " + Std.string(State._find_decl_file));
                if (src_pos != null)
                {
                    State._find_decl_pos = src_pos;
                    trace("src_pos" + Std.string(src_pos) );
                }
                else
                {
                    State._find_decl_pos = 0;
                }


                function show()
                {
                    win.open_file(goto_file);
                }

                Sublime.set_timeout(show, 130);
            }
        }
        State._is_open = true;    
        win.show_quick_panel( function_list , on_selected  , Sublime.MONOSPACE_FONT );
    }


}


@:keep class HaxeGotoBaseListener extends EventListener
{

    override public function on_activated(view:View)
    {
        
        
        // global _find_decl_pos, _find_decl_file, _is_open, _init_text
        var find_pos = State._find_decl_pos;
        var find_file = State._find_decl_file;
        trace("HaxeGotoBaseListener::on_activated");
        
        
        trace(Std.string(view));

        
        if (view != null && State._is_open)
        {
            State._is_open = false;

            ViewTools.insertAtCursor(view, State._init_text);
            State._init_text = "";
        }
                        

        if (view != null && view.file_name() != null)
        {
            trace("show at X");
            trace("decl file: " + Std.string(find_file));
            if (view.file_name() == find_file)
            {
                trace("show at Y");
                view.sel().clear();

                var min = find_pos;

                view.sel().add(new Region(min));

                trace("show at:" + Std.string(min));
                // move to line is delayed, seems to work better
                // without delay the animation to the region does not work properly sometimes
                function show ()
                {
                    trace("show at:" + Std.string(min));
                    view.show_at_center(new Region(min));
                }
                Sublime.set_timeout(show, 100);
                State._find_decl_file = null;
                State._find_decl_pos = null;
            }
        }
    }
}
/*

import sublime_plugin
import sublime

from haxe.trace import trace;
from haxe import project as hxproject

from haxe.tools import viewtools

#shared between FindDelaration Command && Listener



        
*/