package hxsublime.commands;

import hxsublime.project.Base.Projects;
import python.lib.Os;
import sublime.Edit;
import sublime.Region;
import sublime.View;
import sublime.Window;

// stores the info for file creation, this data is shared between command && listener instances.
private class State {
    public static var current_create_type_info = new StringMap();
}



class HaxeCreateTypeCommand extends WindowCommand 
{
    var classpath : String;
    var win : Window;

    public function new (win:Window)
    {
        this.classpath = null;
        this.win = win;
    }


    public function run( paths = [] , t = "class" ) 
    {
        trace("createtype");
        
        var win = this.win;
        var view = win.active_view();

        var project = Projects.current_project(view);

        var builds = project.builds.copy();

        if (project.has_build())
        {
            builds.insert(0, project.get_build(view))
        }

        var pack = [];
        
        if (builds.length == 0 && view != null && view.file_name() != null)
        {
            trace(view.file_name());
            project.extract_build_args(view);
            builds = project.builds;
        }

        if (paths.length == 0 && view != null)
        {
            fn = view.file_name();
            paths.push(fn);
        }

        for (path in paths)
        {

            if (os.path.isfile( path ))
            {
                path = os.path.dirname( path );
            }

            if (this.classpath == null)
            {
                this.classpath = path;
            }

            for (b in builds)
            {
                trace("build file: " + b.build_file);
                var found = false;
                for (cp in b.classpaths)
                {
                    trace("class path: " + cp);
                    trace("path: " + path);
                    if (path.startswith( cp )) 
                    {
                        
                        this.classpath = path.substring(0,cp.length);
                        trace("this.classpath: " + this.classpath);
                        
                        var rel_path = path.substr(cp.length);
                        
                        if (rel_path.length == 0)
                        {
                            found = true;
                        }
                        else
                        {
                            sub_packs = rel_path.split(Os.sep)
                            trace("subpacks:" + Std.string(sub_packs))
                            for (p in sub_packs) 
                            {
                                if ("." in p)
                                { 
                                    break;
                                }
                                else if (p != null) {
                                    pack.push(p);
                                   
                                    found = true;
                                }
                            }
                        }
                    }
     
                    if (found) 
                    {
                        break;
                    }
                }
                if (found) 
                {
                    break;
                }
                trace("found: " + Std.string(found));
            }
        }
        if (this.classpath == null)
        {
            if (builds.length > 0)
            {
                this.classpath = builds[0].classpaths[0];
            }
        }

        // so default text ends with .
        if (pack.length > 0) 
        {
            pack.push("");
        }

        sublime.status_message( "Current classpath : " + this.classpath );
        win.show_input_panel("Enter "+t+" name : " , ".".join(pack) , function (inp) this.on_done(inp, t) , this.on_change , this.on_cancel );
    }

    public function on_done( inp:String, cur_type:String ) 
    {

        var fn = this.classpath;
        var parts = inp.split(".");
        var pack = [];

        while( parts.length > 0 )
        {
            p = parts.shift();
            
            fn = Path.join( fn , p );
            if (hxsrctools.is_type.match( p ))
            {
                cl = p;
                break;
            }
            else 
            {
                pack.push(p);
            }
        }

        if (parts.length > 0)
        {
            cl = parts[0];
        }

        fn += ".hx";

        src = "\npackage " + pack.join(".") + ";\n\n"+cur_type+" "+cl+" " 
        if (cur_type == "typedef")
        {
            src += "= ";
        }
        src += "{\n\n\t\n\n}";

        State.current_create_type_info[fn] = src;

        Sublime.active_window().open_file( fn );
    }
 

    public function on_change( inp:String ) 
    {
        //sublime.status_message( "Current classpath : " + this.classpath )
        trace( inp );
    }

    public function on_cancel( ) 
    {
        trace("cancel");
    }
}

class HaxeCreateTypeListener extends sublime_plugin.EventListener
{

    override public function on_load (view:View)
    {
        var can_create_file = view != null && view.file_name() != null && State.current_create_type_info.exists(view.file_name()) && view.size() == 0;
        
        if (can_create_file) 
        {
            this.create_file(view);
        }
    }

    public function create_file(view:View)
    {
        var data = State.current_create_type_info.get(view.file_name());
        
        function run_edit(v:View, edit:Edit)
        {
            v.insert(edit,0,data);
            v.end_edit(edit);
            var sel = v.sel();
            sel.clear();
            var pt = v.text_point(5,1);
            sel.add( new Region(pt,pt) );
        }

        viewtools.async_edit(view, run_edit);
    }
}

/*
import sublime, sublime_plugin
import os
import sublime_plugin

from haxe.tools import viewtools

from haxe import project as hxproject
from haxe.tools import hxsrctools

from haxe.trace import trace

# TODO Cleanup this module



*/