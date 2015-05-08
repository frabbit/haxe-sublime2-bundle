package hxsublime.commands;

import hxsublime.Codegen.HaxeImportGenerator;
import python.KwArgs;
import sublime.Edit;
import sublime.TextCommand;



@:keep class HaxeGenerateUsingCommand extends TextCommand
{
    override public function run( edit:Edit, ?_:KwArgs<Dynamic> )
    {

        trace("run HaxeGenerateUsingCommand");
        HaxeImportGenerator.generateUsing(view, edit);
    }
}

@:keep class HaxeGenerateImportCommand extends TextCommand
{
    override public function run( edit:Edit, ?_:KwArgs<Dynamic> )
    {
        trace("run HaxeGenerateImportCommand");
        HaxeImportGenerator.generateImport(view, edit);
    }
}
