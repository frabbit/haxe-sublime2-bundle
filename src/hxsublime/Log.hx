package hxsublime;

import hxsublime.panel.Panels;
import python.lib.Codecs;
import sublime.Sublime;

class Log 
{

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
		else if (Settings.useDebugPanel()) 
		{
			
			function f() {
				Panels.debugPanel().writeln(msg);
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
