package hxsublime.commands;

import hxsublime.commands.FindDeclaration.HaxeFindDeclarationCommand;
import hxsublime.panel.Base.Panels;
import python.lib.Types.Dict;
import sublime.View;


@:keep class HaxeGetTypeOfExprCommand extends HaxeFindDeclarationCommand
{
    override public function helper_method() 
    {
        return "hxsublime.FindDeclaration.__getType";
    }
        

    override public function handle_successfull_result(view:View, json_res:Dict<String, Dynamic>, using_insert, insert_before, insert_after, expr_end, build, temp_path, temp_file) 
    {
        var t:String = json_res.get("type", null);
        var e:String = json_res.get("expr", null);
        
        var msg = "Expr: " + e + "\n" + "Type: " + t;

        Panels.slide_panel().writeln(msg, false);
    }
}

/*
import sublime, sublime_plugin
import os
from sublime import Region

from haxe.tools import pathtools

from haxe import panel

from haxe.commands.find_declaration import HaxeFindDeclarationCommand

# TODO this is currently not working


   */