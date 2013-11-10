package hxsublime.project;

import haxe.ds.StringMap;
import hxsublime.project.Project;
import hxsublime.tools.Cache;
import hxsublime.tools.SublimeTools;
import python.lib.Builtin;
import python.lib.os.Path;
import sublime.Sublime;
import sublime.View;
import sublime.Window;




class Projects {
    public static var projects = new Cache<String, Project>(new StringMap());
    public static var userHome = Path.expanduser("~");

    
    public static var logFile = Path.join(userHome, "st3_haxe_log.txt");

    public static var nextServerPort = 6000;

    public static function fileLog (msg:Dynamic) {
        var f = Builtin.open(logFile , "a+" );
        f.write( Std.string(msg) + "\n");
        f.close();
    }



    public static function cleanup_projects() 
    {
        var win_ids = [for (w in Sublime.windows()) w.id()];
        var remove = [];
        for (p in projects.data.keys()) {
            var proj = projects.get_or_default(p, null);
            if (proj != null && !Lambda.has(win_ids, proj.win_id)) {
                remove.push(p);
            }
        }
        
        trace(remove);
        for (pid in remove) {
            trace(pid);
            var project = projects.data.get(pid).val;
            project.destroy();
            trace("delete project from memory");
            projects.data.remove(pid);
        }
    }


    public static function get_project_id(file:String, win:Window) {
        var id = if (file == null) "global" + Std.string(win.id()) else file;
        return id;
    }

    public static function get_window (?view:View):Window
    {
        var win = null;
        if (view != null) {
            win = view.window();
            if (win != null)
                win = Sublime.active_window();
        }
        else {
            win = Sublime.active_window();
        }
        return win;
    }

    public static function current_project(?view:View):Project {


        cleanup_projects();

        var file = SublimeTools.getProjectFile();
        
        var win = get_window(view);
        
        var id = get_project_id(file, win);

        trace("project id:" + id);
        //trace("project file:" + encode_utf8(file));
        trace("win.id:" + Std.string(win.id()));

        var res = projects.get_or_insert(id, create_project.bind(id, file, win));
        
        return res;
    }

    public static function create_project (id:String, file:String, win:Window):Project {
        
        
        var p = new Project(id, file, win.id(), nextServerPort);
        nextServerPort = nextServerPort + 20;
        return p;
    }
}

/*
import sublime
import sublime_plugin
import os

from haxe.tools import viewtools
from haxe.tools import sublimetools

from os.path import expanduser
from haxe.log import log

from haxe.tools.cache import Cache

from haxe.project.tools import get_window
from haxe.project.project import Project

from haxe.tools.stringtools import encode_utf8


_projects = Cache()
_user_home = expanduser("~")
_log_file = os.path.join(_user_home, str("st3_haxe_log.txt"))
_next_server_port = 6000

def file_log (msg):
    f = open(_log_file , "a+" )
    f.write( str(msg) + str("\n") )
    f.close()


#def destroy ():
#    
#    file_log("destroy called")
#
#    global _projects
#    file_log("keys " + str(list(_projects.data.keys())))
#    for p in _projects.data.keys():
#        
#        project = _projects.data[p][1]
#        file_log("project " + project.project_file)
#        project.destroy()
#    _projects = Cache()



#def plugin_unloaded_handler():
#    pass
#    #destroy()
#    
#
#
#def plugin_unloaded():
#    plugin_unloaded_handler()
#
#def unload_handler():
#    plugin_unloaded_handler()






class ProjectListener( sublime_plugin.EventListener ):

    def on_post_save( self , view ) :
        if view is not None and view.file_name() is not None and viewtools.is_hxml(view):
            project = current_project(view)
            project.clear_build()
            
    # if view is None it's a preview
    def on_activated( self , view ) :
        
        if view is not None and view.file_name() is not None and viewtools.is_supported(view): 
            def on_load_delay():
                current_project(view).generate_build( view )

            sublime.set_timeout(on_load_delay, 100)
            

    def on_pre_save( self , view ) :
        if viewtools.is_haxe(view) :
            viewtools.create_missing_folders(view)



*/