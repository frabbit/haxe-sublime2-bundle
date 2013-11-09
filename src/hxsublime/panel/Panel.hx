
package hxsublime.panel;

import sublime.View;

typedef Panel = {

	public var output_view:View;
	public var output_view_id:Int;

	public function clear():Void;

	public function write( text :String , ?scope:String, ?show_timestamp:Bool ):Void;
	public function writeln (msg:String, ?scope:String, ?show_timestamp:Bool):Void;
	public function status (title:String, msg:String):Void;

}