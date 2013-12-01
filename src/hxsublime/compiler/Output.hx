package hxsublime.compiler;

import haxe.ds.StringMap;
import hxsublime.panel.Panels;
import hxsublime.Settings;
import hxsublime.tools.HxSrcTools;
import python.lib.Builtin;
import python.lib.Inspect;
import python.lib.Os;
import python.lib.PPrint;
import python.lib.Re;
import python.lib.Types.Exception;
import python.lib.xml.etree.ElementTree;

import python.lib.Types;
import sublime.Sublime;

using python.lib.StringTools;
using python.Macros;

import StringTools in ST;

class CompletionEntry {

	public var hint:String;
	public var insert:String;
	public var doc:String;
	
	public function new(hint, insert, doc)
	{
		this.hint = hint;
		this.insert = insert;
		this.doc = doc;
	}
}

typedef CompilerError = {
    line : Int,
    file:String,
    from : Int,
    to : Int,
    message:String,
}

class Output {
	public static var compiler_output = Re.compile("^([^:]+):([0-9]+): (?:character(?:s?)|line(?:s?))? ([0-9]+)-?([0-9]+)? : (.*)", Re.M);
	public static var no_classes_found = Re.compile("^No classes found in .*", Re.M);
	public static var no_classes_found_in_trace = Re.compile("^No classes found in trace$", Re.M);
	public static var haxe_compiler_line = "^([^:]*):([0-9]+): characters? ([0-9]+)-?[0-9]* :(.*)$";
	public static var type_parameter_name = Re.compile("^([A-Z][_a-zA-Z0-9]*)");

	public static function get_type_hint (types:PyIterable<Element>) 
	{

		var hints = [];
		
		Macros.pyFor(i, types, {
			var hint = i.text.strip();
			var hint_types = HxSrcTools.splitFunctionSignature(hint);
			hints.push( hint_types );
		});
		

		return hints;
	}


	

	public static function get_function_type_params(name:String, signature_types:Array<String>) 
	{

		var new_args = [];
		var type_params = new StringMap();
		var name_len = name.length;
		for (t in signature_types) 
		{
			
			new_args.push(t.split(name + ".").join(""));
			while (true) 
			{
				
				var index = t.indexOf(name);
				if (index == -1) break;
				var type_start_index = index + name_len + 1;
				t = t.substr(type_start_index);
				
				var m = type_parameter_name.match(t);
				if (m != null) 
				{
					var param_name = m.group(1);
					type_params.set(param_name, true);
				}
				else 
				{
					break;
				}
			}
		}

		var keys = [for (k in type_params.keys()) k];
		keys.reverse();
		var type_param_list = keys;
		
		return Tup2.create(new_args, type_param_list);
	}


	public static function completion_field_to_entry(name:String, sig:String, doc:String) 
	{

		var insert = name;
		var label = name;
		
		var smart_snippets = Settings.smartSnippetsOnCompletion();
		var not_smart = !smart_snippets;



		if (sig != null) {
			var types = HxSrcTools.splitFunctionSignature(sig);

			
			
			var r = get_function_type_params(name, types);
			
			var types = r._1, type_params = r._2;

			var params_sig = "";

			if (type_params.length > 0) {
				params_sig = "<" + type_params.join(", ") + ">";
			}





			

			

			
			
			
			
			var ret = types.pop();

			var signature_separator = " : ";

			if( types.length > 0 ) {
				
				if (types.length == 1 && types[0] == "Void") {

					label = if (not_smart) (name + params_sig + "()" + signature_separator + ret) else (name + "()" + signature_separator+ ret);
					insert = if (not_smart) name  else "" + name + "${1:()}";
				}
				else {
					function escape_type (x:String) {
						return ST.replace(ST.replace(x, "}", "\\}"), "{", "\\{");
					}

					var params = "( " + types.join(", ") + " )";
					label = name + params_sig + params + signature_separator + ret;
					
					//hint_to_long = is_st2 and len(label) > 40
					//if (hint_to_long) { // compact arguments
					//	label = hxsrctools.compact_func.sub("(...)", label);
					//}
					
					var new_types = types.copy();
					for (i in 0...new_types.length) 
					{
						new_types[i] = "${" + Std.string(i+2) + ":" + escape_type(new_types[i]) + "}";
					}

					insert = if (not_smart) name else name + "${1:( " + new_types.join(", ") + " )}";
				}
			}
			else {
				label = name + params_sig + signature_separator + ret;
			}
		}
		else {
			label = if (Re.match("^[A-Z]", name ) != null) name + "\tclass" else name + "\tpackage";
		}
				
		
		//if is_st2 and len(label) > 40: # compact return type
		//	m = hxsrctools.compact_prop.search(label)
		//	if m != null:
		//		label = hxsrctools.compact_prop.sub(": " + m.group(1), label)
		
		var res = new CompletionEntry( label, insert, doc );

		return res;
	}
			

	public static function collect_completion_fields (li:Element) 
	{
		var comps = [];
		if (li != null) {

			Macros.pyFor(i, li.iter("i"), {
				var name = i.get("n");
				var sig = i.find("t").text;
				var doc = i.find("d").text; // nothing to do
				var entry = completion_field_to_entry(name, sig, doc);
					
				comps.push(entry);
			});
			
		}

		return comps;
	}


	public static function extract_errors( str:String ) 
	{
		var errors = [];
		
		//trace("error_str: |||" + str + "|||")
		// swallow no classes found in * errors where * could be trace or an unknown variable etc.
		if (no_classes_found.findallString(str).length > 0) {
			//trace("just no classes found error")
			errors = [];
		}
		else {
			for (infos in compiler_output.findallArray(str)) 
			{
				//var infos = infos.copy();
				var f = infos.shift();
				var l = Std.parseInt( infos.shift() )-1;
				var left = Std.parseInt( infos.shift() );
				var right = infos.shift();

				var rightInt = 0;
				if (right != "") {
					rightInt = Std.parseInt( right );
				}
				else {
					rightInt = left+1;
				}
				var m = infos.shift();

				if (m != "Unexpected |") 
				{
					errors.push({
						"file" : f,
						"line" : l,
						"from" : left,
						"to" : rightInt,
						"message" : m
					});
				}
			}
		}

		
		//errors.append({ "file:" : "", "line" : 0, "from" : 0, "to" : 0, "message" : "".join(str.split("\n")) + " ( are you referencing a variable that doesn't exist?)"})
		//print(errors)
		if (errors.length > 0) 
		{
			
			Panels.slidePanel().writeln(errors[0].message);
			Sublime.status_message(errors[0].message);
		}

		return errors;
	}


	public static function getCompletionOutput(temp_file:String, orig_file:String, output:String, commas:Int) 
	{
		var r = parse_completion_output(temp_file, orig_file, output);
		var hints = r._1, comps = r._2;
		var new_hints = [];
		for (h in hints) 
		{
			if (h.length > commas) 
			{
				var x = h.slice(commas);
				new_hints.push(x);
			}
		}
		hints = new_hints;

		var r1 = get_completion_status_and_errors(hints, comps, output, temp_file, orig_file);
		var status = null, errors = null;
		if (r1 != null) {
			status = r1._1;
			errors = r1._2;
		} 
		
		return Tup4.create(hints, comps, status, errors);
	}

	public static function parse_completion_output(temp_file:String, orig_file:String, output:String):Tup2<Array<Array<String>>, Array<CompletionEntry>>
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

			



			hints = get_type_hint(tree.iter("type"));
			comps = collect_completion_fields(tree.find("list"));
			//trace("hints:" + Std.string(hints));
			//trace("comps:" + Std.string(comps));
		}
		else {
			hints = [];
			comps = [];
		}
			
		if (Re.findallDynamic(no_classes_found_in_trace, output).length > 0) 
		{
			var smart_snippets = Settings.smartSnippetsOnCompletion();
			var insert = null;
			if (smart_snippets) {
				insert = "${1:value:Dynamic}";
			}
			else {
				insert = "${0}";
			}
			comps.push(new CompletionEntry("value:Dynamic", insert, ""));
		}

		return Tup2.create(hints, comps);
	}
		

	public static function get_completion_status_and_errors(hints:Array<Array<String>>, comps:Array<CompletionEntry>, output, temp_file, orig_file) 
	{
		var status = "";
		
		var errors = [];

		var res = null;

		if (hints.length == 0 && comps.length == 0) 
		{
			res = parse_completion_errors(output, temp_file, orig_file, status);
		} else {
			res = Tup2.create("", []);
		}
			
		return res;
	}

	public static function parse_completion_errors(output:String, temp_file:String, orig_file:String, status:String) 
	{
		trace("output:" + output);
		trace("status:" + status);
		trace("orig_file:" + orig_file);
		trace("temp_file:" + temp_file);

		// get rid of slashes in paths inside of error messages on windows
		// to replace temp_file with orig_file afterwards
		var sep = Os.sep;
		trace("sep: " + sep);
		if (sep == "\\") {
			function slash_replace(match_obj:MatchObject) {
				trace("matched");
				return match_obj.group(0).split("/").join(sep);
			}

			output = Re.sub("[A-Za-z]:(.*)[.]hx", slash_replace, output);
		}

		output = ST.replace(output, temp_file , orig_file );
		
		trace("output after replace: " + output);
		output = Re.sub( "\\(display(.*)\\)" ,"",output);
		
		var lines = output.split("\n");
		var l = lines[0].strip();
		
		var status = null;

		if (l.length > 0) {

			if (l == "<list>") {
				status = "No autocompletion available";
			}
			else if (Re.match( haxe_compiler_line , l ) == null) {
				status = l;
				trace(l);
			}
			else {
				status = "";
			}
		}

		var errors = extract_errors( output );
		

		return Tup2.create(status,errors);
	}
}
