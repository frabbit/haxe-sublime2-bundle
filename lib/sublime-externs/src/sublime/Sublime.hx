
package sublime;

import python.lib.Types;


private typedef TODO = Dynamic;

extern 
class Sublime {

	public static var ENCODED_POSITION:Int; // Indicates the file_name should be searched for a :row or :row:col suffix
	public static var TRANSIENT:Int; // Open the file as a preview only: it wont have a tab assigned it until modified

	public static var DRAW_EMPTY:Int; // Draw empty regions with a vertical bar. By default, they arent drawn at all.
	public static var HIDE_ON_MINIMAP:Int; // Dont show the regions on the minimap.
	public static var DRAW_EMPTY_AS_OVERWRITE:Int; // Draw empty regions with a horizontal bar instead of a vertical one.
	public static var DRAW_NO_FILL:Int; // Disable filling the regions, leaving only the outline.
	public static var DRAW_NO_OUTLINE:Int; // Disable drawing the outline of the regions.
	public static var DRAW_SOLID_UNDERLINE:Int; // Draw a solid underline below the regions.
	public static var DRAW_STIPPLED_UNDERLINE:Int; // Draw a stippled underline below the regions.
	public static var DRAW_SQUIGGLY_UNDERLINE:Int; // Draw a squiggly underline below the regions.
	public static var PERSISTENT:Int; // Save the regions in the session.
	public static var HIDDEN:Int; // Dont draw the regions.

	public static var CLASS_WORD_START:Int;
	public static var CLASS_WORD_END:Int;
	public static var CLASS_PUNCTUATION_START:Int;
	public static var CLASS_PUNCTUATION_END:Int;
	public static var CLASS_SUB_WORD_START:Int;
	public static var CLASS_SUB_WORD_END:Int;
	public static var CLASS_LINE_START:Int;
	public static var CLASS_LINE_END:Int;
	public static var CLASS_EMPTY_LINE:Int;

	public static var OP_EQUAL : Int;
	public static var OP_NOT_EQUAL : Int;
	public static var OP_REGEX_MATCH : Int;
	public static var OP_NOT_REGEX_MATCH : Int;
	public static var OP_REGEX_CONTAINS : Int;
	public static var OP_NOT_REGEX_CONTAINS : Int;

	public static var MONOSPACE_FONT:Int;

	
	// None	Runs the callback in the main thread after the given delay (in milliseconds). Callbacks with an equal delay will be run in the order they were added.
	public static function set_timeout(callback:Void->Void, delay:Int):Void;	
	
	// None	Runs the callback on an alternate thread after the given delay (in milliseconds).
	public static function set_async_timeout(callback:Void->Void, delay:Int):Void;
	
	// None	Sets the message that appears in the status bar.
	public static function status_message(string:String):Void;
	
	// None	Displays an error dialog to the user.
	public static function error_message(string:String):Void;
	
	// None	Displays a message dialog to the user.
	public static function message_dialog(string:String):Void;

	// bool	Displays an ok / cancel question dialog to the user. If ok_button is provided, this may be used as the text on the ok button. Returns True if the user presses the ok button.
	public static function ok_cancel_dialog(string:String, ?ok_button:String):Bool;	
	
	// String	Loads the given resource. The name should be in the format Packages/Default/Main.sublime-menu.
	public static function load_resource(name:String):String;
	
	// bytes	Loads the given resource. The name should be in the format Packages/Default/Main.sublime-menu.
	public static function load_binary_resource(name:String):TODO;	
	
	// [String]	Finds resources whose file name matches the given pattern.
	public static function find_resources(pattern:String):Array<String>;
	
	// String	Encode a JSON compatible value into a string representation. If pretty is set to True, the string will include newlines and indentation.
	public static function encode_value(value:Dynamic, ?pretty:Bool):Dynamic;
	
	// value	Decodes a JSON string into an object. If the string is invalid, a ValueError will be thrown.
	public static function decode_value(string:String):Dynamic;
	
	// Settings	Loads the named settings. The name should include a file name and extension, but not a path. The packages will be searched for files matching the base name, and the results will be collated into the settings object. Subsequent calls to load_settings with the name base_name will return the same object, and not load the settings from disk again.
	public static function load_settings(base_name:String):Null<Settings>;
	
	// None	Flushes any in-memory changes to the named settings object to disk.
	public static function save_settings(base_name:String):Void;
	
	// [Window]	Returns a list of all the open windows.
	public static function windows():Array<Window>;
	
	// Window	Returns the most recently used window.
	public static function active_window():Window;	
	
	// String	Returns the base path to the packages.
	public static function packages_path():String;	
	
	// String	Returns the path where all the users *.sublime-package files are.
	public static function installed_packages_path():String;	
	
	// String	Returns the path where Sublime Text stores cache files.
	public static function cache_path():String;
	
	// String	Returns the contents of the clipboard. size_limit is there to protect against unnecessarily large data, defaults to 16,777,216 characters
	public static function get_clipboard(?size_limit:Int):String;	
	
	// None	Sets the contents of the clipboard.
	public static function set_clipboard(string:String):Void;
	
	// Int	Matches the selector against the given scope, returning a score. A score of 0 means no match, above 0 means a match. Different selectors may be compared against the same scope: a higher score means the selector is a better match for the scope.
	public static function score_selector(scope:String, selector:String):Int;
	
	// None	Runs the named ApplicationCommand with the (optional) given arguments.
	public static function run_command(string:String, ?args:KwArgs):Void;
	
	// None	Controls command logging. If enabled, all commands run from key bindings and the menu will be logged to the console.
	public static function log_commands(flag:Int):Void;
	
	// None	Controls input logging. If enabled, all key presses will be logged to the console.
	public static function log_input(flag:Int):Void;
	
	// None	Controls result regex logging. This is useful for debugging regular expressions used in build systems.
	public static function log_result_regex(flag:Int):Void;
	
	// String	Returns the version number
	public static function version():String;
	
	// String	Returns the platform, which may be "osx", "linux" or "windows"
	public static function platform():String;
	
	// String	Returns the CPU architecture, which may be "x32" or "x64"
	public static function arch():String;	

	static function __init__ ():Void {
		python.Macros.importAs("sublime", "sublime.Sublime");
	}
}