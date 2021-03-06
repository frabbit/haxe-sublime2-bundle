import sublime

def get (id, view = None):
	if view == None:
		win = sublime.active_window()
		if (win != None):
			view = sublime.active_window().active_view();

	res = None
	if (view != None):
		settings = view.settings()
		if settings.has(id):
			res = settings.get(id)
	return res;

def get_bool (id, default, view = None):
	r = get(id, view)
	if (r == None):
		return default
	else:
		if isinstance(r, bool):
			return r
		else :
			return None 


def get_int (id, default, view = None):
	r = get(id, view)
	if (r == None):
		return default
	else:
		if isinstance(r, int):
			return r
		else :
			return None 


def get_string (id, default, view = None):
	r = get(id, view)
	if (r == None):
		return default
	else:
		if isinstance(r, unicode):
			return r.decode("iso-8859-1")
		elif isinstance(r, str):
			return r
		else :
			return None



		

def no_fuzzy_completion (view = None):
	return get_bool("haxe_completion_no_fuzzy", False, view)

def top_level_completions_on_demand (view = None):
	return get_bool("haxe_completions_top_level_only_on_demand", False, view)

def only_delayed_completions (view = None):
	return get_bool("haxe_completions_only_delayed", True, view)

def is_delayed_completion (view = None):
	return get_bool("haxe_completion_delayed", True, view)

def get_completion_delays (view = None):
	return (
		get_int("haxe_completion_delayed_timing_hide", 60, view),
		get_int("haxe_completion_delayed_timing_show", 150, view)
	)


def show_completion_times (view = None):
	return get_bool("haxe_completion_show_times", False, view)


def haxe_exec (view = None):
	return get_string("haxe_exec", "haxe", view)

def haxe_library_path (view = None):
	res = get_string("haxe_library_path", None, view)
	return res
	

def haxelib_exec (view = None):
	return get_string("haxe_haxelib_exec", "haxelib", view)
	
def smart_snippets (view = None):
	return get_string("haxe_completion_smart_snippets", "no", view)	

def use_debug_panel (view = None):
	return get_bool("haxe_use_debug_panel", False, view)	

def build_on_save (view = None):
	return get_bool("haxe_build_on_save", True, view)

def use_slide_panel (view = None):
	return get_bool("haxe_use_slide_panel", True, view)	

def smarts_hints_only_next (view = None):
	return get_bool("haxe_smarts_hints_only_next", True, view)	
