package hxsublime.panel;

import sublime.Window;


class SlidePanel 
{
	
	public function new (win:Window) 
	{
		this.win = win;
		this.output_view = null;
	}

	public function clear() 
	{
		this.output_view = this.win.get_output_panel("haxe")
	}

	public function write( text :String , scope:String = null, show_timestamp = true ) 
	{
		
		var win = this.win;

		if (this.output_view == null) 
		{
			this.output_view = win.get_output_panel("haxe");
		}

		this.output_view.settings().set("result_file_regex", haxe_file_regex());
		// force result buffer
		win.get_output_panel("haxe");
		
		panel = this.output_view;
		
		if (show_timestamp) 
		{
			text = timestamp_msg(text);
		}
		
		win.run_command("show_panel",{"panel":"output.haxe"})
		
		function do_edit(v, edit) 
		{
			region = sublime.Region(v.size(),v.size() + len(text))
			v.insert(edit, v.size(), text)
			v.end_edit( edit )
			
			if (scope != null) 
			{
				icon = "dot"
				key = "haxe-" + scope
				regions = v.get_regions( key );
				regions.append(region)
				v.add_regions( key , regions , scope , icon )
			}

			// set seletion to the begin of the document, allows navigating
			// through errors from the start
			v.sel().clear()
			v.sel().add(sublime.Region(0))

			//region = sublime.Region(v.size()+1000, v.size()+1000)
			//sublime.set_timeout(lambda:v.show(region), 800)
		}
		
		viewtools.async_edit(panel, do_edit);

		return panel;
	}

	public function writeln (msg:String, scope = null, show_timestamp = true) 
	{
		if (valid_message(msg))
		{
			this.write(msg + "\n", scope, show_timestamp);
		}
	}

	public function status (title:String, msg:String) 
	{
		if (valid_message(msg))
		{
			this.writeln(title + ": " + msg);
		}
	}
}

/*
import sublime

from haxe.tools import viewtools

from haxe.panel.tools import valid_message, haxe_file_regex, timestamp_msg

*/