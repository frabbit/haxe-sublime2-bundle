
package sublime;

extern class Settings {

	
	static function __init__ ():Void {
		python.Macros.importFromAs("sublime", "Settings", "sublime.Settings");
	}
}