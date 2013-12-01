package hxsublime.commands;

import hxsublime.commands.FindDeclaration.HaxeFindDeclarationCommand;
import hxsublime.panel.Panels;
import python.lib.Types.Dict;
import sublime.View;


@:keep class HaxeGetTypeOfExprCommand extends HaxeFindDeclarationCommand
{
    override public function helperMethod() 
    {
        return "hxsublime.FindDeclaration.__getType";
    }
        

    override public function handleSuccessfulResult(view:View, json_res:Dict<String, Dynamic>, using_insert, insert_before, insert_after, expr_end, build, temp_path, temp_file) 
    {
        var t:String = json_res.get("type", null);
        var e:String = json_res.get("expr", null);
        
        var msg = "Expr: " + e + "\n" + "Type: " + t;

        Panels.slidePanel().writeln(msg, false);
    }
}
