package hxsublime.commands;

import hxsublime.commands.GotoBase.HaxeGotoBaseCommand;

private typedef Entry = { file : String, src_pos : Int};

class HaxeGotoAnythingCommand extends HaxeGotoBaseCommand<Entry>
{

    override public function get_entries (types)
    {
        var fields = [for (k in types.keys()) for (p in types[k].all_fields_list) [p.to_string() + " - " + p.kind, p.type.file]];
        var types = [for (k in types.keys()) [k, types[k].file]];
        fields.extend(types);
        return fields;
    }

    override public function get_data (types)
    {
        fields = [for (k in types.keys()) for (p in types[k].all_fields_list) Tup2.create(k + "." + p.name,p)];
        types = [for (k in types.keys()) Tup2.create(k,types[k])];
        fields.extend(types);
        return fields;
    }

    override public function get_file(data_entry)
    {
        return data_entry.file;
    }

    override public function get_src_pos(data_entry)
    {
        return data_entry.src_pos;
    }
}
/*
from haxe.commands import HaxeGotoBaseCommand
    

*/