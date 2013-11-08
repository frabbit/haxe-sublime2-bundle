package hxsublime.completion.hxml;

import hxsublime.project.Project;
import python.lib.Re;
import sublime.View;

class Base {
	public static var lib_flag = Re.compile("-lib\\s+(.*?)");


	public static function auto_complete( project:Project, view:View , offset:Int, prefix:String ) 
	{
	    var src = view.substr(sublime.Region(0, offset));
	    var current_line = src[src.rfind("\n")+1:offset];
	    var m = lib_flag.match( current_line );
	    if (m != null) {
	        return project.haxelib_manager.get_completions();
	    }
	    else {
	        return [];
	    }
	}
}

/*
import sublime

import re


*/