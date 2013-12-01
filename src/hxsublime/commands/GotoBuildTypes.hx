package hxsublime.commands;

import haxe.ds.StringMap;
import hxsublime.commands.GotoBase.HaxeGotoBaseCommand;
import hxsublime.tools.HxSrcTools.HaxeType;
import python.lib.Types.Tup2;

@:keep class HaxeGotoBuildTypesCommand extends HaxeGotoBaseCommand<HaxeType>
{
	override function getEntries (types:StringMap<HaxeType>):Array<Array<String>>
    {
        return [for (k in types.keys()) [k, types.get(k).file()]];
    }
        
    override function getData (types:StringMap<HaxeType>):Array<Tup2<String, HaxeType>>
    {
        return [for (k in types.keys()) Tup2.create(k,types.get(k))];
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