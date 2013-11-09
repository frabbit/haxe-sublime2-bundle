import Sublime;

class Log {
	public static function debug(msg:Dynamic) 
	{
		log(msg, False)
	}

	public static function log (msg:Dynamic, to_file = false) 
	{
		var msgStr = Std.string(msg);
		if (to_file) 
		{
			f = codecs.open( "st3_haxe_log.txt" , "wb" , "utf-8" , "ignore" );
			f.append( msgStr + "\n" );
			f.close();
		}
		else if (Settings.use_debug_panel()) 
		{
			
			function f() {
				hxpanel.debug_panel().writeln(encode_utf8(msg));
			}
			Sublime.set_timeout(f, 100);
		}
		else {
			try {
				print(msgStr);
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