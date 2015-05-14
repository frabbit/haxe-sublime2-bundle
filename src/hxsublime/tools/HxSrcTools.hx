package hxsublime.tools;

import haxe.ds.StringMap;
import hxsublime.macros.LazyFunctionSupport;
import python.lib.Os;
import python.lib.os.Path;
import python.lib.Re;
import python.lib.Time;
import python.Dict;
import python.Tuple;

import hxsublime.support.Macros;

using hxsublime.support.ArrayTools;


@:allow(hxsublime.tools)
class Regex
{
	public static var space_chars = Re.compile("\\s");
	public static var word_chars = Re.compile("[a-z0-9._]", Re.I);
	public static var import_line = Re.compile("^([ \t]*)import\\s+([a-z0-9._]+);", Re.I | Re.M);
	public static var using_line = Re.compile("^([ \t]*)using\\s+([a-z0-9._]+);", Re.I | Re.M);
	public static var package_line = Re.compile("\\s*package\\s*([a-z0-9.]*)\\s*;", Re.I);
	public static var variables = Re.compile("var\\s+([^:;\\s]*)", Re.I);

	public static var named_functions = Re.compile("function\\s+([a-zA-Z0-9_]+)\\s*", Re.I);
	public static var function_params = Re.compile("function\\s+[a-zA-Z0-9_]+\\s*\\(([^\\)]*)", Re.M);
	public static var param_default = Re.compile("(=\\s*\"*[^\"]*\")", Re.M);
	public static var isType = Re.compile("^[A-Z][a-zA-Z0-9_]*$");

	static var typeDeclWithScope = Re.compile("(private\\s+)?(?:extern\\s+)?(class|typedef|enum|interface|abstract)\\s+([A-Z][a-zA-Z0-9_]*)\\s*" , Re.M );

	static var comments = Re.compile("(//[^\n\r]*?[\n\r]|/\\*(.*?)\\*/)", Re.MULTILINE | Re.DOTALL );
	static var fieldRegex = Re.compile("((?:(?:public|static|inline|private)\\s+)*)(var|function)\\s+([a-zA-Z_][a-zA-Z0-9_]*)", Re.MULTILINE);
	static var typeDeclWithScopeRegex = Re.compile("(private\\s+)?(extern\\s+)?(class|typedef|enum|interface|abstract)\\s+(:?[A-Z][a-zA-Z0-9_]*)\\s*" , Re.M );
	static var enumConstructorStartDecl = Re.compile("\\s+([a-zA-Z_]+)" , Re.M );
}

class HxSrcTools {

	public static function getTypesFromSrc (src:String, moduleName:String, file:String, src_with_comments:String)
	{
		if (moduleName == null)
		{
			moduleName = Path.splitext( Path.basename(file) )._1;
		}

		var pack = getPackage(src);

		var res = new StringMap();
		for (decl in Regex.typeDeclWithScopeRegex.finditer( src ).toHaxeIterator())
		{

			var isPrivate = decl.group(1) != null;

			var type_name = decl.group(4);

			if (type_name == "NME_") {
				trace(Std.string(decl.group(0)));
			}

			var kind = decl.group(3);

			var isExtern = decl.group(2) != null;

			var isModuleType = type_name == moduleName;
			var isStdType = moduleName == "StdTypes";


			var fullType = new HaxeType(pack, moduleName, type_name, kind, isPrivate, isModuleType, isStdType, isExtern, file, src, src_with_comments, decl);


			if (fullType.isEnum()) {
				fullType._enumConstructors = extractEnumConstructorsFromSrc(src, decl.end(4));
			}

			if (!res.exists(fullType.fullQualifiedName())) {

				res.set(fullType.fullQualifiedName(), fullType);
			}
		}
		return new HaxeTypeBundle(res);
	}

	static function extractEnumConstructorsFromSrc (src:String, start_pos:Int)
	{
		var constructors = null;

		var start = searchNextCharOnSameNestingLevel(src, ["{"], start_pos);
		if (start != null) {
			var end = searchNextCharOnSameNestingLevel(src, ["}"], start._1 + 1);
			if (end != null) {
				constructors = extractEnumConstructorsFromEnum(src.substring(start._1 + 1, end._1-1));
			}
		}
		return constructors;
	}

	static function extractEnumConstructorsFromEnum (enumStr:String)
	{

		var constructors = [];
		var start = 0;
		while (true) {
			var m = Regex.enumConstructorStartDecl.match(enumStr, start);
			if (m != null) {
				var constructor = m.group(1);
				constructors.push(constructor);
				var end = searchNextCharOnSameNestingLevel(enumStr, [";"], m.end(1));
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

	public static function skipWhitespaceOrComments(hxSrcSection:String, start_pos:Int)
	{
		var in_single_comment = false;
		var in_multi_comment = false;

		var count = hxSrcSection.length;
		var pos = start_pos;

		while (true)
		{
			if (pos > count-1)
				break;
			var c = hxSrcSection.charAt(pos);
			var next = if (pos < count-1) hxSrcSection.charAt(pos+1) else null;

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
				return Tuple2.make(pos, hxSrcSection.substring(start_pos,pos));
			}
		}
		return null;
	}

	public static function isSameNestingLevelAtPos (hxSrcSection:String, end_pos:Int, start_pos:Int)
	{
		//trace("isSameNestingLevelAtPos - end : " + end_pos + " - start : " + start_pos);
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

		var count = hxSrcSection.length;
		var cur = "";
		var pos = start_pos;

		var lastPos = count-1;
		while (true)
		{

			if (pos == end_pos || pos > lastPos) {
				return open_pars == 0 && open_braces == 0 && open_brackets == 0 && open_angle_brackets == 0 && !in_string && !in_regexp;
			}


			var c = hxSrcSection.charAt(pos);
			var ccode = std.StringTools.fastCodeAt(c, 0);

			var hasNext = pos < lastPos;

			var next = if (hasNext) hxSrcSection.charAt(pos+1) else null;

			var nextCode = if (hasNext) std.StringTools.fastCodeAt(next, 0) else null;


			if (in_regexp)
			{
				pos += 1;
				cur += c;
				if (ccode != "\\".code && nextCode == "/".code) {
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
				else if (ccode == "\\".code && next == string_char)
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


			if (ccode == "~".code && nextCode == "/".code)
			{
				pos +=2;
				in_regexp = true;
				cur += c;
			}
			else if (ccode == "'".code || ccode == '"'.code)
			{
				in_string = true;
				string_char = c;
				cur += c;
				pos += 1;
			}
			else if (ccode == "-".code && nextCode == ">".code)
			{
				cur += "->";
				pos += 2;
			}
			else if (ccode == "{".code)
			{
				pos += 1;
				open_braces += 1;
				cur += c;
			}
			else if (ccode == "}".code)
			{
				pos += 1;
				open_braces -= 1;
				cur += c;
			}
			else if (ccode == "(".code)
			{
				pos += 1;
				open_pars += 1;
				cur += c;
			}
			else if (ccode == ")".code)
			{
				pos += 1;
				open_pars -= 1;
				cur += c;
			}
			else if (ccode == "[".code)
			{
				pos += 1;
				open_brackets += 1;
				cur += c;
			}
			else if (ccode == "]".code)
			{
				pos += 1;
				open_brackets -= 1;
				cur += c;
			}
			else if (ccode == "<".code)
			{
				pos += 1;
				open_angle_brackets += 1;
				cur += c;
			}
			else if (ccode == ">".code)
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

	// searches the next occurrence of `char` in `hxSrcSection` on the same nesting level as the char at position `start_pos`
	// the search starts at position `start_pos` in `hxSrcSection`.
	public static function searchNextCharOnSameNestingLevel (hxSrcSection:String, chars:Array<String>, start_pos:Int)
	{


		var open_pars = 0;
		var open_braces = 0;
		var open_brackets = 0;
		var open_angle_brackets = 0;
		var in_string = false;
		var string_char = null;
		var in_regexp = false;

		var count = hxSrcSection.length;
		var cur = "";
		var pos = start_pos;
		while (true) {
			if (pos > count-1)
				break;

			var c = hxSrcSection.charAt(pos);


			var next = if (pos < count-1) hxSrcSection.charAt(pos+1) else null;

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

			if (open_pars == 0 && open_braces == 0 && open_brackets == 0 && open_angle_brackets == 0 && ArrayTools.contains(chars,c))
			{
				return Tuple2.make(pos,cur);
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

	// reverse search the next occurrence of `char` in `hxSrcSection` on the same nesting level as the char at position `start_pos`.
	// the reverse search starts at position `start_pos` in `hxSrcSection`.
	public static function reverse_search_next_char_on_same_nesting_level (hxSrcSection:String, chars:Array<String>, start_pos:Int)
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

			var c = hxSrcSection.charAt(pos);

			var next = if (pos > 0) hxSrcSection.charAt(pos-1) else null;

			if (in_string)
			{
				pos -= 1;
				cur = c+cur;
				if (c == string_char && next != "\\") {
					in_string = false;
				}

				continue;
			}


			//trace(c + " in " + Std.string(chars) + ":" + Std.string(ArrayTools.contains(chars, c)));

			// single line comment
			if (c == "/" && next == "/")
			{
				pos -= 2;
				cur = "//" + c;
				continue;
			}



			if (open_pars == 0 && open_braces == 0 && open_brackets == 0 && open_angle_brackets == 0 && ArrayTools.contains(chars, c))
			{
				return Tuple2.make(pos,cur);
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
	public static function stripComments (src:String)
	{
		return Regex.comments.sub( "" , src );
	}

	// returns the package of a haxe source file
	static function getPackage(src:String)
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
	public static function splitFunctionSignature (signature:String)
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



	public static function emptyTypeBundle() {
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


class HaxeTypeBundle implements LazyFunctionSupport
{
	var _types:StringMap<HaxeType>;

	public function new(types)
	{
		this._types = types;
	}

	@lazyFunction
	public function toString()
	{
		return "HaxeTypeBundle(\n" + _types.toString() + "\n)";
	}


	// merges `itself` and `other` into a new type bundle. Order matters, because types from `other` shadow the types of self if they have
	// the same fullqualified name, which is the dict identifier.
	public function merge (other:HaxeTypeBundle)
	{
		return mergeAll([other]);
	}

	public function mergeAll (others:Array<HaxeTypeBundle>)
	{
		var res:StringMap<HaxeType> = [for (k in _types.keys()) k => _types.get(k)];

		for (o in others) {
			for (k in o._types.keys()) {
				res.set(k, o._types.get(k));
			}
		}

		return new HaxeTypeBundle(res);
	}

	// returns all available packages based on the types inside of this bundle

	@lazyFunction
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


	@lazyFunction
	public function allModules ()
	{
		var res = new StringMap();
		for (k in _types.keys()) {
			var t = _types.get(k);
			res.set(t.fullPackWithModule(), new HaxeModule(t.pack, t.module, t.file()));
		}
		return res;
	}


	@lazyFunction
	public function allModulesList ()
	{

		var mods = allModules();
		return [ for (m in mods) m];

	}


	@lazyFunction
	public function allTypesAndEnumConstructorsWithInfo ()
	{
		var res = new StringMap();
		for (k in _types.keys()) {
			var t = _types.get(k);
			if (t.isEnum())
				for (ec in t.fullQualifiedEnumConstructorsWithOptionalModule())
					res.set(ec,t);
			var fq_name = t.fullQualifiedNameWithOptionalModule();
			res.set(fq_name, t);
		}
		return res;
	}

	@lazyFunction
	public function allTypesAndEnumConstructors ()
	{
		var res = allTypesAndEnumConstructorsWithInfo();
		return [for (k in res.keys()) k];
	}

	// returns a list of all types stored in this type bundle
	@lazyFunction
	public function allTypes():Array<HaxeType>
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

	/*
	public function filterByClasspath (cp:String)
	{
		return filter(function (p) return p.classpath() == cp);
	}

	public function filterByClasspaths (cps:Array<String>)
	{
		return filter(function (p) return Lambda.has(cps, p.classpath()));
	}
	*/
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

	function toSnippetInsert (import_list:Array<String>, insert_file:String)
	{
		for (i in import_list)
		{
			if (enumType.file() == insert_file ||
				i == enumType.fullQualifiedNameWithOptionalModule() ||
				i == enumType.fullPackWithModule() ||
				i == enumType.fullQualifiedNameWithOptionalModule() + "." + name)
			{
				return name;
			}
		}

		return enumType.fullQualifiedNameWithOptionalModule() + "." + name;
	}

	//@lazyprop
	public function typeHint()
	{
		return "enum value";
	}


	public function toSnippet(insert_file:String, import_list:Array<String>):Tuple2<String, String>
	{
		var location = if (enumType.fullPackWithOptionalModule().length > 0) " (" + enumType.fullPackWithOptionalModule() + ")" else "";
		var display = enumType.name + "." + name + location + "\t" + typeHint();
		var insert = toSnippetInsert(import_list, insert_file);

		return Tuple2.make(display, insert);
	}

	public function toString()
	{
		return this.name;
	}
}

class HaxeField implements LazyFunctionSupport
{
	public var type : HaxeType;
	public var name : String;
	public var kind : String;
	public var isStatic : Bool;
	public var isPublic : Bool;
	public var isInline : Bool;
	public var isPrivate : Bool;

	public var match_decl : MatchObject;

	public function new (type, name, kind, is_static, is_public, is_inline, is_private, match_decl)
	{
		this.type = type;
		this.name = name;
		this.kind = kind;
		this.isStatic = is_static;
		this.isPublic = is_public;
		this.isInline = is_inline;
		this.isPrivate = is_private;
		this.match_decl = match_decl;
	}


	@lazyFunction
	public function srcPos ()
	{

		for (decl in Regex.fieldRegex.finditer( type.src_with_comments ).toHaxeIterator())
		{
			if (decl.group(0) == match_decl.group(0)) {
				return decl.start(0);

			}
		}
		return null;
	}


	@lazyFunction
	public function isVar ()
	{
		return kind == "var";
	}

	@lazyFunction
	public function file ()
	{

		return type.file();
	}

	@lazyFunction
	public function isFunction ()
	{
		return kind == "function";
	}

	@lazyFunction
	public function toString ()
	{
		return type.fullQualifiedNameWithOptionalModule() + ( if (isStatic || name == "new") "::" else ".") + name;
	}

	@lazyFunction
	public function toExpression ()
	{
		return type.fullQualifiedNameWithOptionalModule() + "." + name;
	}

}

class HaxeType implements LazyFunctionSupport
{

	var _src:String;
	public var src_with_comments:String;
	var match_decl:MatchObject;
	public var is_private:Bool;
	public var pack:String;
	public var module:String;
	public var kind:String;
	public var name:String;
	public var is_module_type:Bool;
	var isStdType:Bool;
	public var isExtern:Bool;
	var _file:String;
	public var _enumConstructors:Array<String>;

	public inline function src () return _src;
	public inline function file () return _file;

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
		this.isStdType = is_std_type;
		this.isExtern = is_extern;
		this._file = file;
		this._enumConstructors = null;
	}

	@lazyFunction
	public function strippedStartDeclPos()
	{
		return match_decl.start(0);
	}


	@lazyFunction
	public function classBody ()
	{
		var res = null;
		if (this.strippedEndDeclPos == null)
		{
			res = "";
		}
		else
		{
			res = this.src().substring(this.strippedStartDeclPos(), this.strippedEndDeclPos());
		}
		return res;
	}


	@lazyFunction
	public function publicStaticFields ()
	{
		var res = [];
		res.extend(this.publicStaticVars());
		res.extend(this.publicStaticFunctions());
		return res;
	}





	@lazyFunction
	public function allFields ()
	{
		var startTime = Time.time();
		var res = new StringMap();
		if (classBody() != null) {
			var startPos = classBodyStart()._1;
			Macros.pyFor(decl, Regex.fieldRegex.finditer(classBody()),
			{

				var modifiers = decl.group(1);
				var isStatic = modifiers != null && modifiers.indexOf("static") > -1;
				var isInline = modifiers != null && modifiers.indexOf("inline") > -1;
				var isPrivate = modifiers != null && modifiers.indexOf("private") > -1;
				var isPublic = modifiers != null && modifiers.indexOf("public") > -1;



				function sameNestingLevel () {
					return HxSrcTools.isSameNestingLevelAtPos(classBody(), decl.start(0), startPos);
				}

				if (isPrivate || isPublic || isStatic || this.isExtern || sameNestingLevel())
				{
					var kind = decl.group(2);
					var name = decl.group(3);
					res.set(name, new HaxeField(this, name, kind, isStatic, isPublic, isInline, isPrivate, decl));
				}
				startPos = decl.start(0);
			});
		}
		var runTime = Time.time() - startTime;
		if (runTime > 0.02) {
			trace("allFields Time " + this._file + " : " + (runTime));
		}
		return res;

	}


	@lazyFunction
	public function allFieldsList ()
	{
		var all = allFields();
		return [for (e in all) e ];
	}


	@lazyFunction
	public function publicStaticVars ()
	{
		var all = allFields();
		return  [for (e in all) if (e.isStatic && e.isVar()) e];
	}


	@lazyFunction
	public function publicStaticFunctions ()
	{
		var all = allFields();
		return [for (e in all) if (e.isStatic && e.isFunction() ) e];
	}


	@lazyFunction
	public function classBodyStart ()
	{
		var start = match_decl.start(0);
		if (isAbstract() || isClass()) {
			return HxSrcTools.searchNextCharOnSameNestingLevel(src(), ["{"], start);
		} else {
			return Tuple2.make(0,"");
		}

	}

	@lazyFunction
	public function strippedEndDeclPos ()
	{

		var classBodyStart = this.classBodyStart();
		var res = null;
		if (classBodyStart != null)
		{
			var classBodyEnd = HxSrcTools.searchNextCharOnSameNestingLevel(src(), ["}"], classBodyStart._1+1);
			if (classBodyEnd != null)
			{
				res = classBodyEnd._1;
			}
			else {
				res = null;
			}
		}
		else
		{
			res = null;
		}
		return res;
	}


	@lazyFunction
	public function srcPos ():Int
	{

		Macros.pyFor(decl, Regex.typeDeclWithScope.finditer( src_with_comments ), {
			if (decl.group(0) == match_decl.group(0))
			{
				return decl.start(0);
			}
		});
		return null;

	}

	function toSnippet(insert_file:String, import_list:Array<String>)
	{
		var location = if (fullPackWithOptionalModule().length > 0) (" (" + fullPackWithOptionalModule() + ")") else "";
		var display = name + location + "\t" + typeHint();
		var insert = toSnippetInsert(import_list, insert_file);

		return Tuple2.make(display, insert);
	}

	// convert this type into insert snippets. Multiple snippets when it's an enum, separated into the enum itself and it's constructors.
	public function toSnippets(import_list:Array<String>, insert_file:String)
	{
		var res = [toSnippet(insert_file, import_list)];

		if (isEnum() && _enumConstructors != null)
		{
			for (ev in enumConstructors()) res.push(ev.toSnippet(insert_file, import_list));

		}
		return res;
	}


	public function toSnippetInsert (import_list:Array<String>, insert_file:String)
	{
		for (i in import_list)
		{
			if (_file == insert_file ||
				i == fullPackWithModule() ||
				i == fullQualifiedNameWithOptionalModule() ||
				i == fullQualifiedName())
			{
				return name;
			}
		}

		return fullQualifiedNameWithOptionalModule();
	}

	@lazyFunction
	public function toplevelPack():Null<String>
	{
		var pl = packList();
		if (pl.length > 0)
			return pl[0];
		return null;

	}


	public inline function typeHint()
	{
		return kind;
	}

	@lazyFunction
	public function fullPackWithOptionalModule()
	{
		var mod = if (is_module_type || isStdType) "" else packSuffix() + module;
		return pack + mod;
	}

	@lazyFunction
	public function fullPackWithModule()
	{
		return pack + packSuffix() + module;
	}


	public inline function isEnum ()
	{
		return kind == "enum";
	}

	public inline function isClass ()
	{
		return kind == "class";
	}

	public inline function isAbstract ()
	{
		return kind == "abstract";
	}


	@lazyFunction
	public function packList():Array<String>
	{
		return if (pack.length > 0) pack.split(".") else [];
	}


	@lazyFunction
	public function packSuffix()
	{
		return if (pack.length == 0) "" else ".";
	}


	@lazyFunction
	public function fullQualifiedNameWithOptionalModule()
	{
		var mod = if (is_module_type || isStdType ) "" else module + ".";
		return pack + packSuffix() + mod + name;
	}


	@lazyFunction
	public function enumConstructors()
	{
		var res = null;
		if (isEnum() && _enumConstructors != null) {
			res = [for (e in _enumConstructors) new EnumConstructor(e, this) ];
		}
		else {
			res = [];
		}
		return res;
	}

	@lazyFunction
	public function fullQualifiedEnumConstructorsWithOptionalModule()
	{
		var res = null;
		if (!isEnum() || _enumConstructors == null)
		{
			res = [];
		}
		else
		{
			var fqName = fullQualifiedNameWithOptionalModule();
			res = [for (e in _enumConstructors) fqName + "." + e];
		}
		return res;

	}


	@lazyFunction
	public function classpath()
	{
		var path_append = [for (_ in packList()) ".."];


		var mod_dir = python.lib.os.Path.dirname(_file);
		var fp = [mod_dir];
		fp.extend(path_append);

		var full_dir = fp.join(Os.sep);

		return Path.normpath(full_dir);
	}


	@lazyFunction
	public function fullQualifiedName()
	{
		return pack + packSuffix() + module + "." + name;
	}

	@lazyFunction
	public function toString()
	{
		return ("{"
			+ " pack:" + Std.string(this.pack) + ", "
			+ " module:" + Std.string(this.module) + ", "
			+ " name:" + Std.string(this.name) + ", "
			+ " kind:" + Std.string(this.kind) + ", "
			+ " enum_constructors:" + Std.string(this.enumConstructors().map(function (ec) return ec.toString())) + ", "
			+ " is_private:" + Std.string(this.is_private) + ", "
			+ " is_module_type:" + Std.string(this.is_module_type) + ", "
			+ " isStdType:" + Std.string(this.isStdType) + ", "
			+ " is_extern:" + Std.string(this.isExtern) + ", "
			+ " file:'" + Std.string(this.file()) + "'"
			+ " classpath:'" + Std.string(this.classpath()) + "'"
			+ " }");
	}

}
