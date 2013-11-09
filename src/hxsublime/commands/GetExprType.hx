package hxsublime.commands;


class HaxeGetTypeOfExprCommand extends HaxeFindDeclarationCommand
{
    public function helper_method() 
    {
        return "hxsublime.FindDeclaration.__getType";
    }
        

    public function handle_successfull_result(view:View, json_res, using_insert, insert_before, insert_after, expr_end, build, temp_path, temp_file) 
    {
        var t = json_res["type"];
        var e = json_res["expr"];
        
        var msg = "Expr: " + e + "\n" + "Type: " + t;

        panel.slide_panel().writeln(msg, false);
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