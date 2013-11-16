package hxsublime.commands;

import hxsublime.project.Base.Projects;
import hxsublime.Settings;
import hxsublime.tools.ViewTools;
import python.lib.Types.KwArgs;
import sublime.Edit;
import sublime.EventListener;
import sublime.TextCommand;
import sublime.View;

using StringTools;


@:keep class HaxeSaveAllAndRunCommand extends TextCommand
{
    override public function run ( edit:Edit, ?args:KwArgs ) 
    {
        
        trace("run HaxeSaveAllAndRunCommand");
        var view = this.view;
        view.window().run_command("save_all");
        Projects.current_project(this.view).run_build( view );
    }
}

@:keep class HaxeSaveAllAndCheckCommand extends TextCommand
{
    override public function run ( edit:Edit, ?args:KwArgs ) 
    {
        var edit:Edit = args.get("edit", null);
        trace("run HaxeSaveAllAndCheckCommand");
        var view = this.view;
        view.window().run_command("save_all");
        Projects.current_project(this.view).check_build( view );
    }
}

@:keep class HaxeSaveAllAndBuildCommand extends TextCommand
{
    override public function run ( edit:Edit, ?args:KwArgs ) 
    {
        trace("run HaxeSaveAllAndBuildCommand");
        var view = this.view;
        view.window().run_command("save_all");
        Projects.current_project(this.view).just_build( view );
    }
}

@:keep class HaxeRunBuildCommand extends TextCommand
{
    override public function run ( edit:Edit, ?args:KwArgs ) 
    {
        var view = this.view;
        trace("run HaxeRunBuildCommand");
        var project = Projects.current_project(this.view);

        if (project.has_build()) 
        {
            project.run_build( view );
        }
        else 
        {
            trace("no builds selected");
            project.extract_build_args(view, true);
        }
    }
}

@:keep class HaxeSelectBuildCommand extends TextCommand
{
    override public function run ( edit:Edit, ?args:KwArgs ) 
    {
        trace("run HaxeSelectBuildCommand");
        var view = this.view;
        Projects.current_project(this.view).select_build( view );
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
                if (Settings.check_on_save()) 
                {
                    var project = Projects.current_project(view);
                
                    if (project.has_build())
                    {
                        project.check_build( view );
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