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


class CompletionTypes
{
    var _opt:Int;

    public function new( val = Constants.COMPLETION_TYPE_REGULAR) {
        _opt = val;
    }

    public function val () {
        return _opt;
    }

    public function add (val:Int)
    {
        _opt |= val;
    }

    public function addHint ()
    {
        _opt = _opt | Constants.COMPLETION_TYPE_HINT;
    }

    public function hasRegular () {
        return (_opt & Constants.COMPLETION_TYPE_REGULAR) > 0;
    }

    public function hasHint () {
        return (_opt & Constants.COMPLETION_TYPE_HINT) > 0;
    }

    public function hasToplevel () {
        return (_opt & Constants.COMPLETION_TYPE_TOPLEVEL) > 0;
    }

    public function hasToplevelForced () {
        return (_opt & Constants.COMPLETION_TYPE_TOPLEVEL_FORCED) > 0;
    }

    public function eq (other:CompletionTypes) {
        return _opt == other._opt;
    }

}

