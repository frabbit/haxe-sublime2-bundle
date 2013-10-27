
package sublime;

extern class Window {

	
	static function __init__ ():Void {
		python.Macros.importFromAs("sublime", "Window", "sublime.Window");
	}

}