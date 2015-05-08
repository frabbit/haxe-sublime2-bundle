
package sublime.def.exec;

import python.Dict;


@:pythonImport("Default.exec","AsyncProcess")
extern class AsyncProcess {
	public function new (cmd:Array<String>, shell_cmd:Array<String>, env:Dict<String,String>, listener:ProcessListener, path:String = "", shell:Bool = false):Void;

	public function kill ():Void;
	public function poll ():Bool;
	public function exit_code():Int;
	public function read_stdout():Void;
	public function read_stderr():Void;

	public var start_time(default, null):Int;


}