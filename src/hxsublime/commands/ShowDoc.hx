package hxsublime.commands;

import hxsublime.commands.FindDeclaration.HaxeFindDeclarationCommand;
import hxsublime.panel.Base.Panels;
import python.lib.Types.Dict;
import sublime.View;

class HaxeShowDocCommand extends HaxeFindDeclarationCommand
{

    override public function helper_method()
    {
        return "hxsublime.FindDeclaration.__sublimeShowDoc";
    }

    override public function handle_successfull_result(view:View, json_res:Dict<String,Dynamic>, using_insert, insert_before, insert_after, expr_end, build, temp_path, temp_file)
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
        Panels.slide_panel().writeln(doc, false);
    }
}

/*

import sublime, sublime_plugin
import json

from haxe import panel

from haxe.commands.find_declaration import HaxeFindDeclarationCommand

from haxe.log import log



*/
