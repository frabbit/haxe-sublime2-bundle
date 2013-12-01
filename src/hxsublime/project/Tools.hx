package hxsublime.project;

import sublime.View;
import sublime.Sublime;

class Tools {
	public static function getWindow (view:View) 
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
	static var winStart = "(?:(?:[A-Za-z][:])";
	static var unixStart = "(?:[/]?)";
	public static var haxeFileRegex = "^(" + winStart + "|" + unixStart + ")?(?:[^:]*)):([0-9]+): (?:character(?:s?)|line(?:s?))? ([0-9]+)-?[0-9]*\\s?:(.*)$";
}
