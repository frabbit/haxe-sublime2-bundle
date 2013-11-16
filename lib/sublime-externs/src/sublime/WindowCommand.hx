
package sublime;

import python.lib.Types;
import sublime.Command;
import sublime.Window;

extern class WindowCommand extends Command {

	var window:Window;

	public function new (w:Window):Void;

	static function __init__ ():Void 
	{
		python.Macros.importFromAs("sublime_plugin","WindowCommand", "sublime.WindowCommand");
	}
	// 	None	Called when the command is run.
	public function run(args:KwArgs):Void;

}