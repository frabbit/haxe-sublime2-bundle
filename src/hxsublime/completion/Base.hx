package hxsublime.completion;

import hxsublime.project.Base.Projects;
import sublime.EventListener;


class CompletionListener extends EventListener {

    public function on_query_completions(view:View, prefix:String, locations:Array<Int>) 
    {
        var project = Projects.current_project(view);
        return dispatch_auto_complete(project, view, prefix, locations[0]);
    }

}

class Completion {
    // auto complete is triggered, this function dispatches to actual completion based
    // on the file type of the current view

    public static function get_completion_scopes (view:View, location:Int) {
        return viewtools.get_scopes_at(view, location)
    }

    public static function get_completion_offset (location:Int, prefix:String) {
        return location - prefix.length;
    }

    public static function can_run_completion(offset, scopes:Array<String>) {
        return if (offset == 0) false else is_supported_scope(scopes);
    }

    public static function is_supported_scope(scopes:Array<String>) 
    {
        return !Scopetools.contains_string_or_comment(scopes);
    }

    public static function empty_handler(project:Project, view:View, offset:Int, prefix:String) 
    {
        return [];
    }

    public static function get_auto_complete_handler (view:View, scopes:Array<String>) 
    {
        
        var handler = None

        if (Lambda.has(scopes, hxconfig.SOURCE_HXML)) // hxml completion
            handler = hxml.auto_complete;
        else if (Lambda.has(scopes, hxconfig.SOURCE_HAXE)) // hx can be hxsl or haxe
            if (Viewtools.is_hxsl(view)) {
                handler = hxsl.auto_complete // hxsl completion
            } else {
                handler = hx.auto_complete // hx completion
            }
        else { // empy handler
            handler = empty_handler;
        }
                
        return handler
    }

    public static function dispatch_auto_complete (project:Project, view:View, prefix:String, location:Int) 
    {
        var start_time = Time.time();

        var offset = get_completion_offset(location, prefix);

        var scopes = get_completion_scopes(view, location);

        var comps = null;

        if (can_run_completion(offset, scopes)) {
            handler = get_auto_complete_handler(view, scopes);
            comps = handler(project, view, offset, prefix);
        } else {
            comps = [];
        }

        log_completion_info(start_time, time.time(), comps);

        return comps;
    }

    public static function log_completion_info (start_time:Int, end_time:Int, comps:Array<Tup2<String,String>>) 
    {
        var run_time = end_time-start_time;
        log("on_query_completion time: " + Std.string(run_time));
        log("number of completions: " + Std.string(comps.length));
    }
}
