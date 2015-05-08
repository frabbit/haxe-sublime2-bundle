package sublime;

import sublime.Command;

@:pythonImport("sublime_plugin","ApplicationCommand");
extern class ApplicationCommand extends Command {

	// 	None	Called when the command is run.
	public function run(args:KwArgs):Void;

}