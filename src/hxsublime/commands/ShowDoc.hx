package hxsublime.commands;

import hxsublime.commands.FindDeclaration.HaxeFindDeclarationCommand;
import hxsublime.panel.Panels;
import python.Dict;
import sublime.View;

class HaxeShowDocCommand extends HaxeFindDeclarationCommand
{

    override public function helperMethod()
    {
        return "hxsublime.FindDeclaration.__sublimeShowDoc";
    }

    override public function handleSuccessfulResult(view:View, json_res:Dict<String,Dynamic>, using_insert, insert_before, insert_after, expr_end, build, temp_path, temp_file)
    {
        var doc = null;
        if (json_res.hasKey("doc"))
        {
            doc = json_res.get("doc", null);
        }
        else
        {
            doc = "No documentation found";
        }
        trace("json: " + Std.string(json_res));
        trace("doc: " + Std.string(doc));
        Panels.slidePanel().writeln(doc, false);
    }
}

