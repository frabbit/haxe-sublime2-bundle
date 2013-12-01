package hxsublime.panel;

import hxsublime.panel.Tools;
import hxsublime.tools.ViewTools;
import python.lib.Types.Dict;
import sublime.Edit;
import sublime.Region;
import sublime.View;
import sublime.Window;


class SlidePanel 
{
	
	var win:Window;
	public var outputView:View;
	public var outputViewId:Int;

	public function new (win:Window) 
	{
		this.win = win;
		this.outputView = null;
	}

	public function clear() 
	{
		this.outputView = this.win.create_output_panel("haxe");
	}

	public function write( text :String , scope:String = null, show_timestamp = true ) 
	{
		
		var win = this.win;

		if (this.outputView == null) 
		{
			this.outputView = win.create_output_panel("haxe");
		}

		this.outputView.settings().set("result_file_regex", Tools.haxeFileRegex());
		// force result buffer
		win.create_output_panel("haxe");
		
		var panel = this.outputView;
		
		if (show_timestamp) 
		{
			text = Tools.timestampMsg(text);
		}
		
		win.run_command("show_panel",Dict.fromObject({"panel":"output.haxe"}));
		
		function do_edit(v:View, edit:Edit):Void 
		{
			var region = new Region(v.size(),v.size() + text.length);
			v.insert(edit, v.size(), text);
			
			
			if (scope != null) 
			{
				var icon = "dot";
				var key = "haxe-" + scope;
				var regions = v.get_regions( key );
				regions.push(region);
				v.add_regions( key , regions , scope , icon );
			}

			// set seletion to the begin of the document, allows navigating
			// through errors from the start
			v.sel().clear();
			v.sel().add(new Region(0,0));

			//region = sublime.Region(v.size()+1000, v.size()+1000)
			//sublime.set_timeout(lambda:v.show(region), 800)
		}
		
		ViewTools.asyncEdit(panel, do_edit);

		return panel;
	}

	public function writeln (msg:String, scope = null, show_timestamp = true) 
	{
		if (Tools.isValidMessage(msg))
		{
			this.write(msg + "\n", scope, show_timestamp);
		}
	}

	public function status (title:String, msg:String) 
	{
		if (Tools.isValidMessage(msg))
		{
			this.writeln(title + ": " + msg);
		}
	}
}
