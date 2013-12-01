package hxsublime.commands;

import haxe.ds.StringMap;
import hxsublime.commands.GotoBase.HaxeGotoBaseCommand;
import hxsublime.tools.HxSrcTools.HaxeType;
import python.lib.Types.Tup2;


using python.lib.ArrayTools;

private typedef Entry = { 
    function file() : String;
    function srcPos():Int;
}



@:keep class HaxeGotoAnythingCommand extends HaxeGotoBaseCommand<Entry>
{

    override function getEntries (types:StringMap<HaxeType>)
    {
        var fields:Array<Array<String>> = [for (k in types.keys()) for (p in types.get(k).allFieldsList()) [p.toString() + " - " + p.kind, p.type.file()]];
        var types:Array<Array<String>> = [for (k in types.keys()) [k, types.get(k).file()]];
        fields.extend(types);
        return fields;
    }

    private function toEntry (e:Entry):Entry return e;

    override function getData (types:StringMap<HaxeType>)
    {
        var fields:Array<Tup2<String, Entry>> = [for (k in types.keys()) for (p in types.get(k).allFieldsList()) Tup2.create(k + "." + p.name, toEntry(p) )];
        var types = [for (k in types.keys()) Tup2.create(k,toEntry(types.get(k)))];
        fields.extend(types);
        return fields;
    }

    override function getFile(dataEntry:Entry):String
    {
        return dataEntry.file();
    }

    override function getSrcPos(dataEntry:Entry):Int
    {
        return dataEntry.srcPos();
    }
}
