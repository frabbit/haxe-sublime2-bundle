
package sublime;

extern class Edit {

	static function __init__ ():Void {
		python.Macros.importFromAs("sublime", "Edit", "sublime.Edit");
	}

}