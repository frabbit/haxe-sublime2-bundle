_hx_classes = dict()
import functools as _hx_functools
class Int:
    pass
Int._hx_class_name = 'Int'
Int._hx_class = Int
_hx_classes['Int'] = Int
class Bool:
    pass
Bool._hx_class_name = 'Bool'
Bool._hx_class = Bool
_hx_classes['Bool'] = Bool
class Float:
    pass
Float._hx_class_name = 'Float'
Float._hx_class = Float
_hx_classes['Float'] = Float
class Dynamic:
    pass
Dynamic._hx_class_name = 'Dynamic'
Dynamic._hx_class = Dynamic
_hx_classes['Dynamic'] = Dynamic
def _hx_rshift(val, n):
	return (val % 0x100000000) >> n
import math as _hx_math
def HxOverrides_iterator(it):
	if isinstance(it, list):
		return python_internal_ArrayImpl.iterator(it)
	else:
		return it.iterator()

class _HxException(Exception):
    # String tag;
    # int index;
    # List params;
    def __init__(self, val):
        try:
            message = Std.string(val)
        except Exception as e:
            message = '_HxException'
        Exception.__init__(self, message)
        self.val = val


class _Hx_AnonObject(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
# print Array.list
# print IntIterator.IntIterator
class IntIterator:


	def __init__(self,min,max):
		self.min = min
		self.max = max
	
	# var min
	# var max
	def hasNext(self):
		return self.min < self.max

	def next(self):
		def _hx_local_2():
			def _hx_local_1():
				_hx_local_0 = self.min
				self.min = self.min + 1
				return _hx_local_0
			
			return _hx_local_1()
		
		return _hx_local_2()
	







IntIterator._hx_class = IntIterator
IntIterator._hx_class_name = "IntIterator"
_hx_classes['IntIterator'] = IntIterator
IntIterator._hx_fields = ["min","max"]
IntIterator._hx_props = []
IntIterator._hx_methods = ["hasNext","next"]
IntIterator._hx_statics = []
IntIterator._hx_interfaces = []

# print Lambda.Lambda
class Lambda:

	pass




def Lambda_statics_array(it):
	a = list()
	_it = _hx_functools.partial(HxOverrides_iterator, it)()
	while _it.hasNext():
		i = _it.next()
		a.append(i)
		__builtin__.len(a)
	
	return a
	
Lambda.array = Lambda_statics_array
def Lambda_statics_list(it):
	l = List()
	_it = _hx_functools.partial(HxOverrides_iterator, it)()
	while _it.hasNext():
		i = _it.next()
		l.add(i)
	return l
	
Lambda.list = Lambda_statics_list
def Lambda_statics_map(it,f):
	l = List()
	_it = _hx_functools.partial(HxOverrides_iterator, it)()
	while _it.hasNext():
		x = _it.next()
		l.add(f(x))
	return l
	
Lambda.map = Lambda_statics_map
def Lambda_statics_mapi(it,f):
	l = List()
	i = 0
	_it = _hx_functools.partial(HxOverrides_iterator, it)()
	while _it.hasNext():
		x = _it.next()
		l.add(f(_hx_local_1(), x))
	return l
	
Lambda.mapi = Lambda_statics_mapi
def Lambda_statics_has(it,elt):
	_it = _hx_functools.partial(HxOverrides_iterator, it)()
	while _it.hasNext():
		x = _it.next()
		if x == elt:
			return True
		
	return False
	
Lambda.has = Lambda_statics_has
def Lambda_statics_exists(it,f):
	_it = _hx_functools.partial(HxOverrides_iterator, it)()
	while _it.hasNext():
		x = _it.next()
		if f(x):
			return True
		
	return False
	
Lambda.exists = Lambda_statics_exists
def Lambda_statics_foreach(it,f):
	_it = _hx_functools.partial(HxOverrides_iterator, it)()
	while _it.hasNext():
		x = _it.next()
		if not f(x):
			return False
		
	return True
	
Lambda.foreach = Lambda_statics_foreach
def Lambda_statics_iter(it,f):
	_it = _hx_functools.partial(HxOverrides_iterator, it)()
	while _it.hasNext():
		x = _it.next()
		f(x)
Lambda.iter = Lambda_statics_iter
def Lambda_statics_filter(it,f):
	l = List()
	_it = _hx_functools.partial(HxOverrides_iterator, it)()
	while _it.hasNext():
		x = _it.next()
		if f(x):
			l.add(x)
		
	return l
	
Lambda.filter = Lambda_statics_filter
def Lambda_statics_fold(it,f,first):
	_it = _hx_functools.partial(HxOverrides_iterator, it)()
	while _it.hasNext():
		x = _it.next()
		first = f(x, first)
	return first
	
Lambda.fold = Lambda_statics_fold
def Lambda_statics_count(it,pred = None):
	if pred is None:
		pred = None
	
	n = 0
	if pred is None:
		_it = _hx_functools.partial(HxOverrides_iterator, it)()
		while _it.hasNext():
			_ = _it.next()
			_hx_local_0 = n
			n = n + 1
			_hx_local_0
	
	else:
		_it = _hx_functools.partial(HxOverrides_iterator, it)()
		while _it.hasNext():
			x = _it.next()
			if pred(x):
				_hx_local_1 = n
				n = n + 1
				_hx_local_1
	
			
	return n
	
Lambda.count = Lambda_statics_count
def Lambda_statics_empty(it):
	return not _hx_functools.partial(HxOverrides_iterator, it)().hasNext()
Lambda.empty = Lambda_statics_empty
def Lambda_statics_indexOf(it,v):
	i = 0
	_it = _hx_functools.partial(HxOverrides_iterator, it)()
	while _it.hasNext():
		v2 = _it.next()
		if v == v2:
			return i
		
		_hx_local_0 = i
		i = i + 1
		_hx_local_0
		
	
	return -1
	
Lambda.indexOf = Lambda_statics_indexOf
def Lambda_statics_find(it,f):
	_it = _hx_functools.partial(HxOverrides_iterator, it)()
	while _it.hasNext():
		v = _it.next()
		if f(v):
			return v
		
	return None
	
Lambda.find = Lambda_statics_find
def Lambda_statics_concat(a,b):
	l = List()
	_it = _hx_functools.partial(HxOverrides_iterator, a)()
	while _it.hasNext():
		x = _it.next()
		l.add(x)
	_it = _hx_functools.partial(HxOverrides_iterator, b)()
	while _it.hasNext():
		x = _it.next()
		l.add(x)
	return l
	
Lambda.concat = Lambda_statics_concat


Lambda._hx_class = Lambda
Lambda._hx_class_name = "Lambda"
_hx_classes['Lambda'] = Lambda
Lambda._hx_fields = []
Lambda._hx_props = []
Lambda._hx_methods = []
Lambda._hx_statics = ["array","list","map","mapi","has","exists","foreach","iter","filter","fold","count","empty","indexOf","find","concat"]
Lambda._hx_interfaces = []

# print List.List
class List:


	def __init__(self):
		self.length = 0
	# var h
	# var q
	# var length
	def add(self,item):
		x = [item]
		if self.h is None:
			self.h = x
		else:
			self.q[1] = x
		self.q = x
		_hx_local_0 = self.length
		self.length = self.length + 1
		_hx_local_0
		
	

	def push(self,item):
		x = [item, self.h]
		self.h = x
		if self.q is None:
			self.q = x
		
		_hx_local_0 = self.length
		self.length = self.length + 1
		_hx_local_0
		
	

	def first(self):
		if self.h is None:
			return None
		else:
			return self.h[0]

	def last(self):
		if self.q is None:
			return None
		else:
			return self.q[0]

	def pop(self):
		if self.h is None:
			return None
		
		x = self.h[0]
		self.h = self.h[1]
		if self.h is None:
			self.q = None
		
		_hx_local_0 = self.length
		self.length = self.length - 1
		_hx_local_0
		
		return x
	

	def isEmpty(self):
		return self.h is None

	def clear(self):
		self.h = None
		self.q = None
		self.length = 0
	

	def remove(self,v):
		prev = None
		l = self.h
		while l is not None:
			if l[0] == v:
				if prev is None:
					self.h = l[1]
				else:
					prev[1] = l[1]
				if self.q == l:
					self.q = prev
				
				_hx_local_0 = self.length
				self.length = self.length - 1
				_hx_local_0
				
				return True
			
			
			prev = l
			l = l[1]
		
		return False
	

	def iterator(self):
		def _hx_local_2():
			def _hx_local_0():
				return self.h is not None
			def _hx_local_1():
				if self.h is None:
					return None
				
				x = self.h[0]
				self.h = self.h[1]
				return x
			
			return _Hx_AnonObject(h = self.h ,hasNext = _hx_local_0 ,next = _hx_local_1 )
		
		return _hx_local_2()
	

	def toString(self):
		s = _hx_StringIO()
		first = True
		l = self.h
		s1 = "{"
		s.write(s1)
		
		while l is not None:
			if first:
				first = False
			else:
				s1 = ", "
				s.write(s1)
			
			x = Std.string(l[0])
			s1 = Std.string(x)
			s.write(s1)
			
			
			l = l[1]
		
		s1 = "}"
		s.write(s1)
		
		return s.getvalue()
	

	def join(self,sep):
		s = _hx_StringIO()
		first = True
		l = self.h
		while l is not None:
			if first:
				first = False
			else:
				s1 = Std.string(sep)
				s.write(s1)
			
			s1 = Std.string(l[0])
			s.write(s1)
			
			l = l[1]
		
		return s.getvalue()
	

	def filter(self,f):
		l2 = List()
		l = self.h
		while l is not None:
			v = l[0]
			l = l[1]
			if f(v):
				l2.add(v)
			
		
		return l2
	

	def map(self,f):
		b = List()
		l = self.h
		while l is not None:
			v = l[0]
			l = l[1]
			b.add(f(v))
		
		return b
	







List._hx_class = List
List._hx_class_name = "List"
_hx_classes['List'] = List
List._hx_fields = ["h","q","length"]
List._hx_props = []
List._hx_methods = ["add","push","first","last","pop","isEmpty","clear","remove","iterator","toString","join","filter","map"]
List._hx_statics = []
List._hx_interfaces = []

# print Map.Map_Impl_
class Map_Map_Impl_:

	pass




Map_Map_Impl_._new = None;
def Map_Impl__statics_set(this1,key,value):
	this1.set(key, value)
Map_Map_Impl_.set = Map_Impl__statics_set
def Map_Impl__statics_get(this1,key):
	return this1.get(key)
Map_Map_Impl_.get = Map_Impl__statics_get
def Map_Impl__statics_exists(this1,key):
	return this1.exists(key)
Map_Map_Impl_.exists = Map_Impl__statics_exists
def Map_Impl__statics_remove(this1,key):
	return this1.remove(key)
Map_Map_Impl_.remove = Map_Impl__statics_remove
def Map_Impl__statics_keys(this1):
	return this1.keys()
Map_Map_Impl_.keys = Map_Impl__statics_keys
def Map_Impl__statics_iterator(this1):
	return _hx_functools.partial(HxOverrides_iterator, this1)()
Map_Map_Impl_.iterator = Map_Impl__statics_iterator
def Map_Impl__statics_toString(this1):
	return this1.toString()
Map_Map_Impl_.toString = Map_Impl__statics_toString
def Map_Impl__statics_arrayWrite(this1,k,v):
	this1.set(k, v)
	return v
	
Map_Map_Impl_.arrayWrite = Map_Impl__statics_arrayWrite
def Map_Impl__statics_toStringMap(t):
	return haxe_ds_StringMap()
Map_Map_Impl_.toStringMap = Map_Impl__statics_toStringMap
def Map_Impl__statics_toIntMap(t):
	return haxe_ds_IntMap()
Map_Map_Impl_.toIntMap = Map_Impl__statics_toIntMap
def Map_Impl__statics_toEnumValueMapMap(t):
	return haxe_ds_EnumValueMap()
Map_Map_Impl_.toEnumValueMapMap = Map_Impl__statics_toEnumValueMapMap
def Map_Impl__statics_toObjectMap(t):
	return haxe_ds_ObjectMap()
Map_Map_Impl_.toObjectMap = Map_Impl__statics_toObjectMap
def Map_Impl__statics_fromStringMap(map):
	return map
Map_Map_Impl_.fromStringMap = Map_Impl__statics_fromStringMap
def Map_Impl__statics_fromIntMap(map):
	return map
Map_Map_Impl_.fromIntMap = Map_Impl__statics_fromIntMap
def Map_Impl__statics_fromObjectMap(map):
	return map
Map_Map_Impl_.fromObjectMap = Map_Impl__statics_fromObjectMap


Map_Map_Impl_._hx_class = Map_Map_Impl_
Map_Map_Impl_._hx_class_name = "_Map._Map.Map_Impl_"
_hx_classes['_Map._Map.Map_Impl_'] = Map_Map_Impl_
Map_Map_Impl_._hx_fields = []
Map_Map_Impl_._hx_props = []
Map_Map_Impl_._hx_methods = []
Map_Map_Impl_._hx_statics = ["_new","set","get","exists","remove","keys","iterator","toString","arrayWrite","toStringMap","toIntMap","toEnumValueMapMap","toObjectMap","fromStringMap","fromIntMap","fromObjectMap"]
Map_Map_Impl_._hx_interfaces = []

# print Map.IMap
class IMap:

	# var get
	# var set
	# var exists
	# var remove
	# var keys
	# var iterator
	# var toString
	pass






IMap._hx_class = IMap
IMap._hx_class_name = "IMap"
_hx_classes['IMap'] = IMap
IMap._hx_fields = []
IMap._hx_props = []
IMap._hx_methods = ["get","set","exists","remove","keys","iterator","toString"]
IMap._hx_statics = []
IMap._hx_interfaces = []

# print Math._hx_math
import math as _hx_math
# print Reflect.Reflect
class Reflect:

	pass




def Reflect_statics_hasField(o,field):
	field1 = python_internal_KeywordHandler.handleKeywords(field)
	return __builtin__.hasattr(o, field1)
	
Reflect.hasField = Reflect_statics_hasField
def Reflect_statics_field(o,field):
	field1 = python_internal_KeywordHandler.handleKeywords(field)
	if __builtin__.hasattr(o, field1):
		return __builtin__.getattr(o, field1)
	else:
		return None
	
Reflect.field = Reflect_statics_field
def Reflect_statics_setField(o,field,value):
	field1 = python_internal_KeywordHandler.handleKeywords(field)
	return __builtin__.setattr(o, field1, value)
	
Reflect.setField = Reflect_statics_setField
def Reflect_statics_getProperty(o,field):
	field1 = python_internal_KeywordHandler.handleKeywords(field)
	tmp = None
	if o is None:
		return None
	else:
		tmp = Reflect.field(o, "get_" + field1)
		if tmp is not None and __builtin__.callable(tmp):
			return tmp()
		else:
			return Reflect.field(o, field1)
	
	
Reflect.getProperty = Reflect_statics_getProperty
def Reflect_statics_setProperty(o,field,value):
	field1 = python_internal_KeywordHandler.handleKeyword(field)
	raise _HxException("not implemented")
	
Reflect.setProperty = Reflect_statics_setProperty
def Reflect_statics_callMethod(o,func,args):
	args1 = [o] + args
	if python_lib_Inspect.ismethod(o):
		return func(args1)
	else:
		return None
	
Reflect.callMethod = Reflect_statics_callMethod
def Reflect_statics_fields(o):
	a = []
	if o is not None:
		if __builtin__.hasattr(o, "_hx_fields"):
			haxe_Log.trace("here we go", _Hx_AnonObject(fileName = "Reflect.hx" ,lineNumber = 95 ,className = "Reflect" ,methodName = "fields" ))
			fields = o._hx_fields
			return __builtin__.list(fields)
		
		
		if __builtin__.isinstance(o, _Hx_AnonObject):
			d = __builtin__.getattr(o, "__dict__")
			keys = d.keys()
			handler = python_internal_KeywordHandler.unhandleKeywords
			for k in keys:
				a.append(handler(k))
		
		elif __builtin__.hasattr(o, "__dict__"):
			a1 = []
			d = __builtin__.getattr(o, "__dict__")
			keys = d.keys()
			for k in keys:
				a.append(k)
		
		
	
	
	return a
	
Reflect.fields = Reflect_statics_fields
def Reflect_statics_isFunction(f):
	return python_lib_Inspect.isfunction(f) or python_lib_Inspect.ismethod(f)
Reflect.isFunction = Reflect_statics_isFunction
def Reflect_statics_compare(a,b):
	raise _HxException("not implemented")
Reflect.compare = Reflect_statics_compare
def Reflect_statics_compareMethods(f1,f2):
	if f1 == f2:
		return True
	
	if not Reflect.isFunction(f1) or not Reflect.isFunction(f2):
		return False
	
	raise _HxException("not implemented")
	
Reflect.compareMethods = Reflect_statics_compareMethods
def Reflect_statics_isObject(v):
	raise _HxException("not implemented")
Reflect.isObject = Reflect_statics_isObject
def Reflect_statics_isEnumValue(v):
	raise _HxException("not implemented")
Reflect.isEnumValue = Reflect_statics_isEnumValue
def Reflect_statics_deleteField(o,field):
	if not Reflect.hasField(o, field):
		return False
	
	del o[field]
	return True
	
Reflect.deleteField = Reflect_statics_deleteField
def Reflect_statics_copy(o):
	raise _HxException("not implemented")
Reflect.copy = Reflect_statics_copy
def Reflect_statics_makeVarArgs(f):
	raise _HxException("not implemented")
Reflect.makeVarArgs = Reflect_statics_makeVarArgs


Reflect._hx_class = Reflect
Reflect._hx_class_name = "Reflect"
_hx_classes['Reflect'] = Reflect
Reflect._hx_fields = []
Reflect._hx_props = []
Reflect._hx_methods = []
Reflect._hx_statics = ["hasField","field","setField","getProperty","setProperty","callMethod","fields","isFunction","compare","compareMethods","isObject","isEnumValue","deleteField","copy","makeVarArgs"]
Reflect._hx_interfaces = []

# print Std.Std
class Std:

	pass




def Std_statics_instance(v,c):
	if __builtin__.isinstance(v, c):
		return v
	else:
		return None
Std.instance = Std_statics_instance
def Std_statics__hx_is(v,t):
	if v is None:
		return False
	elif t is None:
		return False
	elif t == Dynamic:
		return True
	elif t == Bool and __builtin__.isinstance(v, bool):
		return True
	elif t == Int and __builtin__.isinstance(v, int):
		return True
	elif t == Float and (__builtin__.isinstance(v, (float,int)) or __builtin__.isinstance(v, int)):
		return True
	elif t == str:
		return __builtin__.isinstance(v, String)
	elif __builtin__.isinstance(v, t):
		return True
	elif python_lib_Inspect.isclass(t):
		loop = None
		loop1 = None
		def _hx_local_0(intf):
			f = Reflect.field(intf, "_hx_interfaces")
			if f is not None:
				_g = 0
				while _g < len(f):
					i = f[_g]
					_g = _g + 1
					if i == t:
						return True
					else:
						l = loop1(i)
						if l:
							return True
						
					
				
				
				return False
			
			else:
				return False
		
		loop1 = _hx_local_0
		loop = loop1
		
		return loop(v.__class__)
	
	else:
		return False
Std._hx_is = Std_statics__hx_is
def Std_statics_string(s):
	return python_Boot.__string_rec(s, "")
Std.string = Std_statics_string
def Std_statics_int(x):
	return int(x)
Std.int = Std_statics_int
def Std_statics_parseInt(x):
	x1 = float(x)
	return int(x1)
	
Std.parseInt = Std_statics_parseInt
def Std_statics_parseFloat(x):
	return float(x)
Std.parseFloat = Std_statics_parseFloat
def Std_statics_random(x):
	if x <= 0:
		return 0
	else:
		x1 = python_lib_Random.random() * x
		return int(x1)
	
Std.random = Std_statics_random


Std._hx_class = Std
Std._hx_class_name = "Std"
_hx_classes['Std'] = Std
Std._hx_fields = []
Std._hx_props = []
Std._hx_methods = []
Std._hx_statics = ["instance","is","string","int","parseInt","parseFloat","random"]
Std._hx_interfaces = []

# print StdTypes.ArrayAccess
# print python.lib.Builtin.__builtin__
import builtins as __builtin__
# print String.String
__builtin__
String = __builtin__.str
	
# print StringBuf._hx_StringIO
from io import StringIO as _hx_StringIO
# print StringTools.StringTools
class StringTools:

	pass




def StringTools_statics_urlEncode(s):
	from urllib.parse import quote
	return quote(s)
	
StringTools.urlEncode = StringTools_statics_urlEncode
def StringTools_statics_urlDecode(s):
	from urllib.parse import unquote
	return unquote(s)
	
StringTools.urlDecode = StringTools_statics_urlDecode
def StringTools_statics_htmlEscape(s,quotes = None):
	if quotes is None:
		quotes = None
	
	def _hx_local_0():
		def _hx_local_1():
			_this2 = s.split("&")
			return "&amp;".join(_this2)
		
		_this1 = (_hx_local_1()).split("<")
		return "&lt;".join(_this1)
	
	_this = (_hx_local_0()).split(">")
	s = "&gt;".join(_this)
	
	if quotes:
		def _hx_local_2():
			_this1 = s.split("\"")
			return "&quot;".join(_this1)
		
		_this = (_hx_local_2()).split("'")
		return "&#039;".join(_this)
	
	else:
		return s
	
StringTools.htmlEscape = StringTools_statics_htmlEscape
def StringTools_statics_htmlUnescape(s):
	def _hx_local_0():
		def _hx_local_1():
			def _hx_local_2():
				def _hx_local_3():
					_this4 = s.split("&gt;")
					return ">".join(_this4)
				
				_this3 = (_hx_local_3()).split("&lt;")
				return "<".join(_this3)
			
			_this2 = (_hx_local_2()).split("&quot;")
			return "\"".join(_this2)
		
		_this1 = (_hx_local_1()).split("&#039;")
		return "'".join(_this1)
	
	_this = (_hx_local_0()).split("&amp;")
	return "&".join(_this)
	
StringTools.htmlUnescape = StringTools_statics_htmlUnescape
def StringTools_statics_startsWith(s,start):
	def _hx_local_1():
		def _hx_local_0():
			len = __builtin__.len(start)
			return python_Tools.substr(s, 0, len)
		
		return __builtin__.len(s) >= __builtin__.len(start) and _hx_local_0() == start
	
	return _hx_local_1()
	
StringTools.startsWith = StringTools_statics_startsWith
def StringTools_statics_endsWith(s,end):
	elen = __builtin__.len(end)
	slen = __builtin__.len(s)
	return slen >= elen and python_Tools.substr(s, slen - elen, elen) == end
	
StringTools.endsWith = StringTools_statics_endsWith
def StringTools_statics_isSpace(s,pos):
	c = ord(s[pos])
	return c > 8 and c < 14 or c == 32
	
StringTools.isSpace = StringTools_statics_isSpace
def StringTools_statics_ltrim(s):
	l = __builtin__.len(s)
	r = 0
	while r < l and StringTools.isSpace(s, r):
		_hx_local_0 = r
		r = r + 1
		_hx_local_0
	
	if r > 0:
		return python_Tools.substr(s, r, l - r)
	else:
		return s
	
StringTools.ltrim = StringTools_statics_ltrim
def StringTools_statics_rtrim(s):
	l = __builtin__.len(s)
	r = 0
	while r < l and StringTools.isSpace(s, l - r - 1):
		_hx_local_0 = r
		r = r + 1
		_hx_local_0
	
	if r > 0:
		return python_Tools.substr(s, 0, l - r)
	else:
		return s
	
StringTools.rtrim = StringTools_statics_rtrim
def StringTools_statics_trim(s):
	return StringTools.ltrim(StringTools.rtrim(s))
StringTools.trim = StringTools_statics_trim
def StringTools_statics_lpad(s,c,l):
	if __builtin__.len(c) <= 0:
		return s
	
	while __builtin__.len(s) < l:
		s = c + s
	return s
	
StringTools.lpad = StringTools_statics_lpad
def StringTools_statics_rpad(s,c,l):
	if __builtin__.len(c) <= 0:
		return s
	
	while __builtin__.len(s) < l:
		s = s + c
	return s
	
StringTools.rpad = StringTools_statics_rpad
def StringTools_statics_replace(s,sub,by):
	_this = s.split(sub)
	return by.join(_this)
	
StringTools.replace = StringTools_statics_replace
def StringTools_statics_hex(n,digits = None):
	if digits is None:
		digits = None
	
	s = ""
	hexChars = "0123456789ABCDEF"
	while True:
		s = hexChars[n & 15] + s
		n = _hx_rshift(n, 4)
		if not n > 0:
			break
		
	
	
StringTools.hex = StringTools_statics_hex
def StringTools_statics_fastCodeAt(s,index):
	return ord(s[index])
StringTools.fastCodeAt = StringTools_statics_fastCodeAt
def StringTools_statics_isEof(c):
	return c == -1
StringTools.isEof = StringTools_statics_isEof


StringTools._hx_class = StringTools
StringTools._hx_class_name = "StringTools"
_hx_classes['StringTools'] = StringTools
StringTools._hx_fields = []
StringTools._hx_props = []
StringTools._hx_methods = []
StringTools._hx_statics = ["urlEncode","urlDecode","htmlEscape","htmlUnescape","startsWith","endsWith","isSpace","ltrim","rtrim","trim","lpad","rpad","replace","hex","fastCodeAt","isEof"]
StringTools._hx_interfaces = []

class _Hx_Enum:
    # String tag;
    # int index;
    # List params;
    def __init__(self, tag, index, params):
        self.tag = tag
        self.index = index
        self.params = params
    
    def __str__(self):
        if params == None:
            res = tag
        else:
            res = tag + '(' + ','.join(params) + ')'
        res

class ValueType(_Hx_Enum):
	def __init__(self, t, i, p): 
		super(ValueType,self).__init__(t, i, p)


ValueType.TInt = ValueType("TInt", 1, list())

ValueType.TUnknown = ValueType("TUnknown", 8, list())

ValueType.TFunction = ValueType("TFunction", 5, list())

ValueType.TNull = ValueType("TNull", 0, list())

def _ValueType_statics_TEnum (e): 
	return ValueType("TEnum", 7, [e])
ValueType.TEnum = _ValueType_statics_TEnum

ValueType.TFloat = ValueType("TFloat", 2, list())

def _ValueType_statics_TClass (c): 
	return ValueType("TClass", 6, [c])
ValueType.TClass = _ValueType_statics_TClass

ValueType.TBool = ValueType("TBool", 3, list())

ValueType.TObject = ValueType("TObject", 4, list())
ValueType._hx_constructs = ["TInt","TUnknown","TFunction","TNull","TEnum","TFloat","TClass","TBool","TObject"]
ValueType._hx_class = ValueType
ValueType._hx_class_name = "ValueType"
_hx_classes['ValueType'] = ValueType

# print Type.Type
class Type:

	pass




def Type_statics_getClass(o):
	if o is None:
		return None
	
	if __builtin__.hasattr(o, "__class__"):
		return o.__class__
	else:
		return None
	
Type.getClass = Type_statics_getClass
def Type_statics_getEnum(o):
	if o is None:
		return None
	
	return o.__class__
	
Type.getEnum = Type_statics_getEnum
def Type_statics_getSuperClass(c):
	if o is None:
		return None
	
	res = None
	try:
		res = __python_array_get(o.__bases__, 0)
	except Exception as _hx_e:
		_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
		if True:
			e = _hx_e1
			None
		else:
			raise _hx_e
	return res
	
Type.getSuperClass = Type_statics_getSuperClass
def Type_statics_getClassName(c):
	if __builtin__.hasattr(c, "_hx_class_name"):
		return c._hx_class_name
	else:
		try:
			s = c.__name__
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			if True:
				e = _hx_e1
				None
			else:
				raise _hx_e
	res = None
	return res
	
Type.getClassName = Type_statics_getClassName
def Type_statics_getEnumName(e):
	return e._hx_class_name
Type.getEnumName = Type_statics_getEnumName
def Type_statics_resolveClass(name):
	cl = _hx_classes[name]
	if cl is None or not cl._hx_class:
		return None
	
	return cl
	
Type.resolveClass = Type_statics_resolveClass
def Type_statics_resolveEnum(name):
	return Type.resolveClass(name)
Type.resolveEnum = Type_statics_resolveEnum
def Type_statics_createInstance(cl,args):
	l = __builtin__.len(args)
	if (l) == 0:
		return cl()
	elif (l) == 1:
		return cl(args[0])
	elif (l) == 2:
		return cl(args[0], args[1])
	elif (l) == 3:
		return cl(args[0], args[1], args[2])
	elif (l) == 4:
		return cl(args[0], args[1], args[2], args[3])
	elif (l) == 5:
		return cl(args[0], args[1], args[2], args[3], args[4])
	elif (l) == 6:
		return cl(args[0], args[1], args[2], args[3], args[4], args[5])
	elif (l) == 7:
		return cl(args[0], args[1], args[2], args[3], args[4], args[5], args[6])
	elif (l) == 8:
		return cl(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7])
	else:
		raise _HxException("Too many arguments")
	return None
	
Type.createInstance = Type_statics_createInstance
def Type_statics_createEmptyInstance(cl):
	return cl.__new__(cl)
Type.createEmptyInstance = Type_statics_createEmptyInstance
def Type_statics_createEnum(e,constr,params = None):
	if params is None:
		params = None
	
	f = Reflect.field(e, constr)
	if f is None:
		raise _HxException("No such constructor " + constr)
	
	if Reflect.isFunction(f):
		if params is None:
			raise _HxException("Constructor " + constr + " need parameters")
		
		return Reflect.callMethod(e, f, params)
	
	
	if params is not None and __builtin__.len(params) != 0:
		raise _HxException("Constructor " + constr + " does not need parameters")
	
	return f
	
Type.createEnum = Type_statics_createEnum
def Type_statics_createEnumIndex(e,index,params = None):
	if params is None:
		params = None
	
	c = e.__constructs__[index]
	if c is None:
		raise _HxException(Std.string(index) + " is not a valid enum constructor index")
	
	return Type.createEnum(e, c, params)
	
Type.createEnumIndex = Type_statics_createEnumIndex
def Type_statics_getInstanceFields(c):
	if __builtin__.hasattr(c, "_hx_fields"):
		x = c._hx_fields
		return __builtin__.list(x)
	
	else:
		return []
Type.getInstanceFields = Type_statics_getInstanceFields
def Type_statics_getClassFields(c):
	if __builtin__.hasattr(c, "_hx_statics"):
		x = c._hx_statics
		return __builtin__.list(x)
	
	else:
		return []
Type.getClassFields = Type_statics_getClassFields
def Type_statics_getEnumConstructs(e):
	if __builtin__.hasattr(e, "_hx_constructs"):
		x = e._hx_constructs
		return __builtin__.list(x)
	
	else:
		return []
Type.getEnumConstructs = Type_statics_getEnumConstructs
def Type_statics_typeof(v):
	if v is None:
		return ValueType.TNull
	elif __builtin__.isinstance(v, bool):
		return ValueType.TBool
	elif __builtin__.isinstance(v, int):
		return ValueType.TInt
	elif __builtin__.isinstance(v, float):
		return ValueType.TFloat
	elif __builtin__.hasattr(v, "__class__"):
		if __builtin__.isinstance(v, _Hx_AnonObject):
			return ValueType.TObject
		
		if __builtin__.isinstance(v, _Hx_Enum):
			return ValueType.TEnum(v.__class__)
		
		return ValueType.TClass(v.__class__)
	
	elif __builtin__.callable(v):
		return ValueType.TFunction
	else:
		return ValueType.TUnknown
Type.typeof = Type_statics_typeof
def Type_statics_enumEq(a,b):
	raise _HxException("enumEq not implemented")
Type.enumEq = Type_statics_enumEq
def Type_statics_enumConstructor(e):
	return e.tag
Type.enumConstructor = Type_statics_enumConstructor
def Type_statics_enumParameters(e):
	return e.params
Type.enumParameters = Type_statics_enumParameters
def Type_statics_enumIndex(e):
	return e.index
Type.enumIndex = Type_statics_enumIndex
def Type_statics_allEnums(e):
	ctors = Type.getEnumConstructs(e)
	ret = []
	_g = 0
	while _g < len(ctors):
		ctor = ctors[_g]
		_g = _g + 1
		v = Reflect.field(e, ctor)
		if Std._hx_is(v, e):
			ret.append(v)
			__builtin__.len(ret)
		
		
	
	
	return ret
	
Type.allEnums = Type_statics_allEnums


Type._hx_class = Type
Type._hx_class_name = "Type"
_hx_classes['Type'] = Type
Type._hx_fields = []
Type._hx_props = []
Type._hx_methods = []
Type._hx_statics = ["getClass","getEnum","getSuperClass","getClassName","getEnumName","resolveClass","resolveEnum","createInstance","createEmptyInstance","createEnum","createEnumIndex","getInstanceFields","getClassFields","getEnumConstructs","typeof","enumEq","enumConstructor","enumParameters","enumIndex","allEnums"]
Type._hx_interfaces = []

# print haxe.EnumTools.EnumTools
# print haxe.EnumTools.EnumValueTools
# print haxe.Log.Log
class haxe_Log:

	pass




def Log_statics_trace(v,infos = None):
	if infos is None:
		infos = None
	
	str = None
	if infos is not None:
		str = infos.fileName + ":" + Std.string(infos.lineNumber) + ": " + Std.string(v)
		if __builtin__.hasattr(infos, "customParams"):
			str = str + "," + ",".join(infos.customParams)
		
	
	else:
		str = v
	print(str)
	
haxe_Log.trace = Log_statics_trace
def Log_statics_clear():
	js_Boot.__clear_trace()
haxe_Log.clear = Log_statics_clear


haxe_Log._hx_class = haxe_Log
haxe_Log._hx_class_name = "haxe.Log"
_hx_classes['haxe.Log'] = haxe_Log
haxe_Log._hx_fields = []
haxe_Log._hx_props = []
haxe_Log._hx_methods = []
haxe_Log._hx_statics = ["trace","clear"]
haxe_Log._hx_interfaces = []

# print haxe.ds.BalancedTree.BalancedTree
class haxe_ds_BalancedTree:


	def __init__(self):
		None
	# var root
	def set(self,key,value):
		self.root = self.setLoop(key, value, self.root)

	def get(self,key):
		node = self.root
		while node is not None:
			c = self.compare(key, node.key)
			if c == 0:
				return node.value
			
			if c < 0:
				node = node.left
			else:
				node = node.right
		
		return None
	

	def remove(self,key):
		try:
			self.root = self.removeLoop(key, self.root)
			return True
	
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			if isinstance(_hx_e1, str):
				e = _hx_e1
				return False
			else:
				raise _hx_e

	def exists(self,key):
		node = self.root
		while node is not None:
			c = self.compare(key, node.key)
			if c == 0:
				return True
			elif c < 0:
				node = node.left
			else:
				node = node.right
		
		return False
	

	def iterator(self):
		ret = []
		self.iteratorLoop(self.root, ret)
		it = ret.__iter__()
		return python_HaxeIterator(it)
		
	

	def keys(self):
		ret = []
		self.keysLoop(self.root, ret)
		it = ret.__iter__()
		return python_HaxeIterator(it)
		
	

	def setLoop(self,k,v,node):
		if node is None:
			return haxe_ds_TreeNode(None, k, v, None)
		
		c = self.compare(k, node.key)
		if c == 0:
			return haxe_ds_TreeNode(node.left, k, v, node.right, 0 if (node is None) else node._height)
		elif c < 0:
			nl = self.setLoop(k, v, node.left)
			return self.balance(nl, node.key, node.value, node.right)
		
		else:
			nr = self.setLoop(k, v, node.right)
			return self.balance(node.left, node.key, node.value, nr)
		
	

	def removeLoop(self,k,node):
		if node is None:
			raise _HxException("Not_found")
		
		c = self.compare(k, node.key)
		if c == 0:
			return self.merge(node.left, node.right)
		elif c < 0:
			return self.balance(self.removeLoop(k, node.left), node.key, node.value, node.right)
		else:
			return self.balance(node.left, node.key, node.value, self.removeLoop(k, node.right))
	

	def iteratorLoop(self,node,acc):
		if node is not None:
			self.iteratorLoop(node.left, acc)
			acc.append(node.value)
			__builtin__.len(acc)
			
			self.iteratorLoop(node.right, acc)
	
		

	def keysLoop(self,node,acc):
		if node is not None:
			self.keysLoop(node.left, acc)
			acc.append(node.key)
			__builtin__.len(acc)
			
			self.keysLoop(node.right, acc)
	
		

	def merge(self,t1,t2):
		if t1 is None:
			return t2
		
		if t2 is None:
			return t1
		
		t = self.minBinding(t2)
		return self.balance(t1, t.key, t.value, self.removeMinBinding(t2))
	

	def minBinding(self,t):
		if t is None:
			raise _HxException("Not_found")
		elif t.left is None:
			return t
		else:
			return self.minBinding(t.left)

	def removeMinBinding(self,t):
		if t.left is None:
			return t.right
		else:
			return self.balance(self.removeMinBinding(t.left), t.key, t.value, t.right)

	def balance(self,l,k,v,r):
		hl = None
		if l is None:
			hl = 0
		else:
			hl = l._height
		hr = None
		if r is None:
			hr = 0
		else:
			hr = r._height
		if hl > hr + 2:
			def _hx_local_1():
				_this = l.left
				return 0 if (_this is None) else _this._height
			
			def _hx_local_0():
				_this = l.right
				return 0 if (_this is None) else _this._height
			
			if _hx_local_1() >= _hx_local_0():
				return haxe_ds_TreeNode(l.left, l.key, l.value, haxe_ds_TreeNode(l.right, k, v, r))
			else:
				return haxe_ds_TreeNode(haxe_ds_TreeNode(l.left, l.key, l.value, l.right.left), l.right.key, l.right.value, haxe_ds_TreeNode(l.right.right, k, v, r))
		
		elif hr > hl + 2:
			def _hx_local_3():
				_this = r.right
				return 0 if (_this is None) else _this._height
			
			def _hx_local_2():
				_this = r.left
				return 0 if (_this is None) else _this._height
			
			if _hx_local_3() > _hx_local_2():
				return haxe_ds_TreeNode(haxe_ds_TreeNode(l, k, v, r.left), r.key, r.value, r.right)
			else:
				return haxe_ds_TreeNode(haxe_ds_TreeNode(l, k, v, r.left.left), r.left.key, r.left.value, haxe_ds_TreeNode(r.left.right, r.key, r.value, r.right))
		
		else:
			return haxe_ds_TreeNode(l, k, v, r, (hl if (hl > hr) else hr) + 1)
	

	def compare(self,k1,k2):
		return Reflect.compare(k1, k2)

	def toString(self):
		return "{" + self.root.toString() + "}"







haxe_ds_BalancedTree._hx_class = haxe_ds_BalancedTree
haxe_ds_BalancedTree._hx_class_name = "haxe.ds.BalancedTree"
_hx_classes['haxe.ds.BalancedTree'] = haxe_ds_BalancedTree
haxe_ds_BalancedTree._hx_fields = ["root"]
haxe_ds_BalancedTree._hx_props = []
haxe_ds_BalancedTree._hx_methods = ["set","get","remove","exists","iterator","keys","setLoop","removeLoop","iteratorLoop","keysLoop","merge","minBinding","removeMinBinding","balance","compare","toString"]
haxe_ds_BalancedTree._hx_statics = []
haxe_ds_BalancedTree._hx_interfaces = []

# print haxe.ds.BalancedTree.TreeNode
class haxe_ds_TreeNode:


	def __init__(self,l,k,v,r,h = -1):
		if h is None:
			h = -1
		
		self.left = l
		self.key = k
		self.value = v
		self.right = r
		if h == -1:
			def _hx_local_4():
				def _hx_local_1():
					_this = self.left
					return 0 if (_this is None) else _this._height
				
				def _hx_local_0():
					_this = self.right
					return 0 if (_this is None) else _this._height
				
				def _hx_local_2():
					_this = self.left
					return 0 if (_this is None) else _this._height
				
				def _hx_local_3():
					_this = self.right
					return 0 if (_this is None) else _this._height
				
				return _hx_local_2() if _hx_local_1() > _hx_local_0() else _hx_local_3()
			
			self._height = (_hx_local_4()) + 1
		
		else:
			self._height = h
	
	# var left
	# var right
	# var key
	# var value
	# var _height
	def toString(self):
		return ("" if (self.left is None) else self.left.toString() + ", ") + ("" + Std.string(self.key) + "=" + Std.string(self.value)) + ("" if (self.right is None) else ", " + self.right.toString())







haxe_ds_TreeNode._hx_class = haxe_ds_TreeNode
haxe_ds_TreeNode._hx_class_name = "haxe.ds.TreeNode"
_hx_classes['haxe.ds.TreeNode'] = haxe_ds_TreeNode
haxe_ds_TreeNode._hx_fields = ["left","right","key","value","_height"]
haxe_ds_TreeNode._hx_props = []
haxe_ds_TreeNode._hx_methods = ["toString"]
haxe_ds_TreeNode._hx_statics = []
haxe_ds_TreeNode._hx_interfaces = []

# print haxe.ds.EnumValueMap.EnumValueMap
class haxe_ds_EnumValueMap(haxe_ds_BalancedTree):


	def __init__(self):
		super().__init__()
	def compare(self,k1,k2):
		d = k1.index - k2.index
		if d != 0:
			return d
		
		p1 = k1.params
		p2 = k2.params
		if __builtin__.len(p1) == 0 and __builtin__.len(p2) == 0:
			return 0
		
		return self.compareArgs(p1, p2)
	

	def compareArgs(self,a1,a2):
		ld = __builtin__.len(a1) - __builtin__.len(a2)
		if ld != 0:
			return ld
		
		_g1 = 0
		_g = __builtin__.len(a1)
		while _g1 < _g:
			def _hx_local_1():
				nonlocal _g1
				_hx_local_0 = _g1
				_g1 = _g1 + 1
				return _hx_local_0
				
			
			i = _hx_local_1()
			d = self.compareArg(a1[i], a2[i])
			if d != 0:
				return d
			
		
		
		return 0
	

	def compareArg(self,v1,v2):
		if Reflect.isEnumValue(v1) and Reflect.isEnumValue(v2):
			return self.compare(v1, v2)
		elif Std._hx_is(v1, list) and Std._hx_is(v2, list):
			return self.compareArgs(v1, v2)
		else:
			return Reflect.compare(v1, v2)







haxe_ds_EnumValueMap._hx_class = haxe_ds_EnumValueMap
haxe_ds_EnumValueMap._hx_class_name = "haxe.ds.EnumValueMap"
_hx_classes['haxe.ds.EnumValueMap'] = haxe_ds_EnumValueMap
haxe_ds_EnumValueMap._hx_fields = []
haxe_ds_EnumValueMap._hx_props = []
haxe_ds_EnumValueMap._hx_methods = ["compare","compareArgs","compareArg"]
haxe_ds_EnumValueMap._hx_statics = []
haxe_ds_EnumValueMap._hx_interfaces = [IMap]
haxe_ds_EnumValueMap._hx_super = haxe_ds_BalancedTree

# print haxe.ds.HashMap.HashMap_Impl_
class haxe_ds_HashMap_HashMap_Impl_:

	pass




def HashMap_Impl__statics__new():
	return _Hx_AnonObject(keys = haxe_ds_IntMap() ,values = haxe_ds_IntMap() )
haxe_ds_HashMap_HashMap_Impl_._new = HashMap_Impl__statics__new
def HashMap_Impl__statics_set(this1,k,v):
	this1.keys.set(k.hashCode(), k)
	this1.values.set(k.hashCode(), v)
	
haxe_ds_HashMap_HashMap_Impl_.set = HashMap_Impl__statics_set
def HashMap_Impl__statics_get(this1,k):
	key = k.hashCode()
	return this1.values.h.get(key, None)
	
haxe_ds_HashMap_HashMap_Impl_.get = HashMap_Impl__statics_get
def HashMap_Impl__statics_exists(this1,k):
	key = k.hashCode()
	return python_lib_DictImpl.hasKey(this1.values.h, key)
	
haxe_ds_HashMap_HashMap_Impl_.exists = HashMap_Impl__statics_exists
def HashMap_Impl__statics_remove(this1,k):
	this1.values.remove(k.hashCode())
	return this1.keys.remove(k.hashCode())
	
haxe_ds_HashMap_HashMap_Impl_.remove = HashMap_Impl__statics_remove
def HashMap_Impl__statics_keys(this1):
	return _hx_functools.partial(HxOverrides_iterator, this1.keys)()
haxe_ds_HashMap_HashMap_Impl_.keys = HashMap_Impl__statics_keys
def HashMap_Impl__statics_iterator(this1):
	return _hx_functools.partial(HxOverrides_iterator, this1.values)()
haxe_ds_HashMap_HashMap_Impl_.iterator = HashMap_Impl__statics_iterator


haxe_ds_HashMap_HashMap_Impl_._hx_class = haxe_ds_HashMap_HashMap_Impl_
haxe_ds_HashMap_HashMap_Impl_._hx_class_name = "haxe.ds._HashMap._HashMap.HashMap_Impl_"
_hx_classes['haxe.ds._HashMap._HashMap.HashMap_Impl_'] = haxe_ds_HashMap_HashMap_Impl_
haxe_ds_HashMap_HashMap_Impl_._hx_fields = []
haxe_ds_HashMap_HashMap_Impl_._hx_props = []
haxe_ds_HashMap_HashMap_Impl_._hx_methods = []
haxe_ds_HashMap_HashMap_Impl_._hx_statics = ["_new","set","get","exists","remove","keys","iterator"]
haxe_ds_HashMap_HashMap_Impl_._hx_interfaces = []

# print haxe.ds.IntMap.IntMap
class haxe_ds_IntMap:


	def __init__(self):
		self.h = {}
	# var h
	def set(self,key,value):
		self.h[key] = value

	def get(self,key):
		return self.h.get(key, None)

	def exists(self,key):
		return python_lib_DictImpl.hasKey(self.h, key)

	def remove(self,key):
		if not python_lib_DictImpl.hasKey(self.h, key):
			return False
		
		del self.h[key]
		return True
	

	def keys(self):
		a = []
		for key in self.h:
			a.append(key)
		it = a.__iter__()
		return python_HaxeIterator(it)
		
	

	def iterator(self):
		iter = self.keys()
		ref = self.h
		def _hx_local_2():
			def _hx_local_0():
				return iter.hasNext()
			def _hx_local_1():
				i = iter.next()
				return ref[i]
			
			return _Hx_AnonObject(hasNext = _hx_local_0 ,next = _hx_local_1 )
		
		return _hx_local_2()
	

	def toString(self):
		s = _hx_StringIO()
		s1 = "{"
		s.write(s1)
		
		it = self.keys()
		_it = it
		while _it.hasNext():
			i = _it.next()
			s1 = Std.string(i)
			s.write(s1)
			
			s1 = " => "
			s.write(s1)
			
			x = Std.string(self.h.get(i, None))
			s1 = Std.string(x)
			s.write(s1)
			
			
			if it.hasNext():
				s1 = ", "
				s.write(s1)
			
			
		
		s1 = "}"
		s.write(s1)
		
		return s.getvalue()
	







haxe_ds_IntMap._hx_class = haxe_ds_IntMap
haxe_ds_IntMap._hx_class_name = "haxe.ds.IntMap"
_hx_classes['haxe.ds.IntMap'] = haxe_ds_IntMap
haxe_ds_IntMap._hx_fields = ["h"]
haxe_ds_IntMap._hx_props = []
haxe_ds_IntMap._hx_methods = ["set","get","exists","remove","keys","iterator","toString"]
haxe_ds_IntMap._hx_statics = []
haxe_ds_IntMap._hx_interfaces = [IMap]

# print haxe.ds.ObjectMap.ObjectMap
class haxe_ds_ObjectMap:


	def __init__(self):
		self.h = _Hx_AnonObject()
		self.h._hx_keys__ = _Hx_AnonObject()
	
	# var h
	def set(self,key,value):
		id = None
		if key._hx_id__ is not None:
			id = key._hx_id__
		else:
			def _hx_local_2():
				def _hx_local_0():
					_hx_local_1 = haxe_ds_ObjectMap.count = haxe_ds_ObjectMap.count + 1
					return _hx_local_1
				
				_hx_local_3 = key._hx_id__ = _hx_local_0()
				return _hx_local_3
			
			id = _hx_local_2()
		
		self.h[id] = value
		self.h._hx_keys__[id] = key
	

	def get(self,key):
		return self.h[key._hx_id__]

	def exists(self,key):
		raise _HxException("not implemented")

	def remove(self,key):
		raise _HxException("not implemented")

	def keys(self):
		raise _HxException("not implemented")

	def iterator(self):
		raise _HxException("not implemented")

	def toString(self):
		s = _hx_StringIO()
		s1 = "{"
		s.write(s1)
		
		it = self.keys()
		_it = it
		while _it.hasNext():
			i = _it.next()
			x = Std.string(i)
			s1 = Std.string(x)
			s.write(s1)
			
			
			s1 = " => "
			s.write(s1)
			
			x = Std.string(self.h[i._hx_id__])
			s1 = Std.string(x)
			s.write(s1)
			
			
			if it.hasNext():
				s1 = ", "
				s.write(s1)
			
			
		
		s1 = "}"
		s.write(s1)
		
		return s.getvalue()
	





haxe_ds_ObjectMap.count = 0
def ObjectMap_statics_assignId(obj):
	def _hx_local_4():
		def _hx_local_2():
			def _hx_local_0():
				_hx_local_1 = haxe_ds_ObjectMap.count = haxe_ds_ObjectMap.count + 1
				return _hx_local_1
			
			_hx_local_3 = obj._hx_id__ = _hx_local_0()
			return _hx_local_3
		
		return _hx_local_2()
	
	return _hx_local_4()
	
haxe_ds_ObjectMap.assignId = ObjectMap_statics_assignId
def ObjectMap_statics_getId(obj):
	return obj._hx_id__
haxe_ds_ObjectMap.getId = ObjectMap_statics_getId


haxe_ds_ObjectMap._hx_class = haxe_ds_ObjectMap
haxe_ds_ObjectMap._hx_class_name = "haxe.ds.ObjectMap"
_hx_classes['haxe.ds.ObjectMap'] = haxe_ds_ObjectMap
haxe_ds_ObjectMap._hx_fields = ["h"]
haxe_ds_ObjectMap._hx_props = []
haxe_ds_ObjectMap._hx_methods = ["set","get","exists","remove","keys","iterator","toString"]
haxe_ds_ObjectMap._hx_statics = ["count","assignId","getId"]
haxe_ds_ObjectMap._hx_interfaces = [IMap]

# print haxe.ds.StringMap.StringMap
class haxe_ds_StringMap:


	def __init__(self):
		self.h = {}
	# var h
	def set(self,key,value):
		self.h["$" + key] = value

	def get(self,key):
		return self.h.get("$" + key, None)

	def exists(self,key):
		return python_lib_DictImpl.hasKey(self.h, "$" + key)

	def remove(self,key):
		key = "$" + key
		if not python_lib_DictImpl.hasKey(self.h, key):
			return False
		
		del self.h[key]
		return True
	

	def keys(self):
		a = []
		for key in self.h:
			a.append(key[1:])
		it = a.__iter__()
		return python_HaxeIterator(it)
		
	

	def iterator(self):
		iter = self.keys()
		ref = self.h
		def _hx_local_2():
			def _hx_local_0():
				return iter.hasNext()
			def _hx_local_1():
				i = iter.next()
				return ref.get("$" + i, None)
			
			return _Hx_AnonObject(hasNext = _hx_local_0 ,next = _hx_local_1 )
		
		return _hx_local_2()
	

	def toString(self):
		s = _hx_StringIO()
		s1 = "{"
		s.write(s1)
		
		it = self.keys()
		_it = it
		while _it.hasNext():
			i = _it.next()
			s1 = Std.string(i)
			s.write(s1)
			
			s1 = " => "
			s.write(s1)
			
			x = Std.string(self.get(i))
			s1 = Std.string(x)
			s.write(s1)
			
			
			if it.hasNext():
				s1 = ", "
				s.write(s1)
			
			
		
		s1 = "}"
		s.write(s1)
		
		return s.getvalue()
	







haxe_ds_StringMap._hx_class = haxe_ds_StringMap
haxe_ds_StringMap._hx_class_name = "haxe.ds.StringMap"
_hx_classes['haxe.ds.StringMap'] = haxe_ds_StringMap
haxe_ds_StringMap._hx_fields = ["h"]
haxe_ds_StringMap._hx_props = []
haxe_ds_StringMap._hx_methods = ["set","get","exists","remove","keys","iterator","toString"]
haxe_ds_StringMap._hx_statics = []
haxe_ds_StringMap._hx_interfaces = [IMap]

# print haxe.ds.WeakMap.WeakMap
class haxe_ds_WeakMap:


	def __init__(self):
		raise _HxException("Not implemented for this platform")
	def set(self,key,value):
		None

	def get(self,key):
		return None

	def exists(self,key):
		return False

	def remove(self,key):
		return False

	def keys(self):
		return None

	def iterator(self):
		return None

	def toString(self):
		return None







haxe_ds_WeakMap._hx_class = haxe_ds_WeakMap
haxe_ds_WeakMap._hx_class_name = "haxe.ds.WeakMap"
_hx_classes['haxe.ds.WeakMap'] = haxe_ds_WeakMap
haxe_ds_WeakMap._hx_fields = []
haxe_ds_WeakMap._hx_props = []
haxe_ds_WeakMap._hx_methods = ["set","get","exists","remove","keys","iterator","toString"]
haxe_ds_WeakMap._hx_statics = []
haxe_ds_WeakMap._hx_interfaces = [IMap]

# print haxe.macro.Context.Context
class haxe_macro_Context:

	pass






haxe_macro_Context._hx_class = haxe_macro_Context
haxe_macro_Context._hx_class_name = "haxe.macro.Context"
_hx_classes['haxe.macro.Context'] = haxe_macro_Context
haxe_macro_Context._hx_fields = []
haxe_macro_Context._hx_props = []
haxe_macro_Context._hx_methods = []
haxe_macro_Context._hx_statics = []
haxe_macro_Context._hx_interfaces = []

class haxe_macro_Constant(_Hx_Enum):
	def __init__(self, t, i, p): 
		super(haxe_macro_Constant,self).__init__(t, i, p)


def _haxe_macro_Constant_statics_CFloat (f): 
	return haxe_macro_Constant("CFloat", 1, [f])
haxe_macro_Constant.CFloat = _haxe_macro_Constant_statics_CFloat

def _haxe_macro_Constant_statics_CIdent (s): 
	return haxe_macro_Constant("CIdent", 3, [s])
haxe_macro_Constant.CIdent = _haxe_macro_Constant_statics_CIdent

def _haxe_macro_Constant_statics_CInt (v): 
	return haxe_macro_Constant("CInt", 0, [v])
haxe_macro_Constant.CInt = _haxe_macro_Constant_statics_CInt

def _haxe_macro_Constant_statics_CRegexp (r,opt): 
	return haxe_macro_Constant("CRegexp", 4, [r,opt])
haxe_macro_Constant.CRegexp = _haxe_macro_Constant_statics_CRegexp

def _haxe_macro_Constant_statics_CString (s): 
	return haxe_macro_Constant("CString", 2, [s])
haxe_macro_Constant.CString = _haxe_macro_Constant_statics_CString
haxe_macro_Constant._hx_constructs = ["CFloat","CIdent","CInt","CRegexp","CString"]
haxe_macro_Constant._hx_class = haxe_macro_Constant
haxe_macro_Constant._hx_class_name = "haxe.macro.Constant"
_hx_classes['haxe.macro.Constant'] = haxe_macro_Constant

class haxe_macro_Binop(_Hx_Enum):
	def __init__(self, t, i, p): 
		super(haxe_macro_Binop,self).__init__(t, i, p)


haxe_macro_Binop.OpNotEq = haxe_macro_Binop("OpNotEq", 6, list())

haxe_macro_Binop.OpShr = haxe_macro_Binop("OpShr", 17, list())

haxe_macro_Binop.OpLt = haxe_macro_Binop("OpLt", 9, list())

haxe_macro_Binop.OpInterval = haxe_macro_Binop("OpInterval", 21, list())

haxe_macro_Binop.OpAssign = haxe_macro_Binop("OpAssign", 4, list())

haxe_macro_Binop.OpBoolOr = haxe_macro_Binop("OpBoolOr", 15, list())

haxe_macro_Binop.OpEq = haxe_macro_Binop("OpEq", 5, list())

haxe_macro_Binop.OpLte = haxe_macro_Binop("OpLte", 10, list())

haxe_macro_Binop.OpAdd = haxe_macro_Binop("OpAdd", 0, list())

haxe_macro_Binop.OpMult = haxe_macro_Binop("OpMult", 1, list())

def _haxe_macro_Binop_statics_OpAssignOp (op): 
	return haxe_macro_Binop("OpAssignOp", 20, [op])
haxe_macro_Binop.OpAssignOp = _haxe_macro_Binop_statics_OpAssignOp

haxe_macro_Binop.OpGt = haxe_macro_Binop("OpGt", 7, list())

haxe_macro_Binop.OpOr = haxe_macro_Binop("OpOr", 12, list())

haxe_macro_Binop.OpShl = haxe_macro_Binop("OpShl", 16, list())

haxe_macro_Binop.OpMod = haxe_macro_Binop("OpMod", 19, list())

haxe_macro_Binop.OpDiv = haxe_macro_Binop("OpDiv", 2, list())

haxe_macro_Binop.OpGte = haxe_macro_Binop("OpGte", 8, list())

haxe_macro_Binop.OpBoolAnd = haxe_macro_Binop("OpBoolAnd", 14, list())

haxe_macro_Binop.OpAnd = haxe_macro_Binop("OpAnd", 11, list())

haxe_macro_Binop.OpUShr = haxe_macro_Binop("OpUShr", 18, list())

haxe_macro_Binop.OpArrow = haxe_macro_Binop("OpArrow", 22, list())

haxe_macro_Binop.OpSub = haxe_macro_Binop("OpSub", 3, list())

haxe_macro_Binop.OpXor = haxe_macro_Binop("OpXor", 13, list())
haxe_macro_Binop._hx_constructs = ["OpNotEq","OpShr","OpLt","OpInterval","OpAssign","OpBoolOr","OpEq","OpLte","OpAdd","OpMult","OpAssignOp","OpGt","OpOr","OpShl","OpMod","OpDiv","OpGte","OpBoolAnd","OpAnd","OpUShr","OpArrow","OpSub","OpXor"]
haxe_macro_Binop._hx_class = haxe_macro_Binop
haxe_macro_Binop._hx_class_name = "haxe.macro.Binop"
_hx_classes['haxe.macro.Binop'] = haxe_macro_Binop

class haxe_macro_Unop(_Hx_Enum):
	def __init__(self, t, i, p): 
		super(haxe_macro_Unop,self).__init__(t, i, p)


haxe_macro_Unop.OpNeg = haxe_macro_Unop("OpNeg", 3, list())

haxe_macro_Unop.OpNegBits = haxe_macro_Unop("OpNegBits", 4, list())

haxe_macro_Unop.OpNot = haxe_macro_Unop("OpNot", 2, list())

haxe_macro_Unop.OpDecrement = haxe_macro_Unop("OpDecrement", 1, list())

haxe_macro_Unop.OpIncrement = haxe_macro_Unop("OpIncrement", 0, list())
haxe_macro_Unop._hx_constructs = ["OpNeg","OpNegBits","OpNot","OpDecrement","OpIncrement"]
haxe_macro_Unop._hx_class = haxe_macro_Unop
haxe_macro_Unop._hx_class_name = "haxe.macro.Unop"
_hx_classes['haxe.macro.Unop'] = haxe_macro_Unop

class haxe_macro_ExprDef(_Hx_Enum):
	def __init__(self, t, i, p): 
		super(haxe_macro_ExprDef,self).__init__(t, i, p)


def _haxe_macro_ExprDef_statics_EArrayDecl (values): 
	return haxe_macro_ExprDef("EArrayDecl", 6, [values])
haxe_macro_ExprDef.EArrayDecl = _haxe_macro_ExprDef_statics_EArrayDecl

def _haxe_macro_ExprDef_statics_EArray (e1,e2): 
	return haxe_macro_ExprDef("EArray", 1, [e1,e2])
haxe_macro_ExprDef.EArray = _haxe_macro_ExprDef_statics_EArray

def _haxe_macro_ExprDef_statics_EUntyped (e): 
	return haxe_macro_ExprDef("EUntyped", 22, [e])
haxe_macro_ExprDef.EUntyped = _haxe_macro_ExprDef_statics_EUntyped

def _haxe_macro_ExprDef_statics_EVars (vars): 
	return haxe_macro_ExprDef("EVars", 10, [vars])
haxe_macro_ExprDef.EVars = _haxe_macro_ExprDef_statics_EVars

def _haxe_macro_ExprDef_statics_ECall (e,params): 
	return haxe_macro_ExprDef("ECall", 7, [e,params])
haxe_macro_ExprDef.ECall = _haxe_macro_ExprDef_statics_ECall

def _haxe_macro_ExprDef_statics_EBlock (exprs): 
	return haxe_macro_ExprDef("EBlock", 12, [exprs])
haxe_macro_ExprDef.EBlock = _haxe_macro_ExprDef_statics_EBlock

def _haxe_macro_ExprDef_statics_EIf (econd,eif,eelse): 
	return haxe_macro_ExprDef("EIf", 15, [econd,eif,eelse])
haxe_macro_ExprDef.EIf = _haxe_macro_ExprDef_statics_EIf

def _haxe_macro_ExprDef_statics_ENew (t,params): 
	return haxe_macro_ExprDef("ENew", 8, [t,params])
haxe_macro_ExprDef.ENew = _haxe_macro_ExprDef_statics_ENew

def _haxe_macro_ExprDef_statics_ETry (e,catches): 
	return haxe_macro_ExprDef("ETry", 18, [e,catches])
haxe_macro_ExprDef.ETry = _haxe_macro_ExprDef_statics_ETry

def _haxe_macro_ExprDef_statics_EWhile (econd,e,normalWhile): 
	return haxe_macro_ExprDef("EWhile", 16, [econd,e,normalWhile])
haxe_macro_ExprDef.EWhile = _haxe_macro_ExprDef_statics_EWhile

def _haxe_macro_ExprDef_statics_ECheckType (e,t): 
	return haxe_macro_ExprDef("ECheckType", 28, [e,t])
haxe_macro_ExprDef.ECheckType = _haxe_macro_ExprDef_statics_ECheckType

haxe_macro_ExprDef.EContinue = haxe_macro_ExprDef("EContinue", 21, list())

def _haxe_macro_ExprDef_statics_EObjectDecl (fields): 
	return haxe_macro_ExprDef("EObjectDecl", 5, [fields])
haxe_macro_ExprDef.EObjectDecl = _haxe_macro_ExprDef_statics_EObjectDecl

def _haxe_macro_ExprDef_statics_EField (e,field): 
	return haxe_macro_ExprDef("EField", 3, [e,field])
haxe_macro_ExprDef.EField = _haxe_macro_ExprDef_statics_EField

def _haxe_macro_ExprDef_statics_EFor (it,expr): 
	return haxe_macro_ExprDef("EFor", 13, [it,expr])
haxe_macro_ExprDef.EFor = _haxe_macro_ExprDef_statics_EFor

def _haxe_macro_ExprDef_statics_EUnop (op,postFix,e): 
	return haxe_macro_ExprDef("EUnop", 9, [op,postFix,e])
haxe_macro_ExprDef.EUnop = _haxe_macro_ExprDef_statics_EUnop

def _haxe_macro_ExprDef_statics_EBinop (op,e1,e2): 
	return haxe_macro_ExprDef("EBinop", 2, [op,e1,e2])
haxe_macro_ExprDef.EBinop = _haxe_macro_ExprDef_statics_EBinop

def _haxe_macro_ExprDef_statics_EConst (c): 
	return haxe_macro_ExprDef("EConst", 0, [c])
haxe_macro_ExprDef.EConst = _haxe_macro_ExprDef_statics_EConst

def _haxe_macro_ExprDef_statics_EFunction (name,f): 
	return haxe_macro_ExprDef("EFunction", 11, [name,f])
haxe_macro_ExprDef.EFunction = _haxe_macro_ExprDef_statics_EFunction

def _haxe_macro_ExprDef_statics_EIn (e1,e2): 
	return haxe_macro_ExprDef("EIn", 14, [e1,e2])
haxe_macro_ExprDef.EIn = _haxe_macro_ExprDef_statics_EIn

def _haxe_macro_ExprDef_statics_ESwitch (e,cases,edef): 
	return haxe_macro_ExprDef("ESwitch", 17, [e,cases,edef])
haxe_macro_ExprDef.ESwitch = _haxe_macro_ExprDef_statics_ESwitch

def _haxe_macro_ExprDef_statics_ETernary (econd,eif,eelse): 
	return haxe_macro_ExprDef("ETernary", 27, [econd,eif,eelse])
haxe_macro_ExprDef.ETernary = _haxe_macro_ExprDef_statics_ETernary

def _haxe_macro_ExprDef_statics_ECast (e,t): 
	return haxe_macro_ExprDef("ECast", 24, [e,t])
haxe_macro_ExprDef.ECast = _haxe_macro_ExprDef_statics_ECast

haxe_macro_ExprDef.EBreak = haxe_macro_ExprDef("EBreak", 20, list())

def _haxe_macro_ExprDef_statics_EReturn (e): 
	return haxe_macro_ExprDef("EReturn", 19, [e])
haxe_macro_ExprDef.EReturn = _haxe_macro_ExprDef_statics_EReturn

def _haxe_macro_ExprDef_statics_EDisplayNew (t): 
	return haxe_macro_ExprDef("EDisplayNew", 26, [t])
haxe_macro_ExprDef.EDisplayNew = _haxe_macro_ExprDef_statics_EDisplayNew

def _haxe_macro_ExprDef_statics_EMeta (s,e): 
	return haxe_macro_ExprDef("EMeta", 29, [s,e])
haxe_macro_ExprDef.EMeta = _haxe_macro_ExprDef_statics_EMeta

def _haxe_macro_ExprDef_statics_EParenthesis (e): 
	return haxe_macro_ExprDef("EParenthesis", 4, [e])
haxe_macro_ExprDef.EParenthesis = _haxe_macro_ExprDef_statics_EParenthesis

def _haxe_macro_ExprDef_statics_EThrow (e): 
	return haxe_macro_ExprDef("EThrow", 23, [e])
haxe_macro_ExprDef.EThrow = _haxe_macro_ExprDef_statics_EThrow

def _haxe_macro_ExprDef_statics_EDisplay (e,isCall): 
	return haxe_macro_ExprDef("EDisplay", 25, [e,isCall])
haxe_macro_ExprDef.EDisplay = _haxe_macro_ExprDef_statics_EDisplay
haxe_macro_ExprDef._hx_constructs = ["EArrayDecl","EArray","EUntyped","EVars","ECall","EBlock","EIf","ENew","ETry","EWhile","ECheckType","EContinue","EObjectDecl","EField","EFor","EUnop","EBinop","EConst","EFunction","EIn","ESwitch","ETernary","ECast","EBreak","EReturn","EDisplayNew","EMeta","EParenthesis","EThrow","EDisplay"]
haxe_macro_ExprDef._hx_class = haxe_macro_ExprDef
haxe_macro_ExprDef._hx_class_name = "haxe.macro.ExprDef"
_hx_classes['haxe.macro.ExprDef'] = haxe_macro_ExprDef

class haxe_macro_ComplexType(_Hx_Enum):
	def __init__(self, t, i, p): 
		super(haxe_macro_ComplexType,self).__init__(t, i, p)


def _haxe_macro_ComplexType_statics_TAnonymous (fields): 
	return haxe_macro_ComplexType("TAnonymous", 2, [fields])
haxe_macro_ComplexType.TAnonymous = _haxe_macro_ComplexType_statics_TAnonymous

def _haxe_macro_ComplexType_statics_TExtend (p,fields): 
	return haxe_macro_ComplexType("TExtend", 4, [p,fields])
haxe_macro_ComplexType.TExtend = _haxe_macro_ComplexType_statics_TExtend

def _haxe_macro_ComplexType_statics_TOptional (t): 
	return haxe_macro_ComplexType("TOptional", 5, [t])
haxe_macro_ComplexType.TOptional = _haxe_macro_ComplexType_statics_TOptional

def _haxe_macro_ComplexType_statics_TPath (p): 
	return haxe_macro_ComplexType("TPath", 0, [p])
haxe_macro_ComplexType.TPath = _haxe_macro_ComplexType_statics_TPath

def _haxe_macro_ComplexType_statics_TFunction (args,ret): 
	return haxe_macro_ComplexType("TFunction", 1, [args,ret])
haxe_macro_ComplexType.TFunction = _haxe_macro_ComplexType_statics_TFunction

def _haxe_macro_ComplexType_statics_TParent (t): 
	return haxe_macro_ComplexType("TParent", 3, [t])
haxe_macro_ComplexType.TParent = _haxe_macro_ComplexType_statics_TParent
haxe_macro_ComplexType._hx_constructs = ["TAnonymous","TExtend","TOptional","TPath","TFunction","TParent"]
haxe_macro_ComplexType._hx_class = haxe_macro_ComplexType
haxe_macro_ComplexType._hx_class_name = "haxe.macro.ComplexType"
_hx_classes['haxe.macro.ComplexType'] = haxe_macro_ComplexType

class haxe_macro_TypeParam(_Hx_Enum):
	def __init__(self, t, i, p): 
		super(haxe_macro_TypeParam,self).__init__(t, i, p)


def _haxe_macro_TypeParam_statics_TPExpr (e): 
	return haxe_macro_TypeParam("TPExpr", 1, [e])
haxe_macro_TypeParam.TPExpr = _haxe_macro_TypeParam_statics_TPExpr

def _haxe_macro_TypeParam_statics_TPType (t): 
	return haxe_macro_TypeParam("TPType", 0, [t])
haxe_macro_TypeParam.TPType = _haxe_macro_TypeParam_statics_TPType
haxe_macro_TypeParam._hx_constructs = ["TPExpr","TPType"]
haxe_macro_TypeParam._hx_class = haxe_macro_TypeParam
haxe_macro_TypeParam._hx_class_name = "haxe.macro.TypeParam"
_hx_classes['haxe.macro.TypeParam'] = haxe_macro_TypeParam

class haxe_macro_Access(_Hx_Enum):
	def __init__(self, t, i, p): 
		super(haxe_macro_Access,self).__init__(t, i, p)


haxe_macro_Access.ADynamic = haxe_macro_Access("ADynamic", 4, list())

haxe_macro_Access.AOverride = haxe_macro_Access("AOverride", 3, list())

haxe_macro_Access.APrivate = haxe_macro_Access("APrivate", 1, list())

haxe_macro_Access.APublic = haxe_macro_Access("APublic", 0, list())

haxe_macro_Access.AMacro = haxe_macro_Access("AMacro", 6, list())

haxe_macro_Access.AInline = haxe_macro_Access("AInline", 5, list())

haxe_macro_Access.AStatic = haxe_macro_Access("AStatic", 2, list())
haxe_macro_Access._hx_constructs = ["ADynamic","AOverride","APrivate","APublic","AMacro","AInline","AStatic"]
haxe_macro_Access._hx_class = haxe_macro_Access
haxe_macro_Access._hx_class_name = "haxe.macro.Access"
_hx_classes['haxe.macro.Access'] = haxe_macro_Access

class haxe_macro_FieldType(_Hx_Enum):
	def __init__(self, t, i, p): 
		super(haxe_macro_FieldType,self).__init__(t, i, p)


def _haxe_macro_FieldType_statics_FFun (f): 
	return haxe_macro_FieldType("FFun", 1, [f])
haxe_macro_FieldType.FFun = _haxe_macro_FieldType_statics_FFun

def _haxe_macro_FieldType_statics_FProp (get,set,t,e): 
	return haxe_macro_FieldType("FProp", 2, [get,set,t,e])
haxe_macro_FieldType.FProp = _haxe_macro_FieldType_statics_FProp

def _haxe_macro_FieldType_statics_FVar (t,e): 
	return haxe_macro_FieldType("FVar", 0, [t,e])
haxe_macro_FieldType.FVar = _haxe_macro_FieldType_statics_FVar
haxe_macro_FieldType._hx_constructs = ["FFun","FProp","FVar"]
haxe_macro_FieldType._hx_class = haxe_macro_FieldType
haxe_macro_FieldType._hx_class_name = "haxe.macro.FieldType"
_hx_classes['haxe.macro.FieldType'] = haxe_macro_FieldType

class haxe_macro_TypeDefKind(_Hx_Enum):
	def __init__(self, t, i, p): 
		super(haxe_macro_TypeDefKind,self).__init__(t, i, p)


haxe_macro_TypeDefKind.TDEnum = haxe_macro_TypeDefKind("TDEnum", 0, list())

def _haxe_macro_TypeDefKind_statics_TDAbstract (tthis,_hx_from,to): 
	return haxe_macro_TypeDefKind("TDAbstract", 4, [tthis,_hx_from,to])
haxe_macro_TypeDefKind.TDAbstract = _haxe_macro_TypeDefKind_statics_TDAbstract

def _haxe_macro_TypeDefKind_statics_TDAlias (t): 
	return haxe_macro_TypeDefKind("TDAlias", 3, [t])
haxe_macro_TypeDefKind.TDAlias = _haxe_macro_TypeDefKind_statics_TDAlias

def _haxe_macro_TypeDefKind_statics_TDClass (superClass,interfaces,isInterface): 
	return haxe_macro_TypeDefKind("TDClass", 2, [superClass,interfaces,isInterface])
haxe_macro_TypeDefKind.TDClass = _haxe_macro_TypeDefKind_statics_TDClass

haxe_macro_TypeDefKind.TDStructure = haxe_macro_TypeDefKind("TDStructure", 1, list())
haxe_macro_TypeDefKind._hx_constructs = ["TDEnum","TDAbstract","TDAlias","TDClass","TDStructure"]
haxe_macro_TypeDefKind._hx_class = haxe_macro_TypeDefKind
haxe_macro_TypeDefKind._hx_class_name = "haxe.macro.TypeDefKind"
_hx_classes['haxe.macro.TypeDefKind'] = haxe_macro_TypeDefKind

# print haxe.macro.Expr.Error
class haxe_macro_Error:


	def __init__(self,m,p):
		self.message = m
		self.pos = p
	
	# var message
	# var pos
	def toString(self):
		return self.message







haxe_macro_Error._hx_class = haxe_macro_Error
haxe_macro_Error._hx_class_name = "haxe.macro.Error"
_hx_classes['haxe.macro.Error'] = haxe_macro_Error
haxe_macro_Error._hx_fields = ["message","pos"]
haxe_macro_Error._hx_props = []
haxe_macro_Error._hx_methods = ["toString"]
haxe_macro_Error._hx_statics = []
haxe_macro_Error._hx_interfaces = []

# print hxsublime.Codegen.HaxeImportGenerator
class hxsublime_HaxeImportGenerator:


	def __init__(self,panel,view):
		self.view = view
		self.panel = panel
		self.start = None
		self.size = None
		self.cname = None
	
	# var panel
	# var start
	# var size
	# var cname
	# var view
	def getEnd(self,src,offset):
		end = __builtin__.len(src)
		while offset < end:
			c = src[offset]
			offset = offset + 1
			if hxsublime_tools_Regex.word_chars.match(c) is None:
				break
			
		
		return offset - 1
	

	def getStart(self,src,offset):
		found_word = 0
		offset = offset - 1
		while offset > 0:
			c = src[offset]
			offset = offset - 1
			if found_word == 0:
				if hxsublime_tools_Regex.space_chars.match(c) is not None:
					continue
				
				found_word = 1
			
			
			if hxsublime_tools_Regex.word_chars.match(c) is None:
				break
			
		
		return offset + 2
	

	def isMemberName(self,token):
		return token[0] >= "Z" or token == token.upper()

	def getClassName(self,view,src):
		loc = view.sel()[0]
		end = __builtin__.max(loc.a, loc.b)
		self.size = loc.size()
		if self.size == 0:
			end = self.getEnd(src, end)
			self.start = self.getStart(src, end)
			self.size = end - self.start
		
		else:
			self.start = end - self.size
		s = view.substr(sublime_Region(self.start, end))
		self.cname = s.rpartition(".")
		
		while not (self.cname[0] == "") and self.isMemberName(self.cname[2]):
			def _hx_local_0():
				_this = self.cname[2]
				return __builtin__.len(_this)
			
			self.size = self.size - 1 + _hx_local_0()
			s = self.cname[0]
			self.cname = s.rpartition(".")
			
		
		return self.cname
	

	def compactClassName(self,edit,view):
		view.replace(edit, sublime_Region(self.start, self.start + self.size), self.cname[2])
		view.sel().clear()
		loc = None
		def _hx_local_0():
			_this = self.cname[2]
			return __builtin__.len(_this)
		
		loc = self.start + _hx_local_0()
		view.sel().add(sublime_Region(loc, loc))
	

	def getIndent(self,src,index):
		if src[index] == "\n":
			return index + 1
		
		return index
	

	def insertStatement(self,edit,view,src,statement,regex):
		cname = self.cname[0] + self.cname[1] + self.cname[2]
		clow = cname.lower()
		last = None
		def _hx_local_0():
			p = regex.finditer(src)
			return python_HaxeIterator(p)
		
		_it = _hx_local_0()
		while _it.hasNext():
			imp = _it.next()
			def _hx_local_1():
				_this = imp.group(2)
				return _this.lower()
			
			if clow < _hx_local_1():
				ins = python_lib_StringTools.format("{0}{1} {2};\n", [imp.group(1), statement, cname])
				view.insert(edit, self.getIndent(src, imp.start(0)), ins)
				return
			
			
			last = imp
		
		if last is not None:
			ins = python_lib_StringTools.format(";\n{0}{1} {2}", [last.group(1), statement, cname])
			view.insert(edit, last.end(2), ins)
		
		else:
			pkg = hxsublime_tools_Regex.package_line.search(src)
			if pkg is not None:
				ins = python_lib_StringTools.format("\n\n{0} {1};", [statement, cname])
				view.insert(edit, pkg.end(0), ins)
			
			else:
				ins = python_lib_StringTools.format("{0} {1};\n\n", [statement, cname])
				view.insert(edit, 0, ins)
			
		
	

	def generateStatement(self,edit,statement,regex):
		view = self.view
		src = view.substr(sublime_Region(0, view.size()))
		cname = self.getClassName(view, src)
		if cname[1] == "" and statement == "import":
			sublime_Sublime.status_message("Nothing to " + statement)
			self.panel.writeln("Nothing to " + statement)
			return
		
		
		self.compactClassName(edit, view)
		fcname = cname[0] + cname[1] + cname[2]
		if python_lib_Re.search(statement + "\\s+${fcname};", src) is not None:
			info = None
			if statement == "import":
				info = "imported"
			else:
				info = "used"
			sublime_Sublime.status_message("Already " + info)
			self.panel.writeln("Already " + info)
			return
		
		
		self.insertStatement(edit, view, src, statement, regex)
	





def HaxeImportGenerator_statics_generateUsing(view,edit):
	p = hxsublime_HaxeImportGenerator(hxsublime_panel_Panels.defaultPanel(), view)
	return p.generateStatement(edit, "using", hxsublime_tools_Regex.using_line)
	
hxsublime_HaxeImportGenerator.generateUsing = HaxeImportGenerator_statics_generateUsing
def HaxeImportGenerator_statics_generateImport(view,edit):
	p = hxsublime_HaxeImportGenerator(hxsublime_panel_Panels.defaultPanel(), view)
	return p.generateStatement(edit, "import", hxsublime_tools_Regex.import_line)
	
hxsublime_HaxeImportGenerator.generateImport = HaxeImportGenerator_statics_generateImport


hxsublime_HaxeImportGenerator._hx_class = hxsublime_HaxeImportGenerator
hxsublime_HaxeImportGenerator._hx_class_name = "hxsublime.HaxeImportGenerator"
_hx_classes['hxsublime.HaxeImportGenerator'] = hxsublime_HaxeImportGenerator
hxsublime_HaxeImportGenerator._hx_fields = ["panel","start","size","cname","view"]
hxsublime_HaxeImportGenerator._hx_props = []
hxsublime_HaxeImportGenerator._hx_methods = ["getEnd","getStart","isMemberName","getClassName","compactClassName","getIndent","insertStatement","generateStatement"]
hxsublime_HaxeImportGenerator._hx_statics = ["generateUsing","generateImport"]
hxsublime_HaxeImportGenerator._hx_interfaces = []

# print hxsublime.Config.NmeTarget
class hxsublime_NmeTarget:


	def __init__(self,name,plattform,args):
		self.name = name
		self.plattform = plattform
		self.args = args
	
	# var name
	# var plattform
	# var args






hxsublime_NmeTarget._hx_class = hxsublime_NmeTarget
hxsublime_NmeTarget._hx_class_name = "hxsublime.NmeTarget"
_hx_classes['hxsublime.NmeTarget'] = hxsublime_NmeTarget
hxsublime_NmeTarget._hx_fields = ["name","plattform","args"]
hxsublime_NmeTarget._hx_props = []
hxsublime_NmeTarget._hx_methods = []
hxsublime_NmeTarget._hx_statics = []
hxsublime_NmeTarget._hx_interfaces = []

# print hxsublime.Config.OpenFlTarget
class hxsublime_OpenFlTarget:


	def __init__(self,name,plattform,args):
		self.name = name
		self.plattform = plattform
		self.args = args
	
	# var name
	# var plattform
	# var args






hxsublime_OpenFlTarget._hx_class = hxsublime_OpenFlTarget
hxsublime_OpenFlTarget._hx_class_name = "hxsublime.OpenFlTarget"
_hx_classes['hxsublime.OpenFlTarget'] = hxsublime_OpenFlTarget
hxsublime_OpenFlTarget._hx_fields = ["name","plattform","args"]
hxsublime_OpenFlTarget._hx_props = []
hxsublime_OpenFlTarget._hx_methods = []
hxsublime_OpenFlTarget._hx_statics = []
hxsublime_OpenFlTarget._hx_interfaces = []

# print hxsublime.Config.Config
class hxsublime_Config:

	pass




hxsublime_Config.target_packages = ["flash", "flash8", "neko", "js", "php", "cpp", "cs", "java", "sys"]
hxsublime_Config.targets = ["js", "cpp", "swf8", "swf", "neko", "php", "java", "cs", "as3"]
def _hx_init_hxsublime_Config_target_std_packages():
	_g = haxe_ds_StringMap()
	_g.set("js", ["js"])
	_g.set("cpp", ["cpp", "sys"])
	_g.set("neko", ["neko", "sys"])
	_g.set("php", ["php", "sys"])
	_g.set("java", ["java", "sys"])
	_g.set("cs", ["cs", "sys"])
	_g.set("swf", ["flash"])
	_g.set("as3", ["flash"])
	_g.set("swf8", ["flash8"])
	return _g
	
hxsublime_Config.target_std_packages = _hx_init_hxsublime_Config_target_std_packages()
hxsublime_Config.ignored_folders_list = [".git", ".svn"]
def Config_statics_mk_ignored_folders():
	x = haxe_ds_StringMap()
	_g = 0
	_g1 = hxsublime_Config.ignored_folders_list
	while _g < len(_g1):
		p = _g1[_g]
		_g = _g + 1
		x.set(p, True)
	
	
	return x
	
hxsublime_Config.mk_ignored_folders = Config_statics_mk_ignored_folders
hxsublime_Config.ignored_folders = hxsublime_Config.mk_ignored_folders()
hxsublime_Config.ignored_packages_list = ["neko._std", "cpp._std", "php._std", "js._std", "flash._std"]
def Config_statics_mk_ignored_packages():
	x = haxe_ds_StringMap()
	_g = 0
	_g1 = hxsublime_Config.ignored_folders_list
	while _g < len(_g1):
		p = _g1[_g]
		_g = _g + 1
		x.set(p, True)
	
	
	return x
	
hxsublime_Config.mk_ignored_packages = Config_statics_mk_ignored_packages
hxsublime_Config.ignored_packages = hxsublime_Config.mk_ignored_packages()
hxsublime_Config.ignored_types = ["haxe.io.BytesData.Unsigned_char__"]
hxsublime_Config.nme_targets = [hxsublime_NmeTarget("Flash", "flash", ["-debug"]), hxsublime_NmeTarget("HTML5", "html5", ["-debug"]), hxsublime_NmeTarget("C++", "cpp", ["-debug"]), hxsublime_NmeTarget("Windows", "windows", ["-debug"]), hxsublime_NmeTarget("Mac", "mac", ["-debug"]), hxsublime_NmeTarget("Linux", "linux", ["-debug"]), hxsublime_NmeTarget("Linux 64", "linux", ["-64 -debug"]), hxsublime_NmeTarget("iOs - iPhone simulator", "ios", ["-simulator -debug"]), hxsublime_NmeTarget("iOs - iPad simulator", "ios", ["-simulator -ipad -debug"]), hxsublime_NmeTarget("iOs - update XCode project", "ios", ["-ipad -debug"]), hxsublime_NmeTarget("Neko", "neko", ["-debug"]), hxsublime_NmeTarget("Neko 64", "neko", ["-64 -debug"]), hxsublime_NmeTarget("WebOs", "webos", ["-debug"]), hxsublime_NmeTarget("BlackBerry", "blackberry", ["-debug"]), hxsublime_NmeTarget("Android", "android", ["-debug"])]
hxsublime_Config.openfl_targets = [hxsublime_OpenFlTarget("Flash", "flash", ["-debug"]), hxsublime_OpenFlTarget("HTML5", "html5", ["-debug"]), hxsublime_OpenFlTarget("C++", "cpp", ["-debug"]), hxsublime_OpenFlTarget("Windows", "windows", ["-debug"]), hxsublime_OpenFlTarget("Mac", "mac", ["-debug"]), hxsublime_OpenFlTarget("Linux", "linux", ["-debug"]), hxsublime_OpenFlTarget("Linux 64", "linux", ["-64 -debug"]), hxsublime_OpenFlTarget("iOs - iPhone simulator", "ios", ["-simulator -debug"]), hxsublime_OpenFlTarget("iOs - iPad simulator", "ios", ["-simulator -ipad -debug"]), hxsublime_OpenFlTarget("iOs - update XCode project", "ios", ["-ipad -debug"]), hxsublime_OpenFlTarget("Neko", "neko", ["-debug"]), hxsublime_OpenFlTarget("Neko 64", "neko", ["-64 -debug"]), hxsublime_OpenFlTarget("Emscripten", "emscripten", ["-debug"]), hxsublime_OpenFlTarget("WebOs", "webos", ["-debug"]), hxsublime_OpenFlTarget("BlackBerry", "blackberry", ["-debug"]), hxsublime_OpenFlTarget("Android", "android", ["-debug"])]
hxsublime_Config.SOURCE_HAXE = "source.haxe.2"
hxsublime_Config.SOURCE_HXML = "source.hxml"
hxsublime_Config.SOURCE_NMML = "source.nmml"
hxsublime_Config.SOURCE_ERAZOR = "source.erazor"
hxsublime_Config.HXSL_SUFFIX = ".hxsl"


hxsublime_Config._hx_class = hxsublime_Config
hxsublime_Config._hx_class_name = "hxsublime.Config"
_hx_classes['hxsublime.Config'] = hxsublime_Config
hxsublime_Config._hx_fields = []
hxsublime_Config._hx_props = []
hxsublime_Config._hx_methods = []
hxsublime_Config._hx_statics = ["target_packages","targets","target_std_packages","ignored_folders_list","mk_ignored_folders","ignored_folders","ignored_packages_list","mk_ignored_packages","ignored_packages","ignored_types","nme_targets","openfl_targets","SOURCE_HAXE","SOURCE_HXML","SOURCE_NMML","SOURCE_ERAZOR","HXSL_SUFFIX"]
hxsublime_Config._hx_interfaces = []

# print python.lib.Types.BaseException
# print python.lib.Types.Exception
# print hxsublime.Exceptions.ExtractBuildPathException
class hxsublime_ExtractBuildPathException(Exception):


	def __init__(self,build):
		super().__init__("Cannot ExtractBuildPath from build " + Std.string(build))






hxsublime_ExtractBuildPathException._hx_class = hxsublime_ExtractBuildPathException
hxsublime_ExtractBuildPathException._hx_class_name = "hxsublime.ExtractBuildPathException"
_hx_classes['hxsublime.ExtractBuildPathException'] = hxsublime_ExtractBuildPathException
hxsublime_ExtractBuildPathException._hx_fields = []
hxsublime_ExtractBuildPathException._hx_props = []
hxsublime_ExtractBuildPathException._hx_methods = []
hxsublime_ExtractBuildPathException._hx_statics = []
hxsublime_ExtractBuildPathException._hx_interfaces = []
hxsublime_ExtractBuildPathException._hx_super = Exception

# print hxsublime.Exceptions.GetRelativePathException
class hxsublime_GetRelativePathException(Exception):


	def __init__(self,build,file):
		super().__init__("Cannot get the relative path of " + Std.string(file) + " for build " + Std.string(build))






hxsublime_GetRelativePathException._hx_class = hxsublime_GetRelativePathException
hxsublime_GetRelativePathException._hx_class_name = "hxsublime.GetRelativePathException"
_hx_classes['hxsublime.GetRelativePathException'] = hxsublime_GetRelativePathException
hxsublime_GetRelativePathException._hx_fields = []
hxsublime_GetRelativePathException._hx_props = []
hxsublime_GetRelativePathException._hx_methods = []
hxsublime_GetRelativePathException._hx_statics = []
hxsublime_GetRelativePathException._hx_interfaces = []
hxsublime_GetRelativePathException._hx_super = Exception

# print hxsublime.Exceptions.CreateTempFileOrFolderException
class hxsublime_CreateTempFileOrFolderException(Exception):


	def __init__(self,build,file_or_folder):
		super().__init__("Cannot create temp file or folder (" + Std.string(file_or_folder) + ") from build (" + Std.string(build) + ")")






hxsublime_CreateTempFileOrFolderException._hx_class = hxsublime_CreateTempFileOrFolderException
hxsublime_CreateTempFileOrFolderException._hx_class_name = "hxsublime.CreateTempFileOrFolderException"
_hx_classes['hxsublime.CreateTempFileOrFolderException'] = hxsublime_CreateTempFileOrFolderException
hxsublime_CreateTempFileOrFolderException._hx_fields = []
hxsublime_CreateTempFileOrFolderException._hx_props = []
hxsublime_CreateTempFileOrFolderException._hx_methods = []
hxsublime_CreateTempFileOrFolderException._hx_statics = []
hxsublime_CreateTempFileOrFolderException._hx_interfaces = []
hxsublime_CreateTempFileOrFolderException._hx_super = Exception

# print hxsublime.Execute.Execute
class hxsublime_Execute:

	pass




def Execute_statics_runCmdAsync(args,callback,input = None,cwd = None,env = None):
	if input is None:
		input = None
	
	if cwd is None:
		cwd = None
	
	if env is None:
		env = None
	
	def _hx_local_2():
		r = hxsublime_Execute.runCmd(args, input, cwd, env)
		out = r[0]
		err = r[1]
		def _hx_local_0():
			f = callback
			a1 = out
			a2 = err
			def _hx_local_1():
				return f(a1, a2)
			return _hx_local_1
		
		sublime_Sublime.set_timeout(_hx_local_0(), 1)
	
	inMainThread = _hx_local_2
	python_lib_ThreadLowLevel.start_new_thread(inMainThread, __builtin__.tuple())
	
hxsublime_Execute.runCmdAsync = Execute_statics_runCmdAsync
def Execute_statics_runCmd(args,input = None,cwd = None,env = None):
	if input is None:
		input = None
	
	if cwd is None:
		cwd = None
	
	if env is None:
		env = None
	
	if cwd is None:
		cwd = "."
	
	try:
		base_env = python_lib_Os.environ.copy()
		if env is not None:
			base_env.update(env)
		
		env1 = base_env
		def _hx_local_0():
			p = None
			_this = env1.keys()
			p = __builtin__.iter(_this)
			
			return python_HaxeIterator(p)
		
		_it = _hx_local_0()
		while _it.hasNext():
			k = _it.next()
			val = env1.get(k, None)
			val1 = python_lib_os_Path.expandvars(val)
			python_lib_DictImpl.set(env1, k, val1)
			
		
		def _hx_local_1(s):
			return s != ""
		cmdArgs = __builtin__.list(__builtin__.filter(_hx_local_1, args))
		p = None
		o = _Hx_AnonObject(cwd = cwd ,stdout = python_lib_Subprocess.PIPE ,stderr = python_lib_Subprocess.PIPE ,stdin = python_lib_Subprocess.PIPE ,startupinfo = hxsublime_Plugin.startupInfo() ,env = env1 )
		if Reflect.hasField(o, "bufsize"):
			o.bufsize = o.bufsize
		else:
			o.bufsize = 0
		if Reflect.hasField(o, "executable"):
			o.executable = o.executable
		else:
			o.executable = None
		if Reflect.hasField(o, "stdin"):
			o.stdin = o.stdin
		else:
			o.stdin = None
		if Reflect.hasField(o, "stdout"):
			o.stdout = o.stdout
		else:
			o.stdout = None
		if Reflect.hasField(o, "stderr"):
			o.stderr = o.stderr
		else:
			o.stderr = None
		if Reflect.hasField(o, "preexec_fn"):
			o.preexec_fn = o.preexec_fn
		else:
			o.preexec_fn = None
		if Reflect.hasField(o, "close_fds"):
			o.close_fds = o.close_fds
		else:
			o.close_fds = None
		if Reflect.hasField(o, "shell"):
			o.shell = o.shell
		else:
			o.shell = None
		if Reflect.hasField(o, "cwd"):
			o.cwd = o.cwd
		else:
			o.cwd = None
		if Reflect.hasField(o, "env"):
			o.env = o.env
		else:
			o.env = None
		if Reflect.hasField(o, "universal_newlines"):
			o.universal_newlines = o.universal_newlines
		else:
			o.universal_newlines = None
		if Reflect.hasField(o, "startupinfo"):
			o.startupinfo = o.startupinfo
		else:
			o.startupinfo = None
		if Reflect.hasField(o, "creationflags"):
			o.creationflags = o.creationflags
		else:
			o.creationflags = 0
		p = python_lib_subprocess_Popen(cmdArgs, o.bufsize, o.executable, o.stdin, o.stdout, o.stderr, o.preexec_fn, o.close_fds, o.shell, o.cwd, o.env, o.universal_newlines, o.startupinfo, o.creationflags)
		
		inputBytes = None
		if input is not None:
			inputBytes = python_lib_StringTools.encode(input, "utf-8")
		else:
			inputBytes = None
		r = p.communicate(inputBytes)
		out = r[0]
		err = r[1]
		a = out.decode("utf-8")
		b = err.decode("utf-8")
		return (a, b)
		
	
	except Exception as _hx_e:
		_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
		if True:
			e = _hx_e1
			haxe_Log.trace(e, _Hx_AnonObject(fileName = "Execute.hx" ,lineNumber = 68 ,className = "hxsublime.Execute" ,methodName = "runCmd" ))
			p = args[0]
			err = "Error while running " + p + ": in " + cwd + " (" + Std.string(e) + ")"
			return ("", err)
	
		else:
			raise _hx_e
	
hxsublime_Execute.runCmd = Execute_statics_runCmd


hxsublime_Execute._hx_class = hxsublime_Execute
hxsublime_Execute._hx_class_name = "hxsublime.Execute"
_hx_classes['hxsublime.Execute'] = hxsublime_Execute
hxsublime_Execute._hx_fields = []
hxsublime_Execute._hx_props = []
hxsublime_Execute._hx_methods = []
hxsublime_Execute._hx_statics = ["runCmdAsync","runCmd"]
hxsublime_Execute._hx_interfaces = []

# print hxsublime.Haxelib.HaxeLibLibrary
class hxsublime_HaxeLibLibrary:


	def __init__(self,manager,name,dev,version):
		self.name = name
		self.dev = dev
		self.version = version
		self.classes = None
		self.packages = None
		if dev:
			self.path = version
			self.version = "dev"
		
		else:
			def _hx_local_0():
				_this = self.version.split(".")
				return ",".join(_this)
			
			self.path = python_lib_os_Path.join(manager.basePath, name, _hx_local_0())
		
	
	# var name
	# var dev
	# var version
	# var classes
	# var packages
	# var path
	def as_cmd_arg(self):
		return self.name + ":" + self.version

	def extract_types(self):
		if self.dev or self.classes is None and self.packages is None:
			t = hxsublime_Types.extractTypes(self.path)
			self.classes = t.allTypes()
			self.packages = t.packs()
		
		
		return (self.classes, self.packages)
	







hxsublime_HaxeLibLibrary._hx_class = hxsublime_HaxeLibLibrary
hxsublime_HaxeLibLibrary._hx_class_name = "hxsublime.HaxeLibLibrary"
_hx_classes['hxsublime.HaxeLibLibrary'] = hxsublime_HaxeLibLibrary
hxsublime_HaxeLibLibrary._hx_fields = ["name","dev","version","classes","packages","path"]
hxsublime_HaxeLibLibrary._hx_props = []
hxsublime_HaxeLibLibrary._hx_methods = ["as_cmd_arg","extract_types"]
hxsublime_HaxeLibLibrary._hx_statics = []
hxsublime_HaxeLibLibrary._hx_interfaces = []

# print python.lib.Re.Re
import re as python_lib_Re
# print hxsublime.Haxelib.HaxeLibManager
class hxsublime_HaxeLibManager:


	def __init__(self,project):
		self._available = haxe_ds_StringMap()
		self.basePath = None
		self.scanned = False
		self.project = project
	
	# var _available
	# var project
	# var basePath
	# var scanned
	def available(self):
		if not self.scanned:
			self.scan()
		
		return self._available
	

	def get(self,name):
		if self.available().exists(name):
			return self.available().get(name)
		else:
			sublime_Sublime.status_message("Haxelib : " + name + " project not installed")
			return None
	

	def getCompletions(self):
		comps = []
		_it = self.available().keys()
		while _it.hasNext():
			k = _it.next()
			lib = self.available().get(k)
			haxe_Log.trace(lib, _Hx_AnonObject(fileName = "Haxelib.hx" ,lineNumber = 107 ,className = "hxsublime.HaxeLibManager" ,methodName = "getCompletions" ))
			x = (lib.name + " [" + lib.version + "]", lib.name)
			comps.append(x)
			__builtin__.len(comps)
			
			
		
		return comps
	

	def scan(self):
		self.scanned = True
		env = self.project.haxeEnv()
		cmd = self.project.haxelibExec()
		cmd.append("config")
		__builtin__.len(cmd)
		
		r = hxsublime_Execute.runCmd(cmd, None, None, env)
		hlout = r[0]
		hlerr = r[1]
		self.basePath = hlout.strip(None)
		self._available = haxe_ds_StringMap()
		cmd1 = self.project.haxelibExec()
		cmd1.append("list")
		__builtin__.len(cmd1)
		
		r1 = hxsublime_Execute.runCmd(cmd1, None, None, env)
		hlout1 = r1[0]
		hlerr1 = r1[1]
		_g = 0
		_g1 = hlout1.split("\n")
		while _g < len(_g1):
			l = _g1[_g]
			_g = _g + 1
			found = hxsublime_HaxeLibManager.libLine.match(l)
			if found is not None:
				g = found.groups(None)
				if g is not None:
					name = g[0]
					dev = g[1]
					version = g[2]
					lib = hxsublime_HaxeLibLibrary(self, name, dev is not None, version)
					self._available.set(name, lib)
				
				
			
			
		
		
	

	def installLib(self,lib):
		cmd = self.project.haxelibExec()
		env = self.project.haxeEnv()
		cmd.append("install")
		__builtin__.len(cmd)
		
		cmd.append(lib)
		__builtin__.len(cmd)
		
		haxe_Log.trace(Std.string(cmd), _Hx_AnonObject(fileName = "Haxelib.hx" ,lineNumber = 160 ,className = "hxsublime.HaxeLibManager" ,methodName = "installLib" ))
		hxsublime_Execute.runCmd(cmd, None, None, env)
		self.scan()
	

	def removeLib(self,lib):
		cmd = self.project.haxelibExec()
		env = self.project.haxeEnv()
		cmd.append("remove")
		__builtin__.len(cmd)
		
		cmd.append(lib)
		__builtin__.len(cmd)
		
		haxe_Log.trace(Std.string(cmd), _Hx_AnonObject(fileName = "Haxelib.hx" ,lineNumber = 171 ,className = "hxsublime.HaxeLibManager" ,methodName = "removeLib" ))
		hxsublime_Execute.runCmd(cmd, None, None, env)
		self.scan()
	

	def upgradeAll(self):
		cmd = self.project.haxelibExec()
		env = self.project.haxeEnv()
		cmd.append("upgrade")
		__builtin__.len(cmd)
		
		haxe_Log.trace(Std.string(cmd), _Hx_AnonObject(fileName = "Haxelib.hx" ,lineNumber = 181 ,className = "hxsublime.HaxeLibManager" ,methodName = "upgradeAll" ))
		hxsublime_Execute.runCmd(cmd, None, None, env)
		self.scan()
	

	def selfUpdate(self):
		cmd = self.project.haxelibExec()
		env = self.project.haxeEnv()
		cmd.append("thisupdate")
		__builtin__.len(cmd)
		
		haxe_Log.trace(Std.string(cmd), _Hx_AnonObject(fileName = "Haxelib.hx" ,lineNumber = 191 ,className = "hxsublime.HaxeLibManager" ,methodName = "selfUpdate" ))
		hxsublime_Execute.runCmd(cmd, None, None, env)
		self.scan()
	

	def searchLibs(self):
		cmd = self.project.haxelibExec()
		env = self.project.haxeEnv()
		cmd.append("search")
		__builtin__.len(cmd)
		
		cmd.append("_")
		__builtin__.len(cmd)
		
		res = hxsublime_Execute.runCmd(cmd, None, None, env)
		out = res[0]
		err = res[1]
		return self.parseLibraries(out)
	

	def parseLibraries(self,out):
		x = None
		_this = out.split("\n")
		def _hx_local_0(x1):
			return x1 != "" and x1.find("libraries found") == -1
		x = __builtin__.list(__builtin__.filter(_hx_local_0, _this))
		
		x.reverse()
		return x
	

	def isLibInstalled(self,lib):
		return self.available().exists(lib)

	def getLib(self,lib):
		return self.available().get(lib)





hxsublime_HaxeLibManager.__meta__ = _Hx_AnonObject(fields = _Hx_AnonObject(available = _Hx_AnonObject(property = None ) ) )
hxsublime_HaxeLibManager.libLine = python_lib_Re.compile("([^:]*):[^\\[]*\\[(dev\\:)?(.*)\\]")


hxsublime_HaxeLibManager._hx_class = hxsublime_HaxeLibManager
hxsublime_HaxeLibManager._hx_class_name = "hxsublime.HaxeLibManager"
_hx_classes['hxsublime.HaxeLibManager'] = hxsublime_HaxeLibManager
hxsublime_HaxeLibManager._hx_fields = ["_available","project","basePath","scanned"]
hxsublime_HaxeLibManager._hx_props = []
hxsublime_HaxeLibManager._hx_methods = ["available","get","getCompletions","scan","installLib","removeLib","upgradeAll","selfUpdate","searchLibs","parseLibraries","isLibInstalled","getLib"]
hxsublime_HaxeLibManager._hx_statics = ["__meta__","libLine"]
hxsublime_HaxeLibManager._hx_interfaces = []

# print hxsublime.Log.Log
class hxsublime_Log:

	pass




def Log_statics_debug(msg):
	hxsublime_Log.log(msg, False)
hxsublime_Log.debug = Log_statics_debug
def Log_statics_log(msg,to_file = False):
	if to_file is None:
		to_file = False
	
	msgStr = Std.string(msg)
	if to_file:
		f = python_lib_Codecs.open("st3_haxe_log.txt", "ab", "utf-8", "ignore")
		f.write(msgStr + "\n")
		f.close()
	
	elif hxsublime_Settings.useDebugPanel():
		def _hx_local_0():
			hxsublime_panel_Panels.debugPanel().writeln(msg)
		f = _hx_local_0
		sublime_Sublime.set_timeout(f, 100)
	
	else:
		try:
			haxe_Log.trace(msgStr, _Hx_AnonObject(fileName = "Log.hx" ,lineNumber = 34 ,className = "hxsublime.Log" ,methodName = "log" ))
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			if True:
				e = _hx_e1
				None
			else:
				raise _hx_e
	
hxsublime_Log.log = Log_statics_log


hxsublime_Log._hx_class = hxsublime_Log
hxsublime_Log._hx_class_name = "hxsublime.Log"
_hx_classes['hxsublime.Log'] = hxsublime_Log
hxsublime_Log._hx_fields = []
hxsublime_Log._hx_props = []
hxsublime_Log._hx_methods = []
hxsublime_Log._hx_statics = ["debug","log"]
hxsublime_Log._hx_interfaces = []

# print hxsublime.Main.Main
class hxsublime_Main:

	pass




def Main_statics_main():
	None
hxsublime_Main.main = Main_statics_main


hxsublime_Main._hx_class = hxsublime_Main
hxsublime_Main._hx_class_name = "hxsublime.Main"
_hx_classes['hxsublime.Main'] = hxsublime_Main
hxsublime_Main._hx_fields = []
hxsublime_Main._hx_props = []
hxsublime_Main._hx_methods = []
hxsublime_Main._hx_statics = ["main"]
hxsublime_Main._hx_interfaces = []

# print hxsublime.Plugin.Plugin
class hxsublime_Plugin:

	pass




hxsublime_Plugin._startupInfo = None
def Plugin_statics_plugin_base_dir():
	return python_lib_os_Path.abspath(python_lib_os_Path.join(python_lib_os_Path.dirname(__file__), "."))
hxsublime_Plugin.plugin_base_dir = Plugin_statics_plugin_base_dir
def Plugin_statics_startupInfo():
	if hxsublime_Plugin._startupInfo is not None:
		return hxsublime_Plugin._startupInfo
	
	try:
		hxsublime_Plugin._startupInfo = python_lib_Subprocess.STARTUPINFO()
		hxsublime_Plugin._startupInfo.dwFlags = hxsublime_Plugin._startupInfo.dwFlags | python_lib_Subprocess.STARTF_USESHOWWINDOW
		hxsublime_Plugin._startupInfo.wShowWindow = python_lib_Subprocess.SW_HIDE
	
	except Exception as _hx_e:
		_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
		if isinstance(_hx_e1, AttributeError):
			e = _hx_e1
			hxsublime_Plugin._startupInfo = None
		else:
			raise _hx_e
	return hxsublime_Plugin._startupInfo
	
hxsublime_Plugin.startupInfo = Plugin_statics_startupInfo


hxsublime_Plugin._hx_class = hxsublime_Plugin
hxsublime_Plugin._hx_class_name = "hxsublime.Plugin"
_hx_classes['hxsublime.Plugin'] = hxsublime_Plugin
hxsublime_Plugin._hx_fields = []
hxsublime_Plugin._hx_props = []
hxsublime_Plugin._hx_methods = []
hxsublime_Plugin._hx_statics = ["_startupInfo","plugin_base_dir","startupInfo"]
hxsublime_Plugin._hx_interfaces = []

# print hxsublime.Settings.Settings
class hxsublime_Settings:

	pass




def Settings_statics_pluginSettings():
	return sublime_Sublime.load_settings("Haxe.sublime-settings")
hxsublime_Settings.pluginSettings = Settings_statics_pluginSettings
def Settings_statics_getFromSettings(id,settings,plugin):
	prefix = None
	if plugin:
		prefix = "plugin_"
	else:
		prefix = ""
	res = None
	pf = sublime_Sublime.platform()
	if settings.has(prefix + id + "_" + pf):
		res = settings.get(prefix + id + "_" + pf)
	
	if res is None and settings.has(prefix + id):
		res = settings.get(prefix + id)
	
	return res
	
hxsublime_Settings.getFromSettings = Settings_statics_getFromSettings
def Settings_statics_get(id,view = None):
	if view is None:
		view = None
	
	if view is None:
		win = sublime_Sublime.active_window()
		if win is not None:
			view = sublime_Sublime.active_window().active_view()
		
	
	
	res = None
	if view is not None:
		settings = view.settings()
		res = hxsublime_Settings.getFromSettings(id, settings, False)
	
	
	if res is None:
		res = hxsublime_Settings.getFromSettings(id, hxsublime_Settings.pluginSettings(), True)
	
	return res
	
hxsublime_Settings.get = Settings_statics_get
def Settings_statics_getBool(id,defaultVal,view = None):
	if view is None:
		view = None
	
	r = hxsublime_Settings.get(id, view)
	if r is None:
		return defaultVal
	elif Std._hx_is(r, Bool):
		return r
	else:
		return defaultVal
	
hxsublime_Settings.getBool = Settings_statics_getBool
def Settings_statics_getInt(id,defaultVal,view = None):
	if view is None:
		view = None
	
	r = hxsublime_Settings.get(id, view)
	if r is None:
		return defaultVal
	elif Std._hx_is(r, Int):
		return r
	else:
		return defaultVal
	
hxsublime_Settings.getInt = Settings_statics_getInt
def Settings_statics_getString(id,defaultVal,view = None):
	if view is None:
		view = None
	
	r = hxsublime_Settings.get(id, view)
	if r is None:
		return defaultVal
	elif Std._hx_is(r, String):
		return r
	else:
		return defaultVal
	
hxsublime_Settings.getString = Settings_statics_getString
def Settings_statics_noFuzzyCompletion(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.getBool("haxe_completion_no_fuzzy", False, view)
	
hxsublime_Settings.noFuzzyCompletion = Settings_statics_noFuzzyCompletion
def Settings_statics_topLevelCompletionsOnDemand(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.getBool("haxe_completions_top_level_only_on_demand", False, view)
	
hxsublime_Settings.topLevelCompletionsOnDemand = Settings_statics_topLevelCompletionsOnDemand
def Settings_statics_showOnlyAsyncCompletions(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.getBool("haxe_completions_show_only_async", True, view)
	
hxsublime_Settings.showOnlyAsyncCompletions = Settings_statics_showOnlyAsyncCompletions
def Settings_statics_isAsyncCompletion(view = None):
	if view is None:
		view = None
	
	r = hxsublime_Settings.getBool("haxe_completion_async", True, view)
	return r
	
hxsublime_Settings.isAsyncCompletion = Settings_statics_isAsyncCompletion
def Settings_statics_getCompletionDelays(view = None):
	if view is None:
		view = None
	
	a = hxsublime_Settings.getInt("haxe_completion_async_timing_hide", 60, view)
	b = hxsublime_Settings.getInt("haxe_completion_async_timing_show", 150, view)
	return (a, b)
	
	
hxsublime_Settings.getCompletionDelays = Settings_statics_getCompletionDelays
def Settings_statics_showCompletionTimes(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.getBool("haxe_completion_show_times", False, view)
	
hxsublime_Settings.showCompletionTimes = Settings_statics_showCompletionTimes
def Settings_statics_haxeExec(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.getString("haxe_exec", "haxe", view)
	
hxsublime_Settings.haxeExec = Settings_statics_haxeExec
def Settings_statics_useHaxeServermode(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.getBool("haxe_use_servermode", True, view)
	
hxsublime_Settings.useHaxeServermode = Settings_statics_useHaxeServermode
def Settings_statics_useHaxeServermodeWrapper(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.getBool("haxe_use_servermode_wrapper", False, view)
	
hxsublime_Settings.useHaxeServermodeWrapper = Settings_statics_useHaxeServermodeWrapper
def Settings_statics_haxeSdkPath(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.getString("haxe_sdk_path", None, view)
	
hxsublime_Settings.haxeSdkPath = Settings_statics_haxeSdkPath
def Settings_statics_openWithDefaultApp(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.getString("haxe_open_with_default_app", None, view)
	
hxsublime_Settings.openWithDefaultApp = Settings_statics_openWithDefaultApp
def Settings_statics_haxeInstPath(view = None):
	if view is None:
		view = None
	
	tmp = hxsublime_Settings.haxeSdkPath(view)
	defaultVal = None
	if tmp is not None:
		defaultVal = python_lib_os_Path.normpath(hxsublime_Settings.haxeSdkPath(view)) + python_lib_os_Path.sep + "haxe"
	else:
		defaultVal = None
	if tmp is None and hxsublime_Settings.haxeExec(view) != "haxe":
		defaultVal = python_lib_os_Path.normpath(python_lib_os_Path.dirname(hxsublime_Settings.haxeExec(view)))
	
	return hxsublime_Settings.getString("haxe_inst_path", defaultVal, view)
	
hxsublime_Settings.haxeInstPath = Settings_statics_haxeInstPath
def Settings_statics_nekoInstPath(view = None):
	if view is None:
		view = None
	
	tmp = hxsublime_Settings.haxeSdkPath(view)
	defaultVal = None
	if tmp is not None:
		defaultVal = python_lib_os_Path.normpath(hxsublime_Settings.haxeSdkPath(view)) + python_lib_os_Path.sep + "default"
	else:
		defaultVal = None
	return hxsublime_Settings.getString("neko_inst_path", defaultVal, view)
	
hxsublime_Settings.nekoInstPath = Settings_statics_nekoInstPath
def Settings_statics_haxeLibraryPath(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.getString("haxe_library_path", None, view)
	
hxsublime_Settings.haxeLibraryPath = Settings_statics_haxeLibraryPath
def Settings_statics_haxelibExec(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.getString("haxe_haxelib_exec", "haxelib", view)
	
hxsublime_Settings.haxelibExec = Settings_statics_haxelibExec
def Settings_statics_smartSnippets(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.getBool("haxe_completion_smart_snippets", True, view)
	
hxsublime_Settings.smartSnippets = Settings_statics_smartSnippets
def Settings_statics_smartSnippetsOnCompletion(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.getBool("haxe_completion_smart_snippets_on_completion", False, view)
	
hxsublime_Settings.smartSnippetsOnCompletion = Settings_statics_smartSnippetsOnCompletion
def Settings_statics_smartSnippetsJustCurrent(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.getBool("haxe_completion_smart_snippets_just_current", False, view)
	
hxsublime_Settings.smartSnippetsJustCurrent = Settings_statics_smartSnippetsJustCurrent
def Settings_statics_useDebugPanel(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.getBool("haxe_use_debug_panel", False, view)
	
hxsublime_Settings.useDebugPanel = Settings_statics_useDebugPanel
def Settings_statics_checkOnSave(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.getBool("haxe_check_on_save", True, view)
	
hxsublime_Settings.checkOnSave = Settings_statics_checkOnSave
def Settings_statics_useSlidePanel(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.getBool("haxe_use_slide_panel", True, view)
	
hxsublime_Settings.useSlidePanel = Settings_statics_useSlidePanel
def Settings_statics_useHaxeServermodeForBuilds(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.getBool("haxe_use_servermode_for_builds", False, view)
	
hxsublime_Settings.useHaxeServermodeForBuilds = Settings_statics_useHaxeServermodeForBuilds
def Settings_statics_useOffsetCompletion(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.getBool("haxe_use_offset_completion", False, view)
	
hxsublime_Settings.useOffsetCompletion = Settings_statics_useOffsetCompletion


hxsublime_Settings._hx_class = hxsublime_Settings
hxsublime_Settings._hx_class_name = "hxsublime.Settings"
_hx_classes['hxsublime.Settings'] = hxsublime_Settings
hxsublime_Settings._hx_fields = []
hxsublime_Settings._hx_props = []
hxsublime_Settings._hx_methods = []
hxsublime_Settings._hx_statics = ["pluginSettings","getFromSettings","get","getBool","getInt","getString","noFuzzyCompletion","topLevelCompletionsOnDemand","showOnlyAsyncCompletions","isAsyncCompletion","getCompletionDelays","showCompletionTimes","haxeExec","useHaxeServermode","useHaxeServermodeWrapper","haxeSdkPath","openWithDefaultApp","haxeInstPath","nekoInstPath","haxeLibraryPath","haxelibExec","smartSnippets","smartSnippetsOnCompletion","smartSnippetsJustCurrent","useDebugPanel","checkOnSave","useSlidePanel","useHaxeServermodeForBuilds","useOffsetCompletion"]
hxsublime_Settings._hx_interfaces = []

# print hxsublime.Temp.Temp
class hxsublime_Temp:

	pass




def Temp_statics_getTempPathId(build):
	path = build.getBuildFolder()
	if path is None:
		raise _HxException(hxsublime_ExtractBuildPathException(build))
	
	path1 = None
	def _hx_local_0():
		_this1 = path.split(python_lib_Os.sep)
		return "_".join(_this1)
	
	_this = (_hx_local_0()).split(":")
	path1 = "_".join(_this)
	
	temp_path = python_lib_os_Path.join(python_lib_Tempfile.gettempdir(), "haxe_sublime_hx" + path1 + "_")
	return temp_path
	
hxsublime_Temp.getTempPathId = Temp_statics_getTempPathId
def Temp_statics_createTempPath(build):
	temp_path = hxsublime_Temp.getTempPathId(build)
	hxsublime_tools_PathTools.removeDir(temp_path)
	python_lib_Os.makedirs(temp_path)
	return temp_path
	
hxsublime_Temp.createTempPath = Temp_statics_createTempPath
def Temp_statics_createFile(temp_path,build,orig_file,content):
	relative = build.getRelativePath(orig_file)
	haxe_Log.trace(relative, _Hx_AnonObject(fileName = "Temp.hx" ,lineNumber = 47 ,className = "hxsublime.Temp" ,methodName = "createFile" ))
	haxe_Log.trace(orig_file, _Hx_AnonObject(fileName = "Temp.hx" ,lineNumber = 48 ,className = "hxsublime.Temp" ,methodName = "createFile" ))
	haxe_Log.trace("relative:" + Std.string(relative), _Hx_AnonObject(fileName = "Temp.hx" ,lineNumber = 49 ,className = "hxsublime.Temp" ,methodName = "createFile" ))
	if relative is None:
		raise _HxException(hxsublime_GetRelativePathException(build, orig_file))
	
	new_file = python_lib_os_Path.join(temp_path, relative)
	new_file_dir = python_lib_os_Path.dirname(new_file)
	if not python_lib_os_Path.exists(new_file_dir):
		python_lib_Os.makedirs(new_file_dir)
	
	f = python_lib_Codecs.open(new_file, "wb", "utf-8", "ignore")
	f.write(content)
	f.close()
	haxe_Log.trace(new_file, _Hx_AnonObject(fileName = "Temp.hx" ,lineNumber = 65 ,className = "hxsublime.Temp" ,methodName = "createFile" ))
	return new_file
	
hxsublime_Temp.createFile = Temp_statics_createFile
def Temp_statics_createTempPathAndFile(build,orig_file,content):
	temp_path = hxsublime_Temp.createTempPath(build)
	temp_file = hxsublime_Temp.createFile(temp_path, build, orig_file, content)
	return (temp_path, temp_file)
	
hxsublime_Temp.createTempPathAndFile = Temp_statics_createTempPathAndFile
def Temp_statics_removePath(temp_path):
	if temp_path is not None:
		hxsublime_tools_PathTools.removeDir(temp_path)
	
hxsublime_Temp.removePath = Temp_statics_removePath


hxsublime_Temp._hx_class = hxsublime_Temp
hxsublime_Temp._hx_class_name = "hxsublime.Temp"
_hx_classes['hxsublime.Temp'] = hxsublime_Temp
hxsublime_Temp._hx_fields = []
hxsublime_Temp._hx_props = []
hxsublime_Temp._hx_methods = []
hxsublime_Temp._hx_statics = ["getTempPathId","createTempPath","createFile","createTempPathAndFile","removePath"]
hxsublime_Temp._hx_interfaces = []

# print hxsublime.Types.Types
class hxsublime_Types:

	pass




def Types_statics_findTypes(classpaths,libs,base_path,filtered_classes = None,filtered_packages = None,include_private_types = True):
	if filtered_classes is None:
		filtered_classes = None
	
	if filtered_packages is None:
		filtered_packages = None
	
	if include_private_types is None:
		include_private_types = True
	
	bundle = hxsublime_tools_HxSrcTools.emptyTypeBundle()
	cp = []
	cp = cp + classpaths
	_g = 0
	while _g < len(libs):
		lib = libs[_g]
		_g = _g + 1
		if lib is not None:
			cp.append(lib.path)
			__builtin__.len(cp)
		
		
	
	
	_g = 0
	while _g < len(cp):
		path = cp[_g]
		_g = _g + 1
		p = python_lib_os_Path.join(base_path, path)
		if python_lib_os_Path.exists(p):
			b = hxsublime_Types.extractTypes(p, filtered_classes, filtered_packages, 0, [], include_private_types)
			bundle = bundle.merge(b)
		
		else:
			hxsublime_panel_Panels.defaultPanel().writeln("Error: The classpath " + p + " does not exist, in case of nme or openfl you need have to build (CTRL + ENTER) the project first (the build creates these paths)")
	
	
	return bundle
	
hxsublime_Types.findTypes = Types_statics_findTypes
hxsublime_Types.validPackageRegex = python_lib_Re.compile("^[_a-z][a-zA-Z0-9_]*$")
def Types_statics_isValidPackage(pack):
	return hxsublime_Types.validPackageRegex.match(pack) is not None and pack != "_std"
hxsublime_Types.isValidPackage = Types_statics_isValidPackage
def Types_statics_extractTypes(path,filtered_classes = None,filtered_packages = None,depth = 0,pack = None,include_private_types = True):
	if filtered_classes is None:
		filtered_classes = None
	
	if filtered_packages is None:
		filtered_packages = None
	
	if depth is None:
		depth = 0
	
	if pack is None:
		pack = None
	
	if include_private_types is None:
		include_private_types = True
	
	if pack is None:
		pack = []
	
	if filtered_classes is None:
		filtered_classes = []
	
	if filtered_packages is None:
		filtered_packages = []
	
	bundle = hxsublime_tools_HxSrcTools.emptyTypeBundle()
	bundles = []
	_g = 0
	_g1 = python_lib_Glob.glob(python_lib_os_Path.join(path, "*.hx"))
	while _g < len(_g1):
		fullpath = _g1[_g]
		_g = _g + 1
		f = python_lib_os_Path.basename(fullpath)
		r = python_lib_os_Path.splitext(f)
		cl = r[0]
		ext = r[1]
		if not Lambda.has(filtered_classes, cl):
			file = python_lib_os_Path.join(path, f)
			if python_lib_os_Path.exists(file):
				module_bundle = hxsublime_Types.extractTypesFromFile(file, cl, include_private_types)
				bundles.append(module_bundle)
				__builtin__.len(bundles)
				
			
			
		
		
	
	
	_g = 0
	_g1 = python_lib_Os.listdir(path)
	while _g < len(_g1):
		f = _g1[_g]
		_g = _g + 1
		if hxsublime_Types.isValidPackage(f):
			r = python_lib_os_Path.splitext(f)
			cl = r[0]
			ext = r[1]
			cur_pack_base = None
			if __builtin__.len(pack) > 0:
				cur_pack_base = ".".join(pack) + "."
			else:
				cur_pack_base = ""
			cur_pack = cur_pack_base + f
			if python_lib_os_Path.isdir(python_lib_os_Path.join(path, f)) and not Lambda.has(filtered_packages, cur_pack) and not hxsublime_Config.ignored_packages.exists(cur_pack):
				next_pack = __builtin__.list(pack)
				next_pack.append(f)
				__builtin__.len(next_pack)
				
				sub_bundle = hxsublime_Types.extractTypes(python_lib_os_Path.join(path, f), filtered_classes, filtered_packages, depth + 1, next_pack, include_private_types)
				bundles.append(sub_bundle)
				__builtin__.len(bundles)
				
			
			
		
		
	
	
	bundle = bundle.mergeAll(bundles)
	return bundle
	
hxsublime_Types.extractTypes = Types_statics_extractTypes
hxsublime_Types.fileTypeCache = haxe_ds_StringMap()
def Types_statics_extractTypesFromFile(file,module_name = None,include_private_types = True):
	if module_name is None:
		module_name = None
	
	if include_private_types is None:
		include_private_types = True
	
	mtime = python_lib_os_Path.getmtime(file)
	def _hx_local_0():
		_this = hxsublime_Types.fileTypeCache.get(file)
		return _this[0]
	
	if hxsublime_Types.fileTypeCache.exists(file) and _hx_local_0() == mtime:
		_this = hxsublime_Types.fileTypeCache.get(file)
		return _this[1]
	
	
	if module_name is None:
		_this = python_lib_os_Path.splitext(python_lib_os_Path.basename(file))
		module_name = _this[0]
	
	
	s = python_lib_Codecs.open(file, "r", "utf-8", "ignore")
	src_with_comments = s.read()
	src = hxsublime_tools_HxSrcTools.stripComments(src_with_comments)
	bundle = hxsublime_tools_HxSrcTools.getTypesFromSrc(src, module_name, file, src_with_comments)
	hxsublime_Types.fileTypeCache.set(file, (mtime, bundle))
	return bundle
	
hxsublime_Types.extractTypesFromFile = Types_statics_extractTypesFromFile


hxsublime_Types._hx_class = hxsublime_Types
hxsublime_Types._hx_class_name = "hxsublime.Types"
_hx_classes['hxsublime.Types'] = hxsublime_Types
hxsublime_Types._hx_fields = []
hxsublime_Types._hx_props = []
hxsublime_Types._hx_methods = []
hxsublime_Types._hx_statics = ["findTypes","validPackageRegex","isValidPackage","extractTypes","fileTypeCache","extractTypesFromFile"]
hxsublime_Types._hx_interfaces = []

# print hxsublime.build.Build.Build
class hxsublime_build_Build:

	# var setHxml
	# var getRelativePath
	# var setStdBundle
	# var toString
	# var copy
	# var buildFile
	# var addClasspath
	# var makeHxml
	# var prepareCheckCmd
	# var prepareBuildCmd
	# var prepareRunCmd
	# var escapeCmd
	# var isTypeAvailable
	# var isPackAvailable
	# var getTypes
	# var getBuildFolder
	# var setAutoCompletion
	# var setTimes
	# var run
	# var stdBundle
	# var target
	# var classpaths
	# var args
	# var addArg
	pass






hxsublime_build_Build._hx_class = hxsublime_build_Build
hxsublime_build_Build._hx_class_name = "hxsublime.build.Build"
_hx_classes['hxsublime.build.Build'] = hxsublime_build_Build
hxsublime_build_Build._hx_fields = []
hxsublime_build_Build._hx_props = []
hxsublime_build_Build._hx_methods = ["setHxml","getRelativePath","setStdBundle","toString","copy","buildFile","addClasspath","makeHxml","prepareCheckCmd","prepareBuildCmd","prepareRunCmd","escapeCmd","isTypeAvailable","isPackAvailable","getTypes","getBuildFolder","setAutoCompletion","setTimes","run","stdBundle","target","classpaths","args","addArg"]
hxsublime_build_Build._hx_statics = []
hxsublime_build_Build._hx_interfaces = []

# print hxsublime.build.HxmlBuild.HxmlBuild
class hxsublime_build_HxmlBuild:


	def __init__(self,hxml,build_file):
		self._showTimes = False
		self._stdBundle = hxsublime_tools_HxSrcTools.emptyTypeBundle()
		self._args = []
		self.main = None
		self._target = None
		self.output = "dummy.js"
		self._hxml = hxml
		self._buildFile = build_file
		self._classpaths = []
		self.libs = []
		self.typeBundle = None
		self._updateTime = None
		self.modeCompletion = False
		self.defines = []
		self.name = None
	
	# var _showTimes
	# var _stdBundle
	# var _args
	# var _hxml
	# var _buildFile
	# var libs
	# var _updateTime
	# var defines
	# var _classpaths
	# var typeBundle
	# var modeCompletion
	# var name
	# var main
	# var _target
	# var output
	def getClassPaths(self):
		return self._classpaths

	def stdBundle(self):
		return self._stdBundle

	def target(self):
		return _Hx_AnonObject(name = self._target ,plattform = self._target ,args = [] )

	def classpaths(self):
		return self._classpaths

	def hxml(self):
		return self._hxml

	def title(self):
		return self.output

	def setHxml(self,hxml):
		self._hxml = hxml

	def buildFile(self):
		return self._buildFile

	def addDefine(self,define):
		_this = self.defines
		_this.append(define)
		__builtin__.len(_this)
		
	

	def setMain(self,main):
		self.main = main

	def getName(self):
		n = None
		if self.name is not None:
			n = self.name
		elif self.main is None:
			n = "[No Main]"
		else:
			n = self.main
		return n
	

	def setStdBundle(self,stdBundle):
		self._stdBundle = stdBundle

	def args(self):
		return self._args

	def equals(self,other):
		return self.args() == other._args() and self.main == other.main and self.name == other.name and self._target == other._target and self.output == other.output and self.hxml() == other.hxml() and self.classpaths() == other.classpaths() and self.libs == other.libs and self._showTimes == other._showTimes and self.modeCompletion == other.modeCompletion and self.defines == other.defines and self._buildFile == other._buildFile

	def merge(self,other_build):
		ob = other_build
		x = ob.args()
		self._args.extend(x)
		
		x = ob.classpaths()
		self._classpaths.extend(x)
		
		self.libs.extend(ob.libs)
		self.defines.extend(ob.defines)
		if self.main is None:
			self.main = ob.main
		
		if self.name is None:
			self.name = ob.name
		
	

	def copy(self):
		self.getTypes()
		hb = hxsublime_build_HxmlBuild(self._hxml, self.buildFile())
		_this = self.args()
		hb._args = __builtin__.list(_this)
		
		hb.main = self.main
		hb.name = self.name
		hb._target = self._target
		hb.output = self.output
		hb.defines = __builtin__.list(self.defines)
		hb._stdBundle = self._stdBundle
		hb._classpaths = __builtin__.list(self._classpaths)
		hb.libs = __builtin__.list(self.libs)
		hb.typeBundle = self.typeBundle
		hb._updateTime = self._updateTime
		hb._showTimes = self._showTimes
		hb.modeCompletion = self.modeCompletion
		return hb
	

	def addArg(self,arg):
		_this = self._args
		_this.append(arg)
		__builtin__.len(_this)
		
	

	def getBuildFolder(self):
		if self.buildFile() is not None:
			return python_lib_os_Path.dirname(self.buildFile())
		else:
			return None

	def setBuildCwd(self):
		self.setCwd(self.getBuildFolder())

	def alignDriveLetter(self,path):
		is_win = sublime_Sublime.platform() == "windows"
		if is_win:
			reg = python_lib_Re.compile("^([a-z]):(.*)$")
			match = python_lib_Re.match(reg, path)
			if match is not None:
				def _hx_local_0():
					_this = match.group(1)
					return _this.upper()
				
				path = _hx_local_0() + ":" + match.group(2)
			
			
		
		
		return path
	

	def addClasspath(self,cp):
		cp1 = self.alignDriveLetter(cp)
		if not Lambda.has(self._classpaths, cp1):
			_this = self._classpaths
			_this.append(cp1)
			__builtin__.len(_this)
			
			
			_this = self._args
			x = ("-cp", cp1)
			_this.append(x)
			__builtin__.len(_this)
			
			
		
		
	

	def addLib(self,lib):
		_this = self.libs
		_this.append(lib)
		__builtin__.len(_this)
		
		
		self.addArg(("-lib", lib.name))
	

	def getClasspathOfFile(self,file):
		file1 = self.alignDriveLetter(file)
		cps = __builtin__.list(self._classpaths)
		build_folder = self.getBuildFolder()
		if build_folder is not None and not Lambda.has(cps, build_folder):
			haxe_Log.trace("add build folder to classpaths: " + build_folder + ", classpaths: " + Std.string(cps), _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 244 ,className = "hxsublime.build.HxmlBuild" ,methodName = "getClasspathOfFile" ))
			cps.append(build_folder)
			__builtin__.len(cps)
			
		
		
		_g = 0
		while _g < len(cps):
			cp = cps[_g]
			_g = _g + 1
			prefix = python_lib_os_Path.commonprefix([cp, file1])
			if prefix == cp:
				return cp
			
		
		
		return None
	

	def getRelativePath(self,file):
		file = self.alignDriveLetter(file)
		cp = self.getClasspathOfFile(file)
		haxe_Log.trace(file, _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 270 ,className = "hxsublime.build.HxmlBuild" ,methodName = "getRelativePath" ))
		haxe_Log.trace(StringTools.replace(file, cp, ""), _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 271 ,className = "hxsublime.build.HxmlBuild" ,methodName = "getRelativePath" ))
		def _hx_local_0():
			_this = StringTools.replace(file, cp, "")
			return python_Tools.substr(_this, 1, None)
		
		haxe_Log.trace(_hx_local_0(), _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 272 ,className = "hxsublime.build.HxmlBuild" ,methodName = "getRelativePath" ))
		if cp is not None:
			_this = StringTools.replace(file, cp, "")
			return python_Tools.substr(_this, 1, None)
		
		else:
			return None
	

	def targetToString(self):
		target = None
		if self._target is None:
			target = "js"
		else:
			target = self._target
			if target == "js" and Lambda.has(self.defines, "nodejs"):
				target = "node.js"
			
		
		return target
	

	def toString(self):
		out = python_lib_os_Path.basename(self.output)
		main = self.getName()
		target = self.targetToString()
		return "" + main + " (" + target + " - " + out + ")"
	

	def makeHxml(self):
		outp = "# Autogenerated " + Std.string(self.hxml) + "\n\n"
		outp = outp + "# " + self.toString() + "\n"
		outp = outp + "-main " + self.main + "\n"
		_g = 0
		_g1 = self._args
		while _g < len(_g1):
			a = _g1[_g]
			_g = _g + 1
			outp = outp + a[0] + " " + a[1] + "\n"
		
		
		d = python_lib_os_Path.dirname(self._hxml) + "/"
		outp = StringTools.replace(outp, d, "")
		outp = StringTools.replace(outp, "-cp " + python_lib_os_Path.dirname(self._hxml) + "\n", "")
		outp = StringTools.replace(outp, "--no-output ", "")
		outp = StringTools.replace(outp, "-v", "")
		outp = StringTools.replace(outp, "dummy", self.main.lower())
		return outp.strip(None)
	

	def setCwd(self,cwd):
		_this = self._args
		x = ("--cwd", cwd)
		_this.append(x)
		__builtin__.len(_this)
		
	

	def setTimes(self):
		self._showTimes = True
		_this = self._args
		x = ("--times", "")
		_this.append(x)
		__builtin__.len(_this)
		
		
		_this = self._args
		x = ("-D", "macro-times")
		_this.append(x)
		__builtin__.len(_this)
		
		
		_this = self._args
		x = ("-D", "macro_times")
		_this.append(x)
		__builtin__.len(_this)
		
		
	

	def setServerMode(self,server_port = 6000):
		if server_port is None:
			server_port = 6000
		
		_this = self._args
		x = None
		b = Std.string(server_port)
		x = ("--connect", b)
		
		_this.append(x)
		__builtin__.len(_this)
		
	

	def getCommandArgs(self,haxe_path):
		cmd = __builtin__.list(haxe_path)
		_g = 0
		_g1 = self._args
		while _g < len(_g1):
			a = _g1[_g]
			_g = _g + 1
			x = [a[0], a[1]]
			cmd.extend(x)
			
		
		
		_g = 0
		_g1 = self.libs
		while _g < len(_g1):
			l = _g1[_g]
			_g = _g + 1
			cmd.append("-lib")
			__builtin__.len(cmd)
			
			x = l.as_cmd_arg()
			cmd.append(x)
			__builtin__.len(cmd)
			
			
		
		
		if self.main is not None:
			cmd.append("-main")
			__builtin__.len(cmd)
			
			cmd.append(self.main)
			__builtin__.len(cmd)
			
		
		
		return cmd
	

	def setAutoCompletion(self,display,macroCompletion = False,noOutput = True):
		if macroCompletion is None:
			macroCompletion = False
		
		if noOutput is None:
			noOutput = True
		
		self.modeCompletion = True
		args = self._args
		self.main = None
		def _hx_local_0(x):
			return x[0] != "-cs" and x[0] != "-x" and x[0] != "-js" and x[0] != "-php" and x[0] != "-cpp" and x[0] != "-swf" and x[0] != "-java"
		filterTargets = _hx_local_0
		if macroCompletion:
			_this = __builtin__.list(__builtin__.filter(filterTargets, args))
			args = __builtin__.list(_this)
		
		else:
			def _hx_local_1(x):
				if x[0] == "-x":
					b = x[1]
					return ("-neko", b)
			
				else:
					return x
			_this = __builtin__.list(__builtin__.map(_hx_local_1, args))
			args = __builtin__.list(_this)
		
		def _hx_local_2(x):
			return x[0] != "-cmd" and x[0] != "-dce"
		filterCommandsAndDce = _hx_local_2
		args = __builtin__.list(__builtin__.filter(filterCommandsAndDce, args))
		if not self._showTimes:
			def _hx_local_3(x):
				return x[0] != "--times"
			filterTimes = _hx_local_3
			_this = __builtin__.list(__builtin__.filter(filterTimes, args))
			args = __builtin__.list(_this)
			
		
		
		if macroCompletion:
			x = ("-neko", "__temp.n")
			args.append(x)
			__builtin__.len(args)
			
		
		
		x = ("--display", display)
		args.append(x)
		__builtin__.len(args)
		
		
		if noOutput:
			x = ("--no-output", "")
			args.append(x)
			__builtin__.len(args)
			
		
		
		self._args = args
	

	def updateTypes(self):
		haxe_Log.trace("update types for classpaths:" + Std.string(self._classpaths), _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 425 ,className = "hxsublime.build.HxmlBuild" ,methodName = "updateTypes" ))
		haxe_Log.trace("update types for libs:" + Std.string(self.libs), _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 426 ,className = "hxsublime.build.HxmlBuild" ,methodName = "updateTypes" ))
		self.typeBundle = hxsublime_Types.findTypes(self._classpaths, self.libs, self.getBuildFolder(), [], [], False)
	

	def shouldRefreshTypes(self,now):
		return self.typeBundle is None or self._updateTime is None or now - self._updateTime > 10

	def getTypes(self):
		now = python_lib_Time.time()
		if self.shouldRefreshTypes(now):
			haxe_Log.trace("UPDATE THE TYPES NOW", _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 444 ,className = "hxsublime.build.HxmlBuild" ,methodName = "getTypes" ))
			self._updateTime = now
			self.updateTypes()
			runTime = python_lib_Time.time() - now
			haxe_Log.trace("update types time: " + Std.string(runTime), _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 448 ,className = "hxsublime.build.HxmlBuild" ,methodName = "getTypes" ))
		
		
		return self.typeBundle
	

	def prepareCheckCmd(self,project,server_mode,view):
		r = self.prepareBuildCmd(project, server_mode, view)
		cmd = r[0]
		build_folder = r[1]
		cmd.append("--no-output")
		__builtin__.len(cmd)
		
		return (cmd, build_folder)
	

	def absoluteOutput(self):
		if python_lib_os_Path.isabs(self.output):
			return self.output
		else:
			return python_lib_os_Path.join(self.getBuildFolder(), self.output)

	def prepareRunCmd(self,project,server_mode,view):
		r = self.prepareRun(project, view, server_mode)
		cmd = r[0]
		build_folder = r[1]
		nekox_file = r[2]
		haxe_Log.trace(self.args, _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 477 ,className = "hxsublime.build.HxmlBuild" ,methodName = "prepareRunCmd" ))
		haxe_Log.trace(cmd, _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 478 ,className = "hxsublime.build.HxmlBuild" ,methodName = "prepareRunCmd" ))
		haxe_Log.trace(build_folder, _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 479 ,className = "hxsublime.build.HxmlBuild" ,methodName = "prepareRunCmd" ))
		haxe_Log.trace(nekox_file, _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 480 ,className = "hxsublime.build.HxmlBuild" ,methodName = "prepareRunCmd" ))
		default_open_ext = hxsublime_Settings.openWithDefaultApp()
		if nekox_file is not None:
			cmd.extend(["-cmd", "neko " + nekox_file])
		elif self._target == "swf" and default_open_ext is not None:
			x = ["-cmd", default_open_ext + " " + self.absoluteOutput()]
			cmd.extend(x)
		
		elif self._target == "neko":
			x = ["-cmd", "neko " + self.absoluteOutput()]
			cmd.extend(x)
		
		elif self._target == "cpp":
			sep_index = self.main.rfind(".", None)
			exe = None
			if sep_index > -1:
				exe = python_Tools.substr(self.main, sep_index + 1, None)
			else:
				exe = self.main
			x = ["-cmd", python_lib_os_Path.join(self.absoluteOutput(), exe) + "-debug"]
			cmd.extend(x)
			
		
		elif self._target == "js" and Lambda.has(self.defines, "nodejs"):
			x = ["-cmd", "nodejs " + self.absoluteOutput()]
			cmd.extend(x)
		
		elif self._target == "java":
			sep_index = None
			_this = self.absoluteOutput()
			sep_index = _this.rfind(python_lib_os_Path.sep, None)
			
			jar = None
			if sep_index == -1:
				jar = self.absoluteOutput() + ".jar"
			else:
				def _hx_local_0():
					_this = self.absoluteOutput()
					return python_Tools.substr(_this, sep_index + 1, None)
				
				jar = _hx_local_0() + ".jar"
			
			x = ["-cmd", "java -jar " + python_lib_os_Path.join(self.absoluteOutput(), jar)]
			cmd.extend(x)
			
		
		elif self._target == "cs":
			x = ["-cmd", "cd " + self.absoluteOutput()]
			cmd.extend(x)
			
			cmd.extend(["-cmd", "gmcs -recurse:*.cs -main:" + self.main + " -out:" + self.main + ".exe-debug"])
			x = ["-cmd", python_lib_os_Path.join(".", self.main + ".exe-debug")]
			cmd.extend(x)
			
		
		
		return (cmd, build_folder)
	

	def prepareBuildCmd(self,project,server_mode,view):
		r = self.prepareRun(project, view, server_mode)
		cmd = r[0]
		build_folder = r[1]
		return (cmd, build_folder)
	

	def prepareRun(self,project,view,server_mode = None):
		if server_mode is None:
			server_mode = None
		
		if server_mode is None:
			server_mode = project.isServerMode()
		else:
			server_mode = server_mode
		run_exec = self.getExecutable(project, view)
		b = self.copy()
		nekoxFileName = None
		_g1 = 0
		_g = __builtin__.len(b._args)
		while _g1 < _g:
			def _hx_local_1():
				nonlocal _g1
				_hx_local_0 = _g1
				_g1 = _g1 + 1
				return _hx_local_0
				
			
			i = _hx_local_1()
			a = b._args[i]
			if a[0] == "-x":
				nekoxFileName = a[1] + ".n"
				b._args[i] = ("-neko", nekoxFileName)
			
			
		
		
		if server_mode:
			project.startServer(view)
			b.setServerMode(project.server.get_server_port())
		
		
		b.setBuildCwd()
		cmd = b.getCommandArgs(run_exec)
		b1 = self.getBuildFolder()
		return (cmd, b1, nekoxFileName)
		
	

	def getExecutable(self,project,view):
		return project.haxeExec(view)

	def escapeCmd(self,cmd):
		print_cmd = __builtin__.list(cmd)
		l = __builtin__.len(print_cmd)
		_g = 0
		while _g < l:
			def _hx_local_1():
				nonlocal _g
				_hx_local_0 = _g
				_g = _g + 1
				return _hx_local_0
				
			
			i = _hx_local_1()
			e = print_cmd[i]
			if e == "--macro" and i < l - 1:
				print_cmd[i + 1] = "'" + print_cmd[i + 1] + "'"
			
		
		
		return print_cmd
	

	def runAsync(self,project,view,callback,server_mode = None):
		if server_mode is None:
			server_mode = None
		
		_g = self
		env = project.haxeEnv(view)
		r = self.prepareRun(project, view, server_mode)
		cmd = r[0]
		build_folder = r[1]
		nekox_file_name = r[2]
		print_cmd = __builtin__.list(cmd)
		_g1 = 0
		_g2 = __builtin__.len(print_cmd)
		while _g1 < _g2:
			def _hx_local_1():
				nonlocal _g1
				_hx_local_0 = _g1
				_g1 = _g1 + 1
				return _hx_local_0
				
			
			i = _hx_local_1()
			e = print_cmd[i]
			if e == "--macro" and i < __builtin__.len(print_cmd) - 1:
				print_cmd[i + 1] = "'" + print_cmd[i + 1] + "'"
			
		
		
		def _hx_local_2(out,err):
			_g.onRunComplete(out, err, build_folder, nekox_file_name)
			callback(out, err)
		
		cb = _hx_local_2
		hxsublime_Execute.runCmdAsync(cmd, cb, "", build_folder, env)
	

	def runSync(self,project,view,server_mode = None):
		if server_mode is None:
			server_mode = None
		
		env = project.haxeEnv(view)
		r = self.prepareRun(project, view, server_mode)
		cmd = r[0]
		build_folder = r[1]
		nekox_file_name = r[2]
		haxe_Log.trace(" ".join(cmd), _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 614 ,className = "hxsublime.build.HxmlBuild" ,methodName = "runSync" ))
		r1 = hxsublime_Execute.runCmd(cmd, "", build_folder, env)
		out = r1[0]
		err = r1[1]
		self.onRunComplete(out, err, build_folder, nekox_file_name)
		return (out, err)
	

	def onRunComplete(self,out,err,build_folder,nekox_file_name):
		haxe_Log.trace("---------------cmd-------------------", _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 626 ,className = "hxsublime.build.HxmlBuild" ,methodName = "onRunComplete" ))
		haxe_Log.trace("out:" + out, _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 627 ,className = "hxsublime.build.HxmlBuild" ,methodName = "onRunComplete" ))
		haxe_Log.trace("err:" + err, _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 628 ,className = "hxsublime.build.HxmlBuild" ,methodName = "onRunComplete" ))
		haxe_Log.trace("---------compiler-output-------------", _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 629 ,className = "hxsublime.build.HxmlBuild" ,methodName = "onRunComplete" ))
		if nekox_file_name is not None:
			self.runNekoX(build_folder, nekox_file_name)
		
	

	def runNekoX(self,build_folder,neko_file_name):
		neko_file = python_lib_os_Path.join(build_folder, neko_file_name)
		haxe_Log.trace("run nekox: " + neko_file, _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 640 ,className = "hxsublime.build.HxmlBuild" ,methodName = "runNekoX" ))
		r = hxsublime_Execute.runCmd(["neko", neko_file])
		out = r[0]
		err = r[1]
		hxsublime_panel_Panels.defaultPanel().writeln(out)
		hxsublime_panel_Panels.defaultPanel().writeln(err)
	

	def run(self,project,view,async,callback,server_mode = None):
		if server_mode is None:
			server_mode = None
		
		if async:
			haxe_Log.trace("RUN ASYNC COMPLETION", _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 651 ,className = "hxsublime.build.HxmlBuild" ,methodName = "run" ))
			self.runAsync(project, view, callback, server_mode)
		
		else:
			haxe_Log.trace("RUN SYNC COMPLETION", _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 656 ,className = "hxsublime.build.HxmlBuild" ,methodName = "run" ))
			r = self.runSync(project, view, server_mode)
			out = r[0]
			err = r[1]
			callback(out, err)
		
	

	def isTypeAvailable(self,type):
		pack = type.toplevelPack()
		return pack is None or self.isPackAvailable(pack)
	

	def isPackAvailable(self,pack):
		if pack == "":
			return True
		
		pack = pack.split(".")[0]
		target = self._target
		available = True
		if pack is not None and target is not None and Lambda.has(hxsublime_Config.target_packages, pack):
			if hxsublime_Config.target_std_packages.exists(target):
				if not Lambda.has(hxsublime_Config.target_std_packages.get(target), pack):
					available = False
				
			
		
		return available
	







hxsublime_build_HxmlBuild._hx_class = hxsublime_build_HxmlBuild
hxsublime_build_HxmlBuild._hx_class_name = "hxsublime.build.HxmlBuild"
_hx_classes['hxsublime.build.HxmlBuild'] = hxsublime_build_HxmlBuild
hxsublime_build_HxmlBuild._hx_fields = ["_showTimes","_stdBundle","_args","_hxml","_buildFile","libs","_updateTime","defines","_classpaths","typeBundle","modeCompletion","name","main","_target","output"]
hxsublime_build_HxmlBuild._hx_props = []
hxsublime_build_HxmlBuild._hx_methods = ["getClassPaths","stdBundle","target","classpaths","hxml","title","setHxml","buildFile","addDefine","setMain","getName","setStdBundle","args","equals","merge","copy","addArg","getBuildFolder","setBuildCwd","alignDriveLetter","addClasspath","addLib","getClasspathOfFile","getRelativePath","targetToString","toString","makeHxml","setCwd","setTimes","setServerMode","getCommandArgs","setAutoCompletion","updateTypes","shouldRefreshTypes","getTypes","prepareCheckCmd","absoluteOutput","prepareRunCmd","prepareBuildCmd","prepareRun","getExecutable","escapeCmd","runAsync","runSync","onRunComplete","runNekoX","run","isTypeAvailable","isPackAvailable"]
hxsublime_build_HxmlBuild._hx_statics = []
hxsublime_build_HxmlBuild._hx_interfaces = [hxsublime_build_Build]

# print hxsublime.macros.LazyFunctionSupport.LazyFunctionSupport
class hxsublime_macros_LazyFunctionSupport:

	pass






hxsublime_macros_LazyFunctionSupport._hx_class = hxsublime_macros_LazyFunctionSupport
hxsublime_macros_LazyFunctionSupport._hx_class_name = "hxsublime.macros.LazyFunctionSupport"
_hx_classes['hxsublime.macros.LazyFunctionSupport'] = hxsublime_macros_LazyFunctionSupport
hxsublime_macros_LazyFunctionSupport._hx_fields = []
hxsublime_macros_LazyFunctionSupport._hx_props = []
hxsublime_macros_LazyFunctionSupport._hx_methods = []
hxsublime_macros_LazyFunctionSupport._hx_statics = []
hxsublime_macros_LazyFunctionSupport._hx_interfaces = []

# print hxsublime.build.NmeBuild.NmeBuild
class hxsublime_build_NmeBuild:


	def __init__(self,project,title,nmml,target,cb = None):
		if cb is None:
			cb = None
		
		self._title = title
		self._target = target
		self.nmml = nmml
		self._hxmlBuild = cb
		self.project = project
	
	# var _title
	# var _target
	# var _hxmlBuild
	# var nmml
	# var project
	def setHxml(self,hxml):
		self.hxmlBuild().setHxml(hxml)

	def makeHxml(self):
		return self.hxmlBuild().makeHxml()

	def title(self):
		return self._title

	def buildFile(self):
		return self.nmml

	def target(self):
		return self._target

	def plattform(self):
		return self._target.plattform

	def getHxmlBuildWithNmeDisplay(self):
		view = sublime_Sublime.active_window().active_view()
		display_cmd = None
		_this = self.getBuildCommand(self.project, view)
		display_cmd = __builtin__.list(_this)
		
		display_cmd.append("display")
		__builtin__.len(display_cmd)
		
		return hxsublime_build_Tools.createHaxeBuildFromNmml(self.project, self._target, self.nmml, display_cmd)
	

	def hxmlBuild(self):
		if self._hxmlBuild is None:
			self._hxmlBuild = self.getHxmlBuildWithNmeDisplay()
		
		return self._hxmlBuild
	

	def toString(self):
		title = self.title()
		target = self.target().name
		return "" + title + " (NME - " + target + ")"
	

	def setStdBundle(self,std_bundle):
		self.hxmlBuild().setStdBundle(std_bundle)

	def _filter_platform_specific(self,packs_or_classes):
		res = []
		_g = 0
		while _g < len(packs_or_classes):
			c = packs_or_classes[_g]
			_g = _g + 1
			if not StringTools.startsWith(c, "native") and not StringTools.startsWith(c, "browser") and not StringTools.startsWith(c, "flash") and not StringTools.startsWith(c, "flash9") and not StringTools.startsWith(c, "flash8"):
				res.append(c)
				__builtin__.len(res)
			
			
		
		
		return res
	

	def getTypes(self):
		bundle = self.hxmlBuild().getTypes()
		return bundle
	

	def stdBundle(self):
		return self.hxmlBuild().stdBundle()

	def addArg(self,arg):
		self.hxmlBuild().addArg(arg)

	def copy(self):
		hxmlCopy = None
		if self._hxmlBuild is not None:
			hxmlCopy = self.hxmlBuild().copy()
		else:
			hxmlCopy = None
		return hxsublime_build_NmeBuild(self.project, self.title(), self.nmml, self._target, hxmlCopy)
	

	def getRelativePath(self,file):
		return self.hxmlBuild().getRelativePath(file)

	def getBuildFolder(self):
		r = None
		if self.nmml is not None:
			r = python_lib_os_Path.dirname(self.nmml)
		
		haxe_Log.trace("build_folder: " + Std.string(r), _Hx_AnonObject(fileName = "NmeBuild.hx" ,lineNumber = 151 ,className = "hxsublime.build.NmeBuild" ,methodName = "getBuildFolder" ))
		haxe_Log.trace("nmml: " + Std.string(self.nmml), _Hx_AnonObject(fileName = "NmeBuild.hx" ,lineNumber = 152 ,className = "hxsublime.build.NmeBuild" ,methodName = "getBuildFolder" ))
		return r
	

	def setAutoCompletion(self,display,macro_completion = False,no_output = True):
		if macro_completion is None:
			macro_completion = False
		
		if no_output is None:
			no_output = True
		
		self.hxmlBuild().setAutoCompletion(display, macro_completion, no_output)
	

	def setTimes(self):
		self.hxmlBuild().setTimes()

	def addDefine(self,define):
		self.hxmlBuild().addDefine(define)

	def addClasspath(self,cp):
		self.hxmlBuild().addClasspath(cp)

	def run(self,project,view,async,on_result,server_mode = None):
		if server_mode is None:
			server_mode = None
		
		self.hxmlBuild().run(project, view, async, on_result, server_mode)
	

	def getExecutable(self,project,view):
		return project.nmeExec(view)

	def getBuildCommand(self,project,view):
		_this = self.getExecutable(project, view)
		return __builtin__.list(_this)
	

	def escapeCmd(self,cmd):
		return self.hxmlBuild().escapeCmd(cmd)

	def prepareCheckCmd(self,project,server_mode,view):
		r = self.prepareBuildCmd(project, server_mode, view)
		cmd = r[0]
		folder = r[1]
		cmd.append("--no-output")
		__builtin__.len(cmd)
		
		return (cmd, folder)
	

	def prepareBuildCmd(self,project,server_mode,view):
		return self.prepareCmd(project, server_mode, view, "build")

	def prepareRunCmd(self,project,server_mode,view):
		return self.prepareCmd(project, server_mode, view, "test")

	def prepareCmd(self,project,server_mode,view,command):
		cmd = self.getBuildCommand(project, view)
		cmd.append(command)
		__builtin__.len(cmd)
		
		x = self.buildFile()
		cmd.append(x)
		__builtin__.len(cmd)
		
		
		cmd.append(self.target().plattform)
		__builtin__.len(cmd)
		
		cmd.extend(self.target().args)
		if server_mode:
			x = ["--connect", Std.string(project.server.get_server_port())]
			cmd.extend(x)
		
		
		b = self.getBuildFolder()
		return (cmd, b)
		
	

	def classpaths(self):
		return self.hxmlBuild().classpaths()

	def args(self):
		return self.hxmlBuild().args()

	def isTypeAvailable(self,type):
		pack = type.toplevelPack()
		return pack is None or self.isPackAvailable(pack)
	

	def isPackAvailable(self,pack):
		if pack == "":
			return True
		
		pack1 = pack.split(".")[0]
		target = self.hxmlBuild().target
		tp = hxsublime_Config.target_packages + ["native", "browser", "nme"]
		noTargetPack = not Lambda.has(tp, pack1)
		isNmePack = pack1 == "nme"
		available = target is None or noTargetPack or isNmePack
		return available
	





hxsublime_build_NmeBuild.__meta__ = _Hx_AnonObject(fields = _Hx_AnonObject(title = _Hx_AnonObject(property = None ) ,buildFile = _Hx_AnonObject(property = None ) ,target = _Hx_AnonObject(property = None ) ,plattform = _Hx_AnonObject(property = None ) ,stdBundle = _Hx_AnonObject(property = None ) ) )


hxsublime_build_NmeBuild._hx_class = hxsublime_build_NmeBuild
hxsublime_build_NmeBuild._hx_class_name = "hxsublime.build.NmeBuild"
_hx_classes['hxsublime.build.NmeBuild'] = hxsublime_build_NmeBuild
hxsublime_build_NmeBuild._hx_fields = ["_title","_target","_hxmlBuild","nmml","project"]
hxsublime_build_NmeBuild._hx_props = []
hxsublime_build_NmeBuild._hx_methods = ["setHxml","makeHxml","title","buildFile","target","plattform","getHxmlBuildWithNmeDisplay","hxmlBuild","toString","setStdBundle","_filter_platform_specific","getTypes","stdBundle","addArg","copy","getRelativePath","getBuildFolder","setAutoCompletion","setTimes","addDefine","addClasspath","run","getExecutable","getBuildCommand","escapeCmd","prepareCheckCmd","prepareBuildCmd","prepareRunCmd","prepareCmd","classpaths","args","isTypeAvailable","isPackAvailable"]
hxsublime_build_NmeBuild._hx_statics = ["__meta__"]
hxsublime_build_NmeBuild._hx_interfaces = [hxsublime_macros_LazyFunctionSupport,hxsublime_build_Build]

# print hxsublime.build.OpenFlBuild.OpenFlBuild
class hxsublime_build_OpenFlBuild(hxsublime_build_NmeBuild):


	def __init__(self,project,title,openfl_xml,target,cb = None):
		if cb is None:
			cb = None
		
		super().__init__(project, title, openfl_xml, target, cb)
	
	def copy(self):
		hxml_copy = None
		if self._hxmlBuild is not None:
			hxml_copy = self.hxmlBuild().copy()
		else:
			hxml_copy = None
		r = hxsublime_build_OpenFlBuild(self.project, self.title(), self.nmml, self.target(), hxml_copy)
		return r
	

	def getExecutable(self,project,view):
		return project.openflExec(view)

	def toString(self):
		out = self.title()
		target = self.target().name
		return "" + out + " (OpenFL - " + target + ")"
	

	def isTypeAvailable(self,type):
		pack = type.toplevelPack()
		return pack is None or self.isPackAvailable(pack)
	

	def isPackAvailable(self,pack):
		if pack == "":
			return True
		
		pack1 = pack.split(".")[0]
		target = self.hxmlBuild().target
		tp = __builtin__.list(hxsublime_Config.target_packages)
		tp.extend(["native", "browser", "nme"])
		no_target_pack = not Lambda.has(tp, pack1)
		is_flash_pack = pack1 == "flash"
		available = target is None or no_target_pack or is_flash_pack
		return available
	







hxsublime_build_OpenFlBuild._hx_class = hxsublime_build_OpenFlBuild
hxsublime_build_OpenFlBuild._hx_class_name = "hxsublime.build.OpenFlBuild"
_hx_classes['hxsublime.build.OpenFlBuild'] = hxsublime_build_OpenFlBuild
hxsublime_build_OpenFlBuild._hx_fields = []
hxsublime_build_OpenFlBuild._hx_props = []
hxsublime_build_OpenFlBuild._hx_methods = ["copy","getExecutable","toString","isTypeAvailable","isPackAvailable"]
hxsublime_build_OpenFlBuild._hx_statics = []
hxsublime_build_OpenFlBuild._hx_interfaces = [hxsublime_macros_LazyFunctionSupport]
hxsublime_build_OpenFlBuild._hx_super = hxsublime_build_NmeBuild

# print hxsublime.build.Tools.Tools
class hxsublime_build_Tools:

	pass




hxsublime_build_Tools._extract_tag = python_lib_Re.compile("<([a-z0-9_-]+).*?\\s(name|main|title|file)=\"([ a-z0-9_./-]+)\"", python_lib_Re.I)
def Tools_statics_hxmlBufferToBuilds(project,hxml_buffer,folder,build_path,buildFile = None,hxml = None):
	if buildFile is None:
		buildFile = None
	
	if hxml is None:
		hxml = None
	
	builds = []
	currentBuild = hxsublime_build_HxmlBuild(hxml, buildFile)
	f = hxml_buffer
	while True:
		l = f.readline()
		if l == "":
			break
		
		if l == "\n":
			continue
		
		l = l.strip(None)
		if StringTools.startsWith(l, "#build-name="):
			currentBuild.name = python_Tools.substr(l, 12, None)
			continue
		
		
		if StringTools.startsWith(l, "#"):
			continue
		
		if StringTools.startsWith(l, "--next"):
			def _hx_local_0():
				_this = currentBuild.getClassPaths()
				return __builtin__.len(_this)
			
			if _hx_local_0() == 0:
				haxe_Log.trace("no classpaths", _Hx_AnonObject(fileName = "Tools.hx" ,lineNumber = 70 ,className = "hxsublime.build.Tools" ,methodName = "hxmlBufferToBuilds" ))
				currentBuild.addClasspath(build_path)
			
			
			builds.append(currentBuild)
			__builtin__.len(builds)
			
			currentBuild = hxsublime_build_HxmlBuild(hxml, buildFile)
			continue
		
		
		if StringTools.endsWith(l, ".hxml"):
			haxe_Log.trace("found ref of hxml file:" + l, _Hx_AnonObject(fileName = "Tools.hx" ,lineNumber = 82 ,className = "hxsublime.build.Tools" ,methodName = "hxmlBufferToBuilds" ))
			path = python_lib_os_Path.dirname(hxml)
			subBuilds = hxsublime_build_Tools.hxmlToBuilds(project, path + python_lib_Os.sep + l, folder)
			if __builtin__.len(subBuilds) == 1:
				b = subBuilds[0]
				currentBuild.merge(b)
			
			
		
		
		if StringTools.startsWith(l, "-main"):
			spl = l.split(" ")
			if __builtin__.len(spl) == 2:
				currentBuild.main = spl[1]
			else:
				sublime_Sublime.status_message("Invalid build.hxml : no Main class")
		
		
		if StringTools.startsWith(l, "-lib"):
			spl = l.split(" ")
			if __builtin__.len(spl) == 2:
				lib = project.haxelibManager().get(spl[1])
				if lib is not None:
					currentBuild.addLib(lib)
				else:
					currentBuild.addArg(("-lib", spl[1]))
					hxsublime_panel_Panels.defaultPanel().writeln("Error: haxelib library " + Std.string(spl[1]) + " is not installed")
				
			
			else:
				sublime_Sublime.status_message("Invalid build.hxml : lib not found")
		
		
		if StringTools.startsWith(l, "-cmd"):
			spl = l.split(" ")
			def _hx_local_1():
				b = None
				_this = spl[1:None]
				b = " ".join(_this)
				
				return ("-cmd", b)
			
			currentBuild.addArg(_hx_local_1())
		
		
		if StringTools.startsWith(l, "--macro"):
			spl = l.split(" ")
			def _hx_local_2():
				b = None
				_this = spl[1:None]
				b = " ".join(_this)
				
				return ("--macro", b)
			
			currentBuild.addArg(_hx_local_2())
		
		
		if StringTools.startsWith(l, "-D"):
			x = l.split(" ")
			tup = (x[0], x[1])
			currentBuild.addArg(tup)
			currentBuild.addDefine(tup[1])
			continue
		
		
		_g = 0
		_g1 = ["swf-version", "swf-header", "debug", "-no-traces", "-flash-use-stage", "-gen-hx-classes", "-remap", "-no-inline", "-no-opt", "-php-prefix", "-js-namespace", "-interp", "-dead-code-elimination", "-php-front", "-php-lib", "dce", "-js-modern", "-times"]
		while _g < len(_g1):
			flag = _g1[_g]
			_g = _g + 1
			if StringTools.startsWith(l, "-" + flag):
				x = l.split(" ")
				p2 = None
				if __builtin__.len(x) == 1:
					p2 = ""
				else:
					p2 = x[1]
				currentBuild.addArg((x[0], p2))
				break
			
			
		
		
		_g = 0
		_g1 = ["resource", "xml", "x", "swf-lib", "java-lib"]
		while _g < len(_g1):
			flag = _g1[_g]
			_g = _g + 1
			if StringTools.startsWith(l, "-" + flag):
				spl = l.split(" ")
				def _hx_local_3():
					_this = spl[1:None]
					return " ".join(_this)
				
				outp = python_lib_os_Path.join(folder, _hx_local_3())
				currentBuild.addArg(("-" + flag, outp))
				if flag == "x":
					currentBuild._target = "neko"
				
				break
			
			
		
		
		_g = 0
		_g1 = hxsublime_Config.targets
		while _g < len(_g1):
			flag = _g1[_g]
			_g = _g + 1
			if StringTools.startsWith(l, "-" + flag + " "):
				spl = l.split(" ")
				spl.pop(0)
				outp = " ".join(spl)
				currentBuild.addArg(("-" + flag, outp))
				currentBuild._target = flag
				currentBuild.output = outp
				break
			
			
		
		
		if StringTools.startsWith(l, "-cp "):
			cp = l.split(" ")
			cp.pop(0)
			classpath = " ".join(cp)
			abs_classpath = hxsublime_tools_PathTools.joinNorm(build_path, classpath)
			currentBuild.addClasspath(abs_classpath)
		
		
	
	def _hx_local_4():
		_this = currentBuild.getClassPaths()
		return __builtin__.len(_this)
	
	if _hx_local_4() == 0:
		currentBuild.addClasspath(build_path)
	
	builds.append(currentBuild)
	__builtin__.len(builds)
	
	return builds
	
hxsublime_build_Tools.hxmlBufferToBuilds = Tools_statics_hxmlBufferToBuilds
def Tools_statics_findBuildFiles(folder,extension):
	if not python_lib_os_Path.isdir(folder):
		return []
	
	files = None
	_this = python_lib_Glob.glob(python_lib_os_Path.join(folder, "*." + extension))
	def _hx_local_0(x):
		return (x, folder)
	files = __builtin__.list(__builtin__.map(_hx_local_0, _this))
	
	_g = 0
	_g1 = python_lib_Os.listdir(folder)
	while _g < len(_g1):
		dir = _g1[_g]
		_g = _g + 1
		f = [python_lib_os_Path.join(folder, dir)]
		x = None
		_this = python_lib_Glob.glob(python_lib_os_Path.join(f[0], "*." + extension))
		def _hx_local_2(f):
			def _hx_local_1(x1):
				return (x1, f[0])
			return _hx_local_1
		
		x = __builtin__.list(__builtin__.map((_hx_local_2)(f), _this))
		
		files.extend(x)
	
	
	return files
	
hxsublime_build_Tools.findBuildFiles = Tools_statics_findBuildFiles
def Tools_statics_hxmlToBuilds(project,hxml,folder):
	build_path = python_lib_os_Path.dirname(hxml)
	hxml_buffer = python_lib_Codecs.open(hxml, "r+", "utf-8", "ignore")
	def _hx_local_1():
		def _hx_local_0():
			return hxml_buffer.readline()
		return hxsublime_build_Tools.hxmlBufferToBuilds(project, _Hx_AnonObject(readline = _hx_local_0 ), folder, build_path, hxml, hxml)
	
	return _hx_local_1()
	
hxsublime_build_Tools.hxmlToBuilds = Tools_statics_hxmlToBuilds
def Tools_statics__find_nme_project_title(nmml_file):
	f = python_lib_Codecs.open(nmml_file, "r+", "utf-8", "ignore")
	title = None
	while True:
		l = f.readline()
		if l is None:
			break
		
		m = hxsublime_build_Tools._extract_tag.search(l)
		if m is not None:
			tag = m.group(1)
			if tag == "meta" or tag == "app":
				mFile = python_lib_Re.search("\\b(file|title)=\"([ a-z0-9_-]+)\"", l, python_lib_Re.I)
				if mFile is not None:
					title = mFile.group(2)
					break
				
				
			
			
		
		
	
	f.close()
	return title
	
hxsublime_build_Tools._find_nme_project_title = Tools_statics__find_nme_project_title
def Tools_statics_createHaxeBuildFromNmml(project,target,nmml,display_cmd):
	cmd = __builtin__.list(display_cmd)
	cmd.append(nmml)
	__builtin__.len(cmd)
	
	cmd.append(target.plattform)
	__builtin__.len(cmd)
	
	cmd.extend(target.args)
	nmml_dir = python_lib_os_Path.dirname(nmml)
	r = hxsublime_Execute.runCmd(cmd, None, nmml_dir)
	out = r[0]
	err = r[1]
	io = python_lib_io_StringIO(out)
	def _hx_local_1():
		def _hx_local_0():
			return io.readline()
		return hxsublime_build_Tools.hxmlBufferToBuilds(project, _Hx_AnonObject(readline = _hx_local_0 ), nmml_dir, nmml_dir, nmml, None)[0]
	
	return _hx_local_1()
	
hxsublime_build_Tools.createHaxeBuildFromNmml = Tools_statics_createHaxeBuildFromNmml
def Tools_statics_findHxmlProjects(project,folder):
	builds = []
	found = hxsublime_build_Tools.findBuildFiles(folder, "hxml")
	_g = 0
	while _g < len(found):
		build = found[_g]
		_g = _g + 1
		hxml_file = build[0]
		hxml_folder = build[1]
		b = hxsublime_build_Tools.hxmlToBuilds(project, hxml_file, hxml_folder)
		builds.extend(b)
	
	
	return builds
	
hxsublime_build_Tools.findHxmlProjects = Tools_statics_findHxmlProjects
def Tools_statics_findNmeProjects(project,folder):
	found = hxsublime_build_Tools.findBuildFiles(folder, "nmml")
	builds = []
	_g = 0
	while _g < len(found):
		build = found[_g]
		_g = _g + 1
		nmml_file = build[0]
		title = hxsublime_build_Tools._find_nme_project_title(nmml_file)
		if title is not None:
			_g1 = 0
			_g2 = hxsublime_Config.nme_targets
			while _g1 < len(_g2):
				t = _g2[_g1]
				_g1 = _g1 + 1
				x = hxsublime_build_NmeBuild(project, title, nmml_file, t)
				builds.append(x)
				__builtin__.len(builds)
				
				
			
		
		
	
	
	return builds
	
hxsublime_build_Tools.findNmeProjects = Tools_statics_findNmeProjects
def Tools_statics_findOpenflProjects(project,folder):
	found = hxsublime_build_Tools.findBuildFiles(folder, "xml")
	builds = []
	_g = 0
	while _g < len(found):
		build = found[_g]
		_g = _g + 1
		openfl_xml = build[0]
		title = hxsublime_build_Tools._find_nme_project_title(openfl_xml)
		if title is not None:
			_g1 = 0
			_g2 = hxsublime_Config.openfl_targets
			while _g1 < len(_g2):
				t = _g2[_g1]
				_g1 = _g1 + 1
				x = hxsublime_build_OpenFlBuild(project, title, openfl_xml, t)
				builds.append(x)
				__builtin__.len(builds)
				
				
			
		
		
	
	
	return builds
	
hxsublime_build_Tools.findOpenflProjects = Tools_statics_findOpenflProjects


hxsublime_build_Tools._hx_class = hxsublime_build_Tools
hxsublime_build_Tools._hx_class_name = "hxsublime.build.Tools"
_hx_classes['hxsublime.build.Tools'] = hxsublime_build_Tools
hxsublime_build_Tools._hx_fields = []
hxsublime_build_Tools._hx_props = []
hxsublime_build_Tools._hx_methods = []
hxsublime_build_Tools._hx_statics = ["_extract_tag","hxmlBufferToBuilds","findBuildFiles","hxmlToBuilds","_find_nme_project_title","createHaxeBuildFromNmml","findHxmlProjects","findNmeProjects","findOpenflProjects"]
hxsublime_build_Tools._hx_interfaces = []

# print sublime.Command.Command
from sublime_plugin import Command as sublime_Command
# print sublime.TextCommand.TextCommand
from sublime_plugin import TextCommand as sublime_TextCommand
# print hxsublime.commands.Build.HaxeSaveAllAndRunCommand
class hxsublime_commands_HaxeSaveAllAndRunCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**args):
		if args is None:
			args = None
		
		haxe_Log.trace("run HaxeSaveAllAndRunCommand", _Hx_AnonObject(fileName = "Build.hx" ,lineNumber = 20 ,className = "hxsublime.commands.HaxeSaveAllAndRunCommand" ,methodName = "run" ))
		view = self.view
		view.window().run_command("save_all")
		hxsublime_project_Projects.currentProject(self.view).runBuild(view)
	







hxsublime_commands_HaxeSaveAllAndRunCommand._hx_class = hxsublime_commands_HaxeSaveAllAndRunCommand
hxsublime_commands_HaxeSaveAllAndRunCommand._hx_class_name = "hxsublime.commands.HaxeSaveAllAndRunCommand"
_hx_classes['hxsublime.commands.HaxeSaveAllAndRunCommand'] = hxsublime_commands_HaxeSaveAllAndRunCommand
hxsublime_commands_HaxeSaveAllAndRunCommand._hx_fields = []
hxsublime_commands_HaxeSaveAllAndRunCommand._hx_props = []
hxsublime_commands_HaxeSaveAllAndRunCommand._hx_methods = ["run"]
hxsublime_commands_HaxeSaveAllAndRunCommand._hx_statics = []
hxsublime_commands_HaxeSaveAllAndRunCommand._hx_interfaces = []
hxsublime_commands_HaxeSaveAllAndRunCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.Build.HaxeSaveAllAndCheckCommand
class hxsublime_commands_HaxeSaveAllAndCheckCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**args):
		if args is None:
			args = None
		
		edit1 = python_lib_Types_KwArgs_Impl_.get(args, "edit", None)
		haxe_Log.trace("run HaxeSaveAllAndCheckCommand", _Hx_AnonObject(fileName = "Build.hx" ,lineNumber = 32 ,className = "hxsublime.commands.HaxeSaveAllAndCheckCommand" ,methodName = "run" ))
		view = self.view
		view.window().run_command("save_all")
		hxsublime_project_Projects.currentProject(self.view).checkBuild(view)
	







hxsublime_commands_HaxeSaveAllAndCheckCommand._hx_class = hxsublime_commands_HaxeSaveAllAndCheckCommand
hxsublime_commands_HaxeSaveAllAndCheckCommand._hx_class_name = "hxsublime.commands.HaxeSaveAllAndCheckCommand"
_hx_classes['hxsublime.commands.HaxeSaveAllAndCheckCommand'] = hxsublime_commands_HaxeSaveAllAndCheckCommand
hxsublime_commands_HaxeSaveAllAndCheckCommand._hx_fields = []
hxsublime_commands_HaxeSaveAllAndCheckCommand._hx_props = []
hxsublime_commands_HaxeSaveAllAndCheckCommand._hx_methods = ["run"]
hxsublime_commands_HaxeSaveAllAndCheckCommand._hx_statics = []
hxsublime_commands_HaxeSaveAllAndCheckCommand._hx_interfaces = []
hxsublime_commands_HaxeSaveAllAndCheckCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.Build.HaxeSaveAllAndBuildCommand
class hxsublime_commands_HaxeSaveAllAndBuildCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**args):
		if args is None:
			args = None
		
		haxe_Log.trace("run HaxeSaveAllAndBuildCommand", _Hx_AnonObject(fileName = "Build.hx" ,lineNumber = 43 ,className = "hxsublime.commands.HaxeSaveAllAndBuildCommand" ,methodName = "run" ))
		view = self.view
		view.window().run_command("save_all")
		hxsublime_project_Projects.currentProject(self.view).justBuild(view)
	







hxsublime_commands_HaxeSaveAllAndBuildCommand._hx_class = hxsublime_commands_HaxeSaveAllAndBuildCommand
hxsublime_commands_HaxeSaveAllAndBuildCommand._hx_class_name = "hxsublime.commands.HaxeSaveAllAndBuildCommand"
_hx_classes['hxsublime.commands.HaxeSaveAllAndBuildCommand'] = hxsublime_commands_HaxeSaveAllAndBuildCommand
hxsublime_commands_HaxeSaveAllAndBuildCommand._hx_fields = []
hxsublime_commands_HaxeSaveAllAndBuildCommand._hx_props = []
hxsublime_commands_HaxeSaveAllAndBuildCommand._hx_methods = ["run"]
hxsublime_commands_HaxeSaveAllAndBuildCommand._hx_statics = []
hxsublime_commands_HaxeSaveAllAndBuildCommand._hx_interfaces = []
hxsublime_commands_HaxeSaveAllAndBuildCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.Build.HaxeRunBuildCommand
class hxsublime_commands_HaxeRunBuildCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**args):
		if args is None:
			args = None
		
		view = self.view
		haxe_Log.trace("run HaxeRunBuildCommand", _Hx_AnonObject(fileName = "Build.hx" ,lineNumber = 55 ,className = "hxsublime.commands.HaxeRunBuildCommand" ,methodName = "run" ))
		project = hxsublime_project_Projects.currentProject(self.view)
		if project.hasBuild():
			project.runBuild(view)
		else:
			haxe_Log.trace("no builds selected", _Hx_AnonObject(fileName = "Build.hx" ,lineNumber = 64 ,className = "hxsublime.commands.HaxeRunBuildCommand" ,methodName = "run" ))
			project.extractBuildArgs(view, True)
		
	







hxsublime_commands_HaxeRunBuildCommand._hx_class = hxsublime_commands_HaxeRunBuildCommand
hxsublime_commands_HaxeRunBuildCommand._hx_class_name = "hxsublime.commands.HaxeRunBuildCommand"
_hx_classes['hxsublime.commands.HaxeRunBuildCommand'] = hxsublime_commands_HaxeRunBuildCommand
hxsublime_commands_HaxeRunBuildCommand._hx_fields = []
hxsublime_commands_HaxeRunBuildCommand._hx_props = []
hxsublime_commands_HaxeRunBuildCommand._hx_methods = ["run"]
hxsublime_commands_HaxeRunBuildCommand._hx_statics = []
hxsublime_commands_HaxeRunBuildCommand._hx_interfaces = []
hxsublime_commands_HaxeRunBuildCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.Build.HaxeSelectBuildCommand
class hxsublime_commands_HaxeSelectBuildCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**args):
		if args is None:
			args = None
		
		haxe_Log.trace("run HaxeSelectBuildCommand", _Hx_AnonObject(fileName = "Build.hx" ,lineNumber = 74 ,className = "hxsublime.commands.HaxeSelectBuildCommand" ,methodName = "run" ))
		view = self.view
		hxsublime_project_Projects.currentProject(self.view).selectBuild(view)
	







hxsublime_commands_HaxeSelectBuildCommand._hx_class = hxsublime_commands_HaxeSelectBuildCommand
hxsublime_commands_HaxeSelectBuildCommand._hx_class_name = "hxsublime.commands.HaxeSelectBuildCommand"
_hx_classes['hxsublime.commands.HaxeSelectBuildCommand'] = hxsublime_commands_HaxeSelectBuildCommand
hxsublime_commands_HaxeSelectBuildCommand._hx_fields = []
hxsublime_commands_HaxeSelectBuildCommand._hx_props = []
hxsublime_commands_HaxeSelectBuildCommand._hx_methods = ["run"]
hxsublime_commands_HaxeSelectBuildCommand._hx_statics = []
hxsublime_commands_HaxeSelectBuildCommand._hx_interfaces = []
hxsublime_commands_HaxeSelectBuildCommand._hx_super = sublime_TextCommand

# print sublime.EventListener.EventListener
from sublime_plugin import EventListener as sublime_EventListener
# print hxsublime.commands.Build.HaxeBuildOnSaveListener
class hxsublime_commands_HaxeBuildOnSaveListener(sublime_EventListener):

	def on_post_save(self,view):
		haxe_Log.trace("on_post_save", _Hx_AnonObject(fileName = "Build.hx" ,lineNumber = 83 ,className = "hxsublime.commands.HaxeBuildOnSaveListener" ,methodName = "on_post_save" ))
		if view is not None and view.file_name() is not None:
			if hxsublime_tools_ViewTools.isSupported(view) or StringTools.endsWith(view.file_name(), ".erazor.html"):
				if hxsublime_Settings.checkOnSave():
					project = hxsublime_project_Projects.currentProject(view)
					if project.hasBuild():
						project.checkBuild(view)
					
		
				
			
		
	







hxsublime_commands_HaxeBuildOnSaveListener._hx_class = hxsublime_commands_HaxeBuildOnSaveListener
hxsublime_commands_HaxeBuildOnSaveListener._hx_class_name = "hxsublime.commands.HaxeBuildOnSaveListener"
_hx_classes['hxsublime.commands.HaxeBuildOnSaveListener'] = hxsublime_commands_HaxeBuildOnSaveListener
hxsublime_commands_HaxeBuildOnSaveListener._hx_fields = []
hxsublime_commands_HaxeBuildOnSaveListener._hx_props = []
hxsublime_commands_HaxeBuildOnSaveListener._hx_methods = ["on_post_save"]
hxsublime_commands_HaxeBuildOnSaveListener._hx_statics = []
hxsublime_commands_HaxeBuildOnSaveListener._hx_interfaces = []
hxsublime_commands_HaxeBuildOnSaveListener._hx_super = sublime_EventListener

# print hxsublime.commands.Completion.HaxeAsyncTriggeredCompletionCommand
class hxsublime_commands_HaxeAsyncTriggeredCompletionCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**kwArgs):
		if kwArgs is None:
			kwArgs = None
		
		options = hxsublime_completion_hx_CompletionOptions(3, 2, 1)
		hxsublime_completion_hx_HxCompletion.triggerCompletion(self.view, options)
	







hxsublime_commands_HaxeAsyncTriggeredCompletionCommand._hx_class = hxsublime_commands_HaxeAsyncTriggeredCompletionCommand
hxsublime_commands_HaxeAsyncTriggeredCompletionCommand._hx_class_name = "hxsublime.commands.HaxeAsyncTriggeredCompletionCommand"
_hx_classes['hxsublime.commands.HaxeAsyncTriggeredCompletionCommand'] = hxsublime_commands_HaxeAsyncTriggeredCompletionCommand
hxsublime_commands_HaxeAsyncTriggeredCompletionCommand._hx_fields = []
hxsublime_commands_HaxeAsyncTriggeredCompletionCommand._hx_props = []
hxsublime_commands_HaxeAsyncTriggeredCompletionCommand._hx_methods = ["run"]
hxsublime_commands_HaxeAsyncTriggeredCompletionCommand._hx_statics = []
hxsublime_commands_HaxeAsyncTriggeredCompletionCommand._hx_interfaces = []
hxsublime_commands_HaxeAsyncTriggeredCompletionCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.Completion.HaxeDisplayCompletionCommand
class hxsublime_commands_HaxeDisplayCompletionCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**kwArgs):
		if kwArgs is None:
			kwArgs = None
		
		input_char = None
		if kwArgs is None:
			input_char = None
		else:
			input_char = python_lib_Types_KwArgs_Impl_.get(kwArgs, "input_char", None)
		if input_char is not None:
			def _hx_local_0():
				x = _Hx_AnonObject(characters = input_char )
				def _hx_local_2():
					def _hx_local_1():
						d = python_lib_Dict()
						_g = 0
						_g1 = Reflect.fields(x)
						while _g < len(_g1):
							f = _g1[_g]
							_g = _g + 1
							val = Reflect.field(x, f)
							python_lib_DictImpl.set(d, f, val)
							
						
						
						return d
					
					return _hx_local_1()
				
				return _hx_local_2()
			
			self.view.run_command("insert", _hx_local_0())
		
		
		haxe_Log.trace("RUN - HaxeDisplayCompletionCommand", _Hx_AnonObject(fileName = "Completion.hx" ,lineNumber = 40 ,className = "hxsublime.commands.HaxeDisplayCompletionCommand" ,methodName = "run" ))
		if input_char == ":":
			return
		
		if hxsublime_commands_Helper.isValidCompletion(self.view, edit, input_char):
			options = hxsublime_completion_hx_CompletionOptions(1, 2, 1)
			hxsublime_completion_hx_HxCompletion.triggerCompletion(self.view, options)
		
		
	







hxsublime_commands_HaxeDisplayCompletionCommand._hx_class = hxsublime_commands_HaxeDisplayCompletionCommand
hxsublime_commands_HaxeDisplayCompletionCommand._hx_class_name = "hxsublime.commands.HaxeDisplayCompletionCommand"
_hx_classes['hxsublime.commands.HaxeDisplayCompletionCommand'] = hxsublime_commands_HaxeDisplayCompletionCommand
hxsublime_commands_HaxeDisplayCompletionCommand._hx_fields = []
hxsublime_commands_HaxeDisplayCompletionCommand._hx_props = []
hxsublime_commands_HaxeDisplayCompletionCommand._hx_methods = ["run"]
hxsublime_commands_HaxeDisplayCompletionCommand._hx_statics = []
hxsublime_commands_HaxeDisplayCompletionCommand._hx_interfaces = []
hxsublime_commands_HaxeDisplayCompletionCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.Completion.HaxeDisplayMacroCompletionCommand
class hxsublime_commands_HaxeDisplayMacroCompletionCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**kwArgs):
		if kwArgs is None:
			kwArgs = None
		
		haxe_Log.trace("RUN - HaxeDisplayMacroCompletionCommand", _Hx_AnonObject(fileName = "Completion.hx" ,lineNumber = 60 ,className = "hxsublime.commands.HaxeDisplayMacroCompletionCommand" ,methodName = "run" ))
		options = hxsublime_completion_hx_CompletionOptions(1, 2, 1)
		hxsublime_completion_hx_HxCompletion.triggerCompletion(self.view, options)
	







hxsublime_commands_HaxeDisplayMacroCompletionCommand._hx_class = hxsublime_commands_HaxeDisplayMacroCompletionCommand
hxsublime_commands_HaxeDisplayMacroCompletionCommand._hx_class_name = "hxsublime.commands.HaxeDisplayMacroCompletionCommand"
_hx_classes['hxsublime.commands.HaxeDisplayMacroCompletionCommand'] = hxsublime_commands_HaxeDisplayMacroCompletionCommand
hxsublime_commands_HaxeDisplayMacroCompletionCommand._hx_fields = []
hxsublime_commands_HaxeDisplayMacroCompletionCommand._hx_props = []
hxsublime_commands_HaxeDisplayMacroCompletionCommand._hx_methods = ["run"]
hxsublime_commands_HaxeDisplayMacroCompletionCommand._hx_statics = []
hxsublime_commands_HaxeDisplayMacroCompletionCommand._hx_interfaces = []
hxsublime_commands_HaxeDisplayMacroCompletionCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.Completion.HaxeHintDisplayCompletionCommand
class hxsublime_commands_HaxeHintDisplayCompletionCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**kwArgs):
		if kwArgs is None:
			kwArgs = None
		
		haxe_Log.trace("RUN - HaxeHintDisplayCompletionCommand", _Hx_AnonObject(fileName = "Completion.hx" ,lineNumber = 74 ,className = "hxsublime.commands.HaxeHintDisplayCompletionCommand" ,methodName = "run" ))
		options = hxsublime_completion_hx_CompletionOptions(1, 2, 2)
		hxsublime_completion_hx_HxCompletion.triggerCompletion(self.view, options)
	







hxsublime_commands_HaxeHintDisplayCompletionCommand._hx_class = hxsublime_commands_HaxeHintDisplayCompletionCommand
hxsublime_commands_HaxeHintDisplayCompletionCommand._hx_class_name = "hxsublime.commands.HaxeHintDisplayCompletionCommand"
_hx_classes['hxsublime.commands.HaxeHintDisplayCompletionCommand'] = hxsublime_commands_HaxeHintDisplayCompletionCommand
hxsublime_commands_HaxeHintDisplayCompletionCommand._hx_fields = []
hxsublime_commands_HaxeHintDisplayCompletionCommand._hx_props = []
hxsublime_commands_HaxeHintDisplayCompletionCommand._hx_methods = ["run"]
hxsublime_commands_HaxeHintDisplayCompletionCommand._hx_statics = []
hxsublime_commands_HaxeHintDisplayCompletionCommand._hx_interfaces = []
hxsublime_commands_HaxeHintDisplayCompletionCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.Completion.HaxeMacroHintDisplayCompletionCommand
class hxsublime_commands_HaxeMacroHintDisplayCompletionCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**kwArgs):
		if kwArgs is None:
			kwArgs = None
		
		haxe_Log.trace("RUN - HaxeMacroHintDisplayCompletionCommand", _Hx_AnonObject(fileName = "Completion.hx" ,lineNumber = 89 ,className = "hxsublime.commands.HaxeMacroHintDisplayCompletionCommand" ,methodName = "run" ))
		options = hxsublime_completion_hx_CompletionOptions(1, 1, 2)
		hxsublime_completion_hx_HxCompletion.triggerCompletion(self.view, options)
	







hxsublime_commands_HaxeMacroHintDisplayCompletionCommand._hx_class = hxsublime_commands_HaxeMacroHintDisplayCompletionCommand
hxsublime_commands_HaxeMacroHintDisplayCompletionCommand._hx_class_name = "hxsublime.commands.HaxeMacroHintDisplayCompletionCommand"
_hx_classes['hxsublime.commands.HaxeMacroHintDisplayCompletionCommand'] = hxsublime_commands_HaxeMacroHintDisplayCompletionCommand
hxsublime_commands_HaxeMacroHintDisplayCompletionCommand._hx_fields = []
hxsublime_commands_HaxeMacroHintDisplayCompletionCommand._hx_props = []
hxsublime_commands_HaxeMacroHintDisplayCompletionCommand._hx_methods = ["run"]
hxsublime_commands_HaxeMacroHintDisplayCompletionCommand._hx_statics = []
hxsublime_commands_HaxeMacroHintDisplayCompletionCommand._hx_interfaces = []
hxsublime_commands_HaxeMacroHintDisplayCompletionCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.Completion.Helper
class hxsublime_commands_Helper:

	pass




def Helper_statics_isValidCompletion(view,edit,inputChar):
	valid = True
	if inputChar == "(":
		src = hxsublime_tools_ViewTools.getContentUntilFirstCursor(view)
		if hxsublime_commands_Helper.isOpenParensAfterFunctionDefinition(src):
			haxe_Log.trace("Invalid Completion is open par after function", _Hx_AnonObject(fileName = "Completion.hx" ,lineNumber = 112 ,className = "hxsublime.commands.Helper" ,methodName = "isValidCompletion" ))
			valid = False
		
		
	
	
	if inputChar == ",":
		src = hxsublime_tools_ViewTools.getContentUntilFirstCursor(view)
		if hxsublime_commands_Helper.isCommaAfterOpenParensInFunctionDefinition(src):
			haxe_Log.trace("Invalid Completion is open par after function", _Hx_AnonObject(fileName = "Completion.hx" ,lineNumber = 122 ,className = "hxsublime.commands.Helper" ,methodName = "isValidCompletion" ))
			valid = False
		
		
	
	
	return valid
	
hxsublime_commands_Helper.isValidCompletion = Helper_statics_isValidCompletion
hxsublime_commands_Helper.anonFunc = python_lib_Re.compile("^function(\\s+[a-zA-Z0-9$_]*\\s+)?\\s*\\($")
def Helper_statics_isOpenParensAfterFunctionDefinition(src):
	lastFunction = src.rfind("function", None)
	srcPart = python_Tools.substr(src, lastFunction, None)
	match = python_lib_Re.match(hxsublime_commands_Helper.anonFunc, srcPart)
	return match is not None
	
hxsublime_commands_Helper.isOpenParensAfterFunctionDefinition = Helper_statics_isOpenParensAfterFunctionDefinition
def Helper_statics_isCommaAfterOpenParensInFunctionDefinition(src):
	found = hxsublime_tools_HxSrcTools.reverse_search_next_char_on_same_nesting_level(src, ["("], __builtin__.len(src) - 1)
	res = False
	if found is not None:
		srcUntilComma = None
		endIndex = found[0] + 1
		srcUntilComma = python_Tools.substring(src, 0, endIndex)
		
		res = hxsublime_commands_Helper.isOpenParensAfterFunctionDefinition(srcUntilComma)
	
	
	return res
	
hxsublime_commands_Helper.isCommaAfterOpenParensInFunctionDefinition = Helper_statics_isCommaAfterOpenParensInFunctionDefinition


hxsublime_commands_Helper._hx_class = hxsublime_commands_Helper
hxsublime_commands_Helper._hx_class_name = "hxsublime.commands.Helper"
_hx_classes['hxsublime.commands.Helper'] = hxsublime_commands_Helper
hxsublime_commands_Helper._hx_fields = []
hxsublime_commands_Helper._hx_props = []
hxsublime_commands_Helper._hx_methods = []
hxsublime_commands_Helper._hx_statics = ["isValidCompletion","anonFunc","isOpenParensAfterFunctionDefinition","isCommaAfterOpenParensInFunctionDefinition"]
hxsublime_commands_Helper._hx_interfaces = []

# print sublime.WindowCommand.WindowCommand
from sublime_plugin import WindowCommand as sublime_WindowCommand
# print hxsublime.commands.CompletionServer.HaxeRestartServerCommand
class hxsublime_commands_HaxeRestartServerCommand(sublime_WindowCommand):


	def __init__(self,w):
		super().__init__(w)
	def run(self,**kwArgs):
		haxe_Log.trace("run HaxeRestartServerCommand", _Hx_AnonObject(fileName = "CompletionServer.hx" ,lineNumber = 14 ,className = "hxsublime.commands.HaxeRestartServerCommand" ,methodName = "run" ))
		view = sublime_Sublime.active_window().active_view()
		project = hxsublime_project_Projects.currentProject(view)
		project.restartServer(view)
	







hxsublime_commands_HaxeRestartServerCommand._hx_class = hxsublime_commands_HaxeRestartServerCommand
hxsublime_commands_HaxeRestartServerCommand._hx_class_name = "hxsublime.commands.HaxeRestartServerCommand"
_hx_classes['hxsublime.commands.HaxeRestartServerCommand'] = hxsublime_commands_HaxeRestartServerCommand
hxsublime_commands_HaxeRestartServerCommand._hx_fields = []
hxsublime_commands_HaxeRestartServerCommand._hx_props = []
hxsublime_commands_HaxeRestartServerCommand._hx_methods = ["run"]
hxsublime_commands_HaxeRestartServerCommand._hx_statics = []
hxsublime_commands_HaxeRestartServerCommand._hx_interfaces = []
hxsublime_commands_HaxeRestartServerCommand._hx_super = sublime_WindowCommand

# print hxsublime.commands.CreateType.State
class hxsublime_commands_CreateType_State:

	pass




hxsublime_commands_CreateType_State.current_create_type_info = haxe_ds_StringMap()


hxsublime_commands_CreateType_State._hx_class = hxsublime_commands_CreateType_State
hxsublime_commands_CreateType_State._hx_class_name = "hxsublime.commands._CreateType._CreateType.State"
_hx_classes['hxsublime.commands._CreateType._CreateType.State'] = hxsublime_commands_CreateType_State
hxsublime_commands_CreateType_State._hx_fields = []
hxsublime_commands_CreateType_State._hx_props = []
hxsublime_commands_CreateType_State._hx_methods = []
hxsublime_commands_CreateType_State._hx_statics = ["current_create_type_info"]
hxsublime_commands_CreateType_State._hx_interfaces = []

# print hxsublime.commands.CreateType.HaxeCreateTypeCommand
class hxsublime_commands_HaxeCreateTypeCommand(sublime_WindowCommand):


	def __init__(self,win):
		super().__init__(win)
		self.classpath = None
		self.win = win
	
	# var classpath
	# var win
	def run(self,**kwArgs):
		_g = self
		paths = python_lib_Types_KwArgs_Impl_.get(kwArgs, "paths", [])
		t = python_lib_Types_KwArgs_Impl_.get(kwArgs, "t", "class")
		haxe_Log.trace("createtype", _Hx_AnonObject(fileName = "CreateType.hx" ,lineNumber = 47 ,className = "hxsublime.commands.HaxeCreateTypeCommand" ,methodName = "run" ))
		view = self.win.active_view()
		project = hxsublime_project_Projects.currentProject(view)
		builds = __builtin__.list(project.builds)
		if project.hasBuild():
			builds.insert(0, project.getBuild(view))
		
		pack = []
		if __builtin__.len(builds) == 0 and view is not None and view.file_name() is not None:
			haxe_Log.trace(view.file_name(), _Hx_AnonObject(fileName = "CreateType.hx" ,lineNumber = 65 ,className = "hxsublime.commands.HaxeCreateTypeCommand" ,methodName = "run" ))
			project.extractBuildArgs(view)
			builds = project.builds
		
		
		if __builtin__.len(paths) == 0 and view is not None:
			fn = view.file_name()
			paths.append(fn)
			__builtin__.len(paths)
			
		
		
		_g1 = 0
		while _g1 < len(paths):
			path = paths[_g1]
			_g1 = _g1 + 1
			if python_lib_os_Path.isfile(path):
				path = python_lib_os_Path.dirname(path)
			
			if self.classpath is None:
				self.classpath = path
			
			_g11 = 0
			while _g11 < len(builds):
				b = builds[_g11]
				_g11 = _g11 + 1
				haxe_Log.trace("build file: " + b.buildFile(), _Hx_AnonObject(fileName = "CreateType.hx" ,lineNumber = 91 ,className = "hxsublime.commands.HaxeCreateTypeCommand" ,methodName = "run" ))
				found = False
				_g2 = 0
				_g3 = b.classpaths()
				while _g2 < len(_g3):
					cp = _g3[_g2]
					_g2 = _g2 + 1
					haxe_Log.trace("class path: " + cp, _Hx_AnonObject(fileName = "CreateType.hx" ,lineNumber = 95 ,className = "hxsublime.commands.HaxeCreateTypeCommand" ,methodName = "run" ))
					haxe_Log.trace("path: " + path, _Hx_AnonObject(fileName = "CreateType.hx" ,lineNumber = 96 ,className = "hxsublime.commands.HaxeCreateTypeCommand" ,methodName = "run" ))
					if StringTools.startsWith(path, cp):
						endIndex = __builtin__.len(cp)
						self.classpath = python_Tools.substring(path, 0, endIndex)
						
						haxe_Log.trace("this.classpath: " + self.classpath, _Hx_AnonObject(fileName = "CreateType.hx" ,lineNumber = 101 ,className = "hxsublime.commands.HaxeCreateTypeCommand" ,methodName = "run" ))
						rel_path = None
						pos = __builtin__.len(cp) + 1
						rel_path = python_Tools.substr(path, pos, None)
						
						haxe_Log.trace(rel_path, _Hx_AnonObject(fileName = "CreateType.hx" ,lineNumber = 105 ,className = "hxsublime.commands.HaxeCreateTypeCommand" ,methodName = "run" ))
						if __builtin__.len(rel_path) == 0:
							found = True
						else:
							sub_packs = rel_path.split(python_lib_Os.sep)
							haxe_Log.trace("subpacks:" + Std.string(sub_packs), _Hx_AnonObject(fileName = "CreateType.hx" ,lineNumber = 113 ,className = "hxsublime.commands.HaxeCreateTypeCommand" ,methodName = "run" ))
							_g4 = 0
							while _g4 < len(sub_packs):
								p = sub_packs[_g4]
								_g4 = _g4 + 1
								if p.find(".") > -1:
									break
								elif p is not None:
									pack.append(p)
									__builtin__.len(pack)
									
									found = True
								
								
							
							
						
					
					
					if found:
						break
					
				
				
				if found:
					break
				
				haxe_Log.trace("found: " + Std.string(found), _Hx_AnonObject(fileName = "CreateType.hx" ,lineNumber = 139 ,className = "hxsublime.commands.HaxeCreateTypeCommand" ,methodName = "run" ))
			
			
		
		
		if self.classpath is None:
			if __builtin__.len(builds) > 0:
				self.classpath = builds[0].classpaths()[0]
			
		
		haxe_Log.trace(pack, _Hx_AnonObject(fileName = "CreateType.hx" ,lineNumber = 150 ,className = "hxsublime.commands.HaxeCreateTypeCommand" ,methodName = "run" ))
		packSuggestion = ".".join(pack)
		if __builtin__.len(packSuggestion) > 0:
			packSuggestion = packSuggestion + "."
		
		sublime_Sublime.status_message("Current classpath : " + self.classpath)
		def _hx_local_0(inp):
			_g.onDone(inp, t)
		self.win.show_input_panel("Enter " + t + " name : ", packSuggestion, _hx_local_0, self.onChange, self.onCancel)
	

	def onDone(self,inp,cur_type):
		fn = self.classpath
		parts = inp.split(".")
		pack = []
		cl = None
		while __builtin__.len(parts) > 0:
			p = parts.pop(0)
			fn = python_lib_os_Path.join(fn, p)
			if hxsublime_tools_Regex.isType.match(p) is not None:
				cl = p
				break
			
			else:
				pack.append(p)
				__builtin__.len(pack)
			
		
		if __builtin__.len(parts) > 0:
			cl = parts[0]
		
		fn = fn + ".hx"
		src = "\npackage " + ".".join(pack) + ";\n\n" + cur_type + " " + Std.string(cl) + " "
		if cur_type == "typedef":
			src = src + "= "
		
		src = src + "{\n\n\t\n\n}"
		hxsublime_commands_CreateType_State.current_create_type_info.set(fn, src)
		sublime_Sublime.active_window().open_file(fn)
	

	def onChange(self,inp):
		haxe_Log.trace(inp, _Hx_AnonObject(fileName = "CreateType.hx" ,lineNumber = 211 ,className = "hxsublime.commands.HaxeCreateTypeCommand" ,methodName = "onChange" ))

	def onCancel(self):
		haxe_Log.trace("cancel", _Hx_AnonObject(fileName = "CreateType.hx" ,lineNumber = 216 ,className = "hxsublime.commands.HaxeCreateTypeCommand" ,methodName = "onCancel" ))







hxsublime_commands_HaxeCreateTypeCommand._hx_class = hxsublime_commands_HaxeCreateTypeCommand
hxsublime_commands_HaxeCreateTypeCommand._hx_class_name = "hxsublime.commands.HaxeCreateTypeCommand"
_hx_classes['hxsublime.commands.HaxeCreateTypeCommand'] = hxsublime_commands_HaxeCreateTypeCommand
hxsublime_commands_HaxeCreateTypeCommand._hx_fields = ["classpath","win"]
hxsublime_commands_HaxeCreateTypeCommand._hx_props = []
hxsublime_commands_HaxeCreateTypeCommand._hx_methods = ["run","onDone","onChange","onCancel"]
hxsublime_commands_HaxeCreateTypeCommand._hx_statics = []
hxsublime_commands_HaxeCreateTypeCommand._hx_interfaces = []
hxsublime_commands_HaxeCreateTypeCommand._hx_super = sublime_WindowCommand

# print hxsublime.commands.CreateType.HaxeCreateTypeListener
class hxsublime_commands_HaxeCreateTypeListener(sublime_EventListener):

	def on_load(self,view):
		can_create_file = view is not None and view.file_name() is not None and hxsublime_commands_CreateType_State.current_create_type_info.exists(view.file_name()) and view.size() == 0
		if can_create_file:
			self.create_file(view)
		
	

	def create_file(self,view):
		data = hxsublime_commands_CreateType_State.current_create_type_info.get(view.file_name())
		def _hx_local_0(v,edit):
			haxe_Log.trace(data, _Hx_AnonObject(fileName = "CreateType.hx" ,lineNumber = 239 ,className = "hxsublime.commands.HaxeCreateTypeListener" ,methodName = "create_file" ))
			v.insert(edit, 0, data)
			sel = v.sel()
			sel.clear()
			pt = v.text_point(5, 1)
			sel.add(sublime_Region(pt, pt))
		
		run_edit = _hx_local_0
		hxsublime_tools_ViewTools.asyncEdit(view, run_edit)
	







hxsublime_commands_HaxeCreateTypeListener._hx_class = hxsublime_commands_HaxeCreateTypeListener
hxsublime_commands_HaxeCreateTypeListener._hx_class_name = "hxsublime.commands.HaxeCreateTypeListener"
_hx_classes['hxsublime.commands.HaxeCreateTypeListener'] = hxsublime_commands_HaxeCreateTypeListener
hxsublime_commands_HaxeCreateTypeListener._hx_fields = []
hxsublime_commands_HaxeCreateTypeListener._hx_props = []
hxsublime_commands_HaxeCreateTypeListener._hx_methods = ["on_load","create_file"]
hxsublime_commands_HaxeCreateTypeListener._hx_statics = []
hxsublime_commands_HaxeCreateTypeListener._hx_interfaces = []
hxsublime_commands_HaxeCreateTypeListener._hx_super = sublime_EventListener

# print hxsublime.commands.Execute.Helper
class hxsublime_commands_Execute_Helper:

	pass




def Helper_statics_escape_cmd(cmd):
	print_cmd = __builtin__.list(cmd)
	l = __builtin__.len(print_cmd)
	_g = 0
	while _g < l:
		def _hx_local_1():
			nonlocal _g
			_hx_local_0 = _g
			_g = _g + 1
			return _hx_local_0
			
		
		i = _hx_local_1()
		e = print_cmd[i]
		if e == "--macro" and i < l - 1:
			print_cmd[i + 1] = "'" + print_cmd[i + 1] + "'"
		
	
	
	return print_cmd
	
hxsublime_commands_Execute_Helper.escape_cmd = Helper_statics_escape_cmd


hxsublime_commands_Execute_Helper._hx_class = hxsublime_commands_Execute_Helper
hxsublime_commands_Execute_Helper._hx_class_name = "hxsublime.commands._Execute._Execute.Helper"
_hx_classes['hxsublime.commands._Execute._Execute.Helper'] = hxsublime_commands_Execute_Helper
hxsublime_commands_Execute_Helper._hx_fields = []
hxsublime_commands_Execute_Helper._hx_props = []
hxsublime_commands_Execute_Helper._hx_methods = []
hxsublime_commands_Execute_Helper._hx_statics = ["escape_cmd"]
hxsublime_commands_Execute_Helper._hx_interfaces = []

# print sublime.def.exec.ProcessListener.ProcessListener
import Default
sublime_def_exec_ProcessListener = getattr(Default, 'exec').ProcessListener
	
# print hxsublime.commands.Execute.HaxeExecCommand
class hxsublime_commands_HaxeExecCommand(sublime_WindowCommand):


	def __init__(self,window):
		self.proc = None
		self.output_view = None
		super().__init__(window)
	
	# var is_check_run
	# var output_view
	# var proc
	# var encoding
	# var quiet
	def run(self,**kwArgs):
		cmd = python_lib_Types_KwArgs_Impl_.get(kwArgs, "cmd", [])
		file_regex = python_lib_Types_KwArgs_Impl_.get(kwArgs, "file_regex", "")
		line_regex = python_lib_Types_KwArgs_Impl_.get(kwArgs, "line_regex", "")
		working_dir = python_lib_Types_KwArgs_Impl_.get(kwArgs, "working_dir", "")
		self.encoding = python_lib_Types_KwArgs_Impl_.get(kwArgs, "encoding", "utf-8")
		env = python_lib_Types_KwArgs_Impl_.get(kwArgs, "env", python_lib_Dict())
		self.quiet = python_lib_Types_KwArgs_Impl_.get(kwArgs, "quiet", False)
		kill = python_lib_Types_KwArgs_Impl_.get(kwArgs, "kill", False)
		is_check_run = python_lib_Types_KwArgs_Impl_.get(kwArgs, "is_check_run", False)
		haxe_Log.trace("ENV1: " + Std.string(env), _Hx_AnonObject(fileName = "Execute.hx" ,lineNumber = 73 ,className = "hxsublime.commands.HaxeExecCommand" ,methodName = "run" ))
		self.is_check_run = is_check_run
		if self.encoding is None:
			self.encoding = python_lib_Sys.getfilesystemencoding()
		
		haxe_Log.trace("run haxe exec", _Hx_AnonObject(fileName = "Execute.hx" ,lineNumber = 83 ,className = "hxsublime.commands.HaxeExecCommand" ,methodName = "run" ))
		if self.output_view is None:
			self.output_view = self.window.create_output_panel("exec")
			self.output_view.settings().set("word_wrap", True)
		
		
		if kill:
			if self.proc is not None:
				self.proc.kill()
				self.proc = None
				self.append_data(None, python_lib_StringTools.encode("[Cancelled]", "utf-8"))
			
			
			return
		
		
		if working_dir == "" and self.window.active_view() is not None and self.window.active_view().file_name() is not None:
			working_dir = python_lib_os_Path.dirname(self.window.active_view().file_name())
		
		self.output_view.settings().set("result_file_regex", file_regex)
		self.output_view.settings().set("result_line_regex", line_regex)
		self.output_view.settings().set("result_base_dir", working_dir)
		haxe_Log.trace("WORKING DIR:" + working_dir, _Hx_AnonObject(fileName = "Execute.hx" ,lineNumber = 114 ,className = "hxsublime.commands.HaxeExecCommand" ,methodName = "run" ))
		self.window.create_output_panel("exec")
		self.proc = None
		if not self.quiet:
			def _hx_local_1(a):
				a1 = None
				_this = a.split("\"")
				a1 = "\\\"".join(_this)
				
				if __builtin__.len(a1) >= 2:
					if StringTools.startsWith(a1, "\\\""):
						a1 = "\"" + python_Tools.substr(a1, 2, None)
					else:
						a1 = a1
					if StringTools.endsWith(a1, "\\\""):
						def _hx_local_0():
							endIndex = __builtin__.len(a1) - 2
							return python_Tools.substring(a1, 0, endIndex)
						
						a1 = _hx_local_0() + "\""
					
					else:
						a1 = a1
				
				
				return a1
			
			escape_arg = _hx_local_1
			def _hx_local_2():
				_this = __builtin__.list(__builtin__.map(escape_arg, cmd))
				return " ".join(_this)
			
			haxe_Log.trace("Running Command : " + _hx_local_2(), _Hx_AnonObject(fileName = "Execute.hx" ,lineNumber = 135 ,className = "hxsublime.commands.HaxeExecCommand" ,methodName = "run" ))
			sublime_Sublime.status_message("Building")
		
		
		show_panel_on_build = sublime_Sublime.load_settings("Preferences.sublime-settings").get("show_panel_on_build", True)
		if show_panel_on_build:
			def _hx_local_3():
				x = _Hx_AnonObject(panel = "output.exec" )
				def _hx_local_5():
					def _hx_local_4():
						d = python_lib_Dict()
						_g = 0
						_g1 = Reflect.fields(x)
						while _g < len(_g1):
							f = _g1[_g]
							_g = _g + 1
							val = Reflect.field(x, f)
							python_lib_DictImpl.set(d, f, val)
							
						
						
						return d
					
					return _hx_local_4()
				
				return _hx_local_5()
			
			self.window.run_command("show_panel", _hx_local_3())
		
		
		merged_env = env.copy()
		if self.window.active_view() is not None:
			user_env = self.window.active_view().settings().get("build_env")
			if user_env is not None:
				merged_env.update(user_env)
			
		
		
		if working_dir != "":
			python_lib_Os.chdir(working_dir)
		
		try:
			haxe_Log.trace("CMD:" + Std.string(cmd), _Hx_AnonObject(fileName = "Execute.hx" ,lineNumber = 174 ,className = "hxsublime.commands.HaxeExecCommand" ,methodName = "run" ))
			haxe_Log.trace("ENV:" + Std.string(merged_env), _Hx_AnonObject(fileName = "Execute.hx" ,lineNumber = 175 ,className = "hxsublime.commands.HaxeExecCommand" ,methodName = "run" ))
			d = kwArgs
			if python_lib_DictImpl.hasKey(d, "working_dir"):
				python_lib_DictImpl.remove(d, "working_dir")
			
			if python_lib_DictImpl.hasKey(d, "file_regex"):
				python_lib_DictImpl.remove(d, "file_regex")
			
			if python_lib_DictImpl.hasKey(d, "line_regex"):
				python_lib_DictImpl.remove(d, "line_regex")
			
			if python_lib_DictImpl.hasKey(d, "encoding"):
				python_lib_DictImpl.remove(d, "encoding")
			
			if python_lib_DictImpl.hasKey(d, "is_check_run"):
				python_lib_DictImpl.remove(d, "is_check_run")
			
			if python_lib_DictImpl.hasKey(d, "env"):
				python_lib_DictImpl.remove(d, "env")
			
			if python_lib_DictImpl.hasKey(d, "cmd"):
				python_lib_DictImpl.remove(d, "cmd")
			
			self.proc = sublime_def_exec_AsyncProcess(cmd, None, merged_env, self, **kwArgs)
			def _hx_local_6():
				_this = hxsublime_commands_Execute_Helper.escape_cmd(cmd)
				return " ".join(_this)
			
			self.append_data(self.proc, python_lib_StringTools.encode("Running Command: " + _hx_local_6() + "\n", "utf-8"))
		
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			if True:
				e = _hx_e1
				self.append_data_str(None, Std.string(e) + "\n")
				self.append_data_str(None, "[cmd:  " + Std.string(cmd) + "]\n")
				self.append_data_str(None, "[dir:  " + python_lib_Os.getcwdb().decode("utf-8") + "]\n")
				if python_lib_DictImpl.hasKey(merged_env, "PATH"):
					self.append_data_str(None, "[path: " + merged_env.get("PATH", "") + "]\n")
				else:
					self.append_data_str(None, "[path: " + Std.string(python_lib_Os.environ.get("PATH", "")) + "]\n")
				if not self.quiet:
					self.append_data_str(None, "[Finished]")
				
		
			else:
				raise _hx_e
	

	def is_enabled(self,**kwArgs):
		kill = python_lib_Types_KwArgs_Impl_.get(kwArgs, "kill", False)
		if kill:
			return self.proc is not None and self.proc.poll()
		else:
			return True
	

	def append_data_str(self,proc,data):
		self.append_data(proc, python_lib_StringTools.encode(data, "utf-8"))

	def append_data(self,proc,data):
		_g = self
		if proc != self.proc:
			if proc is not None:
				try:
					proc.kill()
				except Exception as _hx_e:
					_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
					if True:
						e = _hx_e1
						None
					else:
						raise _hx_e
			
			return
		
		
		st = None
		try:
			st = data.decode(self.encoding)
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			if True:
				e = _hx_e1
				st = "[Decode error - output not " + self.encoding + "]\n"
				proc = None
		
			else:
				raise _hx_e
		if self.is_check_run and st.find("Embedding assets failed! We encountered an error accessing") > -1:
			return
		
		st = StringTools.replace(StringTools.replace(st, "\r\n", "\n"), "\r", "\n")
		sel = self.output_view.sel()
		selection_was_at_end = __builtin__.len(sel) == 1 and sel[0] == sublime_Region(self.output_view.size())
		def _hx_local_0(v,edit):
			v.set_read_only(False)
			v.insert(edit, _g.output_view.size(), st)
			if selection_was_at_end:
				v.show(_g.output_view.size())
			
			v.set_read_only(True)
		
		do_edit = _hx_local_0
		hxsublime_tools_ViewTools.asyncEdit(self.output_view, do_edit)
	

	def finish(self,proc):
		v = self.output_view
		if not self.quiet:
			elapsed = python_lib_Time.time() - proc.start_time
			exit_code = proc.exit_code()
			if exit_code == 0 or exit_code is None:
				self.append_data_str(proc, "[Finished in " + Std.string(elapsed) + "]")
			else:
				self.append_data_str(proc, "[Finished in " + Std.string(elapsed) + " with exit code " + Std.string(exit_code) + "]")
		
		
		if proc != self.proc:
			return
		
		v.sel().clear()
		v.sel().add(sublime_Region(0))
	

	def on_data(self,proc,data):
		def _hx_local_0():
			haxe_Log.trace(data, _Hx_AnonObject(fileName = "Execute.hx" ,lineNumber = 324 ,className = "hxsublime.commands.HaxeExecCommand" ,methodName = "on_data" ))
		sublime_Sublime.set_timeout(_hx_local_0, 0)
		def _hx_local_1():
			f = self.append_data
			a1 = proc
			a2 = data
			def _hx_local_2():
				return f(a1, a2)
			return _hx_local_2
		
		sublime_Sublime.set_timeout(_hx_local_1(), 0)
	

	def on_finished(self,proc):
		def _hx_local_0():
			f = self.finish
			a1 = proc
			def _hx_local_1():
				return f(a1)
			return _hx_local_1
		
		sublime_Sublime.set_timeout(_hx_local_0(), 0)
	







hxsublime_commands_HaxeExecCommand._hx_class = hxsublime_commands_HaxeExecCommand
hxsublime_commands_HaxeExecCommand._hx_class_name = "hxsublime.commands.HaxeExecCommand"
_hx_classes['hxsublime.commands.HaxeExecCommand'] = hxsublime_commands_HaxeExecCommand
hxsublime_commands_HaxeExecCommand._hx_fields = ["is_check_run","output_view","proc","encoding","quiet"]
hxsublime_commands_HaxeExecCommand._hx_props = []
hxsublime_commands_HaxeExecCommand._hx_methods = ["run","is_enabled","append_data_str","append_data","finish","on_data","on_finished"]
hxsublime_commands_HaxeExecCommand._hx_statics = []
hxsublime_commands_HaxeExecCommand._hx_interfaces = [sublime_def_exec_ProcessListener]
hxsublime_commands_HaxeExecCommand._hx_super = sublime_WindowCommand

# print hxsublime.commands.FindDeclaration.HaxeFindDeclarationCommand
class hxsublime_commands_HaxeFindDeclarationCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**_):
		if _ is None:
			_ = None
		
		self.run1(True)
	

	def helperMethod(self):
		return "hxsublime.FindDeclaration.__sublimeFindDecl"

	def run1(self,useDisplay,order = 1):
		if order is None:
			order = 1
		
		_g = self
		haxe_Log.trace("run HaxeFindDeclarationCommand", _Hx_AnonObject(fileName = "FindDeclaration.hx" ,lineNumber = 43 ,className = "hxsublime.commands.HaxeFindDeclarationCommand" ,methodName = "run1" ))
		view = self.view
		if view.file_name() is None:
			return
		
		project = hxsublime_project_Projects.currentProject(view)
		if not project.hasBuild():
			project.extractBuildArgs(view, False)
		
		if not project.hasBuild():
			project.extractBuildArgs(view, True)
			return
		
		
		helperMethod = self.helperMethod()
		src = hxsublime_tools_ViewTools.getContent(view)
		packageMatch = python_lib_Re.match(hxsublime_tools_Regex.package_line, src)
		usingPos = None
		if packageMatch is None:
			usingPos = 0
		else:
			usingPos = packageMatch.end(0)
		usingInsert = "using hxsublime.FindDeclaration;"
		srcBeforeUsing = python_Tools.substring(src, 0, usingPos)
		sel = view.sel()[0]
		pos = sel.begin()
		exprEnd = None
		exprStart = None
		if sel.end() == pos:
			r = hxsublime_commands_FindDeclaration_Helper.getWordAt(view, src, pos)
			word_str = r[0]
			word_start = r[1]
			word_end = r[2]
			chars = ["{", "+", "-", "(", "[", "*", "/", "=", ";", ":"]
			res = hxsublime_tools_HxSrcTools.reverse_search_next_char_on_same_nesting_level(src, chars, word_end - 1)
			res = hxsublime_tools_HxSrcTools.skipWhitespaceOrComments(src, res[0] + 1)
			exprEnd = word_end
			exprStart = res[0]
		
		else:
			exprStart = pos
			exprEnd = sel.end()
		
		srcBeforeExpr = python_Tools.substring(src, usingPos, exprStart)
		srcAfterExpr = python_Tools.substr(src, exprEnd, None)
		exprString = python_Tools.substring(src, exprStart, exprEnd)
		displayStr = None
		if useDisplay:
			displayStr = ".|"
		else:
			displayStr = ""
		insertBefore = helperMethod + "("
		orderStr = Std.string(order)
		insertAfter = ", " + orderStr + ")" + displayStr
		newSrc = srcBeforeUsing + usingInsert + srcBeforeExpr + insertBefore + exprString + insertAfter + srcAfterExpr
		r = hxsublime_commands_FindDeclaration_Helper.prepareBuild(view, project, useDisplay, newSrc)
		build = r[0]
		temp_path = r[1]
		tempFile = r[2]
		def _hx_local_0(out,err):
			hxsublime_Temp.removePath(temp_path)
			filePos = python_lib_Re.compile("\\|\\|\\|\\|\\|([^|]+)\\|\\|\\|\\|\\|", python_lib_Re.I)
			res = python_lib_Re.search(filePos, out)
			if res is not None:
				json_str = res.group(1)
				jsonResult = python_lib_Json.loads(json_str)
				if python_lib_DictImpl.hasKey(jsonResult, "error"):
					error = jsonResult.get("error", None)
					haxe_Log.trace("nothing found (1), cannot find declaration", _Hx_AnonObject(fileName = "FindDeclaration.hx" ,lineNumber = 149 ,className = "hxsublime.commands.HaxeFindDeclarationCommand" ,methodName = "run1" ))
					if order == 1 and useDisplay:
						_g.run1(True, 2)
					elif order == 2 and useDisplay:
						_g.run1(True, 3)
					
				
				else:
					_g.handleSuccessfulResult(view, jsonResult, usingInsert, insertBefore, insertAfter, exprEnd, build, temp_path, tempFile)
			
			elif order == 1 and useDisplay:
				_g.run1(True, 2)
			elif order == 2 and useDisplay:
				_g.run1(True, 3)
			elif useDisplay:
				haxe_Log.trace("nothing found yet (2), try again without display (workaround)", _Hx_AnonObject(fileName = "FindDeclaration.hx" ,lineNumber = 176 ,className = "hxsublime.commands.HaxeFindDeclarationCommand" ,methodName = "run1" ))
				_g.run1(False)
			
			else:
				hxsublime_panel_Panels.defaultPanel().writeln("Cannot find declaration for expression " + exprString.strip(None))
				haxe_Log.trace("nothing found (3), cannot find declaration", _Hx_AnonObject(fileName = "FindDeclaration.hx" ,lineNumber = 182 ,className = "hxsublime.commands.HaxeFindDeclarationCommand" ,methodName = "run1" ))
			
		
		cb = _hx_local_0
		build.run(project, view, False, cb)
	

	def handleSuccessfulResult(self,view,jsonResult,usingInsert,insertBefore,insertAfter,exprEnd,build,temp_path,tempFile):
		file = jsonResult.get("file", None)
		min = jsonResult.get("min", 0)
		max = jsonResult.get("max", 0)
		absPath = hxsublime_tools_PathTools.joinNorm(build.getBuildFolder(), file)
		if absPath == tempFile:
			if min > exprEnd:
				min = min - __builtin__.len(insertAfter)
				min = min - __builtin__.len(insertBefore)
			
			
			min = min - __builtin__.len(usingInsert)
		
		else:
			f = python_lib_Codecs.open(absPath, "r", "utf-8")
			realSrc = f.read()
			f.close()
			offset = 0
			_g = 0
			while _g < min:
				def _hx_local_1():
					nonlocal _g
					_hx_local_0 = _g
					_g = _g + 1
					return _hx_local_0
					
				
				i = _hx_local_1()
				if realSrc[i] == "\r":
					offset = offset + 1
				
			
			
			haxe_Log.trace("offset: " + Std.string(offset), _Hx_AnonObject(fileName = "FindDeclaration.hx" ,lineNumber = 227 ,className = "hxsublime.commands.HaxeFindDeclarationCommand" ,methodName = "handleSuccessfulResult" ))
			min = min - offset
		
		if absPath == tempFile:
			targetView = view
			haxe_Log.trace("line ending: " + Std.string(view.settings().get("line_ending")), _Hx_AnonObject(fileName = "FindDeclaration.hx" ,lineNumber = 239 ,className = "hxsublime.commands.HaxeFindDeclarationCommand" ,methodName = "handleSuccessfulResult" ))
			targetView.sel().clear()
			targetView.sel().add(sublime_Region(min))
			targetView.show(sublime_Region(min))
		
		else:
			hxsublime_commands_FindDeclaration_State.findDeclFile = absPath
			hxsublime_commands_FindDeclaration_State.findDeclPos = min
			view.window().open_file(absPath)
		
	







hxsublime_commands_HaxeFindDeclarationCommand._hx_class = hxsublime_commands_HaxeFindDeclarationCommand
hxsublime_commands_HaxeFindDeclarationCommand._hx_class_name = "hxsublime.commands.HaxeFindDeclarationCommand"
_hx_classes['hxsublime.commands.HaxeFindDeclarationCommand'] = hxsublime_commands_HaxeFindDeclarationCommand
hxsublime_commands_HaxeFindDeclarationCommand._hx_fields = []
hxsublime_commands_HaxeFindDeclarationCommand._hx_props = []
hxsublime_commands_HaxeFindDeclarationCommand._hx_methods = ["run","helperMethod","run1","handleSuccessfulResult"]
hxsublime_commands_HaxeFindDeclarationCommand._hx_statics = []
hxsublime_commands_HaxeFindDeclarationCommand._hx_interfaces = []
hxsublime_commands_HaxeFindDeclarationCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.FindDeclaration.State
class hxsublime_commands_FindDeclaration_State:

	pass




hxsublime_commands_FindDeclaration_State.findDeclFile = None
hxsublime_commands_FindDeclaration_State.findDeclPos = None


hxsublime_commands_FindDeclaration_State._hx_class = hxsublime_commands_FindDeclaration_State
hxsublime_commands_FindDeclaration_State._hx_class_name = "hxsublime.commands._FindDeclaration._FindDeclaration.State"
_hx_classes['hxsublime.commands._FindDeclaration._FindDeclaration.State'] = hxsublime_commands_FindDeclaration_State
hxsublime_commands_FindDeclaration_State._hx_fields = []
hxsublime_commands_FindDeclaration_State._hx_props = []
hxsublime_commands_FindDeclaration_State._hx_methods = []
hxsublime_commands_FindDeclaration_State._hx_statics = ["findDeclFile","findDeclPos"]
hxsublime_commands_FindDeclaration_State._hx_interfaces = []

# print python.lib.os.Path.Path
from os import path as python_lib_os_Path
# print hxsublime.commands.FindDeclaration.Helper
class hxsublime_commands_FindDeclaration_Helper:

	pass




hxsublime_commands_FindDeclaration_Helper.plugin_path = hxsublime_Plugin.plugin_base_dir()
def Helper_statics_getWordAt(view,src,pos):
	word = view.word(pos)
	wordStart = word.a
	wordEnd = word.b
	wordStr = python_Tools.substring(src, wordStart, wordEnd)
	return (wordStr, wordStart, wordEnd)
	
hxsublime_commands_FindDeclaration_Helper.getWordAt = Helper_statics_getWordAt
def Helper_statics_prepareBuild(view,project,useDisplay,newSrc):
	build = project.getBuild(view).copy()
	build.addArg(("-D", "no-inline"))
	r = hxsublime_Temp.createTempPathAndFile(build, view.file_name(), newSrc)
	tempPath = r[0]
	tempFile = r[1]
	build.addClasspath(tempPath)
	build.addClasspath(python_lib_os_Path.join(hxsublime_commands_FindDeclaration_Helper.plugin_path, "haxetools"))
	haxe_Log.trace(build.classpaths, _Hx_AnonObject(fileName = "FindDeclaration.hx" ,lineNumber = 292 ,className = "hxsublime.commands._FindDeclaration.Helper" ,methodName = "prepareBuild" ))
	build.addArg(("-dce", "no"))
	if useDisplay:
		build.setAutoCompletion(tempFile + "@0", False)
	
	return (build, tempPath, tempFile)
	
hxsublime_commands_FindDeclaration_Helper.prepareBuild = Helper_statics_prepareBuild


hxsublime_commands_FindDeclaration_Helper._hx_class = hxsublime_commands_FindDeclaration_Helper
hxsublime_commands_FindDeclaration_Helper._hx_class_name = "hxsublime.commands._FindDeclaration._FindDeclaration.Helper"
_hx_classes['hxsublime.commands._FindDeclaration._FindDeclaration.Helper'] = hxsublime_commands_FindDeclaration_Helper
hxsublime_commands_FindDeclaration_Helper._hx_fields = []
hxsublime_commands_FindDeclaration_Helper._hx_props = []
hxsublime_commands_FindDeclaration_Helper._hx_methods = []
hxsublime_commands_FindDeclaration_Helper._hx_statics = ["plugin_path","getWordAt","prepareBuild"]
hxsublime_commands_FindDeclaration_Helper._hx_interfaces = []

# print hxsublime.commands.FindDeclaration.HaxeFindDeclarationListener
class hxsublime_commands_HaxeFindDeclarationListener(sublime_EventListener):

	def on_activated(self,view):
		if view is not None and view.file_name() is not None:
			if view.file_name() == hxsublime_commands_FindDeclaration_State.findDeclFile:
				view.sel().clear()
				min = hxsublime_commands_FindDeclaration_State.findDeclPos
				view.sel().add(sublime_Region(min))
				def _hx_local_0():
					view.show_at_center(sublime_Region(min))
				show = _hx_local_0
				sublime_Sublime.set_timeout(show, 70)
			
			
			hxsublime_commands_FindDeclaration_State.findDeclFile = None
			hxsublime_commands_FindDeclaration_State.findDeclPos = None
	
		







hxsublime_commands_HaxeFindDeclarationListener._hx_class = hxsublime_commands_HaxeFindDeclarationListener
hxsublime_commands_HaxeFindDeclarationListener._hx_class_name = "hxsublime.commands.HaxeFindDeclarationListener"
_hx_classes['hxsublime.commands.HaxeFindDeclarationListener'] = hxsublime_commands_HaxeFindDeclarationListener
hxsublime_commands_HaxeFindDeclarationListener._hx_fields = []
hxsublime_commands_HaxeFindDeclarationListener._hx_props = []
hxsublime_commands_HaxeFindDeclarationListener._hx_methods = ["on_activated"]
hxsublime_commands_HaxeFindDeclarationListener._hx_statics = []
hxsublime_commands_HaxeFindDeclarationListener._hx_interfaces = []
hxsublime_commands_HaxeFindDeclarationListener._hx_super = sublime_EventListener

# print hxsublime.commands.GenerateImport.HaxeGenerateUsingCommand
class hxsublime_commands_HaxeGenerateUsingCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**_):
		if _ is None:
			_ = None
		
		haxe_Log.trace("run HaxeGenerateUsingCommand", _Hx_AnonObject(fileName = "GenerateImport.hx" ,lineNumber = 15 ,className = "hxsublime.commands.HaxeGenerateUsingCommand" ,methodName = "run" ))
		hxsublime_HaxeImportGenerator.generateUsing(self.view, edit)
	







hxsublime_commands_HaxeGenerateUsingCommand._hx_class = hxsublime_commands_HaxeGenerateUsingCommand
hxsublime_commands_HaxeGenerateUsingCommand._hx_class_name = "hxsublime.commands.HaxeGenerateUsingCommand"
_hx_classes['hxsublime.commands.HaxeGenerateUsingCommand'] = hxsublime_commands_HaxeGenerateUsingCommand
hxsublime_commands_HaxeGenerateUsingCommand._hx_fields = []
hxsublime_commands_HaxeGenerateUsingCommand._hx_props = []
hxsublime_commands_HaxeGenerateUsingCommand._hx_methods = ["run"]
hxsublime_commands_HaxeGenerateUsingCommand._hx_statics = []
hxsublime_commands_HaxeGenerateUsingCommand._hx_interfaces = []
hxsublime_commands_HaxeGenerateUsingCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.GenerateImport.HaxeGenerateImportCommand
class hxsublime_commands_HaxeGenerateImportCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**_):
		if _ is None:
			_ = None
		
		haxe_Log.trace("run HaxeGenerateImportCommand", _Hx_AnonObject(fileName = "GenerateImport.hx" ,lineNumber = 24 ,className = "hxsublime.commands.HaxeGenerateImportCommand" ,methodName = "run" ))
		hxsublime_HaxeImportGenerator.generateImport(self.view, edit)
	







hxsublime_commands_HaxeGenerateImportCommand._hx_class = hxsublime_commands_HaxeGenerateImportCommand
hxsublime_commands_HaxeGenerateImportCommand._hx_class_name = "hxsublime.commands.HaxeGenerateImportCommand"
_hx_classes['hxsublime.commands.HaxeGenerateImportCommand'] = hxsublime_commands_HaxeGenerateImportCommand
hxsublime_commands_HaxeGenerateImportCommand._hx_fields = []
hxsublime_commands_HaxeGenerateImportCommand._hx_props = []
hxsublime_commands_HaxeGenerateImportCommand._hx_methods = ["run"]
hxsublime_commands_HaxeGenerateImportCommand._hx_statics = []
hxsublime_commands_HaxeGenerateImportCommand._hx_interfaces = []
hxsublime_commands_HaxeGenerateImportCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.GetExprType.HaxeGetTypeOfExprCommand
class hxsublime_commands_HaxeGetTypeOfExprCommand(hxsublime_commands_HaxeFindDeclarationCommand):


	def __init__(self,v):
		super().__init__(v)
	def helperMethod(self):
		return "hxsublime.FindDeclaration.__getType"

	def handleSuccessfulResult(self,view,json_res,using_insert,insert_before,insert_after,expr_end,build,temp_path,temp_file):
		t = json_res.get("type", None)
		e = json_res.get("expr", None)
		msg = "Expr: " + e + "\n" + "Type: " + t
		hxsublime_panel_Panels.slidePanel().writeln(msg, None, False)
	







hxsublime_commands_HaxeGetTypeOfExprCommand._hx_class = hxsublime_commands_HaxeGetTypeOfExprCommand
hxsublime_commands_HaxeGetTypeOfExprCommand._hx_class_name = "hxsublime.commands.HaxeGetTypeOfExprCommand"
_hx_classes['hxsublime.commands.HaxeGetTypeOfExprCommand'] = hxsublime_commands_HaxeGetTypeOfExprCommand
hxsublime_commands_HaxeGetTypeOfExprCommand._hx_fields = []
hxsublime_commands_HaxeGetTypeOfExprCommand._hx_props = []
hxsublime_commands_HaxeGetTypeOfExprCommand._hx_methods = ["helperMethod","handleSuccessfulResult"]
hxsublime_commands_HaxeGetTypeOfExprCommand._hx_statics = []
hxsublime_commands_HaxeGetTypeOfExprCommand._hx_interfaces = []
hxsublime_commands_HaxeGetTypeOfExprCommand._hx_super = hxsublime_commands_HaxeFindDeclarationCommand

# print hxsublime.commands.GotoBase.HaxeGotoBaseCommand
class hxsublime_commands_HaxeGotoBaseCommand(sublime_TextCommand):


	def __init__(self,v):
		self.selecting_build = False
		super().__init__(v)
	
	# var selecting_build
	def getEntries(self,types):
		raise _HxException("abstract method")

	def getData(self,types):
		raise _HxException("abstract method")

	def getFile(self,data_entry):
		raise _HxException("abstract method")

	def getSrcPos(self,data_entry):
		raise _HxException("abstract method")

	def run(self,edit,**kwArgs):
		if kwArgs is None:
			kwArgs = None
		
		_g = self
		haxe_Log.trace("run HaxeListBuildFieldsCommand", _Hx_AnonObject(fileName = "GotoBase.hx" ,lineNumber = 51 ,className = "hxsublime.commands.HaxeGotoBaseCommand" ,methodName = "run" ))
		view = self.view
		project = hxsublime_project_Projects.currentProject(view)
		if not project.hasBuild():
			project.extractBuildArgs(view, False)
		
		if not project.hasBuild():
			project.extractBuildArgs(view, True)
			return
		
		
		build = project.getBuild(view)
		bundle = build.getTypes().merge(build.stdBundle())
		bundle_types = bundle.allTypesAndEnumConstructorsWithInfo()
		filtered_types = haxe_ds_StringMap()
		_it = bundle_types.keys()
		while _it.hasNext():
			k = _it.next()
			t = bundle_types.get(k)
			if build.isTypeAvailable(t):
				filtered_types.set(k, t)
			
		
		function_list = self.getEntries(filtered_types)
		function_list_data = self.getData(filtered_types)
		haxe_Log.trace(Std.string(function_list), _Hx_AnonObject(fileName = "GotoBase.hx" ,lineNumber = 93 ,className = "hxsublime.commands.HaxeGotoBaseCommand" ,methodName = "run" ))
		haxe_Log.trace(Std.string(__builtin__.len(function_list)), _Hx_AnonObject(fileName = "GotoBase.hx" ,lineNumber = 95 ,className = "hxsublime.commands.HaxeGotoBaseCommand" ,methodName = "run" ))
		self.selecting_build = True
		sublime_Sublime.status_message("Please select a type")
		win = view.window()
		sel = view.sel()
		if __builtin__.len(sel) == 1 and sel[0].begin() != sel[0].end():
			_this = hxsublime_tools_ViewTools.getContent(view)
			startIndex = sel[0].begin()
			endIndex = sel[0].end()
			hxsublime_commands_GotoBase_State._init_text = python_Tools.substring(_this, startIndex, endIndex)
		
		elif __builtin__.len(sel) == 1:
			reg = view.word(sel[0].begin())
			_this = hxsublime_tools_ViewTools.getContent(view)
			startIndex = reg.begin()
			endIndex = reg.end()
			hxsublime_commands_GotoBase_State._init_text = python_Tools.substring(_this, startIndex, endIndex)
			
		
		else:
			hxsublime_commands_GotoBase_State._init_text = ""
		def _hx_local_1(i):
			hxsublime_commands_GotoBase_State._is_open = False
			hxsublime_commands_GotoBase_State._init_text = ""
			if i >= 0:
				selected_type = function_list_data[i]
				haxe_Log.trace("selected field: " + Std.string(selected_type[0]), _Hx_AnonObject(fileName = "GotoBase.hx" ,lineNumber = 127 ,className = "hxsublime.commands.HaxeGotoBaseCommand" ,methodName = "run" ))
				src_pos = _g.getSrcPos(selected_type[1])
				goto_file = _g.getFile(selected_type[1])
				hxsublime_commands_GotoBase_State._find_decl_file = goto_file
				haxe_Log.trace("find_decl_file: " + Std.string(hxsublime_commands_GotoBase_State._find_decl_file), _Hx_AnonObject(fileName = "GotoBase.hx" ,lineNumber = 135 ,className = "hxsublime.commands.HaxeGotoBaseCommand" ,methodName = "run" ))
				if src_pos is not None:
					hxsublime_commands_GotoBase_State._find_decl_pos = src_pos
					haxe_Log.trace("src_pos" + Std.string(src_pos), _Hx_AnonObject(fileName = "GotoBase.hx" ,lineNumber = 139 ,className = "hxsublime.commands.HaxeGotoBaseCommand" ,methodName = "run" ))
				
				else:
					hxsublime_commands_GotoBase_State._find_decl_pos = 0
				def _hx_local_0():
					win.open_file(goto_file)
				show = _hx_local_0
				sublime_Sublime.set_timeout(show, 130)
			
			
		
		onSelected = _hx_local_1
		hxsublime_commands_GotoBase_State._is_open = True
		win.show_quick_panel(function_list, onSelected, sublime_Sublime.MONOSPACE_FONT)
	







hxsublime_commands_HaxeGotoBaseCommand._hx_class = hxsublime_commands_HaxeGotoBaseCommand
hxsublime_commands_HaxeGotoBaseCommand._hx_class_name = "hxsublime.commands.HaxeGotoBaseCommand"
_hx_classes['hxsublime.commands.HaxeGotoBaseCommand'] = hxsublime_commands_HaxeGotoBaseCommand
hxsublime_commands_HaxeGotoBaseCommand._hx_fields = ["selecting_build"]
hxsublime_commands_HaxeGotoBaseCommand._hx_props = []
hxsublime_commands_HaxeGotoBaseCommand._hx_methods = ["getEntries","getData","getFile","getSrcPos","run"]
hxsublime_commands_HaxeGotoBaseCommand._hx_statics = []
hxsublime_commands_HaxeGotoBaseCommand._hx_interfaces = []
hxsublime_commands_HaxeGotoBaseCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.GotoAnything.HaxeGotoAnythingCommand
class hxsublime_commands_HaxeGotoAnythingCommand(hxsublime_commands_HaxeGotoBaseCommand):


	def __init__(self,v):
		super().__init__(v)
	def getEntries(self,types):
		fields = None
		_g = []
		_it = types.keys()
		while _it.hasNext():
			k = _it.next()
			_g1 = 0
			_g2 = types.get(k).allFieldsList()
			while _g1 < len(_g2):
				p = _g2[_g1]
				_g1 = _g1 + 1
				x = [p.toString() + " - " + p.kind, p.type._file]
				_g.append(x)
				__builtin__.len(_g)
				
			
		
		fields = _g
		
		types1 = None
		_g1 = []
		_it = types.keys()
		while _it.hasNext():
			k = _it.next()
			def _hx_local_0():
				_this = types.get(k)
				return _this._file
			
			x = [k, _hx_local_0()]
			_g1.append(x)
			__builtin__.len(_g1)
			
		
		types1 = _g1
		
		fields.extend(types1)
		return fields
	

	def toEntry(self,e):
		return e

	def getData(self,types):
		fields = None
		_g = []
		_it = types.keys()
		while _it.hasNext():
			k = _it.next()
			_g1 = 0
			_g2 = types.get(k).allFieldsList()
			while _g1 < len(_g2):
				p = _g2[_g1]
				_g1 = _g1 + 1
				x = None
				b = self.toEntry(p)
				x = (k + "." + p.name, b)
				
				_g.append(x)
				__builtin__.len(_g)
				
			
		
		fields = _g
		
		types1 = None
		_g1 = []
		_it = types.keys()
		while _it.hasNext():
			k = _it.next()
			x = None
			b = self.toEntry(types.get(k))
			x = (k, b)
			
			_g1.append(x)
			__builtin__.len(_g1)
			
		
		types1 = _g1
		
		fields.extend(types1)
		return fields
	

	def getFile(self,dataEntry):
		return dataEntry.file()

	def getSrcPos(self,dataEntry):
		return dataEntry.srcPos()







hxsublime_commands_HaxeGotoAnythingCommand._hx_class = hxsublime_commands_HaxeGotoAnythingCommand
hxsublime_commands_HaxeGotoAnythingCommand._hx_class_name = "hxsublime.commands.HaxeGotoAnythingCommand"
_hx_classes['hxsublime.commands.HaxeGotoAnythingCommand'] = hxsublime_commands_HaxeGotoAnythingCommand
hxsublime_commands_HaxeGotoAnythingCommand._hx_fields = []
hxsublime_commands_HaxeGotoAnythingCommand._hx_props = []
hxsublime_commands_HaxeGotoAnythingCommand._hx_methods = ["getEntries","toEntry","getData","getFile","getSrcPos"]
hxsublime_commands_HaxeGotoAnythingCommand._hx_statics = []
hxsublime_commands_HaxeGotoAnythingCommand._hx_interfaces = []
hxsublime_commands_HaxeGotoAnythingCommand._hx_super = hxsublime_commands_HaxeGotoBaseCommand

# print hxsublime.commands.GotoBase.State
class hxsublime_commands_GotoBase_State:

	pass




hxsublime_commands_GotoBase_State._find_decl_file = None
hxsublime_commands_GotoBase_State._find_decl_pos = None
hxsublime_commands_GotoBase_State._init_text = ""
hxsublime_commands_GotoBase_State._is_open = False


hxsublime_commands_GotoBase_State._hx_class = hxsublime_commands_GotoBase_State
hxsublime_commands_GotoBase_State._hx_class_name = "hxsublime.commands._GotoBase._GotoBase.State"
_hx_classes['hxsublime.commands._GotoBase._GotoBase.State'] = hxsublime_commands_GotoBase_State
hxsublime_commands_GotoBase_State._hx_fields = []
hxsublime_commands_GotoBase_State._hx_props = []
hxsublime_commands_GotoBase_State._hx_methods = []
hxsublime_commands_GotoBase_State._hx_statics = ["_find_decl_file","_find_decl_pos","_init_text","_is_open"]
hxsublime_commands_GotoBase_State._hx_interfaces = []

# print hxsublime.commands.GotoBase.HaxeGotoBaseListener
class hxsublime_commands_HaxeGotoBaseListener(sublime_EventListener):

	def on_activated(self,view):
		find_pos = hxsublime_commands_GotoBase_State._find_decl_pos
		find_file = hxsublime_commands_GotoBase_State._find_decl_file
		haxe_Log.trace("HaxeGotoBaseListener::on_activated", _Hx_AnonObject(fileName = "GotoBase.hx" ,lineNumber = 173 ,className = "hxsublime.commands.HaxeGotoBaseListener" ,methodName = "on_activated" ))
		haxe_Log.trace(Std.string(view), _Hx_AnonObject(fileName = "GotoBase.hx" ,lineNumber = 176 ,className = "hxsublime.commands.HaxeGotoBaseListener" ,methodName = "on_activated" ))
		if view is not None and hxsublime_commands_GotoBase_State._is_open:
			hxsublime_commands_GotoBase_State._is_open = False
			hxsublime_tools_ViewTools.insertAtCursor(view, hxsublime_commands_GotoBase_State._init_text)
			hxsublime_commands_GotoBase_State._init_text = ""
		
		
		if view is not None and view.file_name() is not None:
			if view.file_name() == find_file:
				view.sel().clear()
				min = find_pos
				view.sel().add(sublime_Region(min))
				haxe_Log.trace("show at:" + Std.string(min), _Hx_AnonObject(fileName = "GotoBase.hx" ,lineNumber = 200 ,className = "hxsublime.commands.HaxeGotoBaseListener" ,methodName = "on_activated" ))
				def _hx_local_0():
					haxe_Log.trace("show at:" + Std.string(min), _Hx_AnonObject(fileName = "GotoBase.hx" ,lineNumber = 205 ,className = "hxsublime.commands.HaxeGotoBaseListener" ,methodName = "on_activated" ))
					view.show_at_center(sublime_Region(min))
				
				show = _hx_local_0
				sublime_Sublime.set_timeout(show, 100)
				hxsublime_commands_GotoBase_State._find_decl_file = None
				hxsublime_commands_GotoBase_State._find_decl_pos = None
		
			
		
	







hxsublime_commands_HaxeGotoBaseListener._hx_class = hxsublime_commands_HaxeGotoBaseListener
hxsublime_commands_HaxeGotoBaseListener._hx_class_name = "hxsublime.commands.HaxeGotoBaseListener"
_hx_classes['hxsublime.commands.HaxeGotoBaseListener'] = hxsublime_commands_HaxeGotoBaseListener
hxsublime_commands_HaxeGotoBaseListener._hx_fields = []
hxsublime_commands_HaxeGotoBaseListener._hx_props = []
hxsublime_commands_HaxeGotoBaseListener._hx_methods = ["on_activated"]
hxsublime_commands_HaxeGotoBaseListener._hx_statics = []
hxsublime_commands_HaxeGotoBaseListener._hx_interfaces = []
hxsublime_commands_HaxeGotoBaseListener._hx_super = sublime_EventListener

# print hxsublime.commands.GotoBuildFields.HaxeGotoBuildFieldsCommand
class hxsublime_commands_HaxeGotoBuildFieldsCommand(hxsublime_commands_HaxeGotoBaseCommand):


	def __init__(self,v):
		super().__init__(v)
	def getEntries(self,types):
		_g = []
		_it = types.keys()
		while _it.hasNext():
			k = _it.next()
			_g1 = 0
			_g2 = types.get(k).allFieldsList()
			while _g1 < len(_g2):
				p = _g2[_g1]
				_g1 = _g1 + 1
				x = [p.toString() + " - " + p.kind, p.type._file]
				_g.append(x)
				__builtin__.len(_g)
				
			
		
		return _g
	

	def getData(self,types):
		_g = []
		_it = types.keys()
		while _it.hasNext():
			k = _it.next()
			_g1 = 0
			_g2 = types.get(k).allFieldsList()
			while _g1 < len(_g2):
				p = _g2[_g1]
				_g1 = _g1 + 1
				x = (k + "." + p.name, p)
				_g.append(x)
				__builtin__.len(_g)
				
			
		
		return _g
	

	def getFile(self,data_entry):
		return data_entry.type._file

	def getSrcPos(self,data_entry):
		return data_entry.srcPos()







hxsublime_commands_HaxeGotoBuildFieldsCommand._hx_class = hxsublime_commands_HaxeGotoBuildFieldsCommand
hxsublime_commands_HaxeGotoBuildFieldsCommand._hx_class_name = "hxsublime.commands.HaxeGotoBuildFieldsCommand"
_hx_classes['hxsublime.commands.HaxeGotoBuildFieldsCommand'] = hxsublime_commands_HaxeGotoBuildFieldsCommand
hxsublime_commands_HaxeGotoBuildFieldsCommand._hx_fields = []
hxsublime_commands_HaxeGotoBuildFieldsCommand._hx_props = []
hxsublime_commands_HaxeGotoBuildFieldsCommand._hx_methods = ["getEntries","getData","getFile","getSrcPos"]
hxsublime_commands_HaxeGotoBuildFieldsCommand._hx_statics = []
hxsublime_commands_HaxeGotoBuildFieldsCommand._hx_interfaces = []
hxsublime_commands_HaxeGotoBuildFieldsCommand._hx_super = hxsublime_commands_HaxeGotoBaseCommand

# print hxsublime.commands.GotoBuildTypes.HaxeGotoBuildTypesCommand
class hxsublime_commands_HaxeGotoBuildTypesCommand(hxsublime_commands_HaxeGotoBaseCommand):


	def __init__(self,v):
		super().__init__(v)
	def getEntries(self,types):
		_g = []
		_it = types.keys()
		while _it.hasNext():
			k = _it.next()
			def _hx_local_0():
				_this = types.get(k)
				return _this._file
			
			x = [k, _hx_local_0()]
			_g.append(x)
			__builtin__.len(_g)
			
		
		return _g
	

	def getData(self,types):
		_g = []
		_it = types.keys()
		while _it.hasNext():
			k = _it.next()
			x = None
			b = types.get(k)
			x = (k, b)
			
			_g.append(x)
			__builtin__.len(_g)
			
		
		return _g
	

	def getFile(self,dataEntry):
		return dataEntry._file

	def getSrcPos(self,dataEntry):
		return dataEntry.srcPos()







hxsublime_commands_HaxeGotoBuildTypesCommand._hx_class = hxsublime_commands_HaxeGotoBuildTypesCommand
hxsublime_commands_HaxeGotoBuildTypesCommand._hx_class_name = "hxsublime.commands.HaxeGotoBuildTypesCommand"
_hx_classes['hxsublime.commands.HaxeGotoBuildTypesCommand'] = hxsublime_commands_HaxeGotoBuildTypesCommand
hxsublime_commands_HaxeGotoBuildTypesCommand._hx_fields = []
hxsublime_commands_HaxeGotoBuildTypesCommand._hx_props = []
hxsublime_commands_HaxeGotoBuildTypesCommand._hx_methods = ["getEntries","getData","getFile","getSrcPos"]
hxsublime_commands_HaxeGotoBuildTypesCommand._hx_statics = []
hxsublime_commands_HaxeGotoBuildTypesCommand._hx_interfaces = []
hxsublime_commands_HaxeGotoBuildTypesCommand._hx_super = hxsublime_commands_HaxeGotoBaseCommand

# print hxsublime.commands.Haxelib.HaxeInstallLibCommand
class hxsublime_commands_HaxeInstallLibCommand(sublime_WindowCommand):


	def __init__(self,w):
		super().__init__(w)
	def run(self,**_):
		view = sublime_Sublime.active_window().active_view()
		project = hxsublime_project_Projects.currentProject(view)
		if project is not None:
			manager = project.haxelibManager()
			libs = manager.searchLibs()
			menu = self.createMenuItems(libs, manager)
			def _hx_local_0():
				f = self.onEntrySelected
				a1 = libs
				a2 = manager
				def _hx_local_1(i):
					return f(a1, a2, i)
				return _hx_local_1
			
			self.window.show_quick_panel(menu, _hx_local_0())
		
		
	

	def createMenuItems(self,libs,manager):
		menu = []
		_g = 0
		while _g < len(libs):
			l = libs[_g]
			_g = _g + 1
			if manager.isLibInstalled(l):
				menu.append([l + " [" + manager.getLib(l).version + "]", "Remove"])
				__builtin__.len(menu)
			
			else:
				menu.append([l, "Install"])
				__builtin__.len(menu)
			
		
		
		menu.append(["Upgrade libraries", "Upgrade installed libraries"])
		__builtin__.len(menu)
		
		menu.append(["Haxelib Selfupdate", "Updates Haxelib itself"])
		__builtin__.len(menu)
		
		return menu
	

	def onEntrySelected(self,libs,manager,i):
		haxe_Log.trace("install lib command selected " + Std.string(i), _Hx_AnonObject(fileName = "Haxelib.hx" ,lineNumber = 56 ,className = "hxsublime.commands.HaxeInstallLibCommand" ,methodName = "onEntrySelected" ))
		if i < 0:
			return
		
		if i == __builtin__.len(libs):
			haxe_Log.trace("upgrade all", _Hx_AnonObject(fileName = "Haxelib.hx" ,lineNumber = 62 ,className = "hxsublime.commands.HaxeInstallLibCommand" ,methodName = "onEntrySelected" ))
			manager.upgradeAll()
		
		
		if i == __builtin__.len(libs) + 1:
			haxe_Log.trace("self update", _Hx_AnonObject(fileName = "Haxelib.hx" ,lineNumber = 68 ,className = "hxsublime.commands.HaxeInstallLibCommand" ,methodName = "onEntrySelected" ))
			manager.selfUpdate()
		
		else:
			lib = libs[i]
			if manager.available().exists(lib):
				haxe_Log.trace("remove " + lib, _Hx_AnonObject(fileName = "Haxelib.hx" ,lineNumber = 76 ,className = "hxsublime.commands.HaxeInstallLibCommand" ,methodName = "onEntrySelected" ))
				manager.removeLib(lib)
			
			else:
				haxe_Log.trace("install " + lib, _Hx_AnonObject(fileName = "Haxelib.hx" ,lineNumber = 81 ,className = "hxsublime.commands.HaxeInstallLibCommand" ,methodName = "onEntrySelected" ))
				manager.installLib(lib)
			
		
	







hxsublime_commands_HaxeInstallLibCommand._hx_class = hxsublime_commands_HaxeInstallLibCommand
hxsublime_commands_HaxeInstallLibCommand._hx_class_name = "hxsublime.commands.HaxeInstallLibCommand"
_hx_classes['hxsublime.commands.HaxeInstallLibCommand'] = hxsublime_commands_HaxeInstallLibCommand
hxsublime_commands_HaxeInstallLibCommand._hx_fields = []
hxsublime_commands_HaxeInstallLibCommand._hx_props = []
hxsublime_commands_HaxeInstallLibCommand._hx_methods = ["run","createMenuItems","onEntrySelected"]
hxsublime_commands_HaxeInstallLibCommand._hx_statics = []
hxsublime_commands_HaxeInstallLibCommand._hx_interfaces = []
hxsublime_commands_HaxeInstallLibCommand._hx_super = sublime_WindowCommand

# print hxsublime.commands.ShowDoc.HaxeShowDocCommand
class hxsublime_commands_HaxeShowDocCommand(hxsublime_commands_HaxeFindDeclarationCommand):


	def __init__(self,v):
		super().__init__(v)
	def helperMethod(self):
		return "hxsublime.FindDeclaration.__sublimeShowDoc"

	def handleSuccessfulResult(self,view,json_res,using_insert,insert_before,insert_after,expr_end,build,temp_path,temp_file):
		doc = None
		if python_lib_DictImpl.hasKey(json_res, "doc"):
			doc = json_res.get("doc", None)
		else:
			doc = "No documentation found"
		haxe_Log.trace("json: " + Std.string(json_res), _Hx_AnonObject(fileName = "ShowDoc.hx" ,lineNumber = 27 ,className = "hxsublime.commands.HaxeShowDocCommand" ,methodName = "handleSuccessfulResult" ))
		haxe_Log.trace("doc: " + Std.string(doc), _Hx_AnonObject(fileName = "ShowDoc.hx" ,lineNumber = 28 ,className = "hxsublime.commands.HaxeShowDocCommand" ,methodName = "handleSuccessfulResult" ))
		hxsublime_panel_Panels.slidePanel().writeln(doc, None, False)
	







hxsublime_commands_HaxeShowDocCommand._hx_class = hxsublime_commands_HaxeShowDocCommand
hxsublime_commands_HaxeShowDocCommand._hx_class_name = "hxsublime.commands.HaxeShowDocCommand"
_hx_classes['hxsublime.commands.HaxeShowDocCommand'] = hxsublime_commands_HaxeShowDocCommand
hxsublime_commands_HaxeShowDocCommand._hx_fields = []
hxsublime_commands_HaxeShowDocCommand._hx_props = []
hxsublime_commands_HaxeShowDocCommand._hx_methods = ["helperMethod","handleSuccessfulResult"]
hxsublime_commands_HaxeShowDocCommand._hx_statics = []
hxsublime_commands_HaxeShowDocCommand._hx_interfaces = []
hxsublime_commands_HaxeShowDocCommand._hx_super = hxsublime_commands_HaxeFindDeclarationCommand

# print hxsublime.compiler.Output.CompletionEntry
class hxsublime_compiler_CompletionEntry:


	def __init__(self,hint,insert,doc):
		self.hint = hint
		self.insert = insert
		self.doc = doc
	
	# var hint
	# var insert
	# var doc






hxsublime_compiler_CompletionEntry._hx_class = hxsublime_compiler_CompletionEntry
hxsublime_compiler_CompletionEntry._hx_class_name = "hxsublime.compiler.CompletionEntry"
_hx_classes['hxsublime.compiler.CompletionEntry'] = hxsublime_compiler_CompletionEntry
hxsublime_compiler_CompletionEntry._hx_fields = ["hint","insert","doc"]
hxsublime_compiler_CompletionEntry._hx_props = []
hxsublime_compiler_CompletionEntry._hx_methods = []
hxsublime_compiler_CompletionEntry._hx_statics = []
hxsublime_compiler_CompletionEntry._hx_interfaces = []

# print hxsublime.compiler.Output.Output
class hxsublime_compiler_Output:

	pass




hxsublime_compiler_Output.compiler_output = python_lib_Re.compile("^([^:]+):([0-9]+): (?:character(?:s?)|line(?:s?))? ([0-9]+)-?([0-9]+)? : (.*)", python_lib_Re.M)
hxsublime_compiler_Output.no_classes_found = python_lib_Re.compile("^No classes found in .*", python_lib_Re.M)
hxsublime_compiler_Output.no_classes_found_in_trace = python_lib_Re.compile("^No classes found in trace$", python_lib_Re.M)
hxsublime_compiler_Output.haxe_compiler_line = "^([^:]*):([0-9]+): characters? ([0-9]+)-?[0-9]* :(.*)$"
hxsublime_compiler_Output.type_parameter_name = python_lib_Re.compile("^([A-Z][_a-zA-Z0-9]*)")
def Output_statics_get_type_hint(types):
	hints = []
	for i in types:
		hint = i.text.strip(None)
		hint_types = hxsublime_tools_HxSrcTools.splitFunctionSignature(hint)
		hints.append(hint_types)
		__builtin__.len(hints)
		
	
	return hints
	
hxsublime_compiler_Output.get_type_hint = Output_statics_get_type_hint
def Output_statics_get_function_type_params(name,signature_types):
	new_args = []
	type_params = haxe_ds_StringMap()
	name_len = __builtin__.len(name)
	_g = 0
	while _g < len(signature_types):
		t = signature_types[_g]
		_g = _g + 1
		x = None
		_this = t.split(name + ".")
		x = "".join(_this)
		
		new_args.append(x)
		__builtin__.len(new_args)
		
		
		while True:
			index = t.find(name)
			if index == -1:
				break
			
			type_start_index = index + name_len + 1
			t = python_Tools.substr(t, type_start_index, None)
			m = hxsublime_compiler_Output.type_parameter_name.match(t)
			if m is not None:
				param_name = m.group(1)
				type_params.set(param_name, True)
			
			else:
				break
		
	
	
	keys = None
	_g = []
	_it = type_params.keys()
	while _it.hasNext():
		k = _it.next()
		_g.append(k)
		__builtin__.len(_g)
	
	keys = _g
	
	keys.reverse()
	type_param_list = keys
	return (new_args, type_param_list)
	
hxsublime_compiler_Output.get_function_type_params = Output_statics_get_function_type_params
def Output_statics_completion_field_to_entry(name,sig,doc):
	insert = name
	label = name
	smart_snippets = hxsublime_Settings.smartSnippetsOnCompletion()
	not_smart = not smart_snippets
	if sig is not None:
		types = hxsublime_tools_HxSrcTools.splitFunctionSignature(sig)
		r = hxsublime_compiler_Output.get_function_type_params(name, types)
		types1 = r[0]
		type_params = r[1]
		params_sig = ""
		if __builtin__.len(type_params) > 0:
			params_sig = "<" + ", ".join(type_params) + ">"
		
		ret = None
		if __builtin__.len(types1) == 0:
			ret = None
		else:
			ret = types1.pop()
		signature_separator = " : "
		if __builtin__.len(types1) > 0:
			if __builtin__.len(types1) == 1 and types1[0] == "Void":
				if not_smart:
					label = name + params_sig + "()" + signature_separator + Std.string(ret)
				else:
					label = name + "()" + signature_separator + Std.string(ret)
				if not_smart:
					insert = name
				else:
					insert = "" + name + "${1:()}"
		
			else:
				def _hx_local_0(x):
					return StringTools.replace(StringTools.replace(x, "}", "\\}"), "{", "\\{")
				escape_type = _hx_local_0
				params = "( " + ", ".join(types1) + " )"
				label = name + params_sig + params + signature_separator + Std.string(ret)
				new_types = __builtin__.list(types1)
				_g1 = 0
				_g = __builtin__.len(new_types)
				while _g1 < _g:
					def _hx_local_2():
						nonlocal _g1
						_hx_local_1 = _g1
						_g1 = _g1 + 1
						return _hx_local_1
						
					
					i = _hx_local_2()
					new_types[i] = "${" + Std.string(i + 2) + ":" + escape_type(new_types[i]) + "}"
				
				
				if not_smart:
					insert = name
				else:
					insert = name + "${1:( " + ", ".join(new_types) + " )}"
		
		else:
			label = name + params_sig + signature_separator + Std.string(ret)
	
	elif python_lib_Re.match("^[A-Z]", name) is not None:
		label = name + "\tclass"
	else:
		label = name + "\tpackage"
	res = hxsublime_compiler_CompletionEntry(label, insert, doc)
	return res
	
hxsublime_compiler_Output.completion_field_to_entry = Output_statics_completion_field_to_entry
def Output_statics_collect_completion_fields(li):
	comps = []
	if li is not None:
		for i in li.iter("i"):
			name = i.get("n")
			sig = i.find("t").text
			doc = i.find("d").text
			entry = hxsublime_compiler_Output.completion_field_to_entry(name, sig, doc)
			comps.append(entry)
			__builtin__.len(comps)
			
	
	
	return comps
	
hxsublime_compiler_Output.collect_completion_fields = Output_statics_collect_completion_fields
def Output_statics_extract_errors(str):
	errors = []
	def _hx_local_0():
		_this = python_lib_Re_RegexHelper.findallDynamic(hxsublime_compiler_Output.no_classes_found, str, None, None)
		return __builtin__.len(_this)
	
	if _hx_local_0() > 0:
		errors = []
	else:
		_g = 0
		_g1 = None
		_this = python_lib_Re_RegexHelper.findallDynamic(hxsublime_compiler_Output.compiler_output, str, None, None)
		def _hx_local_1(t):
			return __builtin__.list(t)
		_g1 = __builtin__.list(__builtin__.map(_hx_local_1, _this))
		
		while _g < len(_g1):
			infos = _g1[_g]
			_g = _g + 1
			f = infos.pop(0)
			l = None
			def _hx_local_2():
				x = infos.pop(0)
				def _hx_local_4():
					def _hx_local_3():
						x1 = float(x)
						return int(x1)
					
					return _hx_local_3()
				
				return _hx_local_4()
			
			l = _hx_local_2() - 1
			left = None
			x = infos.pop(0)
			x1 = float(x)
			left = int(x1)
			
			
			right = infos.pop(0)
			rightInt = 0
			if right != "":
				x = float(right)
				rightInt = int(x)
			
			else:
				rightInt = left + 1
			m = infos.pop(0)
			if m != "Unexpected |":
				errors.append(_Hx_AnonObject(file = f ,line = l ,_hx_from = left ,to = rightInt ,message = m ))
				__builtin__.len(errors)
			
			
		
	
	if __builtin__.len(errors) > 0:
		hxsublime_panel_Panels.slidePanel().writeln(errors[0].message)
		sublime_Sublime.status_message(errors[0].message)
	
	
	return errors
	
hxsublime_compiler_Output.extract_errors = Output_statics_extract_errors
def Output_statics_getCompletionOutput(temp_file,orig_file,output,commas):
	r = hxsublime_compiler_Output.parse_completion_output(temp_file, orig_file, output)
	hints = r[0]
	comps = r[1]
	new_hints = []
	_g = 0
	while _g < len(hints):
		h = hints[_g]
		_g = _g + 1
		if __builtin__.len(h) > commas:
			x = h[commas:None]
			new_hints.append(x)
			__builtin__.len(new_hints)
			
		
		
	
	
	hints = new_hints
	r1 = hxsublime_compiler_Output.get_completion_status_and_errors(hints, comps, output, temp_file, orig_file)
	status = None
	errors = None
	if r1 is not None:
		status = r1[0]
		errors = r1[1]
	
	
	return (hints, comps, status, errors)
	
hxsublime_compiler_Output.getCompletionOutput = Output_statics_getCompletionOutput
def Output_statics_parse_completion_output(temp_file,orig_file,output):
	tree = None
	try:
		x = "<root>" + output + "</root>"
		tree = python_lib_xml_etree_ElementTree.XML(x)
	
	except Exception as _hx_e:
		_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
		if isinstance(_hx_e1, Exception):
			e = _hx_e1
			haxe_Log.trace("invalid xml - error: " + Std.string(e), _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 311 ,className = "hxsublime.compiler.Output" ,methodName = "parse_completion_output" ))
		else:
			raise _hx_e
	hints = None
	comps = None
	if tree is not None:
		hints = hxsublime_compiler_Output.get_type_hint(tree.iter("type"))
		comps = hxsublime_compiler_Output.collect_completion_fields(tree.find("list"))
	
	else:
		hints = []
		comps = []
	
	def _hx_local_0():
		_this = hxsublime_compiler_Output.no_classes_found_in_trace.findall(output, 0)
		return __builtin__.len(_this)
	
	if _hx_local_0() > 0:
		smart_snippets = hxsublime_Settings.smartSnippetsOnCompletion()
		insert = None
		if smart_snippets:
			insert = "${1:value:Dynamic}"
		else:
			insert = "${0}"
		x = hxsublime_compiler_CompletionEntry("value:Dynamic", insert, "")
		comps.append(x)
		__builtin__.len(comps)
		
		
	
	
	return (hints, comps)
	
hxsublime_compiler_Output.parse_completion_output = Output_statics_parse_completion_output
def Output_statics_get_completion_status_and_errors(hints,comps,output,temp_file,orig_file):
	status = ""
	errors = []
	res = None
	if __builtin__.len(hints) == 0 and __builtin__.len(comps) == 0:
		res = hxsublime_compiler_Output.parse_completion_errors(output, temp_file, orig_file, status)
	else:
		res = ("", [])
	return res
	
hxsublime_compiler_Output.get_completion_status_and_errors = Output_statics_get_completion_status_and_errors
def Output_statics_parse_completion_errors(output,temp_file,orig_file,status):
	haxe_Log.trace("output:" + output, _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 371 ,className = "hxsublime.compiler.Output" ,methodName = "parse_completion_errors" ))
	haxe_Log.trace("status:" + status, _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 372 ,className = "hxsublime.compiler.Output" ,methodName = "parse_completion_errors" ))
	haxe_Log.trace("orig_file:" + orig_file, _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 373 ,className = "hxsublime.compiler.Output" ,methodName = "parse_completion_errors" ))
	haxe_Log.trace("temp_file:" + temp_file, _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 374 ,className = "hxsublime.compiler.Output" ,methodName = "parse_completion_errors" ))
	sep = python_lib_Os.sep
	haxe_Log.trace("sep: " + sep, _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 379 ,className = "hxsublime.compiler.Output" ,methodName = "parse_completion_errors" ))
	if sep == "\\":
		def _hx_local_0(match_obj):
			haxe_Log.trace("matched", _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 382 ,className = "hxsublime.compiler.Output" ,methodName = "parse_completion_errors" ))
			_this = match_obj.group(0).split("/")
			return sep.join(_this)
			
		
		slash_replace = _hx_local_0
		output = python_lib_Re.sub("[A-Za-z]:(.*)[.]hx", slash_replace, output)
	
	
	output = StringTools.replace(output, temp_file, orig_file)
	haxe_Log.trace("output after replace: " + output, _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 391 ,className = "hxsublime.compiler.Output" ,methodName = "parse_completion_errors" ))
	output = python_lib_Re.sub("\\(display(.*)\\)", "", output)
	lines = output.split("\n")
	l = lines[0].strip(None)
	status1 = None
	if __builtin__.len(l) > 0:
		if l == "<list>":
			status1 = "No autocompletion available"
		elif python_lib_Re.match(hxsublime_compiler_Output.haxe_compiler_line, l) is None:
			status1 = l
			haxe_Log.trace(l, _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 406 ,className = "hxsublime.compiler.Output" ,methodName = "parse_completion_errors" ))
	
		else:
			status1 = ""
	
	errors = hxsublime_compiler_Output.extract_errors(output)
	return (status1, errors)
	
hxsublime_compiler_Output.parse_completion_errors = Output_statics_parse_completion_errors


hxsublime_compiler_Output._hx_class = hxsublime_compiler_Output
hxsublime_compiler_Output._hx_class_name = "hxsublime.compiler.Output"
_hx_classes['hxsublime.compiler.Output'] = hxsublime_compiler_Output
hxsublime_compiler_Output._hx_fields = []
hxsublime_compiler_Output._hx_props = []
hxsublime_compiler_Output._hx_methods = []
hxsublime_compiler_Output._hx_statics = ["compiler_output","no_classes_found","no_classes_found_in_trace","haxe_compiler_line","type_parameter_name","get_type_hint","get_function_type_params","completion_field_to_entry","collect_completion_fields","extract_errors","getCompletionOutput","parse_completion_output","get_completion_status_and_errors","parse_completion_errors"]
hxsublime_compiler_Output._hx_interfaces = []

# print hxsublime.compiler.Server.Server
class hxsublime_compiler_Server:


	def __init__(self,port):
		self._use_wrapper = hxsublime_Settings.useHaxeServermodeWrapper()
		self._server_proc = None
		self._server_port = port
		self._orig_server_port = port
	
	# var _use_wrapper
	# var _server_proc
	# var _server_port
	# var _orig_server_port
	def get_server_port(self):
		return self._server_port

	def start(self,haxe_path,cwd = None,env = None,retries = 10):
		if cwd is None:
			cwd = None
		
		if env is None:
			env = None
		
		if retries is None:
			retries = 10
		
		_g = self
		if self._server_proc is None:
			cmd = None
			if self._use_wrapper:
				wrapper = hxsublime_Plugin.plugin_base_dir() + "/wrapper"
				cmd = ["neko", wrapper]
			
			else:
				cmd = []
			x = [haxe_path, "--wait", Std.string(self._server_port)]
			cmd.extend(x)
			
			haxe_Log.trace("start server:", _Hx_AnonObject(fileName = "Server.hx" ,lineNumber = 55 ,className = "hxsublime.compiler.Server" ,methodName = "start" ))
			haxe_Log.trace(" ".join(cmd), _Hx_AnonObject(fileName = "Server.hx" ,lineNumber = 57 ,className = "hxsublime.compiler.Server" ,methodName = "start" ))
			def _hx_local_0(e):
				err = "Error starting server " + " ".join(cmd) + ": " + Std.string(e)
				sublime_Sublime.error_message(err)
				if retries > 0:
					_g.stop()
					_g._server_port = _g._server_port + 1
					haxe_Log.trace("retry starting server at port: " + Std.string(_g._server_port), _Hx_AnonObject(fileName = "Server.hx" ,lineNumber = 66 ,className = "hxsublime.compiler.Server" ,methodName = "start" ))
					_g.start(haxe_path, cwd, env, retries - 1)
				
				else:
					msg = "Cannot start haxe compilation server on ports {0}-{1}"
					msg = python_lib_StringTools.format(msg, [_g._orig_server_port, _g._server_port])
					haxe_Log.trace("Server starting error", _Hx_AnonObject(fileName = "Server.hx" ,lineNumber = 73 ,className = "hxsublime.compiler.Server" ,methodName = "start" ))
				
			
			onError = _hx_local_0
			try:
				full_env = python_lib_Os.environ.copy()
				if env is not None:
					full_env.update(env)
				
				if env is not None:
					def _hx_local_1():
						p = None
						_this = env.keys()
						p = __builtin__.iter(_this)
						
						return python_HaxeIterator(p)
					
					_it = _hx_local_1()
					while _it.hasNext():
						k = _it.next()
						val = None
						try:
							val = env.get(k, None)
						except Exception as _hx_e:
							_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
							if True:
								e = _hx_e1
								val = env.get(k, None)
							else:
								raise _hx_e
						val1 = python_lib_os_Path.expandvars(val)
						python_lib_DictImpl.set(full_env, k, val1)
						
					
				
				
				haxe_Log.trace("server env:" + Std.string(full_env), _Hx_AnonObject(fileName = "Server.hx" ,lineNumber = 106 ,className = "hxsublime.compiler.Server" ,methodName = "start" ))
				o = _Hx_AnonObject(cwd = cwd ,env = full_env ,stdin = python_lib_Subprocess.PIPE ,stdout = python_lib_Subprocess.PIPE ,startupinfo = hxsublime_Plugin.startupInfo() )
				if Reflect.hasField(o, "bufsize"):
					o.bufsize = o.bufsize
				else:
					o.bufsize = 0
				if Reflect.hasField(o, "executable"):
					o.executable = o.executable
				else:
					o.executable = None
				if Reflect.hasField(o, "stdin"):
					o.stdin = o.stdin
				else:
					o.stdin = None
				if Reflect.hasField(o, "stdout"):
					o.stdout = o.stdout
				else:
					o.stdout = None
				if Reflect.hasField(o, "stderr"):
					o.stderr = o.stderr
				else:
					o.stderr = None
				if Reflect.hasField(o, "preexec_fn"):
					o.preexec_fn = o.preexec_fn
				else:
					o.preexec_fn = None
				if Reflect.hasField(o, "close_fds"):
					o.close_fds = o.close_fds
				else:
					o.close_fds = None
				if Reflect.hasField(o, "shell"):
					o.shell = o.shell
				else:
					o.shell = None
				if Reflect.hasField(o, "cwd"):
					o.cwd = o.cwd
				else:
					o.cwd = None
				if Reflect.hasField(o, "env"):
					o.env = o.env
				else:
					o.env = None
				if Reflect.hasField(o, "universal_newlines"):
					o.universal_newlines = o.universal_newlines
				else:
					o.universal_newlines = None
				if Reflect.hasField(o, "startupinfo"):
					o.startupinfo = o.startupinfo
				else:
					o.startupinfo = None
				if Reflect.hasField(o, "creationflags"):
					o.creationflags = o.creationflags
				else:
					o.creationflags = 0
				self._server_proc = python_lib_subprocess_Popen(cmd, o.bufsize, o.executable, o.stdin, o.stdout, o.stderr, o.preexec_fn, o.close_fds, o.shell, o.cwd, o.env, o.universal_newlines, o.startupinfo, o.creationflags)
				
				self._server_proc.poll()
				python_lib_Time.sleep(0.05)
				haxe_Log.trace("server started at port: " + Std.string(self._server_port), _Hx_AnonObject(fileName = "Server.hx" ,lineNumber = 113 ,className = "hxsublime.compiler.Server" ,methodName = "start" ))
			
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				if isinstance(_hx_e1, OSError):
					e = _hx_e1
					onError(e)
				elif isinstance(_hx_e1, ValueError):
					e = _hx_e1
					onError(e)
				if True:
					e = _hx_e1
					haxe_Log.trace("ERROR : " + Std.string(e), _Hx_AnonObject(fileName = "Server.hx" ,lineNumber = 126 ,className = "hxsublime.compiler.Server" ,methodName = "start" ))
				else:
					raise _hx_e
		
		
	

	def stop(self,completeCallback = None):
		if completeCallback is None:
			completeCallback = None
		
		old_port = self._server_port
		try:
			proc = self._server_proc
			if proc is not None:
				self._server_proc = None
				if self._use_wrapper:
					proc.stdin.write("x")
					python_lib_Time.sleep(0.2)
				
				else:
					proc.terminate()
					python_lib_Time.sleep(0.2)
				
				proc.kill()
				proc.wait()
				proc = None
				self._server_port = self._server_port + 1
			
			
		
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			if True:
				e = _hx_e1
				self._server_proc = None
				self._server_port = self._server_port + 1
		
			else:
				raise _hx_e
		if completeCallback is not None:
			hxsublime_panel_Panels.defaultPanel().writeln("stopping server on port: " + Std.string(old_port))
			completeCallback()
		
		
	

	def __del__(self):
		self.stop()







hxsublime_compiler_Server._hx_class = hxsublime_compiler_Server
hxsublime_compiler_Server._hx_class_name = "hxsublime.compiler.Server"
_hx_classes['hxsublime.compiler.Server'] = hxsublime_compiler_Server
hxsublime_compiler_Server._hx_fields = ["_use_wrapper","_server_proc","_server_port","_orig_server_port"]
hxsublime_compiler_Server._hx_props = []
hxsublime_compiler_Server._hx_methods = ["get_server_port","start","stop","__del__"]
hxsublime_compiler_Server._hx_statics = []
hxsublime_compiler_Server._hx_interfaces = []

# print hxsublime.completion.Completion.CompletionListener
class hxsublime_completion_CompletionListener(sublime_EventListener):

	def on_query_completions(self,view,prefix,locations):
		project = hxsublime_project_Projects.currentProject(view)
		return hxsublime_completion_Completion.dispatchAutoComplete(project, view, prefix, locations[0])
	







hxsublime_completion_CompletionListener._hx_class = hxsublime_completion_CompletionListener
hxsublime_completion_CompletionListener._hx_class_name = "hxsublime.completion.CompletionListener"
_hx_classes['hxsublime.completion.CompletionListener'] = hxsublime_completion_CompletionListener
hxsublime_completion_CompletionListener._hx_fields = []
hxsublime_completion_CompletionListener._hx_props = []
hxsublime_completion_CompletionListener._hx_methods = ["on_query_completions"]
hxsublime_completion_CompletionListener._hx_statics = []
hxsublime_completion_CompletionListener._hx_interfaces = []
hxsublime_completion_CompletionListener._hx_super = sublime_EventListener

# print hxsublime.completion.Completion.Completion
class hxsublime_completion_Completion:

	pass




def Completion_statics_getCompletionScopes(view,location):
	return hxsublime_tools_ViewTools.getScopesAt(view, location)
hxsublime_completion_Completion.getCompletionScopes = Completion_statics_getCompletionScopes
def Completion_statics_getCompletionOffset(location,prefix):
	return location - __builtin__.len(prefix)
hxsublime_completion_Completion.getCompletionOffset = Completion_statics_getCompletionOffset
def Completion_statics_canRunCompletion(offset,scopes):
	if offset == 0:
		return False
	else:
		return hxsublime_completion_Completion.isSupportedScope(scopes)
hxsublime_completion_Completion.canRunCompletion = Completion_statics_canRunCompletion
def Completion_statics_isSupportedScope(scopes):
	return not hxsublime_tools_ScopeTools.containsStringOrComment(scopes)
hxsublime_completion_Completion.isSupportedScope = Completion_statics_isSupportedScope
def Completion_statics_emptyHandler(project,view,offset,prefix):
	return []
hxsublime_completion_Completion.emptyHandler = Completion_statics_emptyHandler
def Completion_statics_getAutoCompleteHandler(view,scopes):
	handler = None
	if Lambda.has(scopes, hxsublime_Config.SOURCE_HXML):
		handler = hxsublime_completion_hxml_HxmlCompletion.autoComplete
	elif Lambda.has(scopes, hxsublime_Config.SOURCE_HAXE):
		if hxsublime_tools_ViewTools.isHxsl(view):
			handler = hxsublime_completion_hxsl_HxslCompletion.autoComplete
		else:
			handler = hxsublime_completion_hx_HxCompletion.autoComplete
	else:
		handler = hxsublime_completion_Completion.emptyHandler
	return handler
	
hxsublime_completion_Completion.getAutoCompleteHandler = Completion_statics_getAutoCompleteHandler
def Completion_statics_dispatchAutoComplete(project,view,prefix,location):
	startTime = python_lib_Time.time()
	offset = hxsublime_completion_Completion.getCompletionOffset(location, prefix)
	scopes = hxsublime_completion_Completion.getCompletionScopes(view, location)
	comps = None
	haxe_Log.trace("pre handler", _Hx_AnonObject(fileName = "Completion.hx" ,lineNumber = 86 ,className = "hxsublime.completion.Completion" ,methodName = "dispatchAutoComplete" ))
	if hxsublime_completion_Completion.canRunCompletion(offset, scopes):
		haxe_Log.trace("run handler", _Hx_AnonObject(fileName = "Completion.hx" ,lineNumber = 88 ,className = "hxsublime.completion.Completion" ,methodName = "dispatchAutoComplete" ))
		handler = hxsublime_completion_Completion.getAutoCompleteHandler(view, scopes)
		comps = handler(project, view, offset, prefix)
	
	else:
		haxe_Log.trace("no handler", _Hx_AnonObject(fileName = "Completion.hx" ,lineNumber = 93 ,className = "hxsublime.completion.Completion" ,methodName = "dispatchAutoComplete" ))
		comps = []
	
	haxe_Log.trace("do log info", _Hx_AnonObject(fileName = "Completion.hx" ,lineNumber = 97 ,className = "hxsublime.completion.Completion" ,methodName = "dispatchAutoComplete" ))
	hxsublime_completion_Completion.logCompletionInfo(startTime, python_lib_Time.time(), comps)
	return comps
	
hxsublime_completion_Completion.dispatchAutoComplete = Completion_statics_dispatchAutoComplete
def Completion_statics_logCompletionInfo(startTime,endTime,comps):
	runTime = endTime - startTime
	haxe_Log.trace("on_query_completion time: " + Std.string(runTime), _Hx_AnonObject(fileName = "Completion.hx" ,lineNumber = 106 ,className = "hxsublime.completion.Completion" ,methodName = "logCompletionInfo" ))
	haxe_Log.trace("number of completions: " + Std.string(__builtin__.len(comps)), _Hx_AnonObject(fileName = "Completion.hx" ,lineNumber = 107 ,className = "hxsublime.completion.Completion" ,methodName = "logCompletionInfo" ))
	
hxsublime_completion_Completion.logCompletionInfo = Completion_statics_logCompletionInfo


hxsublime_completion_Completion._hx_class = hxsublime_completion_Completion
hxsublime_completion_Completion._hx_class_name = "hxsublime.completion.Completion"
_hx_classes['hxsublime.completion.Completion'] = hxsublime_completion_Completion
hxsublime_completion_Completion._hx_fields = []
hxsublime_completion_Completion._hx_props = []
hxsublime_completion_Completion._hx_methods = []
hxsublime_completion_Completion._hx_statics = ["getCompletionScopes","getCompletionOffset","canRunCompletion","isSupportedScope","emptyHandler","getAutoCompleteHandler","dispatchAutoComplete","logCompletionInfo"]
hxsublime_completion_Completion._hx_interfaces = []

# print hxsublime.completion.hx.CompletionBuild.CompletionBuild
class hxsublime_completion_hx_CompletionBuild:


	def __init__(self,ctx,temp_path,temp_file):
		self.display_cache_set = False
		self.display_cache = None
		self.build = ctx.build().copy()
		self.build.addClasspath(temp_path)
		self.ctx = ctx
		self.tempPath = temp_path
		self.tempFile = temp_file
		self.cache = ctx.project.completionContext.current
	
	# var build
	# var ctx
	# var tempPath
	# var tempFile
	# var cache
	# var display_cache
	# var display_cache_set
	def display(self):
		_g = self
		if not self.display_cache_set:
			self.display_cache_set = True
			def _hx_local_0():
				pos = None
				if not hxsublime_Settings.useOffsetCompletion():
					pos = "0"
				else:
					pos = Std.string(_g.ctx.complete_offset_in_bytes)
				return _g.tempFile + "@" + pos
			
			eval = _hx_local_0
			self.display_cache = eval()
		
		
		return self.display_cache
	







hxsublime_completion_hx_CompletionBuild._hx_class = hxsublime_completion_hx_CompletionBuild
hxsublime_completion_hx_CompletionBuild._hx_class_name = "hxsublime.completion.hx.CompletionBuild"
_hx_classes['hxsublime.completion.hx.CompletionBuild'] = hxsublime_completion_hx_CompletionBuild
hxsublime_completion_hx_CompletionBuild._hx_fields = ["build","ctx","tempPath","tempFile","cache","display_cache","display_cache_set"]
hxsublime_completion_hx_CompletionBuild._hx_props = []
hxsublime_completion_hx_CompletionBuild._hx_methods = ["display"]
hxsublime_completion_hx_CompletionBuild._hx_statics = []
hxsublime_completion_hx_CompletionBuild._hx_interfaces = [hxsublime_macros_LazyFunctionSupport]

# print hxsublime.completion.hx.CompletionContext.CompletionContext
class hxsublime_completion_hx_CompletionContext:


	def __init__(self,view,project,offset,options,settings,prefix):
		self.prefixIsWhitespace_cache_set = False
		self.prefixIsWhitespace_cache = None
		self.tempCompletionSrc_cache_set = False
		self.tempCompletionSrc_cache = None
		self.srcUntilOffset_cache_set = False
		self.srcUntilOffset_cache = None
		self.is_new_cache_set = False
		self.is_new_cache = None
		self.complete_offset_cache_set = False
		self.complete_offset_cache = None
		self.commas_cache_set = False
		self.commas_cache = None
		self.completionInfo_cache_set = False
		self.completionInfo_cache = None
		self.completeChar_cache_set = False
		self.completeChar_cache = None
		self.src_cache_set = False
		self.src_cache = None
		self.lineAfterOffset_cache_set = False
		self.lineAfterOffset_cache = None
		self.srcUntilCompleteOffset_cache_set = False
		self.srcUntilCompleteOffset_cache = None
		self.inControlStruct_cache_set = False
		self.inControlStruct_cache = None
		self.completeCharIsAfterControlStruct_cache_set = False
		self.completeCharIsAfterControlStruct_cache = None
		self.build_cache_set = False
		self.build_cache = None
		self.orig_file_cache_set = False
		self.orig_file_cache = None
		self.complete_offset_in_bytes_cache_set = False
		self.complete_offset_in_bytes_cache = None
		self.view = view
		self.prefix = prefix
		self.offset = offset
		self.project = project
		self.options = options
		self.settings = settings
		self.view_id = view.id()
		self.id = hxsublime_completion_hx_CompletionContext.getCompletionId()
		self.view_pos = hxsublime_tools_ViewTools.getFirstCursorPos(view)
	
	# var prefix
	# var view
	# var view_id
	# var id
	# var options
	# var settings
	# var offset
	# var project
	# var view_pos
	# var complete_offset_in_bytes_cache
	# var complete_offset_in_bytes_cache_set
	def complete_offset_in_bytes(self):
		_g = self
		if not self.complete_offset_in_bytes_cache_set:
			self.complete_offset_in_bytes_cache_set = True
			def _hx_local_0():
				s = _g.srcUntilCompleteOffset()
				b = python_lib_StringTools.encode(s)
				return __builtin__.len(b)
			
			eval = _hx_local_0
			self.complete_offset_in_bytes_cache = eval()
		
		
		return self.complete_offset_in_bytes_cache
	

	# var orig_file_cache
	# var orig_file_cache_set
	def orig_file(self):
		_g = self
		if not self.orig_file_cache_set:
			self.orig_file_cache_set = True
			def _hx_local_0():
				return _g.view.file_name()
			eval = _hx_local_0
			self.orig_file_cache = eval()
		
		
		return self.orig_file_cache
	

	# var build_cache
	# var build_cache_set
	def build(self):
		_g = self
		if not self.build_cache_set:
			self.build_cache_set = True
			def _hx_local_0():
				if not _g.project.hasBuild():
					_g.project.extractBuildArgs()
				
				return _g.project.getBuild(_g.view).copy()
			
			eval = _hx_local_0
			self.build_cache = eval()
		
		
		return self.build_cache
	

	# var completeCharIsAfterControlStruct_cache
	# var completeCharIsAfterControlStruct_cache_set
	def completeCharIsAfterControlStruct(self):
		_g = self
		if not self.completeCharIsAfterControlStruct_cache_set:
			self.completeCharIsAfterControlStruct_cache_set = True
			def _hx_local_0():
				return _g.inControlStruct() and _g.completeChar() == "("
			eval = _hx_local_0
			self.completeCharIsAfterControlStruct_cache = eval()
		
		
		return self.completeCharIsAfterControlStruct_cache
	

	# var inControlStruct_cache
	# var inControlStruct_cache_set
	def inControlStruct(self):
		_g = self
		if not self.inControlStruct_cache_set:
			self.inControlStruct_cache_set = True
			def _hx_local_0():
				return hxsublime_completion_hx_CompletionContext.controlStructRegex.search(_g.srcUntilCompleteOffset()) is not None
			eval = _hx_local_0
			self.inControlStruct_cache = eval()
		
		
		return self.inControlStruct_cache
	

	# var srcUntilCompleteOffset_cache
	# var srcUntilCompleteOffset_cache_set
	def srcUntilCompleteOffset(self):
		_g = self
		if not self.srcUntilCompleteOffset_cache_set:
			self.srcUntilCompleteOffset_cache_set = True
			def _hx_local_0():
				_this = _g.src()
				endIndex = _g.complete_offset()
				return python_Tools.substring(_this, 0, endIndex)
			
			eval = _hx_local_0
			self.srcUntilCompleteOffset_cache = eval()
		
		
		return self.srcUntilCompleteOffset_cache
	

	# var lineAfterOffset_cache
	# var lineAfterOffset_cache_set
	def lineAfterOffset(self):
		_g = self
		if not self.lineAfterOffset_cache_set:
			self.lineAfterOffset_cache_set = True
			def _hx_local_0():
				line_end = None
				_this = _g.src()
				startIndex = _g.offset
				if startIndex is None:
					line_end = _this.find("\n")
				else:
					line_end = _this.find("\n", startIndex)
				
				_this = _g.src()
				return python_Tools.substring(_this, _g.offset, line_end)
				
			
			eval = _hx_local_0
			self.lineAfterOffset_cache = eval()
		
		
		return self.lineAfterOffset_cache
	

	# var src_cache
	# var src_cache_set
	def src(self):
		_g = self
		if not self.src_cache_set:
			self.src_cache_set = True
			def _hx_local_0():
				return hxsublime_tools_ViewTools.getContent(_g.view)
			eval = _hx_local_0
			self.src_cache = eval()
		
		
		return self.src_cache
	

	# var completeChar_cache
	# var completeChar_cache_set
	def completeChar(self):
		_g = self
		if not self.completeChar_cache_set:
			self.completeChar_cache_set = True
			def _hx_local_0():
				_this = _g.src()
				index = _g.complete_offset() - 1
				return _this[index]
			
			eval = _hx_local_0
			self.completeChar_cache = eval()
		
		
		return self.completeChar_cache
	

	# var completionInfo_cache
	# var completionInfo_cache_set
	def completionInfo(self):
		_g = self
		if not self.completionInfo_cache_set:
			self.completionInfo_cache_set = True
			def _hx_local_0():
				return hxsublime_completion_hx_CompletionContext.get_completion_info(_g.view, _g.offset, _g.src())
			eval = _hx_local_0
			self.completionInfo_cache = eval()
		
		
		return self.completionInfo_cache
	

	# var commas_cache
	# var commas_cache_set
	def commas(self):
		_g = self
		if not self.commas_cache_set:
			self.commas_cache_set = True
			def _hx_local_0():
				_this = _g.completionInfo()
				return _this[0]
			
			eval = _hx_local_0
			self.commas_cache = eval()
		
		
		return self.commas_cache
	

	# var complete_offset_cache
	# var complete_offset_cache_set
	def complete_offset(self):
		_g = self
		if not self.complete_offset_cache_set:
			self.complete_offset_cache_set = True
			def _hx_local_0():
				_this = _g.completionInfo()
				return _this[1]
			
			eval = _hx_local_0
			self.complete_offset_cache = eval()
		
		
		return self.complete_offset_cache
	

	# var is_new_cache
	# var is_new_cache_set
	def is_new(self):
		_g = self
		if not self.is_new_cache_set:
			self.is_new_cache_set = True
			def _hx_local_0():
				_this = _g.completionInfo()
				return _this[3]
			
			eval = _hx_local_0
			self.is_new_cache = eval()
		
		
		return self.is_new_cache
	

	# var srcUntilOffset_cache
	# var srcUntilOffset_cache_set
	def srcUntilOffset(self):
		_g = self
		if not self.srcUntilOffset_cache_set:
			self.srcUntilOffset_cache_set = True
			def _hx_local_0():
				_this = _g.src()
				return python_Tools.substring(_this, 0, _g.offset - 1)
			
			eval = _hx_local_0
			self.srcUntilOffset_cache = eval()
		
		
		return self.srcUntilOffset_cache
	

	# var tempCompletionSrc_cache
	# var tempCompletionSrc_cache_set
	def tempCompletionSrc(self):
		_g = self
		if not self.tempCompletionSrc_cache_set:
			self.tempCompletionSrc_cache_set = True
			def _hx_local_3():
				def _hx_local_2():
					def _hx_local_1():
						_this = _g.src()
						len = _g.complete_offset()
						return python_Tools.substr(_this, 0, len)
					
					def _hx_local_0():
						_this = _g.src()
						pos = _g.complete_offset()
						return python_Tools.substr(_this, pos, None)
					
					return _hx_local_1() + "|" + _hx_local_0()
				
				return _hx_local_2()
			
			eval = _hx_local_3
			self.tempCompletionSrc_cache = eval()
		
		
		return self.tempCompletionSrc_cache
	

	# var prefixIsWhitespace_cache
	# var prefixIsWhitespace_cache_set
	def prefixIsWhitespace(self):
		_g = self
		if not self.prefixIsWhitespace_cache_set:
			self.prefixIsWhitespace_cache_set = True
			def _hx_local_0():
				return hxsublime_tools_StringTools.isWhitespaceOrEmpty(_g.prefix)
			eval = _hx_local_0
			self.prefixIsWhitespace_cache = eval()
		
		
		return self.prefixIsWhitespace_cache
	

	def eq(self,other):
		_g = self
		def _hx_local_0():
			prefixSame = True
			if _g.options.types().hasHint():
				prefixSame = _g.prefix == other.prefix or _g.prefixIsWhitespace() and other.prefixIsWhitespace()
			
			haxe_Log.trace("same PREFIX:" + Std.string(prefixSame), _Hx_AnonObject(fileName = "CompletionContext.hx" ,lineNumber = 214 ,className = "hxsublime.completion.hx.CompletionContext" ,methodName = "eq" ))
			haxe_Log.trace("PREFIXES:" + _g.prefix + " - " + other.prefix, _Hx_AnonObject(fileName = "CompletionContext.hx" ,lineNumber = 215 ,className = "hxsublime.completion.hx.CompletionContext" ,methodName = "eq" ))
			return prefixSame
		
		prefixCheck = _hx_local_0
		return other is not None and self.orig_file() == other.orig_file() and self.offset == other.offset and self.commas() == other.commas() and self.srcUntilOffset() == other.srcUntilOffset() and self.options.eq(other.options) and self.completeChar() == other.completeChar() and self.lineAfterOffset() == other.lineAfterOffset() and prefixCheck()
	





hxsublime_completion_hx_CompletionContext.controlStructRegex = python_lib_Re.compile("\\s+(if|switch|for|while)\\s*\\($")
def CompletionContext_statics_getCompletionId():
	return python_lib_Time.time()
hxsublime_completion_hx_CompletionContext.getCompletionId = CompletionContext_statics_getCompletionId
def CompletionContext_statics_count_commas_and_complete_offset(src,prev_comma,complete_offset):
	commas = 0
	closed_pars = 0
	closed_braces = 0
	closed_brackets = 0
	_g = 0
	while _g < prev_comma:
		def _hx_local_1():
			nonlocal _g
			_hx_local_0 = _g
			_g = _g + 1
			return _hx_local_0
			
		
		j = _hx_local_1()
		i = prev_comma - j
		c = src[i]
		if c == ")":
			closed_pars = closed_pars + 1
		elif c == "(":
			if closed_pars < 1:
				complete_offset = i + 1
				break
		
			else:
				closed_pars = closed_pars - 1
		elif c == ",":
			if closed_pars == 0 and closed_braces == 0 and closed_brackets == 0:
				commas = commas + 1
			
		elif c == "{":
			closed_braces = closed_braces - 1
		elif c == "}":
			closed_braces = closed_braces + 1
		elif c == "[":
			closed_brackets = closed_brackets - 1
		elif c == "]":
			closed_brackets = closed_brackets + 1
		
	
	
	return (commas, complete_offset)
	
hxsublime_completion_hx_CompletionContext.count_commas_and_complete_offset = CompletionContext_statics_count_commas_and_complete_offset
def CompletionContext_statics_get_completion_info(view,offset,src):
	prev = src[offset - 1]
	commas = 0
	complete_offset = offset
	is_new = False
	prevSymbolIsComma = False
	if prev == " " and offset - 4 >= 0 and python_Tools.substring(src, offset - 4, offset - 1) == "new":
		is_new = True
	elif not prev in "(.;":
		fragment = view.substr(sublime_Region(0, offset))
		prev_dot = fragment.rfind(".", None)
		prev_par = fragment.rfind("(", None)
		prev_comma = fragment.rfind(",", None)
		prev_colon = fragment.rfind(":", None)
		prev_brace = fragment.rfind("{", None)
		prev_semi = fragment.rfind(";", None)
		prev_symbol = __builtin__.max(prev_dot, prev_par, prev_comma, prev_brace, prev_colon, prev_semi)
		if prev_symbol == prev_comma:
			r = hxsublime_completion_hx_CompletionContext.count_commas_and_complete_offset(src, prev_comma, complete_offset)
			commas = r[0]
			complete_offset = r[1]
			prevSymbolIsComma = True
		
		else:
			complete_offset = __builtin__.max(prev_dot + 1, prev_par + 1, prev_colon + 1, prev_brace + 1, prev_semi + 1)
	
	
	return (commas, complete_offset, prevSymbolIsComma, is_new)
	
hxsublime_completion_hx_CompletionContext.get_completion_info = CompletionContext_statics_get_completion_info


hxsublime_completion_hx_CompletionContext._hx_class = hxsublime_completion_hx_CompletionContext
hxsublime_completion_hx_CompletionContext._hx_class_name = "hxsublime.completion.hx.CompletionContext"
_hx_classes['hxsublime.completion.hx.CompletionContext'] = hxsublime_completion_hx_CompletionContext
hxsublime_completion_hx_CompletionContext._hx_fields = ["prefix","view","view_id","id","options","settings","offset","project","view_pos","complete_offset_in_bytes_cache","complete_offset_in_bytes_cache_set","orig_file_cache","orig_file_cache_set","build_cache","build_cache_set","completeCharIsAfterControlStruct_cache","completeCharIsAfterControlStruct_cache_set","inControlStruct_cache","inControlStruct_cache_set","srcUntilCompleteOffset_cache","srcUntilCompleteOffset_cache_set","lineAfterOffset_cache","lineAfterOffset_cache_set","src_cache","src_cache_set","completeChar_cache","completeChar_cache_set","completionInfo_cache","completionInfo_cache_set","commas_cache","commas_cache_set","complete_offset_cache","complete_offset_cache_set","is_new_cache","is_new_cache_set","srcUntilOffset_cache","srcUntilOffset_cache_set","tempCompletionSrc_cache","tempCompletionSrc_cache_set","prefixIsWhitespace_cache","prefixIsWhitespace_cache_set"]
hxsublime_completion_hx_CompletionContext._hx_props = []
hxsublime_completion_hx_CompletionContext._hx_methods = ["complete_offset_in_bytes","orig_file","build","completeCharIsAfterControlStruct","inControlStruct","srcUntilCompleteOffset","lineAfterOffset","src","completeChar","completionInfo","commas","complete_offset","is_new","srcUntilOffset","tempCompletionSrc","prefixIsWhitespace","eq"]
hxsublime_completion_hx_CompletionContext._hx_statics = ["controlStructRegex","getCompletionId","count_commas_and_complete_offset","get_completion_info"]
hxsublime_completion_hx_CompletionContext._hx_interfaces = [hxsublime_macros_LazyFunctionSupport]

# print hxsublime.completion.hx.CompletionOptions.CompletionOptions
class hxsublime_completion_hx_CompletionOptions:


	def __init__(self,trigger,context = 2,types = 1,toplevel = 4):
		if context is None:
			context = 2
		
		if types is None:
			types = 1
		
		if toplevel is None:
			toplevel = 4
		
		self.regularCompletion_cache_set = False
		self.regularCompletion_cache = None
		self.macroCompletion_cache_set = False
		self.macroCompletion_cache = None
		self.manualCompletion_cache_set = False
		self.manualCompletion_cache = None
		self.asyncTrigger_cache_set = False
		self.asyncTrigger_cache = None
		self._types = hxsublime_completion_hx_CompletionTypes(types)
		self._toplevel = hxsublime_completion_hx_TopLevelOptions(toplevel)
		self._context = context
		self._trigger = trigger
	
	# var _types
	# var _toplevel
	# var _context
	# var _trigger
	def copyAsManual(self):
		return hxsublime_completion_hx_CompletionOptions(1, self._context, self.types().val(), self._toplevel.val())

	def copyAsAsync(self):
		return hxsublime_completion_hx_CompletionOptions(3, self._context, self.types().val(), self._toplevel.val())

	def types(self):
		return self._types

	# var asyncTrigger_cache
	# var asyncTrigger_cache_set
	def asyncTrigger(self):
		_g = self
		if not self.asyncTrigger_cache_set:
			self.asyncTrigger_cache_set = True
			def _hx_local_0():
				return _g._trigger == 3
			eval = _hx_local_0
			self.asyncTrigger_cache = eval()
		
		
		return self.asyncTrigger_cache
	

	# var manualCompletion_cache
	# var manualCompletion_cache_set
	def manualCompletion(self):
		_g = self
		if not self.manualCompletion_cache_set:
			self.manualCompletion_cache_set = True
			def _hx_local_0():
				return _g._trigger == 1
			eval = _hx_local_0
			self.manualCompletion_cache = eval()
		
		
		return self.manualCompletion_cache
	

	# var macroCompletion_cache
	# var macroCompletion_cache_set
	def macroCompletion(self):
		_g = self
		if not self.macroCompletion_cache_set:
			self.macroCompletion_cache_set = True
			def _hx_local_0():
				return _g._context == 1
			eval = _hx_local_0
			self.macroCompletion_cache = eval()
		
		
		return self.macroCompletion_cache
	

	# var regularCompletion_cache
	# var regularCompletion_cache_set
	def regularCompletion(self):
		_g = self
		if not self.regularCompletion_cache_set:
			self.regularCompletion_cache_set = True
			def _hx_local_0():
				return _g._context == 2
			eval = _hx_local_0
			self.regularCompletion_cache = eval()
		
		
		return self.regularCompletion_cache
	

	def eq(self,other):
		return self._trigger == other._trigger and self._types.eq(other._types) and self._toplevel.eq(other._toplevel) and self._context == other._context





hxsublime_completion_hx_CompletionOptions.__meta__ = _Hx_AnonObject(fields = _Hx_AnonObject(types = _Hx_AnonObject(property = None ) ) )


hxsublime_completion_hx_CompletionOptions._hx_class = hxsublime_completion_hx_CompletionOptions
hxsublime_completion_hx_CompletionOptions._hx_class_name = "hxsublime.completion.hx.CompletionOptions"
_hx_classes['hxsublime.completion.hx.CompletionOptions'] = hxsublime_completion_hx_CompletionOptions
hxsublime_completion_hx_CompletionOptions._hx_fields = ["_types","_toplevel","_context","_trigger","asyncTrigger_cache","asyncTrigger_cache_set","manualCompletion_cache","manualCompletion_cache_set","macroCompletion_cache","macroCompletion_cache_set","regularCompletion_cache","regularCompletion_cache_set"]
hxsublime_completion_hx_CompletionOptions._hx_props = []
hxsublime_completion_hx_CompletionOptions._hx_methods = ["copyAsManual","copyAsAsync","types","asyncTrigger","manualCompletion","macroCompletion","regularCompletion","eq"]
hxsublime_completion_hx_CompletionOptions._hx_statics = ["__meta__"]
hxsublime_completion_hx_CompletionOptions._hx_interfaces = [hxsublime_macros_LazyFunctionSupport]

# print hxsublime.completion.hx.CompletionResult.CompletionResult
class hxsublime_completion_hx_CompletionResult:


	def __init__(self,ret,comps,status,hints,ctx,retrieve_toplevel_comps):
		self.allComps_cache_set = False
		self.allComps_cache = None
		self.requiresToplevelComps_cache_set = False
		self.requiresToplevelComps_cache = None
		self.showTopLevelSnippets_cache_set = False
		self.showTopLevelSnippets_cache = None
		self.hasResults_cache_set = False
		self.hasResults_cache = None
		self.hasCompilerResults_cache_set = False
		self.hasCompilerResults_cache = None
		self.hasHints_cache_set = False
		self.hasHints_cache = None
		self._toplevel_comps_cache_set = False
		self._toplevel_comps_cache = None
		self.ret = ret
		self.comps = comps
		self.status = status
		self.hints = hints
		self.ctx = ctx
		if retrieve_toplevel_comps is None:
			def _hx_local_0():
				return []
			retrieve_toplevel_comps = _hx_local_0
		
		
		self.retrieve_toplevel_comps = retrieve_toplevel_comps
	
	# var hints
	# var ctx
	# var ret
	# var comps
	# var status
	# var retrieve_toplevel_comps
	# var _toplevel_comps_cache
	# var _toplevel_comps_cache_set
	def _toplevel_comps(self):
		_g = self
		if not self._toplevel_comps_cache_set:
			self._toplevel_comps_cache_set = True
			def _hx_local_0():
				return _g.retrieve_toplevel_comps()
			eval = _hx_local_0
			self._toplevel_comps_cache = eval()
		
		
		return self._toplevel_comps_cache
	

	# var hasHints_cache
	# var hasHints_cache_set
	def hasHints(self):
		_g = self
		if not self.hasHints_cache_set:
			self.hasHints_cache_set = True
			def _hx_local_0():
				return __builtin__.len(_g.hints) > 0
			eval = _hx_local_0
			self.hasHints_cache = eval()
		
		
		return self.hasHints_cache
	

	# var hasCompilerResults_cache
	# var hasCompilerResults_cache_set
	def hasCompilerResults(self):
		_g = self
		if not self.hasCompilerResults_cache_set:
			self.hasCompilerResults_cache_set = True
			def _hx_local_0():
				return __builtin__.len(_g.comps) > 0
			eval = _hx_local_0
			self.hasCompilerResults_cache = eval()
		
		
		return self.hasCompilerResults_cache
	

	# var hasResults_cache
	# var hasResults_cache_set
	def hasResults(self):
		_g = self
		if not self.hasResults_cache_set:
			self.hasResults_cache_set = True
			def _hx_local_2():
				def _hx_local_1():
					def _hx_local_0():
						_this = _g._toplevel_comps()
						return __builtin__.len(_this)
					
					return __builtin__.len(_g.comps) > 0 or __builtin__.len(_g.hints) > 0 or _g.requiresToplevelComps() and _hx_local_0() > 0
				
				return _hx_local_1()
			
			eval = _hx_local_2
			self.hasResults_cache = eval()
		
		
		return self.hasResults_cache
	

	# var showTopLevelSnippets_cache
	# var showTopLevelSnippets_cache_set
	def showTopLevelSnippets(self):
		_g = self
		if not self.showTopLevelSnippets_cache_set:
			self.showTopLevelSnippets_cache_set = True
			def _hx_local_0():
				req = _g.requiresToplevelComps()
				r = req and not _g.ctx.is_new()
				return r
			
			eval = _hx_local_0
			self.showTopLevelSnippets_cache = eval()
		
		
		return self.showTopLevelSnippets_cache
	

	# var requiresToplevelComps_cache
	# var requiresToplevelComps_cache_set
	def requiresToplevelComps(self):
		_g = self
		if not self.requiresToplevelComps_cache_set:
			self.requiresToplevelComps_cache_set = True
			def _hx_local_0():
				prefix_is_whitespace = hxsublime_tools_StringTools.isWhitespaceOrEmpty(_g.ctx.prefix)
				haxe_Log.trace("prefix_is_whitespace:" + Std.string(prefix_is_whitespace), _Hx_AnonObject(fileName = "CompletionResult.hx" ,lineNumber = 99 ,className = "hxsublime.completion.hx.CompletionResult" ,methodName = "requiresToplevelComps" ))
				haxe_Log.trace("has_hints:" + Std.string(_g.hasHints()), _Hx_AnonObject(fileName = "CompletionResult.hx" ,lineNumber = 100 ,className = "hxsublime.completion.hx.CompletionResult" ,methodName = "requiresToplevelComps" ))
				haxe_Log.trace("has_hint:" + Std.string(_g.ctx.options.types().hasHint()), _Hx_AnonObject(fileName = "CompletionResult.hx" ,lineNumber = 101 ,className = "hxsublime.completion.hx.CompletionResult" ,methodName = "requiresToplevelComps" ))
				haxe_Log.trace("has_compiler_results:" + Std.string(_g.hasCompilerResults()), _Hx_AnonObject(fileName = "CompletionResult.hx" ,lineNumber = 102 ,className = "hxsublime.completion.hx.CompletionResult" ,methodName = "requiresToplevelComps" ))
				r = not (prefix_is_whitespace and _g.hasHints() and _g.ctx.options.types().hasHint() or _g.hasCompilerResults())
				haxe_Log.trace("requires_toplevel_comps:" + Std.string(r), _Hx_AnonObject(fileName = "CompletionResult.hx" ,lineNumber = 104 ,className = "hxsublime.completion.hx.CompletionResult" ,methodName = "requiresToplevelComps" ))
				return r
			
			eval = _hx_local_0
			self.requiresToplevelComps_cache = eval()
		
		
		return self.requiresToplevelComps_cache
	

	# var allComps_cache
	# var allComps_cache_set
	def allComps(self):
		_g = self
		if not self.allComps_cache_set:
			self.allComps_cache_set = True
			def _hx_local_1():
				res = []
				if _g.requiresToplevelComps():
					x = _g._toplevel_comps()
					res.extend(x)
				
				
				res.extend(_g.comps)
				def _hx_local_0(s1,s2):
					if s1[0] < s2[0]:
						return -1
					elif s1[0] > s2[0]:
						return 1
					else:
						return 0
				res.sort(key=python_lib_FuncTools.cmp_to_key(_hx_local_0))
				return res
			
			eval = _hx_local_1
			self.allComps_cache = eval()
		
		
		return self.allComps_cache
	





def CompletionResult_statics_emptyResult(ctx,retrieve_toplevel_comps = None):
	if retrieve_toplevel_comps is None:
		retrieve_toplevel_comps = None
	
	return hxsublime_completion_hx_CompletionResult("", [], "", [], ctx, retrieve_toplevel_comps)
	
hxsublime_completion_hx_CompletionResult.emptyResult = CompletionResult_statics_emptyResult


hxsublime_completion_hx_CompletionResult._hx_class = hxsublime_completion_hx_CompletionResult
hxsublime_completion_hx_CompletionResult._hx_class_name = "hxsublime.completion.hx.CompletionResult"
_hx_classes['hxsublime.completion.hx.CompletionResult'] = hxsublime_completion_hx_CompletionResult
hxsublime_completion_hx_CompletionResult._hx_fields = ["hints","ctx","ret","comps","status","retrieve_toplevel_comps","_toplevel_comps_cache","_toplevel_comps_cache_set","hasHints_cache","hasHints_cache_set","hasCompilerResults_cache","hasCompilerResults_cache_set","hasResults_cache","hasResults_cache_set","showTopLevelSnippets_cache","showTopLevelSnippets_cache_set","requiresToplevelComps_cache","requiresToplevelComps_cache_set","allComps_cache","allComps_cache_set"]
hxsublime_completion_hx_CompletionResult._hx_props = []
hxsublime_completion_hx_CompletionResult._hx_methods = ["_toplevel_comps","hasHints","hasCompilerResults","hasResults","showTopLevelSnippets","requiresToplevelComps","allComps"]
hxsublime_completion_hx_CompletionResult._hx_statics = ["emptyResult"]
hxsublime_completion_hx_CompletionResult._hx_interfaces = [hxsublime_macros_LazyFunctionSupport]

# print hxsublime.completion.hx.CompletionSettings.CompletionSettings
class hxsublime_completion_hx_CompletionSettings:


	def __init__(self,settings):
		self.getCompletionDelays_cache_set = False
		self.getCompletionDelays_cache = None
		self.showOnlyAsyncCompletions_cache_set = False
		self.showOnlyAsyncCompletions_cache = None
		self.isAsyncCompletion_cache_set = False
		self.isAsyncCompletion_cache = None
		self.topLevelCompletionsOnDemand_cache_set = False
		self.topLevelCompletionsOnDemand_cache = None
		self.noFuzzyCompletion_cache_set = False
		self.noFuzzyCompletion_cache = None
		self.settings = settings
	
	# var settings
	# var noFuzzyCompletion_cache
	# var noFuzzyCompletion_cache_set
	def noFuzzyCompletion(self):
		_g = self
		if not self.noFuzzyCompletion_cache_set:
			self.noFuzzyCompletion_cache_set = True
			def _hx_local_0():
				return _g.settings.noFuzzyCompletion()
			eval = _hx_local_0
			self.noFuzzyCompletion_cache = eval()
		
		
		return self.noFuzzyCompletion_cache
	

	# var topLevelCompletionsOnDemand_cache
	# var topLevelCompletionsOnDemand_cache_set
	def topLevelCompletionsOnDemand(self):
		_g = self
		if not self.topLevelCompletionsOnDemand_cache_set:
			self.topLevelCompletionsOnDemand_cache_set = True
			def _hx_local_0():
				return _g.settings.topLevelCompletionsOnDemand()
			eval = _hx_local_0
			self.topLevelCompletionsOnDemand_cache = eval()
		
		
		return self.topLevelCompletionsOnDemand_cache
	

	# var isAsyncCompletion_cache
	# var isAsyncCompletion_cache_set
	def isAsyncCompletion(self):
		_g = self
		if not self.isAsyncCompletion_cache_set:
			self.isAsyncCompletion_cache_set = True
			def _hx_local_0():
				return _g.settings.isAsyncCompletion()
			eval = _hx_local_0
			self.isAsyncCompletion_cache = eval()
		
		
		return self.isAsyncCompletion_cache
	

	# var showOnlyAsyncCompletions_cache
	# var showOnlyAsyncCompletions_cache_set
	def showOnlyAsyncCompletions(self):
		_g = self
		if not self.showOnlyAsyncCompletions_cache_set:
			self.showOnlyAsyncCompletions_cache_set = True
			def _hx_local_0():
				return _g.settings.showOnlyAsyncCompletions()
			eval = _hx_local_0
			self.showOnlyAsyncCompletions_cache = eval()
		
		
		return self.showOnlyAsyncCompletions_cache
	

	# var getCompletionDelays_cache
	# var getCompletionDelays_cache_set
	def getCompletionDelays(self):
		_g = self
		if not self.getCompletionDelays_cache_set:
			self.getCompletionDelays_cache_set = True
			def _hx_local_0():
				return _g.settings.getCompletionDelays()
			eval = _hx_local_0
			self.getCompletionDelays_cache = eval()
		
		
		return self.getCompletionDelays_cache
	

	def showCompletionTimes(self,view):
		return self.settings.showCompletionTimes(view)







hxsublime_completion_hx_CompletionSettings._hx_class = hxsublime_completion_hx_CompletionSettings
hxsublime_completion_hx_CompletionSettings._hx_class_name = "hxsublime.completion.hx.CompletionSettings"
_hx_classes['hxsublime.completion.hx.CompletionSettings'] = hxsublime_completion_hx_CompletionSettings
hxsublime_completion_hx_CompletionSettings._hx_fields = ["settings","noFuzzyCompletion_cache","noFuzzyCompletion_cache_set","topLevelCompletionsOnDemand_cache","topLevelCompletionsOnDemand_cache_set","isAsyncCompletion_cache","isAsyncCompletion_cache_set","showOnlyAsyncCompletions_cache","showOnlyAsyncCompletions_cache_set","getCompletionDelays_cache","getCompletionDelays_cache_set"]
hxsublime_completion_hx_CompletionSettings._hx_props = []
hxsublime_completion_hx_CompletionSettings._hx_methods = ["noFuzzyCompletion","topLevelCompletionsOnDemand","isAsyncCompletion","showOnlyAsyncCompletions","getCompletionDelays","showCompletionTimes"]
hxsublime_completion_hx_CompletionSettings._hx_statics = []
hxsublime_completion_hx_CompletionSettings._hx_interfaces = [hxsublime_macros_LazyFunctionSupport]

# print hxsublime.completion.hx.CompletionTypes.CompletionTypes
class hxsublime_completion_hx_CompletionTypes:


	def __init__(self,val = 1):
		if val is None:
			val = 1
		
		self._opt = val
	
	# var _opt
	def val(self):
		return self._opt

	def add(self,val):
		self._opt = self._opt | val

	def addHint(self):
		self._opt = self._opt | 2

	def hasRegular(self):
		return (self._opt & 1) > 0

	def hasHint(self):
		return (self._opt & 2) > 0

	def hasToplevel(self):
		return (self._opt & 4) > 0

	def hasToplevelForced(self):
		return (self._opt & 12) > 0

	def eq(self,other):
		return self._opt == other._opt







hxsublime_completion_hx_CompletionTypes._hx_class = hxsublime_completion_hx_CompletionTypes
hxsublime_completion_hx_CompletionTypes._hx_class_name = "hxsublime.completion.hx.CompletionTypes"
_hx_classes['hxsublime.completion.hx.CompletionTypes'] = hxsublime_completion_hx_CompletionTypes
hxsublime_completion_hx_CompletionTypes._hx_fields = ["_opt"]
hxsublime_completion_hx_CompletionTypes._hx_props = []
hxsublime_completion_hx_CompletionTypes._hx_methods = ["val","add","addHint","hasRegular","hasHint","hasToplevel","hasToplevelForced","eq"]
hxsublime_completion_hx_CompletionTypes._hx_statics = []
hxsublime_completion_hx_CompletionTypes._hx_interfaces = []

# print hxsublime.completion.hx.Constants.Constants
class hxsublime_completion_hx_Constants:

	pass




hxsublime_completion_hx_Constants.COMPLETION_TRIGGER_MANUAL = 1
hxsublime_completion_hx_Constants.COMPLETION_TRIGGER_AUTO = 2
hxsublime_completion_hx_Constants.COMPLETION_TRIGGER_ASYNC = 3
hxsublime_completion_hx_Constants.COMPILER_CONTEXT_MACRO = 1
hxsublime_completion_hx_Constants.COMPILER_CONTEXT_REGULAR = 2
hxsublime_completion_hx_Constants.COMPLETION_TYPE_REGULAR = 1
hxsublime_completion_hx_Constants.COMPLETION_TYPE_HINT = 2
hxsublime_completion_hx_Constants.COMPLETION_TYPE_TOPLEVEL = 4
hxsublime_completion_hx_Constants.COMPLETION_TYPE_TOPLEVEL_FORCED = 12
hxsublime_completion_hx_Constants.TOPLEVEL_OPTION_TYPES = 1
hxsublime_completion_hx_Constants.TOPLEVEL_OPTION_LOCALS = 2
hxsublime_completion_hx_Constants.TOPLEVEL_OPTION_KEYWORDS = 4
hxsublime_completion_hx_Constants.TOPLEVEL_OPTION_ALL = 7


hxsublime_completion_hx_Constants._hx_class = hxsublime_completion_hx_Constants
hxsublime_completion_hx_Constants._hx_class_name = "hxsublime.completion.hx.Constants"
_hx_classes['hxsublime.completion.hx.Constants'] = hxsublime_completion_hx_Constants
hxsublime_completion_hx_Constants._hx_fields = []
hxsublime_completion_hx_Constants._hx_props = []
hxsublime_completion_hx_Constants._hx_methods = []
hxsublime_completion_hx_Constants._hx_statics = ["COMPLETION_TRIGGER_MANUAL","COMPLETION_TRIGGER_AUTO","COMPLETION_TRIGGER_ASYNC","COMPILER_CONTEXT_MACRO","COMPILER_CONTEXT_REGULAR","COMPLETION_TYPE_REGULAR","COMPLETION_TYPE_HINT","COMPLETION_TYPE_TOPLEVEL","COMPLETION_TYPE_TOPLEVEL_FORCED","TOPLEVEL_OPTION_TYPES","TOPLEVEL_OPTION_LOCALS","TOPLEVEL_OPTION_KEYWORDS","TOPLEVEL_OPTION_ALL"]
hxsublime_completion_hx_Constants._hx_interfaces = []

# print hxsublime.completion.hx.HxCompletion.HxCompletion
class hxsublime_completion_hx_HxCompletion:

	pass




def HxCompletion_statics_triggerCompletion(view,options,show_top_level_snippets = False):
	if show_top_level_snippets is None:
		show_top_level_snippets = False
	
	def _hx_local_3():
		project = hxsublime_project_Projects.currentProject(view)
		if not project.hasBuild():
			project.extractBuildArgs(view, False)
		
		if project.hasBuild():
			project.completionContext.setTrigger(view, options)
			def _hx_local_0():
				x = _Hx_AnonObject(api_completions_only = not show_top_level_snippets ,disable_auto_insert = True ,next_completion_if_showing = True ,auto_complete_commit_on_tab = True )
				def _hx_local_2():
					def _hx_local_1():
						d = python_lib_Dict()
						_g = 0
						_g1 = Reflect.fields(x)
						while _g < len(_g1):
							f = _g1[_g]
							_g = _g + 1
							val = Reflect.field(x, f)
							python_lib_DictImpl.set(d, f, val)
							
						
						
						return d
					
					return _hx_local_1()
				
				return _hx_local_2()
			
			view.run_command("auto_complete", _hx_local_0())
		
		else:
			project.extractBuildArgs(view, True)
	
	run = _hx_local_3
	view.run_command("hide_auto_complete")
	sublime_Sublime.set_timeout(run, 0)
	
hxsublime_completion_hx_HxCompletion.triggerCompletion = HxCompletion_statics_triggerCompletion
def HxCompletion_statics_autoComplete(project,view,offset,prefix):
	haxe_Log.trace("run auto_complete", _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 70 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "autoComplete" ))
	options = project.completionContext.getAndDeleteTrigger(view)
	res = None
	if options is not None and options.asyncTrigger():
		haxe_Log.trace("run auto_complete 1", _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 78 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "autoComplete" ))
		async_result = project.completionContext.getAndDeleteAsync(view)
		use_async_results = async_result is not None and async_result.hasResults()
		if use_async_results:
			haxe_Log.trace("run auto_complete 2", _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 84 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "autoComplete" ))
			res = hxsublime_completion_hx_HxCompletion.getAvailableAsyncCompletions(async_result, view)
			res = hxsublime_completion_hx_HxCompletion.completionResultWithSmartSnippets(view, res, async_result, options)
			haxe_Log.trace(res, _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 87 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "autoComplete" ))
		
		else:
			haxe_Log.trace("run auto_complete 3", _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 91 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "autoComplete" ))
			res = hxsublime_completion_hx_HxCompletion.cancelCompletion(view)
		
	
	else:
		haxe_Log.trace("create comps", _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 97 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "autoComplete" ))
		res = hxsublime_completion_hx_HxCompletion.createNewCompletions(project, view, offset, options, prefix)
		haxe_Log.trace("after create comps", _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 100 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "autoComplete" ))
	
	return res
	
hxsublime_completion_hx_HxCompletion.autoComplete = HxCompletion_statics_autoComplete
def HxCompletion_statics_getAvailableAsyncCompletions(compResult,view):
	ctx = compResult.ctx
	has_results = compResult.hasResults()
	discard_results = not has_results and ctx.options.types().hasHint()
	if discard_results:
		return hxsublime_completion_hx_HxCompletion.cancelCompletion(view)
	else:
		return hxsublime_completion_hx_HxCompletion.combineHintsAndComps(compResult)
	
hxsublime_completion_hx_HxCompletion.getAvailableAsyncCompletions = HxCompletion_statics_getAvailableAsyncCompletions
def HxCompletion_statics_completionResultWithSmartSnippets(view,comps,result,options):
	use_snippets = hxsublime_Settings.smartSnippets(view)
	prefix_is_whitespace = hxsublime_tools_StringTools.isWhitespaceOrEmpty(result.ctx.prefix)
	has_one_hint = options.types().hasHint() and __builtin__.len(result.hints) == 1
	same_cursor_pos = hxsublime_tools_ViewTools.getFirstCursorPos(view) == result.ctx.view_pos
	lineAfterOffset = None
	s = result.ctx.lineAfterOffset()
	lineAfterOffset = s.strip(None)
	
	really_insert = None
	def _hx_local_0():
		str = lineAfterOffset[0]
		return "),".find(str)
	
	really_insert = __builtin__.len(lineAfterOffset) == 0 or _hx_local_0() > -1
	if really_insert and prefix_is_whitespace and use_snippets and has_one_hint and same_cursor_pos:
		onlyHint = comps[0]
		hxsublime_tools_ViewTools.insertSnippet(view, onlyHint[1])
		comps = hxsublime_completion_hx_HxCompletion.cancelCompletion(view)
	
	
	return comps
	
hxsublime_completion_hx_HxCompletion.completionResultWithSmartSnippets = HxCompletion_statics_completionResultWithSmartSnippets
def HxCompletion_statics_createNewCompletions(project,view,offset,options,prefix):
	cache = project.completionContext.current
	haxe_Log.trace("------- COMPLETION START -----------", _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 150 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "createNewCompletions" ))
	ctx = hxsublime_completion_hx_HxCompletion.createCompletionContext(project, view, offset, options, prefix)
	res = None
	haxe_Log.trace("MANUAL COMPLETION: " + Std.string(ctx.options.manualCompletion()), _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 156 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "createNewCompletions" ))
	if hxsublime_completion_hx_HxCompletion.isEquivalentCompletionAlreadyRunning(ctx):
		haxe_Log.trace("cancel completion, same is running", _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 164 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "createNewCompletions" ))
		res = hxsublime_completion_hx_HxCompletion.cancelCompletion(ctx.view)
	
	elif not ctx.options.manualCompletion():
		hxsublime_completion_hx_HxCompletion.triggerManualCompletion(ctx.view, ctx.options.copyAsManual())
		res = hxsublime_completion_hx_HxCompletion.cancelCompletion(ctx.view)
	
	elif hxsublime_completion_hx_HxCompletion.isAfterIntIterator(ctx.src(), ctx.offset):
		res = hxsublime_completion_hx_HxCompletion.cancelCompletion(ctx.view)
	elif hxsublime_completion_hx_HxCompletion.isIntIteratorCompletion(ctx.src(), ctx.offset):
		haxe_Log.trace("iterator completion", _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 178 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "createNewCompletions" ))
		res = [(".\tint iterator", "..")]
	
	else:
		if hxsublime_completion_hx_HxCompletion.isHintCompletion(ctx):
			haxe_Log.trace("ADD HINT", _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 185 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "createNewCompletions" ))
			ctx.options.types().addHint()
		
		
		isDirectlyAfterControlStruct = ctx.completeCharIsAfterControlStruct()
		onlyTopLevel = ctx.is_new() or isDirectlyAfterControlStruct
		haxe_Log.trace("onlyTopLevel: " + Std.string(onlyTopLevel), _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 194 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "createNewCompletions" ))
		if onlyTopLevel:
			res = hxsublime_completion_hx_HxCompletion.getToplevelCompletions(ctx)
		else:
			last_ctx = cache.input
			if hxsublime_completion_hx_HxCompletion.useCompletionCache(ctx, last_ctx):
				haxe_Log.trace("USE COMPLETION CACHE", _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 208 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "createNewCompletions" ))
				out = cache.output
				hxsublime_completion_hx_HxCompletion.updateCompletionCache(cache, out)
				project.completionContext.addCompletionResult(out)
				res = hxsublime_completion_hx_HxCompletion.cancelCompletion(view)
				hxsublime_completion_hx_HxCompletion.triggerAsyncCompletion(view, ctx.options, out.showTopLevelSnippets())
			
			elif hxsublime_completion_hx_HxCompletion.supportedCompilerCompletionChar(ctx.completeChar()):
				haxe_Log.trace("supported char", _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 217 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "createNewCompletions" ))
				compBuild = hxsublime_completion_hx_HxCompletion.createCompletionBuild(ctx)
				if compBuild is not None:
					def _hx_local_0(out,err):
						hxsublime_completion_hx_HxCompletion.completionFinished(ctx, compBuild, out, err)
					hxsublime_completion_hx_HxCompletion.runCompilerCompletion(compBuild, _hx_local_0)
				
				else:
					haxe_Log.trace("couldn't create temp path && files which are neccessary for completion", _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 223 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "createNewCompletions" ))
				res = hxsublime_completion_hx_HxCompletion.cancelCompletion(view, True)
			
			else:
				def _hx_local_1():
					return hxsublime_completion_hx_HxCompletion.getToplevelCompletions(ctx)
				compResult = hxsublime_completion_hx_CompletionResult.emptyResult(ctx, _hx_local_1)
				hxsublime_completion_hx_HxCompletion.updateCompletionCache(cache, compResult)
				project.completionContext.addCompletionResult(compResult)
				res = hxsublime_completion_hx_HxCompletion.cancelCompletion(view)
				hxsublime_completion_hx_HxCompletion.triggerAsyncCompletion(view, ctx.options, compResult.showTopLevelSnippets())
			
		
	
	return res
	
hxsublime_completion_hx_HxCompletion.createNewCompletions = HxCompletion_statics_createNewCompletions
def HxCompletion_statics_createCompletionBuild(ctx):
	tmp_src = ctx.tempCompletionSrc()
	r = hxsublime_Temp.createTempPathAndFile(ctx.build(), ctx.orig_file(), tmp_src)
	tempPath = r[0]
	tempFile = r[1]
	temp_creation_success = tempPath is not None and tempFile is not None
	def _hx_local_0():
		compBuild = hxsublime_completion_hx_CompletionBuild(ctx, tempPath, tempFile)
		build = compBuild.build
		display = compBuild.display()
		macroCompletion = ctx.options.macroCompletion()
		build.setAutoCompletion(display, macroCompletion)
		if ctx.settings.showCompletionTimes(compBuild.ctx.view):
			build.setTimes()
		
		return compBuild
	
	mkBuild = _hx_local_0
	if temp_creation_success:
		return mkBuild()
	else:
		return None
	
hxsublime_completion_hx_HxCompletion.createCompletionBuild = HxCompletion_statics_createCompletionBuild
def HxCompletion_statics_runCompilerCompletion(compBuild,callback):
	startTime = python_lib_Time.time()
	ctx = compBuild.ctx
	project = ctx.project
	build = compBuild.build
	view = ctx.view
	async = ctx.settings.isAsyncCompletion()
	def _hx_local_1(out,err):
		def _hx_local_0():
			runTime = python_lib_Time.time() - startTime
			haxe_Log.trace("completion time: " + Std.string(runTime), _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 286 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "runCompilerCompletion" ))
			hxsublime_Temp.removePath(compBuild.tempPath)
			callback(out, err)
		
		run = _hx_local_0
		project.completionContext.runIfStillUpToDate(ctx.id, run)
	
	inMainThread = _hx_local_1
	def _hx_local_4(out,err):
		def _hx_local_2():
			f = inMainThread
			a1 = out
			a2 = err
			def _hx_local_3():
				return f(a1, a2)
			return _hx_local_3
		
		sublime_Sublime.set_timeout(_hx_local_2(), 2)
	
	onResult = _hx_local_4
	project.completionContext.setNewCompletion(ctx)
	haxe_Log.trace("ASYNC: " + Std.string(async), _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 304 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "runCompilerCompletion" ))
	build.run(project, view, async, onResult)
	
hxsublime_completion_hx_HxCompletion.runCompilerCompletion = HxCompletion_statics_runCompilerCompletion
def HxCompletion_statics_completionFinished(ctx,compBuild,out,err):
	ctx1 = compBuild.ctx
	tempFile = compBuild.tempFile
	cache = compBuild.cache
	project = ctx1.project
	view = ctx1.view
	def _hx_local_0():
		return hxsublime_completion_hx_HxCompletion.getToplevelCompletions(ctx1)
	compResult = hxsublime_completion_hx_HxCompletion.outputToResult(ctx1, tempFile, err, out, _hx_local_0)
	hasResults = compResult.hasResults()
	if hasResults:
		hxsublime_completion_hx_HxCompletion.updateCompletionCache(cache, compResult)
		project.completionContext.addCompletionResult(compResult)
		showTopLevelSnippets = compResult.showTopLevelSnippets()
		hxsublime_completion_hx_HxCompletion.triggerAsyncCompletion(view, ctx1.options, showTopLevelSnippets)
	
	else:
		haxe_Log.trace("ignore background completion on finished", _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 333 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "completionFinished" ))
	
hxsublime_completion_hx_HxCompletion.completionFinished = HxCompletion_statics_completionFinished
def HxCompletion_statics_hintsToSublimeCompletions(hints):
	def _hx_local_5(h):
		hintIsJustAType = __builtin__.len(h) == 1
		res = None
		if hintIsJustAType:
			res = (h[0] + " - No Completion", "${}")
		else:
			isFunctionWithoutParams = __builtin__.len(h) == 2 and h[0] == "Void"
			insert = None
			show = None
			if isFunctionWithoutParams:
				insert = ")"
				show = "Void"
			
			else:
				def _hx_local_0(p):
					_this = p.split("}")
					return "\\}".join(_this)
				
				escapeParam = _hx_local_0
				last_index = __builtin__.len(h) - 1
				params = h[0:last_index]
				show = ", ".join(params)
				if hxsublime_Settings.smartSnippetsJustCurrent():
					first = escapeParam(params[0])
					if __builtin__.len(params) == 1:
						insert = "${1:" + first + "})${0}"
					else:
						insert = "${0:" + first + "}"
				
				else:
					def _hx_local_1(listIndex):
						return Std.string(listIndex + 1)
					getSnippetIndex = _hx_local_1
					def _hx_local_2(param,index):
						return "${" + getSnippetIndex(index) + ":" + escapeParam(param) + "}"
					paramSnippet = _hx_local_2
					snippetList = None
					_g = []
					_g2 = 0
					_g1 = __builtin__.len(params)
					while _g2 < _g1:
						def _hx_local_4():
							nonlocal _g2
							_hx_local_3 = _g2
							_g2 = _g2 + 1
							return _hx_local_3
							
						
						index = _hx_local_4()
						x = paramSnippet(params[index], index)
						_g.append(x)
						__builtin__.len(_g)
						
					
					
					snippetList = _g
					
					insert = ",".join(snippetList) + ")${0}"
				
			
			res = (show, insert)
		
		return res
	
	make_hint_comp = _hx_local_5
	_g = []
	_g1 = 0
	while _g1 < len(hints):
		h = hints[_g1]
		_g1 = _g1 + 1
		x = make_hint_comp(h)
		_g.append(x)
		__builtin__.len(_g)
		
	
	
	return _g
	
	
hxsublime_completion_hx_HxCompletion.hintsToSublimeCompletions = HxCompletion_statics_hintsToSublimeCompletions
def HxCompletion_statics_combineHintsAndComps(compResult):
	all_comps = hxsublime_completion_hx_HxCompletion.hintsToSublimeCompletions(compResult.hints)
	if not compResult.ctx.options.types().hasHint() or __builtin__.len(compResult.hints) == 0:
		haxe_Log.trace("TAKE TOP LEVEL COMPS", _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 420 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "combineHintsAndComps" ))
		x = compResult.allComps()
		all_comps.extend(x)
		
	
	elif __builtin__.len(compResult.hints) == 1:
		sublime_Sublime.status_message("signature: " + "->".join(compResult.hints[0]))
	
	return all_comps
	
hxsublime_completion_hx_HxCompletion.combineHintsAndComps = HxCompletion_statics_combineHintsAndComps
def HxCompletion_statics_isIntIteratorCompletion(src,offset):
	o = offset
	s = src
	return o > 3 and s[o] == "\n" and s[o - 1] == "." and s[o - 2] == "." and s[o - 3] != "."
	
hxsublime_completion_hx_HxCompletion.isIntIteratorCompletion = HxCompletion_statics_isIntIteratorCompletion
def HxCompletion_statics_isAfterIntIterator(src,offset):
	o = offset
	s = src
	return o > 3 and s[o] == "\n" and s[o - 1] == "." and s[o - 2] == "." and s[o - 3] == "."
	
hxsublime_completion_hx_HxCompletion.isAfterIntIterator = HxCompletion_statics_isAfterIntIterator
def HxCompletion_statics_isHintCompletion(ctx):
	whitespace_re = python_lib_Re.compile("^\\s*$")
	def _hx_local_1():
		def _hx_local_0():
			str = ctx.completeChar()
			return "(,".find(str)
		
		return _hx_local_0() > -1 and python_lib_Re.match(whitespace_re, ctx.prefix) is not None
	
	return _hx_local_1()
	
hxsublime_completion_hx_HxCompletion.isHintCompletion = HxCompletion_statics_isHintCompletion
def HxCompletion_statics_isEquivalentCompletionAlreadyRunning(ctx):
	return ctx.project.completionContext.isEquivalentCompletionAlreadyRunning(ctx)
hxsublime_completion_hx_HxCompletion.isEquivalentCompletionAlreadyRunning = HxCompletion_statics_isEquivalentCompletionAlreadyRunning
def HxCompletion_statics_shouldIncludeTopLevelCompletion(ctx):
	haxe_Log.trace("complete Char: '" + ctx.completeChar() + "'", _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 469 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "shouldIncludeTopLevelCompletion" ))
	toplevel_complete = None
	def _hx_local_0():
		str = ctx.completeChar()
		return ":(,{;})".find(str)
	
	toplevel_complete = _hx_local_0() > -1 or ctx.inControlStruct() or ctx.is_new()
	haxe_Log.trace("should include: " + Std.string(toplevel_complete), _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 472 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "shouldIncludeTopLevelCompletion" ))
	return toplevel_complete
	
hxsublime_completion_hx_HxCompletion.shouldIncludeTopLevelCompletion = HxCompletion_statics_shouldIncludeTopLevelCompletion
def HxCompletion_statics_getToplevelCompletions(ctx):
	haxe_Log.trace("get top level completions", _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 481 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "getToplevelCompletions" ))
	comps = None
	if hxsublime_completion_hx_HxCompletion.shouldIncludeTopLevelCompletion(ctx):
		comps = hxsublime_completion_hx_TopLevel.getToplevelCompletionFiltered(ctx)
	else:
		comps = []
	return comps
	
hxsublime_completion_hx_HxCompletion.getToplevelCompletions = HxCompletion_statics_getToplevelCompletions
def HxCompletion_statics_createCompletionContext(project,view,offset,options,prefix):
	haxe_Log.trace("OPTIONS:" + Std.string(options), _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 502 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "createCompletionContext" ))
	if options is None:
		options = hxsublime_completion_hx_CompletionOptions(2)
	
	haxe_Log.trace(options, _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 508 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "createCompletionContext" ))
	settings = hxsublime_completion_hx_CompletionSettings(hxsublime_Settings)
	ctx = hxsublime_completion_hx_CompletionContext(view, project, offset, options, settings, prefix)
	return ctx
	
hxsublime_completion_hx_HxCompletion.createCompletionContext = HxCompletion_statics_createCompletionContext
def HxCompletion_statics_updateCompletionCache(cache,compResult):
	cache.output = compResult
	cache.input = compResult.ctx
	
hxsublime_completion_hx_HxCompletion.updateCompletionCache = HxCompletion_statics_updateCompletionCache
def HxCompletion_statics_log_completion_status(status,comps,hints):
	if status != "":
		if comps.length > 0 or hints.length > 0:
			haxe_Log.trace(status, _Hx_AnonObject(fileName = "HxCompletion.hx" ,lineNumber = 527 ,className = "hxsublime.completion.hx.HxCompletion" ,methodName = "log_completion_status" ))
		else:
			hxsublime_panel_Panels.defaultPanel().writeln(status)
	
hxsublime_completion_hx_HxCompletion.log_completion_status = HxCompletion_statics_log_completion_status
def HxCompletion_statics_outputToResult(ctx,temp_file,err,ret,retrieve_tl_comps):
	r = hxsublime_compiler_Output.getCompletionOutput(temp_file, ctx.orig_file(), err, ctx.commas())
	hints = r[0]
	comps1 = r[1]
	status = r[2]
	errors = r[3]
	comps2 = None
	_g = []
	_g1 = 0
	while _g1 < len(comps1):
		t = comps1[_g1]
		_g1 = _g1 + 1
		x = (t.hint, t.insert)
		_g.append(x)
		__builtin__.len(_g)
		
	
	
	comps2 = _g
	
	ctx.project.completionContext.setErrors(errors)
	hxsublime_completion_hx_HxCompletion.highlightErrors(errors, ctx.view)
	return hxsublime_completion_hx_CompletionResult(ret, comps2, status, hints, ctx, retrieve_tl_comps)
	
hxsublime_completion_hx_HxCompletion.outputToResult = HxCompletion_statics_outputToResult
def HxCompletion_statics_useCompletionCache(lastInput,current_input):
	return lastInput.eq(current_input)
hxsublime_completion_hx_HxCompletion.useCompletionCache = HxCompletion_statics_useCompletionCache
def HxCompletion_statics_supportedCompilerCompletionChar(char):
	return "(.,".find(char) > -1
hxsublime_completion_hx_HxCompletion.supportedCompilerCompletionChar = HxCompletion_statics_supportedCompilerCompletionChar
def HxCompletion_statics_highlightErrors(errors,view):
	regions = []
	_g = 0
	while _g < len(errors):
		e = errors[_g]
		_g = _g + 1
		l = e.line
		left = e._hx_from
		right = e.to
		a = view.text_point(l, left)
		b = view.text_point(l, right)
		x = sublime_Region(a, b)
		regions.append(x)
		
		hxsublime_panel_Panels.defaultPanel().status("Error", e.file + ":" + Std.string(l) + ": characters " + Std.string(left) + "-" + Std.string(right) + ": " + e.message)
	
	
	view.add_regions("haxe-error", regions, "invalid", "dot")
	
hxsublime_completion_hx_HxCompletion.highlightErrors = HxCompletion_statics_highlightErrors
def HxCompletion_statics_cancelCompletion(view,hideComplete = True):
	if hideComplete is None:
		hideComplete = True
	
	if hideComplete:
		view.run_command("hide_auto_complete")
	
	return [("  ...  ", "")]
	
hxsublime_completion_hx_HxCompletion.cancelCompletion = HxCompletion_statics_cancelCompletion
def HxCompletion_statics_triggerAsyncCompletion(view,options,showTopLevelSnippets = False):
	if showTopLevelSnippets is None:
		showTopLevelSnippets = False
	
	asyncOptions = options.copyAsAsync()
	def _hx_local_0():
		hxsublime_completion_hx_HxCompletion.triggerCompletion(view, asyncOptions, showTopLevelSnippets)
	runComplete = _hx_local_0
	sublime_Sublime.set_timeout(runComplete, 2)
	
hxsublime_completion_hx_HxCompletion.triggerAsyncCompletion = HxCompletion_statics_triggerAsyncCompletion
def HxCompletion_statics_triggerManualCompletion(view,options):
	hint = options.types().hasHint()
	macroComp = options.macroCompletion()
	def _hx_local_0():
		if hint and macroComp:
			view.run_command("hxsublime_commands__haxe_hint_display_macro_completion")
		elif hint:
			view.run_command("hxsublime_commands__haxe_hint_display_completion")
		elif macroComp:
			view.run_command("hxsublime_commands__haxe_display_macro_completion")
		else:
			view.run_command("hxsublime_commands__haxe_display_completion")
	runComplete = _hx_local_0
	sublime_Sublime.set_timeout(runComplete, 2)
	
hxsublime_completion_hx_HxCompletion.triggerManualCompletion = HxCompletion_statics_triggerManualCompletion


hxsublime_completion_hx_HxCompletion._hx_class = hxsublime_completion_hx_HxCompletion
hxsublime_completion_hx_HxCompletion._hx_class_name = "hxsublime.completion.hx.HxCompletion"
_hx_classes['hxsublime.completion.hx.HxCompletion'] = hxsublime_completion_hx_HxCompletion
hxsublime_completion_hx_HxCompletion._hx_fields = []
hxsublime_completion_hx_HxCompletion._hx_props = []
hxsublime_completion_hx_HxCompletion._hx_methods = []
hxsublime_completion_hx_HxCompletion._hx_statics = ["triggerCompletion","autoComplete","getAvailableAsyncCompletions","completionResultWithSmartSnippets","createNewCompletions","createCompletionBuild","runCompilerCompletion","completionFinished","hintsToSublimeCompletions","combineHintsAndComps","isIntIteratorCompletion","isAfterIntIterator","isHintCompletion","isEquivalentCompletionAlreadyRunning","shouldIncludeTopLevelCompletion","getToplevelCompletions","createCompletionContext","updateCompletionCache","log_completion_status","outputToResult","useCompletionCache","supportedCompilerCompletionChar","highlightErrors","cancelCompletion","triggerAsyncCompletion","triggerManualCompletion"]
hxsublime_completion_hx_HxCompletion._hx_interfaces = []

# print hxsublime.completion.hx.TopLevelOptions.TopLevelOptions
class hxsublime_completion_hx_TopLevelOptions:


	def __init__(self,val = 0):
		if val is None:
			val = 0
		
		self._opt = val
	
	# var _opt
	def val(self):
		return self._opt

	def set(self,val):
		self._opt = self._opt | val

	def hasTypes(self):
		return (self._opt & 1) > 0

	def hasLocals(self):
		return (self._opt & 2) > 0

	def hasKeywords(self):
		return (self._opt & 4) > 0

	def eq(self,other):
		return self._opt == other._opt







hxsublime_completion_hx_TopLevelOptions._hx_class = hxsublime_completion_hx_TopLevelOptions
hxsublime_completion_hx_TopLevelOptions._hx_class_name = "hxsublime.completion.hx.TopLevelOptions"
_hx_classes['hxsublime.completion.hx.TopLevelOptions'] = hxsublime_completion_hx_TopLevelOptions
hxsublime_completion_hx_TopLevelOptions._hx_fields = ["_opt"]
hxsublime_completion_hx_TopLevelOptions._hx_props = []
hxsublime_completion_hx_TopLevelOptions._hx_methods = ["val","set","hasTypes","hasLocals","hasKeywords","eq"]
hxsublime_completion_hx_TopLevelOptions._hx_statics = []
hxsublime_completion_hx_TopLevelOptions._hx_interfaces = []

# print hxsublime.completion.hx.Toplevel.TopLevel
class hxsublime_completion_hx_TopLevel:

	pass




hxsublime_completion_hx_TopLevel.TOP_LEVEL_KEYWORDS = [("trace\ttoplevel", "trace"), ("this\ttoplevel", "this"), ("super\ttoplevel", "super")]
def TopLevel_statics_getToplevelKeywords(ctx):
	if ctx.is_new():
		return []
	else:
		return hxsublime_completion_hx_TopLevel.TOP_LEVEL_KEYWORDS
hxsublime_completion_hx_TopLevel.getToplevelKeywords = TopLevel_statics_getToplevelKeywords
def TopLevel_statics_getBuildTarget(ctx):
	if ctx.options.macroCompletion():
		return "neko"
	else:
		return ctx.build().target().plattform
hxsublime_completion_hx_TopLevel.getBuildTarget = TopLevel_statics_getBuildTarget
def TopLevel_statics_getLocalVars(ctx):
	comps = []
	def _hx_local_0():
		p = hxsublime_tools_Regex.variables.finditer(ctx.src())
		return python_HaxeIterator(p)
	
	_it = _hx_local_0()
	while _it.hasNext():
		v = _it.next()
		x = None
		a = v.group(1) + "\tvar"
		b = v.group(1)
		x = (a, b)
		
		comps.append(x)
		__builtin__.len(comps)
		
	
	return comps
	
hxsublime_completion_hx_TopLevel.getLocalVars = TopLevel_statics_getLocalVars
def TopLevel_statics_getLocalFunctions(ctx):
	comps = []
	def _hx_local_0():
		p = hxsublime_tools_Regex.named_functions.finditer(ctx.src())
		return python_HaxeIterator(p)
	
	_it = _hx_local_0()
	while _it.hasNext():
		i = _it.next()
		f = i.group(1)
		if f != "new":
			x = (f + "\tfunction", f)
			comps.append(x)
			__builtin__.len(comps)
			
		
		
	
	return comps
	
hxsublime_completion_hx_TopLevel.getLocalFunctions = TopLevel_statics_getLocalFunctions
def TopLevel_statics_getLocalFunctionParams(ctx):
	comps = []
	_g = 0
	_g1 = None
	string = ctx.src()
	_g1 = python_lib_Re_RegexHelper.findallDynamic(hxsublime_tools_Regex.function_params, string, None, None)
	
	while _g < len(_g1):
		params_text = _g1[_g]
		_g = _g + 1
		cleaned_params_text = python_lib_Re.sub(hxsublime_tools_Regex.param_default, "", params_text)
		params_list = cleaned_params_text.split(",")
		_g2 = 0
		while _g2 < len(params_list):
			param = params_list[_g2]
			_g2 = _g2 + 1
			a = param.strip(None)
			if StringTools.startsWith(a, "?"):
				a = python_Tools.substr(a, 1, None)
			
			idx = a.find(":")
			if idx > -1:
				a = python_Tools.substring(a, 0, idx)
			
			idx1 = a.find("=")
			if idx1 > -1:
				a = python_Tools.substring(a, 0, idx1)
			
			a = a.strip(None)
			cm = (a + "\tvar", a)
			if not Lambda.has(comps, cm):
				comps.append(cm)
				__builtin__.len(comps)
			
			
		
		
	
	
	return comps
	
hxsublime_completion_hx_TopLevel.getLocalFunctionParams = TopLevel_statics_getLocalFunctionParams
def TopLevel_statics_getLocalVarsAndFunctions(ctx):
	comps = []
	x = hxsublime_completion_hx_TopLevel.getLocalVars(ctx)
	comps.extend(x)
	
	x = hxsublime_completion_hx_TopLevel.getLocalFunctions(ctx)
	comps.extend(x)
	
	x = hxsublime_completion_hx_TopLevel.getLocalFunctionParams(ctx)
	comps.extend(x)
	
	return comps
	
hxsublime_completion_hx_TopLevel.getLocalVarsAndFunctions = TopLevel_statics_getLocalVarsAndFunctions
def TopLevel_statics_getImports(ctx):
	imports = None
	string = ctx.src()
	imports = python_lib_Re_RegexHelper.findallDynamic(hxsublime_tools_Regex.import_line, string, None, None)
	
	imported = []
	_g = 0
	while _g < len(imports):
		i = imports[_g]
		_g = _g + 1
		imp = i[1]
		imported.append(imp)
		__builtin__.len(imported)
		
	
	
	return imported
	
hxsublime_completion_hx_TopLevel.getImports = TopLevel_statics_getImports
def TopLevel_statics_getUsings(ctx):
	usings = None
	string = ctx.src()
	usings = python_lib_Re_RegexHelper.findallDynamic(hxsublime_tools_Regex.using_line, string, None, None)
	
	used = []
	_g = 0
	while _g < len(usings):
		i = usings[_g]
		_g = _g + 1
		imp = i[1]
		used.append(imp)
		__builtin__.len(used)
		
	
	
	return used
	
hxsublime_completion_hx_TopLevel.getUsings = TopLevel_statics_getUsings
def TopLevel_statics_getImportsAndUsings(ctx):
	res = hxsublime_completion_hx_TopLevel.getImports(ctx)
	a = hxsublime_completion_hx_TopLevel.getUsings(ctx)
	res = res + a
	
	return res
	
hxsublime_completion_hx_TopLevel.getImportsAndUsings = TopLevel_statics_getImportsAndUsings
def TopLevel_statics_haxeTypeAsCompletion(type):
	insert = type.full_pack_with_optional_module_type_and_enum_value
	display = type.type_name_with_optional_enum_value
	display = display + "\t" + type.get_type_hint
	return (display, insert)
	
hxsublime_completion_hx_TopLevel.haxeTypeAsCompletion = TopLevel_statics_haxeTypeAsCompletion
def TopLevel_statics_getTypeComps(ctx,bundle,imported):
	build_target = hxsublime_completion_hx_TopLevel.getBuildTarget(ctx)
	comps = []
	startTime = python_lib_Time.time()
	allTypes = bundle.allTypes()
	runTime0 = python_lib_Time.time() - startTime
	_g = 0
	while _g < len(allTypes):
		t = allTypes[_g]
		_g = _g + 1
		if ctx.build().isTypeAvailable(t):
			snippets = t.toSnippets(imported, ctx.orig_file())
			comps.extend(snippets)
		
		
	
	
	runTime1 = python_lib_Time.time() - startTime
	_g = 0
	_g1 = bundle.packs()
	while _g < len(_g1):
		p = _g1[_g]
		_g = _g + 1
		if ctx.build().isPackAvailable(p):
			cm = (p + "\tpackage", p)
			comps.append(cm)
			__builtin__.len(comps)
			
		
		
	
	
	runTime2 = python_lib_Time.time() - startTime
	haxe_Log.trace("get_type_comps time0" + Std.string(runTime0), _Hx_AnonObject(fileName = "Toplevel.hx" ,lineNumber = 170 ,className = "hxsublime.completion.hx.TopLevel" ,methodName = "getTypeComps" ))
	haxe_Log.trace("get_type_comps time1" + Std.string(runTime1), _Hx_AnonObject(fileName = "Toplevel.hx" ,lineNumber = 171 ,className = "hxsublime.completion.hx.TopLevel" ,methodName = "getTypeComps" ))
	haxe_Log.trace("get_type_comps time2" + Std.string(runTime2), _Hx_AnonObject(fileName = "Toplevel.hx" ,lineNumber = 172 ,className = "hxsublime.completion.hx.TopLevel" ,methodName = "getTypeComps" ))
	return comps
	
hxsublime_completion_hx_TopLevel.getTypeComps = TopLevel_statics_getTypeComps
def TopLevel_statics_getToplevelCompletion(ctx):
	startTime = python_lib_Time.time()
	comps = []
	if not ctx.is_new():
		x = hxsublime_completion_hx_TopLevel.getToplevelKeywords(ctx)
		comps.extend(x)
		
		x = hxsublime_completion_hx_TopLevel.getLocalVarsAndFunctions(ctx)
		comps.extend(x)
		
	
	
	imported = hxsublime_completion_hx_TopLevel.getImportsAndUsings(ctx)
	runTime1 = python_lib_Time.time() - startTime
	build_bundle = ctx.build().getTypes()
	runTime2 = python_lib_Time.time() - startTime
	std_bundle = ctx.build().stdBundle()
	def _hx_local_0(t):
		return not t.is_private or t._file == ctx.orig_file()
	filterPrivates = _hx_local_0
	merged_bundle = std_bundle.merge(build_bundle).filter(filterPrivates)
	runTime3 = python_lib_Time.time() - startTime
	comps1 = hxsublime_completion_hx_TopLevel.getTypeComps(ctx, merged_bundle, imported)
	runTime4 = python_lib_Time.time() - startTime
	comps.extend(comps1)
	runTime = python_lib_Time.time() - startTime
	haxe_Log.trace("TOP LEVEL COMPLETION TIME1:" + Std.string(runTime1), _Hx_AnonObject(fileName = "Toplevel.hx" ,lineNumber = 221 ,className = "hxsublime.completion.hx.TopLevel" ,methodName = "getToplevelCompletion" ))
	haxe_Log.trace("TOP LEVEL COMPLETION TIME2:" + Std.string(runTime2), _Hx_AnonObject(fileName = "Toplevel.hx" ,lineNumber = 222 ,className = "hxsublime.completion.hx.TopLevel" ,methodName = "getToplevelCompletion" ))
	haxe_Log.trace("TOP LEVEL COMPLETION TIME3:" + Std.string(runTime3), _Hx_AnonObject(fileName = "Toplevel.hx" ,lineNumber = 223 ,className = "hxsublime.completion.hx.TopLevel" ,methodName = "getToplevelCompletion" ))
	haxe_Log.trace("TOP LEVEL COMPLETION TIME4:" + Std.string(runTime4), _Hx_AnonObject(fileName = "Toplevel.hx" ,lineNumber = 224 ,className = "hxsublime.completion.hx.TopLevel" ,methodName = "getToplevelCompletion" ))
	haxe_Log.trace("TOP LEVEL COMPLETION TIME END:" + Std.string(runTime), _Hx_AnonObject(fileName = "Toplevel.hx" ,lineNumber = 225 ,className = "hxsublime.completion.hx.TopLevel" ,methodName = "getToplevelCompletion" ))
	return comps
	
hxsublime_completion_hx_TopLevel.getToplevelCompletion = TopLevel_statics_getToplevelCompletion
def TopLevel_statics_getToplevelCompletionFiltered(ctx):
	comps = hxsublime_completion_hx_TopLevel.getToplevelCompletion(ctx)
	haxe_Log.trace(ctx.prefix, _Hx_AnonObject(fileName = "Toplevel.hx" ,lineNumber = 234 ,className = "hxsublime.completion.hx.TopLevel" ,methodName = "getToplevelCompletionFiltered" ))
	return hxsublime_completion_hx_TopLevel.filterTopLevelCompletions(ctx.prefix, comps)
	
hxsublime_completion_hx_TopLevel.getToplevelCompletionFiltered = TopLevel_statics_getToplevelCompletionFiltered
def TopLevel_statics_filterTopLevelCompletions(prefix,all_comps):
	comps = []
	haxe_Log.trace("c : " + prefix, _Hx_AnonObject(fileName = "Toplevel.hx" ,lineNumber = 242 ,className = "hxsublime.completion.hx.TopLevel" ,methodName = "filterTopLevelCompletions" ))
	if __builtin__.len(prefix) == 0:
		comps = __builtin__.list(all_comps)
	else:
		test = []
		_g1 = 0
		_g = __builtin__.len(prefix)
		while _g1 < _g:
			def _hx_local_1():
				nonlocal _g1
				_hx_local_0 = _g1
				_g1 = _g1 + 1
				return _hx_local_0
				
			
			i = _hx_local_1()
			c = prefix[i]
			isLower = "abcdefghijklmnopqrstuvwxyz".find(c) > -1
			isUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(c) > -1
			is_digit = "0123456789".find(c) > -1
			is_special = "$_#".find(c) > -1
			if isLower or isUpper or is_digit or is_special:
				offsetUpper = c.upper()
				offsetLower = c.lower()
				test.append(offsetLower)
				__builtin__.len(test)
				
			
			
		
		
		_g = 0
		while _g < len(all_comps):
			c = all_comps[_g]
			_g = _g + 1
			found = True
			id = None
			_this = c[1]
			id = _this.lower()
			
			oldId = id
			_g1 = 0
			while _g1 < len(test):
				cur = test[_g1]
				_g1 = _g1 + 1
				if found:
					index = id.find(cur)
					if index > -1:
						id = python_Tools.substr(id, index + 1, None)
					else:
						found = False
						break
					
				
				
			
			
			if found:
				comps.append(c)
				__builtin__.len(comps)
			
			
		
		
	
	haxe_Log.trace("number of top level completions (all: " + Std.string(__builtin__.len(all_comps)) + ", filtered: " + Std.string(__builtin__.len(comps)) + ")", _Hx_AnonObject(fileName = "Toplevel.hx" ,lineNumber = 303 ,className = "hxsublime.completion.hx.TopLevel" ,methodName = "filterTopLevelCompletions" ))
	return comps
	
hxsublime_completion_hx_TopLevel.filterTopLevelCompletions = TopLevel_statics_filterTopLevelCompletions


hxsublime_completion_hx_TopLevel._hx_class = hxsublime_completion_hx_TopLevel
hxsublime_completion_hx_TopLevel._hx_class_name = "hxsublime.completion.hx.TopLevel"
_hx_classes['hxsublime.completion.hx.TopLevel'] = hxsublime_completion_hx_TopLevel
hxsublime_completion_hx_TopLevel._hx_fields = []
hxsublime_completion_hx_TopLevel._hx_props = []
hxsublime_completion_hx_TopLevel._hx_methods = []
hxsublime_completion_hx_TopLevel._hx_statics = ["TOP_LEVEL_KEYWORDS","getToplevelKeywords","getBuildTarget","getLocalVars","getLocalFunctions","getLocalFunctionParams","getLocalVarsAndFunctions","getImports","getUsings","getImportsAndUsings","haxeTypeAsCompletion","getTypeComps","getToplevelCompletion","getToplevelCompletionFiltered","filterTopLevelCompletions"]
hxsublime_completion_hx_TopLevel._hx_interfaces = []

# print hxsublime.completion.hxml.HxmlCompletion.HxmlCompletion
class hxsublime_completion_hxml_HxmlCompletion:

	pass




hxsublime_completion_hxml_HxmlCompletion.libFlag = python_lib_Re.compile("-lib\\s+(.*?)")
def HxmlCompletion_statics_autoComplete(project,view,offset,prefix):
	src = view.substr(sublime_Region(0, offset))
	currentLine = None
	startIndex = src.find("\n") + 1
	currentLine = python_Tools.substring(src, startIndex, offset)
	
	m = hxsublime_completion_hxml_HxmlCompletion.libFlag.match(currentLine)
	if m is not None:
		return project.haxelibManager().getCompletions()
	else:
		return []
	
hxsublime_completion_hxml_HxmlCompletion.autoComplete = HxmlCompletion_statics_autoComplete


hxsublime_completion_hxml_HxmlCompletion._hx_class = hxsublime_completion_hxml_HxmlCompletion
hxsublime_completion_hxml_HxmlCompletion._hx_class_name = "hxsublime.completion.hxml.HxmlCompletion"
_hx_classes['hxsublime.completion.hxml.HxmlCompletion'] = hxsublime_completion_hxml_HxmlCompletion
hxsublime_completion_hxml_HxmlCompletion._hx_fields = []
hxsublime_completion_hxml_HxmlCompletion._hx_props = []
hxsublime_completion_hxml_HxmlCompletion._hx_methods = []
hxsublime_completion_hxml_HxmlCompletion._hx_statics = ["libFlag","autoComplete"]
hxsublime_completion_hxml_HxmlCompletion._hx_interfaces = []

# print hxsublime.completion.hxsl.HxslCompletion.HxslCompletion
class hxsublime_completion_hxsl_HxslCompletion:

	pass




def HxslCompletion_statics_autoComplete(project,view,offset,prefix):
	comps = []
	_g = 0
	_g1 = ["Float", "Float2", "Float3", "Float4", "Matrix", "M44", "M33", "M34", "M43", "Texture", "CubeTexture", "Int", "Color", "include"]
	while _g < len(_g1):
		t = _g1[_g]
		_g = _g + 1
		x = (t, "hxsl Type")
		comps.append(x)
		__builtin__.len(comps)
		
		
	
	
	return comps
	
hxsublime_completion_hxsl_HxslCompletion.autoComplete = HxslCompletion_statics_autoComplete


hxsublime_completion_hxsl_HxslCompletion._hx_class = hxsublime_completion_hxsl_HxslCompletion
hxsublime_completion_hxsl_HxslCompletion._hx_class_name = "hxsublime.completion.hxsl.HxslCompletion"
_hx_classes['hxsublime.completion.hxsl.HxslCompletion'] = hxsublime_completion_hxsl_HxslCompletion
hxsublime_completion_hxsl_HxslCompletion._hx_fields = []
hxsublime_completion_hxsl_HxslCompletion._hx_props = []
hxsublime_completion_hxsl_HxslCompletion._hx_methods = []
hxsublime_completion_hxsl_HxslCompletion._hx_statics = ["autoComplete"]
hxsublime_completion_hxsl_HxslCompletion._hx_interfaces = []

# print hxsublime.panel.Panels.PanelCloseListener
class hxsublime_panel_PanelCloseListener(sublime_EventListener):

	def on_close(self,view):
		win = view.window()
		if win is None:
			win = sublime_Sublime.active_window()
		
		win_id = win.id()
		view_id = view.id()
		if python_lib_DictImpl.hasKey(hxsublime_panel_Panels._slidePanels.h, win_id):
			panel = hxsublime_panel_Panels.slidePanel(win)
			if panel.outputView is not None and view_id == panel.outputView.id():
				panel.outputView = None
			
		
		
		panel_win_id = view.settings().get("haxe_panel_win_id")
		if panel_win_id is not None:
			_g = 0
			_g1 = [hxsublime_panel_Panels._tabPanels, hxsublime_panel_Panels._debugPanels]
			while _g < len(_g1):
				p = _g1[_g]
				_g = _g + 1
				panel = p.getOrDefault(panel_win_id, None)
				if panel is not None and panel.outputView is not None and view_id == panel.outputViewId:
					haxe_Log.trace("panel safely removed", _Hx_AnonObject(fileName = "Panels.hx" ,lineNumber = 43 ,className = "hxsublime.panel.PanelCloseListener" ,methodName = "on_close" ))
					panel.outputView = None
					panel.outputViewId = None
				
				
			
		
		
	







hxsublime_panel_PanelCloseListener._hx_class = hxsublime_panel_PanelCloseListener
hxsublime_panel_PanelCloseListener._hx_class_name = "hxsublime.panel.PanelCloseListener"
_hx_classes['hxsublime.panel.PanelCloseListener'] = hxsublime_panel_PanelCloseListener
hxsublime_panel_PanelCloseListener._hx_fields = []
hxsublime_panel_PanelCloseListener._hx_props = []
hxsublime_panel_PanelCloseListener._hx_methods = ["on_close"]
hxsublime_panel_PanelCloseListener._hx_statics = []
hxsublime_panel_PanelCloseListener._hx_interfaces = []
hxsublime_panel_PanelCloseListener._hx_super = sublime_EventListener

# print hxsublime.tools.Cache.Cache
class hxsublime_tools_Cache:


	def __init__(self,data,cache_time = -1):
		if cache_time is None:
			cache_time = -1
		
		self.data = data
		self.cache_time = cache_time
		self.time_driven = cache_time != -1
	
	# var time_driven
	# var cache_time
	# var data
	def insert(self,id,value):
		self.data.set(id, _Hx_AnonObject(time = python_lib_Time.time() ,val = value ))

	def exists(self,id):
		return self.getOrDefault(id, None) is not None

	def getOrInsert(self,id,creator):
		res = None
		if self.data.exists(id):
			res = self.unsafeGetVal(id)
		else:
			res = creator()
			self.insert(id, res)
		
		return res
	

	def unsafeGetVal(self,id):
		return self.data.get(id).val

	def isCacheInvalid(self,id):
		return not self.isCacheValid(id)

	def isCacheValid(self,id):
		now = python_lib_Time.time()
		return now - self.data.get(id).time <= self.cache_time
	

	def getOrDefault(self,id,defaultVal = None):
		if defaultVal is None:
			defaultVal = None
		
		res = defaultVal
		if self.data.exists(id):
			if self.time_driven and self.isCacheInvalid(id):
				self.data.remove(id)
			else:
				res = self.unsafeGetVal(id)
		
		return res
	

	def getAndDelete(self,id,defaultVal = None):
		if defaultVal is None:
			defaultVal = None
		
		val = defaultVal
		if self.data.exists(id):
			if not self.time_driven or self.isCacheValid(id):
				val = self.unsafeGetVal(id)
			
			self.data.remove(id)
		
		
		return val
	

	def delete(self,id):
		if self.data.exists(id):
			self.data.remove(id)
		







hxsublime_tools_Cache._hx_class = hxsublime_tools_Cache
hxsublime_tools_Cache._hx_class_name = "hxsublime.tools.Cache"
_hx_classes['hxsublime.tools.Cache'] = hxsublime_tools_Cache
hxsublime_tools_Cache._hx_fields = ["time_driven","cache_time","data"]
hxsublime_tools_Cache._hx_props = []
hxsublime_tools_Cache._hx_methods = ["insert","exists","getOrInsert","unsafeGetVal","isCacheInvalid","isCacheValid","getOrDefault","getAndDelete","delete"]
hxsublime_tools_Cache._hx_statics = []
hxsublime_tools_Cache._hx_interfaces = []

# print hxsublime.panel.Panels.Panels
class hxsublime_panel_Panels:

	pass




hxsublime_panel_Panels._tabPanels = hxsublime_tools_Cache(haxe_ds_IntMap())
hxsublime_panel_Panels._debugPanels = hxsublime_tools_Cache(haxe_ds_IntMap())
hxsublime_panel_Panels._slidePanels = haxe_ds_IntMap()
def Panels_statics_tabPanel(win = None):
	if win is None:
		win = None
	
	if win is None:
		win = sublime_Sublime.active_window()
	
	def _hx_local_1():
		def _hx_local_0():
			return hxsublime_panel_TabPanel(win, "Haxe Output")
		return hxsublime_panel_Panels._tabPanels.getOrInsert(win.id(), _hx_local_0)
	
	return _hx_local_1()
	
hxsublime_panel_Panels.tabPanel = Panels_statics_tabPanel
def Panels_statics_debugPanel(win = None):
	if win is None:
		win = None
	
	if win is None:
		win = sublime_Sublime.active_window()
	
	def _hx_local_1():
		def _hx_local_0():
			return hxsublime_panel_TabPanel(win, "Haxe Plugin Debug Panel")
		return hxsublime_panel_Panels._debugPanels.getOrInsert(win.id(), _hx_local_0)
	
	return _hx_local_1()
	
hxsublime_panel_Panels.debugPanel = Panels_statics_debugPanel
def Panels_statics_defaultPanel(win = None):
	if win is None:
		win = None
	
	if hxsublime_Settings.useSlidePanel():
		return hxsublime_panel_Panels.slidePanel(win)
	else:
		return hxsublime_panel_Panels.tabPanel(win)
	
hxsublime_panel_Panels.defaultPanel = Panels_statics_defaultPanel
def Panels_statics_slidePanel(win = None):
	if win is None:
		win = None
	
	if win is None:
		win = sublime_Sublime.active_window()
	
	win_id = win.id()
	if not python_lib_DictImpl.hasKey(hxsublime_panel_Panels._slidePanels.h, win_id):
		hxsublime_panel_Panels._slidePanels.set(win_id, hxsublime_panel_SlidePanel(win))
	
	return hxsublime_panel_Panels._slidePanels.h.get(win_id, None)
	
hxsublime_panel_Panels.slidePanel = Panels_statics_slidePanel


hxsublime_panel_Panels._hx_class = hxsublime_panel_Panels
hxsublime_panel_Panels._hx_class_name = "hxsublime.panel.Panels"
_hx_classes['hxsublime.panel.Panels'] = hxsublime_panel_Panels
hxsublime_panel_Panels._hx_fields = []
hxsublime_panel_Panels._hx_props = []
hxsublime_panel_Panels._hx_methods = []
hxsublime_panel_Panels._hx_statics = ["_tabPanels","_debugPanels","_slidePanels","tabPanel","debugPanel","defaultPanel","slidePanel"]
hxsublime_panel_Panels._hx_interfaces = []

# print hxsublime.panel.SlidePanel.SlidePanel
class hxsublime_panel_SlidePanel:


	def __init__(self,win):
		self.win = win
		self.outputView = None
	
	# var win
	# var outputView
	# var outputViewId
	def clear(self):
		self.outputView = self.win.create_output_panel("haxe")

	def write(self,text,scope = None,show_timestamp = True):
		if scope is None:
			scope = None
		
		if show_timestamp is None:
			show_timestamp = True
		
		win = self.win
		if self.outputView is None:
			self.outputView = win.create_output_panel("haxe")
		
		self.outputView.settings().set("result_file_regex", hxsublime_panel_Tools.haxeFileRegex())
		win.create_output_panel("haxe")
		panel = self.outputView
		if show_timestamp:
			text = hxsublime_panel_Tools.timestampMsg(text)
		
		def _hx_local_0():
			x = _Hx_AnonObject(panel = "output.haxe" )
			def _hx_local_2():
				def _hx_local_1():
					d = python_lib_Dict()
					_g = 0
					_g1 = Reflect.fields(x)
					while _g < len(_g1):
						f = _g1[_g]
						_g = _g + 1
						val = Reflect.field(x, f)
						python_lib_DictImpl.set(d, f, val)
						
					
					
					return d
				
				return _hx_local_1()
			
			return _hx_local_2()
		
		win.run_command("show_panel", _hx_local_0())
		def _hx_local_3(v,edit):
			region = sublime_Region(v.size(), v.size() + __builtin__.len(text))
			v.insert(edit, v.size(), text)
			if scope is not None:
				icon = "dot"
				key = "haxe-" + scope
				regions = v.get_regions(key)
				regions.append(region)
				__builtin__.len(regions)
				
				v.add_regions(key, regions, scope, icon)
			
			
			v.sel().clear()
			v.sel().add(sublime_Region(0, 0))
		
		do_edit = _hx_local_3
		hxsublime_tools_ViewTools.asyncEdit(panel, do_edit)
		return panel
	

	def writeln(self,msg,scope = None,show_timestamp = True):
		if scope is None:
			scope = None
		
		if show_timestamp is None:
			show_timestamp = True
		
		if hxsublime_panel_Tools.isValidMessage(msg):
			self.write(msg + "\n", scope, show_timestamp)
		
	

	def status(self,title,msg):
		if hxsublime_panel_Tools.isValidMessage(msg):
			self.writeln(title + ": " + msg)
		







hxsublime_panel_SlidePanel._hx_class = hxsublime_panel_SlidePanel
hxsublime_panel_SlidePanel._hx_class_name = "hxsublime.panel.SlidePanel"
_hx_classes['hxsublime.panel.SlidePanel'] = hxsublime_panel_SlidePanel
hxsublime_panel_SlidePanel._hx_fields = ["win","outputView","outputViewId"]
hxsublime_panel_SlidePanel._hx_props = []
hxsublime_panel_SlidePanel._hx_methods = ["clear","write","writeln","status"]
hxsublime_panel_SlidePanel._hx_statics = []
hxsublime_panel_SlidePanel._hx_interfaces = []

# print hxsublime.panel.TabPanel.TabPanel
class hxsublime_panel_TabPanel:


	def __init__(self,win,panel_name = "Haxe Output",panel_syntax = "Packages/Haxe/Haxe.tmLanguage"):
		if panel_name is None:
			panel_name = "Haxe Output"
		
		if panel_syntax is None:
			panel_syntax = "Packages/Haxe/Haxe.tmLanguage"
		
		self.win = win
		self.outputView = None
		self.outputViewId = None
		self.all = []
		self.panel_name = panel_name
		self.panel_syntax = panel_syntax
	
	# var win
	# var all
	# var panel_name
	# var panel_syntax
	# var outputView
	# var outputViewId
	def clear(self):
		None

	def write(self,msg,scope = None,showTimestamp = True):
		if scope is None:
			scope = None
		
		if showTimestamp is None:
			showTimestamp = True
		
		_g = self
		def _hx_local_3():
			max = None
			x = None
			a = __builtin__.len(_g.all)
			x = __builtin__.min(a, 300)
			
			max = int(x)
			
			_g1 = []
			_g2 = 0
			while _g2 < max:
				def _hx_local_1():
					nonlocal _g2
					_hx_local_0 = _g2
					_g2 = _g2 + 1
					return _hx_local_0
					
				
				i = _hx_local_1()
				_g1.append(_g.all[i])
				__builtin__.len(_g1)
			
			
			_g.all = _g1
			
			msg1 = None
			if showTimestamp:
				msg1 = hxsublime_panel_Tools.timestampMsg(msg)
			else:
				msg1 = msg
			if hxsublime_panel_Tools.isValidMessage(msg):
				_g.all = [msg1] + _g.all
				v = _g.outputView
				if v is None:
					v = hxsublime_tools_ViewTools.findViewByName(_g.panel_name)
					if v is None:
						v = hxsublime_panel_TabPanel.makeTabPanel(_g.win, _g.panel_name, _g.panel_syntax)
						hxsublime_tools_ViewTools.replaceContent(v, "".join(_g.all))
					
					
					_g.outputView = v
					_g.outputViewId = v.id()
				
				
				if v is not None:
					def _hx_local_2(v1,edit):
						v1.insert(edit, 0, msg1)
					do_edit = _hx_local_2
					hxsublime_tools_ViewTools.asyncEdit(v, do_edit)
				
				
			
			
		
		f = _hx_local_3
		sublime_Sublime.set_timeout(f, 40)
	

	def writeln(self,msg,scope = None,showTimestamp = True):
		if scope is None:
			scope = None
		
		if showTimestamp is None:
			showTimestamp = True
		
		self.write(msg + "\n")
	

	def status(self,title,msg):
		if hxsublime_panel_Tools.isValidMessage(msg):
			self.writeln(title + ": " + msg)
		





def TabPanel_statics_makeTabPanel(win,name,syntax):
	active = win.active_view()
	v = win.new_file()
	v.set_name(name)
	v.settings().set("word_wrap", True)
	v.settings().set("result_file_regex", hxsublime_panel_Tools.haxeFileRegex())
	v.settings().set("haxe_panel_win_id", win.id())
	v.set_scratch(True)
	v.set_syntax_file(syntax)
	last_group = win.num_groups() - 1
	win.set_view_index(v, last_group, 0)
	win.focus_view(active)
	return v
	
hxsublime_panel_TabPanel.makeTabPanel = TabPanel_statics_makeTabPanel


hxsublime_panel_TabPanel._hx_class = hxsublime_panel_TabPanel
hxsublime_panel_TabPanel._hx_class_name = "hxsublime.panel.TabPanel"
_hx_classes['hxsublime.panel.TabPanel'] = hxsublime_panel_TabPanel
hxsublime_panel_TabPanel._hx_fields = ["win","all","panel_name","panel_syntax","outputView","outputViewId"]
hxsublime_panel_TabPanel._hx_props = []
hxsublime_panel_TabPanel._hx_methods = ["clear","write","writeln","status"]
hxsublime_panel_TabPanel._hx_statics = ["makeTabPanel"]
hxsublime_panel_TabPanel._hx_interfaces = []

# print hxsublime.panel.Tools.Tools
class hxsublime_panel_Tools:

	pass




def Tools_statics_haxeFileRegex():
	return "^[0-9]{2}:[0-9]{2}:[0-9]{2}[ ]Error:[ ]" + python_Tools.substr(hxsublime_project_Tools.haxeFileRegex, 1, None)
hxsublime_panel_Tools.haxeFileRegex = Tools_statics_haxeFileRegex
def Tools_statics_timestampMsg(msg):
	return python_lib_datetime_DateTime.now().strftime("%H:%M:%S") + " " + msg
hxsublime_panel_Tools.timestampMsg = Tools_statics_timestampMsg
def Tools_statics_isValidMessage(msg):
	return msg is not None and msg != "" and msg != "\n"
hxsublime_panel_Tools.isValidMessage = Tools_statics_isValidMessage


hxsublime_panel_Tools._hx_class = hxsublime_panel_Tools
hxsublime_panel_Tools._hx_class_name = "hxsublime.panel.Tools"
_hx_classes['hxsublime.panel.Tools'] = hxsublime_panel_Tools
hxsublime_panel_Tools._hx_fields = []
hxsublime_panel_Tools._hx_props = []
hxsublime_panel_Tools._hx_methods = []
hxsublime_panel_Tools._hx_statics = ["haxeFileRegex","timestampMsg","isValidMessage"]
hxsublime_panel_Tools._hx_interfaces = []

# print hxsublime.project.CompletionState.ProjectCompletionState
class hxsublime_project_ProjectCompletionState:


	def __init__(self):
		self.running = hxsublime_tools_Cache(haxe_ds_IntMap())
		self.trigger = hxsublime_tools_Cache(haxe_ds_IntMap(), 1000)
		self.currentId = None
		self.errors = []
		self.async = hxsublime_tools_Cache(haxe_ds_IntMap(), 1000)
		self.current = _Hx_AnonObject(input = None ,output = None )
	
	# var running
	# var trigger
	# var currentId
	# var errors
	# var async
	# var current
	def addCompletionResult(self,compResult):
		self.async.insert(compResult.ctx.view_id, compResult)

	def isEquivalentCompletionAlreadyRunning(self,ctx):
		complete_offset = ctx.complete_offset
		view_id = ctx.view_id
		last_completion_id = self.currentId
		running_completion = self.running.getOrDefault(last_completion_id, None)
		return running_completion is not None and running_completion[0] == complete_offset() and running_completion[1] == view_id
	

	def runIfStillUpToDate(self,comp_id,run):
		self.running.delete(comp_id)
		if self.currentId == comp_id:
			run()
		
	

	def setNewCompletion(self,ctx):
		def _hx_local_0():
			a = ctx.complete_offset()
			return (a, ctx.view_id)
		
		self.running.insert(ctx.id, _hx_local_0())
		self.currentId = ctx.id
		self.setErrors([])
	

	def setTrigger(self,view,options):
		haxe_Log.trace("SET TRIGGER", _Hx_AnonObject(fileName = "CompletionState.hx" ,lineNumber = 81 ,className = "hxsublime.project.ProjectCompletionState" ,methodName = "setTrigger" ))
		self.trigger.insert(view.id(), options)
	

	def clearCompletion(self):
		self.current = _Hx_AnonObject(input = None ,output = None )

	def setErrors(self,errors):
		self.errors = errors

	def getAndDeleteTrigger(self,view):
		return self.trigger.getAndDelete(view.id(), None)

	def getAndDeleteAsync(self,view):
		return self.async.getAndDelete(view.id(), None)

	def getAsync(self,view):
		return self.async.getOrDefault(view.id(), None)

	def deleteAsync(self,view):
		return self.async.delete(view.id())







hxsublime_project_ProjectCompletionState._hx_class = hxsublime_project_ProjectCompletionState
hxsublime_project_ProjectCompletionState._hx_class_name = "hxsublime.project.ProjectCompletionState"
_hx_classes['hxsublime.project.ProjectCompletionState'] = hxsublime_project_ProjectCompletionState
hxsublime_project_ProjectCompletionState._hx_fields = ["running","trigger","currentId","errors","async","current"]
hxsublime_project_ProjectCompletionState._hx_props = []
hxsublime_project_ProjectCompletionState._hx_methods = ["addCompletionResult","isEquivalentCompletionAlreadyRunning","runIfStillUpToDate","setNewCompletion","setTrigger","clearCompletion","setErrors","getAndDeleteTrigger","getAndDeleteAsync","getAsync","deleteAsync"]
hxsublime_project_ProjectCompletionState._hx_statics = []
hxsublime_project_ProjectCompletionState._hx_interfaces = []

class hxsublime_project_BuildType(_Hx_Enum):
	def __init__(self, t, i, p): 
		super(hxsublime_project_BuildType,self).__init__(t, i, p)


hxsublime_project_BuildType.Build = hxsublime_project_BuildType("Build", 1, list())

hxsublime_project_BuildType.Check = hxsublime_project_BuildType("Check", 2, list())

hxsublime_project_BuildType.Run = hxsublime_project_BuildType("Run", 0, list())
hxsublime_project_BuildType._hx_constructs = ["Build","Check","Run"]
hxsublime_project_BuildType._hx_class = hxsublime_project_BuildType
hxsublime_project_BuildType._hx_class_name = "hxsublime.project.BuildType"
_hx_classes['hxsublime.project.BuildType'] = hxsublime_project_BuildType

# print hxsublime.project.Project.Project
class hxsublime_project_Project:


	def __init__(self,id,file,win_id,server_port):
		self.completionContext = hxsublime_project_ProjectCompletionState()
		self._haxelibManager = hxsublime_HaxeLibManager(self)
		self._currentBuild = None
		self._selectingBuild = False
		self.builds = []
		self.winId = win_id
		self.server = hxsublime_compiler_Server(server_port)
		self._projectFile = file
		self._projectId = id
		if self._projectFile is not None:
			self._projectPath = python_lib_os_Path.normpath(python_lib_os_Path.dirname(self._projectFile))
		else:
			self._projectPath = None
		self.updateCompilerInfo()
	
	# var _haxelibManager
	# var _currentBuild
	# var _selectingBuild
	# var _projectFile
	# var _projectId
	# var _projectPath
	# var _stdBundle
	# var _stdPaths
	# var _serverMode
	# var completionContext
	# var builds
	# var winId
	# var server
	def haxelibManager(self):
		return self._haxelibManager

	def projectDir(self,defaultVal):
		if self._projectPath is not None:
			return self._projectPath
		else:
			return defaultVal

	def nmeExec(self,view = None):
		if view is None:
			view = None
		
		return [hxsublime_Settings.haxelibExec(), "run", "nme"]
	

	def openflExec(self,view = None):
		if view is None:
			view = None
		
		return [hxsublime_Settings.haxelibExec(), "run", "openfl"]
	

	def haxelibExec(self,view = None):
		if view is None:
			view = None
		
		return [hxsublime_Settings.haxelibExec()]
	

	def haxeExec(self,view = None):
		if view is None:
			view = None
		
		_hx_exec = hxsublime_Settings.haxeExec(view)
		if not python_lib_os_Path.isabs(_hx_exec) and _hx_exec != "haxe":
			cwd = self.projectDir(".")
			def _hx_local_0():
				_this = python_lib_os_Path.join(cwd, hxsublime_Settings.haxeExec(view)).split("/")
				return python_lib_Os.sep.join(_this)
			
			_hx_exec = python_lib_os_Path.normpath(_hx_local_0())
		
		
		return [_hx_exec]
	

	def haxeEnv(self,view = None):
		if view is None:
			view = None
		
		return hxsublime_project_Project.haxeBuildEnv(self.projectDir("."))
	

	def startServer(self,view):
		cwd = self.projectDir(".")
		haxe_exec = self.haxeExec(view)[0]
		env = self.haxeEnv()
		self.server.start(haxe_exec, cwd, env)
	

	def restartServer(self,view):
		def _hx_local_0():
			f = self.startServer
			a1 = view
			def _hx_local_1():
				return f(a1)
			return _hx_local_1
		
		self.server.stop(_hx_local_0())
	

	def isServerMode(self):
		return self._serverMode and hxsublime_Settings.useHaxeServermode()

	def isServerModeForBuilds(self):
		return self.isServerMode() and hxsublime_Settings.useHaxeServermodeForBuilds()

	def generateBuild(self,view):
		_g = self
		fn = view.file_name()
		def _hx_local_0():
			return Std._hx_is(_g._currentBuild, hxsublime_build_HxmlBuild)
		is_hxml_build = _hx_local_0
		if self._currentBuild is not None and is_hxml_build() and fn == self._currentBuild.buildFile() and view.size() == 0:
			def _hx_local_1(v,e):
				hxml_src = _g._currentBuild.makeHxml()
				v.insert(e, 0, hxml_src)
			
			run_edit = _hx_local_1
			hxsublime_tools_ViewTools.asyncEdit(view, run_edit)
		
		
	

	def selectBuild(self,view):
		scopes = view.scope_name(view.sel()[0].end()).split(" ")
		if Lambda.has(scopes, "source.hxml"):
			view.run_command("save")
		
		self.extractBuildArgs(view, True)
	

	def extractBuildArgs(self,view = None,force_panel = False):
		if view is None:
			view = None
		
		if force_panel is None:
			force_panel = False
		
		if view is None:
			view = sublime_Sublime.active_window().active_view()
		
		folders = self.getFolders(view)
		self.builds = self.findBuildsInFolders(folders)
		num_builds = __builtin__.len(self.builds)
		view_build_id = view.settings().get("haxe-current-build-id")
		if view_build_id is not None and view_build_id < num_builds and not force_panel:
			self.setCurrentBuild(view, view_build_id)
		elif num_builds == 1:
			if force_panel:
				sublime_Sublime.status_message("There is only one build")
			
			self.setCurrentBuild(view, 0)
		
		elif num_builds == 0 and force_panel:
			sublime_Sublime.status_message("No build files found (e.g. hxml, nmml, xml)")
			self.createNewHxml(view, folders[0])
		
		elif num_builds > 1 and force_panel:
			self.showBuildSelectionPanel(view)
		else:
			self.setCurrentBuild(view, 0)
	

	def hasBuild(self):
		return self._currentBuild is not None

	def checkBuild(self,view):
		self.build(view, hxsublime_project_BuildType.Check)

	def justBuild(self,view):
		self.build(view, hxsublime_project_BuildType.Build)

	def runBuild(self,view):
		self.build(view, hxsublime_project_BuildType.Run)

	def updateCompilerInfo(self):
		info = hxsublime_project_Project.collectCompilerInfo(self.haxeExec(), self._projectPath)
		bundle = info[0]
		ver = info[1]
		std_paths = info[2]
		self._serverMode = ver is None or ver >= 209
		self._stdBundle = bundle
		self._stdPaths = std_paths
	

	def findBuildsInFolders(self,folders):
		builds = []
		haxe_Log.trace("find builds start", _Hx_AnonObject(fileName = "Project.hx" ,lineNumber = 257 ,className = "hxsublime.project.Project" ,methodName = "findBuildsInFolders" ))
		_g = 0
		while _g < len(folders):
			f = folders[_g]
			_g = _g + 1
			x = None
			_this = hxsublime_build_Tools.findHxmlProjects(self, f)
			def _hx_local_0(x1):
				return x1
			x = __builtin__.list(__builtin__.map(_hx_local_0, _this))
			
			builds.extend(x)
			
			x = None
			_this = hxsublime_build_Tools.findNmeProjects(self, f)
			def _hx_local_1(x1):
				return x1
			x = __builtin__.list(__builtin__.map(_hx_local_1, _this))
			
			builds.extend(x)
			
			x = None
			_this = hxsublime_build_Tools.findOpenflProjects(self, f)
			def _hx_local_2(x1):
				return x1
			x = __builtin__.list(__builtin__.map(_hx_local_2, _this))
			
			builds.extend(x)
			
		
		
		haxe_Log.trace("find builds end", _Hx_AnonObject(fileName = "Project.hx" ,lineNumber = 265 ,className = "hxsublime.project.Project" ,methodName = "findBuildsInFolders" ))
		return builds
	

	def getViewFileName(self,view):
		if view is None:
			view = sublime_Sublime.active_window().active_view()
		
		return view.file_name()
	

	def getCurrentWindow(self,view):
		return hxsublime_project_Tools.getWindow(view)

	def getFolders(self,view):
		win = self.getCurrentWindow(view)
		folders = win.folders()
		return folders
	

	def createNewHxml(self,view,folder):
		win = sublime_Sublime.active_window()
		f = python_lib_os_Path.join(folder, "build.hxml")
		self._currentBuild = None
		self.getBuild(view)
		self._currentBuild.setHxml(f)
		win.open_file(f, sublime_Sublime.TRANSIENT)
		self.setCurrentBuild(view, 0)
	

	def showBuildSelectionPanel(self,view):
		_g1 = self
		buildsView = None
		_g = []
		_g11 = 0
		_g2 = self.builds
		while _g11 < len(_g2):
			b = _g2[_g11]
			_g11 = _g11 + 1
			x = [b.toString(), python_lib_os_Path.basename(b.buildFile())]
			_g.append(x)
			__builtin__.len(_g)
			
		
		
		buildsView = _g
		
		self._selectingBuild = True
		sublime_Sublime.status_message("Please select your build")
		def _hx_local_0(i):
			_g1._selectingBuild = False
			_g1.setCurrentBuild(view, i)
		
		onSelected = _hx_local_0
		win = sublime_Sublime.active_window()
		win.show_quick_panel(buildsView, onSelected, sublime_Sublime.MONOSPACE_FONT)
	

	def setCurrentBuild(self,view,id):
		haxe_Log.trace("setCurrentBuild", _Hx_AnonObject(fileName = "Project.hx" ,lineNumber = 327 ,className = "hxsublime.project.Project" ,methodName = "setCurrentBuild" ))
		if id < 0 or id >= __builtin__.len(self.builds):
			id = 0
		
		if __builtin__.len(self.builds) > 0:
			view.settings().set("haxe-current-build-id", id)
			self._currentBuild = self.builds[id]
			self._currentBuild.setStdBundle(self._stdBundle)
			view.set_status("haxe-build", self._currentBuild.toString())
		
		else:
			view.set_status("haxe-build", "No build found/selected")
	

	def build(self,view,type):
		if view is None:
			view = sublime_Sublime.active_window().active_view()
		
		win = view.window()
		env = hxsublime_project_Project.haxeBuildEnv(self.projectDir("."))
		build = None
		if self.hasBuild():
			build = self.getOriginalBuild(view)
		else:
			self.extractBuildArgs(view)
			build = self.getOriginalBuild(view)
		
		r = None
		if (type.index) == 0:
			r = build.prepareRunCmd(self, self.isServerModeForBuilds(), view)
		elif (type.index) == 1:
			r = build.prepareBuildCmd(self, self.isServerModeForBuilds(), view)
		elif (type.index) == 2:
			r = build.prepareCheckCmd(self, self.isServerMode(), view)
		
		cmd = r[0]
		build_folder = r[1]
		escaped_cmd = build.escapeCmd(cmd)
		hxsublime_panel_Panels.defaultPanel().writeln("running: " + " ".join(escaped_cmd))
		def _hx_local_0():
			x = _Hx_AnonObject(cmd = cmd ,is_check_run = type == hxsublime_project_BuildType.Check ,working_dir = build_folder ,file_regex = hxsublime_project_Tools.haxeFileRegex ,env = env )
			def _hx_local_2():
				def _hx_local_1():
					d = python_lib_Dict()
					_g = 0
					_g1 = Reflect.fields(x)
					while _g < len(_g1):
						f = _g1[_g]
						_g = _g + 1
						val = Reflect.field(x, f)
						python_lib_DictImpl.set(d, f, val)
						
					
					
					return d
				
				return _hx_local_1()
			
			return _hx_local_2()
		
		win.run_command("hxsublime_commands__haxe_exec", _hx_local_0())
	

	def clearBuild(self):
		self._currentBuild = None
		self.completionContext.clearCompletion()
	

	def destroy(self):
		self.server.stop()

	def createDefaultBuild(self,view):
		fn = view.file_name()
		src_dir = python_lib_os_Path.dirname(fn)
		src = view.substr(sublime_Region(0, view.size()))
		build = hxsublime_build_HxmlBuild(None, None)
		build._target = "js"
		folder = python_lib_os_Path.dirname(fn)
		folders = view.window().folders()
		_g = 0
		while _g < len(folders):
			f = folders[_g]
			_g = _g + 1
			if fn.find(f) > -1:
				folder = f
			
		
		
		pack = []
		_g = 0
		_g1 = python_lib_Re_RegexHelper.findallDynamic(hxsublime_tools_Regex.package_line, src, None, None)
		while _g < len(_g1):
			ps = _g1[_g]
			_g = _g + 1
			if ps == "":
				continue
			
			pack = ps.split(".")
			packrev = __builtin__.list(pack)
			packrev.reverse()
			_g2 = 0
			while _g2 < len(packrev):
				p = packrev[_g2]
				_g2 = _g2 + 1
				spl = python_lib_os_Path.split(src_dir)
				if spl[1] == p:
					src_dir = spl[0]
				
			
			
		
		
		cl = python_lib_os_Path.basename(fn)
		endIndex = cl.rfind(".", None)
		cl = python_Tools.substring(cl, 0, endIndex)
		
		main = __builtin__.list(pack)
		main.append(cl)
		__builtin__.len(main)
		
		build.main = ".".join(main)
		build.output = python_lib_os_Path.join(folder, build.main.lower() + ".js")
		build.addArg(("-cp", src_dir))
		build.addArg(("-js", build.output))
		build.setHxml(python_lib_os_Path.join(src_dir, "build.hxml"))
		return build
	

	def getOriginalBuild(self,view):
		if self._currentBuild is None and view.score_selector(0, "source.haxe.2") > 0:
			self._currentBuild = self.createDefaultBuild(view)
		
		return self._currentBuild
	

	def getBuild(self,view):
		return self.getOriginalBuild(view).copy()





def Project_statics_haxeBuildEnv(project_dir):
	lib_path = hxsublime_Settings.haxeLibraryPath()
	haxe_inst_path = hxsublime_Settings.haxeInstPath()
	neko_inst_path = hxsublime_Settings.nekoInstPath()
	env = python_lib_Os.environ.copy()
	env_path = python_lib_Os.environ.copy().get("PATH", "")
	paths = []
	path = None
	if lib_path is not None:
		if hxsublime_tools_PathTools.isAbsPath(lib_path):
			path = lib_path
		else:
			path = python_lib_os_Path.normpath(python_lib_os_Path.join(project_dir, lib_path))
		val = None
		_this = path.split("/")
		val = python_lib_Os.sep.join(_this)
		
		python_lib_DictImpl.set(env, "HAXE_LIBRARY_PATH", val)
		
		val = None
		_this = path.split("/")
		val = python_lib_Os.sep.join(_this)
		
		python_lib_DictImpl.set(env, "HAXE_STD_PATH", val)
		
	
	
	if haxe_inst_path is not None:
		if hxsublime_tools_PathTools.isAbsPath(haxe_inst_path):
			path = haxe_inst_path
		else:
			path = python_lib_os_Path.normpath(python_lib_os_Path.join(project_dir, haxe_inst_path))
		val = None
		_this = path.split("/")
		val = python_lib_Os.sep.join(_this)
		
		python_lib_DictImpl.set(env, "HAXEPATH", val)
		
		x = None
		_this = path.split("/")
		x = python_lib_Os.sep.join(_this)
		
		paths.append(x)
		__builtin__.len(paths)
		
		
	
	
	if neko_inst_path is not None:
		path = python_lib_os_Path.normpath(python_lib_os_Path.join(project_dir, neko_inst_path))
		val = None
		_this = path.split("/")
		val = python_lib_Os.sep.join(_this)
		
		python_lib_DictImpl.set(env, "NEKO_INSTPATH", val)
		
		x = None
		_this = path.split("/")
		x = python_lib_Os.sep.join(_this)
		
		paths.append(x)
		
	
	
	if __builtin__.len(paths) > 0:
		val = python_lib_Os.pathsep.join(paths) + python_lib_Os.pathsep + env_path
		python_lib_DictImpl.set(env, "PATH", val)
	
	
	return env
	
hxsublime_project_Project.haxeBuildEnv = Project_statics_haxeBuildEnv
def Project_statics_getCompilerInfoEnv(project_path):
	return hxsublime_project_Project.haxeBuildEnv(project_path)
hxsublime_project_Project.getCompilerInfoEnv = Project_statics_getCompilerInfoEnv
def Project_statics_collectCompilerInfo(haxeExec,project_path):
	env = hxsublime_project_Project.getCompilerInfoEnv(project_path)
	cmd = __builtin__.list(haxeExec)
	cmd.extend(["-main", "Nothing", "-v", "--no-output"])
	r = hxsublime_Execute.runCmd(cmd, None, None, env)
	out = r[0]
	err = r[1]
	stdClasspaths = hxsublime_project_Project.parseStdClasspaths(out)
	bundle = hxsublime_project_Project.collectStdClassesAndPacks(stdClasspaths)
	ver = hxsublime_project_Project.extractHaxeVersion(out)
	return (bundle, ver, stdClasspaths)
	
hxsublime_project_Project.collectCompilerInfo = Project_statics_collectCompilerInfo
def Project_statics_extractHaxeVersion(out):
	ver = python_lib_Re.search(hxsublime_project_Project.haxeVersionRegex, out)
	if ver is not None:
		x = ver.group(1)
		x1 = float(x)
		return int(x1)
		
	
	else:
		return None
	
hxsublime_project_Project.extractHaxeVersion = Project_statics_extractHaxeVersion
def Project_statics_removeTrailingPathSep(path):
	if __builtin__.len(path) > 1:
		last_pos = __builtin__.len(path) - 1
		last_char = path[last_pos]
		if last_char == "/" or last_char == "\\" or last_char == python_lib_os_Path.sep:
			path = python_Tools.substring(path, 0, last_pos)
		
	
	
	return path
	
hxsublime_project_Project.removeTrailingPathSep = Project_statics_removeTrailingPathSep
def Project_statics_isValidClasspath(path):
	return __builtin__.len(path) > 1 and python_lib_os_Path.exists(path) and python_lib_os_Path.isdir(path)
hxsublime_project_Project.isValidClasspath = Project_statics_isValidClasspath
def Project_statics_parseStdClasspaths(out):
	m = hxsublime_project_Project.classpathLineRegex.match(out)
	stdClasspaths = []
	all_paths = m.group(1).split(";")
	ignored_paths = [".", "./"]
	std_paths = None
	if m is not None:
		_this = python_lib_Set(all_paths)
		other = python_lib_Set(ignored_paths)
		std_paths = _this - other
	
	else:
		std_paths = python_lib_Set()
	def _hx_local_0():
		p = std_paths.__iter__()
		return python_HaxeIterator(p)
	
	_it = _hx_local_0()
	while _it.hasNext():
		p = _it.next()
		p1 = python_lib_os_Path.normpath(p)
		p1 = hxsublime_project_Project.removeTrailingPathSep(p1)
		if hxsublime_project_Project.isValidClasspath(p1):
			stdClasspaths.append(p1)
		
	
	return stdClasspaths
	
hxsublime_project_Project.parseStdClasspaths = Project_statics_parseStdClasspaths
def Project_statics_collectStdClassesAndPacks(stdCps):
	bundle = hxsublime_tools_HxSrcTools.emptyTypeBundle()
	_g = 0
	while _g < len(stdCps):
		p = stdCps[_g]
		_g = _g + 1
		bundle1 = hxsublime_Types.extractTypes(p, [], [], 0, [], False)
		bundle = bundle.merge(bundle1)
	
	
	return bundle
	
hxsublime_project_Project.collectStdClassesAndPacks = Project_statics_collectStdClassesAndPacks
hxsublime_project_Project.classpathLineRegex = python_lib_Re.compile("Classpath : (.*)")
hxsublime_project_Project.haxeVersionRegex = python_lib_Re.compile("haxe_([0-9]{3})", python_lib_Re.M)


hxsublime_project_Project._hx_class = hxsublime_project_Project
hxsublime_project_Project._hx_class_name = "hxsublime.project.Project"
_hx_classes['hxsublime.project.Project'] = hxsublime_project_Project
hxsublime_project_Project._hx_fields = ["_haxelibManager","_currentBuild","_selectingBuild","_projectFile","_projectId","_projectPath","_stdBundle","_stdPaths","_serverMode","completionContext","builds","winId","server"]
hxsublime_project_Project._hx_props = []
hxsublime_project_Project._hx_methods = ["haxelibManager","projectDir","nmeExec","openflExec","haxelibExec","haxeExec","haxeEnv","startServer","restartServer","isServerMode","isServerModeForBuilds","generateBuild","selectBuild","extractBuildArgs","hasBuild","checkBuild","justBuild","runBuild","updateCompilerInfo","findBuildsInFolders","getViewFileName","getCurrentWindow","getFolders","createNewHxml","showBuildSelectionPanel","setCurrentBuild","build","clearBuild","destroy","createDefaultBuild","getOriginalBuild","getBuild"]
hxsublime_project_Project._hx_statics = ["haxeBuildEnv","getCompilerInfoEnv","collectCompilerInfo","extractHaxeVersion","removeTrailingPathSep","isValidClasspath","parseStdClasspaths","collectStdClassesAndPacks","classpathLineRegex","haxeVersionRegex"]
hxsublime_project_Project._hx_interfaces = []

# print hxsublime.project.Projects.Projects
class hxsublime_project_Projects:

	def fileLog(self,msg):
		f = __builtin__.open(hxsublime_project_Projects.logFile, "a+")
		f.write(Std.string(msg) + "\n")
		f.close()
	





hxsublime_project_Projects.projects = hxsublime_tools_Cache(haxe_ds_StringMap())
hxsublime_project_Projects.userHome = python_lib_os_Path.expanduser("~")
hxsublime_project_Projects.logFile = python_lib_os_Path.join(hxsublime_project_Projects.userHome, "st3_haxe_log.txt")
hxsublime_project_Projects.nextServerPort = 6000
def Projects_statics_cleanupProjects():
	win_ids = None
	_g = []
	_g1 = 0
	_g2 = sublime_Sublime.windows()
	while _g1 < len(_g2):
		w = _g2[_g1]
		_g1 = _g1 + 1
		x = w.id()
		_g.append(x)
		__builtin__.len(_g)
		
	
	
	win_ids = _g
	
	remove = []
	_it = hxsublime_project_Projects.projects.data.keys()
	while _it.hasNext():
		p = _it.next()
		proj = hxsublime_project_Projects.projects.getOrDefault(p, None)
		if proj is not None and not Lambda.has(win_ids, proj.winId):
			remove.append(p)
			__builtin__.len(remove)
		
		
	
	haxe_Log.trace(remove, _Hx_AnonObject(fileName = "Projects.hx" ,lineNumber = 46 ,className = "hxsublime.project.Projects" ,methodName = "cleanupProjects" ))
	_g1 = 0
	while _g1 < len(remove):
		pid = remove[_g1]
		_g1 = _g1 + 1
		haxe_Log.trace(pid, _Hx_AnonObject(fileName = "Projects.hx" ,lineNumber = 48 ,className = "hxsublime.project.Projects" ,methodName = "cleanupProjects" ))
		project = hxsublime_project_Projects.projects.data.get(pid).val
		project.destroy()
		haxe_Log.trace("delete project from memory", _Hx_AnonObject(fileName = "Projects.hx" ,lineNumber = 51 ,className = "hxsublime.project.Projects" ,methodName = "cleanupProjects" ))
		hxsublime_project_Projects.projects.data.remove(pid)
	
	
	
hxsublime_project_Projects.cleanupProjects = Projects_statics_cleanupProjects
def Projects_statics_getProjectId(file,win):
	id = None
	if file is None:
		id = "global" + Std.string(win.id())
	else:
		id = file
	return id
	
hxsublime_project_Projects.getProjectId = Projects_statics_getProjectId
def Projects_statics_getWindow(view = None):
	if view is None:
		view = None
	
	win = None
	if view is not None:
		win = view.window()
		if win is not None:
			win = sublime_Sublime.active_window()
		
	
	else:
		win = sublime_Sublime.active_window()
	return win
	
hxsublime_project_Projects.getWindow = Projects_statics_getWindow
def Projects_statics_currentProject(view = None):
	if view is None:
		view = None
	
	hxsublime_project_Projects.cleanupProjects()
	file = hxsublime_tools_SublimeTools.getProjectFile()
	win = hxsublime_project_Projects.getWindow(view)
	id = hxsublime_project_Projects.getProjectId(file, win)
	haxe_Log.trace("project id:" + id, _Hx_AnonObject(fileName = "Projects.hx" ,lineNumber = 87 ,className = "hxsublime.project.Projects" ,methodName = "currentProject" ))
	haxe_Log.trace("win.id:" + Std.string(win.id()), _Hx_AnonObject(fileName = "Projects.hx" ,lineNumber = 88 ,className = "hxsublime.project.Projects" ,methodName = "currentProject" ))
	def _hx_local_0():
		id1 = id
		a1 = file
		a2 = win
		def _hx_local_1():
			return hxsublime_project_Projects.createProject(id1, a1, a2)
		return _hx_local_1
	
	res = hxsublime_project_Projects.projects.getOrInsert(id, _hx_local_0())
	return res
	
hxsublime_project_Projects.currentProject = Projects_statics_currentProject
def Projects_statics_createProject(id,file,win):
	p = hxsublime_project_Project(id, file, win.id(), hxsublime_project_Projects.nextServerPort)
	hxsublime_project_Projects.nextServerPort = hxsublime_project_Projects.nextServerPort + 20
	return p
	
hxsublime_project_Projects.createProject = Projects_statics_createProject


hxsublime_project_Projects._hx_class = hxsublime_project_Projects
hxsublime_project_Projects._hx_class_name = "hxsublime.project.Projects"
_hx_classes['hxsublime.project.Projects'] = hxsublime_project_Projects
hxsublime_project_Projects._hx_fields = []
hxsublime_project_Projects._hx_props = []
hxsublime_project_Projects._hx_methods = ["fileLog"]
hxsublime_project_Projects._hx_statics = ["projects","userHome","logFile","nextServerPort","cleanupProjects","getProjectId","getWindow","currentProject","createProject"]
hxsublime_project_Projects._hx_interfaces = []

# print hxsublime.project.Tools.Tools
class hxsublime_project_Tools:

	pass




def Tools_statics_getWindow(view):
	win = None
	if view is not None:
		win = view.window()
		if win is None:
			win = sublime_Sublime.active_window()
		
	
	else:
		win = sublime_Sublime.active_window()
	return win
	
hxsublime_project_Tools.getWindow = Tools_statics_getWindow
hxsublime_project_Tools.winStart = "(?:(?:[A-Za-z][:])"
hxsublime_project_Tools.unixStart = "(?:[/]?)"
hxsublime_project_Tools.haxeFileRegex = "^(" + hxsublime_project_Tools.winStart + "|" + hxsublime_project_Tools.unixStart + ")?(?:[^:]*)):([0-9]+): (?:character(?:s?)|line(?:s?))? ([0-9]+)-?[0-9]*\\s?:(.*)$"


hxsublime_project_Tools._hx_class = hxsublime_project_Tools
hxsublime_project_Tools._hx_class_name = "hxsublime.project.Tools"
_hx_classes['hxsublime.project.Tools'] = hxsublime_project_Tools
hxsublime_project_Tools._hx_fields = []
hxsublime_project_Tools._hx_props = []
hxsublime_project_Tools._hx_methods = []
hxsublime_project_Tools._hx_statics = ["getWindow","winStart","unixStart","haxeFileRegex"]
hxsublime_project_Tools._hx_interfaces = []

# print hxsublime.tools.HxSrcTools.Regex
class hxsublime_tools_Regex:

	pass




hxsublime_tools_Regex.space_chars = python_lib_Re.compile("\\s")
hxsublime_tools_Regex.word_chars = python_lib_Re.compile("[a-z0-9._]", python_lib_Re.I)
hxsublime_tools_Regex.import_line = python_lib_Re.compile("^([ \t]*)import\\s+([a-z0-9._]+);", python_lib_Re.I | python_lib_Re.M)
hxsublime_tools_Regex.using_line = python_lib_Re.compile("^([ \t]*)using\\s+([a-z0-9._]+);", python_lib_Re.I | python_lib_Re.M)
hxsublime_tools_Regex.package_line = python_lib_Re.compile("\\s*package\\s*([a-z0-9.]*)\\s*;", python_lib_Re.I)
hxsublime_tools_Regex.variables = python_lib_Re.compile("var\\s+([^:;\\s]*)", python_lib_Re.I)
hxsublime_tools_Regex.named_functions = python_lib_Re.compile("function\\s+([a-zA-Z0-9_]+)\\s*", python_lib_Re.I)
hxsublime_tools_Regex.function_params = python_lib_Re.compile("function\\s+[a-zA-Z0-9_]+\\s*\\(([^\\)]*)", python_lib_Re.M)
hxsublime_tools_Regex.param_default = python_lib_Re.compile("(=\\s*\"*[^\"]*\")", python_lib_Re.M)
hxsublime_tools_Regex.isType = python_lib_Re.compile("^[A-Z][a-zA-Z0-9_]*$")
hxsublime_tools_Regex.typeDeclWithScope = python_lib_Re.compile("(private\\s+)?(?:extern\\s+)?(class|typedef|enum|interface|abstract)\\s+([A-Z][a-zA-Z0-9_]*)\\s*(<[a-zA-Z0-9_,]+>)?", python_lib_Re.M)
hxsublime_tools_Regex.comments = python_lib_Re.compile("(//[^\n\r]*?[\n\r]|/\\*(.*?)\\*/)", python_lib_Re.MULTILINE | python_lib_Re.DOTALL)
hxsublime_tools_Regex.fieldRegex = python_lib_Re.compile("((?:(?:public|static|inline|private)\\s+)*)(var|function)\\s+([a-zA-Z_][a-zA-Z0-9_]*)", python_lib_Re.MULTILINE)
hxsublime_tools_Regex.typeDeclWithScopeRegex = python_lib_Re.compile("(private\\s+)?(extern\\s+)?(class|typedef|enum|interface|abstract)\\s+([A-Z][a-zA-Z0-9_]*)\\s*(<[a-zA-Z0-9,_]+>)?(:?\\{|\\s+)", python_lib_Re.M)
hxsublime_tools_Regex.enumConstructorStartDecl = python_lib_Re.compile("\\s+([a-zA-Z_]+)", python_lib_Re.M)


hxsublime_tools_Regex._hx_class = hxsublime_tools_Regex
hxsublime_tools_Regex._hx_class_name = "hxsublime.tools.Regex"
_hx_classes['hxsublime.tools.Regex'] = hxsublime_tools_Regex
hxsublime_tools_Regex._hx_fields = []
hxsublime_tools_Regex._hx_props = []
hxsublime_tools_Regex._hx_methods = []
hxsublime_tools_Regex._hx_statics = ["space_chars","word_chars","import_line","using_line","package_line","variables","named_functions","function_params","param_default","isType","typeDeclWithScope","comments","fieldRegex","typeDeclWithScopeRegex","enumConstructorStartDecl"]
hxsublime_tools_Regex._hx_interfaces = []

# print hxsublime.tools.HxSrcTools.HxSrcTools
class hxsublime_tools_HxSrcTools:

	pass




def HxSrcTools_statics_getTypesFromSrc(src,moduleName,file,src_with_comments):
	if moduleName is None:
		_this = python_lib_os_Path.splitext(python_lib_os_Path.basename(file))
		moduleName = _this[0]
	
	
	pack = hxsublime_tools_HxSrcTools.getPackage(src)
	res = haxe_ds_StringMap()
	def _hx_local_0():
		p = hxsublime_tools_Regex.typeDeclWithScopeRegex.finditer(src)
		return python_HaxeIterator(p)
	
	_it = _hx_local_0()
	while _it.hasNext():
		decl = _it.next()
		isPrivate = decl.group(1) is not None
		type_name = decl.group(4)
		if type_name == "NME_":
			haxe_Log.trace(Std.string(decl.group(0)), _Hx_AnonObject(fileName = "HxSrcTools.hx" ,lineNumber = 80 ,className = "hxsublime.tools.HxSrcTools" ,methodName = "getTypesFromSrc" ))
		
		kind = decl.group(3)
		isExtern = decl.group(2) is not None
		isModuleType = type_name == moduleName
		isStdType = moduleName == "StdTypes"
		fullType = hxsublime_tools_HaxeType(pack, moduleName, type_name, kind, isPrivate, isModuleType, isStdType, isExtern, file, src, src_with_comments, decl)
		if fullType.kind == "enum":
			fullType._enumConstructors = hxsublime_tools_HxSrcTools.extractEnumConstructorsFromSrc(src, decl.end(4))
		
		if not res.exists(fullType.fullQualifiedName()):
			res.set(fullType.fullQualifiedName(), fullType)
		
	
	return hxsublime_tools_HaxeTypeBundle(res)
	
hxsublime_tools_HxSrcTools.getTypesFromSrc = HxSrcTools_statics_getTypesFromSrc
def HxSrcTools_statics_extractEnumConstructorsFromSrc(src,start_pos):
	constructors = None
	start = hxsublime_tools_HxSrcTools.searchNextCharOnSameNestingLevel(src, ["{"], start_pos)
	if start is not None:
		end = hxsublime_tools_HxSrcTools.searchNextCharOnSameNestingLevel(src, ["}"], start[0] + 1)
		if end is not None:
			def _hx_local_0():
				startIndex = start[0] + 1
				endIndex = end[0] - 1
				return python_Tools.substring(src, startIndex, endIndex)
			
			constructors = hxsublime_tools_HxSrcTools.extractEnumConstructorsFromEnum(_hx_local_0())
		
		
	
	
	return constructors
	
hxsublime_tools_HxSrcTools.extractEnumConstructorsFromSrc = HxSrcTools_statics_extractEnumConstructorsFromSrc
def HxSrcTools_statics_extractEnumConstructorsFromEnum(enumStr):
	constructors = []
	start = 0
	while True:
		m = hxsublime_tools_Regex.enumConstructorStartDecl.match(enumStr, start)
		if m is not None:
			constructor = m.group(1)
			constructors.append(constructor)
			__builtin__.len(constructors)
			
			end = hxsublime_tools_HxSrcTools.searchNextCharOnSameNestingLevel(enumStr, [";"], m.end(1))
			if end is not None:
				start = end[0] + 1
			else:
				break
		
		else:
			break
	
	return constructors
	
hxsublime_tools_HxSrcTools.extractEnumConstructorsFromEnum = HxSrcTools_statics_extractEnumConstructorsFromEnum
def HxSrcTools_statics_skipWhitespaceOrComments(hxSrcSection,start_pos):
	in_single_comment = False
	in_multi_comment = False
	count = __builtin__.len(hxSrcSection)
	pos = start_pos
	while True:
		if pos > count - 1:
			break
		
		c = hxSrcSection[pos]
		next = None
		if pos < count - 1:
			next = hxSrcSection[pos + 1]
		else:
			next = None
		if in_single_comment and c == "\n":
			pos = pos + 1
			in_single_comment = False
		
		elif in_multi_comment and c == "*" and next == "/":
			in_multi_comment = False
			pos = pos + 2
		
		elif in_single_comment or in_multi_comment:
			pos = pos + 1
		elif c == "/" and next == "/":
			pos = pos + 2
			in_single_comment = True
		
		elif c == "/" and next == "*":
			pos = pos + 2
			in_multi_comment = True
		
		elif c == " " or c == "\t" or c == "\n":
			pos = pos + 1
		else:
			b = python_Tools.substring(hxSrcSection, start_pos, pos)
			return (pos, b)
		
	
	return None
	
hxsublime_tools_HxSrcTools.skipWhitespaceOrComments = HxSrcTools_statics_skipWhitespaceOrComments
def HxSrcTools_statics_isSameNestingLevelAtPos(hxSrcSection,end_pos,start_pos):
	if end_pos < start_pos:
		return False
	
	open_pars = 0
	open_braces = 0
	open_brackets = 0
	open_angle_brackets = 0
	in_string = False
	string_char = None
	in_regexp = False
	count = __builtin__.len(hxSrcSection)
	cur = ""
	pos = start_pos
	lastPos = count - 1
	while True:
		if pos == end_pos or pos > lastPos:
			return open_pars == 0 and open_braces == 0 and open_brackets == 0 and open_angle_brackets == 0 and not in_string and not in_regexp
		
		c = hxSrcSection[pos]
		ccode = ord(c)
		hasNext = pos < lastPos
		next = None
		if hasNext:
			next = hxSrcSection[pos + 1]
		else:
			next = None
		nextCode = None
		if hasNext:
			nextCode = ord(next)
		else:
			nextCode = None
		if in_regexp:
			pos = pos + 1
			cur = cur + c
			if ccode != 92 and nextCode == 47:
				in_regexp = False
			
			continue
		
		
		if in_string:
			if c == string_char:
				pos = pos + 1
				cur = cur + c
				in_string = False
			
			elif ccode == 92 and next == string_char:
				pos = pos + 2
				cur = cur + c + next
				in_string = False
			
			else:
				cur = cur + c
				pos = pos + 1
			
			continue
		
		
		if ccode == 126 and nextCode == 47:
			pos = pos + 2
			in_regexp = True
			cur = cur + c
		
		elif ccode == 39 or ccode == 34:
			in_string = True
			string_char = c
			cur = cur + c
			pos = pos + 1
		
		elif ccode == 45 and nextCode == 62:
			cur = cur + "->"
			pos = pos + 2
		
		elif ccode == 123:
			pos = pos + 1
			open_braces = open_braces + 1
			cur = cur + c
		
		elif ccode == 125:
			pos = pos + 1
			open_braces = open_braces - 1
			cur = cur + c
		
		elif ccode == 40:
			pos = pos + 1
			open_pars = open_pars + 1
			cur = cur + c
		
		elif ccode == 41:
			pos = pos + 1
			open_pars = open_pars - 1
			cur = cur + c
		
		elif ccode == 91:
			pos = pos + 1
			open_brackets = open_brackets + 1
			cur = cur + c
		
		elif ccode == 93:
			pos = pos + 1
			open_brackets = open_brackets - 1
			cur = cur + c
		
		elif ccode == 60:
			pos = pos + 1
			open_angle_brackets = open_angle_brackets + 1
			cur = cur + c
		
		elif ccode == 62:
			pos = pos + 1
			open_angle_brackets = open_angle_brackets - 1
			cur = cur + c
		
		else:
			pos = pos + 1
			cur = cur + c
		
	
	return False
	
hxsublime_tools_HxSrcTools.isSameNestingLevelAtPos = HxSrcTools_statics_isSameNestingLevelAtPos
def HxSrcTools_statics_searchNextCharOnSameNestingLevel(hxSrcSection,chars,start_pos):
	open_pars = 0
	open_braces = 0
	open_brackets = 0
	open_angle_brackets = 0
	in_string = False
	string_char = None
	in_regexp = False
	count = __builtin__.len(hxSrcSection)
	cur = ""
	pos = start_pos
	while True:
		if pos > count - 1:
			break
		
		c = hxSrcSection[pos]
		next = None
		if pos < count - 1:
			next = hxSrcSection[pos + 1]
		else:
			next = None
		if in_regexp:
			pos = pos + 1
			cur = cur + c
			if c != "\\" and next == "/":
				in_regexp = False
			
			continue
		
		
		if in_string:
			if c == string_char:
				pos = pos + 1
				cur = cur + c
				in_string = False
			
			elif c == "\\" and next == string_char:
				pos = pos + 2
				cur = cur + c + next
				in_string = False
			
			else:
				cur = cur + c
				pos = pos + 1
			
			continue
		
		
		if open_pars == 0 and open_braces == 0 and open_brackets == 0 and open_angle_brackets == 0 and c in chars:
			return (pos, cur)
		
		if c == "~" and next == "/":
			pos = pos + 2
			in_regexp = True
			cur = cur + c
		
		elif c == "'" or c == "\"":
			in_string = True
			string_char = c
			cur = cur + c
			pos = pos + 1
		
		elif c == "-" and next == ">":
			cur = cur + "->"
			pos = pos + 2
		
		elif c == "{":
			pos = pos + 1
			open_braces = open_braces + 1
			cur = cur + c
		
		elif c == "}":
			pos = pos + 1
			open_braces = open_braces - 1
			cur = cur + c
		
		elif c == "(":
			pos = pos + 1
			open_pars = open_pars + 1
			cur = cur + c
		
		elif c == ")":
			pos = pos + 1
			open_pars = open_pars - 1
			cur = cur + c
		
		elif c == "[":
			pos = pos + 1
			open_brackets = open_brackets + 1
			cur = cur + c
		
		elif c == "]":
			pos = pos + 1
			open_brackets = open_brackets - 1
			cur = cur + c
		
		elif c == "<":
			pos = pos + 1
			open_angle_brackets = open_angle_brackets + 1
			cur = cur + c
		
		elif c == ">":
			pos = pos + 1
			open_angle_brackets = open_angle_brackets - 1
			cur = cur + c
		
		else:
			pos = pos + 1
			cur = cur + c
		
	
	return None
	
hxsublime_tools_HxSrcTools.searchNextCharOnSameNestingLevel = HxSrcTools_statics_searchNextCharOnSameNestingLevel
def HxSrcTools_statics_reverse_search_next_char_on_same_nesting_level(hxSrcSection,chars,start_pos):
	open_pars = 0
	open_braces = 0
	open_brackets = 0
	open_angle_brackets = 0
	in_string = False
	string_char = None
	cur = ""
	pos = start_pos
	while True:
		if pos <= -1:
			break
		
		c = hxSrcSection[pos]
		next = None
		if pos > 0:
			next = hxSrcSection[pos - 1]
		else:
			next = None
		if in_string:
			pos = pos - 1
			cur = c + cur
			if c == string_char and next != "\\":
				in_string = False
			
			continue
		
		
		if c == "/" and next == "/":
			pos = pos - 2
			cur = "//" + c
			continue
		
		
		if open_pars == 0 and open_braces == 0 and open_brackets == 0 and open_angle_brackets == 0 and c in chars:
			return (pos, cur)
		
		if c == "'" or c == "\"":
			in_string = True
			string_char = c
			cur = c + cur
			pos = pos - 1
		
		elif c == ">" and next == "-":
			cur = "->" + cur
			pos = pos - 2
		
		elif c == "}":
			pos = pos - 1
			open_braces = open_braces + 1
			cur = c + cur
		
		elif c == "{":
			pos = pos - 1
			open_braces = open_braces - 1
			cur = c + cur
		
		elif c == ")":
			pos = pos - 1
			open_pars = open_pars + 1
			cur = c + cur
		
		elif c == "(":
			pos = pos - 1
			open_pars = open_pars - 1
			cur = c + cur
		
		elif c == "]":
			pos = pos - 1
			open_brackets = open_brackets + 1
			cur = c + cur
		
		elif c == "[":
			pos = pos - 1
			open_brackets = open_brackets - 1
			cur = c + cur
		
		elif c == ">":
			pos = pos - 1
			open_angle_brackets = open_angle_brackets + 1
			cur = c + cur
		
		elif c == "<":
			pos = pos - 1
			open_angle_brackets = open_angle_brackets - 1
			cur = c + cur
		
		else:
			pos = pos - 1
			cur = c + cur
		
	
	return None
	
hxsublime_tools_HxSrcTools.reverse_search_next_char_on_same_nesting_level = HxSrcTools_statics_reverse_search_next_char_on_same_nesting_level
def HxSrcTools_statics_stripComments(src):
	return hxsublime_tools_Regex.comments.sub("", src)
hxsublime_tools_HxSrcTools.stripComments = HxSrcTools_statics_stripComments
def HxSrcTools_statics_getPackage(src):
	pack = ""
	all = python_lib_Re_RegexHelper.findallDynamic(hxsublime_tools_Regex.package_line, src, None, None)
	_g = 0
	while _g < len(all):
		ps = all[_g]
		_g = _g + 1
		pack = ps
	
	
	return pack
	
hxsublime_tools_HxSrcTools.getPackage = HxSrcTools_statics_getPackage
def HxSrcTools_statics_splitFunctionSignature(signature):
	open_pars = 0
	open_braces = 0
	open_brackets = 0
	types = []
	count = __builtin__.len(signature)
	cur = ""
	pos = 0
	while True:
		if pos > count - 1:
			types.append(cur)
			break
		
		
		c = signature[pos]
		next = None
		if pos < count - 1:
			next = signature[pos + 1]
		else:
			next = None
		if c == "-" and next == ">":
			if open_pars == 0 and open_braces == 0 and open_brackets == 0:
				types.append(cur)
				cur = ""
			
			else:
				cur = cur + "->"
			pos = pos + 2
		
		elif c == " " and open_pars == 0 and open_braces == 0 and open_brackets == 0:
			pos = pos + 1
		elif c == "{":
			pos = pos + 1
			open_braces = open_braces + 1
			cur = cur + c
		
		elif c == "}":
			pos = pos + 1
			open_braces = open_braces - 1
			cur = cur + c
		
		elif c == "(":
			pos = pos + 1
			open_pars = open_pars + 1
			cur = cur + c
		
		elif c == ")":
			pos = pos + 1
			open_pars = open_pars - 1
			cur = cur + c
		
		elif c == "<":
			pos = pos + 1
			open_brackets = open_brackets + 1
			cur = cur + c
		
		elif c == ">":
			pos = pos + 1
			open_brackets = open_brackets - 1
			cur = cur + c
		
		else:
			pos = pos + 1
			cur = cur + c
		
	
	return types
	
hxsublime_tools_HxSrcTools.splitFunctionSignature = HxSrcTools_statics_splitFunctionSignature
def HxSrcTools_statics_emptyTypeBundle():
	return hxsublime_tools_HaxeTypeBundle(haxe_ds_StringMap())
hxsublime_tools_HxSrcTools.emptyTypeBundle = HxSrcTools_statics_emptyTypeBundle


hxsublime_tools_HxSrcTools._hx_class = hxsublime_tools_HxSrcTools
hxsublime_tools_HxSrcTools._hx_class_name = "hxsublime.tools.HxSrcTools"
_hx_classes['hxsublime.tools.HxSrcTools'] = hxsublime_tools_HxSrcTools
hxsublime_tools_HxSrcTools._hx_fields = []
hxsublime_tools_HxSrcTools._hx_props = []
hxsublime_tools_HxSrcTools._hx_methods = []
hxsublime_tools_HxSrcTools._hx_statics = ["getTypesFromSrc","extractEnumConstructorsFromSrc","extractEnumConstructorsFromEnum","skipWhitespaceOrComments","isSameNestingLevelAtPos","searchNextCharOnSameNestingLevel","reverse_search_next_char_on_same_nesting_level","stripComments","getPackage","splitFunctionSignature","emptyTypeBundle"]
hxsublime_tools_HxSrcTools._hx_interfaces = []

# print hxsublime.tools.HxSrcTools.HaxeModule
class hxsublime_tools_HaxeModule:


	def __init__(self,pack,name,file):
		self.pack = pack
		self.name = name
		self.file = file
	
	# var pack
	# var name
	# var file






hxsublime_tools_HaxeModule._hx_class = hxsublime_tools_HaxeModule
hxsublime_tools_HaxeModule._hx_class_name = "hxsublime.tools.HaxeModule"
_hx_classes['hxsublime.tools.HaxeModule'] = hxsublime_tools_HaxeModule
hxsublime_tools_HaxeModule._hx_fields = ["pack","name","file"]
hxsublime_tools_HaxeModule._hx_props = []
hxsublime_tools_HaxeModule._hx_methods = []
hxsublime_tools_HaxeModule._hx_statics = []
hxsublime_tools_HaxeModule._hx_interfaces = []

# print hxsublime.tools.HxSrcTools.HaxeTypeBundle
class hxsublime_tools_HaxeTypeBundle:


	def __init__(self,types):
		self.allTypes_cache_set = False
		self.allTypes_cache = None
		self.allTypesAndEnumConstructors_cache_set = False
		self.allTypesAndEnumConstructors_cache = None
		self.allTypesAndEnumConstructorsWithInfo_cache_set = False
		self.allTypesAndEnumConstructorsWithInfo_cache = None
		self.allModulesList_cache_set = False
		self.allModulesList_cache = None
		self.allModules_cache_set = False
		self.allModules_cache = None
		self.packs_cache_set = False
		self.packs_cache = None
		self.toString_cache_set = False
		self.toString_cache = None
		self._types = types
	
	# var _types
	# var toString_cache
	# var toString_cache_set
	def toString(self):
		_g = self
		if not self.toString_cache_set:
			self.toString_cache_set = True
			def _hx_local_0():
				return "HaxeTypeBundle(\n" + _g._types.toString() + "\n)"
			eval = _hx_local_0
			self.toString_cache = eval()
		
		
		return self.toString_cache
	

	def merge(self,other):
		return self.mergeAll([other])

	def mergeAll(self,others):
		res = None
		_g = haxe_ds_StringMap()
		_it = self._types.keys()
		while _it.hasNext():
			k = _it.next()
			value = self._types.get(k)
			_g.set(k, value)
		
		res = _g
		
		_g1 = 0
		while _g1 < len(others):
			o = others[_g1]
			_g1 = _g1 + 1
			_it = o._types.keys()
			while _it.hasNext():
				k = _it.next()
				res.set(k, o._types.get(k))
		
		
		return hxsublime_tools_HaxeTypeBundle(res)
	

	# var packs_cache
	# var packs_cache_set
	def packs(self):
		_g = self
		if not self.packs_cache_set:
			self.packs_cache_set = True
			def _hx_local_2():
				res = haxe_ds_StringMap()
				_it = _g._types.keys()
				while _it.hasNext():
					k = _it.next()
					p = _g._types.get(k).pack
					if p != "":
						res.set(p, None)
					
				
				def _hx_local_1():
					def _hx_local_0():
						return res.keys()
					return Lambda.array(_Hx_AnonObject(iterator = _hx_local_0 ))
				
				return _hx_local_1()
			
			eval = _hx_local_2
			self.packs_cache = eval()
		
		
		return self.packs_cache
	

	# var allModules_cache
	# var allModules_cache_set
	def allModules(self):
		_g = self
		if not self.allModules_cache_set:
			self.allModules_cache_set = True
			def _hx_local_0():
				res = haxe_ds_StringMap()
				_it = _g._types.keys()
				while _it.hasNext():
					k = _it.next()
					t = _g._types.get(k)
					res.set(t.fullPackWithModule(), hxsublime_tools_HaxeModule(t.pack, t.module, t._file))
				
				return res
			
			eval = _hx_local_0
			self.allModules_cache = eval()
		
		
		return self.allModules_cache
	

	# var allModulesList_cache
	# var allModulesList_cache_set
	def allModulesList(self):
		_g = self
		if not self.allModulesList_cache_set:
			self.allModulesList_cache_set = True
			def _hx_local_0():
				mods = _g.allModules()
				_g1 = []
				_it = _hx_functools.partial(HxOverrides_iterator, mods)()
				while _it.hasNext():
					m = _it.next()
					_g1.append(m)
					__builtin__.len(_g1)
				
				return _g1
				
			
			eval = _hx_local_0
			self.allModulesList_cache = eval()
		
		
		return self.allModulesList_cache
	

	# var allTypesAndEnumConstructorsWithInfo_cache
	# var allTypesAndEnumConstructorsWithInfo_cache_set
	def allTypesAndEnumConstructorsWithInfo(self):
		_g = self
		if not self.allTypesAndEnumConstructorsWithInfo_cache_set:
			self.allTypesAndEnumConstructorsWithInfo_cache_set = True
			def _hx_local_0():
				res = haxe_ds_StringMap()
				_it = _g._types.keys()
				while _it.hasNext():
					k = _it.next()
					t = _g._types.get(k)
					if t.kind == "enum":
						_g1 = 0
						_g2 = t.fullQualifiedEnumConstructorsWithOptionalModule()
						while _g1 < len(_g2):
							ec = _g2[_g1]
							_g1 = _g1 + 1
							res.set(ec, t)
						
					
					
					fq_name = t.fullQualifiedNameWithOptionalModule()
					res.set(fq_name, t)
				
				return res
			
			eval = _hx_local_0
			self.allTypesAndEnumConstructorsWithInfo_cache = eval()
		
		
		return self.allTypesAndEnumConstructorsWithInfo_cache
	

	# var allTypesAndEnumConstructors_cache
	# var allTypesAndEnumConstructors_cache_set
	def allTypesAndEnumConstructors(self):
		_g = self
		if not self.allTypesAndEnumConstructors_cache_set:
			self.allTypesAndEnumConstructors_cache_set = True
			def _hx_local_0():
				res = _g.allTypesAndEnumConstructorsWithInfo()
				_g1 = []
				_it = res.keys()
				while _it.hasNext():
					k = _it.next()
					_g1.append(k)
					__builtin__.len(_g1)
				
				return _g1
				
			
			eval = _hx_local_0
			self.allTypesAndEnumConstructors_cache = eval()
		
		
		return self.allTypesAndEnumConstructors_cache
	

	# var allTypes_cache
	# var allTypes_cache_set
	def allTypes(self):
		_g1 = self
		if not self.allTypes_cache_set:
			self.allTypes_cache_set = True
			def _hx_local_0():
				_g = []
				_it = _hx_functools.partial(HxOverrides_iterator, _g1._types)()
				while _it.hasNext():
					v = _it.next()
					_g.append(v)
					__builtin__.len(_g)
				
				return _g
			
			eval = _hx_local_0
			self.allTypes_cache = eval()
		
		
		return self.allTypes_cache
	

	def filter(self,fn):
		res = haxe_ds_StringMap()
		_it = self._types.keys()
		while _it.hasNext():
			k = _it.next()
			t = self._types.get(k)
			if fn(t):
				res.set(k, t)
			
		
		return hxsublime_tools_HaxeTypeBundle(res)
	







hxsublime_tools_HaxeTypeBundle._hx_class = hxsublime_tools_HaxeTypeBundle
hxsublime_tools_HaxeTypeBundle._hx_class_name = "hxsublime.tools.HaxeTypeBundle"
_hx_classes['hxsublime.tools.HaxeTypeBundle'] = hxsublime_tools_HaxeTypeBundle
hxsublime_tools_HaxeTypeBundle._hx_fields = ["_types","toString_cache","toString_cache_set","packs_cache","packs_cache_set","allModules_cache","allModules_cache_set","allModulesList_cache","allModulesList_cache_set","allTypesAndEnumConstructorsWithInfo_cache","allTypesAndEnumConstructorsWithInfo_cache_set","allTypesAndEnumConstructors_cache","allTypesAndEnumConstructors_cache_set","allTypes_cache","allTypes_cache_set"]
hxsublime_tools_HaxeTypeBundle._hx_props = []
hxsublime_tools_HaxeTypeBundle._hx_methods = ["toString","merge","mergeAll","packs","allModules","allModulesList","allTypesAndEnumConstructorsWithInfo","allTypesAndEnumConstructors","allTypes","filter"]
hxsublime_tools_HaxeTypeBundle._hx_statics = []
hxsublime_tools_HaxeTypeBundle._hx_interfaces = [hxsublime_macros_LazyFunctionSupport]

# print hxsublime.tools.HxSrcTools.EnumConstructor
class hxsublime_tools_EnumConstructor:


	def __init__(self,name,enum_type):
		self.name = name
		self.enumType = enum_type
	
	# var name
	# var enumType
	def toSnippetInsert(self,import_list,insert_file):
		_g = 0
		while _g < len(import_list):
			i = import_list[_g]
			_g = _g + 1
			if self.enumType._file == insert_file or i == self.enumType.fullQualifiedNameWithOptionalModule() or i == self.enumType.fullPackWithModule() or i == self.enumType.fullQualifiedNameWithOptionalModule() + "." + self.name:
				return self.name
			
		
		
		return self.enumType.fullQualifiedNameWithOptionalModule() + "." + self.name
	

	def typeHint(self):
		return "enum value"

	def toSnippet(self,insert_file,import_list):
		location = None
		def _hx_local_0():
			_this = self.enumType.fullPackWithOptionalModule()
			return __builtin__.len(_this)
		
		if _hx_local_0() > 0:
			location = " (" + self.enumType.fullPackWithOptionalModule() + ")"
		else:
			location = ""
		display = self.enumType.name + "." + self.name + location + "\t" + self.typeHint()
		insert = self.toSnippetInsert(import_list, insert_file)
		return (display, insert)
	

	def toString(self):
		return self.name







hxsublime_tools_EnumConstructor._hx_class = hxsublime_tools_EnumConstructor
hxsublime_tools_EnumConstructor._hx_class_name = "hxsublime.tools.EnumConstructor"
_hx_classes['hxsublime.tools.EnumConstructor'] = hxsublime_tools_EnumConstructor
hxsublime_tools_EnumConstructor._hx_fields = ["name","enumType"]
hxsublime_tools_EnumConstructor._hx_props = []
hxsublime_tools_EnumConstructor._hx_methods = ["toSnippetInsert","typeHint","toSnippet","toString"]
hxsublime_tools_EnumConstructor._hx_statics = []
hxsublime_tools_EnumConstructor._hx_interfaces = []

# print hxsublime.tools.HxSrcTools.HaxeField
class hxsublime_tools_HaxeField:


	def __init__(self,type,name,kind,is_static,is_public,is_inline,is_private,match_decl):
		self.toExpression_cache_set = False
		self.toExpression_cache = None
		self.toString_cache_set = False
		self.toString_cache = None
		self.isFunction_cache_set = False
		self.isFunction_cache = None
		self.file_cache_set = False
		self.file_cache = None
		self.isVar_cache_set = False
		self.isVar_cache = None
		self.srcPos_cache_set = False
		self.srcPos_cache = None
		self.type = type
		self.name = name
		self.kind = kind
		self.isStatic = is_static
		self.isPublic = is_public
		self.isInline = is_inline
		self.isPrivate = is_private
		self.match_decl = match_decl
	
	# var type
	# var name
	# var kind
	# var isStatic
	# var isPublic
	# var isInline
	# var isPrivate
	# var match_decl
	# var srcPos_cache
	# var srcPos_cache_set
	def srcPos(self):
		_g = self
		if not self.srcPos_cache_set:
			self.srcPos_cache_set = True
			def _hx_local_1():
				def _hx_local_0():
					p = hxsublime_tools_Regex.fieldRegex.finditer(_g.type.src_with_comments)
					return python_HaxeIterator(p)
				
				_it = _hx_local_0()
				while _it.hasNext():
					decl = _it.next()
					if decl.group(0) == _g.match_decl.group(0):
						return decl.start(0)
					
				return None
			
			eval = _hx_local_1
			self.srcPos_cache = eval()
		
		
		return self.srcPos_cache
	

	# var isVar_cache
	# var isVar_cache_set
	def isVar(self):
		_g = self
		if not self.isVar_cache_set:
			self.isVar_cache_set = True
			def _hx_local_0():
				return _g.kind == "var"
			eval = _hx_local_0
			self.isVar_cache = eval()
		
		
		return self.isVar_cache
	

	# var file_cache
	# var file_cache_set
	def file(self):
		_g = self
		if not self.file_cache_set:
			self.file_cache_set = True
			def _hx_local_0():
				return _g.type._file
			eval = _hx_local_0
			self.file_cache = eval()
		
		
		return self.file_cache
	

	# var isFunction_cache
	# var isFunction_cache_set
	def isFunction(self):
		_g = self
		if not self.isFunction_cache_set:
			self.isFunction_cache_set = True
			def _hx_local_0():
				return _g.kind == "function"
			eval = _hx_local_0
			self.isFunction_cache = eval()
		
		
		return self.isFunction_cache
	

	# var toString_cache
	# var toString_cache_set
	def toString(self):
		_g = self
		if not self.toString_cache_set:
			self.toString_cache_set = True
			def _hx_local_0():
				return _g.type.fullQualifiedNameWithOptionalModule() + ("::" if (_g.isStatic or _g.name == "new") else ".") + _g.name
			eval = _hx_local_0
			self.toString_cache = eval()
		
		
		return self.toString_cache
	

	# var toExpression_cache
	# var toExpression_cache_set
	def toExpression(self):
		_g = self
		if not self.toExpression_cache_set:
			self.toExpression_cache_set = True
			def _hx_local_0():
				return _g.type.fullQualifiedNameWithOptionalModule() + "." + _g.name
			eval = _hx_local_0
			self.toExpression_cache = eval()
		
		
		return self.toExpression_cache
	







hxsublime_tools_HaxeField._hx_class = hxsublime_tools_HaxeField
hxsublime_tools_HaxeField._hx_class_name = "hxsublime.tools.HaxeField"
_hx_classes['hxsublime.tools.HaxeField'] = hxsublime_tools_HaxeField
hxsublime_tools_HaxeField._hx_fields = ["type","name","kind","isStatic","isPublic","isInline","isPrivate","match_decl","srcPos_cache","srcPos_cache_set","isVar_cache","isVar_cache_set","file_cache","file_cache_set","isFunction_cache","isFunction_cache_set","toString_cache","toString_cache_set","toExpression_cache","toExpression_cache_set"]
hxsublime_tools_HaxeField._hx_props = []
hxsublime_tools_HaxeField._hx_methods = ["srcPos","isVar","file","isFunction","toString","toExpression"]
hxsublime_tools_HaxeField._hx_statics = []
hxsublime_tools_HaxeField._hx_interfaces = [hxsublime_macros_LazyFunctionSupport]

# print hxsublime.tools.HxSrcTools.HaxeType
class hxsublime_tools_HaxeType:


	def __init__(self,pack,module,name,kind,is_private,is_module_type,is_std_type,is_extern,file,src,src_with_comments,match_decl):
		self.toString_cache_set = False
		self.toString_cache = None
		self.fullQualifiedName_cache_set = False
		self.fullQualifiedName_cache = None
		self.classpath_cache_set = False
		self.classpath_cache = None
		self.fullQualifiedEnumConstructorsWithOptionalModule_cache_set = False
		self.fullQualifiedEnumConstructorsWithOptionalModule_cache = None
		self.enumConstructors_cache_set = False
		self.enumConstructors_cache = None
		self.fullQualifiedNameWithOptionalModule_cache_set = False
		self.fullQualifiedNameWithOptionalModule_cache = None
		self.packSuffix_cache_set = False
		self.packSuffix_cache = None
		self.packList_cache_set = False
		self.packList_cache = None
		self.fullPackWithModule_cache_set = False
		self.fullPackWithModule_cache = None
		self.fullPackWithOptionalModule_cache_set = False
		self.fullPackWithOptionalModule_cache = None
		self.toplevelPack_cache_set = False
		self.toplevelPack_cache = None
		self.srcPos_cache_set = False
		self.srcPos_cache = None
		self.strippedEndDeclPos_cache_set = False
		self.strippedEndDeclPos_cache = None
		self.classBodyStart_cache_set = False
		self.classBodyStart_cache = None
		self.publicStaticFunctions_cache_set = False
		self.publicStaticFunctions_cache = None
		self.publicStaticVars_cache_set = False
		self.publicStaticVars_cache = None
		self.allFieldsList_cache_set = False
		self.allFieldsList_cache = None
		self.allFields_cache_set = False
		self.allFields_cache = None
		self.publicStaticFields_cache_set = False
		self.publicStaticFields_cache = None
		self.classBody_cache_set = False
		self.classBody_cache = None
		self.strippedStartDeclPos_cache_set = False
		self.strippedStartDeclPos_cache = None
		self._src = src
		self.src_with_comments = src_with_comments
		self.match_decl = match_decl
		self.is_private = is_private
		self.pack = pack
		self.module = module
		self.kind = kind
		self.name = name
		self.is_module_type = is_module_type
		self.isStdType = is_std_type
		self.isExtern = is_extern
		self._file = file
		self._enumConstructors = None
	
	# var _src
	# var src_with_comments
	# var match_decl
	# var is_private
	# var pack
	# var module
	# var kind
	# var name
	# var is_module_type
	# var isStdType
	# var isExtern
	# var _file
	# var _enumConstructors
	def src(self):
		return self._src

	def file(self):
		return self._file

	# var strippedStartDeclPos_cache
	# var strippedStartDeclPos_cache_set
	def strippedStartDeclPos(self):
		_g = self
		if not self.strippedStartDeclPos_cache_set:
			self.strippedStartDeclPos_cache_set = True
			def _hx_local_0():
				return _g.match_decl.start(0)
			eval = _hx_local_0
			self.strippedStartDeclPos_cache = eval()
		
		
		return self.strippedStartDeclPos_cache
	

	# var classBody_cache
	# var classBody_cache_set
	def classBody(self):
		_g = self
		if not self.classBody_cache_set:
			self.classBody_cache_set = True
			def _hx_local_0():
				res = None
				if _g.strippedEndDeclPos is None:
					res = ""
				else:
					startIndex = _g.strippedStartDeclPos()
					endIndex = _g.strippedEndDeclPos()
					res = python_Tools.substring(_g._src, startIndex, endIndex)
				
				return res
			
			eval = _hx_local_0
			self.classBody_cache = eval()
		
		
		return self.classBody_cache
	

	# var publicStaticFields_cache
	# var publicStaticFields_cache_set
	def publicStaticFields(self):
		_g = self
		if not self.publicStaticFields_cache_set:
			self.publicStaticFields_cache_set = True
			def _hx_local_0():
				res = []
				x = _g.publicStaticVars()
				res.extend(x)
				
				x = _g.publicStaticFunctions()
				res.extend(x)
				
				return res
			
			eval = _hx_local_0
			self.publicStaticFields_cache = eval()
		
		
		return self.publicStaticFields_cache
	

	# var allFields_cache
	# var allFields_cache_set
	def allFields(self):
		_g = self
		if not self.allFields_cache_set:
			self.allFields_cache_set = True
			def _hx_local_1():
				startTime = python_lib_Time.time()
				res = haxe_ds_StringMap()
				if _g.classBody() is not None:
					startPos = None
					_this = _g.classBodyStart()
					startPos = _this[0]
					
					for decl in hxsublime_tools_Regex.fieldRegex.finditer(_g.classBody()):
						modifiers = decl.group(1)
						isStatic = modifiers is not None and modifiers.find("static") > -1
						isInline = modifiers is not None and modifiers.find("inline") > -1
						isPrivate = modifiers is not None and modifiers.find("private") > -1
						isPublic = modifiers is not None and modifiers.find("public") > -1
						def _hx_local_0():
							return hxsublime_tools_HxSrcTools.isSameNestingLevelAtPos(_g.classBody(), decl.start(0), startPos)
						sameNestingLevel = _hx_local_0
						if isPrivate or isPublic or isStatic or _g.isExtern or sameNestingLevel():
							kind = decl.group(2)
							name = decl.group(3)
							res.set(name, hxsublime_tools_HaxeField(_g, name, kind, isStatic, isPublic, isInline, isPrivate, decl))
						
						
						startPos = decl.start(0)
					
				
				
				runTime = python_lib_Time.time() - startTime
				if runTime > 0.02:
					haxe_Log.trace("allFields Time " + _g._file + " : " + Std.string(runTime), _Hx_AnonObject(fileName = "HxSrcTools.hx" ,lineNumber = 1115 ,className = "hxsublime.tools.HaxeType" ,methodName = "allFields" ))
				
				return res
			
			eval = _hx_local_1
			self.allFields_cache = eval()
		
		
		return self.allFields_cache
	

	# var allFieldsList_cache
	# var allFieldsList_cache_set
	def allFieldsList(self):
		_g = self
		if not self.allFieldsList_cache_set:
			self.allFieldsList_cache_set = True
			def _hx_local_0():
				all = _g.allFields()
				_g1 = []
				_it = _hx_functools.partial(HxOverrides_iterator, all)()
				while _it.hasNext():
					e = _it.next()
					_g1.append(e)
					__builtin__.len(_g1)
				
				return _g1
				
			
			eval = _hx_local_0
			self.allFieldsList_cache = eval()
		
		
		return self.allFieldsList_cache
	

	# var publicStaticVars_cache
	# var publicStaticVars_cache_set
	def publicStaticVars(self):
		_g = self
		if not self.publicStaticVars_cache_set:
			self.publicStaticVars_cache_set = True
			def _hx_local_0():
				all = _g.allFields()
				_g1 = []
				_it = _hx_functools.partial(HxOverrides_iterator, all)()
				while _it.hasNext():
					e = _it.next()
					if e.isStatic and e.isVar():
						_g1.append(e)
						__builtin__.len(_g1)
				
					
				return _g1
				
			
			eval = _hx_local_0
			self.publicStaticVars_cache = eval()
		
		
		return self.publicStaticVars_cache
	

	# var publicStaticFunctions_cache
	# var publicStaticFunctions_cache_set
	def publicStaticFunctions(self):
		_g = self
		if not self.publicStaticFunctions_cache_set:
			self.publicStaticFunctions_cache_set = True
			def _hx_local_0():
				all = _g.allFields()
				_g1 = []
				_it = _hx_functools.partial(HxOverrides_iterator, all)()
				while _it.hasNext():
					e = _it.next()
					if e.isStatic and e.isFunction():
						_g1.append(e)
						__builtin__.len(_g1)
				
					
				return _g1
				
			
			eval = _hx_local_0
			self.publicStaticFunctions_cache = eval()
		
		
		return self.publicStaticFunctions_cache
	

	# var classBodyStart_cache
	# var classBodyStart_cache_set
	def classBodyStart(self):
		_g = self
		if not self.classBodyStart_cache_set:
			self.classBodyStart_cache_set = True
			def _hx_local_0():
				start = _g.match_decl.start(0)
				if _g.kind == "abstract" or _g.kind == "class":
					return hxsublime_tools_HxSrcTools.searchNextCharOnSameNestingLevel(_g._src, ["{"], start)
				else:
					return (0, "")
			
			eval = _hx_local_0
			self.classBodyStart_cache = eval()
		
		
		return self.classBodyStart_cache
	

	# var strippedEndDeclPos_cache
	# var strippedEndDeclPos_cache_set
	def strippedEndDeclPos(self):
		_g = self
		if not self.strippedEndDeclPos_cache_set:
			self.strippedEndDeclPos_cache_set = True
			def _hx_local_0():
				classBodyStart = _g.classBodyStart()
				res = None
				if classBodyStart is not None:
					classBodyEnd = hxsublime_tools_HxSrcTools.searchNextCharOnSameNestingLevel(_g._src, ["}"], classBodyStart[0] + 1)
					if classBodyEnd is not None:
						res = classBodyEnd[0]
					else:
						res = None
				
				else:
					res = None
				return res
			
			eval = _hx_local_0
			self.strippedEndDeclPos_cache = eval()
		
		
		return self.strippedEndDeclPos_cache
	

	# var srcPos_cache
	# var srcPos_cache_set
	def srcPos(self):
		_g = self
		if not self.srcPos_cache_set:
			self.srcPos_cache_set = True
			def _hx_local_0():
				for decl in hxsublime_tools_Regex.typeDeclWithScope.finditer(_g.src_with_comments):
					if decl.group(0) == _g.match_decl.group(0):
						return decl.start(0)
					
				return None
			
			eval = _hx_local_0
			self.srcPos_cache = eval()
		
		
		return self.srcPos_cache
	

	def toSnippet(self,insert_file,import_list):
		location = None
		def _hx_local_0():
			_this = self.fullPackWithOptionalModule()
			return __builtin__.len(_this)
		
		if _hx_local_0() > 0:
			location = " (" + self.fullPackWithOptionalModule() + ")"
		else:
			location = ""
		display = self.name + location + "\t" + self.kind
		insert = self.toSnippetInsert(import_list, insert_file)
		return (display, insert)
	

	def toSnippets(self,import_list,insert_file):
		res = [self.toSnippet(insert_file, import_list)]
		if self.kind == "enum" and self._enumConstructors is not None:
			_g = 0
			_g1 = self.enumConstructors()
			while _g < len(_g1):
				ev = _g1[_g]
				_g = _g + 1
				x = ev.toSnippet(insert_file, import_list)
				res.append(x)
				__builtin__.len(res)
				
			
		
		
		return res
	

	def toSnippetInsert(self,import_list,insert_file):
		_g = 0
		while _g < len(import_list):
			i = import_list[_g]
			_g = _g + 1
			if self._file == insert_file or i == self.fullPackWithModule() or i == self.fullQualifiedNameWithOptionalModule() or i == self.fullQualifiedName():
				return self.name
			
		
		
		return self.fullQualifiedNameWithOptionalModule()
	

	# var toplevelPack_cache
	# var toplevelPack_cache_set
	def toplevelPack(self):
		_g = self
		if not self.toplevelPack_cache_set:
			self.toplevelPack_cache_set = True
			def _hx_local_0():
				pl = _g.packList()
				if __builtin__.len(pl) > 0:
					return pl[0]
				
				return None
			
			eval = _hx_local_0
			self.toplevelPack_cache = eval()
		
		
		return self.toplevelPack_cache
	

	def typeHint(self):
		return self.kind

	# var fullPackWithOptionalModule_cache
	# var fullPackWithOptionalModule_cache_set
	def fullPackWithOptionalModule(self):
		_g = self
		if not self.fullPackWithOptionalModule_cache_set:
			self.fullPackWithOptionalModule_cache_set = True
			def _hx_local_0():
				mod = None
				if _g.is_module_type or _g.isStdType:
					mod = ""
				else:
					mod = _g.packSuffix() + _g.module
				return _g.pack + mod
			
			eval = _hx_local_0
			self.fullPackWithOptionalModule_cache = eval()
		
		
		return self.fullPackWithOptionalModule_cache
	

	# var fullPackWithModule_cache
	# var fullPackWithModule_cache_set
	def fullPackWithModule(self):
		_g = self
		if not self.fullPackWithModule_cache_set:
			self.fullPackWithModule_cache_set = True
			def _hx_local_0():
				return _g.pack + _g.packSuffix() + _g.module
			eval = _hx_local_0
			self.fullPackWithModule_cache = eval()
		
		
		return self.fullPackWithModule_cache
	

	def isEnum(self):
		return self.kind == "enum"

	def isClass(self):
		return self.kind == "class"

	def isAbstract(self):
		return self.kind == "abstract"

	# var packList_cache
	# var packList_cache_set
	def packList(self):
		_g = self
		if not self.packList_cache_set:
			self.packList_cache_set = True
			def _hx_local_0():
				if __builtin__.len(_g.pack) > 0:
					return _g.pack.split(".")
				else:
					return []
			eval = _hx_local_0
			self.packList_cache = eval()
		
		
		return self.packList_cache
	

	# var packSuffix_cache
	# var packSuffix_cache_set
	def packSuffix(self):
		_g = self
		if not self.packSuffix_cache_set:
			self.packSuffix_cache_set = True
			def _hx_local_0():
				if __builtin__.len(_g.pack) == 0:
					return ""
				else:
					return "."
			eval = _hx_local_0
			self.packSuffix_cache = eval()
		
		
		return self.packSuffix_cache
	

	# var fullQualifiedNameWithOptionalModule_cache
	# var fullQualifiedNameWithOptionalModule_cache_set
	def fullQualifiedNameWithOptionalModule(self):
		_g = self
		if not self.fullQualifiedNameWithOptionalModule_cache_set:
			self.fullQualifiedNameWithOptionalModule_cache_set = True
			def _hx_local_0():
				mod = None
				if _g.is_module_type or _g.isStdType:
					mod = ""
				else:
					mod = _g.module + "."
				return _g.pack + _g.packSuffix() + mod + _g.name
			
			eval = _hx_local_0
			self.fullQualifiedNameWithOptionalModule_cache = eval()
		
		
		return self.fullQualifiedNameWithOptionalModule_cache
	

	# var enumConstructors_cache
	# var enumConstructors_cache_set
	def enumConstructors(self):
		_g = self
		if not self.enumConstructors_cache_set:
			self.enumConstructors_cache_set = True
			def _hx_local_0():
				res = None
				if _g.kind == "enum" and _g._enumConstructors is not None:
					_g1 = []
					_g2 = 0
					_g3 = _g._enumConstructors
					while _g2 < len(_g3):
						e = _g3[_g2]
						_g2 = _g2 + 1
						x = hxsublime_tools_EnumConstructor(e, _g)
						_g1.append(x)
						__builtin__.len(_g1)
						
					
					
					res = _g1
				
				else:
					res = []
				return res
			
			eval = _hx_local_0
			self.enumConstructors_cache = eval()
		
		
		return self.enumConstructors_cache
	

	# var fullQualifiedEnumConstructorsWithOptionalModule_cache
	# var fullQualifiedEnumConstructorsWithOptionalModule_cache_set
	def fullQualifiedEnumConstructorsWithOptionalModule(self):
		_g = self
		if not self.fullQualifiedEnumConstructorsWithOptionalModule_cache_set:
			self.fullQualifiedEnumConstructorsWithOptionalModule_cache_set = True
			def _hx_local_0():
				res = None
				if not (_g.kind == "enum") or _g._enumConstructors is None:
					res = []
				else:
					fqName = _g.fullQualifiedNameWithOptionalModule()
					_g1 = []
					_g2 = 0
					_g3 = _g._enumConstructors
					while _g2 < len(_g3):
						e = _g3[_g2]
						_g2 = _g2 + 1
						_g1.append(fqName + "." + e)
						__builtin__.len(_g1)
					
					
					res = _g1
					
				
				return res
			
			eval = _hx_local_0
			self.fullQualifiedEnumConstructorsWithOptionalModule_cache = eval()
		
		
		return self.fullQualifiedEnumConstructorsWithOptionalModule_cache
	

	# var classpath_cache
	# var classpath_cache_set
	def classpath(self):
		_g1 = self
		if not self.classpath_cache_set:
			self.classpath_cache_set = True
			def _hx_local_0():
				path_append = None
				_g = []
				_g2 = 0
				_g3 = _g1.packList()
				while _g2 < len(_g3):
					_ = _g3[_g2]
					_g2 = _g2 + 1
					_g.append("..")
					__builtin__.len(_g)
				
				
				path_append = _g
				
				mod_dir = python_lib_os_Path.dirname(_g1._file)
				fp = [mod_dir]
				fp.extend(path_append)
				full_dir = python_lib_Os.sep.join(fp)
				return python_lib_os_Path.normpath(full_dir)
			
			eval = _hx_local_0
			self.classpath_cache = eval()
		
		
		return self.classpath_cache
	

	# var fullQualifiedName_cache
	# var fullQualifiedName_cache_set
	def fullQualifiedName(self):
		_g = self
		if not self.fullQualifiedName_cache_set:
			self.fullQualifiedName_cache_set = True
			def _hx_local_0():
				return _g.pack + _g.packSuffix() + _g.module + "." + _g.name
			eval = _hx_local_0
			self.fullQualifiedName_cache = eval()
		
		
		return self.fullQualifiedName_cache
	

	# var toString_cache
	# var toString_cache_set
	def toString(self):
		_g = self
		if not self.toString_cache_set:
			self.toString_cache_set = True
			def _hx_local_4():
				def _hx_local_3():
					def _hx_local_0():
						_this = _g.enumConstructors()
						def _hx_local_2():
							def _hx_local_1(ec):
								return ec.toString()
							return __builtin__.list(__builtin__.map(_hx_local_1, _this))
						
						return _hx_local_2()
					
					return "{" + " pack:" + Std.string(_g.pack) + ", " + " module:" + Std.string(_g.module) + ", " + " name:" + Std.string(_g.name) + ", " + " kind:" + Std.string(_g.kind) + ", " + " enum_constructors:" + Std.string(_hx_local_0()) + ", " + " is_private:" + Std.string(_g.is_private) + ", " + " is_module_type:" + Std.string(_g.is_module_type) + ", " + " isStdType:" + Std.string(_g.isStdType) + ", " + " is_extern:" + Std.string(_g.isExtern) + ", " + " file:'" + Std.string(_g._file) + "'" + " classpath:'" + Std.string(_g.classpath()) + "'" + " }"
				
				return _hx_local_3()
			
			eval = _hx_local_4
			self.toString_cache = eval()
		
		
		return self.toString_cache
	







hxsublime_tools_HaxeType._hx_class = hxsublime_tools_HaxeType
hxsublime_tools_HaxeType._hx_class_name = "hxsublime.tools.HaxeType"
_hx_classes['hxsublime.tools.HaxeType'] = hxsublime_tools_HaxeType
hxsublime_tools_HaxeType._hx_fields = ["_src","src_with_comments","match_decl","is_private","pack","module","kind","name","is_module_type","isStdType","isExtern","_file","_enumConstructors","strippedStartDeclPos_cache","strippedStartDeclPos_cache_set","classBody_cache","classBody_cache_set","publicStaticFields_cache","publicStaticFields_cache_set","allFields_cache","allFields_cache_set","allFieldsList_cache","allFieldsList_cache_set","publicStaticVars_cache","publicStaticVars_cache_set","publicStaticFunctions_cache","publicStaticFunctions_cache_set","classBodyStart_cache","classBodyStart_cache_set","strippedEndDeclPos_cache","strippedEndDeclPos_cache_set","srcPos_cache","srcPos_cache_set","toplevelPack_cache","toplevelPack_cache_set","fullPackWithOptionalModule_cache","fullPackWithOptionalModule_cache_set","fullPackWithModule_cache","fullPackWithModule_cache_set","packList_cache","packList_cache_set","packSuffix_cache","packSuffix_cache_set","fullQualifiedNameWithOptionalModule_cache","fullQualifiedNameWithOptionalModule_cache_set","enumConstructors_cache","enumConstructors_cache_set","fullQualifiedEnumConstructorsWithOptionalModule_cache","fullQualifiedEnumConstructorsWithOptionalModule_cache_set","classpath_cache","classpath_cache_set","fullQualifiedName_cache","fullQualifiedName_cache_set","toString_cache","toString_cache_set"]
hxsublime_tools_HaxeType._hx_props = []
hxsublime_tools_HaxeType._hx_methods = ["src","file","strippedStartDeclPos","classBody","publicStaticFields","allFields","allFieldsList","publicStaticVars","publicStaticFunctions","classBodyStart","strippedEndDeclPos","srcPos","toSnippet","toSnippets","toSnippetInsert","toplevelPack","typeHint","fullPackWithOptionalModule","fullPackWithModule","isEnum","isClass","isAbstract","packList","packSuffix","fullQualifiedNameWithOptionalModule","enumConstructors","fullQualifiedEnumConstructorsWithOptionalModule","classpath","fullQualifiedName","toString"]
hxsublime_tools_HaxeType._hx_statics = []
hxsublime_tools_HaxeType._hx_interfaces = [hxsublime_macros_LazyFunctionSupport]

# print hxsublime.tools.PathTools.PathTools
class hxsublime_tools_PathTools:

	pass




def PathTools_statics_removeDir(path):
	if python_lib_os_Path.isdir(path):
		python_lib_ShUtil.rmtree(path)
	
hxsublime_tools_PathTools.removeDir = PathTools_statics_removeDir
def PathTools_statics_joinNorm(path1,path2):
	return python_lib_os_Path.normpath(python_lib_os_Path.join(path1, path2))
hxsublime_tools_PathTools.joinNorm = PathTools_statics_joinNorm
def PathTools_statics_isAbsPath(path):
	return python_lib_os_Path.normpath(path) == python_lib_os_Path.abspath(path)
hxsublime_tools_PathTools.isAbsPath = PathTools_statics_isAbsPath


hxsublime_tools_PathTools._hx_class = hxsublime_tools_PathTools
hxsublime_tools_PathTools._hx_class_name = "hxsublime.tools.PathTools"
_hx_classes['hxsublime.tools.PathTools'] = hxsublime_tools_PathTools
hxsublime_tools_PathTools._hx_fields = []
hxsublime_tools_PathTools._hx_props = []
hxsublime_tools_PathTools._hx_methods = []
hxsublime_tools_PathTools._hx_statics = ["removeDir","joinNorm","isAbsPath"]
hxsublime_tools_PathTools._hx_interfaces = []

# print hxsublime.tools.ScopeTools.ScopeTools
class hxsublime_tools_ScopeTools:

	pass




def ScopeTools_statics_containsAny(scopes,scopes_test):
	_g = 0
	while _g < len(scopes):
		s = scopes[_g]
		_g = _g + 1
		def _hx_local_0():
			x = s.split(".")[0]
			return x in scopes_test
		
		if _hx_local_0():
			return True
		
	
	
	return False
	
hxsublime_tools_ScopeTools.containsAny = ScopeTools_statics_containsAny
def ScopeTools_statics_containsStringOrComment(scopes):
	return hxsublime_tools_ScopeTools.containsAny(scopes, ["string", "comments"])
hxsublime_tools_ScopeTools.containsStringOrComment = ScopeTools_statics_containsStringOrComment


hxsublime_tools_ScopeTools._hx_class = hxsublime_tools_ScopeTools
hxsublime_tools_ScopeTools._hx_class_name = "hxsublime.tools.ScopeTools"
_hx_classes['hxsublime.tools.ScopeTools'] = hxsublime_tools_ScopeTools
hxsublime_tools_ScopeTools._hx_fields = []
hxsublime_tools_ScopeTools._hx_props = []
hxsublime_tools_ScopeTools._hx_methods = []
hxsublime_tools_ScopeTools._hx_statics = ["containsAny","containsStringOrComment"]
hxsublime_tools_ScopeTools._hx_interfaces = []

# print hxsublime.tools.StringTools.StringTools
class hxsublime_tools_StringTools:

	pass




hxsublime_tools_StringTools._whitespace = python_lib_Re.compile("^\\s*$")
def StringTools_statics_startsWithAny(s,l):
	_g = 0
	while _g < len(l):
		s1 = l[_g]
		_g = _g + 1
		if StringTools.startsWith(s, s1):
			return True
		
	
	
	return False
	
hxsublime_tools_StringTools.startsWithAny = StringTools_statics_startsWithAny
def StringTools_statics_isWhitespaceOrEmpty(s):
	return python_lib_Re.match(hxsublime_tools_StringTools._whitespace, s) is not None
hxsublime_tools_StringTools.isWhitespaceOrEmpty = StringTools_statics_isWhitespaceOrEmpty


hxsublime_tools_StringTools._hx_class = hxsublime_tools_StringTools
hxsublime_tools_StringTools._hx_class_name = "hxsublime.tools.StringTools"
_hx_classes['hxsublime.tools.StringTools'] = hxsublime_tools_StringTools
hxsublime_tools_StringTools._hx_fields = []
hxsublime_tools_StringTools._hx_props = []
hxsublime_tools_StringTools._hx_methods = []
hxsublime_tools_StringTools._hx_statics = ["_whitespace","startsWithAny","isWhitespaceOrEmpty"]
hxsublime_tools_StringTools._hx_interfaces = []

# print hxsublime.tools.SublimeTools.SublimeTools
class hxsublime_tools_SublimeTools:

	pass




def SublimeTools_statics_getProjectFile(winId = None):
	if winId is None:
		winId = None
	
	if winId is None:
		winId = sublime_Sublime.active_window().id()
	
	return sublime_Sublime.active_window().project_file_name()
	
hxsublime_tools_SublimeTools.getProjectFile = SublimeTools_statics_getProjectFile


hxsublime_tools_SublimeTools._hx_class = hxsublime_tools_SublimeTools
hxsublime_tools_SublimeTools._hx_class_name = "hxsublime.tools.SublimeTools"
_hx_classes['hxsublime.tools.SublimeTools'] = hxsublime_tools_SublimeTools
hxsublime_tools_SublimeTools._hx_fields = []
hxsublime_tools_SublimeTools._hx_props = []
hxsublime_tools_SublimeTools._hx_methods = []
hxsublime_tools_SublimeTools._hx_statics = ["getProjectFile"]
hxsublime_tools_SublimeTools._hx_interfaces = []

# print python.lib.Types.Dict
from builtins import dict as python_lib_Dict
# print hxsublime.tools.ViewTools.AsyncEdit
class hxsublime_tools_AsyncEdit:

	pass




hxsublime_tools_AsyncEdit.dict = python_lib_Dict()
hxsublime_tools_AsyncEdit.id = 0


hxsublime_tools_AsyncEdit._hx_class = hxsublime_tools_AsyncEdit
hxsublime_tools_AsyncEdit._hx_class_name = "hxsublime.tools.AsyncEdit"
_hx_classes['hxsublime.tools.AsyncEdit'] = hxsublime_tools_AsyncEdit
hxsublime_tools_AsyncEdit._hx_fields = []
hxsublime_tools_AsyncEdit._hx_props = []
hxsublime_tools_AsyncEdit._hx_methods = []
hxsublime_tools_AsyncEdit._hx_statics = ["dict","id"]
hxsublime_tools_AsyncEdit._hx_interfaces = []

# print hxsublime.tools.ViewTools.HaxeTextEditCommand
class hxsublime_tools_HaxeTextEditCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**args):
		if args is None:
			args = None
		
		d = args
		id = d.get("id", None)
		haxe_Log.trace(id, _Hx_AnonObject(fileName = "ViewTools.hx" ,lineNumber = 37 ,className = "hxsublime.tools.HaxeTextEditCommand" ,methodName = "run" ))
		if python_lib_DictImpl.hasKey(hxsublime_tools_AsyncEdit.dict, id):
			fun = hxsublime_tools_AsyncEdit.dict.get(id, None)
			python_lib_DictImpl.remove(hxsublime_tools_AsyncEdit.dict, id)
			fun(self.view, edit)
		
		
	





hxsublime_tools_HaxeTextEditCommand._async_edit_dict = None;


hxsublime_tools_HaxeTextEditCommand._hx_class = hxsublime_tools_HaxeTextEditCommand
hxsublime_tools_HaxeTextEditCommand._hx_class_name = "hxsublime.tools.HaxeTextEditCommand"
_hx_classes['hxsublime.tools.HaxeTextEditCommand'] = hxsublime_tools_HaxeTextEditCommand
hxsublime_tools_HaxeTextEditCommand._hx_fields = []
hxsublime_tools_HaxeTextEditCommand._hx_props = []
hxsublime_tools_HaxeTextEditCommand._hx_methods = ["run"]
hxsublime_tools_HaxeTextEditCommand._hx_statics = ["_async_edit_dict"]
hxsublime_tools_HaxeTextEditCommand._hx_interfaces = []
hxsublime_tools_HaxeTextEditCommand._hx_super = sublime_TextCommand

# print hxsublime.tools.ViewTools.ViewTools
class hxsublime_tools_ViewTools:

	pass




def ViewTools_statics_insertSnippet(view,snippet):
	def _hx_local_0():
		x = _Hx_AnonObject(contents = snippet )
		def _hx_local_2():
			def _hx_local_1():
				d = python_lib_Dict()
				_g = 0
				_g1 = Reflect.fields(x)
				while _g < len(_g1):
					f = _g1[_g]
					_g = _g + 1
					val = Reflect.field(x, f)
					python_lib_DictImpl.set(d, f, val)
					
				
				
				return d
			
			return _hx_local_1()
		
		return _hx_local_2()
	
	view.run_command("insert_snippet", _hx_local_0())
	
hxsublime_tools_ViewTools.insertSnippet = ViewTools_statics_insertSnippet
def ViewTools_statics_insertAtCursor(view,txt):
	def _hx_local_0(v,e):
		v.insert(e, hxsublime_tools_ViewTools.getFirstCursorPos(v), txt)
	doEdit = _hx_local_0
	hxsublime_tools_ViewTools.asyncEdit(view, doEdit)
	
hxsublime_tools_ViewTools.insertAtCursor = ViewTools_statics_insertAtCursor
def ViewTools_statics_getFirstCursorPos(view):
	return view.sel()[0].begin()
hxsublime_tools_ViewTools.getFirstCursorPos = ViewTools_statics_getFirstCursorPos
def ViewTools_statics_asyncEdit(view,doEdit):
	def _hx_local_3():
		id = hxsublime_tools_AsyncEdit.id
		if hxsublime_tools_AsyncEdit.id > 1000000:
			hxsublime_tools_AsyncEdit.id = 0
		else:
			hxsublime_tools_AsyncEdit.id = hxsublime_tools_AsyncEdit.id + 1
		python_lib_DictImpl.set(hxsublime_tools_AsyncEdit.dict, id, doEdit)
		def _hx_local_0():
			x = _Hx_AnonObject(id = id )
			def _hx_local_2():
				def _hx_local_1():
					d = python_lib_Dict()
					_g = 0
					_g1 = Reflect.fields(x)
					while _g < len(_g1):
						f = _g1[_g]
						_g = _g + 1
						val = Reflect.field(x, f)
						python_lib_DictImpl.set(d, f, val)
						
					
					
					return d
				
				return _hx_local_1()
			
			return _hx_local_2()
		
		view.run_command("hxsublime_tools__haxe_text_edit", _hx_local_0())
	
	start = _hx_local_3
	sublime_Sublime.set_timeout(start, 10)
	
hxsublime_tools_ViewTools.asyncEdit = ViewTools_statics_asyncEdit
def ViewTools_statics_findViewByName(name):
	windows = sublime_Sublime.windows()
	_g = 0
	while _g < len(windows):
		w = windows[_g]
		_g = _g + 1
		views = w.views()
		_g1 = 0
		while _g1 < len(views):
			v = views[_g1]
			_g1 = _g1 + 1
			if v.name() == name:
				return v
			
		
		
	
	
	return None
	
hxsublime_tools_ViewTools.findViewByName = ViewTools_statics_findViewByName
def ViewTools_statics_createMissingFolders(view):
	fn = view.file_name()
	path = python_lib_os_Path.dirname(fn)
	if not python_lib_os_Path.isdir(path):
		python_lib_Os.makedirs(path)
	
	
hxsublime_tools_ViewTools.createMissingFolders = ViewTools_statics_createMissingFolders
def ViewTools_statics_getContentUntilFirstCursor(view):
	end = hxsublime_tools_ViewTools.getFirstCursorPos(view)
	return hxsublime_tools_ViewTools.getContentUntil(view, end)
	
hxsublime_tools_ViewTools.getContentUntilFirstCursor = ViewTools_statics_getContentUntilFirstCursor
def ViewTools_statics_getContentUntil(view,endPos):
	return view.substr(sublime_Region(0, endPos))
hxsublime_tools_ViewTools.getContentUntil = ViewTools_statics_getContentUntil
def ViewTools_statics_getContent(view):
	return view.substr(sublime_Region(0, view.size()))
hxsublime_tools_ViewTools.getContent = ViewTools_statics_getContent
def ViewTools_statics_isHxsl(view):
	return StringTools.endsWith(view.file_name(), hxsublime_Config.HXSL_SUFFIX)
hxsublime_tools_ViewTools.isHxsl = ViewTools_statics_isHxsl
def ViewTools_statics_isSupported(view):
	return view.score_selector(0, hxsublime_Config.SOURCE_HAXE + "," + hxsublime_Config.SOURCE_HXML + "," + hxsublime_Config.SOURCE_ERAZOR + "," + hxsublime_Config.SOURCE_NMML) > 0
hxsublime_tools_ViewTools.isSupported = ViewTools_statics_isSupported
def ViewTools_statics_isUnsupported(view):
	return not hxsublime_tools_ViewTools.isSupported(view)
hxsublime_tools_ViewTools.isUnsupported = ViewTools_statics_isUnsupported
def ViewTools_statics_getScopesAt(view,pos):
	return view.scope_name(pos).split(" ")
hxsublime_tools_ViewTools.getScopesAt = ViewTools_statics_getScopesAt
def ViewTools_statics_isHaxe(view):
	return view.score_selector(0, hxsublime_Config.SOURCE_HAXE) > 0
hxsublime_tools_ViewTools.isHaxe = ViewTools_statics_isHaxe
def ViewTools_statics_isHxml(view):
	return view.score_selector(0, hxsublime_Config.SOURCE_HXML) > 0
hxsublime_tools_ViewTools.isHxml = ViewTools_statics_isHxml
def ViewTools_statics_isErazor(view):
	return view.score_selector(0, hxsublime_Config.SOURCE_ERAZOR) > 0
hxsublime_tools_ViewTools.isErazor = ViewTools_statics_isErazor
def ViewTools_statics_isNmml(view):
	return view.score_selector(0, hxsublime_Config.SOURCE_NMML) > 0
hxsublime_tools_ViewTools.isNmml = ViewTools_statics_isNmml
def ViewTools_statics_replaceContent(view,newContent):
	def _hx_local_0(view1,edit):
		view1.replace(edit, sublime_Region(0, view1.size()), newContent)
	doEdit = _hx_local_0
	view.set_read_only(False)
	hxsublime_tools_ViewTools.asyncEdit(view, doEdit)
	
hxsublime_tools_ViewTools.replaceContent = ViewTools_statics_replaceContent
def ViewTools_statics_inHaxeCode(view,caret):
	return view.score_selector(caret, "source.haxe") > 0 and view.score_selector(caret, "string") == 0 and view.score_selector(caret, "comment") == 0
hxsublime_tools_ViewTools.inHaxeCode = ViewTools_statics_inHaxeCode
def ViewTools_statics_inHaxeString(view,caret):
	return view.score_selector(caret, "source.haxe") > 0 and view.score_selector(caret, "string") > 0
hxsublime_tools_ViewTools.inHaxeString = ViewTools_statics_inHaxeString
def ViewTools_statics_inHaxeComments(view,caret):
	return view.score_selector(caret, "source.haxe") > 0 and view.score_selector(caret, "comment") > 0
hxsublime_tools_ViewTools.inHaxeComments = ViewTools_statics_inHaxeComments


hxsublime_tools_ViewTools._hx_class = hxsublime_tools_ViewTools
hxsublime_tools_ViewTools._hx_class_name = "hxsublime.tools.ViewTools"
_hx_classes['hxsublime.tools.ViewTools'] = hxsublime_tools_ViewTools
hxsublime_tools_ViewTools._hx_fields = []
hxsublime_tools_ViewTools._hx_props = []
hxsublime_tools_ViewTools._hx_methods = []
hxsublime_tools_ViewTools._hx_statics = ["insertSnippet","insertAtCursor","getFirstCursorPos","asyncEdit","findViewByName","createMissingFolders","getContentUntilFirstCursor","getContentUntil","getContent","isHxsl","isSupported","isUnsupported","getScopesAt","isHaxe","isHxml","isErazor","isNmml","replaceContent","inHaxeCode","inHaxeString","inHaxeComments"]
hxsublime_tools_ViewTools._hx_interfaces = []

# print js.Boot.Boot
# print python.Boot.Boot
class python_Boot:

	pass




def Boot_statics_isClass(o):
	return o._hx_class
python_Boot.isClass = Boot_statics_isClass
def Boot_statics___string_rec(o,s):
	if s is None:
		s = ""
	
	if o is None:
		return "null"
	
	if __builtin__.len(s) >= 5:
		return "<...>"
	
	builtin = __builtin__
	inspect = python_lib_Inspect
	if builtin.isinstance(o, String):
		return o
	
	if builtin.isinstance(o, bool):
		if o:
			return "true"
		else:
			return "false"
	
	if builtin.isinstance(o, int):
		return __builtin__.str(o)
	
	if builtin.isinstance(o, float):
		return __builtin__.str(o)
	
	if inspect.isfunction(o) or inspect.ismethod(o):
		return "<function>"
	
	if builtin.isinstance(o, list):
		o1 = o
		l = __builtin__.len(o1)
		st = "["
		s = s + "\t"
		_g = 0
		while _g < l:
			def _hx_local_1():
				nonlocal _g
				_hx_local_0 = _g
				_g = _g + 1
				return _hx_local_0
				
			
			i = _hx_local_1()
			prefix = ""
			if i > 0:
				prefix = ","
			
			st = st + prefix + python_Boot.__string_rec(o1[i], s)
		
		
		st = st + "]"
		return st
	
	
	if builtin.hasattr(o, "toString"):
		return o.toString()
	
	if builtin.hasattr(o, "__class__"):
		if builtin.isinstance(o, _Hx_AnonObject):
			toStr = None
			try:
				fields = Reflect.fields(o)
				fieldsStr = None
				_g = []
				_g1 = 0
				while _g1 < len(fields):
					f = fields[_g1]
					_g1 = _g1 + 1
					x = "" + f + " : " + python_Boot.__string_rec(Reflect.field(o, f), s + "\t")
					_g.append(x)
					__builtin__.len(_g)
					
				
				
				fieldsStr = _g
				
				toStr = "{ " + ", ".join(fieldsStr) + " }"
			
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				if True:
					e = _hx_e1
					haxe_Log.trace(e, _Hx_AnonObject(fileName = "Boot.hx" ,lineNumber = 77 ,className = "python.Boot" ,methodName = "__string_rec" ))
				else:
					raise _hx_e
			if toStr is None:
				return "{ ... }"
			else:
				return toStr
		
		
		if builtin.isinstance(o, _Hx_Enum):
			l = builtin.len(o.params)
			hasParams = l > 0
			if hasParams:
				paramsStr = ""
				_g = 0
				while _g < l:
					def _hx_local_3():
						nonlocal _g
						_hx_local_2 = _g
						_g = _g + 1
						return _hx_local_2
						
					
					i = _hx_local_3()
					prefix = ""
					if i > 0:
						prefix = ","
					
					paramsStr = paramsStr + prefix + python_Boot.__string_rec(o.params[i], s)
				
				
				return Std.string(o.tag) + "(" + paramsStr + ")"
			
			else:
				return o.tag
		
		
		if builtin.hasattr(o, "_hx_class_name") and o.__class__.__name__ != "type":
			fields = Type.getInstanceFields(o)
			fieldsStr = None
			_g = []
			_g1 = 0
			while _g1 < len(fields):
				f = fields[_g1]
				_g1 = _g1 + 1
				x = "" + f + " : " + python_Boot.__string_rec(Reflect.field(o, f), s + "\t")
				_g.append(x)
				__builtin__.len(_g)
				
			
			
			fieldsStr = _g
			
			toStr = Std.string(o._hx_class_name) + "( " + ", ".join(fieldsStr) + " )"
			return toStr
		
		
		if builtin.hasattr(o, "_hx_class_name") and o.__class__.__name__ == "type":
			fields = Type.getClassFields(o)
			fieldsStr = None
			_g = []
			_g1 = 0
			while _g1 < len(fields):
				f = fields[_g1]
				_g1 = _g1 + 1
				x = "" + f + " : " + python_Boot.__string_rec(Reflect.field(o, f), s + "\t")
				_g.append(x)
				__builtin__.len(_g)
				
			
			
			fieldsStr = _g
			
			toStr = "#" + Std.string(o._hx_class_name) + "( " + ", ".join(fieldsStr) + " )"
			return toStr
		
		
		if o == String:
			return "#String"
		
		if builtin.hasattr(o, "__repr__"):
			return o.__repr__()
		
		if builtin.hasattr(o, "__str__"):
			return o.__str__()
		
		if builtin.hasattr(o, "__name__"):
			return o.__name__
		
		return "???"
	
	else:
		try:
			def _hx_local_4(_):
				return True
			python_lib_Inspect.getmembers(o, _hx_local_4)
			return __builtin__.str(o)
	
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			if True:
				e = _hx_e1
				return "???"
			else:
				raise _hx_e
	
python_Boot.__string_rec = Boot_statics___string_rec


python_Boot._hx_class = python_Boot
python_Boot._hx_class_name = "python.Boot"
_hx_classes['python.Boot'] = python_Boot
python_Boot._hx_fields = []
python_Boot._hx_props = []
python_Boot._hx_methods = []
python_Boot._hx_statics = ["isClass","__string_rec"]
python_Boot._hx_interfaces = []

# print python.Lib.HaxeIterable
class python_HaxeIterable:


	def __init__(self,x):
		self.x = x
	# var x
	def iterator(self):
		return python_HaxeIterator(self.x.__iter__())







python_HaxeIterable._hx_class = python_HaxeIterable
python_HaxeIterable._hx_class_name = "python.HaxeIterable"
_hx_classes['python.HaxeIterable'] = python_HaxeIterable
python_HaxeIterable._hx_fields = ["x"]
python_HaxeIterable._hx_props = []
python_HaxeIterable._hx_methods = ["iterator"]
python_HaxeIterable._hx_statics = []
python_HaxeIterable._hx_interfaces = []

# print python.Lib.HaxeIterator
class python_HaxeIterator:


	def __init__(self,it):
		self.checked = False
		self.x = None
		self.it = it
	
	# var it
	# var x
	# var checked
	def next(self):
		self.checked = False
		return self.x
	

	def hasNext(self):
		if self.checked:
			return self.x is not None
		else:
			try:
				self.x = self.it.__next__()
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				if isinstance(_hx_e1, StopIteration):
					s = _hx_e1
					self.x = None
				else:
					raise _hx_e
			self.checked = True
			return self.x is not None
	







python_HaxeIterator._hx_class = python_HaxeIterator
python_HaxeIterator._hx_class_name = "python.HaxeIterator"
_hx_classes['python.HaxeIterator'] = python_HaxeIterator
python_HaxeIterator._hx_fields = ["it","x","checked"]
python_HaxeIterator._hx_props = []
python_HaxeIterator._hx_methods = ["next","hasNext"]
python_HaxeIterator._hx_statics = []
python_HaxeIterator._hx_interfaces = []

# print python.Lib.Lib
class python_Lib:

	pass




def Lib_statics__hx_print(v):
	python_lib_Sys.stdout.write(Std.string(v))
	python_lib_Sys.stdout.flush()
	
python_Lib._hx_print = Lib_statics__hx_print
def Lib_statics_println(v):
	_g = 0
	while _g < len(v):
		e = v[_g]
		_g = _g + 1
		print(Std.string(e))
	
	
python_Lib.println = Lib_statics_println
def Lib_statics_toPythonIterable(it):
	def _hx_local_3():
		def _hx_local_2():
			it1 = _hx_functools.partial(HxOverrides_iterator, it)()
			self = None
			def _hx_local_0():
				if it1.hasNext():
					return it1.next()
				else:
					raise _HxException(StopIteration())
			def _hx_local_1():
				return self
			self = _Hx_AnonObject(__next__ = _hx_local_0 ,__iter__ = _hx_local_1 )
			return self
		
		return _Hx_AnonObject(__iter__ = _hx_local_2 )
	
	return _hx_local_3()
	
python_Lib.toPythonIterable = Lib_statics_toPythonIterable
def Lib_statics_toHaxeIterable(it):
	return python_HaxeIterable(it)
python_Lib.toHaxeIterable = Lib_statics_toHaxeIterable
def Lib_statics_toHaxeIterator(it):
	return python_HaxeIterator(it)
python_Lib.toHaxeIterator = Lib_statics_toHaxeIterator


python_Lib._hx_class = python_Lib
python_Lib._hx_class_name = "python.Lib"
_hx_classes['python.Lib'] = python_Lib
python_Lib._hx_fields = []
python_Lib._hx_props = []
python_Lib._hx_methods = []
python_Lib._hx_statics = ["print","println","toPythonIterable","toHaxeIterable","toHaxeIterator"]
python_Lib._hx_interfaces = []

# print python.Macros.Macros
class python_Macros:

	pass






python_Macros._hx_class = python_Macros
python_Macros._hx_class_name = "python.Macros"
_hx_classes['python.Macros'] = python_Macros
python_Macros._hx_fields = []
python_Macros._hx_props = []
python_Macros._hx_methods = []
python_Macros._hx_statics = []
python_Macros._hx_interfaces = []

# print python.Tools.Tools
class python_Tools:

	pass




def Tools_statics_substring(s,startIndex,endIndex = None):
	if endIndex is None:
		endIndex = None
	
	return s[startIndex:endIndex]
	
python_Tools.substring = Tools_statics_substring
def Tools_statics_substr(s,startIndex,len = None):
	if len is None:
		len = None
	
	if len is None:
		return s[startIndex:]
	else:
		return s[startIndex:startIndex+len]
	
python_Tools.substr = Tools_statics_substr


python_Tools._hx_class = python_Tools
python_Tools._hx_class_name = "python.Tools"
_hx_classes['python.Tools'] = python_Tools
python_Tools._hx_fields = []
python_Tools._hx_props = []
python_Tools._hx_methods = []
python_Tools._hx_statics = ["substring","substr"]
python_Tools._hx_interfaces = []

# print python.internal.ArrayImpl.ArrayImpl
class python_internal_ArrayImpl:

	pass




def ArrayImpl_statics_get_length(x):
	return __builtin__.len(x)
python_internal_ArrayImpl.get_length = ArrayImpl_statics_get_length
def ArrayImpl_statics_concat(a1,a2):
	return a1 + a2
python_internal_ArrayImpl.concat = ArrayImpl_statics_concat
def ArrayImpl_statics_copy(x):
	return __builtin__.list(x)
python_internal_ArrayImpl.copy = ArrayImpl_statics_copy
def ArrayImpl_statics_iterator(x):
	it = x.__iter__()
	return python_HaxeIterator(it)
	
python_internal_ArrayImpl.iterator = ArrayImpl_statics_iterator
def ArrayImpl_statics_join(x,sep):
	return sep.join(x)
python_internal_ArrayImpl.join = ArrayImpl_statics_join
def ArrayImpl_statics_toString(x):
	return str(x)
python_internal_ArrayImpl.toString = ArrayImpl_statics_toString
def ArrayImpl_statics_pop(x):
	if __builtin__.len(x) == 0:
		return None
	else:
		return x.pop()
python_internal_ArrayImpl.pop = ArrayImpl_statics_pop
def ArrayImpl_statics_push(x,e):
	x.append(e)
	return __builtin__.len(x)
	
python_internal_ArrayImpl.push = ArrayImpl_statics_push
def ArrayImpl_statics_unshift(x,e):
	return x.insert(0, e)
python_internal_ArrayImpl.unshift = ArrayImpl_statics_unshift
def ArrayImpl_statics_remove(x,e):
	try:
		x.remove(e)
		return True
	
	except Exception as _hx_e:
		_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
		if True:
			e1 = _hx_e1
			return False
		else:
			raise _hx_e
python_internal_ArrayImpl.remove = ArrayImpl_statics_remove
def ArrayImpl_statics_shift(x):
	return x.pop(0)
python_internal_ArrayImpl.shift = ArrayImpl_statics_shift
def ArrayImpl_statics_slice(x,pos,end = None):
	if end is None:
		end = None
	
	return x[pos:end]
	
python_internal_ArrayImpl.slice = ArrayImpl_statics_slice
def ArrayImpl_statics_sort(x,f):
	return x.sort(key=python_lib_FuncTools.cmp_to_key(f))
python_internal_ArrayImpl.sort = ArrayImpl_statics_sort
def ArrayImpl_statics_splice(x,pos,len):
	res = x[pos:pos + len]
	del x[pos:pos + len]
	return res
	
python_internal_ArrayImpl.splice = ArrayImpl_statics_splice
def ArrayImpl_statics_map(x,f):
	return __builtin__.list(__builtin__.map(f, x))
python_internal_ArrayImpl.map = ArrayImpl_statics_map
def ArrayImpl_statics_filter(x,f):
	return __builtin__.list(__builtin__.filter(f, x))
python_internal_ArrayImpl.filter = ArrayImpl_statics_filter
def ArrayImpl_statics___get(x,idx):
	_hx_a = x
	if idx >= __builtin__.len(_hx_a) or idx < 0:
		return None
	else:
		return x[idx]
	
python_internal_ArrayImpl.__get = ArrayImpl_statics___get
def ArrayImpl_statics___set(x,idx,v):
	_hx_a = x
	_hx_a[idx] = v
	return v
	
python_internal_ArrayImpl.__set = ArrayImpl_statics___set
def ArrayImpl_statics___unsafe_get(x,idx):
	return x[idx]
python_internal_ArrayImpl.__unsafe_get = ArrayImpl_statics___unsafe_get
def ArrayImpl_statics___unsafe_set(x,idx,val):
	x[idx] = val
	return val
	
python_internal_ArrayImpl.__unsafe_set = ArrayImpl_statics___unsafe_set


python_internal_ArrayImpl._hx_class = python_internal_ArrayImpl
python_internal_ArrayImpl._hx_class_name = "python.internal.ArrayImpl"
_hx_classes['python.internal.ArrayImpl'] = python_internal_ArrayImpl
python_internal_ArrayImpl._hx_fields = []
python_internal_ArrayImpl._hx_props = []
python_internal_ArrayImpl._hx_methods = []
python_internal_ArrayImpl._hx_statics = ["get_length","concat","copy","iterator","join","toString","pop","push","unshift","remove","shift","slice","sort","splice","map","filter","__get","__set","__unsafe_get","__unsafe_set"]
python_internal_ArrayImpl._hx_interfaces = []

# print python.internal.KeywordHandler.KeywordHandler
class python_internal_KeywordHandler:

	pass




def _hx_init_python_internal_KeywordHandler_keywords():
	_g = haxe_ds_StringMap()
	_g.set("and", True)
	_g.set("del", True)
	_g.set("from", True)
	_g.set("not", True)
	_g.set("while", True)
	_g.set("as", True)
	_g.set("elif", True)
	_g.set("global", True)
	_g.set("or", True)
	_g.set("with", True)
	_g.set("assert", True)
	_g.set("else", True)
	_g.set("if", True)
	_g.set("pass", True)
	_g.set("yield", True)
	_g.set("break", True)
	_g.set("except", True)
	_g.set("import", True)
	_g.set("print", True)
	_g.set("float", True)
	_g.set("class", True)
	_g.set("exec", True)
	_g.set("in", True)
	_g.set("raise", True)
	_g.set("continue", True)
	_g.set("finally", True)
	_g.set("is", True)
	_g.set("return", True)
	_g.set("def", True)
	_g.set("for", True)
	_g.set("lambda", True)
	_g.set("try", True)
	return _g
	
python_internal_KeywordHandler.keywords = _hx_init_python_internal_KeywordHandler_keywords()
def KeywordHandler_statics_handleKeywords(name):
	if python_internal_KeywordHandler.keywords.exists(name):
		return "_hx_" + name
	
	return name
	
python_internal_KeywordHandler.handleKeywords = KeywordHandler_statics_handleKeywords
def KeywordHandler_statics_unhandleKeywords(name):
	if python_Tools.substr(name, 0, 4) == "_hx_":
		real = python_Tools.substr(name, 4, None)
		if python_internal_KeywordHandler.keywords.exists(real):
			return real
		
	
	
	return name
	
python_internal_KeywordHandler.unhandleKeywords = KeywordHandler_statics_unhandleKeywords


python_internal_KeywordHandler._hx_class = python_internal_KeywordHandler
python_internal_KeywordHandler._hx_class_name = "python.internal.KeywordHandler"
_hx_classes['python.internal.KeywordHandler'] = python_internal_KeywordHandler
python_internal_KeywordHandler._hx_fields = []
python_internal_KeywordHandler._hx_props = []
python_internal_KeywordHandler._hx_methods = []
python_internal_KeywordHandler._hx_statics = ["keywords","handleKeywords","unhandleKeywords"]
python_internal_KeywordHandler._hx_interfaces = []

# print python.lib.ArrayTools.ArrayTools
class python_lib_ArrayTools:

	pass




def ArrayTools_statics_extend(a,x):
	a.extend(x)
python_lib_ArrayTools.extend = ArrayTools_statics_extend
def ArrayTools_statics_append(a,x):
	a.append(x)
python_lib_ArrayTools.append = ArrayTools_statics_append
def ArrayTools_statics_contains(a,x):
	return x in a
python_lib_ArrayTools.contains = ArrayTools_statics_contains


python_lib_ArrayTools._hx_class = python_lib_ArrayTools
python_lib_ArrayTools._hx_class_name = "python.lib.ArrayTools"
_hx_classes['python.lib.ArrayTools'] = python_lib_ArrayTools
python_lib_ArrayTools._hx_fields = []
python_lib_ArrayTools._hx_props = []
python_lib_ArrayTools._hx_methods = []
python_lib_ArrayTools._hx_statics = ["extend","append","contains"]
python_lib_ArrayTools._hx_interfaces = []

# print python.lib.Codecs.Codec
# print python.lib.Codecs.StreamReader
# print python.lib.Codecs.StreamWriter
# print python.lib.Codecs.StreamReaderWriterText
# print python.lib.Codecs.Codecs
import codecs as python_lib_Codecs
# print python.lib.FuncTools.FuncTools
import functools as python_lib_FuncTools
# print python.lib.Glob.Glob
import glob as python_lib_Glob
# print python.lib.Inspect.Inspect
import inspect as python_lib_Inspect
# print python.lib.Json.Json
import json as python_lib_Json
# print python.lib.Os.Stat
# print python.lib.Os.Os
import os as python_lib_Os
# print python.lib.PPrint.PPrint
import pprint as python_lib_PPrint
# print python.lib.Random.Random
import random as python_lib_Random
# print python.lib.Re.MatchObject
# print python.lib.Re.RegexHelper
class python_lib_Re_RegexHelper:

	pass




def RegexHelper_statics_findallDynamic(r,string,pos = None,endpos = None):
	if pos is None:
		pos = None
	
	if endpos is None:
		endpos = None
	
	if endpos is None:
		if pos is None:
			return r.findall(string)
		else:
			return r.findall(string, pos)
	else:
		return r.findall(string, pos, endpos)
	
python_lib_Re_RegexHelper.findallDynamic = RegexHelper_statics_findallDynamic


python_lib_Re_RegexHelper._hx_class = python_lib_Re_RegexHelper
python_lib_Re_RegexHelper._hx_class_name = "python.lib._Re._Re.RegexHelper"
_hx_classes['python.lib._Re._Re.RegexHelper'] = python_lib_Re_RegexHelper
python_lib_Re_RegexHelper._hx_fields = []
python_lib_Re_RegexHelper._hx_props = []
python_lib_Re_RegexHelper._hx_methods = []
python_lib_Re_RegexHelper._hx_statics = ["findallDynamic"]
python_lib_Re_RegexHelper._hx_interfaces = []

# print python.lib.Re.Regex
# print python.lib.ShUtil.ShUtil
import shutil as python_lib_ShUtil
# print python.lib.StringTools.StringTools
class python_lib_StringTools:

	pass




def StringTools_statics_format(s,args):
	return s.format(*args)
python_lib_StringTools.format = StringTools_statics_format
def StringTools_statics_encode(s,encoding = "utf-8",errors = "strict"):
	if encoding is None:
		encoding = "utf-8"
	
	if errors is None:
		errors = "strict"
	
	return s.encode(encoding, errors)
	
python_lib_StringTools.encode = StringTools_statics_encode
def StringTools_statics_contains(s,e):
	return e in s
python_lib_StringTools.contains = StringTools_statics_contains
def StringTools_statics_strip(s,chars = None):
	if chars is None:
		chars = None
	
	return s.strip(chars)
	
python_lib_StringTools.strip = StringTools_statics_strip
def StringTools_statics_rpartition(s,sep):
	return s.rpartition(sep)
python_lib_StringTools.rpartition = StringTools_statics_rpartition


python_lib_StringTools._hx_class = python_lib_StringTools
python_lib_StringTools._hx_class_name = "python.lib.StringTools"
_hx_classes['python.lib.StringTools'] = python_lib_StringTools
python_lib_StringTools._hx_fields = []
python_lib_StringTools._hx_props = []
python_lib_StringTools._hx_methods = []
python_lib_StringTools._hx_statics = ["format","encode","contains","strip","rpartition"]
python_lib_StringTools._hx_interfaces = []

# print python.lib.Subprocess.StartupInfo
# print python.lib.Subprocess.Subprocess
import subprocess as python_lib_Subprocess
# print python.lib.Sys.Sys
import sys as python_lib_Sys
# print python.lib.Tempfile.Tempfile
import tempfile as python_lib_Tempfile
# print python.lib.ThreadLowLevel.ThreadLowLevel
import _thread as python_lib_ThreadLowLevel
# print python.lib.Time.Time
import time as python_lib_Time
# print python.lib.Types.Choice_Impl_
class python_lib_Types_Choice_Impl_:

	pass




def Choice_Impl__statics_fromA(x):
	return x
python_lib_Types_Choice_Impl_.fromA = Choice_Impl__statics_fromA
def Choice_Impl__statics_fromB(x):
	return x
python_lib_Types_Choice_Impl_.fromB = Choice_Impl__statics_fromB


python_lib_Types_Choice_Impl_._hx_class = python_lib_Types_Choice_Impl_
python_lib_Types_Choice_Impl_._hx_class_name = "python.lib._Types._Types.Choice_Impl_"
_hx_classes['python.lib._Types._Types.Choice_Impl_'] = python_lib_Types_Choice_Impl_
python_lib_Types_Choice_Impl_._hx_fields = []
python_lib_Types_Choice_Impl_._hx_props = []
python_lib_Types_Choice_Impl_._hx_methods = []
python_lib_Types_Choice_Impl_._hx_statics = ["fromA","fromB"]
python_lib_Types_Choice_Impl_._hx_interfaces = []

# print python.lib.Types.KwArgs_Impl_
class python_lib_Types_KwArgs_Impl_:

	pass




def KwArgs_Impl__statics_get(this1,key,_hx_def):
	return this1.get(key, _hx_def)
python_lib_Types_KwArgs_Impl_.get = KwArgs_Impl__statics_get


python_lib_Types_KwArgs_Impl_._hx_class = python_lib_Types_KwArgs_Impl_
python_lib_Types_KwArgs_Impl_._hx_class_name = "python.lib._Types._Types.KwArgs_Impl_"
_hx_classes['python.lib._Types._Types.KwArgs_Impl_'] = python_lib_Types_KwArgs_Impl_
python_lib_Types_KwArgs_Impl_._hx_fields = []
python_lib_Types_KwArgs_Impl_._hx_props = []
python_lib_Types_KwArgs_Impl_._hx_methods = []
python_lib_Types_KwArgs_Impl_._hx_statics = ["get"]
python_lib_Types_KwArgs_Impl_._hx_interfaces = []

# print python.lib.Types.VarArgs_Impl_
# print python.lib.Types.ByteArray
# print python.lib.Types.Bytes
from builtins import bytes as python_lib_Bytes
# print python.lib.Types.PyIterator_Impl_
class python_lib_Types_PyIterator_Impl_:

	pass




def PyIterator_Impl__statics__new(p):
	return p
python_lib_Types_PyIterator_Impl_._new = PyIterator_Impl__statics__new
def PyIterator_Impl__statics_toHaxeIterator(p):
	return python_HaxeIterator(p)
python_lib_Types_PyIterator_Impl_.toHaxeIterator = PyIterator_Impl__statics_toHaxeIterator
def PyIterator_Impl__statics_toPyIterable(p):
	return p
python_lib_Types_PyIterator_Impl_.toPyIterable = PyIterator_Impl__statics_toPyIterable
def PyIterator_Impl__statics_getNativeIterator(this1):
	return this1
python_lib_Types_PyIterator_Impl_.getNativeIterator = PyIterator_Impl__statics_getNativeIterator


python_lib_Types_PyIterator_Impl_._hx_class = python_lib_Types_PyIterator_Impl_
python_lib_Types_PyIterator_Impl_._hx_class_name = "python.lib._Types._Types.PyIterator_Impl_"
_hx_classes['python.lib._Types._Types.PyIterator_Impl_'] = python_lib_Types_PyIterator_Impl_
python_lib_Types_PyIterator_Impl_._hx_fields = []
python_lib_Types_PyIterator_Impl_._hx_props = []
python_lib_Types_PyIterator_Impl_._hx_methods = []
python_lib_Types_PyIterator_Impl_._hx_statics = ["_new","toHaxeIterator","toPyIterable","getNativeIterator"]
python_lib_Types_PyIterator_Impl_._hx_interfaces = []

# print python.lib.Types.PyIterable_Impl_
class python_lib_Types_PyIterable_Impl_:

	pass




def PyIterable_Impl__statics_toHaxeIterable(p):
	return python_HaxeIterable(p)
python_lib_Types_PyIterable_Impl_.toHaxeIterable = PyIterable_Impl__statics_toHaxeIterable
def PyIterable_Impl__statics_iterator(this1):
	_this_x = this1
	return python_HaxeIterator(_this_x.__iter__())
	
python_lib_Types_PyIterable_Impl_.iterator = PyIterable_Impl__statics_iterator
def PyIterable_Impl__statics_getNativeIterable(this1):
	return this1
python_lib_Types_PyIterable_Impl_.getNativeIterable = PyIterable_Impl__statics_getNativeIterable
def PyIterable_Impl__statics_getNativeIterator(this1):
	return this1.__iter__()
python_lib_Types_PyIterable_Impl_.getNativeIterator = PyIterable_Impl__statics_getNativeIterator


python_lib_Types_PyIterable_Impl_._hx_class = python_lib_Types_PyIterable_Impl_
python_lib_Types_PyIterable_Impl_._hx_class_name = "python.lib._Types._Types.PyIterable_Impl_"
_hx_classes['python.lib._Types._Types.PyIterable_Impl_'] = python_lib_Types_PyIterable_Impl_
python_lib_Types_PyIterable_Impl_._hx_fields = []
python_lib_Types_PyIterable_Impl_._hx_props = []
python_lib_Types_PyIterable_Impl_._hx_methods = []
python_lib_Types_PyIterable_Impl_._hx_statics = ["toHaxeIterable","iterator","getNativeIterable","getNativeIterator"]
python_lib_Types_PyIterable_Impl_._hx_interfaces = []

# print python.lib.Types.IterHelper
class python_lib_IterHelper:

	pass




def IterHelper_statics_iterableToIterator(it):
	_this_x = it
	return python_HaxeIterator(_this_x.__iter__())
	
python_lib_IterHelper.iterableToIterator = IterHelper_statics_iterableToIterator


python_lib_IterHelper._hx_class = python_lib_IterHelper
python_lib_IterHelper._hx_class_name = "python.lib.IterHelper"
_hx_classes['python.lib.IterHelper'] = python_lib_IterHelper
python_lib_IterHelper._hx_fields = []
python_lib_IterHelper._hx_props = []
python_lib_IterHelper._hx_methods = []
python_lib_IterHelper._hx_statics = ["iterableToIterator"]
python_lib_IterHelper._hx_interfaces = []

# print python.lib.Types.FileDescriptor
# print python.lib.Types.Set
from builtins import set as python_lib_Set
# print python.lib.Types.DictView
# print python.lib.Types.DictImpl
class python_lib_DictImpl:

	pass




def DictImpl_statics_fromObject(x):
	d = python_lib_Dict()
	_g = 0
	_g1 = Reflect.fields(x)
	while _g < len(_g1):
		f = _g1[_g]
		_g = _g + 1
		val = Reflect.field(x, f)
		python_lib_DictImpl.set(d, f, val)
		
	
	
	return d
	
python_lib_DictImpl.fromObject = DictImpl_statics_fromObject
def DictImpl_statics_hasKey(d,key):
	return key in d
python_lib_DictImpl.hasKey = DictImpl_statics_hasKey
def DictImpl_statics_remove(d,key):
	del d[key]
python_lib_DictImpl.remove = DictImpl_statics_remove
def DictImpl_statics_set(d,key,val):
	d[key] = val
python_lib_DictImpl.set = DictImpl_statics_set


python_lib_DictImpl._hx_class = python_lib_DictImpl
python_lib_DictImpl._hx_class_name = "python.lib.DictImpl"
_hx_classes['python.lib.DictImpl'] = python_lib_DictImpl
python_lib_DictImpl._hx_fields = []
python_lib_DictImpl._hx_props = []
python_lib_DictImpl._hx_methods = []
python_lib_DictImpl._hx_statics = ["fromObject","hasKey","remove","set"]
python_lib_DictImpl._hx_interfaces = []

# print python.lib.Types.Tuple
# print python.lib.Types.Tup2
# print python.lib.Types.Tup3
# print python.lib.Types.Tup4
# print python.lib.Types.Tup5
# print python.lib.Types.BufferError
# print python.lib.Types.GeneratorExit
# print python.lib.Types.KeyboardInterrupt
# print python.lib.Types.SyntaxError
# print python.lib.Types.StopIteration
# print python.lib.Types.RuntimeError
# print python.lib.Types.NotImplementedError
# print python.lib.Types.IndentationError
# print python.lib.Types.EnvironmentError
# print python.lib.Types.OSError
# print python.lib.Types.BlockingIOError
# print python.lib.Types.ChildProcessError
# print python.lib.Types.ConnectionError
# print python.lib.Types.BrokenPipeError
# print python.lib.Types.ConnectionAbortedError
# print python.lib.Types.ConnectionRefusedError
# print python.lib.Types.ConnectionResetError
# print python.lib.Types.FileExistsError
# print python.lib.Types.FileNotFoundError
# print python.lib.Types.InterruptedError
# print python.lib.Types.IsADirectoryError
# print python.lib.Types.NotADirectoryError
# print python.lib.Types.PermissionError
# print python.lib.Types.ProcessLookupError
# print python.lib.Types.TimeoutError
# print python.lib.Types.NameError
# print python.lib.Types.UnboundLocalError
# print python.lib.Types.MemoryError
# print python.lib.Types.AssertionError
# print python.lib.Types.AttributeError
# print python.lib.Types.EOFError
# print python.lib.Types.ArithmeticError
# print python.lib.Types.FloatingPointError
# print python.lib.Types.OverflowError
# print python.lib.Types.ZeroDivisionError
# print python.lib.Types.ImportError
# print python.lib.Types.LookupError
# print python.lib.Types.IndexError
# print python.lib.Types.KeyError
# print python.lib.Types.IOError
# print python.lib.Types.VMSError
# print python.lib.Types.WindowsError
# print python.lib.Types.ValueError
# print python.lib.Types.UnicodeError
# print python.lib.Types.UnicodeDecodeError
# print python.lib.Types.UnicodeEncodeError
# print python.lib.Types.UnicodeTranslateError
# print python.lib.Types.Warning
# print python.lib.Types.DeprecationWarning
# print python.lib.Types.PendingDeprecationWarning
# print python.lib.Types.RuntimeWarning
# print python.lib.Types.SyntaxWarning
# print python.lib.Types.UserWarning
# print python.lib.Types.FutureWarning
# print python.lib.Types.ImportWarning
# print python.lib.Types.UnicodeWarning
# print python.lib.Types.BytesWarning
# print python.lib.Types.ResourceWarning
# print python.lib.datetime.DateTime.DateTime
from datetime import datetime as python_lib_datetime_DateTime
# print python.lib.datetime.TimeDelta.TimeDelta
from datetime import timedelta as python_lib_datetime_TimeDelta
# print python.lib.datetime.TzInfo.TzInfo
from datetime import tzinfo as python_lib_datetime_TzInfo
# print python.lib.io.IOBase.IOBase
# print python.lib.io.RawIOBase.RawIOBase
# print python.lib.io.FileIO.FileIO
# print python.lib.io.TextIOBase.TextIOBase
# print python.lib.io.StringIO.StringIO
from io import StringIO as python_lib_io_StringIO
# print python.lib.subprocess.Popen.Popen
from subprocess import Popen as python_lib_subprocess_Popen
# print python.lib.xml.etree.ElementTree.XMLParser
# print python.lib.xml.etree.ElementTree.Element
from xml.etree.ElementTree import Element as python_lib_xml_etree_Element
# print python.lib.xml.etree.ElementTree.ElementTree
import xml.etree.ElementTree as python_lib_xml_etree_ElementTree
# print sublime.Edit.Edit
from sublime import Edit as sublime_Edit
# print sublime.Region.Region
from sublime import Region as sublime_Region
# print sublime.Selection.Selection
from sublime import Selection as sublime_Selection
# print sublime.Settings.Settings
from sublime import Settings as sublime_Settings
# print sublime.Sublime.Sublime
import sublime as sublime_Sublime
# print sublime.View.View
from sublime import View as sublime_View
# print sublime.Window.Window
from sublime import Window as sublime_Window
# print sublime.def.exec.AsyncProcess.AsyncProcess
from Default.exec import AsyncProcess as sublime_def_exec_AsyncProcess
hxsublime_Main.main()
