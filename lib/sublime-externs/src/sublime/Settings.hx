
package sublime;


@:pythonImport("sublime", "Settings")
extern class Settings {


	public function get<T>(name:String, ?def:T):T;	//Returns the named setting, or default if it's not defined.
	public function set(name:String, value:Dynamic):Void;	//Sets the named setting. Only primitive types, lists, and dictionaries are accepted.
	public function erase(name:String):Void;	//Removes the named setting. Does not remove it from any parent Settings.
	public function has(name:String):Bool;	//Returns true iff the named option exists in this set of Settings or one of its parents.
	public function add_on_change(key:String, on_change:Void->Void):Void;	//None	Register a callback to be run whenever a setting in this object is changed.
	public function clear_on_change(key:String):Void;	//Remove all callbacks registered with the given key.

}