package hxsublime.completion;

import hxsublime.completion.hxsl.HxslCompletion;
import hxsublime.completion.hxml.HxmlCompletion;
import hxsublime.Config;
import hxsublime.project.Projects;
import hxsublime.project.Project;
import hxsublime.tools.ScopeTools;
import hxsublime.tools.ViewTools;
import python.lib.Time;
import python.Tuple;
import sublime.EventListener;
import sublime.View;


class CompletionListener extends EventListener {

    public function on_query_completions(view:View, prefix:String, locations:Array<Int>)
    {
        var project = Projects.currentProject(view);
        return Completion.dispatchAutoComplete(project, view, prefix, locations[0]);
    }

}

class Completion
{
    // auto complete is triggered, this function dispatches to actual completion based
    // on the file type of the current view

    public static function getCompletionScopes (view:View, location:Int)
    {
        return ViewTools.getScopesAt(view, location);
    }

    public static function getCompletionOffset (location:Int, prefix:String)
    {
        return location - prefix.length;
    }

    public static function canRunCompletion(offset, scopes:Array<String>)
    {
        return if (offset == 0) false else isSupportedScope(scopes);
    }

    public static function isSupportedScope(scopes:Array<String>)
    {
        return !ScopeTools.containsStringOrComment(scopes);
    }

    public static function emptyHandler(project:Project, view:View, offset:Int, prefix:String)
    {
        return [];
    }

    public static function getAutoCompleteHandler (view:View, scopes:Array<String>)
    {
        var handler = if (Lambda.has(scopes, Config.SOURCE_HXML)) // hxml completion
            HxmlCompletion.autoComplete;
        else if (Lambda.has(scopes, Config.SOURCE_HAXE)) // hx can be hxsl or haxe
            if (ViewTools.isHxsl(view))
            {
                HxslCompletion.autoComplete; // hxsl completion
            }
            else
            {
                hxsublime.completion.hx.HxCompletion.autoComplete; // hx completion
            }
        else { // empy handler
            emptyHandler;
        }
        return handler;
    }

    public static function dispatchAutoComplete (project:Project, view:View, prefix:String, location:Int)
    {
        var startTime = Time.time();

        var offset = getCompletionOffset(location, prefix);

        var scopes = getCompletionScopes(view, location);

        var comps = null;


        trace("pre handler");
        if (canRunCompletion(offset, scopes)) {
            trace("run handler");
            var handler = getAutoCompleteHandler(view, scopes);
            comps = handler(project, view, offset, prefix);

        } else {
            trace("no handler");
            comps = [];
        }

        trace("do log info");
        logCompletionInfo(startTime, Time.time(), comps);

        return comps;
    }

    public static function logCompletionInfo (startTime:Float, endTime:Float, comps:Array<Tuple2<String,String>>)
    {
        var runTime = endTime-startTime;
        trace("on_query_completion time: " + Std.string(runTime));
        trace("number of completions: " + Std.string(comps.length));
    }
}
