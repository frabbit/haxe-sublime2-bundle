package hxsublime.tools;

import python.lib.Re;
import python.lib.Sys;
import python.lib.Types.Bytes;

import StringTools in ST;

class StringTools {

	static var _whitespace = Re.compile("^\\s*$");

	public static function startsWithAny (s:String, l:Array<String>) 
	{
		for (s1 in l) {
			if (ST.startsWith(s, s1)) {
				return true;
			}
		}
		return false;
	}

	public static function reverse (s:String) 
	{
		return untyped __python__("s[::-1]");
	}


	public static function isWhitespaceOrEmpty(s:String) 
	{
		return Re.match(_whitespace, s) != null;
	}


	public static function unicodeToStr(s:Bytes, encoding:String, errors:String = "") 
	{
		return s.decode(encoding, errors);
	}

	public static function strToUnicodeToStr (s:String, encoding1:String, encoding2:String) 
	{
		return unicodeToStr(python.lib.StringTools.encode(s, encoding1), encoding2);
	}

	public static function strToUnicode (s:String, encoding:String, ?errors:String = "") 
	{
		return python.lib.StringTools.encode(s, encoding, errors);
	}

	public static function toUnicode (s:String):Bytes 
	{
		var res:Bytes = null;
		if (s == null) 
		{
			return null;
		} 
		else 
		{
			try
				res = strToUnicode(s, "utf-8", "ignore")
			catch (e:Dynamic)
				try 
					res = strToUnicode(s,"ascii")
				catch (e:Dynamic)
					try
						res = strToUnicode(s,"iso-8859-1")
					catch (e:Dynamic)
						try
							res = strToUnicode(s,"ascii")
						catch (e:Dynamic)
							throw "cannot decode str";
		}

		return res;
	}

	public static function st3EncodeUtf8 (s:String):String {
		return encodeUtf8(s);
	}
	
	public static function st2EncodeUtf8 (s:String):String
	{
		return s;
	}


	public static function st2ToUnicode(s:Bytes):Bytes {
		return s;
	}

	public static function encodeUtf8Bytes (s:Bytes):String {
		return s.decode("utf-8", "ignore");
	}

	public static function encodeUtf8 (s:String):String 
	{
		if (s == null)
			return null;

		var res = null;
		
		try
			res = strToUnicodeToStr(s, "ascii", "utf-8")
		catch (e:Dynamic)
			try
				res = strToUnicodeToStr(s, "iso-8859-1", "utf-8")
			catch (e:Dynamic)
				throw "cannot decode str";
		
		return res;
	}
	
}
