package sublime;

import sublime.Command;
import sublime.View;

import python.KwArgs;


@:pythonImport("sublime_plugin","TextCommand")
extern class TextCommand extends Command {

	var view:View;



	public function new (v:View):Void;

	// 	None	Called when the command is run.
	public function run(edit:Edit, ?args:KwArgs<Dynamic>):Void;



}