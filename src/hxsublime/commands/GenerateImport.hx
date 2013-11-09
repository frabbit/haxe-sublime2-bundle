package hxsublime.commands;



class HaxeGenerateUsingCommand extends TextCommand
{
    override public function run( kwArgs:KwArgs )
    {
    	var edit:Edit = kwArgs.get("edit");
        trace("run HaxeGenerateUsingCommand");
        Codegen.generate_using(view, edit);
    }
}
        
class HaxeGenerateImportCommand extends TextCommand
{
    override public function run( kwArgs:KwArgs )
    {
    	var edit:Edit = kwArgs.get("edit");
        trace("run HaxeGenerateImportCommand");
        codegen.generate_import(view, edit);
    }
}

/*
import sublime_plugin

from haxe import codegen

from haxe.log import log


*/