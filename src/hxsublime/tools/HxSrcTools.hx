//import re
//import os
//
//from haxe.tools.decorator import lazyprop
//from haxe.trace import trace
//import pprint
//
//pp = pprint.PrettyPrinter(indent=4, depth=3)

package hxsublime.tools;

import haxe.ds.StringMap;
import python.lib.ArrayTools;
import python.lib.Os;
import python.lib.os.Path;
import python.lib.Re;
import python.lib.Types.Dict;
import python.lib.Types.Tup2;
import python.lib.Types.Tup3;

using python.lib.ArrayTools;

class Regex 
{
	public static var compact_func = Re.compile("\\(.*\\)");
	public static var compact_prop = Re.compile(":.*\\.([a-z_0-9]+)", Re.I);
	public static var space_chars = Re.compile("\\s");
	public static var word_chars = Re.compile("[a-z0-9._]", Re.I);
	public static var import_line = Re.compile("^([ \t]*)import\\s+([a-z0-9._]+);", Re.I | Re.M);
	public static var using_line = Re.compile("^([ \t]*)using\\s+([a-z0-9._]+);", Re.I | Re.M);
	public static var package_line = Re.compile("\\s*package\\s*([a-z0-9.]*)\\s*;", Re.I);
	public static var type_decl_with_scope = Re.compile("(private\\s+)?(?:extern\\s+)?(class|typedef|enum|interface|abstract)\\s+([A-Z][a-zA-Z0-9_]*)\\s*(<[a-zA-Z0-9_,]+>)?" , Re.M );
	public static var type_decl = Re.compile("(class|typedef|enum|interface|abstract)\\s+([A-Z][a-zA-Z0-9_]*)\\s*(<[a-zA-Z0-9_,]+>)?" , Re.M );
	public static var enum_start_decl = Re.compile("enum\\s+([A-Z][a-zA-Z0-9_]*)\\s*(<[a-zA-Z0-9_,]+>)?" , Re.M );
	public static var skippable = Re.compile("^[a-zA-Z0-9_\\s]*$");
	public static var in_anonymous = Re.compile("[{,]\\s*([a-zA-Z0-9_\"\']+)\\s*:\\s*$" , Re.M | Re.U );
	public static var variables = Re.compile("var\\s+([^:;\\s]*)", Re.I);
	public static var functions = Re.compile("function\\s+([^;\\.\\(\\)\\s]*)", Re.I);
	public static var named_functions = Re.compile("function\\s+([a-zA-Z0-9_]+)\\s*", Re.I);
	public static var function_params = Re.compile("function\\s+[a-zA-Z0-9_]+\\s*\\(([^\\)]*)", Re.M);
	public static var param_default = Re.compile("(=\\s*\"*[^\"]*\")", Re.M);
	public static var is_type = Re.compile("^[A-Z][a-zA-Z0-9_]*$");
	public static var comments = Re.compile("(//[^\n\r]*?[\n\r]|/\\*(.*?)\\*/)", Re.MULTILINE | Re.DOTALL );
	public static var _field = Re.compile("((?:(?:public|static|inline|private)\\s+)*)(var|function)\\s+([a-zA-Z_][a-zA-Z0-9_]*)", Re.MULTILINE);
	public static var _type_decl_with_scope = Re.compile("(private\\s+)?(extern\\s+)?(class|typedef|enum|interface|abstract)\\s+([A-Z][a-zA-Z0-9_]*)\\s*(<[a-zA-Z0-9,_]+>)?(:?\\{|\\s+)" , Re.M );
	public static var enum_constructor_start_decl = Re.compile("\\s+([a-zA-Z_]+)" , Re.M );
}

class HxSrcTools {

	public static function get_types_from_src (src:String, module_name:String, file:String, src_with_comments:String) 
	{
		if (module_name == null) {
			module_name = Path.splitext( Path.basename(file) )._1;
		}

		var pack = get_package(src);

		var res = new StringMap();
		for (decl in Regex._type_decl_with_scope.finditer( src ).toHaxeIterator()) {



			var is_private = decl.group(1) != null;
			
			var type_name = decl.group(4);

			if (type_name == "NME_") {
				trace(Std.string(decl.group(0)));
			}

			var kind = decl.group(3);

			var is_extern = decl.group(2) != null;

			var is_module_type = type_name == module_name;
			var is_std_type = module_name == "StdTypes";


			var full_type = new HaxeType(pack, module_name, type_name, kind, is_private, is_module_type, is_std_type, is_extern, file, src, src_with_comments, decl);


			if (full_type.is_enum()) {
				full_type._enum_constructors = _extract_enum_constructors_from_src(src, decl.end(4));
			}



			if (!res.exists(full_type.full_qualified_name())) {

				res.set(full_type.full_qualified_name(), full_type);
			}	

			

		}
		

		return new HaxeTypeBundle(res);
	}



	private static function _extract_enum_constructors_from_src (src:String, start_pos:Int) 
	{

		var constructors = null;
		
		var start = search_next_char_on_same_nesting_level(src, ["{"], start_pos);
		if (start != null) {
			var end = search_next_char_on_same_nesting_level(src, ["}"], start._1 + 1);
			if (end != null) {
				constructors = _extract_enum_constructors_from_enum(src.substring(start._1 + 1, end._1-1));
			}
		}
				
		return constructors;
	}

	

	private static function _extract_enum_constructors_from_enum (enumStr:String) 
	{
		
		var constructors = [];
		var start = 0;
		while (true) {
			var m = Regex.enum_constructor_start_decl.match(enumStr, start);
			if (m != null) {
				var constructor = m.group(1);
				constructors.push(constructor);
				var end = search_next_char_on_same_nesting_level(enumStr, [";"], m.end(1));
				if (end != null) {
					start = end._1+1;
				}	
				else {
					break;
				}
			}
			else {
				break;
			}
		}
		return constructors;
	}

	public static function skip_whitespace_or_comments(hx_src_section:String, start_pos:Int) 
	{
		var in_single_comment = false;
		var in_multi_comment = false;

		var count = hx_src_section.length;
		var pos = start_pos;

		while (true) 
		{

			if (pos > count-1)
				break;
			var c = hx_src_section.charAt(pos);
			var next = if (pos < count-1) hx_src_section.charAt(pos+1) else null;

			if (in_single_comment && c == "\n") 
			{
				pos += 1;
				in_single_comment = false;
			}
			else if (in_multi_comment && c == "*" && next == "/") 
			{
				in_multi_comment = false;
				pos += 2;
			}
			else if (in_single_comment || in_multi_comment) 
			{
				pos += 1;
			}
			else if (c == "/" && next == "/") 
			{
				pos += 2;
				in_single_comment = true;
			}
			else if (c == "/" && next == "*") 
			{
				pos += 2;
				in_multi_comment = true;
			}
			else if (c == " " || c == "\t" || c == "\n") 
			{
				pos += 1;
			}
			else {
				// we are done
				return Tup2.create(pos, hx_src_section.substring(start_pos,pos));
			}
		}
		return null;
	}

	public static function is_same_nesting_level_at_pos (hx_src_section:String, end_pos:Int, start_pos:Int) 
	{

		if (end_pos < start_pos)
		{
			return false;
		}
		var open_pars = 0;
		var open_braces = 0;
		var open_brackets = 0;
		var open_angle_brackets = 0;
		var in_string = false;
		var string_char = null;
		var in_regexp = false;

		var count = hx_src_section.length;
		var cur = "";
		var pos = start_pos;

		while (true) {

			if (pos == end_pos || pos > count-1) {
				return open_pars == 0 && open_braces == 0 && open_brackets == 0 && open_angle_brackets == 0 && !in_string && !in_regexp;
			}


			var c = hx_src_section.charAt(pos);


			var next = if (pos < count-1) hx_src_section.charAt(pos+1) else null;

			if (in_regexp) 
			{
				pos += 1;
				cur += c;
				if (c != "\\" && next == "/") {
					in_regexp = false;
				}
				continue;
			}

			if (in_string) 
			{
				
				if (c == string_char) 
				{
					pos += 1;
					cur += c;
					in_string = false;
				}
				else if (c == "\\" && next == string_char) 
				{
					pos += 2;
					cur += c + next;
					in_string = false;
				}
				else 
				{
					cur += c;
					pos += 1;
				}
				continue;
			}

		
			if (c == "~" && next == "/") 
			{
				pos +=2;
				in_regexp = true;
				cur += c;
			}
			else if (c == "'" || c == '"')
			{
				in_string = true;
				string_char = c;
				cur += c;
				pos += 1;
			}
			else if (c == "-" && next == ">") 
			{
				cur += "->";
				pos += 2;
			}
			else if (c == "{") 
			{
				pos += 1;
				open_braces += 1;
				cur += c;
			}
			else if (c == "}") 
			{
				pos += 1;
				open_braces -= 1;
				cur += c;
			}
			else if (c == "(") 
			{
				pos += 1;
				open_pars += 1;
				cur += c;
			}
			else if (c == ")") 
			{
				pos += 1;
				open_pars -= 1;
				cur += c;
			}
			else if (c == "[") 
			{
				pos += 1;
				open_brackets += 1;
				cur += c;
			}
			else if (c == "]") 
			{
				pos += 1;
				open_brackets -= 1;
				cur += c;
			}
			else if (c == "<") 
			{
				pos += 1;
				open_angle_brackets += 1;
				cur += c;
			}
			else if (c == ">")
			{
				pos += 1;
				open_angle_brackets -= 1;
				cur += c;
			}
			else 
			{
				pos += 1;
				cur += c;
			}
		}
		return false;
	}


	// searches the next occurrence of `char` in `hx_src_section` on the same nesting level as the char at position `start_pos`
	// the search starts at position `start_pos` in `hx_src_section`.
	public static function search_next_char_on_same_nesting_level (hx_src_section:String, chars:Array<String>, start_pos:Int) 
	{
		

		var open_pars = 0;
		var open_braces = 0;
		var open_brackets = 0;
		var open_angle_brackets = 0;
		var in_string = false;
		var string_char = null;
		var in_regexp = false;

		var count = hx_src_section.length;
		var cur = "";
		var pos = start_pos;
		while (true) {
			if (pos > count-1)
				break;

			var c = hx_src_section.charAt(pos);


			var next = if (pos < count-1) hx_src_section.charAt(pos+1) else null;

			if (in_regexp) 
			{
				pos += 1;
				cur += c;
				if (c != "\\" && next == "/")
					in_regexp = false;
				continue;
			}

			if (in_string)
			{
				
				if (c == string_char)
				{
					pos += 1;
					cur += c;
					in_string = false;
				}
				else if (c == "\\" && next == string_char)
				{
					pos += 2;
					cur += c + next;
					in_string = false;
				}
				else 
				{
					cur += c;
					pos += 1;
				}
				continue;
			}

			if (ArrayTools.contains(chars,c) && open_pars == 0 && open_braces == 0 && open_brackets == 0 && open_angle_brackets == 0) 
			{
				return Tup2.create(pos,cur);
			}
			
			if (c == "~" && next == "/")
			{
				pos +=2;
				in_regexp = true;
				cur += c;
			}
			else if (c == "'" || c == '"')
			{
				in_string = true;
				string_char = c;
				cur += c;
				pos += 1;
			}
			else if (c == "-" && next == ">")
			{
				cur += "->";
				pos += 2;
			}
			else if (c == "{")
			{
				pos += 1;
				open_braces += 1;
				cur += c;
			}
			else if (c == "}")
			{
				pos += 1;
				open_braces -= 1;
				cur += c;
			}
			else if (c == "(")
			{
				pos += 1;
				open_pars += 1;
				cur += c;
			}
			else if (c == ")")
			{
				pos += 1;
				open_pars -= 1;
				cur += c;
			}
			else if (c == "[")
			{
				pos += 1;
				open_brackets += 1;
				cur += c;
			}
			else if (c == "]")
			{
				pos += 1;
				open_brackets -= 1;
				cur += c;
			}
			else if (c == "<")
			{
				pos += 1;
				open_angle_brackets += 1;
				cur += c;
			}
			else if (c == ">")
			{
				pos += 1;
				open_angle_brackets -= 1;
				cur += c;
			}
			else
			{
				pos += 1;
				cur += c;
			}
		}
		return null;
	}

	// reverse search the next occurrence of `char` in `hx_src_section` on the same nesting level as the char at position `start_pos`.
	// the reverse search starts at position `start_pos` in `hx_src_section`.
	public static function reverse_search_next_char_on_same_nesting_level (hx_src_section:String, chars:Array<String>, start_pos:Int) 
	{
		
		var open_pars = 0;
		var open_braces = 0;
		var open_brackets = 0;
		var open_angle_brackets = 0;
		var in_string = false;
		var string_char = null;

		
		var cur = "";
		var pos = start_pos;
		while (true) 
		{
			if (pos <= -1) 
			{
				break;
			}

			var c = hx_src_section.charAt(pos);

			var next = if (pos > 0) hx_src_section.charAt(pos-1) else null;

			if (in_string) 
			{
				pos -= 1;
				cur = c+cur;
				if (c == string_char && next != "\\") {
					in_string = false;
				}

				continue;
			}


			trace(c + " in " + Std.string(chars) + ":" + Std.string(ArrayTools.contains(chars, c)));

			// single line comment
			if (c == "/" && next == "/") 
			{
				pos -= 2;
				cur = "//" + c;
				continue;
			}



			if (ArrayTools.contains(chars, c) && open_pars == 0 && open_braces == 0 && open_brackets == 0 && open_angle_brackets == 0) 
			{
				return Tup2.create(pos,cur);
			}
					

			if (c == "'" || c == '\"') 
			{
				in_string = true;
				string_char = c;
				cur = c + cur;
				pos -= 1;
			}
			else if (c == ">" && next == "-")
			{
				cur = "->" + cur;
				pos -= 2;
			}
			else if (c == "}")
			{
				pos -= 1;
				open_braces += 1;
				cur = c + cur;
			}
			else if (c == "{")
			{
				pos -= 1;
				open_braces -= 1;
				cur = c + cur;
			}
			else if (c == ")")
			{
				pos -= 1;
				open_pars += 1;
				cur = c + cur;
			}
			else if (c == "(")
			{	
				pos -= 1;
				open_pars -= 1;
				cur = c + cur;
			}
			else if (c == "]")
			{
				pos -= 1;
				open_brackets += 1;
				cur = c + cur;
			}
			else if (c == "[")
			{
				pos -= 1;
				open_brackets -= 1;
				cur = c + cur;
			}
			else if (c == ">")
			{
				pos -= 1;
				open_angle_brackets += 1;
				cur = c + cur;
			}
			else if (c == "<")
			{
				pos -= 1;
				open_angle_brackets -= 1;
				cur = c + cur;
			}
			else
			{
				pos -= 1;
				cur = c + cur;
			}
		}
		return null;
	}

	// removes comments from a haxe source
	public static function strip_comments (src:String) 
	{
		return Regex.comments.sub( "" , src );
	}

	// returns the package of a haxe source file
	public static function get_package(src:String) 
	{
		var pack = "";
		var all = Regex.package_line.findallString( src );
		
		for (ps in all) {
			pack = ps;
		}
		return pack;
	}


	//
	// splits a function signature into a list of types
	// e.g.
	// split_function_signature("A -> Array<T> -> (Void->Void) -> Int")
	// returns:
	// ["A","Array<T>","(Void->Void)","Int"]
	//
	public static function split_function_signature (signature:String) 
	{
		var open_pars = 0;
		var open_braces = 0;
		var open_brackets = 0;

		var types = [];
		var count = signature.length;
		var cur = "";
		var pos = 0;
		while (true) 
		{
			if (pos > count-1) 
			{
				ArrayTools.append(types, cur);
				break;
			}

			var c = signature.charAt(pos);
			var next = if (pos < count-1) signature.charAt(pos+1) else null;
			
			if (c == "-" && next == ">") 
			{
				if (open_pars == 0 && open_braces == 0 && open_brackets == 0) 
				{
					ArrayTools.append(types, cur);
					cur = "";
				}
				else 
				{
					cur += "->";
				}
				
				pos += 2;
			}
			else if (c == " " && open_pars == 0 && open_braces == 0 && open_brackets == 0)
			{
				pos += 1;
			}
			else if (c == "{")
			{
				pos += 1;
				open_braces += 1;
				cur += c;
			}
			else if (c == "}")
			{
				pos += 1;
				open_braces -= 1;
				cur += c;
			}
			else if (c == "(")
			{
				pos += 1;
				open_pars += 1;
				cur += c;
			}
			else if (c == ")")
			{
				pos += 1;
				open_pars -= 1;
				cur += c;
			}
			else if (c == "<")
			{
				pos += 1;
				open_brackets += 1;
				cur += c;
			}
			else if (c == ">")
			{
				pos += 1;
				open_brackets -= 1;
				cur += c;
			}
			else
			{
				pos += 1;
				cur += c;
			}
		}
		return types;
	}



	public static function empty_type_bundle() {
		return new HaxeTypeBundle(new StringMap());
	}
}


class HaxeModule 
{
	public var pack:String;
	public var name:String;
	public var file:String;
	
	public function new(pack:String, name:String, file:String) 
	{
		this.pack = pack;
		this.name = name;
		this.file = file;
	}
}


class HaxeTypeBundle 
{
	var _types:StringMap<HaxeType>;

	public function new(types) 
	{
		this._types = types;
	}

	public function toString() 
	{
		return "HaxeTypeBundle(\n" + _types.toString() + "\n)";
	}


	// merges `itself` and `other` into a new type bundle. Order matters, because types from `other` shadow the types of self if they have
	// the same fullqualified name, which is the dict identifier.
	public function merge (other:HaxeTypeBundle) 
	{

		var res:StringMap<HaxeType> = [for (k in _types.keys()) k => _types.get(k)];

		for (k in other._types.keys()) {
			res.set(k, other._types.get(k));
		}

		return new HaxeTypeBundle(res);
	}

	// returns all available packages based on the types inside of this bundle
	public function packs () 
	{
		var res = new StringMap();

		for (k in _types.keys()) {
			var p = _types.get(k).pack;
			if (p != "") {
				res.set(p,null);
			}
		}

		return Lambda.array({ iterator : function () return res.keys()});
	}

	public function all_modules () 
	{
		var res = new StringMap();
		for (k in _types.keys()) {
			var t = _types.get(k);
			res.set(t.full_pack_with_module(), new HaxeModule(t.pack, t.module, t.file()));
		}
			
		return res;
	}

	public function all_modules_list () 
	{
		var mods = all_modules();
		return [ for (m in mods) m];
	}


	public function all_types_and_enum_constructors_with_info () 
	{
		var res = new StringMap();
		for (k in _types.keys()) {
			var t = _types.get(k);
			if (t.is_enum())
				for (ec in t.full_qualified_enum_constructors_with_optional_module())
					res.set(ec,t);
			var fq_name = t.full_qualified_name_with_optional_module();
			res.set(fq_name, t);
		}

		return res;
	}

	public function all_types_and_enum_constructors () 
	{
		var res = all_types_and_enum_constructors_with_info();
		return [for (k in res.keys()) k];
	}

	// returns a list of all types stored in this type bundle
	public function all_types():Array<HaxeType> 
	{
		return [for (v in _types) v];
	}


	public function filter (fn:HaxeType->Bool) 
	{
		var res = new StringMap();
		for (k in _types.keys()) {
			var t = _types.get(k);
			if (fn(t)) {
				res.set(k, t);
			}
		}

		return new HaxeTypeBundle(res);
	}	

	public function filter_by_classpath (cp:String) 
	{
		return filter(function (p) return p.classpath() == cp);
	}

	public function filter_by_classpaths (cps:Array<String>) 
	{
		return filter(function (p) return Lambda.has(cps, p.classpath()));
	}
}
class EnumConstructor 
{
	
	var name:String;
	var enumType : HaxeType;
	public function new (name, enum_type) 
	{
		this.name = name;
		this.enumType = enum_type;
	}

	public function to_snippet_insert (import_list:Array<String>, insert_file:String) 
	{
		for (i in import_list) 
		{
			if (enumType.file() == insert_file ||
				i == enumType.full_qualified_name_with_optional_module() ||
				i == enumType.full_pack_with_module() ||
				i == enumType.full_qualified_name_with_optional_module() + "." + name) 
			{
				return name;
			}
		}
		
		return enumType.full_qualified_name_with_optional_module() + "." + name;
	}

	//@lazyprop
	public function type_hint() 
	{
		return "enum value";
	}


	public function to_snippet(insert_file:String, import_list:Array<String>):Tup2<String, String>
	{
		var location = if (enumType.full_pack_with_optional_module().length > 0) " (" + enumType.full_pack_with_optional_module() + ")" else "";
		var display = enumType.name + "." + name + location + "\t" + type_hint();
		var insert = to_snippet_insert(import_list, insert_file);

		return Tup2.create(display, insert);
	}

	public function toString()
	{
		return this.name;
	}
}

class HaxeField 
{
	public var type : HaxeType;
	public var name : String;
	public var kind : String;
	public var is_static : Bool;
	public var is_public : Bool;
	public var is_inline : Bool;
	public var is_private : Bool;

	public var match_decl : MatchObject;

	public function new (type, name, kind, is_static, is_public, is_inline, is_private, match_decl) 
	{
		this.type = type;
		this.name = name;
		this.kind = kind;
		this.is_static = is_static;
		this.is_public = is_public;
		this.is_inline = is_inline;
		this.is_private = is_private;
		this.match_decl = match_decl;
	}
		
	private var _src_pos = null;
	@lazyprop
	public function src_pos () 
	{
		if (_src_pos == null) {
			for (decl in Regex._field.finditer( type.src_with_comments ).toHaxeIterator())
			{
				if (decl.group(0) == match_decl.group(0)) {
					_src_pos = decl.start(0);
					return _src_pos;
				}
			}
		}
		return _src_pos;
	}

	private var _is_var:Bool;
	@lazyprop
	public function is_var () 
	{
		if (_is_var == null) {
			_is_var = kind == "var";
		}
		return _is_var;
		
	}

	private var _file = null;
	@property
	public function file () 
	{
		if (_file == null) {
			_file = type.file();
		}
		return _file;
	}

	private var _is_function = null;
	@lazyprop
	public function is_function () 
	{
		if (_is_function == null)
			_is_function = kind == "function";
		return _is_function;
	}

	
	public function toString () 
	{
		return type.full_qualified_name_with_optional_module() + ( if (is_static || name == "new") "::" else ".") + name;
	}

	public function to_expression () 
	{
		return type.full_qualified_name_with_optional_module() + "." + name;
	}

}

class HaxeType 
{

	public var _src:String;
	public var src_with_comments:String;
	public var match_decl:MatchObject;
	public var is_private:Bool;
	public var pack:String;
	public var module:String;
	public var kind:String;
	public var name:String;
	public var is_module_type:Bool;
	public var is_std_type:Bool;
	public var is_extern:Bool;
	public var _file:String;
	public var _enum_constructors:Array<String>;

	public function src () return _src;
	public function file () return _file;

	public function new(pack, module, name, kind, is_private, is_module_type, is_std_type, is_extern, file, src, src_with_comments, match_decl) 
	{
		this._src = src; // src without comments
		this.src_with_comments = src_with_comments;
		this.match_decl = match_decl;
		this.is_private = is_private;
		this.pack = pack;
		this.module = module;
		this.kind = kind;
		this.name = name;
		this.is_module_type = is_module_type;
		this.is_std_type = is_std_type;
		this.is_extern = is_extern;
		this._file = file;
		this._enum_constructors = null;
	}

	var _stripped_start_decl_pos = null;
	@lazyprop
	public function stripped_start_decl_pos() 
	{
		if (_stripped_start_decl_pos == null) {
			_stripped_start_decl_pos = match_decl.start(0);
		}
		return _stripped_start_decl_pos;
	}

	var _class_body:String = null;
	@lazyprop
	public function class_body () 
	{
		if (_class_body == null) {
			var res = null;
			if (this.stripped_end_decl_pos == null) 
			{
				res = "";
			}
			else 
			{
				res = this.src().substring(this.stripped_start_decl_pos(), this.stripped_end_decl_pos());
			}
			_class_body = res;

		}

		return _class_body;
	}

	
	var _public_static_fields = null;
	@lazyprop
	public function public_static_fields () 
	{
		if (_public_static_fields == null) {
			var res = [];
			res.extend(this.public_static_vars());
			res.extend(this.public_static_functions());
			_public_static_fields = res;
		}
		return _public_static_fields;
	}




	var _all_fields = null;
	@lazyprop 
	public function all_fields () 
	{
		if (_all_fields == null) {
			var res = new StringMap();
			if (class_body != null) {
				for (decl in Regex._field.finditer(class_body()).toHaxeIterator()) 
				{
					var modifiers = decl.group(1);
					var is_static = modifiers != null && modifiers.indexOf("static") > -1;
					var is_inline = modifiers != null && modifiers.indexOf("inline") > -1;
					var is_private = modifiers != null && modifiers.indexOf("private") > -1;
					var is_public = modifiers != null && modifiers.indexOf("public") > -1;
					var kind = decl.group(2);
					var name = decl.group(3);
					if (name == "WAIT_END_RET") trace(modifiers);

					if (is_private || is_public || is_static || this.is_extern || HxSrcTools.is_same_nesting_level_at_pos(class_body(), decl.start(0), class_body_start()._1))
						res.set(name, new HaxeField(this, name, kind, is_static, is_public, is_inline, is_private, decl));
				}
			}
			_all_fields = res;
		}
		return _all_fields;
	}

	var _all_fields_list = null;
	@lazyprop
	public function all_fields_list () 
	{
		if (_all_fields_list == null) {
			var all = all_fields();
			_all_fields_list = [for (k in all.keys()) all.get(k) ];
		} 
		return _all_fields_list;
	}
	var _public_static_vars = null;
	@lazyprop
	public function public_static_vars () 
	{
		if (_public_static_vars == null) {
			var all = all_fields();
			_public_static_vars =  [for (k in all.keys()) if (all.get(k).is_static && all.get(k).is_var()) all.get(k)];
		}
		return _public_static_vars;
	}
	
	var _public_static_functions = null;
	@lazyprop
	public function public_static_functions () 
	{
		if (_public_static_functions == null) {
			var all = all_fields();
			_public_static_functions =  [for (k in all.keys()) if (all.get(k).is_static && all.get(k).is_function() ) all.get(k)];
		}
		return _public_static_functions;
	}
	var _class_body_start = null;
	var _class_body_start_set = false;
	@lazyprop
	public function class_body_start () 
	{
		if (!_class_body_start_set) 
		{
			_class_body_start_set = true;
			var start = match_decl.start(0);
			if (is_abstract() || is_class()) {
				_class_body_start = HxSrcTools.search_next_char_on_same_nesting_level(src(), ["{"], start);
			} else {
				_class_body_start = Tup2.create(0,"");
			}
		}
		return _class_body_start;
	}
	var _stripped_end_decl_pos = null;
	var _stripped_end_decl_pos_set = false;
	@lazyprop
	public function stripped_end_decl_pos () 
	{
		if (!_stripped_end_decl_pos_set) 
		{
			_stripped_end_decl_pos_set = true;
			var class_body_start = this.class_body_start();
			var res = null;
			if (class_body_start != null) 
			{
				//trace("have class_body_start:" + Std.string(class_body_start._1));
				var class_body_end = HxSrcTools.search_next_char_on_same_nesting_level(src(), ["}"], class_body_start._1+1);
				if (class_body_end != null) 
				{
					//trace("have class_body_end:" + Std.string(class_body_end._1));
					res = class_body_end._1;
				}
				else {
					res = null;
				}
			}
			else 
			{
				res = null;
			}
			_stripped_end_decl_pos = res;
		}
		return _stripped_end_decl_pos;

	}
		


	var _src_pos = null;
	var _src_pos_set = false;
	@lazyprop
	public function src_pos ():Int 
	{
		if (!_src_pos_set) {
			_src_pos_set = true;
			for (decl in Regex.type_decl_with_scope.finditer( src_with_comments ).toHaxeIterator()) 
			{
				//trace(Std.string(decl.group(0)));
				//trace(Std.string(match_decl.group(0)));
				if (decl.group(0) == match_decl.group(0)) 
				{
					_src_pos = decl.start(0);

					return _src_pos;
				}
			}
			
		}
		return _src_pos;
		
	}

	public function to_snippet(insert_file:String, import_list:Array<String>) 
	{
		var location = if (full_pack_with_optional_module().length > 0) (" (" + full_pack_with_optional_module() + ")") else "";
		var display = name + location + "\t" + type_hint();
		var insert = to_snippet_insert(import_list, insert_file);

		return Tup2.create(display, insert);
	}

	// convert this type into insert snippets. Multiple snippets when it's an enum, separated into the enum itself and it's constructors.
	public function to_snippets(import_list:Array<String>, insert_file:String) 
	{
		var res = [to_snippet(insert_file, import_list)];

		if (is_enum() && _enum_constructors != null) 
		{
			res.extend([for (ev in enum_constructors()) ev.to_snippet(insert_file, import_list)]);
		}
		return res;
	}


	public function to_snippet_insert (import_list:Array<String>, insert_file:String)
	{
		for (i in import_list) 
		{
			if (_file == insert_file ||
				i == full_pack_with_module() ||
				i == full_qualified_name_with_optional_module() || 
				i == full_qualified_name()) 
			{
				return name;
			}
		}
		
		return full_qualified_name_with_optional_module();
	}
	var _toplevel_pack_set = false;
	var _toplevel_pack = null;
	@lazyprop
	public function toplevel_pack():Null<String> 
	{
		if (!_toplevel_pack_set) 
		{
			_toplevel_pack_set = true;
			var pl = pack_list();
			if (pl.length > 0)
				_toplevel_pack = pl[0];
		}
		return _toplevel_pack;
	}

	@lazyprop	
	public function type_hint() 
	{
		return kind;
	}

	var _full_pack_with_optional_module = null;
	@lazyprop
	public function full_pack_with_optional_module() 
	{
		if (_full_pack_with_optional_module == null) {
			var mod = if (is_module_type || is_std_type) "" else pack_suffix() + module;
			_full_pack_with_optional_module = pack + mod;
		}
		return _full_pack_with_optional_module;
	}

	var _full_pack_with_module = null;
	@lazyprop
	public function full_pack_with_module() 
	{
		if (_full_pack_with_module == null) {
			_full_pack_with_module = pack + pack_suffix() + module;
		}
		return _full_pack_with_module;
	}

	@lazyprop
	public function is_enum () 
	{
		return kind == "enum";
	}

	@lazyprop
	public function is_class () 
	{
		return kind == "class";
	}

	@lazyprop
	public function is_abstract () 
	{
		return kind == "abstract";
	}

	public function __repr__() 
	{
		return toString();
	}

	var _pack_list = null;
	@lazyprop
	public function pack_list():Array<String> 
	{
		if (_pack_list == null) {
			_pack_list = if (pack.length > 0) pack.split(".") else [];
		}
		return _pack_list;
		
	}


	var _pack_suffix = null;
	@lazyprop
	public function pack_suffix() 
	{
		if (_pack_suffix == null) {
			_pack_suffix = if (pack.length == 0) "" else ".";	
		}
		return _pack_suffix;
		
	}

	var _full_qualified_name_with_optional_module = null;
	@lazyprop
	public function full_qualified_name_with_optional_module() 
	{
		if (_full_qualified_name_with_optional_module == null) {
			var mod = if (is_module_type || is_std_type ) "" else module + ".";
			_full_qualified_name_with_optional_module =  pack + pack_suffix() + mod + name;
		}
		return _full_qualified_name_with_optional_module;
	}

	var _lazy_enum_constructors = null;
	@lazyprop
	public function enum_constructors() 
	{
		if (_lazy_enum_constructors == null) {
			var res = null;
			if (is_enum() && _enum_constructors != null) {
				res = [for (e in _enum_constructors) new EnumConstructor(e, this) ];
			}
			else {
				res = [];
			}
			_lazy_enum_constructors = res;
		}
		return _lazy_enum_constructors;
	}
	
	var _full_qualified_enum_constructors_with_optional_module = null;
	@lazyprop
	public function full_qualified_enum_constructors_with_optional_module() 
	{
		if (_full_qualified_enum_constructors_with_optional_module == null) {
			var res = null;
			if (!is_enum() || _enum_constructors == null) 
			{
				res = [];
			}
			else 
			{
				var fqName = full_qualified_name_with_optional_module();
				res = [for (e in _enum_constructors) fqName + "." + e];
			}
			_full_qualified_enum_constructors_with_optional_module = res;
		}
		return _full_qualified_enum_constructors_with_optional_module;
	}

	var _classpath = null;
	@lazyprop
	public function classpath() 
	{
		if (_classpath == null) {
			var path_append = [for (_ in pack_list()) ".."];

			
			var mod_dir = python.lib.os.Path.dirname(_file);
			var fp = [mod_dir];
			fp.extend(path_append);

			var full_dir = fp.join(Os.sep);

			_classpath = Path.normpath(full_dir);
		}
		return _classpath;
	}

	var _full_qualified_name = null;
	@lazyprop
	public function full_qualified_name() 
	{
		if (_full_qualified_name == null) {
			_full_qualified_name = pack + pack_suffix() + module + "." + name;
		}
		return _full_qualified_name;
	}

	public function toString() 
	{
		return ("{"
			+ " pack:" + Std.string(this.pack) + ", "
			+ " module:" + Std.string(this.module) + ", "
			+ " name:" + Std.string(this.name) + ", "
			+ " kind:" + Std.string(this.kind) + ", "
			+ " enum_constructors:" + Std.string(this.enum_constructors().map(function (ec) return ec.toString())) + ", "
			+ " is_private:" + Std.string(this.is_private) + ", "
			+ " is_module_type:" + Std.string(this.is_module_type) + ", "
			+ " is_std_type:" + Std.string(this.is_std_type) + ", "
			+ " is_extern:" + Std.string(this.is_extern) + ", "
			+ " file:'" + Std.string(this.file()) + "'"
			+ " classpath:'" + Std.string(this.classpath()) + "'"
			+ " }");
	}

}

/*



























*/