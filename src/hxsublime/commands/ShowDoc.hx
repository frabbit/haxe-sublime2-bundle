package hxsublime.commands;

import hxsublime.commands.FindDeclaration.HaxeFindDeclarationCommand;

class HaxeShowDocCommand extends HaxeFindDeclarationCommand
{

    override public function helper_method()
    {
        return "hxsublime.FindDeclaration.__sublimeShowDoc";
    }

    override public function handle_successfull_result(view:View, json_res, using_insert, insert_before, insert_after, expr_end, build, temp_path, temp_file)
    {
        if ("doc" in json_res.keys()) 
        {
            doc = json_res["doc"];
        }
        else 
        {
            doc = "No documentation found";
        }
        trace("json: " + Std.string(json_res));
        trace("doc: " + Std.string(doc));
        panel.slide_panel().writeln(doc, false);
    }
}

/*

import sublime, sublime_plugin
import json

from haxe import panel

from haxe.commands.find_declaration import HaxeFindDeclarationCommand

from haxe.log import log



*/
