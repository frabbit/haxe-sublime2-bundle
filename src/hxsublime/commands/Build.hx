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
        var edit:Edit = args.get("edit", null);
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
        trace("run HaxeSelectBuildCommand");
        var view = this.view;
        Projects.currentProject(this.view).selectBuild( view );
    }
}

@:keep class HaxeBuildOnSaveListener extends EventListener {
    override public function on_post_save(view:View)
    {
        trace("on_post_save");
        if (view != null && view.file_name() != null)
        {
            if (ViewTools.isSupported(view) || view.file_name().endsWith(".erazor.html"))
            {
                if (Settings.checkOnSave())
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
}

/*
import sublime, sublime_plugin
from haxe.tools import viewtools
from haxe import project as hxproject
from haxe import settings
from haxe.trace import trace;


*/