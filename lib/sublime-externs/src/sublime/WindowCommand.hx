package sublime;

import sublime.Command;
import sublime.Window;
import python.KwArgs;

@:pythonImport("sublime_plugin","WindowCommand")
extern class WindowCommand extends Command 
{
	var window:Window;

	public function new (w:Window):Void;

	// 	None	Called when the command is run.
	public function run(args:KwArgs<Dynamic>):Void;
}