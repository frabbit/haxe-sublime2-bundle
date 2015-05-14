package hxsublime;

import python.lib.os.Path;
import python.Tuple.Tuple2;
import sublime.Settings;
import sublime.Sublime;
import sublime.View;

class Settings
{
	public static function pluginSettings():sublime.Settings
	{
		return Sublime.load_settings('Haxe.sublime-settings');
	}

	public static function getFromSettings(id:String, settings:sublime.Settings, plugin:Bool)
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
			res = getFromSettings(id, settings, false);
		}

		if (res == null)
		{
			res = getFromSettings(id, pluginSettings(), true);
		}

		return res;
	}

	public static function getBool (id:String, defaultVal:Bool, view:View = null):Bool
	{
		var r = get(id, view);
		return 
			if (r == null) defaultVal
			else if (Std.is(r, Bool)) r
			else defaultVal;
	}


	public static function getInt (id:String, defaultVal:Int, view = null):Int
	{
		var r = get(id, view);
		return 
			if (r == null) defaultVal
			else if (Std.is(r, Int)) r
			else defaultVal;
	}

	public static function getString (id:String, defaultVal:String, view = null):String
	{
		var r = get(id, view);
		return 
			if (r == null) defaultVal
			else if (Std.is(r, String)) r
			else defaultVal;
	}

	public static function noFuzzyCompletion (view:View = null)
	{
		return getBool("haxe_completion_no_fuzzy", false, view);
	}

	public static function topLevelCompletionsOnDemand (view:View = null)
	{
		return getBool("haxe_completions_top_level_only_on_demand", false, view);
	}

	public static function showOnlyAsyncCompletions (view:View = null)
	{
		return getBool("haxe_completions_show_only_async", true, view);
	}

	public static function isAsyncCompletion (view:View = null)
	{
		return getBool("haxe_completion_async", true, view);
	}

	public static function getCompletionDelays (view:View = null)
	{
		return Tuple2.make(
			getInt("haxe_completion_async_timing_hide", 60, view),
			getInt("haxe_completion_async_timing_show", 150, view)
		);
	}

	public static function showCompletionTimes (view:View = null)
	{
		return getBool("haxe_completion_show_times", false, view);
	}


	public static function haxeExec (view:View = null)
	{
		return getString("haxe_exec", "haxe", view);
	}

	public static function useHaxeServermode(view:View = null)
	{
		return getBool("haxe_use_servermode", true, view);
	}

	public static function useHaxeServermodeWrapper (view:View = null)
	{
		return getBool("haxe_use_servermode_wrapper", false, view);
	}

	public static function haxeSdkPath (view:View = null)
	{
		return getString("haxe_sdk_path", null, view);
	}

	public static function openWithDefaultApp(view:View = null)
	{
		return getString("haxe_open_with_default_app", null, view);
	}

	public static function haxeInstPath (view:View = null)
	{
		var tmp = haxeSdkPath(view);
		var defaultVal = if (tmp != null) (Path.normpath(haxeSdkPath(view)) + Path.sep + "haxe") else null;
		if (tmp == null && haxeExec(view) != "haxe")
		{
			defaultVal = (Path.normpath(Path.dirname(haxeExec(view))));
		}

		return getString("haxe_inst_path", defaultVal, view);
	}

	public static function nekoInstPath (view:View = null)
	{
		var tmp = haxeSdkPath(view);

		var defaultVal = if (tmp != null) (Path.normpath(haxeSdkPath(view)) + Path.sep + "default") else null;
		return getString("neko_inst_path", defaultVal, view);
	}

	public static function haxeLibraryPath (view:View = null)
	{
		return getString("haxe_library_path", null, view);
	}

	public static function haxelibExec (view:View = null)
	{
		return getString("haxe_haxelib_exec", "haxelib", view);
	}

	public static function smartSnippets (view:View = null)
	{
		return getBool("haxe_completion_smart_snippets", true, view);
	}

	public static function smartSnippetsOnCompletion (view:View = null)
	{
		return getBool("haxe_completion_smart_snippets_on_completion", false, view);
	}

	public static function smartSnippetsJustCurrent (view:View = null)
	{
		return getBool("haxe_completion_smart_snippets_just_current", false, view);
	}

	public static function checkOnSave (view:View = null)
	{
		return getBool("haxe_check_on_save", true, view);
	}

	public static function useSlidePanel (view:View = null)
	{
		return getBool("haxe_use_slide_panel", true, view);
	}

	public static function useHaxeServermodeForBuilds(view:View = null)
	{
		return getBool("haxe_use_servermode_for_builds", false, view);
	}

	public static function useOffsetCompletion(view:View = null)
	{
		return getBool("haxe_use_offset_completion", false, view);
	}
}
