package hxsublime;

import python.lib.os.Path;
import python.lib.Subprocess;
import python.Exceptions.AttributeError;

class Plugin
{
	static var _startupInfo = null;

	public static function plugin_base_dir()
	{
		return Path.abspath(Path.join(Path.dirname(python.Syntax.pythonCode("__file__")), "."));
	}

	public static function startupInfo ()
	{
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
