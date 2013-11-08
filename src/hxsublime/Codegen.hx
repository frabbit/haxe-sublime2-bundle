package hxsublime;

import python.lib.Re.Regex;
import sublime.Edit;
import sublime.View;


class HaxeImportGenerator {
	public static function generate_using (view:View, edit:Edit) {
		var p = HaxeImportGenerator(hxpanel.default_panel(), view);
		return p.generate_statement(edit, "using", hxsrctools.using_line);
	}

	public static function generate_import (view:View, edit:Edit) {
		var p = HaxeImportGenerator(hxpanel.default_panel(), view);
		return p.generate_statement(edit, "import", hxsrctools.import_line);
	}

	var panel;
	var start;
	var size;
	var cname:Array<String>;

	public function new (panel, view){
		trace( "construct");
		this.view = view;
		trace(Std.string(this.view));
		this.panel = panel;
		this.start = null;
		this.size = null;
		this.cname = null;
	}
		
	public function _get_end( src:String, offset:Int ) {
		var end = len(src);
		while (offset < end) {
			var c = src.charAt(offset);
			offset += 1;
			if (!hxsrctools.word_chars.match(c)) break;
		}
		return offset - 1;
	}

	public function _get_start( src, offset ) {
		var found_word = 0;
		offset -= 1;
		while (offset > 0) {
			var c = src.charAt(offset);
			offset -= 1;
			if (found_word == 0) {
				if (hxsrctools.space_chars.match(c)) continue;
				found_word = 1;
			}
			if (!hxsrctools.word_chars.match(c)) break;
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
		var end = max(loc.a, loc.b);
		this.size = loc.size();
		if (this.size == 0) {
			end = this._get_end(src, end);
			this.start = this._get_start(src, end);
			this.size = end - this.start;
		}
		else {
			this.start = end - this.size;
		}

		this.cname = view.substr(sublime.Region(this.start, end)).rpartition(".");

		while (!this.cname[0] == "" && this._is_membername(this.cname[2])) {
			this.size -= 1 + this.cname[2].length;
			this.cname = this.cname[0].rpartition(".");
		}

		return this.cname;
	}

	public function _compact_classname( edit:Edit, view:View ) 
	{
		view.replace(edit, sublime.Region(this.start, this.start+this.size), this.cname[2]);
		view.sel().clear();
		loc = this.start + len(this.cname[2]);
		view.sel().add(sublime.Region(loc, loc));
	}

	public function _get_indent( src:String, index:Int ):Int {
	
		if (src[index] == "\n") return index + 1;
		return index;
	}

	public function _insert_statement( edit, view, src, statement, regex) 
	{
		var cname = "".join(this.cname);
		var clow = cname.lower();
		var last = null;

		for (imp in regex.finditer(src)) {
			if (clow < imp.group(2).lower()) {
				ins = "{0}{1} {2};\n".format(imp.group(1), statement, cname);
				view.insert(edit, this._get_indent(src, imp.start(0)), ins);
				return;
			}
			last = imp;
		}

		if (last != null) {
			ins = ";\n{0}{1} {2}".format(last.group(1), statement, cname);
			view.insert(edit, last.end(2), ins);
		}
		else {
			var pkg = hxsrctools.package_line.search(src);
			if (pkg != null) {
				ins = "\n\n{0} {1};".format(statement, cname);
				view.insert(edit, pkg.end(0), ins);
			}
			else {
				ins = "{0} {1};\n\n".format(statement, cname);
				view.insert(edit, 0, ins);
			}
		}
	}


	public function generate_statement( edit:Edit, statement:String, regex:Regex ) 
	{
		var view = this.view;
		var src = view.substr(sublime.Region(0, view.size()));
		var cname = this._get_classname(view, src);
		
		if (cname[1] == "" && statement == "import") {
			sublime.status_message("Nothing to " + statement);
			this.panel.writeln("Nothing to " + statement);
			return;
		}

		this._compact_classname(edit, view);

		if (re.search((statement + "\\s+{0};").format("".join(cname)), src)) {
			info = if (statement == "import") "imported" else "used";
			sublime.status_message("Already " + info);
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