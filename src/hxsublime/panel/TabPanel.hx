package hxsublime.panel;

import hxsublime.panel.Tools;
import hxsublime.tools.ViewTools;
import sublime.Edit;
import sublime.Sublime;
import sublime.View;
import sublime.Window;

class TabPanel {
	
	public var win:Window;
	public var output_view:View;
	public var output_view_id:Int;
	public var all:Array<String>;
	public var panel_name:String;
	public var panel_syntax:String;


	public function new (win:Window, panel_name = "Haxe Output", panel_syntax = "Packages/Haxe/Haxe.tmLanguage") 
	{
		this.win = win;
		this.output_view = null;
		this.output_view_id = null;
		this.all = [];
		this.panel_name = panel_name;
		this.panel_syntax = panel_syntax;
	}

	public function clear() 
	{
		
	}

	public function write (msg:String, scope:String = null, show_timestamp=true):Void {
		
		function f () 
		{
			var max = Std.int(Math.max(this.all.length, 300));
			this.all = [for (i in 0...max) this.all[i]];
			
			var msg1 = if (show_timestamp) Tools.timestamp_msg(msg) else msg;
			
			if (Tools.valid_message(msg)) {
				this.all = [msg1].concat(all);

				var v = this.output_view;

				if (v == null) 
				{
					v = ViewTools.find_view_by_name(this.panel_name);
					
					if (v == null) 
					{
						v = make_tab_panel(this.win, this.panel_name, this.panel_syntax);
						ViewTools.replaceContent(v, this.all.join(""));
					}

					this.output_view = v;
					this.output_view_id = v.id();
				}

				if (v != null) 
				{
					function do_edit(v:View, edit:Edit) 
					{
						v.insert(edit, 0, msg1);
					}
					ViewTools.asyncEdit(v, do_edit);
				}
			}
		}

		Sublime.set_timeout(f,40);
	}

	
	public function writeln (msg:String, scope:String = null, show_timestamp=true):Void
	{
		this.write(msg + "\n");
	}

	
	public function status (title:String, msg:String):Void
	{
		
		if (Tools.valid_message(msg)) {
			this.writeln(title + ": " + msg);
		}
	}

	public static function make_tab_panel (win:Window, name:String, syntax:String) 
	{
		var active = win.active_view();
		var v = win.new_file();
		v.set_name(name);
		//v.set_read_only(true)
		v.settings().set('word_wrap', true);
		
		v.settings().set("result_file_regex", Tools.haxe_file_regex());
		//v.settings().set("result_line_regex", _haxe_file_regex())
		v.settings().set("haxe_panel_win_id", win.id());
		v.set_scratch(true);
		v.set_syntax_file(syntax);
		// always create the output panels on the last group (nicer)
		var last_group = win.num_groups()-1;
		win.set_view_index(v, last_group, 0);
		// restore old focus
		win.focus_view(active);
		return v;
	}
}

/*

import sublime

from haxe.tools import viewtools

from haxe.panel import tools as paneltools

from haxe.tools.stringtools import encode_utf8,to_unicode, st2_encode_utf8, st3_encode_utf8





*/