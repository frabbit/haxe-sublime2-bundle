
package sublime;

import python.Tuple;
import python.Dict;

@:pythonImport("sublime", "Window")
extern class Window {

	// 	int	Returns a number that uniquely identifies this window.
	public function id():Int;
	// 	View	Creates a new file. The returned view will be empty, and its is_loaded method will return True.
	public function new_file():View;
	/*
	View	Opens the named file, and returns the corresponding view. If the file is already opened, it will be brought to the front. Note that as file loading is asynchronous, operations on the returned view wont be possible until its is_loading() method returns False.
	The optional flags parameter is a bitwise combination of:

	sublime.ENCODED_POSITION. Indicates the file_name should be searched for a :row or :row:col suffix
	sublime.TRANSIENT. Open the file as a preview only: it wont have a tab assigned it until modified
	*/
	public function open_file(file_name:String, ?flags:Int):View;
	// View	Finds the named file in the list of open files, and returns the corresponding View, or None if no such file is open.
	public function find_open_file(file_name:String):View;
	// View	Returns the currently edited view.
	public function active_view():View;
	// View	Returns the currently edited view in the given group.
	public function active_view_in_group(group:Int):View;
	// 	[View]	Returns all open views in the window.
	public function views():Array<View>;
	// 	[View]	Returns all open views in the given group.
	public function views_in_group(group:Int):Array<View>;
	// int	Returns the number of view groups in the window.
	public function num_groups():Int;
	// int	Returns the index of the currently selected group.
	public function active_group():Int;
	// None	Makes the given group active.
	public function focus_group(group:Int):Void;
	// None	Switches to the given view.
	public function focus_view(view:View):Void;
	// 	(group, index)	Returns the group, and index within the group of the view. Returns -1 if not found.
	public function get_view_index(view:View):Tuple2<Int, Int>;
	// None	Moves the view to the given group and index.
	public function set_view_index(view:View, group:Int, index:Int):Void;
	// 	[String]	Returns a list of the currently open folders.
	public function folders():Array<String>;
	// String	Returns name of the currently opened project file, if any.
	public function project_file_name():String;

	// Dictionary	Returns the project data associated with the current window. The data is in the same format as the contents of a .sublime-project file.
	public function project_data():Dict<String, Dynamic>;
	// 	None	Updates the project data associated with the current window.
	// If the window is associated with a .sublime-project file, the project file will be updated on disk, otherwise the window will store the data internally.
	public function set_project_data(data:Dict<String,Dynamic>):Void;
	// None	Runs the named Command with the (optional) given arguments. Window.run_command is able to run both any sort of command, dispatching the command via input focus.

	// TODO

	public function run_command(string:String, ?args:Dict<String, Dynamic>):Void;
	/*
	None	Shows a quick panel, to select an item in a list. on_done will be called once, with the index of the selected item. If the quick panel was cancelled, on_done will be called with an argument of -1.
	Items may be an array of strings, or an array of string arrays. In the latter case, each entry in the quick panel will show multiple rows.

	Flags currently only has one option, sublime.MONOSPACE_FONT

	on_highlighted, if given, will be called every time the highlighted item in the quick panel is changed.
	*/
	@:overload(function (items:Array<Array<String>>, on_done:Int->Void, ?flags:Int, ?selected_index:Int, ?on_highlighted:Int->Void):Void {})
	@:overload(function (items:Array<Tuple2<String, String>>, on_done:Int->Void, ?flags:Int, ?selected_index:Int, ?on_highlighted:Int->Void):Void {})
	public function show_quick_panel(items:Array<String>, on_done:Int->Void, ?flags:Int, ?selected_index:Int, ?on_highlighted:Int->Void):Void;
	// Shows the input panel, to collect a line of input from the user.
	// on_done and on_change, if not None, should both be functions that expect a single string argument.
	// on_cancel should be a function that expects no arguments. The view used for the input widget is returned.
	public function show_input_panel(caption:String, initial_text:String, on_done:String->Void, on_change:String->Void, on_cancel:Void->Void):View;

	public function create_output_panel(name:String):View; //	View	Returns the view associated with the named output panel, created it if required. The output panel can be shown by running the show_panel window command, with the panel argument set to the name with an "output." prefix.
	//public function lookup_symbol_in_index(symbol)	[Location]	Returns all locations where the symbol is defined across files in the current project.
	//public function lookup_symbol_in_open_files(symbol)	[Location]	Returns all locations where the symbol is defined across open files.


}