package hxsublime.completion.hxml;

import hxsublime.project.Project;
import python.lib.Re;
import sublime.Region;
import sublime.View;

class HxmlCompletion 
{
	static var libFlag = Re.compile("-lib\\s+(.*?)");

	public static function autoComplete( project:Project, view:View , offset:Int, prefix:String ) 
	{
	    var src = view.substr(new Region(0, offset));
	    var currentLine = src.substring(src.indexOf("\n")+1,offset);
	    var m = libFlag.match( currentLine );
	    if (m != null) {
	        return project.haxelibManager().getCompletions();
	    }
	    else {
	        return [];
	    }
	}
}
