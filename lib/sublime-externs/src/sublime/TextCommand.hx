
package sublime;

import python.lib.Types;
import sublime.Command;
import sublime.View;

extern class TextCommand extends Command {

	var view:View;

	static function __init__ ():Void 
	{
		python.Macros.importFromAs("sublime_plugin","TextCommand", "sublime.TextCommand");
	}

	public function new (v:View):Void;

	// 	None	Called when the command is run.
	public function run(edit:Edit, ?args:KwArgs):Void;

	

}