package hxsublime.panel;

import haxe.ds.IntMap;
import haxe.ds.StringMap;
import hxsublime.Settings;
import hxsublime.tools.Cache;
import sublime.EventListener;
import sublime.Sublime;
import sublime.View;
import sublime.Window;



class PanelCloseListener extends EventListener 
{
	override public function on_close(view:View) 
	{
		var win = view.window();
		if (win == null) {
			win = Sublime.active_window();
		}
		
		var win_id = win.id();
		var view_id = view.id();

		if (Panels._slide_panel.exists(win_id)) 
		{
			var panel = Panels.slide_panel(win);
			if (panel.output_view != null && view_id == panel.output_view.id()) 
			{
				panel.output_view = null;
			}
		}

		var panel_win_id = view.settings().get("haxe_panel_win_id");
		if (panel_win_id != null) 
		{
			for (p in [Panels._tab_panel, Panels._debug_panel]) 
			{
				var panel = p.get_or_default(panel_win_id, null);
				if (panel != null && panel.output_view != null && view_id == panel.output_view_id) 
				{
					trace("panel safely removed");
					panel.output_view = null;
					panel.output_view_id = null;
				}
			}
		}
	}
}

class Panels {

	public static var _tab_panel = new Cache<Int, Panel>(new IntMap());
	public static var _debug_panel = new Cache<Int, Panel>(new IntMap());
	public static var _slide_panel = new IntMap<Panel>();

	public static function tab_panel(win:Window = null)
	{
		if (win == null) 
		{
			win = Sublime.active_window();
		}
		
		return _tab_panel.get_or_insert(win.id(), function ():Panel return new TabPanel(win, "Haxe Output"));
	}

	public static function debug_panel(win:Window = null)
	{
		if (win == null) 
		{
			win = Sublime.active_window();
		}
		return _debug_panel.get_or_insert(win.id(), function ():Panel return new TabPanel(win, "Haxe Plugin Debug Panel"));
	}

	public static function __slide_panel(win:Window = null)
	{
		return tab_panel(win);
	}

	public static function default_panel(win:Window = null):Panel
	{
		if (Settings.use_slide_panel()) 
		{
			return slide_panel(win);
		}
		else 
		{
			return tab_panel(win);
		}
	}

	public static function slide_panel(win:Window = null)
	{
		
		if (win == null) 
		{
			win = Sublime.active_window();
		}
		
		var win_id = win.id();
		
		if (!_slide_panel.exists(win_id)) 
		{
			_slide_panel.set(win_id, new SlidePanel(win));
		}
		return _slide_panel.get(win_id);
	}
}

/*
import sublime, sublime_plugin

from haxe import settings

from haxe.tools.cache import Cache
from haxe.trace import trace

from haxe.panel.slidepanel import SlidePanel
from haxe.panel.tabpanel import TabPanel





*/