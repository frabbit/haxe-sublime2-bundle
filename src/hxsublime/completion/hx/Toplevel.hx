package hxsublime.completion.hx;

import hxsublime.completion.hx.Types;
import hxsublime.tools.HxSrcTools;
import python.lib.Re;
import python.lib.Time;
import python.lib.Types;

using python.lib.StringTools;

using StringTools;
using python.lib.ArrayTools;

class TopLevel {
    public static var TOP_LEVEL_KEYWORDS = [Tup2.create("trace\ttoplevel","trace"),Tup2.create("this\ttoplevel","this"),Tup2.create("super\ttoplevel","super")];

    public static function get_toplevel_keywords (ctx:CompletionContext) 
    {
        return if (ctx.is_new()) [] else TOP_LEVEL_KEYWORDS;
    }
        

    public static function get_build_target(ctx:CompletionContext) 
    {
        return if (ctx.options.macro_completion()) "neko" else ctx.build().target;
    }


    public static function get_local_vars(ctx:CompletionContext):Array<Tup2<String,String>> 
    {
        var comps = [];
        for (v in hxsublime.tools.HxSrcTools.Regex.variables.finditer(ctx.src()).toHaxeIterator()) {
            comps.push(Tup2.create( v.group(1) + "\tvar" , v.group(1) ));
        }
        return comps;
    }

    public static function get_local_functions(ctx:CompletionContext):Array<Tup2<String,String>>
    {
        var comps = [];
        for (i in hxsublime.tools.HxSrcTools.Regex.named_functions.finditer(ctx.src()).toHaxeIterator()) 
        {
            var f = i.group(1);
            if (f != "new") 
            {
                comps.push(Tup2.create( f + "\tfunction" , f ));
            }
        }
        return comps;
    }

    public static function get_local_function_params(ctx:CompletionContext):Array<Tup2<String,String>>
    {
        var comps = [];
        //TODO can we restrict this to local scope ?
        for (params_text in hxsublime.tools.HxSrcTools.Regex.function_params.findallString(ctx.src())) 
        {
            var cleaned_params_text = Re.sub(hxsublime.tools.HxSrcTools.Regex.param_default,"",params_text);
            var params_list = cleaned_params_text.split(",");
            for (param in params_list) 
            {
                var a = param.strip();
                if (a.startsWith("?"))
                    a = a.substr(1);
                
                var idx = a.indexOf(":");
                if (idx > -1)
                    a = a.substring(0,idx);

                var idx = a.indexOf("=");
                if (idx > -1)
                    a = a.substring(0,idx);
                    
                a = a.strip();
                var cm = Tup2.create(a + "\tvar", a);
                if (!Lambda.has(comps, cm))
                    comps.push( cm );
            }
        }
        return comps;
    }

    public static function get_local_vars_and_functions (ctx:CompletionContext):Array<Tup2<String,String>> {
        var comps = [];
        comps.extend(get_local_vars(ctx));
        comps.extend(get_local_functions(ctx));
        comps.extend(get_local_function_params(ctx));

        return comps;
    }

    public static function get_imports (ctx:CompletionContext) 
    {
        var imports = hxsublime.tools.HxSrcTools.Regex.import_line.findallTuple( ctx.src() );
        var imported = [];
        for (i in imports) 
        {
            var imp = i.at(1);
            imported.push(imp);
        }

        return imported;
    }

    public static function get_usings (ctx:CompletionContext) 
    {
        var usings = hxsublime.tools.HxSrcTools.Regex.using_line.findallTuple( ctx.src() );
        var used = [];
        for (i in usings) 
        {

            var imp = i.at(1);
            used.push(imp);
        }

        return used;
    }

    public static function get_imports_and_usings (ctx:CompletionContext) 
    {
        var res = get_imports(ctx);
        
        res = res.concat(get_usings(ctx));

        return res;
    }


    public static function haxe_type_as_completion (type) 
    {
        var insert = type.full_pack_with_optional_module_type_and_enum_value;
        var display = type.type_name_with_optional_enum_value;
        display += "\t" + type.get_type_hint;
        return Tup2.create(display, insert);
    }

    


    public static function get_type_comps (ctx:CompletionContext, bundle:HaxeTypeBundle, imported) 
    {
        var build_target = get_build_target(ctx);
        var comps = [];
        
        for (t in bundle.all_types()) {
            if (ctx.build().is_type_available(t)) {
                var snippets = t.to_snippets(imported, ctx.orig_file());
                comps = comps.concat(snippets);
            }
        }

        for (p in bundle.packs()) {
            if (ctx.build().is_pack_available(p)) {
                var cm = Tup2.create(p + "\tpackage",p);
                comps.push(cm);
            }
        }

        return comps;
    }


    public static function get_toplevel_completion( ctx :CompletionContext )  
    {
        var start_time = Time.time();
        var comps = [];
        
        if (!ctx.is_new()) {
            comps.extend(get_toplevel_keywords(ctx));
            comps.extend(get_local_vars_and_functions(ctx));
        }


        var imported = get_imports_and_usings(ctx);

        var run_time1 = Time.time() - start_time;

        var build_bundle = ctx.build().get_types();

        var run_time2 = Time.time() - start_time;

        var std_bundle = ctx.build().std_bundle;

        

        function filter_privates(t:HaxeType) 
        {
            return !t.is_private || t.file() == ctx.orig_file();
        }

        

        var merged_bundle = std_bundle.merge(build_bundle).filter(filter_privates);

        
        var run_time3 = Time.time() - start_time;

        var comps1 = get_type_comps(ctx, merged_bundle, imported);

        var run_time4 = Time.time() - start_time;

        comps = comps.concat(comps1);
        
        var run_time = Time.time() - start_time;

        trace("TOP LEVEL COMPLETION TIME1:" + Std.string(run_time1));
        trace("TOP LEVEL COMPLETION TIME2:" + Std.string(run_time2));
        trace("TOP LEVEL COMPLETION TIME3:" + Std.string(run_time3));
        trace("TOP LEVEL COMPLETION TIME4:" + Std.string(run_time4));
        trace("TOP LEVEL COMPLETION TIME END:" + Std.string(run_time));

        return comps;
    }

    public static function get_toplevel_completion_filtered(ctx:CompletionContext) 
    {
        var comps = get_toplevel_completion(ctx);
        
        return filter_top_level_completions(ctx.offset_char(), comps);
    }

    public static function filter_top_level_completions (offset_char:String, all_comps:Array<Tup2<String, String>>) {
            
        var comps = [];

        var is_lower = "abcdefghijklmnopqrstuvwxyz".indexOf(offset_char) >= 0;
        var is_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".indexOf(offset_char) >= 0;
        var is_digit = "0123456789".indexOf(offset_char) >= 0;
        var is_special = "$_#".indexOf(offset_char) >= 0;
        
        if (is_lower || is_upper || is_digit || is_special) 
        {
            var offset_upper = offset_char.toUpperCase();
            var offset_lower = offset_char.toLowerCase();

            for (c in all_comps) 
            {

                var id = c._2;

                if (id.indexOf(offset_char) >= 0
                    || (is_upper && id.indexOf(offset_lower) >= 0)
                    || (is_lower && id.indexOf(offset_upper) >= 0)) 
                {
                    comps.push(c);
                }
            }
        }
        else {
            comps = all_comps.copy();
        }

        trace("number of top level completions (all: " + Std.string(all_comps.length) + ", filtered: " + Std.string(comps.length) + ")");
        return comps;
    }
}


/*
import re

from haxe.tools.decorator import lazyprop

from haxe.tools import hxsrctools

from haxe.log import log

import haxe.config as hxconfig

import time





*/