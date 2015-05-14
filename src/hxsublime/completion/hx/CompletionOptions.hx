package hxsublime.completion.hx;

import hxsublime.build.Build;
import hxsublime.completion.hx.Constants;
import hxsublime.completion.hx.CompletionTypes;
import hxsublime.completion.hx.TopLevelOptions;
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

class CompletionOptions implements LazyFunctionSupport
{

    var _types:CompletionTypes;
    var _toplevel:TopLevelOptions;
    var _context:Int;
    
    public var userActivated:Bool;

    public function new(types = Constants.COMPLETION_TYPE_REGULAR, userActivated = false, toplevel = Constants.COMPLETION_TYPE_TOPLEVEL)
    {
        this.userActivated = userActivated;
        this._types = new CompletionTypes(types);
        this._toplevel = new TopLevelOptions(toplevel);
    }

    public function copy()
    {
        return new CompletionOptions(this.types().val(), this.userActivated, this._toplevel.val());
    }

    @property
    public function types()
    {
        return this._types;
    }

    public function eq (other:CompletionOptions)
    {
        return this._types.eq(other._types) && this._toplevel.eq(other._toplevel) && this.userActivated == other.userActivated;
    }
}


