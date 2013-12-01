package hxsublime.commands;

import hxsublime.project.Projects;
import python.lib.Types.KwArgs;
import sublime.Sublime;
import sublime.WindowCommand;


@:keep class HaxeRestartServerCommand extends WindowCommand 
{

    public override function run(kwArgs:KwArgs) 
    { 
        trace("run HaxeRestartServerCommand");
        
        var view = Sublime.active_window().active_view();
        
        var project = Projects.currentProject(view);

        project.restartServer( view );
    }
}
