package hxsublime.completion.hx;

import hxsublime.build.Build;
import hxsublime.macros.LazyFunctionSupport;
import hxsublime.project.CompletionState.CompletionCache;
import hxsublime.project.Project;
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

private typedef Settings = {
    
    public function showCompletionTimes(?view:View):Bool;
}

class CompletionSettings implements LazyFunctionSupport
{
    var settings:Settings;
    public function new(settings)
    {
        this.settings = settings;
    }

    @lazyFunction
    public function showCompletionTimes(view:View) {
        return settings.showCompletionTimes(view);
    }
}
