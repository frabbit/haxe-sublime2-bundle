package hxsublime;

import hxsublime.panel.Base.Panels;
import python.lib.Codecs;
import sublime.Sublime;

class Log {
	public static function debug(msg:Dynamic) 
	{
		log(msg, false);
	}

	public static function log (msg:Dynamic, to_file = false) 
	{
		var msgStr = Std.string(msg);
		if (to_file) 
		{
			var f = Codecs.open( "st3_haxe_log.txt" , "ab" , "utf-8" , "ignore" );
			f.write( msgStr + "\n" );
			f.close();
		}
		else if (Settings.use_debug_panel()) 
		{
			
			function f() {
				Panels.debug_panel().writeln(msg);
			}
			Sublime.set_timeout(f, 100);
		}
		else {
			try {
				trace(msgStr);
			}
			catch (e:Dynamic) {}
		}
	}
}

/*
import sublime

import codecs

from haxe.tools.stringtools import encode_utf8




# debug should only be used for internal debugging
# currently it's the same as log but this should change in the future (2 levels (debug, log))


*/