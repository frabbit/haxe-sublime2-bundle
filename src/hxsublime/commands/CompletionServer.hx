package hxsublime.commands;

import hxsublime.project.Base.Projects;
import sublime.Sublime;
import sublime.WindowCommand;


class HaxeRestartServerCommand extends WindowCommand 
{

    public override function run(_:KwArgs) 
    { 
        trace("run HaxeRestartServerCommand");
        
        var view = Sublime.active_window().active_view();
        
        var project = Projects.current_project(view);

        project.restart_server( view );
    }
}

/*
import sublime, sublime_plugin
import os
import re
import functools

from haxe import project as hxproject

from haxe.log import log

 */      