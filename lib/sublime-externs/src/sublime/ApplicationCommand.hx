
package sublime;

import sublime.Command;

extern class ApplicationCommand extends Command {

	static function __init__ ():Void 
	{
		python.Macros.importFromAs("sublime_plugin","ApplicationCommand", "sublime.ApplicationCommand");
	}

	// 	None	Called when the command is run.
	public function run(args:KwArgs):Void;

	
	

}