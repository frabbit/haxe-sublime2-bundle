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
import python.lib.Builtin;
import python.lib.Re;
import python.lib.Time;
import python.lib.Types.Tup2;
import python.lib.Types.Tup4;
import python.lib.Types.Tup5;
import sublime.Region;
import sublime.View;

using python.lib.StringTools;


using python.lib.ArrayTools;

class CompletionOptions implements LazyFunctionSupport 
{

    var _types:CompletionTypes;
    var _toplevel:TopLevelOptions;
    var _context:Int;
    var _trigger:Int;

    public function new(trigger:Int, context = Constants.COMPILER_CONTEXT_REGULAR, types = Constants.COMPLETION_TYPE_REGULAR, toplevel = Constants.COMPLETION_TYPE_TOPLEVEL)
    {
        this._types = new CompletionTypes(types);
        this._toplevel = new TopLevelOptions(toplevel);
        this._context = context;
        this._trigger = trigger;
    }

    public function copyAsManual() 
    {
        return new CompletionOptions(Constants.COMPLETION_TRIGGER_MANUAL, this._context, this.types().val(), this._toplevel.val());
    }

    public function copyAsAsync() 
    {
        return new CompletionOptions(Constants.COMPLETION_TRIGGER_ASYNC, this._context, this.types().val(), this._toplevel.val());
    }

    @property
    public function types() 
    {
        return this._types;
    }


    @lazyFunction
    public function asyncTrigger() 
    {
        return this._trigger == Constants.COMPLETION_TRIGGER_ASYNC;
    }

    @lazyFunction
    public function manualCompletion() 
    {
        return this._trigger == Constants.COMPLETION_TRIGGER_MANUAL;
    }

    @lazyFunction
    public function macroCompletion() 
    {
        return this._context == Constants.COMPILER_CONTEXT_MACRO;
    }

    @lazyFunction
    public function regularCompletion() 
    {
        return this._context == Constants.COMPILER_CONTEXT_REGULAR;
    }

    public function eq (other:CompletionOptions) 
    {
        return this._trigger == other._trigger && this._types.eq(other._types) && this._toplevel.eq(other._toplevel) && this._context == other._context;
    }
}


