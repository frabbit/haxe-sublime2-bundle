
package sublime;

import python.lib.Re.Pattern;

import python.lib.Types;

private typedef TODO = Dynamic;



private typedef Vector = Tup2<Int,Int>;

extern class View {

	static function __init__ ():Void {
		python.Macros.importFromAs("sublime", "View", "sublime.View");
	}

	// 	int	Returns a number that uniquely identifies this view.
	public static function id():Int;
	
	// 	int	Returns a number that uniquely identifies the buffer underlying this view.
	public static function buffer_id():Int;
	
	// String	The full name file the file associated with the buffer, or None if it doesnt exist on disk.
	public static function file_name():String;
	
	// String	The name assigned to the buffer, if any
	public static function name():String;
	
	// Assigns a name to the buffer
	public static function set_name(name:String):Void;	
	
	// Returns true if the buffer is still loading from disk, and not ready for use.
	public static function is_loading():Bool;
	
	// Returns true if there are any unsaved modifications to the buffer.
	public static function is_dirty():Bool;
	
	// Returns true if the buffer may not be modified.
	public static function is_read_only():Bool;
	
	// Sets the read only property on the buffer.
	public static function set_read_only(value:Bool):Void;	
	
	// Returns true if the buffer is a scratch buffer. Scratch buffers never report as being dirty.
	public static function is_scratch():Bool;
	
	// Sets the scratch property on the buffer.
	public static function set_scratch(value:Bool):Void;	
	
	// Settings	Returns a reference to the views settings object. Any changes to this settings object will be private to this view.
	public static function settings():Settings;
	
	// Window	Returns a reference to the window containing the view.
	public static function window():Window;
	
	// Runs the named TextCommand with the (optional) given arguments.
	//public static function run_command(string:String, args:NamedArgs):Void;	

	macro public static function run_command(string:ExprOf<String>, args:ExprOf<{}>):Void {
		return return macro @:pos(string.pos) 
			untyped __named__(untyped __field__(sublime.View, $string), $args);
	}	

	// int	Returns the number of character in the file.
	public static function size():Int;
	
	// String	Returns the contents of the region as a string.
	// String	Returns the character to the right of the point.
	@:overload(function (point:Int):String {})
	public static function substr(region:Region):String;
	
	
	
	
	// int	Inserts the given string in the buffer at the specified point. Returns the number of characters inserted: this may be different if tabs are being translated into spaces in the current buffer.
	public static function insert(edit:Edit, point:Int, string:String):Int;
	
	// Erases the contents of the region from the buffer.
	public static function erase(edit:Edit, region:Region):Void;	
	
	// Replaces the contents of the region with the given string.
	public static function replace(edit:Edit, region:Region, string:String):Void;	
	
	// Selection	Returns a reference to the selection.
	public static function sel():Selection;
	
	// Region	Returns a modified copy of region such that it starts at the beginning of a line, and ends at the end of a line. Note that it may span several lines.
	// Region	Returns the line that contains the point.
	@:overload(function (region:Region):Region {})
	public static function line(point:Int):Region;
	
	
	
	// Region	As line(), but the region includes the trailing newline character, if any.
	// Region	As line(), but the region includes the trailing newline character, if any.
	@:overload(function (region:Region):Region {})
	public static function full_line(point:Int):Region;
	
	
	
	
	// [Region]	Returns a list of lines (in sorted order) intersecting the region.
	public static function lines(region:Region):Array<Region>;
	
	// [Region]	Splits the region up such that each region returned exists on exactly one line.
	public static function split_by_newlines(region:Region):Array<Region>;
	
	
	
	public static var CLASS_WORD_START:Int;
	public static var CLASS_WORD_END:Int;
	public static var CLASS_PUNCTUATION_START:Int;
	public static var CLASS_PUNCTUATION_END:Int;
	public static var CLASS_SUB_WORD_START:Int;
	public static var CLASS_SUB_WORD_END:Int;
	public static var CLASS_LINE_START:Int;
	public static var CLASS_LINE_END:Int;
	public static var CLASS_EMPTY_LINE:Int;

	// Region	Returns the word that contains the point.
	
	// Region	Returns a modified copy of region such that it starts at the beginning of a word, and ends at the end of a word. Note that it may span several words.
	@:overload(function (point:Int):Region {})
	public static function word(region:Region):Region;
	
	/*
		Classifies pt, returning a bitwise OR of zero or more of these flags:
		CLASS_WORD_START
		CLASS_WORD_END
		CLASS_PUNCTUATION_START
		CLASS_PUNCTUATION_END
		CLASS_SUB_WORD_START
		CLASS_SUB_WORD_END
		CLASS_LINE_START
		CLASS_LINE_END
		CLASS_EMPTY_LINE
	*/
	public static function classify(point:Int):Int;
	
	// Region	Finds the next location after point that matches the given classes. If forward is False, searches backwards instead of forwards. classes is a bitwise OR of the sublime.CLASS_XXX flags. separators may be passed in, to define what characters should be considered to separate words.
	public static function find_by_class(point:Int, forward:Bool, classes:Int, separators:String):Region;
	
	// Region	Expands point to the left and right, until each side lands on a location that matches classes. classes is a bitwise OR of the sublime.CLASS_XXX flags. separators may be passed in, to define what characters should be considered to separate words.
	// Region	Expands region to the left and right, until each side lands on a location that matches classes. classes is a bitwise OR of the sublime.CLASS_XXX flags. separators may be passed in, to define what characters should be considered to separate words.
	@:overload(function (region:Int, classes:Int, separators:String):Region {})
	public static function expand_by_class(point:Int, classes:Int, separators:String):Region;
	
	
	
	// Region	Returns the first Region matching the regex pattern, starting from the given point, or None if it cant be found. The optional flags parameter may be sublime.LITERAL, sublime.IGNORECASE, or the two ORed together.
	public static function find(pattern:Pattern, fromPosition:Int, ?flags:Int):Region;
	
	// [Region]	Returns all (non-overlapping) regions matching the regex pattern. 
	// The optional flags parameter may be sublime.LITERAL, sublime.IGNORECASE, or the two ORed together. If a format string is given, then all matches will be formatted with the formatted string and placed into the extractions list.
	public static function find_all(pattern:Pattern, ?flags:Int, ?format:String, ?extractions:Array<String>):Array<Region>;
	
	// 	(int, int)	Calculates the 0 based line and column numbers of the point.
	public static function rowcol(point:Int):Tup2<Int, Int>;
	
	// int	Calculates the character offset of the given, 0 based, row and column. Note that 'col' is interpreted as the number of characters to advance past the beginning of the row.
	public static function text_point(row:Int, col:Int):Int;
	
	// None	Changes the syntax used by the view. syntax_file should be a name along the lines of Packages/Python/Python.tmLanguage. To retrieve the current syntax, use view.settings().get('syntax').
	public static function set_syntax_file(syntax_file:String):Void;	
	
	// Region	Returns the extent of the syntax name assigned to the character at the given point.
	public static function extract_scope(point:Int):Region;
	
	// String	Returns the syntax name assigned to the character at the given point.
	public static function scope_name(point:Int):String;
	
	// Int	Matches the selector against the scope at the given location, returning a score. A score of 0 means no match, above 0 means a match. Different selectors may be compared against the same scope: a higher score means the selector is a better match for the scope.
	public static function score_selector(point:Int, selector:String):Int;
	
	// [Regions]	Finds all regions in the file matching the given selector, returning them as a list.
	public static function find_by_selector(selector:String):Array<Region>;
	
	// None	Scroll the view to show the given point.
	
	
	// None	Scroll the view to show the given region.
	// None	Scroll the view to show the given region set.
	@:overload(function (point:Int, ?show_surrounds:Bool):Void {})
	@:overload(function (region_set:Set<Region>, ?show_surrounds:Bool):Void {})
	public static function show(region:Region, ?show_surrounds:Bool):Void;	
	
	
	
	
	// None	Scroll the view to center on the region.
	@:overload(function (region:Region):Void {})
	// None	Scroll the view to center on the point.
	public static function show_at_center(point:Int):Void;
	
	// 	Region	Returns the currently visible area of the view.
	public static function visible_region():Region;

	// Vector	Returns the offset of the viewport in layout coordinates.
	public static function viewport_position():Vector;

	// None	Scrolls the viewport to the given layout position.
	public static function set_viewport_position(vector:Vector, ?animate:Bool):Void;	

	// 	vector	Returns the width and height of the viewport.
	public static function viewport_extent():Vector;

	// vector	Returns the width and height of the layout.
	public static function layout_extent():Vector;

	// vector	Converts a text position to a layout position
	public static function text_to_layout(point:Int):Vector;

	// point	Converts a layout position to a text position
	public static function layout_to_text(vector:Vector):Int;

	// real	Returns the light height used in the layout
	public static function line_height():Float;
	
	// real	Returns the typical character width used in the layout
	public static function em_width():Float;
	

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

	/*
		Add a set of regions to the view. If a set of regions already exists with the given key, they will be overwritten. The scope is used to source a color to draw the regions in, it should be the name of a scope, such as "comment" or "string". If the scope is empty, the regions wont be drawn.
		The optional icon name, if given, will draw the named icons in the gutter next to each region. The icon will be tinted using the color associated with the scope. Valid icon names are dot, circle, bookmark and cross. The icon name may also be a full package relative path, such as Packages/Theme - Default/dot.png.

		The optional flags parameter is a bitwise combination of:

		sublime.DRAW_EMPTY. Draw empty regions with a vertical bar. By default, they arent drawn at all.
		sublime.HIDE_ON_MINIMAP. Dont show the regions on the minimap.
		sublime.DRAW_EMPTY_AS_OVERWRITE. Draw empty regions with a horizontal bar instead of a vertical one.
		sublime.DRAW_NO_FILL. Disable filling the regions, leaving only the outline.
		sublime.DRAW_NO_OUTLINE. Disable drawing the outline of the regions.
		sublime.DRAW_SOLID_UNDERLINE. Draw a solid underline below the regions.
		sublime.DRAW_STIPPLED_UNDERLINE. Draw a stippled underline below the regions.
		sublime.DRAW_SQUIGGLY_UNDERLINE. Draw a squiggly underline below the regions.
		sublime.PERSISTENT. Save the regions in the session.
		sublime.HIDDEN. Dont draw the regions.
		The underline styles are exclusive, either zero or one of them should be given. If using an underline, DRAW_NO_FILL and DRAW_NO_OUTLINE should generally be passed in.

	*/
	// None	
	public static function add_regions(key:String, regions:Array<Region>, ?scope:String, ?icon:String, ?flags:Int):Void;	
	
	// [regions]	Return the regions associated with the given key, if any
	public static function get_regions(key:String):Array<Region>;
	
	// None	Removed the named regions
	public static function erase_regions(key:String):Void;	
	
	// None	Adds the status key to the view. The value will be displayed in the status bar, in a comma separated list of all status values, ordered by key. Setting the value to the empty string will clear the status.
	public static function set_status(key:String, value:TODO):Void;	
	
	// 	String	Returns the previously assigned value associated with the key, if any.
	public static function get_status(key:String):String;
	
	// 	None	Clears the named status.
	public static function erase_status(key:String):Void;
	
	/*
		Returns the command name, command arguments, and repeat count for the given history entry, as stored in the undo / redo stack.
		Index 0 corresponds to the most recent command, -1 the command before that, and so on. Positive values for index indicate to look in the redo stack for commands. If the undo / redo history doesnt extend far enough, then (None, None, 0) will be returned.

		Setting modifying_only to True (the default is False) will only return entries that modified the buffer.
	*/
	public static function command_history(index:Int, ?modifying_only:Bool):Tup3<String, Dict<TODO, TODO>, Int>;

	// int	Returns the current change count. Each time the buffer is modified, the change count is incremented. The change count can be used to determine if the buffer has changed since the last it was inspected.
	public static function change_count():Int;
	
	// bool	Folds the given region/s, returning False if it was already folded
	@:overload(function (region:Region):Bool {})
	public static function fold(regions:Array<Region>):Bool;
	
	
	
	// [regions]	Unfolds all text in the region/s, returning the unfolded regions
	@:overload(function (region:Region):Array<Region> {})
	public static function unfold(regions:Array<Region>):Array<Region>;
	
	// String	Returns the encoding currently associated with the file
	public static function encoding():String;
	
	// None	Applies a new encoding to the file. This encoding will be used the next time the file is saved.
	public static function set_encoding(encoding:String):Void;
	
	// String	Returns the line endings used by the current file.
	public static function line_endings():String;
	
	// None	Sets the line endings that will be applied when next saving.
	public static function set_line_endings(line_endings:String):Void;
	
	// Bool	Returns the overwrite status, which the user normally toggles via the insert key.
	public static function overwrite_status():Bool;
	
	// None	Sets the overwrite status.
	public static function set_overwrite_status(enabled:Bool):Void;
	
	// [(Region, String)]	Extract all the symbols defined in the buffer.
	public static function symbols(line_endings:String):Array<Tup2<Region, String>>;
	
	/*
		Shows a pop up menu at the caret, to select an item in a list. on_done will be called once, with the index of the selected item. If the pop up menu was cancelled, on_done will be called with an argument of -1. Items is an array of strings.

		Flags currently only has no option.

		
	*/
	public static function show_popup_menu(items:Array<String>, on_done:Int->Void, ?flags:Int):Void;
}