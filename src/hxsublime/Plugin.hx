package hxsublime;

import python.lib.os.Path;
import python.lib.Subprocess;
import python.lib.Types.AttributeError;

class Plugin {
	public static function plugin_base_dir() 
	{
		return Path.abspath(Path.join(Path.dirname(untyped __python__("__file__")), ".."));
	}
	static var _startupInfo = null;
	public static function startupInfo () {
		if (_startupInfo != null) return _startupInfo;
		try {
			_startupInfo = Subprocess.STARTUPINFO();
			_startupInfo.dwFlags |= Subprocess.STARTF_USESHOWWINDOW;
			_startupInfo.wShowWindow = Subprocess.SW_HIDE;
		}
		catch (e:AttributeError) {
			_startupInfo = null;
		}
		return _startupInfo;
	}
}

/*

import sublime
import os
import subprocess


try:  
	STARTUP_INFO = subprocess.STARTUPINFO()
	STARTUP_INFO.dwFlags |= subprocess.STARTF_USESHOWWINDOW
	STARTUP_INFO.wShowWindow = subprocess.SW_HIDE
except (AttributeError):
	STARTUP_INFO = None



is_st3 = int(sublime.version()) >= 3000

is_st2 = int(sublime.version()) < 3000


def plugin_base_dir():
	return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


#print("IS SUBLIME TEXT 3: " + str(is_st3))

*/