
package sublime;

extern class Region {
	//	Creates a Region with initial values a and b.
	public function new (a:Int, b:Int):Void;

	
	// 	int	The first end of the region.
	public var a(default, null):Int;
	// 	int	The second end of the region. May be less that a, in which case the region is a reversed one.
	public var b(default, null):Int;
	// 	int	The target horizontal position of the region, or -1 if undefined. Effects behavior when pressing the up or down keys.
	public var xpos(default, null):Int;

	// int	Returns the minimum of a and b.
	public function begin():Int;
	// int	Returns the maximum of a and b.
	public function end():Int;
	// int	Returns the number of characters spanned by the region. Always >= 0.
	public function size():Int;
	// bool	Returns true iff begin() == end().
	public function empty():Bool;
	// Region	Returns a Region spanning both this and the given regions.
	public function cover(region:Region):Region;
	// Region	Returns the set intersection of the two regions.
	public function intersection(region:Region):Region;
	// bool	Returns True iff this == region or both include one or more positions in common.
	public function intersects(region:Region):Bool;
	// bool	Returns True iff the given region is a subset.
	// bool	Returns True iff begin() <= point <= end().
	@:overload(function (point:Int):Bool {})
	public function contains(region:Region):Bool;
	

	static function __init__ ():Void {
		python.Macros.importFromAs("sublime", "Region", "sublime.Region");
	}

}