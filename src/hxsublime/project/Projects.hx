package hxsublime.project;

import haxe.ds.StringMap;
import hxsublime.project.Project;
import hxsublime.tools.Cache;
import hxsublime.tools.SublimeTools;
import python.lib.Builtins;
import python.lib.os.Path;
import sublime.Sublime;
import sublime.View;
import sublime.Window;




class Projects
{
    static var projects = new Cache<String, Project>(new StringMap());
    static var userHome = Path.expanduser("~");


    static var logFile = Path.join(userHome, "st3_haxe_log.txt");

    static var nextServerPort = 6000;

    function fileLog (msg:Dynamic)
    {
        var f = cast( Builtins.open(logFile , "a+" ), python.lib.io.TextIOBase);
        f.write( Std.string(msg) + "\n");
        f.close();
    }



    static function cleanupProjects()
    {
        var win_ids = [for (w in Sublime.windows()) w.id()];
        var remove = [];
        for (p in projects.data.keys()) {
            var proj = projects.getOrDefault(p, null);
            if (proj != null && !Lambda.has(win_ids, proj.winId)) {
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


    static function getProjectId(file:String, win:Window)
    {
        var id = if (file == null) "global" + Std.string(win.id()) else file;
        return id;
    }

    static function getWindow (?view:View):Window
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

    public static function currentProject(?view:View):Project
    {
        cleanupProjects();

        var file = SublimeTools.getProjectFile();

        var win = getWindow(view);

        var id = getProjectId(file, win);

        trace("project id:" + id);
        trace("win.id:" + Std.string(win.id()));

        var res = projects.getOrInsert(id, createProject.bind(id, file, win));

        return res;
    }

    static function createProject (id:String, file:String, win:Window):Project
    {
        var p = new Project(id, file, win.id(), nextServerPort);
        nextServerPort = nextServerPort + 20;
        return p;
    }
}
