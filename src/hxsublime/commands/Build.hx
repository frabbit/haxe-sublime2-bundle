package hxsublime.commands;

import hxsublime.project.Base.Projects;
import sublime.Edit;
import sublime.EventListener;
import sublime.TextCommand;



class HaxeSaveAllAndRunCommand extends TextCommand
{
    override public function run ( args:KwArgs ) 
    {
        var edit:Edit = args.get("edit");
        trace("run HaxeSaveAllAndBuildCommand");
        var view = self.view;
        view.window().run_command("save_all");
        Projects.current_project(self.view).run_build( view )
    }
}

class HaxeSaveAllAndCheckCommand extends TextCommand
{
    override public function run ( args:KwArgs ) 
    {
        var edit:Edit = args.get("edit");
        trace("run HaxeSaveAllAndBuildCommand");
        var view = self.view;
        view.window().run_command("save_all");
        Projects.current_project(self.view).check_build( view )
    }
}

class HaxeSaveAllAndBuildCommand extends TextCommand
{
    override public function run ( args:KwArgs ) 
    {
        var edit:Edit = args.get("edit");
        trace("run HaxeSaveAllAndBuildCommand");
        var view = self.view;
        view.window().run_command("save_all");
        Projects.current_project(self.view).just_build( view )
    }
}

class HaxeRunBuildCommand extends TextCommand
{
    override public function run ( args:KwArgs ) 
    {
        var edit:Edit = args.get("edit");
        var view = self.view;
        trace("run HaxeRunBuildCommand");
        var project = Projects.current_project(self.view);

        if (project.has_build()) 
        {
            project.run_sublime_build( view );
        }
        else 
        {
            trace("no builds selected");
            project.extract_build_args(view, True);
        }
    }
}

class HaxeSelectBuildCommand extends TextCommand
{
    override public function run ( args:KwArgs ) 
    {
        var edit:Edit = args.get("edit");
        trace("run HaxeSelectBuildCommand");
        var view = self.view;
        Projects.current_project(self.view).select_build( view );
    }
}

class HaxeBuildOnSaveListener extends EventListener {
    override public function on_post_save(view:View) 
    {
        trace("on_post_save");
        if (view != null && view.file_name() != null) 
        {
            if (viewtools.is_supported(view) || view.file_name().endswith(".erazor.html"))
            {
                if (settings.check_on_save()) 
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