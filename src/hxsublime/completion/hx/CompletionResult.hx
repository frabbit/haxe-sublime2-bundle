package hxsublime.completion.hx;

import hxsublime.build.Build;
import hxsublime.macros.LazyFunctionSupport;
import hxsublime.project.CompletionState.CompletionCache;
import hxsublime.project.Project;
import hxsublime.Settings;
import hxsublime.tools.StringTools;
import hxsublime.tools.ViewTools;
import python.lib.Builtins;
import python.lib.Re;
import python.lib.Time;
import python.Tuple;
import sublime.Region;
import sublime.View;

using hxsublime.support.StringTools;


using hxsublime.support.ArrayTools;

class CompletionResult implements LazyFunctionSupport {

    public static function emptyResult (ctx:CompletionContext, retrieve_toplevel_comps = null) {
        return new CompletionResult("", [], "", [], ctx, retrieve_toplevel_comps);
    }

    public var hints:Array<Array<String>>;
    public var ctx:CompletionContext;

    var ret:String;
    var comps:Array<Tuple2<String, String>>;
    var status:String;


    var retrieve_toplevel_comps:Void->Array<Tuple2<String, String>>;



    public function new (ret:String, comps:Array<Tuple2<String, String>>, status:String, hints:Array<Array<String>>, ctx:CompletionContext, retrieve_toplevel_comps:Void->Array<Tuple2<String, String>>)
    {

        this.ret = ret;
        this.comps = comps;
        this.status = status;
        this.hints = hints;
        this.ctx = ctx;
        if (retrieve_toplevel_comps == null) {

            retrieve_toplevel_comps = function () return [];
        }

        this.retrieve_toplevel_comps = retrieve_toplevel_comps;
    }


    @lazyFunction
    function _toplevel_comps():Array<Tuple2<String, String>> {

        return retrieve_toplevel_comps();
    }

    @lazyFunction
    function hasHints () {
        return hints.length > 0;
    }

    @lazyFunction
    function hasCompilerResults () {
        return comps.length > 0;
    }

    @lazyFunction
    public function hasResults () {
        return comps.length > 0 || hints.length > 0 || (requiresToplevelComps() && this._toplevel_comps().length > 0);
    }

    @lazyFunction
    public function showTopLevelSnippets () 
    {
        var req = requiresToplevelComps();

        var r = req && !ctx.is_new();

        return r;
    }


    @lazyFunction
    function requiresToplevelComps()
    {
        var prefix_is_whitespace = hxsublime.tools.StringTools.isWhitespaceOrEmpty(ctx.prefix);
        
        var r = !((prefix_is_whitespace && hasHints() && ctx.isHint()) || hasCompilerResults());
        return r;
    }

    @lazyFunction
    public function allComps ()
    {
        var res = [];

        if (requiresToplevelComps()) {
            res.extend(_toplevel_comps());
        }
        res.extend(comps);
        res.sort(function (s1, s2) return (s1._1 < s2._1) ? -1 : (s1._1 > s2._1) ? 1 : 0);
        return res;
    }
}


