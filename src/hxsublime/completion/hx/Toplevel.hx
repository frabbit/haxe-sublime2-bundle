package hxsublime.completion.hx;

import hxsublime.completion.hx.CompletionContext;
import hxsublime.tools.HxSrcTools;
import python.lib.Re;
import python.lib.Time;

import python.Tuple;

using hxsublime.support.StringTools;

using StringTools;
using hxsublime.support.ArrayTools;

class TopLevel
{
    public static var TOP_LEVEL_KEYWORDS = [Tuple2.make("trace\ttoplevel","trace"),Tuple2.make("this\ttoplevel","this"),Tuple2.make("super\ttoplevel","super")];

    public static function getToplevelKeywords (ctx:CompletionContext)
    {
        return if (ctx.is_new()) [] else TOP_LEVEL_KEYWORDS;
    }


    public static function getBuildTarget(ctx:CompletionContext)
    {
        return if (ctx.options.macroCompletion()) "neko" else ctx.build().target().plattform;
    }


    public static function getLocalVars(ctx:CompletionContext):Array<Tuple2<String,String>>
    {
        var comps = [];
        for (v in hxsublime.tools.HxSrcTools.Regex.variables.finditer(ctx.src())) {
            comps.push(Tuple2.make( v.group(1) + "\tvar" , v.group(1) ));
        }
        return comps;
    }

    public static function getLocalFunctions(ctx:CompletionContext):Array<Tuple2<String,String>>
    {
        var comps = [];
        for (i in hxsublime.tools.HxSrcTools.Regex.named_functions.finditer(ctx.src()).toHaxeIterator())
        {
            var f = i.group(1);
            if (f != "new")
            {
                comps.push(Tuple2.make( f + "\tfunction" , f ));
            }
        }
        return comps;
    }

    public static function getLocalFunctionParams(ctx:CompletionContext):Array<Tuple2<String,String>>
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
                var cm = Tuple2.make(a + "\tvar", a);
                if (!Lambda.has(comps, cm))
                    comps.push( cm );
            }
        }
        return comps;
    }

    public static function getLocalVarsAndFunctions (ctx:CompletionContext):Array<Tuple2<String,String>> {
        var comps = [];
        comps.extend(getLocalVars(ctx));
        comps.extend(getLocalFunctions(ctx));
        comps.extend(getLocalFunctionParams(ctx));

        return comps;
    }

    public static function getImports (ctx:CompletionContext)
    {
        var imports = hxsublime.tools.HxSrcTools.Regex.import_line.findallTuple( ctx.src() );
        var imported = [];
        for (i in imports)
        {
            var imp = i[1];
            imported.push(imp);
        }

        return imported;
    }

    public static function getUsings (ctx:CompletionContext)
    {
        var usings = hxsublime.tools.HxSrcTools.Regex.using_line.findallTuple( ctx.src() );
        var used = [];
        for (i in usings)
        {

            var imp = i[1];
            used.push(imp);
        }

        return used;
    }

    public static function getImportsAndUsings (ctx:CompletionContext)
    {
        var res = getImports(ctx);

        res = res.concat(getUsings(ctx));

        return res;
    }


    public static function haxeTypeAsCompletion (type)
    {
        var insert = type.full_pack_with_optional_module_type_and_enum_value;
        var display = type.type_name_with_optional_enum_value;
        display += "\t" + type.get_type_hint;
        return Tuple2.make(display, insert);
    }




    public static function getTypeComps (ctx:CompletionContext, bundle:HaxeTypeBundle, imported)
    {
        var build_target = getBuildTarget(ctx);
        var comps = [];

        var startTime = Time.time();

        var allTypes = bundle.allTypes();

        var runTime0 = Time.time() - startTime;

        for (t in allTypes) {
            if (ctx.build().isTypeAvailable(t)) {
                var snippets = t.toSnippets(imported, ctx.orig_file());
                comps.extend(snippets);
            }
        }

        var runTime1 = Time.time() - startTime;

        for (p in bundle.packs()) {
            if (ctx.build().isPackAvailable(p)) {
                var cm = Tuple2.make(p + "\tpackage",p);
                comps.push(cm);
            }
        }

        var runTime2 = Time.time() - startTime;

        trace("get_type_comps time0" + Std.string(runTime0));
        trace("get_type_comps time1" + Std.string(runTime1));
        trace("get_type_comps time2" + Std.string(runTime2));

        return comps;
    }


    public static function getToplevelCompletion( ctx :CompletionContext )
    {
        var startTime = Time.time();
        var comps = [];

        if (!ctx.is_new()) {
            comps.extend(getToplevelKeywords(ctx));
            comps.extend(getLocalVarsAndFunctions(ctx));
        }


        var imported = getImportsAndUsings(ctx);

        var runTime1 = Time.time() - startTime;

        var build_bundle = ctx.build().getTypes();

        var runTime2 = Time.time() - startTime;

        var std_bundle = ctx.build().stdBundle();



        function filterPrivates(t:HaxeType)
        {
            return !t.is_private || t.file() == ctx.orig_file();
        }



        var merged_bundle = std_bundle.merge(build_bundle).filter(filterPrivates);


        var runTime3 = Time.time() - startTime;

        var comps1 = getTypeComps(ctx, merged_bundle, imported);

        var runTime4 = Time.time() - startTime;

        comps.extend(comps1);

        var runTime = Time.time() - startTime;

        trace("TOP LEVEL COMPLETION TIME1:" + Std.string(runTime1));
        trace("TOP LEVEL COMPLETION TIME2:" + Std.string(runTime2));
        trace("TOP LEVEL COMPLETION TIME3:" + Std.string(runTime3));
        trace("TOP LEVEL COMPLETION TIME4:" + Std.string(runTime4));
        trace("TOP LEVEL COMPLETION TIME END:" + Std.string(runTime));

        return comps;
    }

    public static function getToplevelCompletionFiltered(ctx:CompletionContext)
    {
        var comps = getToplevelCompletion(ctx);

        trace(ctx.prefix);
        return filterTopLevelCompletions(ctx.prefix, comps);
    }

    public static function filterTopLevelCompletions (prefix:String, all_comps:Array<Tuple2<String, String>>)
    {
        var comps = [];

        trace("c : " + prefix);

        if (prefix.length == 0)
        {
            comps = all_comps.copy();
        }
        else
        {
            var test = [];
            for (i in 0...prefix.length) {


                var c = prefix.charAt(i);

                var isLower = "abcdefghijklmnopqrstuvwxyz".indexOf(c) > -1;
                var isUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".indexOf(c) > -1;
                var is_digit = "0123456789".indexOf(c) > -1;
                var is_special = "$_#".indexOf(c) > -1;
                if (isLower || isUpper || is_digit || is_special)
                {
                    var offsetUpper = c.toUpperCase();
                    var offsetLower = c.toLowerCase();

                    test.push(offsetLower);
                }


            }
            for (c in all_comps)
            {
                var found = true;
                var id = c._2.toLowerCase();
                var oldId = id;

                for (cur in test)
                {
                    if (found)
                    {
                        var index = id.indexOf(cur);

                        if (index > -1)
                        {
                            id = id.substr(index+1);
                        }
                        else
                        {
                            found = false;
                            break;
                        }

                    }
                }

                if (found)
                {
                    comps.push(c);
                }


            }
        }
        trace("number of top level completions (all: " + Std.string(all_comps.length) + ", filtered: " + Std.string(comps.length) + ")");
        return comps;
    }
}

