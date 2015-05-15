package hxsublime.commands;

import haxe.ds.StringMap;
import hxsublime.commands.GotoBase.HaxeGotoBaseCommand;
import hxsublime.tools.HxSrcTools.HaxeType;
import python.Tuple;

@:keep class HaxeGotoBuildTypesCommand extends HaxeGotoBaseCommand<HaxeType>
{

    public static var COMMAND_ID = "hxsublime_commands__haxe_goto_build_types";

	override function getEntries (types:StringMap<HaxeType>):Array<Array<String>>
    {
        return [for (k in types.keys()) [k, types.get(k).file()]];
    }

    override function getData (types:StringMap<HaxeType>):Array<Tuple2<String, HaxeType>>
    {
        return [for (k in types.keys()) Tuple2.make(k,types.get(k))];
    }

    override function getFile(dataEntry:HaxeType):String
    {
        return dataEntry.file();
    }

    override function getSrcPos(dataEntry:HaxeType):Int
    {
        return dataEntry.srcPos();
    }
}