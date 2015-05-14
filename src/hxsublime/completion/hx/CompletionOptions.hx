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

class CompletionOptions implements LazyFunctionSupport
{

    public var userActivated:Bool;

    public function new(userActivated = false)
    {
        this.userActivated = userActivated;
    }

    public function copy()
    {
        return new CompletionOptions(this.userActivated);
    }

    public function eq (other:CompletionOptions)
    {
        return this.userActivated == other.userActivated;
    }
}


