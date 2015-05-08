package hxsublime.commands;

import haxe.ds.StringMap;
import hxsublime.project.Projects;
import hxsublime.tools.HxSrcTools;
import hxsublime.tools.ViewTools;
import python.lib.Os;
import python.lib.os.Path;
import python.KwArgs;
import sublime.Edit;
import sublime.EventListener;
import sublime.Region;
import sublime.Sublime;
import sublime.View;
import sublime.Window;
import sublime.WindowCommand;

using StringTools;

// stores the info for file creation, this data is shared between command && listener instances.
private class State {
    public static var current_create_type_info = new StringMap();
}



@:keep class HaxeCreateTypeCommand extends WindowCommand
{
    var classpath : String;
    var win : Window;

    public function new (win:Window)
    {
        super(win);
        this.classpath = null;
        this.win = win;
    }


    override public function run( kwArgs:KwArgs<Dynamic> )
    {

        var paths = kwArgs.get("paths", []);
        var t = kwArgs.get("t", "class");


        trace("createtype");


        var view = win.active_view();

        var project = Projects.currentProject(view);

        var builds = project.builds.copy();

        if (project.hasBuild())
        {
            builds.insert(0, project.getBuild(view));
        }

        var pack = [];

        if (builds.length == 0 && view != null && view.file_name() != null)
        {
            trace(view.file_name());
            project.extractBuildArgs(view);
            builds = project.builds;
        }

        if (paths.length == 0 && view != null)
        {
            var fn = view.file_name();
            paths.push(fn);
        }

        for (path in paths)
        {

            if (Path.isfile( path ))
            {
                path = Path.dirname( path );
            }

            if (this.classpath == null)
            {
                this.classpath = path;
            }

            for (b in builds)
            {
                trace("build file: " + b.buildFile());
                var found = false;
                for (cp in b.classpaths())
                {
                    trace("class path: " + cp);
                    trace("path: " + path);
                    if (path.startsWith( cp ))
                    {

                        this.classpath = path.substring(0,cp.length);
                        trace("this.classpath: " + this.classpath);

                        var rel_path = path.substr(cp.length+1);

                        trace(rel_path);
                        if (rel_path.length == 0)
                        {
                            found = true;
                        }
                        else
                        {
                            var sub_packs = rel_path.split(Os.sep);
                            trace("subpacks:" + Std.string(sub_packs));
                            for (p in sub_packs)
                            {

                                if (p.indexOf(".") > -1)
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
                this.classpath = builds[0].classpaths()[0];
            }
        }

        trace(pack);
        // so default text ends with .

        var packSuggestion = pack.join(".");
        if (packSuggestion.length > 0) {
            packSuggestion += ".";
        }

        Sublime.status_message( "Current classpath : " + this.classpath );
        win.show_input_panel("Enter "+t+" name : " , packSuggestion , function (inp) this.onDone(inp, t) , this.onChange , this.onCancel );
    }

    public function onDone( inp:String, cur_type:String )
    {

        var fn = this.classpath;
        var parts = inp.split(".");
        var pack = [];

        var cl = null;

        while( parts.length > 0 )
        {
            var p = parts.shift();

            fn = Path.join( fn , p );

            if (hxsublime.tools.HxSrcTools.Regex.isType.match( p ) != null)
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

        var src = "\npackage " + pack.join(".") + ";\n\n"+cur_type+" "+cl+" ";
        if (cur_type == "typedef")
        {
            src += "= ";
        }
        src += "{\n\n\t\n\n}";

        State.current_create_type_info.set(fn, src);

        Sublime.active_window().open_file( fn );
    }


    public function onChange( inp:String )
    {
        //sublime.status_message( "Current classpath : " + this.classpath )
        trace( inp );
    }

    public function onCancel( )
    {
        trace("cancel");
    }
}

@:keep class HaxeCreateTypeListener extends EventListener
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
            trace(data);
            v.insert(edit,0,data);
            var sel = v.sel();
            sel.clear();
            var pt = v.text_point(5,1);
            sel.add( new Region(pt,pt) );
        }

        ViewTools.asyncEdit(view, run_edit);
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