package hxsublime.commands;

import hxsublime.Codegen.HaxeImportGenerator;
import python.lib.Types.KwArgs;
import sublime.Edit;
import sublime.TextCommand;



@:keep class HaxeGenerateUsingCommand extends TextCommand
{
    override public function run( edit:Edit, ?_:KwArgs )
    {
    	
        trace("run HaxeGenerateUsingCommand");
        HaxeImportGenerator.generateUsing(view, edit);
    }
}
        
@:keep class HaxeGenerateImportCommand extends TextCommand
{
    override public function run( edit:Edit, ?_:KwArgs )
    {
        trace("run HaxeGenerateImportCommand");
        HaxeImportGenerator.generateImport(view, edit);
    }
}
