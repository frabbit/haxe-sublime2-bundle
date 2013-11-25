package hxsublime;

import python.lib.os.Path;
import python.lib.Types.Tup2;
import sublime.Settings;
import sublime.Sublime;
import sublime.View;



class Settings 
{
	public static function plugin_settings():sublime.Settings 
	{
		return Sublime.load_settings('Haxe.sublime-settings');
	}


	public static function get_from_settings(id:String, settings:sublime.Settings, plugin:Bool) 
	{
		var prefix = if (plugin) "plugin_" else "";
		var res = null;
		var pf = Sublime.platform();
		if (settings.has(prefix + id + "_" + pf)) 
		{
			res = settings.get(prefix + id + "_" + pf);
		}
		if (res == null && settings.has(prefix + id)) 
		{
			res = settings.get(prefix + id);
		}
		return res;
	}

	public static function get (id:String, view:View = null):Dynamic
	{
		if (view == null) 
		{
			var win = Sublime.active_window();
			if (win != null) 
			{
				view = Sublime.active_window().active_view();
			}
		}

		var res = null;
		if (view != null) 
		{
			var settings = view.settings();
			res = get_from_settings(id, settings, false);
		}

		if (res == null) 
		{
			res = get_from_settings(id, plugin_settings(), true);
		}
			
		return res;
	}

	public static function get_bool (id:String, defaultVal:Bool, view:View = null):Bool
	{
		var r = get(id, view);
		if (r == null) 
		{
			return defaultVal;
		}
		else 
		{
			
			if (Std.is(r, Bool))
			{
				return r;
			}
			else 
			{
				return null;
			}
		}
	}


	public static function get_int (id:String, defaultVal:Int, view = null):Int {
		var r = get(id, view);
		if (r == null) {
			return defaultVal;
		}
		else {
			if (Std.is(r, Int)) 
			{
				return r;
			}
			else {
				return null;
			}
		}
	}

	public static function get_string (id:String, defaultVal:String, view = null):String {
		var r = get(id, view);
		if (r == null) {
			return defaultVal;
		}
		else {
			if (Std.is(r, String)) {
				return r;
			}
			else {
				return null;
			}
		}
	}

	public static function no_fuzzy_completion (view:View = null) 
	{
		return get_bool("haxe_completion_no_fuzzy", false, view);
	}

	public static function top_level_completions_on_demand (view:View = null) 
	{
		return get_bool("haxe_completions_top_level_only_on_demand", false, view);
	}

	public static function show_only_async_completions (view:View = null) 
	{
		return get_bool("haxe_completions_show_only_async", true, view);
	}

	public static function is_async_completion (view:View = null) 
	{

		var r = get_bool("haxe_completion_async", true, view);

		trace("AAAAAASYNC:" + r);
		return r;
	}

	public static function get_completion_delays (view:View = null) 
	{
		return Tup2.create(
			get_int("haxe_completion_async_timing_hide", 60, view),
			get_int("haxe_completion_async_timing_show", 150, view)
		);
	}


	public static function show_completion_times (view:View = null) 
	{
		return get_bool("haxe_completion_show_times", false, view);
	}


	public static function haxe_exec (view:View = null) 
	{
		return get_string("haxe_exec", "haxe", view);
	}

	public static function use_haxe_servermode(view:View = null) 
	{
		return get_bool("haxe_use_servermode", true, view);
	}

	public static function use_haxe_servermode_wrapper (view:View = null) 
	{
		return get_bool("haxe_use_servermode_wrapper", false, view);
	}

	public static function haxe_sdk_path (view:View = null) 
	{
		return get_string("haxe_sdk_path", null, view);
	}

	public static function open_with_default_app(view:View = null) 
	{
		return get_string("haxe_open_with_default_app", null, view);
	}

	public static function haxe_inst_path (view:View = null) 
	{
		var tmp = haxe_sdk_path(view);
		var defaultVal = if (tmp != null) (Path.normpath(haxe_sdk_path(view)) + Path.sep + "haxe") else null;
		if (tmp == null && haxe_exec(view) != "haxe") 
		{
			defaultVal = (Path.normpath(Path.dirname(haxe_exec(view))));
		}
		
		return get_string("haxe_inst_path", defaultVal, view);
	}

	public static function neko_inst_path (view:View = null) 
	{
		var tmp = haxe_sdk_path(view);
			
		var defaultVal = if (tmp != null) (Path.normpath(haxe_sdk_path(view)) + Path.sep + "default") else null;
		return get_string("neko_inst_path", defaultVal, view);
	}

	public static function haxe_library_path (view:View = null) 
	{
		return get_string("haxe_library_path", null, view);
	}
		
	public static function haxelib_exec (view:View = null) 
	{
		return get_string("haxe_haxelib_exec", "haxelib", view);
	}
		
	public static function smart_snippets (view:View = null) 
	{
		return get_bool("haxe_completion_smart_snippets", true, view);
	}

	public static function smart_snippets_on_completion (view:View = null) 
	{
		return get_bool("haxe_completion_smart_snippets_on_completion", false, view);
	}

	public static function smart_snippets_just_current (view:View = null) 
	{
		return get_bool("haxe_completion_smart_snippets_just_current", false, view);
	}

	public static function use_debug_panel (view:View = null) 
	{
		return get_bool("haxe_use_debug_panel", false, view);
	}

	public static function check_on_save (view:View = null) 
	{
		return get_bool("haxe_check_on_save", true, view);
	}

	public static function use_slide_panel (view:View = null) 
	{
		return get_bool("haxe_use_slide_panel", true, view);
	}

	public static function use_haxe_servermode_for_builds(view:View = null) 
	{
		return get_bool("haxe_use_servermode_for_builds", false, view);
	}

	public static function use_offset_completion(view:View = null) 
	{
		return get_bool("haxe_use_offset_completion", false, view);
	}
}

/*
import sublime
import os

from haxe.plugin import is_st2





*/