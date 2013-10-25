
package sublime;

class Sublime {

	public static var OP_EQUAL : Int;
	public static var OP_NOT_EQUAL : Int;
	public static var OP_REGEX_MATCH : Int;
	public static var OP_NOT_REGEX_MATCH : Int;
	public static var OP_REGEX_CONTAINS : Int;
	public static var OP_NOT_REGEX_CONTAINS : Int;

	static function __init__ ():Void {
		python.Macros.importAs("sublime", "sublime.Sublime");
	}
}