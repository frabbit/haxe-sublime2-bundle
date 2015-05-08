package hxsublime.commands;

import haxe.ds.StringMap;
import hxsublime.commands.GotoBase.HaxeGotoBaseCommand;
import hxsublime.tools.HxSrcTools;
import python.Tuple;

@:keep class HaxeGotoBuildFieldsCommand extends HaxeGotoBaseCommand<HaxeField>
{
    override public function getEntries (types:StringMap<HaxeType>):Array<Array<String>>
    {
        return [for (k in types.keys()) for (p in types.get(k).allFieldsList() ) [p.toString() + " - " + p.kind, p.type.file()]];
    }

    override public function getData (types:StringMap<HaxeType>):Array<Tuple2<String, HaxeField>>
    {
        return [for (k in types.keys()) for (p in types.get(k).allFieldsList() ) Tuple2.make(k + "." + p.name, p )];
    }

    override public function getFile(data_entry:HaxeField):String
    {
        return data_entry.type.file();
    }

    override public function getSrcPos(data_entry:HaxeField):Int
    {
        return data_entry.srcPos();
    }

}
