package hxsublime.commands;



import haxe.ds.StringMap;
import hxsublime.commands.GotoBase.HaxeGotoBaseCommand;
import hxsublime.tools.HxSrcTools;
import python.lib.Types.Tup2;

class HaxeGotoBuildFieldsCommand extends HaxeGotoBaseCommand<HaxeField>
{

    override public function get_entries (types:StringMap<HaxeType>):Array<Array<String>>
    {
        return [for (k in types.keys()) for (p in types.get(k).all_fields_list() ) [p.toString() + " - " + p.kind, p.type.file()]];
    }
        
    override public function get_data (types:StringMap<HaxeType>):Array<Tup2<String, HaxeField>>
    {
        return [for (k in types.keys()) for (p in types.get(k).all_fields_list() ) Tup2.create(k + "." + p.name, p )];
    }

    override public function get_file(data_entry:HaxeField):String
    {
        return data_entry.type.file();
    }

    override public function get_src_pos(data_entry:HaxeField):Int
    {
        return data_entry.src_pos();
    }

}

/*

from haxe.commands import HaxeGotoBaseCommand
    


*/