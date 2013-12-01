package hxsublime;

import hxsublime.panel.Panels;
import hxsublime.panel.Panel;
import python.lib.Builtin;
import python.lib.Re;
import python.lib.Re.Regex;
import python.lib.Types.Tup3;
import sublime.Edit;
import sublime.Region;
import sublime.Sublime;
import sublime.View;

import hxsublime.tools.HxSrcTools.Regex in HxRegex;

using python.lib.StringTools;

class HaxeImportGenerator 
{
	
	public static function generateUsing (view:View, edit:Edit) 
	{
		var p = new HaxeImportGenerator(Panels.defaultPanel(), view);
		return p.generateStatement(edit, "using", HxRegex.using_line);
	}

	public static function generateImport (view:View, edit:Edit) 
	{
		var p = new HaxeImportGenerator(Panels.defaultPanel(), view);
		return p.generateStatement(edit, "import", HxRegex.import_line);
	}

	var panel:Panel;
	var start:Int;
	var size:Int;
	var cname:Tup3<String, String, String>;
	

	var view : View;

	function new (panel, view:View)
	{
		this.view = view;
		this.panel = panel;
		this.start = null;
		this.size = null;
		this.cname = null;
	}
		
	function getEnd( src:String, offset:Int ) 
	{
		var end = src.length;
		while (offset < end) 
		{
			var c = src.charAt(offset);
			offset += 1;
			if (HxRegex.word_chars.match(c) == null) break;
		}
		return offset - 1;
	}

	function getStart( src:String, offset:Int ) 
	{
		var found_word = 0;
		offset -= 1;
		while (offset > 0) 
		{
			var c = src.charAt(offset);
			offset -= 1;
			if (found_word == 0) 
			{
				if (HxRegex.space_chars.match(c) != null) continue;
				found_word = 1;
			}
			if (HxRegex.word_chars.match(c) == null) break;
		}

		return offset + 2;
	}
	
	function isMemberName( token:String ) 
	{
		return token.charAt(0) >= "Z" || token == token.toUpperCase();
	}

	function getClassName( view:View, src:String ) 
	{
		var loc = view.sel()[0];
		var end = Builtin.max(loc.a, loc.b);
		this.size = loc.size();
		if (this.size == 0) 
		{
			end = this.getEnd(src, end);
			this.start = this.getStart(src, end);
			this.size = end - this.start;
		}
		else 
		{
			this.start = end - this.size;
		}

		this.cname = view.substr( new Region(this.start, end)).rpartition(".");

		while (!(this.cname._1 == "") && this.isMemberName(this.cname._3)) 
		{
			this.size -= 1 + this.cname._3.length;
			this.cname = this.cname._1.rpartition(".");
		}

		return this.cname;
	}

	function compactClassName( edit:Edit, view:View ) 
	{
		view.replace(edit, new Region(this.start, this.start+this.size), this.cname._3);
		view.sel().clear();
		var loc = this.start + this.cname._3.length;
		view.sel().add( new Region(loc, loc));
	}

	function getIndent( src:String, index:Int ):Int 
	{
	
		if (src.charAt(index) == "\n") return index + 1;
		return index;
	}

	function insertStatement( edit, view, src, statement, regex:Regex) 
	{
		var cname = this.cname._1 + this.cname._2 + this.cname._3;
		var clow = cname.toLowerCase();
		var last = null;

		for (imp in regex.finditer(src).toHaxeIterator()) 
		{
			if (clow < imp.group(2).toLowerCase()) 
			{
				var ins = "{0}{1} {2};\n".format([imp.group(1), statement, cname]);
				view.insert(edit, this.getIndent(src, imp.start(0)), ins);
				return;
			}
			last = imp;
		}

		if (last != null) 
		{
			var ins = ";\n{0}{1} {2}".format([last.group(1), statement, cname]);
			view.insert(edit, last.end(2), ins);
		}
		else 
		{
			var pkg = HxRegex.package_line.search(src);
			if (pkg != null) 
			{
				var ins = "\n\n{0} {1};".format([statement, cname]);
				view.insert(edit, pkg.end(0), ins);
			}
			else 
			{
				var ins = "{0} {1};\n\n".format([statement, cname]);
				view.insert(edit, 0, ins);
			}
		}
	}


	function generateStatement( edit:Edit, statement:String, regex:Regex ) 
	{
		var view = this.view;
		var src = view.substr( new Region(0, view.size()));
		var cname = this.getClassName(view, src);
		
		if (cname._2 == "" && statement == "import") 
		{
			Sublime.status_message("Nothing to " + statement);
			this.panel.writeln("Nothing to " + statement);
			return;
		}

		this.compactClassName(edit, view);

		var fcname = cname._1 + cname._2 + cname._3;
		
		if (Re.search(statement + "\\s+${fcname};", src) != null) 
		{
			var info = if (statement == "import") "imported" else "used";
			Sublime.status_message("Already " + info);
			this.panel.writeln("Already " + info);
			return;
		}
		 
		this.insertStatement(edit, view, src, statement, regex);
	}
}
