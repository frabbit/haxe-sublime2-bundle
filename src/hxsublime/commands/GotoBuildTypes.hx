package hxsublime.commands;

import haxe.ds.StringMap;
import hxsublime.commands.GotoBase.HaxeGotoBaseCommand;
import hxsublime.tools.HxSrcTools.HaxeType;
import python.lib.Types.Tup2;

class HaxeGotoBuildTypesCommand extends HaxeGotoBaseCommand<HaxeType>
{
	override public function get_entries (types:StringMap<HaxeType>):Array<Array<String>>
    {
        return [for (k in types.keys()) [k, types.get(k).file()]];
    }
        
    override public function get_data (types:StringMap<HaxeType>):Array<Tup2<String, HaxeType>>
    {
        return [for (k in types.keys()) Tup2.create(k,types.get(k))];
    }

    override public function get_file(data_entry:HaxeType):String
    {
        return data_entry.file();
    }

    override public function get_src_pos(data_entry:HaxeType):Int
    {
        return data_entry.src_pos();
    }
}