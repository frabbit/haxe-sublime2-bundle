package hxsublime.commands;

import hxsublime.Codegen.HaxeImportGenerator;
import python.lib.Types.KwArgs;
import sublime.Edit;
import sublime.TextCommand;



@:keep class HaxeGenerateUsingCommand extends TextCommand
{
    override public function run( edit:Edit, ?kwArgs:KwArgs )
    {
    	
        trace("run HaxeGenerateUsingCommand");
        HaxeImportGenerator.generate_using(view, edit);
    }
}
        
@:keep class HaxeGenerateImportCommand extends TextCommand
{
    override public function run( edit:Edit, ?kwArgs:KwArgs )
    {
        trace("run HaxeGenerateImportCommand");
        HaxeImportGenerator.generate_import(view, edit);
    }
}

/*
import sublime_plugin

from haxe import codegen

from haxe.log import log


*/