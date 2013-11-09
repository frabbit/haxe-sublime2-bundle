package hxsublime.compiler;

import python.lib.Types.Exception;

class CompletionEntry {

	var hint:String;
	var insert:String;
	var doc:String;
	
	public function new(hint, insert, doc):
		this.hint = hint;
		this.insert = insert;
		this.doc = doc;
}

class Output {
	public static var compiler_output = Re.compile("^([^:]+):([0-9]+): (?:character(?:s?)|line(?:s?))? ([0-9]+)-?([0-9]+)? : (.*)", re.M);
	public static var no_classes_found = Re.compile("^No classes found in .*", re.M);
	public static var no_classes_found_in_trace = Re.compile("^No classes found in trace$", re.M);
	public static var haxe_compiler_line = "^([^:]*):([0-9]+): characters? ([0-9]+)-?[0-9]* :(.*)$";
	public static var type_parameter_name = Re.compile("^([A-Z][_a-zA-Z0-9]*)");

	public static function get_type_hint (types) {
		var hints = []
		for (i in types) {
			hint = i.text.strip();
			hint_types = hxsrctools.split_function_signature(hint);
			hints.push( hint_types );
		}
		return hints;
	}


	

	public static function get_function_type_params(name:String, signature_types:Array<String>) {

		var new_args = []
		var type_params = dict()
		var name_len = name.length;
		for (t in signature_types) {
			new_args.append("".join(t.split(name + ".")))
			while (true) {
				index = t.find(name)
				if (index == -1) break;
				type_start_index = index + name_len + 1
				t = t[type_start_index:]
				m = type_parameter_name.match(t)
				if (m != null) {
					param_name = m.group(1)
					type_params[param_name] = true
				}
				else {
					break;
				}
			}
		}

		type_param_list = list(reversed(list(type_params.keys())))
		return new_args, type_param_list
	}


	public static function completion_field_to_entry(name, sig, doc) {
		insert = name
		label = name
		
		smart_snippets = hxsettings.smart_snippets_on_completion()
		not_smart = not smart_snippets

		if (sig != null) {
			types = hxsrctools.split_function_signature(sig) 
			
			var r = get_function_type_params(name, types);
			var types = r._1, type_params = r._2;

			params_sig = ""

			if (len(type_params) > 0) {
				params_sig = "<" + ", ".join(type_params) + ">"
			}


			trace(Std.string(types))
			trace(Std.string(type_params))
			
			
			ret = types.pop()

			signature_separator = " : ";

			if( len(types) > 0 ) {
				
				if (len(types) == 1 and types[0] == "Void") {

					label = if (not_smart) (name + params_sig + "()" + signature_separator + ret) else (name + "()" + signature_separator+ ret)
					insert = if (not_smart) name  else "" + name + "${1:()}"
				}
				else {
					function escape_type (x) {
						return x.replace("}", "\}").replace("{", "\{")
					}

					params = "( " + types.join(", ") + " )"
					label = name + params_sig + params + signature_separator + ret
					
					//hint_to_long = is_st2 and len(label) > 40
					//if (hint_to_long) { // compact arguments
					//	label = hxsrctools.compact_func.sub("(...)", label);
					//}
					
					new_types = list(types)
					for (i in range(0, len(new_types))) {
						new_types[i] = "${" + Std.string(i+2) + ":" + escape_type(new_types[i]) + "}"
					}

					insert = if (not_smart) name else name + "${1:( " + new_types.join(", ") + " )}"
				}
			}
			else {
				label = name + params_sig + signature_separator + ret
			}
		}
		else {
			label = if (Re.match("^[A-Z]",name )) name + "\tclass" else name + "\tpackage"
		}
				
		
		//if is_st2 and len(label) > 40: # compact return type
		//	m = hxsrctools.compact_prop.search(label)
		//	if m != null:
		//		label = hxsrctools.compact_prop.sub(": " + m.group(1), label)
		
		var res = new CompletionEntry( label, insert, doc );

		return res
	}
			

	public static function collect_completion_fields (li) 
	{
		var comps = []
		if (li != null) {
			for (i in li.getiterator("i")) {
				name = i.get("n")
				sig = i.find("t").text
				doc = i.find("d").text // nothing to do
				entry = completion_field_to_entry(name, sig, doc)
				
				comps.append(entry)
			}
		}

		return comps;
	}


	public static function extract_errors( str:String ) 
	{
		errors = []
		
		//trace("error_str: |||" + str + "|||")
		// swallow no classes found in * errors where * could be trace or an unknown variable etc.
		if (no_classes_found.findall(str).length > 0) {
			//trace("just no classes found error")
			errors = []
		}
		else {
			for (infos in compiler_output.findall(str)) 
			{
				var infos = infos.copy();
				var f = infos.shift();
				var l = Std.parseInt( infos.shift() )-1;
				var left = Std.parseInt( infos.shift() );
				var right = infos.shift();

				if (right != "") {
					right = Std.parseInt( right );
				}
				else {
					right = left+1;
				}
				m = infos.shift();

				if (m != "Unexpected |") 
				{
					errors.append({
						"file" : f,
						"line" : l,
						"from" : left,
						"to" : right,
						"message" : m
					}) 
				}
			}
		}

		
		//errors.append({ "file:" : "", "line" : 0, "from" : 0, "to" : 0, "message" : "".join(str.split("\n")) + " ( are you referencing a variable that doesn't exist?)"})
		//print(errors)
		if (len(errors) > 0) {
			trace("should show panel")
			hxpanel.slide_panel().writeln(errors[0]["message"])
			sublime.status_message(errors[0]["message"])
		}

		return errors
	}


	public static function get_completion_output(temp_file, orig_file, output, commas) 
	{
		hints, comps = parse_completion_output(temp_file, orig_file, output)

		new_hints = []
		for (h in hints) 
		{
			if (h.length > commas) 
			{
				new_hints.append(h[commas:])
			}
		}
		hints = new_hints

		status, errors = get_completion_status_and_errors(hints, comps, output, temp_file, orig_file)

		return (hints, comps, status, errors)
	}

	public static function parse_completion_output(temp_file, orig_file, output) 
	{

		var tree = null;
		try {
			
			var x = "<root>"+output+"</root>";
			
			tree = ElementTree.XML(x);
		}
		catch (e:Exception) {
			trace("invalid xml - error: " + Std.string(e));
		}

		var hints = null;
		var comps = null;


		if (tree != null) {

			hints = get_type_hint(tree.getiterator("type"))
			comps = collect_completion_fields(tree.find("list"))
			trace("hints:" + Std.string(hints))
			trace("comps:" + Std.string(comps))
		}
		else {
			hints = [];
			comps = [];
		}
			
		if (re.findall(no_classes_found_in_trace, output).length > 0) {
			var smart_snippets = hxsettings.smart_snippets_on_completion();
			var insert = null;
			if (smart_snippets) {
				insert = "${1:value:Dynamic}";
			}
			else {
				insert = "${0}";
			}
			comps.append(CompletionEntry("value:Dynamic", insert, ""))
		}

		return (hints, comps)
	}
		

	public static function get_completion_status_and_errors(hints, comps, output, temp_file, orig_file) {
		var status = "";
		
		var errors = [];

		var res = null;
		if (hints.lenth == 0 and len(comps) == 0) 
		{
			res = parse_completion_errors(output, temp_file, orig_file, status);
		}
			
		return res;
	}

	public static function parse_completion_errors(output:String, temp_file:String, orig_file:String, status:String) {
		trace("output:" + output);
		trace("status:" + status);
		trace("orig_file:" + orig_file);
		trace("temp_file:" + temp_file);

		// get rid of slashes in paths inside of error messages on windows
		// to replace temp_file with orig_file afterwards
		var sep = Os.sep;
		trace("sep: " + sep)
		if (sep == "\\") {
			function slash_replace(match_obj) {
				trace("matched")
				return sep.join(match_obj.group(0).split("/"))
			}

			output = Re.sub(u"[A-Za-z]:(.*)[.]hx", slash_replace, output);
		}

		output = output.replace( temp_file , orig_file );
		
		trace("output after replace: " + output);
		output = Re.sub( u"\(display(.*)\)" ,"",output);
		
		var lines = output.split("\n")
		l = lines[0].strip()
		
		var status = null;

		if (l.length > 0) {

			if (l == "<list>") {
				status = "No autocompletion available";
			}
			else if (!Re.match( haxe_compiler_line , l )) {
				status = l;
				trace(l);
			}
			else {
				status = "";
			}
		}

		var errors = extract_errors( output );
		

		return Tup2.create(status,errors)
	}
}

/*

import sublime
import re
import os

from haxe import panel as hxpanel
from haxe import settings as hxsettings

from haxe.tools import hxsrctools

from haxe.trace import trace

from haxe.plugin import is_st2, is_st3

from xml.etree import ElementTree
from xml.etree.ElementTree import XMLTreeBuilder

if is_st2:
	from elementtree import SimpleXMLTreeBuilder # part of your codebase
	ElementTree.XMLTreeBuilder = SimpleXMLTreeBuilder.TreeBuilder



*/