package hxsublime.completion.hx;

import hxsublime.build.Build;
import hxsublime.completion.hx.Constants;
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





class TopLevelOptions {

    var _opt:Int;

    public function new(val = 0)
    {
        this._opt = val;
    }

    public function val () {
        return this._opt;
    }

    public function set (val) {
        this._opt |= val;
    }

    public function hasTypes () {
        return (this._opt & Constants.TOPLEVEL_OPTION_TYPES) > 0;
    }

    public function hasLocals () {
        return (this._opt & Constants.TOPLEVEL_OPTION_LOCALS) > 0;
    }

    public function hasKeywords () {
        return (this._opt & Constants.TOPLEVEL_OPTION_KEYWORDS) > 0;
    }

    public function eq (other:TopLevelOptions) {
        return this._opt == other._opt;
    }
}

