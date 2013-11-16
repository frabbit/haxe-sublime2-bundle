
package sublime;

import python.lib.Builtin;
import sublime.Region;

import python.lib.Types;

extern class Selection implements ArrayAccess<Region> {

	// None	Removes all regions.
	public function clear():Void;
	// None	Adds the given region. It will be merged with any intersecting regions already contained within the set.
	public function add(region:Region):Void;
	// None	Adds all regions in the given set.
	public function add_all(region_set:Set<Region>):Void;
	// None	Subtracts the region from all regions in the set.
	public function subtract(region:Region):Void;
	// 	bool	Returns true iff the given region is a subset.
	public function contains(region:Region):Bool;


	public var length(get_length, null):Int;

	private inline function get_length():Int {
		return Builtin.len( (this:Dynamic) );
	}

	static function __init__ ():Void {
		python.Macros.importFromAs("sublime", "Selection", "sublime.Selection");
	}

}