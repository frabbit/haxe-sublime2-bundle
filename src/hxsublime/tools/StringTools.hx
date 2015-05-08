package hxsublime.tools;

import python.lib.Re;
import python.lib.Sys;
import python.Bytes;

import StringTools in ST;

class StringTools
{
	static var _whitespace = Re.compile("^\\s*$");

	public static function startsWithAny (s:String, l:Array<String>)
	{
		for (s1 in l)
		{
			if (ST.startsWith(s, s1))
			{
				return true;
			}
		}
		return false;
	}

	public static function isWhitespaceOrEmpty(s:String)
	{
		return Re.match(_whitespace, s) != null;
	}
}
