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

typedef SettingsInterface = {
    //public function smarts_hints_only_next(?view:View):Bool;
    public function noFuzzyCompletion(?view:View):Bool;
    public function topLevelCompletionsOnDemand(?view:View):Bool;
    public function isAsyncCompletion(?view:View):Bool;
    public function showOnlyAsyncCompletions(?view:View):Bool;
    public function getCompletionDelays(?view:View):Tuple2<Int, Int>;
    public function showCompletionTimes(?view:View):Bool;
}

class CompletionSettings implements LazyFunctionSupport
{
    var settings:SettingsInterface;
    public function new(settings)
    {

        this.settings = settings;
    }

    //@lazyprop
    //public function smarts_hints_only_next() {
    //    return settings.smarts_hints_only_next();
    //}

    @lazyFunction
    public function noFuzzyCompletion() {
        return settings.noFuzzyCompletion();
    }

    @lazyFunction
    public function topLevelCompletionsOnDemand() {
        return settings.topLevelCompletionsOnDemand();
    }

    @lazyFunction
    public function isAsyncCompletion() {
        return settings.isAsyncCompletion();
    }

    @lazyFunction
    public function showOnlyAsyncCompletions() {
        return settings.showOnlyAsyncCompletions();
    }

    @lazyFunction
    public function getCompletionDelays() {
        return settings.getCompletionDelays();
    }

    @lazyFunction
    public function showCompletionTimes(view:View) {
        return settings.showCompletionTimes(view);
    }
}
