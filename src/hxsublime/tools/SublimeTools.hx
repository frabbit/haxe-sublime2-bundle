package hxsublime.tools;

import sublime.Sublime;





class SublimeTools {

    public static function getProjectFile (?winId:Int = null) {
        if (winId == null) {
            winId = Sublime.active_window().id();
        }
        return Sublime.active_window().project_file_name();
    }
}

