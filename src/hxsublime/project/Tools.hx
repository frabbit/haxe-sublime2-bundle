package hxsublime.project;

import sublime.View;
import sublime.Sublime;

class Tools {
	public static function get_window (view:View) 
	{
		var win = null;
	    if (view != null) 
	    {
	        win = view.window();
	        if (win == null) 
	        {
	            win = Sublime.active_window();
	        }
	    }
	    else {
	        win = Sublime.active_window();
	    }
	    return win;
	}


	// allow windows drives
	static var _win_start = "(?:(?:[A-Za-z][:])";
	static var _unix_start = "(?:[/]?)";
	public static var haxe_file_regex = "^(" + _win_start + "|" + _unix_start + ")?(?:[^:]*)):([0-9]+): (?:character(?:s?)|line(?:s?))? ([0-9]+)-?[0-9]*\\s?:(.*)$";
}
/*
import sublime

*/