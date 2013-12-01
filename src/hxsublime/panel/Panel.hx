
package hxsublime.panel;

import sublime.View;

typedef Panel = {

	public var outputView:View;
	public var outputViewId:Int;

	public function clear():Void;

	public function write( text :String , ?scope:String, ?show_timestamp:Bool ):Void;
	public function writeln (msg:String, ?scope:String, ?show_timestamp:Bool):Void;
	public function status (title:String, msg:String):Void;

}