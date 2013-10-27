
package sublime;

extern class Selection {

	static function __init__ ():Void {
		python.Macros.importFromAs("sublime", "Selection", "sublime.Selection");
	}

}