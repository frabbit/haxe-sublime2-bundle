package hxsublime.commands;

import hxsublime.Codegen.HaxeImportGenerator;
import python.lib.Types.KwArgs;
import sublime.Edit;
import sublime.TextCommand;



class HaxeGenerateUsingCommand extends TextCommand
{
    override public function run( kwArgs:KwArgs )
    {
    	var edit:Edit = kwArgs.get("edit", null);
        trace("run HaxeGenerateUsingCommand");
        HaxeImportGenerator.generate_using(view, edit);
    }
}
        
class HaxeGenerateImportCommand extends TextCommand
{
    override public function run( kwArgs:KwArgs )
    {
    	var edit:Edit = kwArgs.get("edit", null);
        trace("run HaxeGenerateImportCommand");
        HaxeImportGenerator.generate_import(view, edit);
    }
}

/*
import sublime_plugin

from haxe import codegen

from haxe.log import log


*/