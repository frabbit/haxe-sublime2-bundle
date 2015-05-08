package hxsublime.support;

import python.Bytes;
import python.Tuple;

class StringTools {

	public static function format (s:String, args:Array<Dynamic>):String
	{
		return python.Syntax.callField(s, "format", (args:python.VarArgs<Dynamic>));
	}

	public static function encode(s:String, encoding:String="utf-8", errors:String="strict"):Bytes {
		return python.Syntax.callField(s, "encode", encoding, errors);
	}

	public static inline function contains(s:String, e:String):Bool {
		return untyped __python_in__(e,s);
	}

	public static inline function strip(s:String, ?chars:String):String
	{
		return untyped __field__(s, "strip")(chars);
	}

	public static inline function rpartition (s:String, sep:String):Tuple3<String, String, String>
	{
		return untyped __field__(s, "rpartition")(sep);
	}

}