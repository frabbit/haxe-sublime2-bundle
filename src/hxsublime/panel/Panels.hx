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

		if (Panels._slidePanels.exists(win_id)) 
		{
			var panel = Panels.slidePanel(win);
			if (panel.outputView != null && view_id == panel.outputView.id()) 
			{
				panel.outputView = null;
			}
		}

		var panel_win_id = view.settings().get("haxe_panel_win_id");
		if (panel_win_id != null) 
		{
			for (p in [Panels._debugPanels]) 
			{
				var panel = p.getOrDefault(panel_win_id, null);
				if (panel != null && panel.outputView != null && view_id == panel.outputViewId) 
				{
					trace("panel safely removed");
					panel.outputView = null;
					panel.outputViewId = null;
				}
			}
		}
	}
}

@:allow(hxsublime.panel)
class Panels 
{

	static var _debugPanels = new Cache<Int, Panel>(new IntMap());
	static var _slidePanels = new IntMap<Panel>();


	

	public static function defaultPanel(win:Window = null):Panel
	{
		return slidePanel(win);
	}

	public static function slidePanel(win:Window = null)
	{
		if (win == null) 
		{
			win = Sublime.active_window();
		}
		
		var win_id = win.id();
		
		if (!_slidePanels.exists(win_id)) 
		{
			_slidePanels.set(win_id, new SlidePanel(win));
		}
		return _slidePanels.get(win_id);
	}
}
