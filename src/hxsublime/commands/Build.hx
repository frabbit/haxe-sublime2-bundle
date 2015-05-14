package hxsublime.commands;

import hxsublime.project.Projects;
import hxsublime.Settings;
import hxsublime.tools.ViewTools;
import python.KwArgs;
import sublime.Edit;
import sublime.EventListener;
import sublime.TextCommand;
import sublime.View;

using StringTools;


@:keep class HaxeSaveAllAndRunCommand extends TextCommand
{
    override public function run ( edit:Edit, ?args:KwArgs<Dynamic> )
    {
        trace("run HaxeSaveAllAndRunCommand");
        var view = this.view;
        view.window().run_command("save_all");
        Projects.currentProject(this.view).runBuild( view );
    }
}

@:keep class HaxeSaveAllAndCheckCommand extends TextCommand
{
    override public function run ( edit:Edit, ?args:KwArgs<Dynamic> )
    {
        trace("run HaxeSaveAllAndCheckCommand");
        var view = this.view;
        view.window().run_command("save_all");
        Projects.currentProject(this.view).checkBuild( view );
    }
}

@:keep class HaxeSaveAllAndBuildCommand extends TextCommand
{
    override public function run ( edit:Edit, ?args:KwArgs<Dynamic> )
    {   
        trace("run HaxeSaveAllAndBuildCommand");
        var view = this.view;
        view.window().run_command("save_all");
        Projects.currentProject(this.view).justBuild( view );
    }
}

@:keep class HaxeRunBuildCommand extends TextCommand
{
    override public function run ( edit:Edit, ?args:KwArgs<Dynamic> )
    {
        var view = this.view;
        trace("run HaxeRunBuildCommand");
        var project = Projects.currentProject(this.view);

        if (project.hasBuild())
        {
            project.runBuild( view );
        }
        else
        {
            trace("no builds selected");
            project.extractBuildArgs(view, true);
        }
    }
}

@:keep class HaxeSelectBuildCommand extends TextCommand
{
    override public function run ( edit:Edit, ?args:KwArgs<Dynamic> )
    {
        Projects.currentProject(view).selectBuild( view );
    }
}

@:keep class HaxeBuildOnSaveListener extends EventListener 
{
    override public function on_post_save(view:View)
    {
        var validView = view != null && view.file_name() != null;
        if (validView)
        {
            var supportedView = ViewTools.isSupported(view) || view.file_name().endsWith(".erazor.html");

            if (supportedView && Settings.checkOnSave())
            {
                var project = Projects.currentProject(view);

                if (project.hasBuild())
                {
                    project.checkBuild( view );
                }
                
            }
        }
    }
}
