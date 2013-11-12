package hxsublime;

import hxsublime.panel.Base.Panels;
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

class HaxeImportGenerator {
	public static function generate_using (view:View, edit:Edit) {
		var p = new HaxeImportGenerator(Panels.default_panel(), view);
		return p.generate_statement(edit, "using", HxRegex.using_line);
	}

	public static function generate_import (view:View, edit:Edit) {
		var p = new HaxeImportGenerator(Panels.default_panel(), view);
		return p.generate_statement(edit, "import", HxRegex.import_line);
	}

	var panel:Panel;
	var start:Int;
	var size:Int;
	var cname:Tup3<String, String, String>;
	public var view : View;

	public function new (panel, view:View){
		trace( "construct");
		this.view = view;
		trace(Std.string(this.view));
		this.panel = panel;
		this.start = null;
		this.size = null;
		this.cname = null;
	}
		
	public function _get_end( src:String, offset:Int ) {
		var end = src.length;
		while (offset < end) {
			var c = src.charAt(offset);
			offset += 1;
			if (HxRegex.word_chars.match(c) == null) break;
		}
		return offset - 1;
	}

	public function _get_start( src:String, offset:Int ) {
		var found_word = 0;
		offset -= 1;
		while (offset > 0) {
			var c = src.charAt(offset);
			offset -= 1;
			if (found_word == 0) {
				if (HxRegex.space_chars.match(c) != null) continue;
				found_word = 1;
			}
			if (HxRegex.word_chars.match(c) == null) break;
		}

		return offset + 2;
	}
	
	public function _is_membername( token:String ) {
		return token.charAt(0) >= "Z" || token == token.toUpperCase();
	}

	// public function is_module( this , token ) {
	//	return re.search("[\.^][A-Z]+", token);

	public function _get_classname( view:View, src:String ) 
	{
		var loc = view.sel()[0];
		var end = Builtin.max(loc.a, loc.b);
		this.size = loc.size();
		if (this.size == 0) {
			end = this._get_end(src, end);
			this.start = this._get_start(src, end);
			this.size = end - this.start;
		}
		else {
			this.start = end - this.size;
		}

		this.cname = view.substr( new Region(this.start, end)).rpartition(".");

		while (!(this.cname._1 == "") && this._is_membername(this.cname._3)) {
			this.size -= 1 + this.cname._3.length;
			this.cname = this.cname._1.rpartition(".");
		}

		return this.cname;
	}

	public function _compact_classname( edit:Edit, view:View ) 
	{
		view.replace(edit, new Region(this.start, this.start+this.size), this.cname._3);
		view.sel().clear();
		var loc = this.start + this.cname._3.length;
		view.sel().add( new Region(loc, loc));
	}

	public function _get_indent( src:String, index:Int ):Int {
	
		if (src.charAt(index) == "\n") return index + 1;
		return index;
	}

	public function _insert_statement( edit, view, src, statement, regex:Regex) 
	{
		var cname = this.cname._1 + this.cname._2 + this.cname._3;
		var clow = cname.toLowerCase();
		var last = null;

		for (imp in regex.finditer(src)) {
			if (clow < imp.group(2).toLowerCase()) {
				var ins = "{0}{1} {2};\n".format([imp.group(1), statement, cname]);
				view.insert(edit, this._get_indent(src, imp.start(0)), ins);
				return;
			}
			last = imp;
		}

		if (last != null) {
			var ins = ";\n{0}{1} {2}".format([last.group(1), statement, cname]);
			view.insert(edit, last.end(2), ins);
		}
		else {
			var pkg = HxRegex.package_line.search(src);
			if (pkg != null) {
				var ins = "\n\n{0} {1};".format([statement, cname]);
				view.insert(edit, pkg.end(0), ins);
			}
			else {
				var ins = "{0} {1};\n\n".format([statement, cname]);
				view.insert(edit, 0, ins);
			}
		}
	}


	public function generate_statement( edit:Edit, statement:String, regex:Regex ) 
	{
		var view = this.view;
		var src = view.substr( new Region(0, view.size()));
		var cname = this._get_classname(view, src);
		
		if (cname._2 == "" && statement == "import") {
			Sublime.status_message("Nothing to " + statement);
			this.panel.writeln("Nothing to " + statement);
			return;
		}

		this._compact_classname(edit, view);

		var fcname = cname._1 + cname._2 + cname._3;
		if (Re.search((statement + "\\s+${fcname};"), src) != null) {
			var info = if (statement == "import") "imported" else "used";
			Sublime.status_message("Already " + info);
			this.panel.writeln("Already " + info);
			return;
		}
		 
		this._insert_statement(edit, view, src, statement, regex);
	}
}
/*
import sublime
import re

from haxe import panel as hxpanel
from haxe.tools import hxsrctools

from haxe.log import log





// TODO clean up this class, it's really dirty

class HaxeImportGenerator:

	

*/