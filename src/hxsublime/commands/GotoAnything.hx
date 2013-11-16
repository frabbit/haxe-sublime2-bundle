package hxsublime.commands;

import haxe.ds.StringMap;
import hxsublime.commands.GotoBase.HaxeGotoBaseCommand;
import hxsublime.tools.HxSrcTools.HaxeType;
import python.lib.Types.Tup2;


using python.lib.ArrayTools;

private typedef Entry = { 
    function file() : String;
    function src_pos():Int;
}



@:keep class HaxeGotoAnythingCommand extends HaxeGotoBaseCommand<Entry>
{

    override public function get_entries (types:StringMap<HaxeType>)
    {
        var fields:Array<Array<String>> = [for (k in types.keys()) for (p in types.get(k).all_fields_list()) [p.toString() + " - " + p.kind, p.type.file()]];
        var types:Array<Array<String>> = [for (k in types.keys()) [k, types.get(k).file()]];
        fields.extend(types);
        return fields;
    }

    private function toEntry (e:Entry):Entry return e;

    override public function get_data (types:StringMap<HaxeType>)
    {
        var fields:Array<Tup2<String, Entry>> = [for (k in types.keys()) for (p in types.get(k).all_fields_list()) Tup2.create(k + "." + p.name, toEntry(p) )];
        var types = [for (k in types.keys()) Tup2.create(k,toEntry(types.get(k)))];
        fields.extend(types);
        return fields;
    }

    override public function get_file(data_entry:Entry):String
    {
        return data_entry.file();
    }

    override public function get_src_pos(data_entry:Entry):Int
    {
        return data_entry.src_pos();
    }
}
/*
from haxe.commands import HaxeGotoBaseCommand
    

*/