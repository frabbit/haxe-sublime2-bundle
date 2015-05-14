package hxsublime.completion;

import haxe.ds.Option.None;
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
import sublime.Sublime;
import sublime.View;

typedef CompletionList = Array<Tuple2<String,String>>;
typedef CompletionInput = {
    offset : Int, 
    prefix:String,
    view : View,
    project : Project
}


class CompletionListener extends EventListener {

    static var triggerCb : CompletionInput->CompletionList;
    static var triggerId : Int = -1;

    static var id = 0;

    public static function trigger (view:View, showTopLevelSnippets:Bool, cb:CompletionInput->CompletionList) 
    {
        triggerId = ++id;
        triggerCb = cb;

        function run()
        {
            view.run_command( "auto_complete" , python.Lib.anonToDict({
                "api_completions_only" : !showTopLevelSnippets,
                "disable_auto_insert" : true,
                "next_completion_if_showing" : true,
                'auto_complete_commit_on_tab': true
            }));
        }
        
        view.run_command('hide_auto_complete');

        Sublime.set_timeout(run, 0);
    }

    function clear () {

        triggerCb = null;
        triggerId = -1;
    }

    public function on_query_completions(view:View, prefix:String, locations:Array<Int>)
    {
        var f = triggerCb;
        return if (f != null && triggerId == id) {
            var offset = Completion.getCompletionOffset(locations[0], prefix);
            var project = Projects.currentProject(view);
            clear();
            f({ offset : offset, prefix : prefix, view : view, project : project});
        } else {
            clear();
            trace("------------ ON QUERY COMPLETION ---------------");
            var project = Projects.currentProject(view);
            Completion.dispatchAutoComplete(project, view, prefix, locations[0]);
        }
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
        var handler = 
            if (Lambda.has(scopes, Config.SOURCE_HXML)) HxmlCompletion.autoComplete;
                
            else if (Lambda.has(scopes, Config.SOURCE_HAXE)) 
            {
                if (ViewTools.isHxsl(view)) 
                    HxslCompletion.autoComplete
                else 
                    hxsublime.completion.hx.HxCompletion.eventTriggeredAutoComplete; // hx completion
            } else emptyHandler;
        return handler;
    }

    public static function dispatchAutoComplete (project:Project, view:View, prefix:String, location:Int)
    {
        var startTime = Time.time();

        var offset = getCompletionOffset(location, prefix);

        var scopes = getCompletionScopes(view, location);

        var comps = 
            if (canRunCompletion(offset, scopes)) 
            {
                var handler = getAutoCompleteHandler(view, scopes);
                handler(project, view, offset, prefix);
            } 
            else [];
        
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
