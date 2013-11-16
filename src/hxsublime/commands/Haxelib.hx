package hxsublime.commands;


import hxsublime.Haxelib.HaxeLibLibrary;
import python.lib.Types;

import hxsublime.Haxelib.HaxeLibManager;
import hxsublime.project.Base.Projects;
import sublime.Sublime;
import sublime.WindowCommand;


@:keep class HaxeInstallLibCommand extends WindowCommand
{


    override public function run(_:KwArgs)
    {
        var view = Sublime.active_window().active_view();

        var project = Projects.current_project(view);

        if (project != null) 
        {
            var manager = project.haxelib_manager();
            var libs = manager.search_libs();
            var menu = this._prepare_menu(libs, manager);
            var on_selected = this._entry_selected.bind(libs, manager);
            trace(libs);
            this.window.show_quick_panel(menu, on_selected);
        }
    }

    public function _prepare_menu (libs:Array<String>, manager:HaxeLibManager) 
    {
        var menu = [];
        for (l in libs) {
            if (manager.is_lib_installed(l))
            {
                menu.push( [ l + " [" + manager.get_lib(l).version + "]" , "Remove" ] );
            }
            else 
            {
                menu.push( [ l , 'Install' ] );
            }
        }

        menu.push( ["Upgrade libraries", "Upgrade installed libraries"] );
        menu.push( ["Haxelib Selfupdate", "Updates Haxelib itself"] );
        
        return menu;
    }

    public function _entry_selected( libs:Array<String>, manager:HaxeLibManager, i:Int )
    {
        trace("install lib command selected " + Std.string(i));
        if (i < 0) {
            return;
        }
        if (i == libs.length) 
        {
            trace("upgrade all");
            manager.upgrade_all();
        }
            
        if (i == libs.length+1) 
        {
            trace("self update");
            manager.self_update();
        }
        else 
        {
            var lib = libs[i];
            if (manager.available().exists(lib)) 
            {
                trace("remove " + lib);
                manager.remove_lib(lib);
            }
            else 
            {
                trace("install " + lib);
                manager.install_lib(lib);
            }
        }
    }
}
/*
import sublime, sublime_plugin
import functools

from haxe import project as hxproject
from haxe.trace import trace



*/