package hxsublime.commands;


import hxsublime.Haxelib.HaxeLibLibrary;
import python.lib.Types;

import hxsublime.Haxelib.HaxeLibManager;
import hxsublime.project.Projects;
import sublime.Sublime;
import sublime.WindowCommand;


@:keep class HaxeInstallLibCommand extends WindowCommand
{


    override public function run(_:KwArgs)
    {
        var view = Sublime.active_window().active_view();

        var project = Projects.currentProject(view);

        if (project != null) 
        {
            var manager = project.haxelibManager();
            var libs = manager.searchLibs();
            var menu = this.createMenuItems(libs, manager);
            
            this.window.show_quick_panel(menu, onEntrySelected.bind(libs, manager));
        }
    }

    function createMenuItems (libs:Array<String>, manager:HaxeLibManager) 
    {
        var menu = [];
        for (l in libs) 
        {
            if (manager.isLibInstalled(l))
            {
                menu.push( [ l + " [" + manager.getLib(l).version + "]" , "Remove" ] );
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

    function onEntrySelected( libs:Array<String>, manager:HaxeLibManager, i:Int )
    {
        trace("install lib command selected " + Std.string(i));
        if (i < 0) {
            return;
        }
        if (i == libs.length) 
        {
            trace("upgrade all");
            manager.upgradeAll();
        }
            
        if (i == libs.length+1) 
        {
            trace("self update");
            manager.selfUpdate();
        }
        else 
        {
            var lib = libs[i];
            if (manager.available().exists(lib)) 
            {
                trace("remove " + lib);
                manager.removeLib(lib);
            }
            else 
            {
                trace("install " + lib);
                manager.installLib(lib);
            }
        }
    }
}
