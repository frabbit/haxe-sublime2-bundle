
package sublime;

private typedef TODO = Dynamic;

class EventListener {

	// Called when a new buffer is created.
	public function on_new(view:View):Void;
	
	// Called when a new buffer is created. Runs in a separate thread, and does not block the application.
	public function on_new_async(view:View):Void;
	
	// Called when a view is cloned from an existing one.
	public function on_clone(view:View):Void;
	
	// Called when a view is cloned from an existing one. Runs in a separate thread, and does not block the application.
	public function on_clone_async(view:View):Void;
	
	// Called when the file is finished loading.
	public function on_load(view:View):Void;
	
	// Called when the file is finished loading. Runs in a separate thread, and does not block the application.
	public function on_load_async(view:View):Void;
	
	// Called when a view is about to be closed. The view will still be in the window at this point.
	public function on_pre_close(view:View):Void;
	
	// Called when a view is closed (note, there may still be other views into the same buffer).
	public function on_close(view:View):Void;
	
	// Called just before a view is saved.
	public function on_pre_save(view:View):Void;
	
	// Called just before a view is saved. Runs in a separate thread, and does not block the application.
	public function on_pre_save_async(view:View):Void;
	
	// Called after a view has been saved.
	public function on_post_save(view:View):Void;
	
	// Called after a view has been saved. Runs in a separate thread, and does not block the application.
	public function on_post_save_async(view:View):Void;
	
	// Called after changes have been made to a view.
	public function on_modified(view:View):Void;
	
	// Called after changes have been made to a view. Runs in a separate thread, and does not block the application.
	public function on_modified_async(view:View):Void;
	
	// Called after the selection has been modified in a view.
	public function on_selection_modified(view:View):Void;
	
	// Called after the selection has been modified in a view. Runs in a separate thread, and does not block the application.
	public function on_selection_modified_async(view:View):Void;
	
	// Called when a view gains input focus.
	public function on_activated(view:View):Void;
	
	// Called when a view gains input focus. Runs in a separate thread, and does not block the application.
	public function on_activated_async(view:View):Void;
	
	// Called when a view loses input focus.
	public function on_deactivated(view:View):Void;
	
	// Called when a view loses input focus. Runs in a separate thread, and does not block the application.
	public function on_deactivated_async(view:View):Void;
	
	// Called when a text command is issued. The listener may return a (command, arguments) tuple to rewrite the command, or None to run the command unmodified.
	// returns 	(new_command_name, new_args)
	public function on_text_command(view, command_name, args):Tup2<String, TODO>
	
	// Called when a window command is issued. The listener may return a (command, arguments) tuple to rewrite the command, or None to run the command unmodified.
	// returns 	(new_command_name, new_args)	
	public function on_window_command(window, command_name, args):Tup2<String, TODO>
	
	// Called after a text command has been executed.
	public function post_text_command(view, command_name, args):Void;
	
	// Called after a window command has been executed.
	public function post_window_command(window, command_name, args):Void;

	
	public function on_query_context(view, key, operator, operand, match_all):Void;


}