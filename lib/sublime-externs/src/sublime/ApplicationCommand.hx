
package sublime;

extern class ApplicationCommand {

	static function __init__ ():Void 
	{
		python.Macros.importFromAs("sublime_plugin","ApplicationCommand", "sublime.ApplicationCommand");
	}

	// 	None	Called when the command is run.
	public function run(args:KwArgs):Void;

	// 	bool	Returns true if the command is able to be run at this time. The default implementation simply always returns True.
	public function is_enabled(args:KwArgs):Bool;

	// 	bool	Returns true if the command should be shown in the menu at this time. The default implementation always returns True.
	public function is_visible(args:KwArgs):Bool;

	// 	String	Returns a description of the command with the given arguments. Used in the menu, if no caption is provided. Return None to get the default description.
	public function description(args:KwArgs):String;

	// 	bool	Returns true if a checkbox should be shown next to the menu item. The .sublime-menu file must have the checkbox attribute set to true for this to be used.
	public function is_checked(args:KwArgs):Bool;
	

}