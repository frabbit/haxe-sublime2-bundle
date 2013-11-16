package hxsublime.completion;

import hxsublime.Config;
import hxsublime.project.Base.Projects;
import hxsublime.project.Project;
import hxsublime.tools.ScopeTools;
import hxsublime.tools.ViewTools;
import python.lib.Time;
import python.lib.Types.Tup2;
import sublime.EventListener;
import sublime.View;


class CompletionListener extends EventListener {

    public function on_query_completions(view:View, prefix:String, locations:Array<Int>) 
    {
        var project = Projects.current_project(view);
        return Completion.dispatch_auto_complete(project, view, prefix, locations[0]);
    }

}

class Completion {
    // auto complete is triggered, this function dispatches to actual completion based
    // on the file type of the current view

    public static function get_completion_scopes (view:View, location:Int) {
        return ViewTools.getScopesAt(view, location);
    }

    public static function get_completion_offset (location:Int, prefix:String) {
        return location - prefix.length;
    }

    public static function can_run_completion(offset, scopes:Array<String>) {
        return if (offset == 0) false else is_supported_scope(scopes);
    }

    public static function is_supported_scope(scopes:Array<String>) 
    {
        return !ScopeTools.containsStringOrComment(scopes);
    }

    public static function empty_handler(project:Project, view:View, offset:Int, prefix:String) 
    {
        return [];
    }

    public static function get_auto_complete_handler (view:View, scopes:Array<String>) 
    {
        
        var handler = null;

        if (Lambda.has(scopes, Config.SOURCE_HXML)) // hxml completion
            handler =  hxsublime.completion.hxml.Base.auto_complete;
        else if (Lambda.has(scopes, Config.SOURCE_HAXE)) // hx can be hxsl or haxe
            if (ViewTools.isHxsl(view)) {
                handler = hxsublime.completion.hxsl.Base.auto_complete; // hxsl completion
            } else {
                handler = hxsublime.completion.hx.Base.auto_complete; // hx completion
            }
        else { // empy handler
            handler = empty_handler;
        }
                
        return handler;
    }

    public static function dispatch_auto_complete (project:Project, view:View, prefix:String, location:Int) 
    {
        var start_time = Time.time();

        var offset = get_completion_offset(location, prefix);

        var scopes = get_completion_scopes(view, location);

        var comps = null;


        trace("pre handler");
        if (can_run_completion(offset, scopes)) {
            trace("run handler");
            var handler = get_auto_complete_handler(view, scopes);
            comps = handler(project, view, offset, prefix);
            
        } else {
            trace("no handler");
            comps = [];
        }

        trace("do log info");
        log_completion_info(start_time, Time.time(), comps);

        return comps;
    }

    public static function log_completion_info (start_time:Int, end_time:Int, comps:Array<Tup2<String,String>>) 
    {
        var run_time = end_time-start_time;
        trace("on_query_completion time: " + Std.string(run_time));
        trace("number of completions: " + Std.string(comps.length));
    }
}
