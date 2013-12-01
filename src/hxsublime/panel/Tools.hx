package hxsublime.panel;

import python.lib.datetime.DateTime;

class Tools {
	public static function haxeFileRegex() 
	{
		return "^[0-9]{2}:[0-9]{2}:[0-9]{2}[ ]Error:[ ]" + hxsublime.project.Tools.haxeFileRegex.substr(1);
	}

	public static function timestampMsg (msg:String) 
	{
		return DateTime.now().strftime("%H:%M:%S") + " " + msg;
	}

	public static function isValidMessage (msg:String) 
	{
		return msg != null && msg != "" && msg != "\n";
	}
}
