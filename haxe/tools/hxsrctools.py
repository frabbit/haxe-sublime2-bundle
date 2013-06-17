import re
import os

from haxe.tools.decorator import lazyprop

import pprint

pp = pprint.PrettyPrinter(indent=4, depth=3)


compact_func = re.compile("\(.*\)")
compact_prop = re.compile(":.*\.([a-z_0-9]+)", re.I)
space_chars = re.compile("\s")
word_chars = re.compile("[a-z0-9._]", re.I)
import_line = re.compile("^([ \t]*)import\s+([a-z0-9._]+);", re.I | re.M)
using_line = re.compile("^([ \t]*)using\s+([a-z0-9._]+);", re.I | re.M)
package_line = re.compile("package\s*([a-z0-9.]*);", re.I)

type_decl_with_scope = re.compile("(private\s+)?(?:extern\s+)?(class|typedef|enum|interface|abstract)\s+([A-Z][a-zA-Z0-9_]*)\s*(<[a-zA-Z0-9_,]+>)?" , re.M )

type_decl = re.compile("(class|typedef|enum|interface|abstract)\s+([A-Z][a-zA-Z0-9_]*)\s*(<[a-zA-Z0-9_,]+>)?" , re.M )

enum_start_decl = re.compile("enum\s+([A-Z][a-zA-Z0-9_]*)\s*(<[a-zA-Z0-9_,]+>)?" , re.M )

skippable = re.compile("^[a-zA-Z0-9_\s]*$")
in_anonymous = re.compile("[{,]\s*([a-zA-Z0-9_\"\']+)\s*:\s*$" , re.M | re.U )

variables = re.compile("var\s+([^:;\s]*)", re.I)
functions = re.compile("function\s+([^;\.\(\)\s]*)", re.I)
named_functions = re.compile("function\s+([a-zA-Z0-9_]+)\s*", re.I)
function_params = re.compile("function\s+[a-zA-Z0-9_]+\s*\(([^\)]*)", re.M)
param_default = re.compile("(=\s*\"*[^\"]*\")", re.M)
is_type = re.compile("^[A-Z][a-zA-Z0-9_]*$")
comments = re.compile("(//[^\n\r]*?[\n\r]|/\*(.*?)\*/)", re.MULTILINE | re.DOTALL )



# searches the next occurrence of `char` in `hx_src_section` on the same nesting level as the char at position `start_pos`
# the search starts at position `start_pos` in `hx_src_section`.
def search_next_char_on_same_nesting_level (hx_src_section, char, start_pos):
	open_pars = 0
	open_braces = 0
	open_brackets = 0
	open_angle_brackets = 0

	count = len(hx_src_section)
	cur = ""
	pos = start_pos
	while (True):
		if pos > count-1:
			break

		c = hx_src_section[pos]

		next = hx_src_section[pos+1] if pos < count-1 else None

		if (c == char and open_pars == 0 and open_braces == 0 and open_brackets == 0 and open_angle_brackets == 0):
			return (pos,cur)
						
		if (c == "-" and next == ">"):
			cur += "->"
			pos += 2
		elif (c == "{"):
			pos += 1
			open_braces += 1
			cur += c
		elif (c == "}"):
			pos += 1
			open_braces -= 1
			cur += c
		elif (c == "("):
			pos += 1
			open_pars += 1
			cur += c
		elif (c == ")"):
			pos += 1
			open_pars -= 1
			cur += c
		elif (c == "["):
			pos += 1
			open_brackets += 1
			cur += c
		elif (c == "]"):
			pos += 1
			open_brackets -= 1
			cur += c
		elif (c == "<"):
			pos += 1
			open_angle_brackets += 1
			cur += c
		elif (c == ">"):
			pos += 1
			open_angle_brackets -= 1
			cur += c
		else:
			pos += 1
			cur += c
	return None

# reverse search the next occurrence of `char` in `hx_src_section` on the same nesting level as the char at position `start_pos`.
# the reverse search starts at position `start_pos` in `hx_src_section`.
def reverse_search_next_char_on_same_nesting_level (hx_src_section, char, start_pos):
	open_pars = 0
	open_braces = 0
	open_brackets = 0
	open_angle_brackets = 0

	
	cur = ""
	pos = start_pos
	while (True):
		if pos <= -1:
			break

		c = hx_src_section[pos]

		next = hx_src_section[pos-1] if pos > 0 else None

		if (c == char and open_pars == 0 and open_braces == 0 and open_brackets == 0 and open_angle_brackets == 0):
			return (pos,cur)
						
		if (c == ">" and next == "-"):
			cur = "->" + cur
			pos -= 2
		elif (c == "}"):
			pos -= 1
			open_braces += 1
			cur = c + cur
		elif (c == "{"):
			pos -= 1
			open_braces -= 1
			cur = c + cur
		elif (c == ")"):
			pos -= 1
			open_pars += 1
			cur = c + cur
		elif (c == "("):
			pos -= 1
			open_pars -= 1
			cur = c + cur
		elif (c == "]"):
			pos -= 1
			open_brackets += 1
			cur = c + cur
		elif (c == "["):
			pos -= 1
			open_brackets -= 1
			cur = c + cur
		elif (c == ">"):
			pos -= 1
			open_angle_brackets += 1
			cur = c + cur
		elif (c == "<"):
			pos -= 1
			open_angle_brackets -= 1
			cur = c + cur
		else:
			pos -= 1
			cur = c + cur
	return None

# removes comments from a haxe source
def strip_comments (src):
	return comments.sub( "" , src )


# returns the package a haxe source
def get_package(src):
	pack = ""
	for ps in package_line.findall( src ) :
		pack = ps
	return pack



def empty_type_bundle():
	return HaxeTypeBundle(dict())

class HaxeTypeBundle:
	def __init__(self, types):
		self._types = types

	def __repr__(self):
		return "HaxeTypeBundle(\n" + pp.pformat(self._types) + "\n)"


	# merges `itself` and `other` into a new type bundle. Order matters, because types from `other` shadow the types of self if they have
	# the same fullqualified name, which is the dict identifier.
	def merge (self, other):
		res = dict(self._types)
		for k,v in other._types.items():
			res[k] = v
		return HaxeTypeBundle(res)

	# returns all available packages based on the types inside of this bundle
	def packs (self):
		res = dict()
		for k in self._types:
			p = self._types[k].pack
			if p != "":
				res[p] = None

		return list(res.keys())


	def all_types_and_enum_constructors (self):
		res = dict()
		for k in self._types:
			t = self._types[k]
			if t.is_enum:
				for ec in t.full_qualified_enum_constructors_with_optional_module:
					res[ec] = None
			fq_name = t.full_qualified_name_with_optional_module
			res[fq_name] = None

		return list(res.keys())

	# returns a list of all types stored in this type bundle
	def all_types(self):
		return list(self._types.values())


	def filter (self, fn):
		res = dict()
		for k in self._types:
			t = self._types[k]
			if fn(t) == True:
				res[k] = t

		return HaxeTypeBundle(res)

	def filter_by_classpath (self, cp):
		return self.filter(lambda p: p.classpath == cp)

	def filter_by_classpaths (self, cps):
		return self.filter(lambda p: p.classpath in cps)

class EnumConstructor:
	def __init__(self, name, enum_type):
		self.name = name
		self.enum = enum_type

	def to_snippet_insert (self, import_list, insert_file):
		for i in import_list:
			if (self.enum.file == insert_file or
				i == self.enum.full_qualified_name_with_optional_module or
				i == self.enum.full_pack_with_module or 
				i == self.enum.full_qualified_name_with_optional_module + "." + self.name):
				return self.name
		
		return self.enum.full_qualified_name_with_optional_module + "." + self.name

	@lazyprop
	def type_hint(self):
		return "enum value"


	def to_snippet(self, insert_file, import_list):
		location = " (" + self.enum.full_pack_with_optional_module + ")" if len(self.enum.full_pack_with_optional_module) > 0 else ""
		display = self.enum.name + "." + self.name + location + "\t" + self.type_hint
		insert = self.to_snippet_insert(import_list, insert_file)

		return (display, insert)


class HaxeType:
	def __init__(self, pack, module, name, kind, is_private, is_module_type, is_std_type, is_extern, file):
		self.is_private = is_private
		self.pack = pack
		self.module = module
		self.kind = kind
		self.name = name
		self.is_module_type = is_module_type
		self.is_std_type = is_std_type
		self.is_extern = is_extern

		self.file = file

		self._enum_constructors = None

	def to_snippet(self, insert_file, import_list):
		location = " (" + self.full_pack_with_optional_module + ")" if len(self.full_pack_with_optional_module) > 0 else ""
		display = self.name + location + "\t" + self.type_hint
		insert = self.to_snippet_insert(import_list, insert_file)

		return (display, insert)

	# convert this type into insert snippets. Multiple snippets when it's an enum, separated into the enum itself and it's constructors.
	def to_snippets(self, import_list, insert_file):
	    if self.is_enum:
	        return [ev.to_snippet(insert_file, import_list) for ev in self.enum_constructors]
	    else:
	        return [self.to_snippet(insert_file, import_list)]


	def to_snippet_insert (self, import_list, insert_file):
		for i in import_list:
			if (self.file == insert_file or
				i == self.full_pack_with_module or
				i == self.full_qualified_name_with_optional_module or 
				i == self.full_qualified_name):
				return self.name
		
		return self.full_qualified_name_with_optional_module


	@lazyprop
	def toplevel_pack(self):
		if len(self.pack_list) > 0:
			return self.pack_list[0]
		return None

	@lazyprop	
	def type_hint(self):
		return self.kind

	
	@lazyprop
	def full_pack_with_optional_module(self):
		mod = "" if (self.is_module_type or self.is_std_type) else self.pack_suffix + self.module
		return self.pack + mod

	@lazyprop
	def full_pack_with_module(self):
		return self.pack + self.pack_suffix + self.module
	

	@lazyprop
	def is_enum (self):
		return self.kind == "enum"

	def __repr__(self):
		return self.to_string()

	@lazyprop
	def pack_list(self):
		return self.pack.split(".") if len(self.pack) > 0 else []

	@lazyprop
	def pack_suffix(self):
		return "" if len(self.pack) == 0 else "."

	@lazyprop
	def full_qualified_name_with_optional_module(self):
		mod = "" if (self.is_module_type or self.is_std_type) else self.module + "."
		return self.pack + self.pack_suffix + mod + self.name

	@lazyprop
	def enum_constructors(self):
		if self.is_enum:
			res = [EnumConstructor(e, self) for e in self._enum_constructors ]
		else:
			res = []
		return res

	@lazyprop
	def full_qualified_enum_constructors_with_optional_module(self):
		if not self.is_enum:
			res = []
		else:
			res = [self.full_qualified_name_with_optional_module + "." + e for e in self._enum_constructors]
		return res

	@lazyprop
	def classpath(self):
		path_append = [".." for _ in self.pack_list]
		
		mod_dir = os.path.dirname(self.file)
		fp = [mod_dir]
		fp.extend(path_append)

		full_dir = os.sep.join(fp)

		return os.path.normpath(full_dir)


	@lazyprop
	def full_qualified_name(self):
		return self.pack + self.pack_suffix + self.module + "." + self.name

	def to_string(self):
		return ("{"
			+ " pack:" + str(self.pack) + ", "
			+ " module:" + str(self.module) + ", "
			+ " name:" + str(self.name) + ", "
			+ " kind:" + str(self.kind) + ", "
			+ " enum_constructors:" + str(self.enum_constructors) + ", "
			+ " is_private:" + str(self.is_private) + ", "
			+ " is_module_type:" + str(self.is_module_type) + ", "
			+ " is_std_type:" + str(self.is_std_type) + ", "
			+ " is_extern:" + str(self.is_extern) + ", "
			+ " file:'" + str(self.file) + "'"
			+ " classpath:'" + str(self.classpath) + "'"
			+ " }")


_type_decl_with_scope = re.compile("(private\s+)?(extern\s+)?(class|typedef|enum|interface|abstract)\s+([A-Z][a-zA-Z0-9_]*)\s*(<[a-zA-Z0-9,_]+>)?(:?\{|\s+)" , re.M )

def get_types_from_src (src, module_name, file):
	if module_name == None:
		module_name = os.path.splitext( os.path.basename(file) )[0]

	pack = get_package(src)

	res = dict()
	for decl in _type_decl_with_scope.finditer( src ):
		is_private = decl.group(1) != None
		
		type_name = decl.group(4)

		if type_name == "NME_":
			print(str(decl.group(0)))
		kind = decl.group(3)

		is_extern = decl.group(2) is not None

		is_module_type = type_name == module_name
		is_std_type = module_name == "StdTypes"

		full_type = HaxeType(pack, module_name, type_name, kind, is_private, is_module_type, is_std_type, is_extern, file)

		if full_type.is_enum:
			full_type._enum_constructors = _extract_enum_constructors_from_src(src, decl.end(4))

		if not full_type.full_qualified_name in res:
			res[full_type.full_qualified_name] = full_type

	return HaxeTypeBundle(res)



def _extract_enum_constructors_from_src (src, start_pos):

	constructors = None
	
	start = search_next_char_on_same_nesting_level(src, "{", start_pos)
	if start is not None:
		end = search_next_char_on_same_nesting_level(src, "}", start[0]+1)
		if end is not None:
			constructors = _extract_enum_constructors_from_enum(src[start[0]+1: end[0]-1])
			
	return constructors

enum_constructor_start_decl = re.compile("\s+([a-zA-Z_]+)" , re.M )

def _extract_enum_constructors_from_enum (enumStr):
	
	constructors = []
	start = 0;
	while True:
		m = enum_constructor_start_decl.match(enumStr, start)
		if m != None:
			constructor = m.group(1)
			constructors.append(constructor)
			end = search_next_char_on_same_nesting_level(enumStr, ";", m.end(1))
			if end != None:
				start = end[0]+1
			else:
				break
		else:
			break
	return constructors