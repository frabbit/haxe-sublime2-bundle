_hx_classes = dict()
class Int:
    pass
_hx_classes['Int'] = Int
class Bool:
    pass
_hx_classes['Bool'] = Bool
class Float:
    pass
_hx_classes['Float'] = Float
class Dynamic:
    pass
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
		def _hx_local_1():
			def _hx_local_0():
				_hx_r = self.min
				self.min = self.min + 1
				return _hx_r
			
			return _hx_local_0()
		
		return _hx_local_1()
	







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
	_it = HxOverrides_iterator(it)
	while _it.hasNext():
		i = _it.next()
		a.append(i)
		__builtin__.len(a)
		
	
	
	return a
	
Lambda.array = Lambda_statics_array
def Lambda_statics_list(it):
	l = List()
	_it = HxOverrides_iterator(it)
	while _it.hasNext():
		i = _it.next()
		l.add(i)
	
	
	return l
	
Lambda.list = Lambda_statics_list
def Lambda_statics_map(it,f):
	l = List()
	_it = HxOverrides_iterator(it)
	while _it.hasNext():
		x = _it.next()
		l.add(f(x))
	
	
	return l
	
Lambda.map = Lambda_statics_map
def Lambda_statics_mapi(it,f):
	l = List()
	i = 0
	_it = HxOverrides_iterator(it)
	while _it.hasNext():
		x = _it.next()
		def _hx_local_0():
			nonlocal i
			_hx_r = i
			i = i + 1
			return _hx_r
			
		
		l.add(f(_hx_local_0(), x))
	
	
	return l
	
Lambda.mapi = Lambda_statics_mapi
def Lambda_statics_has(it,elt):
	_it = HxOverrides_iterator(it)
	while _it.hasNext():
		x = _it.next()
		if x == elt:
			return True
		
	
	
	return False
	
Lambda.has = Lambda_statics_has
def Lambda_statics_exists(it,f):
	_it = HxOverrides_iterator(it)
	while _it.hasNext():
		x = _it.next()
		if f(x):
			return True
		
	
	
	return False
	
Lambda.exists = Lambda_statics_exists
def Lambda_statics_foreach(it,f):
	_it = HxOverrides_iterator(it)
	while _it.hasNext():
		x = _it.next()
		if not f(x):
			return False
		
	
	
	return True
	
Lambda.foreach = Lambda_statics_foreach
def Lambda_statics_iter(it,f):
	_it = HxOverrides_iterator(it)
	while _it.hasNext():
		x = _it.next()
		f(x)
	
	
Lambda.iter = Lambda_statics_iter
def Lambda_statics_filter(it,f):
	l = List()
	_it = HxOverrides_iterator(it)
	while _it.hasNext():
		x = _it.next()
		if f(x):
			l.add(x)
		
	
	
	return l
	
Lambda.filter = Lambda_statics_filter
def Lambda_statics_fold(it,f,first):
	_it = HxOverrides_iterator(it)
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
		_it = HxOverrides_iterator(it)
		while _it.hasNext():
			_ = _it.next()
			_hx_r = n
			n = n + 1
			_hx_r
			
		
	
	else:
		_it = HxOverrides_iterator(it)
		while _it.hasNext():
			x = _it.next()
			if pred(x):
				_hx_r = n
				n = n + 1
				_hx_r
			
			
		
	
	return n
	
Lambda.count = Lambda_statics_count
def Lambda_statics_empty(it):
	return not HxOverrides_iterator(it).hasNext()
Lambda.empty = Lambda_statics_empty
def Lambda_statics_indexOf(it,v):
	i = 0
	_it = HxOverrides_iterator(it)
	while _it.hasNext():
		v2 = _it.next()
		if v == v2:
			return i
		
		_hx_r = i
		i = i + 1
		_hx_r
		
		
	
	
	return -1
	
Lambda.indexOf = Lambda_statics_indexOf
def Lambda_statics_find(it,f):
	_it = HxOverrides_iterator(it)
	while _it.hasNext():
		v = _it.next()
		if f(v):
			return v
		
	
	
	return None
	
Lambda.find = Lambda_statics_find
def Lambda_statics_concat(a,b):
	l = List()
	_it = HxOverrides_iterator(a)
	while _it.hasNext():
		x = _it.next()
		l.add(x)
	
	
	_it = HxOverrides_iterator(b)
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
		_hx_r = self.length
		self.length = self.length + 1
		_hx_r
		
	

	def push(self,item):
		x = [item, self.h]
		self.h = x
		if self.q is None:
			self.q = x
		
		_hx_r = self.length
		self.length = self.length + 1
		_hx_r
		
	

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
		
		_hx_r = self.length
		self.length = self.length - 1
		_hx_r
		
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
				
				_hx_r = self.length
				self.length = self.length - 1
				_hx_r
				
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
class _Map_Map_Impl_:

	pass




_Map_Map_Impl_._new = None;
def Map_Impl__statics_set(this1,key,value):
	this1.set(key, value)
_Map_Map_Impl_.set = Map_Impl__statics_set
def Map_Impl__statics_get(this1,key):
	return this1.get(key)
_Map_Map_Impl_.get = Map_Impl__statics_get
def Map_Impl__statics_exists(this1,key):
	return this1.exists(key)
_Map_Map_Impl_.exists = Map_Impl__statics_exists
def Map_Impl__statics_remove(this1,key):
	return this1.remove(key)
_Map_Map_Impl_.remove = Map_Impl__statics_remove
def Map_Impl__statics_keys(this1):
	return this1.keys()
_Map_Map_Impl_.keys = Map_Impl__statics_keys
def Map_Impl__statics_iterator(this1):
	return HxOverrides_iterator(this1)
_Map_Map_Impl_.iterator = Map_Impl__statics_iterator
def Map_Impl__statics_toString(this1):
	return this1.toString()
_Map_Map_Impl_.toString = Map_Impl__statics_toString
def Map_Impl__statics_arrayWrite(this1,k,v):
	this1.set(k, v)
	return v
	
_Map_Map_Impl_.arrayWrite = Map_Impl__statics_arrayWrite
def Map_Impl__statics_toStringMap(t):
	return haxe_ds_StringMap()
_Map_Map_Impl_.toStringMap = Map_Impl__statics_toStringMap
def Map_Impl__statics_toIntMap(t):
	return haxe_ds_IntMap()
_Map_Map_Impl_.toIntMap = Map_Impl__statics_toIntMap
def Map_Impl__statics_toEnumValueMapMap(t):
	return haxe_ds_EnumValueMap()
_Map_Map_Impl_.toEnumValueMapMap = Map_Impl__statics_toEnumValueMapMap
def Map_Impl__statics_toObjectMap(t):
	return haxe_ds_ObjectMap()
_Map_Map_Impl_.toObjectMap = Map_Impl__statics_toObjectMap
def Map_Impl__statics_fromStringMap(map):
	return map
_Map_Map_Impl_.fromStringMap = Map_Impl__statics_fromStringMap
def Map_Impl__statics_fromIntMap(map):
	return map
_Map_Map_Impl_.fromIntMap = Map_Impl__statics_fromIntMap
def Map_Impl__statics_fromObjectMap(map):
	return map
_Map_Map_Impl_.fromObjectMap = Map_Impl__statics_fromObjectMap


_Map_Map_Impl_._hx_class = _Map_Map_Impl_
_Map_Map_Impl_._hx_class_name = "_Map._Map.Map_Impl_"
_hx_classes['_Map._Map.Map_Impl_'] = _Map_Map_Impl_
_Map_Map_Impl_._hx_fields = []
_Map_Map_Impl_._hx_props = []
_Map_Map_Impl_._hx_methods = []
_Map_Map_Impl_._hx_statics = ["_new","set","get","exists","remove","keys","iterator","toString","arrayWrite","toStringMap","toIntMap","toEnumValueMapMap","toObjectMap","fromStringMap","fromIntMap","fromObjectMap"]
_Map_Map_Impl_._hx_interfaces = []

# print Map.IMap
class Map_IMap:

	# var get
	# var set
	# var exists
	# var remove
	# var keys
	# var iterator
	# var toString
	pass






Map_IMap._hx_class = Map_IMap
Map_IMap._hx_class_name = "IMap"
_hx_classes['IMap'] = Map_IMap
Map_IMap._hx_fields = []
Map_IMap._hx_props = []
Map_IMap._hx_methods = ["get","set","exists","remove","keys","iterator","toString"]
Map_IMap._hx_statics = []
Map_IMap._hx_interfaces = []

# print Math._hx_math
import math as _hx_math
# print Reflect.Reflect
class Reflect:

	pass




def Reflect_statics_hasField(o,field):
	return __builtin__.hasattr(o, field)
Reflect.hasField = Reflect_statics_hasField
def Reflect_statics_field(o,field):
	v = None
	try:
		v = __builtin__.getattr(o, field)
	except Exception as _hx_e:
		_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
		if True:
			e = _hx_e1
			None
		else:
			raise _hx_e
	return v
	
Reflect.field = Reflect_statics_field
def Reflect_statics_setField(o,field,value):
	return __builtin__.setattr(o, field, value)
Reflect.setField = Reflect_statics_setField
def Reflect_statics_getProperty(o,field):
	tmp = None
	if o is None:
		return None
	else:
		v = None
		try:
			v = __builtin__.getattr(o, "get_" + field)
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			if True:
				e = _hx_e1
				None
			else:
				raise _hx_e
		tmp = v
		
		if tmp is not None and __builtin__.callable(tmp):
			return tmp()
		else:
			v = None
			try:
				v = __builtin__.getattr(o, field)
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				if True:
					e = _hx_e1
					None
				else:
					raise _hx_e
			return v
		
	
	
Reflect.getProperty = Reflect_statics_getProperty
def Reflect_statics_setProperty(o,field,value):
	raise _HxException("not implemented")
Reflect.setProperty = Reflect_statics_setProperty
def Reflect_statics_callMethod(o,func,args):
	raise _HxException("not implemented")
Reflect.callMethod = Reflect_statics_callMethod
def Reflect_statics_fields(o):
	a = []
	if o is not None:
		if __builtin__.hasattr(o, "_hx_fields"):
			fields = o._hx_fields
			return __builtin__.list(fields)
		
		
		if __builtin__.hasattr(o, "__dict__"):
			d = __builtin__.getattr(o, "__dict__")
			keys = d.keys()
			for k in keys:
				a.append(k)
		
		
	
	
	return a
	raise _HxException("not implemented")
	
Reflect.fields = Reflect_statics_fields
def Reflect_statics_isFunction(f):
	return __builtin__.callable(f)
Reflect.isFunction = Reflect_statics_isFunction
def Reflect_statics_compare(a,b):
	raise _HxException("not implemented")
Reflect.compare = Reflect_statics_compare
def Reflect_statics_compareMethods(f1,f2):
	raise _HxException("not implemented")
Reflect.compareMethods = Reflect_statics_compareMethods
def Reflect_statics_isObject(v):
	raise _HxException("not implemented")
Reflect.isObject = Reflect_statics_isObject
def Reflect_statics_isEnumValue(v):
	raise _HxException("not implemented")
Reflect.isEnumValue = Reflect_statics_isEnumValue
def Reflect_statics_deleteField(o,field):
	raise _HxException("not implemented")
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
	elif t == (Int and __builtin__.isinstance(v, int)):
		return True
	elif t == (Float and (__builtin__.isinstance(v, (float,int)) or __builtin__.isinstance(v, int))):
		return True
	elif t == str:
		return __builtin__.isinstance(v, String)
	elif __builtin__.isinstance(v, t):
		return True
	elif python_lib_Inspect.isclass(t):
		loop = None
		loop1 = None
		def _hx_local_0(intf):
			f = None
			v1 = None
			try:
				v1 = __builtin__.getattr(intf, "_hx_interfaces")
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				if True:
					e = _hx_e1
					None
				else:
					raise _hx_e
			f = v1
			
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
		x1 = _hx_random.random() * x
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
	def _hx_local_3():
		def _hx_local_2():
			def _hx_local_1():
				def _hx_local_0():
					len = __builtin__.len(start)
					return python_Tools.substr(s, 0, len)
				
				return _hx_local_0() == start
			
			return __builtin__.len(s) >= __builtin__.len(start) and _hx_local_1()
		
		return _hx_local_2()
	
	return _hx_local_3()
	
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
		_hx_r = r
		r = r + 1
		_hx_r
	
	if r > 0:
		return python_Tools.substr(s, r, l - r)
	else:
		return s
	
StringTools.ltrim = StringTools_statics_ltrim
def StringTools_statics_rtrim(s):
	l = __builtin__.len(s)
	r = 0
	while r < l and StringTools.isSpace(s, l - r - 1):
		_hx_r = r
		r = r + 1
		_hx_r
	
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
	if index < __builtin__.len(s):
		return ord(s[index])
	else:
		return -1
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

class Type_ValueType(_Hx_Enum):
	def __init__(self, t, i, p): 
		super(Type_ValueType,self).__init__(t, i, p)


Type_ValueType.TInt = Type_ValueType("TInt", 1, list())

Type_ValueType.TUnknown = Type_ValueType("TUnknown", 8, list())

Type_ValueType.TFunction = Type_ValueType("TFunction", 5, list())

Type_ValueType.TNull = Type_ValueType("TNull", 0, list())

def _Type_ValueType_statics_TEnum (e): 
	return Type_ValueType("TEnum", 7, [e])
Type_ValueType.TEnum = _Type_ValueType_statics_TEnum

Type_ValueType.TFloat = Type_ValueType("TFloat", 2, list())

def _Type_ValueType_statics_TClass (c): 
	return Type_ValueType("TClass", 6, [c])
Type_ValueType.TClass = _Type_ValueType_statics_TClass

Type_ValueType.TBool = Type_ValueType("TBool", 3, list())

Type_ValueType.TObject = Type_ValueType("TObject", 4, list())
Type_ValueType._hx_constructs = ["TInt","TUnknown","TFunction","TNull","TEnum","TFloat","TClass","TBool","TObject"]
Type_ValueType._hx_class = Type_ValueType
Type_ValueType._hx_class_name = "ValueType"
_hx_classes['ValueType'] = Type_ValueType

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
	
	f = None
	v = None
	try:
		v = __builtin__.getattr(e, constr)
	except Exception as _hx_e:
		_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
		if True:
			e1 = _hx_e1
			None
		else:
			raise _hx_e
	f = v
	
	if f is None:
		raise _HxException("No such constructor " + constr)
	
	if Reflect.isFunction(f):
		if params is None:
			raise _HxException("Constructor " + constr + " need parameters")
		
		raise _HxException("not implemented")
	
	
	if params is not None and __builtin__.len(params) != 0:
		raise _HxException("Constructor " + constr + " does not need parameters")
	
	return f
	
Type.createEnum = Type_statics_createEnum
def Type_statics_createEnumIndex(e,index,params = None):
	if params is None:
		params = None
	
	c = e.__constructs__[index]
	if c is None:
		raise _HxException(index + " is not a valid enum constructor index")
	
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
		x = c._hx_constructs
		return __builtin__.list(x)
	
	else:
		return []
Type.getEnumConstructs = Type_statics_getEnumConstructs
def Type_statics_typeof(v):
	if v is None:
		return Type_ValueType.TNull
	elif __builtin__.isinstance(v, bool):
		return Type_ValueType.TBool
	elif __builtin__.isinstance(v, int):
		return Type_ValueType.TInt
	elif __builtin__.isinstance(v, float):
		return Type_ValueType.TFloat
	elif __builtin__.hasattr(v, "__class__"):
		if __builtin__.isinstance(v, _Hx_AnonObject):
			return Type_ValueType.TObject
		
		if __builtin__.isinstance(v, _Hx_Enum):
			return Type_ValueType.TEnum(v.__class__)
		
		return Type_ValueType.TClass(v.__class__)
	
	elif __builtin__.callable(v):
		return Type_ValueType.TFunction
	else:
		return Type_ValueType.TUnknown
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
		v = None
		v1 = None
		try:
			v1 = __builtin__.getattr(e, ctor)
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			if True:
				e1 = _hx_e1
				None
			else:
				raise _hx_e
		v = v1
		
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
		return python_Lib_HaxeIterator(it)
		
	

	def keys(self):
		ret = []
		self.keysLoop(self.root, ret)
		it = ret.__iter__()
		return python_Lib_HaxeIterator(it)
		
	

	def setLoop(self,k,v,node):
		if node is None:
			return haxe_ds_BalancedTree_TreeNode(None, k, v, None)
		
		c = self.compare(k, node.key)
		if c == 0:
			def _hx_local_1():
				def _hx_local_0():
					return 0 if node is None else node._height
				return haxe_ds_BalancedTree_TreeNode(node.left, k, v, node.right, _hx_local_0())
			
			return _hx_local_1()
		
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
			def _hx_local_6():
				def _hx_local_3():
					_this = l.left
					def _hx_local_5():
						def _hx_local_4():
							return 0 if _this is None else _this._height
						return _hx_local_4()
					
					return _hx_local_5()
				
				def _hx_local_0():
					_this = l.right
					def _hx_local_2():
						def _hx_local_1():
							return 0 if _this is None else _this._height
						return _hx_local_1()
					
					return _hx_local_2()
				
				return _hx_local_3() >= _hx_local_0()
			
			if _hx_local_6():
				return haxe_ds_BalancedTree_TreeNode(l.left, l.key, l.value, haxe_ds_BalancedTree_TreeNode(l.right, k, v, r))
			else:
				return haxe_ds_BalancedTree_TreeNode(haxe_ds_BalancedTree_TreeNode(l.left, l.key, l.value, l.right.left), l.right.key, l.right.value, haxe_ds_BalancedTree_TreeNode(l.right.right, k, v, r))
		
		elif hr > hl + 2:
			def _hx_local_13():
				def _hx_local_10():
					_this = r.right
					def _hx_local_12():
						def _hx_local_11():
							return 0 if _this is None else _this._height
						return _hx_local_11()
					
					return _hx_local_12()
				
				def _hx_local_7():
					_this = r.left
					def _hx_local_9():
						def _hx_local_8():
							return 0 if _this is None else _this._height
						return _hx_local_8()
					
					return _hx_local_9()
				
				return _hx_local_10() > _hx_local_7()
			
			if _hx_local_13():
				return haxe_ds_BalancedTree_TreeNode(haxe_ds_BalancedTree_TreeNode(l, k, v, r.left), r.key, r.value, r.right)
			else:
				return haxe_ds_BalancedTree_TreeNode(haxe_ds_BalancedTree_TreeNode(l, k, v, r.left.left), r.left.key, r.left.value, haxe_ds_BalancedTree_TreeNode(r.left.right, r.key, r.value, r.right))
		
		else:
			def _hx_local_16():
				def _hx_local_15():
					def _hx_local_14():
						return hl if hl > hr else hr
					return (_hx_local_14()) + 1
				
				return haxe_ds_BalancedTree_TreeNode(l, k, v, r, _hx_local_15())
			
			return _hx_local_16()
		
	

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
class haxe_ds_BalancedTree_TreeNode:


	def __init__(self,l,k,v,r,h = -1):
		if h is None:
			h = -1
		
		self.left = l
		self.key = k
		self.value = v
		self.right = r
		if h == -1:
			def _hx_local_14():
				def _hx_local_13():
					def _hx_local_6():
						def _hx_local_3():
							_this = self.left
							def _hx_local_5():
								def _hx_local_4():
									return 0 if _this is None else _this._height
								return _hx_local_4()
							
							return _hx_local_5()
						
						def _hx_local_0():
							_this = self.right
							def _hx_local_2():
								def _hx_local_1():
									return 0 if _this is None else _this._height
								return _hx_local_1()
							
							return _hx_local_2()
						
						return _hx_local_3() > _hx_local_0()
					
					def _hx_local_7():
						_this = self.left
						def _hx_local_9():
							def _hx_local_8():
								return 0 if _this is None else _this._height
							return _hx_local_8()
						
						return _hx_local_9()
					
					def _hx_local_10():
						_this = self.right
						def _hx_local_12():
							def _hx_local_11():
								return 0 if _this is None else _this._height
							return _hx_local_11()
						
						return _hx_local_12()
					
					return _hx_local_7() if _hx_local_6() else _hx_local_10()
				
				return (_hx_local_13()) + 1
			
			self._height = _hx_local_14()
		
		else:
			self._height = h
	
	# var left
	# var right
	# var key
	# var value
	# var _height
	def toString(self):
		def _hx_local_4():
			def _hx_local_3():
				def _hx_local_2():
					def _hx_local_1():
						return "" if self.left is None else self.left.toString() + ", "
					return (_hx_local_1()) + ("" + Std.string(self.key) + "=" + Std.string(self.value))
				
				def _hx_local_0():
					return "" if self.right is None else ", " + self.right.toString()
				return _hx_local_2() + (_hx_local_0())
			
			return _hx_local_3()
		
		return _hx_local_4()
	







haxe_ds_BalancedTree_TreeNode._hx_class = haxe_ds_BalancedTree_TreeNode
haxe_ds_BalancedTree_TreeNode._hx_class_name = "haxe.ds.TreeNode"
_hx_classes['haxe.ds.TreeNode'] = haxe_ds_BalancedTree_TreeNode
haxe_ds_BalancedTree_TreeNode._hx_fields = ["left","right","key","value","_height"]
haxe_ds_BalancedTree_TreeNode._hx_props = []
haxe_ds_BalancedTree_TreeNode._hx_methods = ["toString"]
haxe_ds_BalancedTree_TreeNode._hx_statics = []
haxe_ds_BalancedTree_TreeNode._hx_interfaces = []

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
			def _hx_local_0():
				nonlocal _g1
				_hx_r = _g1
				_g1 = _g1 + 1
				return _hx_r
				
			
			i = _hx_local_0()
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
haxe_ds_EnumValueMap._hx_interfaces = [Map_IMap]
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
	return python_lib_Types_DictImpl.hasKey(this1.values.h, key)
	
haxe_ds_HashMap_HashMap_Impl_.exists = HashMap_Impl__statics_exists
def HashMap_Impl__statics_remove(this1,k):
	this1.values.remove(k.hashCode())
	return this1.keys.remove(k.hashCode())
	
haxe_ds_HashMap_HashMap_Impl_.remove = HashMap_Impl__statics_remove
def HashMap_Impl__statics_keys(this1):
	return HxOverrides_iterator(this1.keys)
haxe_ds_HashMap_HashMap_Impl_.keys = HashMap_Impl__statics_keys
def HashMap_Impl__statics_iterator(this1):
	return HxOverrides_iterator(this1.values)
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
		return python_lib_Types_DictImpl.hasKey(self.h, key)

	def remove(self,key):
		if not python_lib_Types_DictImpl.hasKey(self.h, key):
			return False
		
		del self.h[key]
		return True
	

	def keys(self):
		a = []
		for key in self.h:
			a.append(key)
		it = a.__iter__()
		return python_Lib_HaxeIterator(it)
		
	

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
haxe_ds_IntMap._hx_interfaces = [Map_IMap]

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
haxe_ds_ObjectMap._hx_interfaces = [Map_IMap]

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
		return python_lib_Types_DictImpl.hasKey(self.h, "$" + key)

	def remove(self,key):
		key = "$" + key
		if not python_lib_Types_DictImpl.hasKey(self.h, key):
			return False
		
		del self.h[key]
		return True
	

	def keys(self):
		a = []
		for key in self.h:
			a.append(key[1:])
		it = a.__iter__()
		return python_Lib_HaxeIterator(it)
		
	

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
haxe_ds_StringMap._hx_interfaces = [Map_IMap]

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
haxe_ds_WeakMap._hx_interfaces = [Map_IMap]

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

class haxe_macro_Expr_Constant(_Hx_Enum):
	def __init__(self, t, i, p): 
		super(haxe_macro_Expr_Constant,self).__init__(t, i, p)


def _haxe_macro_Expr_Constant_statics_CFloat (f): 
	return haxe_macro_Expr_Constant("CFloat", 1, [f])
haxe_macro_Expr_Constant.CFloat = _haxe_macro_Expr_Constant_statics_CFloat

def _haxe_macro_Expr_Constant_statics_CIdent (s): 
	return haxe_macro_Expr_Constant("CIdent", 3, [s])
haxe_macro_Expr_Constant.CIdent = _haxe_macro_Expr_Constant_statics_CIdent

def _haxe_macro_Expr_Constant_statics_CInt (v): 
	return haxe_macro_Expr_Constant("CInt", 0, [v])
haxe_macro_Expr_Constant.CInt = _haxe_macro_Expr_Constant_statics_CInt

def _haxe_macro_Expr_Constant_statics_CRegexp (r,opt): 
	return haxe_macro_Expr_Constant("CRegexp", 4, [r,opt])
haxe_macro_Expr_Constant.CRegexp = _haxe_macro_Expr_Constant_statics_CRegexp

def _haxe_macro_Expr_Constant_statics_CString (s): 
	return haxe_macro_Expr_Constant("CString", 2, [s])
haxe_macro_Expr_Constant.CString = _haxe_macro_Expr_Constant_statics_CString
haxe_macro_Expr_Constant._hx_constructs = ["CFloat","CIdent","CInt","CRegexp","CString"]
haxe_macro_Expr_Constant._hx_class = haxe_macro_Expr_Constant
haxe_macro_Expr_Constant._hx_class_name = "haxe.macro.Constant"
_hx_classes['haxe.macro.Constant'] = haxe_macro_Expr_Constant

class haxe_macro_Expr_Binop(_Hx_Enum):
	def __init__(self, t, i, p): 
		super(haxe_macro_Expr_Binop,self).__init__(t, i, p)


haxe_macro_Expr_Binop.OpNotEq = haxe_macro_Expr_Binop("OpNotEq", 6, list())

haxe_macro_Expr_Binop.OpShr = haxe_macro_Expr_Binop("OpShr", 17, list())

haxe_macro_Expr_Binop.OpLt = haxe_macro_Expr_Binop("OpLt", 9, list())

haxe_macro_Expr_Binop.OpInterval = haxe_macro_Expr_Binop("OpInterval", 21, list())

haxe_macro_Expr_Binop.OpAssign = haxe_macro_Expr_Binop("OpAssign", 4, list())

haxe_macro_Expr_Binop.OpBoolOr = haxe_macro_Expr_Binop("OpBoolOr", 15, list())

haxe_macro_Expr_Binop.OpEq = haxe_macro_Expr_Binop("OpEq", 5, list())

haxe_macro_Expr_Binop.OpLte = haxe_macro_Expr_Binop("OpLte", 10, list())

haxe_macro_Expr_Binop.OpAdd = haxe_macro_Expr_Binop("OpAdd", 0, list())

haxe_macro_Expr_Binop.OpMult = haxe_macro_Expr_Binop("OpMult", 1, list())

def _haxe_macro_Expr_Binop_statics_OpAssignOp (op): 
	return haxe_macro_Expr_Binop("OpAssignOp", 20, [op])
haxe_macro_Expr_Binop.OpAssignOp = _haxe_macro_Expr_Binop_statics_OpAssignOp

haxe_macro_Expr_Binop.OpGt = haxe_macro_Expr_Binop("OpGt", 7, list())

haxe_macro_Expr_Binop.OpOr = haxe_macro_Expr_Binop("OpOr", 12, list())

haxe_macro_Expr_Binop.OpShl = haxe_macro_Expr_Binop("OpShl", 16, list())

haxe_macro_Expr_Binop.OpMod = haxe_macro_Expr_Binop("OpMod", 19, list())

haxe_macro_Expr_Binop.OpDiv = haxe_macro_Expr_Binop("OpDiv", 2, list())

haxe_macro_Expr_Binop.OpGte = haxe_macro_Expr_Binop("OpGte", 8, list())

haxe_macro_Expr_Binop.OpBoolAnd = haxe_macro_Expr_Binop("OpBoolAnd", 14, list())

haxe_macro_Expr_Binop.OpAnd = haxe_macro_Expr_Binop("OpAnd", 11, list())

haxe_macro_Expr_Binop.OpUShr = haxe_macro_Expr_Binop("OpUShr", 18, list())

haxe_macro_Expr_Binop.OpArrow = haxe_macro_Expr_Binop("OpArrow", 22, list())

haxe_macro_Expr_Binop.OpSub = haxe_macro_Expr_Binop("OpSub", 3, list())

haxe_macro_Expr_Binop.OpXor = haxe_macro_Expr_Binop("OpXor", 13, list())
haxe_macro_Expr_Binop._hx_constructs = ["OpNotEq","OpShr","OpLt","OpInterval","OpAssign","OpBoolOr","OpEq","OpLte","OpAdd","OpMult","OpAssignOp","OpGt","OpOr","OpShl","OpMod","OpDiv","OpGte","OpBoolAnd","OpAnd","OpUShr","OpArrow","OpSub","OpXor"]
haxe_macro_Expr_Binop._hx_class = haxe_macro_Expr_Binop
haxe_macro_Expr_Binop._hx_class_name = "haxe.macro.Binop"
_hx_classes['haxe.macro.Binop'] = haxe_macro_Expr_Binop

class haxe_macro_Expr_Unop(_Hx_Enum):
	def __init__(self, t, i, p): 
		super(haxe_macro_Expr_Unop,self).__init__(t, i, p)


haxe_macro_Expr_Unop.OpNeg = haxe_macro_Expr_Unop("OpNeg", 3, list())

haxe_macro_Expr_Unop.OpNegBits = haxe_macro_Expr_Unop("OpNegBits", 4, list())

haxe_macro_Expr_Unop.OpNot = haxe_macro_Expr_Unop("OpNot", 2, list())

haxe_macro_Expr_Unop.OpDecrement = haxe_macro_Expr_Unop("OpDecrement", 1, list())

haxe_macro_Expr_Unop.OpIncrement = haxe_macro_Expr_Unop("OpIncrement", 0, list())
haxe_macro_Expr_Unop._hx_constructs = ["OpNeg","OpNegBits","OpNot","OpDecrement","OpIncrement"]
haxe_macro_Expr_Unop._hx_class = haxe_macro_Expr_Unop
haxe_macro_Expr_Unop._hx_class_name = "haxe.macro.Unop"
_hx_classes['haxe.macro.Unop'] = haxe_macro_Expr_Unop

class haxe_macro_Expr_ExprDef(_Hx_Enum):
	def __init__(self, t, i, p): 
		super(haxe_macro_Expr_ExprDef,self).__init__(t, i, p)


def _haxe_macro_Expr_ExprDef_statics_EArrayDecl (values): 
	return haxe_macro_Expr_ExprDef("EArrayDecl", 6, [values])
haxe_macro_Expr_ExprDef.EArrayDecl = _haxe_macro_Expr_ExprDef_statics_EArrayDecl

def _haxe_macro_Expr_ExprDef_statics_EArray (e1,e2): 
	return haxe_macro_Expr_ExprDef("EArray", 1, [e1,e2])
haxe_macro_Expr_ExprDef.EArray = _haxe_macro_Expr_ExprDef_statics_EArray

def _haxe_macro_Expr_ExprDef_statics_EUntyped (e): 
	return haxe_macro_Expr_ExprDef("EUntyped", 22, [e])
haxe_macro_Expr_ExprDef.EUntyped = _haxe_macro_Expr_ExprDef_statics_EUntyped

def _haxe_macro_Expr_ExprDef_statics_EVars (vars): 
	return haxe_macro_Expr_ExprDef("EVars", 10, [vars])
haxe_macro_Expr_ExprDef.EVars = _haxe_macro_Expr_ExprDef_statics_EVars

def _haxe_macro_Expr_ExprDef_statics_ECall (e,params): 
	return haxe_macro_Expr_ExprDef("ECall", 7, [e,params])
haxe_macro_Expr_ExprDef.ECall = _haxe_macro_Expr_ExprDef_statics_ECall

def _haxe_macro_Expr_ExprDef_statics_EBlock (exprs): 
	return haxe_macro_Expr_ExprDef("EBlock", 12, [exprs])
haxe_macro_Expr_ExprDef.EBlock = _haxe_macro_Expr_ExprDef_statics_EBlock

def _haxe_macro_Expr_ExprDef_statics_EIf (econd,eif,eelse): 
	return haxe_macro_Expr_ExprDef("EIf", 15, [econd,eif,eelse])
haxe_macro_Expr_ExprDef.EIf = _haxe_macro_Expr_ExprDef_statics_EIf

def _haxe_macro_Expr_ExprDef_statics_ENew (t,params): 
	return haxe_macro_Expr_ExprDef("ENew", 8, [t,params])
haxe_macro_Expr_ExprDef.ENew = _haxe_macro_Expr_ExprDef_statics_ENew

def _haxe_macro_Expr_ExprDef_statics_ETry (e,catches): 
	return haxe_macro_Expr_ExprDef("ETry", 18, [e,catches])
haxe_macro_Expr_ExprDef.ETry = _haxe_macro_Expr_ExprDef_statics_ETry

def _haxe_macro_Expr_ExprDef_statics_EWhile (econd,e,normalWhile): 
	return haxe_macro_Expr_ExprDef("EWhile", 16, [econd,e,normalWhile])
haxe_macro_Expr_ExprDef.EWhile = _haxe_macro_Expr_ExprDef_statics_EWhile

def _haxe_macro_Expr_ExprDef_statics_ECheckType (e,t): 
	return haxe_macro_Expr_ExprDef("ECheckType", 28, [e,t])
haxe_macro_Expr_ExprDef.ECheckType = _haxe_macro_Expr_ExprDef_statics_ECheckType

haxe_macro_Expr_ExprDef.EContinue = haxe_macro_Expr_ExprDef("EContinue", 21, list())

def _haxe_macro_Expr_ExprDef_statics_EObjectDecl (fields): 
	return haxe_macro_Expr_ExprDef("EObjectDecl", 5, [fields])
haxe_macro_Expr_ExprDef.EObjectDecl = _haxe_macro_Expr_ExprDef_statics_EObjectDecl

def _haxe_macro_Expr_ExprDef_statics_EField (e,field): 
	return haxe_macro_Expr_ExprDef("EField", 3, [e,field])
haxe_macro_Expr_ExprDef.EField = _haxe_macro_Expr_ExprDef_statics_EField

def _haxe_macro_Expr_ExprDef_statics_EFor (it,expr): 
	return haxe_macro_Expr_ExprDef("EFor", 13, [it,expr])
haxe_macro_Expr_ExprDef.EFor = _haxe_macro_Expr_ExprDef_statics_EFor

def _haxe_macro_Expr_ExprDef_statics_EUnop (op,postFix,e): 
	return haxe_macro_Expr_ExprDef("EUnop", 9, [op,postFix,e])
haxe_macro_Expr_ExprDef.EUnop = _haxe_macro_Expr_ExprDef_statics_EUnop

def _haxe_macro_Expr_ExprDef_statics_EBinop (op,e1,e2): 
	return haxe_macro_Expr_ExprDef("EBinop", 2, [op,e1,e2])
haxe_macro_Expr_ExprDef.EBinop = _haxe_macro_Expr_ExprDef_statics_EBinop

def _haxe_macro_Expr_ExprDef_statics_EConst (c): 
	return haxe_macro_Expr_ExprDef("EConst", 0, [c])
haxe_macro_Expr_ExprDef.EConst = _haxe_macro_Expr_ExprDef_statics_EConst

def _haxe_macro_Expr_ExprDef_statics_EFunction (name,f): 
	return haxe_macro_Expr_ExprDef("EFunction", 11, [name,f])
haxe_macro_Expr_ExprDef.EFunction = _haxe_macro_Expr_ExprDef_statics_EFunction

def _haxe_macro_Expr_ExprDef_statics_EIn (e1,e2): 
	return haxe_macro_Expr_ExprDef("EIn", 14, [e1,e2])
haxe_macro_Expr_ExprDef.EIn = _haxe_macro_Expr_ExprDef_statics_EIn

def _haxe_macro_Expr_ExprDef_statics_ESwitch (e,cases,edef): 
	return haxe_macro_Expr_ExprDef("ESwitch", 17, [e,cases,edef])
haxe_macro_Expr_ExprDef.ESwitch = _haxe_macro_Expr_ExprDef_statics_ESwitch

def _haxe_macro_Expr_ExprDef_statics_ETernary (econd,eif,eelse): 
	return haxe_macro_Expr_ExprDef("ETernary", 27, [econd,eif,eelse])
haxe_macro_Expr_ExprDef.ETernary = _haxe_macro_Expr_ExprDef_statics_ETernary

def _haxe_macro_Expr_ExprDef_statics_ECast (e,t): 
	return haxe_macro_Expr_ExprDef("ECast", 24, [e,t])
haxe_macro_Expr_ExprDef.ECast = _haxe_macro_Expr_ExprDef_statics_ECast

haxe_macro_Expr_ExprDef.EBreak = haxe_macro_Expr_ExprDef("EBreak", 20, list())

def _haxe_macro_Expr_ExprDef_statics_EReturn (e): 
	return haxe_macro_Expr_ExprDef("EReturn", 19, [e])
haxe_macro_Expr_ExprDef.EReturn = _haxe_macro_Expr_ExprDef_statics_EReturn

def _haxe_macro_Expr_ExprDef_statics_EDisplayNew (t): 
	return haxe_macro_Expr_ExprDef("EDisplayNew", 26, [t])
haxe_macro_Expr_ExprDef.EDisplayNew = _haxe_macro_Expr_ExprDef_statics_EDisplayNew

def _haxe_macro_Expr_ExprDef_statics_EMeta (s,e): 
	return haxe_macro_Expr_ExprDef("EMeta", 29, [s,e])
haxe_macro_Expr_ExprDef.EMeta = _haxe_macro_Expr_ExprDef_statics_EMeta

def _haxe_macro_Expr_ExprDef_statics_EParenthesis (e): 
	return haxe_macro_Expr_ExprDef("EParenthesis", 4, [e])
haxe_macro_Expr_ExprDef.EParenthesis = _haxe_macro_Expr_ExprDef_statics_EParenthesis

def _haxe_macro_Expr_ExprDef_statics_EThrow (e): 
	return haxe_macro_Expr_ExprDef("EThrow", 23, [e])
haxe_macro_Expr_ExprDef.EThrow = _haxe_macro_Expr_ExprDef_statics_EThrow

def _haxe_macro_Expr_ExprDef_statics_EDisplay (e,isCall): 
	return haxe_macro_Expr_ExprDef("EDisplay", 25, [e,isCall])
haxe_macro_Expr_ExprDef.EDisplay = _haxe_macro_Expr_ExprDef_statics_EDisplay
haxe_macro_Expr_ExprDef._hx_constructs = ["EArrayDecl","EArray","EUntyped","EVars","ECall","EBlock","EIf","ENew","ETry","EWhile","ECheckType","EContinue","EObjectDecl","EField","EFor","EUnop","EBinop","EConst","EFunction","EIn","ESwitch","ETernary","ECast","EBreak","EReturn","EDisplayNew","EMeta","EParenthesis","EThrow","EDisplay"]
haxe_macro_Expr_ExprDef._hx_class = haxe_macro_Expr_ExprDef
haxe_macro_Expr_ExprDef._hx_class_name = "haxe.macro.ExprDef"
_hx_classes['haxe.macro.ExprDef'] = haxe_macro_Expr_ExprDef

class haxe_macro_Expr_ComplexType(_Hx_Enum):
	def __init__(self, t, i, p): 
		super(haxe_macro_Expr_ComplexType,self).__init__(t, i, p)


def _haxe_macro_Expr_ComplexType_statics_TAnonymous (fields): 
	return haxe_macro_Expr_ComplexType("TAnonymous", 2, [fields])
haxe_macro_Expr_ComplexType.TAnonymous = _haxe_macro_Expr_ComplexType_statics_TAnonymous

def _haxe_macro_Expr_ComplexType_statics_TExtend (p,fields): 
	return haxe_macro_Expr_ComplexType("TExtend", 4, [p,fields])
haxe_macro_Expr_ComplexType.TExtend = _haxe_macro_Expr_ComplexType_statics_TExtend

def _haxe_macro_Expr_ComplexType_statics_TOptional (t): 
	return haxe_macro_Expr_ComplexType("TOptional", 5, [t])
haxe_macro_Expr_ComplexType.TOptional = _haxe_macro_Expr_ComplexType_statics_TOptional

def _haxe_macro_Expr_ComplexType_statics_TPath (p): 
	return haxe_macro_Expr_ComplexType("TPath", 0, [p])
haxe_macro_Expr_ComplexType.TPath = _haxe_macro_Expr_ComplexType_statics_TPath

def _haxe_macro_Expr_ComplexType_statics_TFunction (args,ret): 
	return haxe_macro_Expr_ComplexType("TFunction", 1, [args,ret])
haxe_macro_Expr_ComplexType.TFunction = _haxe_macro_Expr_ComplexType_statics_TFunction

def _haxe_macro_Expr_ComplexType_statics_TParent (t): 
	return haxe_macro_Expr_ComplexType("TParent", 3, [t])
haxe_macro_Expr_ComplexType.TParent = _haxe_macro_Expr_ComplexType_statics_TParent
haxe_macro_Expr_ComplexType._hx_constructs = ["TAnonymous","TExtend","TOptional","TPath","TFunction","TParent"]
haxe_macro_Expr_ComplexType._hx_class = haxe_macro_Expr_ComplexType
haxe_macro_Expr_ComplexType._hx_class_name = "haxe.macro.ComplexType"
_hx_classes['haxe.macro.ComplexType'] = haxe_macro_Expr_ComplexType

class haxe_macro_Expr_TypeParam(_Hx_Enum):
	def __init__(self, t, i, p): 
		super(haxe_macro_Expr_TypeParam,self).__init__(t, i, p)


def _haxe_macro_Expr_TypeParam_statics_TPExpr (e): 
	return haxe_macro_Expr_TypeParam("TPExpr", 1, [e])
haxe_macro_Expr_TypeParam.TPExpr = _haxe_macro_Expr_TypeParam_statics_TPExpr

def _haxe_macro_Expr_TypeParam_statics_TPType (t): 
	return haxe_macro_Expr_TypeParam("TPType", 0, [t])
haxe_macro_Expr_TypeParam.TPType = _haxe_macro_Expr_TypeParam_statics_TPType
haxe_macro_Expr_TypeParam._hx_constructs = ["TPExpr","TPType"]
haxe_macro_Expr_TypeParam._hx_class = haxe_macro_Expr_TypeParam
haxe_macro_Expr_TypeParam._hx_class_name = "haxe.macro.TypeParam"
_hx_classes['haxe.macro.TypeParam'] = haxe_macro_Expr_TypeParam

class haxe_macro_Expr_Access(_Hx_Enum):
	def __init__(self, t, i, p): 
		super(haxe_macro_Expr_Access,self).__init__(t, i, p)


haxe_macro_Expr_Access.ADynamic = haxe_macro_Expr_Access("ADynamic", 4, list())

haxe_macro_Expr_Access.AOverride = haxe_macro_Expr_Access("AOverride", 3, list())

haxe_macro_Expr_Access.APrivate = haxe_macro_Expr_Access("APrivate", 1, list())

haxe_macro_Expr_Access.APublic = haxe_macro_Expr_Access("APublic", 0, list())

haxe_macro_Expr_Access.AMacro = haxe_macro_Expr_Access("AMacro", 6, list())

haxe_macro_Expr_Access.AInline = haxe_macro_Expr_Access("AInline", 5, list())

haxe_macro_Expr_Access.AStatic = haxe_macro_Expr_Access("AStatic", 2, list())
haxe_macro_Expr_Access._hx_constructs = ["ADynamic","AOverride","APrivate","APublic","AMacro","AInline","AStatic"]
haxe_macro_Expr_Access._hx_class = haxe_macro_Expr_Access
haxe_macro_Expr_Access._hx_class_name = "haxe.macro.Access"
_hx_classes['haxe.macro.Access'] = haxe_macro_Expr_Access

class haxe_macro_Expr_FieldType(_Hx_Enum):
	def __init__(self, t, i, p): 
		super(haxe_macro_Expr_FieldType,self).__init__(t, i, p)


def _haxe_macro_Expr_FieldType_statics_FFun (f): 
	return haxe_macro_Expr_FieldType("FFun", 1, [f])
haxe_macro_Expr_FieldType.FFun = _haxe_macro_Expr_FieldType_statics_FFun

def _haxe_macro_Expr_FieldType_statics_FProp (get,set,t,e): 
	return haxe_macro_Expr_FieldType("FProp", 2, [get,set,t,e])
haxe_macro_Expr_FieldType.FProp = _haxe_macro_Expr_FieldType_statics_FProp

def _haxe_macro_Expr_FieldType_statics_FVar (t,e): 
	return haxe_macro_Expr_FieldType("FVar", 0, [t,e])
haxe_macro_Expr_FieldType.FVar = _haxe_macro_Expr_FieldType_statics_FVar
haxe_macro_Expr_FieldType._hx_constructs = ["FFun","FProp","FVar"]
haxe_macro_Expr_FieldType._hx_class = haxe_macro_Expr_FieldType
haxe_macro_Expr_FieldType._hx_class_name = "haxe.macro.FieldType"
_hx_classes['haxe.macro.FieldType'] = haxe_macro_Expr_FieldType

class haxe_macro_Expr_TypeDefKind(_Hx_Enum):
	def __init__(self, t, i, p): 
		super(haxe_macro_Expr_TypeDefKind,self).__init__(t, i, p)


haxe_macro_Expr_TypeDefKind.TDEnum = haxe_macro_Expr_TypeDefKind("TDEnum", 0, list())

def _haxe_macro_Expr_TypeDefKind_statics_TDAbstract (tthis,_hx_from,to): 
	return haxe_macro_Expr_TypeDefKind("TDAbstract", 4, [tthis,_hx_from,to])
haxe_macro_Expr_TypeDefKind.TDAbstract = _haxe_macro_Expr_TypeDefKind_statics_TDAbstract

def _haxe_macro_Expr_TypeDefKind_statics_TDAlias (t): 
	return haxe_macro_Expr_TypeDefKind("TDAlias", 3, [t])
haxe_macro_Expr_TypeDefKind.TDAlias = _haxe_macro_Expr_TypeDefKind_statics_TDAlias

def _haxe_macro_Expr_TypeDefKind_statics_TDClass (superClass,interfaces,isInterface): 
	return haxe_macro_Expr_TypeDefKind("TDClass", 2, [superClass,interfaces,isInterface])
haxe_macro_Expr_TypeDefKind.TDClass = _haxe_macro_Expr_TypeDefKind_statics_TDClass

haxe_macro_Expr_TypeDefKind.TDStructure = haxe_macro_Expr_TypeDefKind("TDStructure", 1, list())
haxe_macro_Expr_TypeDefKind._hx_constructs = ["TDEnum","TDAbstract","TDAlias","TDClass","TDStructure"]
haxe_macro_Expr_TypeDefKind._hx_class = haxe_macro_Expr_TypeDefKind
haxe_macro_Expr_TypeDefKind._hx_class_name = "haxe.macro.TypeDefKind"
_hx_classes['haxe.macro.TypeDefKind'] = haxe_macro_Expr_TypeDefKind

# print haxe.macro.Expr.Error
class haxe_macro_Expr_Error:


	def __init__(self,m,p):
		self.message = m
		self.pos = p
	
	# var message
	# var pos
	def toString(self):
		return self.message







haxe_macro_Expr_Error._hx_class = haxe_macro_Expr_Error
haxe_macro_Expr_Error._hx_class_name = "haxe.macro.Error"
_hx_classes['haxe.macro.Error'] = haxe_macro_Expr_Error
haxe_macro_Expr_Error._hx_fields = ["message","pos"]
haxe_macro_Expr_Error._hx_props = []
haxe_macro_Expr_Error._hx_methods = ["toString"]
haxe_macro_Expr_Error._hx_statics = []
haxe_macro_Expr_Error._hx_interfaces = []

# print hxsublime.Codegen.HaxeImportGenerator
class hxsublime_Codegen_HaxeImportGenerator:


	def __init__(self,panel,view):
		haxe_Log.trace("construct", _Hx_AnonObject(fileName = "Codegen.hx" ,lineNumber = 36 ,className = "hxsublime.HaxeImportGenerator" ,methodName = "new" ))
		self.view = view
		haxe_Log.trace(Std.string(self.view), _Hx_AnonObject(fileName = "Codegen.hx" ,lineNumber = 38 ,className = "hxsublime.HaxeImportGenerator" ,methodName = "new" ))
		self.panel = panel
		self.start = None
		self.size = None
		self.cname = None
	
	# var panel
	# var start
	# var size
	# var cname
	# var view
	def _get_end(self,src,offset):
		end = __builtin__.len(src)
		while offset < end:
			c = src[offset]
			offset = offset + 1
			if hxsublime_tools_HxSrcTools_Regex.word_chars.match(c) is None:
				break
			
		
		return offset - 1
	

	def _get_start(self,src,offset):
		found_word = 0
		offset = offset - 1
		while offset > 0:
			c = src[offset]
			offset = offset - 1
			if found_word == 0:
				if hxsublime_tools_HxSrcTools_Regex.space_chars.match(c) is not None:
					continue
				
				found_word = 1
			
			
			if hxsublime_tools_HxSrcTools_Regex.word_chars.match(c) is None:
				break
			
		
		return offset + 2
	

	def _is_membername(self,token):
		return token[0] >= "Z" or token == token.upper()

	def _get_classname(self,view,src):
		loc = view.sel()[0]
		end = __builtin__.max(loc.a, loc.b)
		self.size = loc.size()
		if self.size == 0:
			end = self._get_end(src, end)
			self.start = self._get_start(src, end)
			self.size = end - self.start
		
		else:
			self.start = end - self.size
		s = view.substr(sublime_Region(self.start, end))
		self.cname = s.rpartition(".")
		
		while not (self.cname[0] == "") and self._is_membername(self.cname[2]):
			def _hx_local_2():
				def _hx_local_1():
					def _hx_local_0():
						_this = self.cname[2]
						return __builtin__.len(_this)
					
					return 1 + _hx_local_0()
				
				return self.size - _hx_local_1()
			
			self.size = _hx_local_2()
			s = self.cname[0]
			self.cname = s.rpartition(".")
			
		
		return self.cname
	

	def _compact_classname(self,edit,view):
		view.replace(edit, sublime_Region(self.start, self.start + self.size), self.cname[2])
		view.sel().clear()
		loc = None
		def _hx_local_1():
			def _hx_local_0():
				_this = self.cname[2]
				return __builtin__.len(_this)
			
			return self.start + _hx_local_0()
		
		loc = _hx_local_1()
		view.sel().add(sublime_Region(loc, loc))
	

	def _get_indent(self,src,index):
		if src[index] == "\n":
			return index + 1
		
		return index
	

	def _insert_statement(self,edit,view,src,statement,regex):
		cname = self.cname[0] + self.cname[1] + self.cname[2]
		clow = cname.lower()
		last = None
		def _hx_local_0():
			p = regex.finditer(src)
			return python_Lib_HaxeIterator(p)
		
		_it = _hx_local_0()
		while _it.hasNext():
			imp = _it.next()
			def _hx_local_2():
				def _hx_local_1():
					_this = imp.group(2)
					return _this.lower()
				
				return clow < _hx_local_1()
			
			if _hx_local_2():
				ins = python_lib_StringTools.format("{0}{1} {2};\n", [imp.group(1), statement, cname])
				view.insert(edit, self._get_indent(src, imp.start(0)), ins)
				return
			
			
			last = imp
			
		
		
		if last is not None:
			ins = python_lib_StringTools.format(";\n{0}{1} {2}", [last.group(1), statement, cname])
			view.insert(edit, last.end(2), ins)
		
		else:
			pkg = hxsublime_tools_HxSrcTools_Regex.package_line.search(src)
			if pkg is not None:
				ins = python_lib_StringTools.format("\n\n{0} {1};", [statement, cname])
				view.insert(edit, pkg.end(0), ins)
			
			else:
				ins = python_lib_StringTools.format("{0} {1};\n\n", [statement, cname])
				view.insert(edit, 0, ins)
			
		
	

	def generate_statement(self,edit,statement,regex):
		view = self.view
		src = view.substr(sublime_Region(0, view.size()))
		cname = self._get_classname(view, src)
		if cname[1] == "" and statement == "import":
			sublime_Sublime.status_message("Nothing to " + statement)
			self.panel.writeln("Nothing to " + statement)
			return
		
		
		self._compact_classname(edit, view)
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
		
		
		self._insert_statement(edit, view, src, statement, regex)
	





def HaxeImportGenerator_statics_generate_using(view,edit):
	p = hxsublime_Codegen_HaxeImportGenerator(hxsublime_panel_Base_Panels.default_panel(), view)
	return p.generate_statement(edit, "using", hxsublime_tools_HxSrcTools_Regex.using_line)
	
hxsublime_Codegen_HaxeImportGenerator.generate_using = HaxeImportGenerator_statics_generate_using
def HaxeImportGenerator_statics_generate_import(view,edit):
	p = hxsublime_Codegen_HaxeImportGenerator(hxsublime_panel_Base_Panels.default_panel(), view)
	return p.generate_statement(edit, "import", hxsublime_tools_HxSrcTools_Regex.import_line)
	
hxsublime_Codegen_HaxeImportGenerator.generate_import = HaxeImportGenerator_statics_generate_import


hxsublime_Codegen_HaxeImportGenerator._hx_class = hxsublime_Codegen_HaxeImportGenerator
hxsublime_Codegen_HaxeImportGenerator._hx_class_name = "hxsublime.HaxeImportGenerator"
_hx_classes['hxsublime.HaxeImportGenerator'] = hxsublime_Codegen_HaxeImportGenerator
hxsublime_Codegen_HaxeImportGenerator._hx_fields = ["panel","start","size","cname","view"]
hxsublime_Codegen_HaxeImportGenerator._hx_props = []
hxsublime_Codegen_HaxeImportGenerator._hx_methods = ["_get_end","_get_start","_is_membername","_get_classname","_compact_classname","_get_indent","_insert_statement","generate_statement"]
hxsublime_Codegen_HaxeImportGenerator._hx_statics = ["generate_using","generate_import"]
hxsublime_Codegen_HaxeImportGenerator._hx_interfaces = []

# print hxsublime.Config.NmeTarget
class hxsublime_Config_NmeTarget:


	def __init__(self,name,plattform,args):
		self.name = name
		self.plattform = plattform
		self.args = args
	
	# var name
	# var plattform
	# var args






hxsublime_Config_NmeTarget._hx_class = hxsublime_Config_NmeTarget
hxsublime_Config_NmeTarget._hx_class_name = "hxsublime.NmeTarget"
_hx_classes['hxsublime.NmeTarget'] = hxsublime_Config_NmeTarget
hxsublime_Config_NmeTarget._hx_fields = ["name","plattform","args"]
hxsublime_Config_NmeTarget._hx_props = []
hxsublime_Config_NmeTarget._hx_methods = []
hxsublime_Config_NmeTarget._hx_statics = []
hxsublime_Config_NmeTarget._hx_interfaces = []

# print hxsublime.Config.OpenFlTarget
class hxsublime_Config_OpenFlTarget:


	def __init__(self,name,plattform,args):
		self.name = name
		self.plattform = plattform
		self.args = args
	
	# var name
	# var plattform
	# var args






hxsublime_Config_OpenFlTarget._hx_class = hxsublime_Config_OpenFlTarget
hxsublime_Config_OpenFlTarget._hx_class_name = "hxsublime.OpenFlTarget"
_hx_classes['hxsublime.OpenFlTarget'] = hxsublime_Config_OpenFlTarget
hxsublime_Config_OpenFlTarget._hx_fields = ["name","plattform","args"]
hxsublime_Config_OpenFlTarget._hx_props = []
hxsublime_Config_OpenFlTarget._hx_methods = []
hxsublime_Config_OpenFlTarget._hx_statics = []
hxsublime_Config_OpenFlTarget._hx_interfaces = []

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
hxsublime_Config.nme_targets = [hxsublime_Config_NmeTarget("Flash", "flash", ["-debug"]), hxsublime_Config_NmeTarget("HTML5", "html5", ["-debug"]), hxsublime_Config_NmeTarget("C++", "cpp", ["-debug"]), hxsublime_Config_NmeTarget("Windows", "windows", ["-debug"]), hxsublime_Config_NmeTarget("Mac", "mac", ["-debug"]), hxsublime_Config_NmeTarget("Linux", "linux", ["-debug"]), hxsublime_Config_NmeTarget("Linux 64", "linux", ["-64 -debug"]), hxsublime_Config_NmeTarget("iOs - iPhone simulator", "ios", ["-simulator -debug"]), hxsublime_Config_NmeTarget("iOs - iPad simulator", "ios", ["-simulator -ipad -debug"]), hxsublime_Config_NmeTarget("iOs - update XCode project", "ios", ["-ipad -debug"]), hxsublime_Config_NmeTarget("Neko", "neko", ["-debug"]), hxsublime_Config_NmeTarget("Neko 64", "neko", ["-64 -debug"]), hxsublime_Config_NmeTarget("WebOs", "webos", ["-debug"]), hxsublime_Config_NmeTarget("BlackBerry", "blackberry", ["-debug"]), hxsublime_Config_NmeTarget("Android", "android", ["-debug"])]
hxsublime_Config.openfl_targets = [hxsublime_Config_OpenFlTarget("Flash", "flash", ["-debug"]), hxsublime_Config_OpenFlTarget("HTML5", "html5", ["-debug"]), hxsublime_Config_OpenFlTarget("C++", "cpp", ["-debug"]), hxsublime_Config_OpenFlTarget("Windows", "windows", ["-debug"]), hxsublime_Config_OpenFlTarget("Mac", "mac", ["-debug"]), hxsublime_Config_OpenFlTarget("Linux", "linux", ["-debug"]), hxsublime_Config_OpenFlTarget("Linux 64", "linux", ["-64 -debug"]), hxsublime_Config_OpenFlTarget("iOs - iPhone simulator", "ios", ["-simulator -debug"]), hxsublime_Config_OpenFlTarget("iOs - iPad simulator", "ios", ["-simulator -ipad -debug"]), hxsublime_Config_OpenFlTarget("iOs - update XCode project", "ios", ["-ipad -debug"]), hxsublime_Config_OpenFlTarget("Neko", "neko", ["-debug"]), hxsublime_Config_OpenFlTarget("Neko 64", "neko", ["-64 -debug"]), hxsublime_Config_OpenFlTarget("Emscripten", "emscripten", ["-debug"]), hxsublime_Config_OpenFlTarget("WebOs", "webos", ["-debug"]), hxsublime_Config_OpenFlTarget("BlackBerry", "blackberry", ["-debug"]), hxsublime_Config_OpenFlTarget("Android", "android", ["-debug"])]
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
class hxsublime_Exceptions_ExtractBuildPathException(Exception):


	def __init__(self,build):
		super().__init__("Cannot ExtractBuildPath from build " + Std.string(build))






hxsublime_Exceptions_ExtractBuildPathException._hx_class = hxsublime_Exceptions_ExtractBuildPathException
hxsublime_Exceptions_ExtractBuildPathException._hx_class_name = "hxsublime.ExtractBuildPathException"
_hx_classes['hxsublime.ExtractBuildPathException'] = hxsublime_Exceptions_ExtractBuildPathException
hxsublime_Exceptions_ExtractBuildPathException._hx_fields = []
hxsublime_Exceptions_ExtractBuildPathException._hx_props = []
hxsublime_Exceptions_ExtractBuildPathException._hx_methods = []
hxsublime_Exceptions_ExtractBuildPathException._hx_statics = []
hxsublime_Exceptions_ExtractBuildPathException._hx_interfaces = []
hxsublime_Exceptions_ExtractBuildPathException._hx_super = Exception

# print hxsublime.Exceptions.GetRelativePathException
class hxsublime_Exceptions_GetRelativePathException(Exception):


	def __init__(self,build,file):
		super().__init__("Cannot get the relative path of " + Std.string(file) + " for build " + Std.string(build))






hxsublime_Exceptions_GetRelativePathException._hx_class = hxsublime_Exceptions_GetRelativePathException
hxsublime_Exceptions_GetRelativePathException._hx_class_name = "hxsublime.GetRelativePathException"
_hx_classes['hxsublime.GetRelativePathException'] = hxsublime_Exceptions_GetRelativePathException
hxsublime_Exceptions_GetRelativePathException._hx_fields = []
hxsublime_Exceptions_GetRelativePathException._hx_props = []
hxsublime_Exceptions_GetRelativePathException._hx_methods = []
hxsublime_Exceptions_GetRelativePathException._hx_statics = []
hxsublime_Exceptions_GetRelativePathException._hx_interfaces = []
hxsublime_Exceptions_GetRelativePathException._hx_super = Exception

# print hxsublime.Exceptions.CreateTempFileOrFolderException
class hxsublime_Exceptions_CreateTempFileOrFolderException(Exception):


	def __init__(self,build,file_or_folder):
		super().__init__("Cannot create temp file or folder (" + Std.string(file_or_folder) + ") from build (" + Std.string(build) + ")")






hxsublime_Exceptions_CreateTempFileOrFolderException._hx_class = hxsublime_Exceptions_CreateTempFileOrFolderException
hxsublime_Exceptions_CreateTempFileOrFolderException._hx_class_name = "hxsublime.CreateTempFileOrFolderException"
_hx_classes['hxsublime.CreateTempFileOrFolderException'] = hxsublime_Exceptions_CreateTempFileOrFolderException
hxsublime_Exceptions_CreateTempFileOrFolderException._hx_fields = []
hxsublime_Exceptions_CreateTempFileOrFolderException._hx_props = []
hxsublime_Exceptions_CreateTempFileOrFolderException._hx_methods = []
hxsublime_Exceptions_CreateTempFileOrFolderException._hx_statics = []
hxsublime_Exceptions_CreateTempFileOrFolderException._hx_interfaces = []
hxsublime_Exceptions_CreateTempFileOrFolderException._hx_super = Exception

# print hxsublime.Execute.Execute
class hxsublime_Execute:

	pass




def Execute_statics_run_cmd_async(args,callback,input = None,cwd = None,env = None):
	if input is None:
		input = None
	
	if cwd is None:
		cwd = None
	
	if env is None:
		env = None
	
	def _hx_local_0():
		r = hxsublime_Execute.run_cmd(args, input, cwd, env)
		out = r[0]
		err = r[1]
		def _hx_local_1():
			f = callback
			a1 = out
			a2 = err
			def _hx_local_2():
				return f(a1, a2)
			return _hx_local_2
		
		sublime_Sublime.set_timeout(_hx_local_1(), 1)
	
	in_thread = _hx_local_0
	python_lib_ThreadLowLevel.start_new_thread(in_thread, __builtin__.tuple())
	
hxsublime_Execute.run_cmd_async = Execute_statics_run_cmd_async
def Execute_statics_run_cmd(args,input = None,cwd = None,env = None):
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
			
			return python_Lib_HaxeIterator(p)
		
		_it = _hx_local_0()
		while _it.hasNext():
			k = _it.next()
			val = env1.get(k, None)
			val1 = python_lib_os_Path.expandvars(val)
			python_lib_Types_DictImpl.set(env1, k, val1)
			
			
		
		
		def _hx_local_1(s):
			return s != ""
		encoded_args = __builtin__.list(__builtin__.filter(_hx_local_1, args))
		p = None
		o = _Hx_AnonObject(cwd = cwd ,stdout = python_lib_Subprocess.PIPE ,stderr = python_lib_Subprocess.PIPE ,stdin = python_lib_Subprocess.PIPE ,startupinfo = hxsublime_Plugin.startupInfo() ,env = env1 )
		if __builtin__.hasattr(o, "bufsize"):
			o.bufsize = o.bufsize
		else:
			o.bufsize = 0
		if __builtin__.hasattr(o, "executable"):
			o.executable = o.executable
		else:
			o.executable = None
		if __builtin__.hasattr(o, "stdin"):
			o.stdin = o.stdin
		else:
			o.stdin = None
		if __builtin__.hasattr(o, "stdout"):
			o.stdout = o.stdout
		else:
			o.stdout = None
		if __builtin__.hasattr(o, "stderr"):
			o.stderr = o.stderr
		else:
			o.stderr = None
		if __builtin__.hasattr(o, "preexec_fn"):
			o.preexec_fn = o.preexec_fn
		else:
			o.preexec_fn = None
		if __builtin__.hasattr(o, "close_fds"):
			o.close_fds = o.close_fds
		else:
			o.close_fds = None
		if __builtin__.hasattr(o, "shell"):
			o.shell = o.shell
		else:
			o.shell = None
		if __builtin__.hasattr(o, "cwd"):
			o.cwd = o.cwd
		else:
			o.cwd = None
		if __builtin__.hasattr(o, "env"):
			o.env = o.env
		else:
			o.env = None
		if __builtin__.hasattr(o, "universal_newlines"):
			o.universal_newlines = o.universal_newlines
		else:
			o.universal_newlines = None
		if __builtin__.hasattr(o, "startupinfo"):
			o.startupinfo = o.startupinfo
		else:
			o.startupinfo = None
		if __builtin__.hasattr(o, "creationflags"):
			o.creationflags = o.creationflags
		else:
			o.creationflags = 0
		p = python_lib_subprocess_Popen(encoded_args, o.bufsize, o.executable, o.stdin, o.stdout, o.stderr, o.preexec_fn, o.close_fds, o.shell, o.cwd, o.env, o.universal_newlines, o.startupinfo, o.creationflags)
		
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
			haxe_Log.trace(e, _Hx_AnonObject(fileName = "Execute.hx" ,lineNumber = 74 ,className = "hxsublime.Execute" ,methodName = "run_cmd" ))
			p = args[0]
			err = "Error while running " + p + ": in " + cwd + " (" + Std.string(e) + ")"
			return ("", err)
	
		else:
			raise _hx_e
	
hxsublime_Execute.run_cmd = Execute_statics_run_cmd


hxsublime_Execute._hx_class = hxsublime_Execute
hxsublime_Execute._hx_class_name = "hxsublime.Execute"
_hx_classes['hxsublime.Execute'] = hxsublime_Execute
hxsublime_Execute._hx_fields = []
hxsublime_Execute._hx_props = []
hxsublime_Execute._hx_methods = []
hxsublime_Execute._hx_statics = ["run_cmd_async","run_cmd"]
hxsublime_Execute._hx_interfaces = []

# print hxsublime.Haxelib.HaxeLibLibrary
class hxsublime_Haxelib_HaxeLibLibrary:


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
			t = hxsublime_Types.extract_types(self.path)
			self.classes = t.all_types()
			self.packages = t.packs()
		
		
		return (self.classes, self.packages)
	







hxsublime_Haxelib_HaxeLibLibrary._hx_class = hxsublime_Haxelib_HaxeLibLibrary
hxsublime_Haxelib_HaxeLibLibrary._hx_class_name = "hxsublime.HaxeLibLibrary"
_hx_classes['hxsublime.HaxeLibLibrary'] = hxsublime_Haxelib_HaxeLibLibrary
hxsublime_Haxelib_HaxeLibLibrary._hx_fields = ["name","dev","version","classes","packages","path"]
hxsublime_Haxelib_HaxeLibLibrary._hx_props = []
hxsublime_Haxelib_HaxeLibLibrary._hx_methods = ["as_cmd_arg","extract_types"]
hxsublime_Haxelib_HaxeLibLibrary._hx_statics = []
hxsublime_Haxelib_HaxeLibLibrary._hx_interfaces = []

# print python.lib.Re.Re
import re as python_lib_Re
# print hxsublime.Haxelib.HaxeLibManager
class hxsublime_Haxelib_HaxeLibManager:


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
	

	def get_completions(self):
		comps = []
		_it = self.available().keys()
		while _it.hasNext():
			k = _it.next()
			lib = self.available().get(k)
			haxe_Log.trace(lib, _Hx_AnonObject(fileName = "Haxelib.hx" ,lineNumber = 102 ,className = "hxsublime.HaxeLibManager" ,methodName = "get_completions" ))
			x = (lib.name + " [" + lib.version + "]", lib.name)
			comps.append(x)
			__builtin__.len(comps)
			
			
			
		
		
		return comps
	

	def scan(self):
		self.scanned = True
		env = self.project.haxe_env()
		cmd = self.project.haxelib_exec()
		cmd.append("config")
		__builtin__.len(cmd)
		
		r = hxsublime_Execute.run_cmd(cmd, None, None, env)
		hlout = r[0]
		hlerr = r[1]
		self.basePath = hlout.strip(None)
		self._available = haxe_ds_StringMap()
		cmd1 = self.project.haxelib_exec()
		cmd1.append("list")
		__builtin__.len(cmd1)
		
		r1 = hxsublime_Execute.run_cmd(cmd1, None, None, env)
		hlout1 = r1[0]
		hlerr1 = r1[1]
		_g = 0
		_g1 = hlout1.split("\n")
		while _g < len(_g1):
			l = _g1[_g]
			_g = _g + 1
			found = hxsublime_Haxelib_HaxeLibManager.libLine.match(l)
			if found is not None:
				g = found.groups(None)
				if g is not None:
					name = g[0]
					dev = g[1]
					version = g[2]
					lib = hxsublime_Haxelib_HaxeLibLibrary(self, name, dev is not None, version)
					self._available.set(name, lib)
				
				
			
			
		
		
	

	def install_lib(self,lib):
		cmd = self.project.haxelib_exec()
		env = self.project.haxe_env()
		cmd.append("install")
		__builtin__.len(cmd)
		
		cmd.append(lib)
		__builtin__.len(cmd)
		
		haxe_Log.trace(Std.string(cmd), _Hx_AnonObject(fileName = "Haxelib.hx" ,lineNumber = 155 ,className = "hxsublime.HaxeLibManager" ,methodName = "install_lib" ))
		hxsublime_Execute.run_cmd(cmd, None, None, env)
		self.scan()
	

	def remove_lib(self,lib):
		cmd = self.project.haxelib_exec()
		env = self.project.haxe_env()
		cmd.append("remove")
		__builtin__.len(cmd)
		
		cmd.append(lib)
		__builtin__.len(cmd)
		
		haxe_Log.trace(Std.string(cmd), _Hx_AnonObject(fileName = "Haxelib.hx" ,lineNumber = 166 ,className = "hxsublime.HaxeLibManager" ,methodName = "remove_lib" ))
		hxsublime_Execute.run_cmd(cmd, None, None, env)
		self.scan()
	

	def upgrade_all(self):
		cmd = self.project.haxelib_exec()
		env = self.project.haxe_env()
		cmd.append("upgrade")
		__builtin__.len(cmd)
		
		haxe_Log.trace(Std.string(cmd), _Hx_AnonObject(fileName = "Haxelib.hx" ,lineNumber = 176 ,className = "hxsublime.HaxeLibManager" ,methodName = "upgrade_all" ))
		hxsublime_Execute.run_cmd(cmd, None, None, env)
		self.scan()
	

	def self_update(self):
		cmd = self.project.haxelib_exec()
		env = self.project.haxe_env()
		cmd.append("thisupdate")
		__builtin__.len(cmd)
		
		haxe_Log.trace(Std.string(cmd), _Hx_AnonObject(fileName = "Haxelib.hx" ,lineNumber = 186 ,className = "hxsublime.HaxeLibManager" ,methodName = "self_update" ))
		hxsublime_Execute.run_cmd(cmd, None, None, env)
		self.scan()
	

	def search_libs(self):
		cmd = self.project.haxelib_exec()
		env = self.project.haxe_env()
		cmd.append("search")
		__builtin__.len(cmd)
		
		cmd.append("_")
		__builtin__.len(cmd)
		
		res = hxsublime_Execute.run_cmd(cmd, None, None, env)
		out = res[0]
		err = res[1]
		return self._collect_libraries(out)
	

	def _collect_libraries(self,out):
		x = None
		_this = out.split("\n")
		def _hx_local_0(x1):
			return x1 != "" and x1.find("libraries found") == -1
		x = __builtin__.list(__builtin__.filter(_hx_local_0, _this))
		
		x.reverse()
		return x
	

	def is_lib_installed(self,lib):
		return self.available().exists(lib)

	def get_lib(self,lib):
		return self.available().get(lib)





hxsublime_Haxelib_HaxeLibManager.__meta__ = _Hx_AnonObject(fields = _Hx_AnonObject(available = _Hx_AnonObject(property = None ) ) )
hxsublime_Haxelib_HaxeLibManager.libLine = python_lib_Re.compile("([^:]*):[^\\[]*\\[(dev\\:)?(.*)\\]")


hxsublime_Haxelib_HaxeLibManager._hx_class = hxsublime_Haxelib_HaxeLibManager
hxsublime_Haxelib_HaxeLibManager._hx_class_name = "hxsublime.HaxeLibManager"
_hx_classes['hxsublime.HaxeLibManager'] = hxsublime_Haxelib_HaxeLibManager
hxsublime_Haxelib_HaxeLibManager._hx_fields = ["_available","project","basePath","scanned"]
hxsublime_Haxelib_HaxeLibManager._hx_props = []
hxsublime_Haxelib_HaxeLibManager._hx_methods = ["available","get","get_completions","scan","install_lib","remove_lib","upgrade_all","self_update","search_libs","_collect_libraries","is_lib_installed","get_lib"]
hxsublime_Haxelib_HaxeLibManager._hx_statics = ["__meta__","libLine"]
hxsublime_Haxelib_HaxeLibManager._hx_interfaces = []

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
	
	elif hxsublime_Settings.use_debug_panel():
		def _hx_local_0():
			hxsublime_panel_Base_Panels.debug_panel().writeln(msg)
		f = _hx_local_0
		sublime_Sublime.set_timeout(f, 100)
	
	else:
		try:
			haxe_Log.trace(msgStr, _Hx_AnonObject(fileName = "Log.hx" ,lineNumber = 32 ,className = "hxsublime.Log" ,methodName = "log" ))
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

# print hxsublime.Main.Hui
class hxsublime_Main_Hui:


	def __init__(self):
		None
	def foo(self):
		return 1





def Hui_statics_doIt():
	None
hxsublime_Main_Hui.doIt = Hui_statics_doIt


hxsublime_Main_Hui._hx_class = hxsublime_Main_Hui
hxsublime_Main_Hui._hx_class_name = "hxsublime.Hui"
_hx_classes['hxsublime.Hui'] = hxsublime_Main_Hui
hxsublime_Main_Hui._hx_fields = []
hxsublime_Main_Hui._hx_props = []
hxsublime_Main_Hui._hx_methods = ["foo"]
hxsublime_Main_Hui._hx_statics = ["doIt"]
hxsublime_Main_Hui._hx_interfaces = []

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




def Plugin_statics_plugin_base_dir():
	return python_lib_os_Path.abspath(python_lib_os_Path.join(python_lib_os_Path.dirname(__file__), "."))
hxsublime_Plugin.plugin_base_dir = Plugin_statics_plugin_base_dir
hxsublime_Plugin._startupInfo = None
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
hxsublime_Plugin._hx_statics = ["plugin_base_dir","_startupInfo","startupInfo"]
hxsublime_Plugin._hx_interfaces = []

# print hxsublime.Settings.Settings
class hxsublime_Settings:

	pass




def Settings_statics_plugin_settings():
	return sublime_Sublime.load_settings("Haxe.sublime-settings")
hxsublime_Settings.plugin_settings = Settings_statics_plugin_settings
def Settings_statics_get_from_settings(id,settings,plugin):
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
	
hxsublime_Settings.get_from_settings = Settings_statics_get_from_settings
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
		res = hxsublime_Settings.get_from_settings(id, settings, False)
	
	
	if res is None:
		res = hxsublime_Settings.get_from_settings(id, hxsublime_Settings.plugin_settings(), True)
	
	return res
	
hxsublime_Settings.get = Settings_statics_get
def Settings_statics_get_bool(id,defaultVal,view = None):
	if view is None:
		view = None
	
	r = hxsublime_Settings.get(id, view)
	if r is None:
		return defaultVal
	elif Std._hx_is(r, Bool):
		return r
	else:
		return None
	
hxsublime_Settings.get_bool = Settings_statics_get_bool
def Settings_statics_get_int(id,defaultVal,view = None):
	if view is None:
		view = None
	
	r = hxsublime_Settings.get(id, view)
	if r is None:
		return defaultVal
	elif Std._hx_is(r, Int):
		return r
	else:
		return None
	
hxsublime_Settings.get_int = Settings_statics_get_int
def Settings_statics_get_string(id,defaultVal,view = None):
	if view is None:
		view = None
	
	r = hxsublime_Settings.get(id, view)
	if r is None:
		return defaultVal
	elif Std._hx_is(r, String):
		return r
	else:
		return None
	
hxsublime_Settings.get_string = Settings_statics_get_string
def Settings_statics_no_fuzzy_completion(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.get_bool("haxe_completion_no_fuzzy", False, view)
	
hxsublime_Settings.no_fuzzy_completion = Settings_statics_no_fuzzy_completion
def Settings_statics_top_level_completions_on_demand(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.get_bool("haxe_completions_top_level_only_on_demand", False, view)
	
hxsublime_Settings.top_level_completions_on_demand = Settings_statics_top_level_completions_on_demand
def Settings_statics_show_only_async_completions(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.get_bool("haxe_completions_show_only_async", True, view)
	
hxsublime_Settings.show_only_async_completions = Settings_statics_show_only_async_completions
def Settings_statics_is_async_completion(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.get_bool("haxe_completion_async", True, view)
	
hxsublime_Settings.is_async_completion = Settings_statics_is_async_completion
def Settings_statics_get_completion_delays(view = None):
	if view is None:
		view = None
	
	a = hxsublime_Settings.get_int("haxe_completion_async_timing_hide", 60, view)
	b = hxsublime_Settings.get_int("haxe_completion_async_timing_show", 150, view)
	return (a, b)
	
	
hxsublime_Settings.get_completion_delays = Settings_statics_get_completion_delays
def Settings_statics_show_completion_times(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.get_bool("haxe_completion_show_times", False, view)
	
hxsublime_Settings.show_completion_times = Settings_statics_show_completion_times
def Settings_statics_haxe_exec(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.get_string("haxe_exec", "haxe", view)
	
hxsublime_Settings.haxe_exec = Settings_statics_haxe_exec
def Settings_statics_use_haxe_servermode(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.get_bool("haxe_use_servermode", True, view)
	
hxsublime_Settings.use_haxe_servermode = Settings_statics_use_haxe_servermode
def Settings_statics_use_haxe_servermode_wrapper(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.get_bool("haxe_use_servermode_wrapper", False, view)
	
hxsublime_Settings.use_haxe_servermode_wrapper = Settings_statics_use_haxe_servermode_wrapper
def Settings_statics_haxe_sdk_path(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.get_string("haxe_sdk_path", None, view)
	
hxsublime_Settings.haxe_sdk_path = Settings_statics_haxe_sdk_path
def Settings_statics_open_with_default_app(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.get_string("haxe_open_with_default_app", None, view)
	
hxsublime_Settings.open_with_default_app = Settings_statics_open_with_default_app
def Settings_statics_haxe_inst_path(view = None):
	if view is None:
		view = None
	
	tmp = hxsublime_Settings.haxe_sdk_path(view)
	defaultVal = None
	if tmp is not None:
		defaultVal = python_lib_os_Path.normpath(hxsublime_Settings.haxe_sdk_path(view)) + python_lib_os_Path.sep + "haxe"
	else:
		defaultVal = None
	if tmp is None and hxsublime_Settings.haxe_exec(view) != "haxe":
		defaultVal = python_lib_os_Path.normpath(python_lib_os_Path.dirname(hxsublime_Settings.haxe_exec(view)))
	
	return hxsublime_Settings.get_string("haxe_inst_path", defaultVal, view)
	
hxsublime_Settings.haxe_inst_path = Settings_statics_haxe_inst_path
def Settings_statics_neko_inst_path(view = None):
	if view is None:
		view = None
	
	tmp = hxsublime_Settings.haxe_sdk_path(view)
	defaultVal = None
	if tmp is not None:
		defaultVal = python_lib_os_Path.normpath(hxsublime_Settings.haxe_sdk_path(view)) + python_lib_os_Path.sep + "default"
	else:
		defaultVal = None
	return hxsublime_Settings.get_string("neko_inst_path", defaultVal, view)
	
hxsublime_Settings.neko_inst_path = Settings_statics_neko_inst_path
def Settings_statics_haxe_library_path(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.get_string("haxe_library_path", None, view)
	
hxsublime_Settings.haxe_library_path = Settings_statics_haxe_library_path
def Settings_statics_haxelib_exec(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.get_string("haxe_haxelib_exec", "haxelib", view)
	
hxsublime_Settings.haxelib_exec = Settings_statics_haxelib_exec
def Settings_statics_smart_snippets(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.get_bool("haxe_completion_smart_snippets", True, view)
	
hxsublime_Settings.smart_snippets = Settings_statics_smart_snippets
def Settings_statics_smart_snippets_on_completion(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.get_bool("haxe_completion_smart_snippets_on_completion", False, view)
	
hxsublime_Settings.smart_snippets_on_completion = Settings_statics_smart_snippets_on_completion
def Settings_statics_smart_snippets_just_current(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.get_bool("haxe_completion_smart_snippets_just_current", False, view)
	
hxsublime_Settings.smart_snippets_just_current = Settings_statics_smart_snippets_just_current
def Settings_statics_use_debug_panel(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.get_bool("haxe_use_debug_panel", False, view)
	
hxsublime_Settings.use_debug_panel = Settings_statics_use_debug_panel
def Settings_statics_check_on_save(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.get_bool("haxe_check_on_save", True, view)
	
hxsublime_Settings.check_on_save = Settings_statics_check_on_save
def Settings_statics_use_slide_panel(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.get_bool("haxe_use_slide_panel", True, view)
	
hxsublime_Settings.use_slide_panel = Settings_statics_use_slide_panel
def Settings_statics_use_haxe_servermode_for_builds(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.get_bool("haxe_use_servermode_for_builds", False, view)
	
hxsublime_Settings.use_haxe_servermode_for_builds = Settings_statics_use_haxe_servermode_for_builds
def Settings_statics_use_offset_completion(view = None):
	if view is None:
		view = None
	
	return hxsublime_Settings.get_bool("haxe_use_offset_completion", False, view)
	
hxsublime_Settings.use_offset_completion = Settings_statics_use_offset_completion


hxsublime_Settings._hx_class = hxsublime_Settings
hxsublime_Settings._hx_class_name = "hxsublime.Settings"
_hx_classes['hxsublime.Settings'] = hxsublime_Settings
hxsublime_Settings._hx_fields = []
hxsublime_Settings._hx_props = []
hxsublime_Settings._hx_methods = []
hxsublime_Settings._hx_statics = ["plugin_settings","get_from_settings","get","get_bool","get_int","get_string","no_fuzzy_completion","top_level_completions_on_demand","show_only_async_completions","is_async_completion","get_completion_delays","show_completion_times","haxe_exec","use_haxe_servermode","use_haxe_servermode_wrapper","haxe_sdk_path","open_with_default_app","haxe_inst_path","neko_inst_path","haxe_library_path","haxelib_exec","smart_snippets","smart_snippets_on_completion","smart_snippets_just_current","use_debug_panel","check_on_save","use_slide_panel","use_haxe_servermode_for_builds","use_offset_completion"]
hxsublime_Settings._hx_interfaces = []

# print hxsublime.Temp.Temp
class hxsublime_Temp:

	pass




def Temp_statics_get_temp_path_id(build):
	path = build.get_build_folder()
	if path is None:
		raise _HxException(hxsublime_Exceptions_ExtractBuildPathException(build))
	
	path1 = None
	def _hx_local_0():
		_this1 = path.split(python_lib_Os.sep)
		return "_".join(_this1)
	
	_this = (_hx_local_0()).split(":")
	path1 = "_".join(_this)
	
	temp_path = python_lib_os_Path.join(python_lib_Tempfile.gettempdir(), "haxe_sublime_hx" + path1 + "_")
	return temp_path
	
hxsublime_Temp.get_temp_path_id = Temp_statics_get_temp_path_id
def Temp_statics_create_temp_path(build):
	temp_path = hxsublime_Temp.get_temp_path_id(build)
	hxsublime_tools_PathTools.removeDir(temp_path)
	python_lib_Os.makedirs(temp_path)
	return temp_path
	
hxsublime_Temp.create_temp_path = Temp_statics_create_temp_path
def Temp_statics_create_file(temp_path,build,orig_file,content):
	relative = build.get_relative_path(orig_file)
	haxe_Log.trace(relative, _Hx_AnonObject(fileName = "Temp.hx" ,lineNumber = 47 ,className = "hxsublime.Temp" ,methodName = "create_file" ))
	haxe_Log.trace(orig_file, _Hx_AnonObject(fileName = "Temp.hx" ,lineNumber = 48 ,className = "hxsublime.Temp" ,methodName = "create_file" ))
	haxe_Log.trace("relative:" + Std.string(relative), _Hx_AnonObject(fileName = "Temp.hx" ,lineNumber = 49 ,className = "hxsublime.Temp" ,methodName = "create_file" ))
	if relative is None:
		raise _HxException(hxsublime_Exceptions_GetRelativePathException(build, orig_file))
	
	new_file = python_lib_os_Path.join(temp_path, relative)
	new_file_dir = python_lib_os_Path.dirname(new_file)
	if not python_lib_os_Path.exists(new_file_dir):
		python_lib_Os.makedirs(new_file_dir)
	
	f = python_lib_Codecs.open(new_file, "wb", "utf-8", "ignore")
	f.write(content)
	f.close()
	haxe_Log.trace(new_file, _Hx_AnonObject(fileName = "Temp.hx" ,lineNumber = 63 ,className = "hxsublime.Temp" ,methodName = "create_file" ))
	return new_file
	
hxsublime_Temp.create_file = Temp_statics_create_file
def Temp_statics_create_temp_path_and_file(build,orig_file,content):
	temp_path = hxsublime_Temp.create_temp_path(build)
	temp_file = hxsublime_Temp.create_file(temp_path, build, orig_file, content)
	return (temp_path, temp_file)
	
hxsublime_Temp.create_temp_path_and_file = Temp_statics_create_temp_path_and_file
def Temp_statics_remove_path(temp_path):
	if temp_path is not None:
		hxsublime_tools_PathTools.removeDir(temp_path)
	
hxsublime_Temp.remove_path = Temp_statics_remove_path


hxsublime_Temp._hx_class = hxsublime_Temp
hxsublime_Temp._hx_class_name = "hxsublime.Temp"
_hx_classes['hxsublime.Temp'] = hxsublime_Temp
hxsublime_Temp._hx_fields = []
hxsublime_Temp._hx_props = []
hxsublime_Temp._hx_methods = []
hxsublime_Temp._hx_statics = ["get_temp_path_id","create_temp_path","create_file","create_temp_path_and_file","remove_path"]
hxsublime_Temp._hx_interfaces = []

# print hxsublime.Types.Types
class hxsublime_Types:

	pass




def Types_statics_find_types(classpaths,libs,base_path,filtered_classes = None,filtered_packages = None,include_private_types = True):
	if filtered_classes is None:
		filtered_classes = None
	
	if filtered_packages is None:
		filtered_packages = None
	
	if include_private_types is None:
		include_private_types = True
	
	bundle = hxsublime_tools_HxSrcTools.empty_type_bundle()
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
			b = hxsublime_Types.extract_types(p, filtered_classes, filtered_packages, 0, [], include_private_types)
			bundle = bundle.merge(b)
		
		else:
			hxsublime_panel_Base_Panels.default_panel().writeln("Error: The classpath " + p + " does not exist, in case of nme or openfl you need have to build (CTRL + ENTER) the project first (the build creates these paths)")
	
	
	return bundle
	
hxsublime_Types.find_types = Types_statics_find_types
hxsublime_Types.valid_package = python_lib_Re.compile("^[_a-z][a-zA-Z0-9_]*$")
def Types_statics_is_valid_package(pack):
	return hxsublime_Types.valid_package.match(pack) is not None and pack != "_std"
hxsublime_Types.is_valid_package = Types_statics_is_valid_package
def Types_statics_extract_types(path,filtered_classes = None,filtered_packages = None,depth = 0,pack = None,include_private_types = True):
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
	
	bundle = hxsublime_tools_HxSrcTools.empty_type_bundle()
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
				module_bundle = hxsublime_Types.extract_types_from_file(file, cl, include_private_types)
				bundle = bundle.merge(module_bundle)
			
			
		
		
	
	
	_g = 0
	_g1 = python_lib_Os.listdir(path)
	while _g < len(_g1):
		f = _g1[_g]
		_g = _g + 1
		if hxsublime_Types.is_valid_package(f):
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
				
				sub_bundle = hxsublime_Types.extract_types(python_lib_os_Path.join(path, f), filtered_classes, filtered_packages, depth + 1, next_pack, include_private_types)
				bundle = bundle.merge(sub_bundle)
			
			
		
		
	
	
	return bundle
	
hxsublime_Types.extract_types = Types_statics_extract_types
hxsublime_Types.file_type_cache = haxe_ds_StringMap()
def Types_statics_extract_types_from_file(file,module_name = None,include_private_types = True):
	if module_name is None:
		module_name = None
	
	if include_private_types is None:
		include_private_types = True
	
	mtime = python_lib_os_Path.getmtime(file)
	def _hx_local_2():
		def _hx_local_1():
			def _hx_local_0():
				_this = hxsublime_Types.file_type_cache.get(file)
				return _this[0]
			
			return _hx_local_0() == mtime
		
		return hxsublime_Types.file_type_cache.exists(file) and _hx_local_1()
	
	if _hx_local_2():
		_this = hxsublime_Types.file_type_cache.get(file)
		return _this[1]
	
	
	if module_name is None:
		_this = python_lib_os_Path.splitext(python_lib_os_Path.basename(file))
		module_name = _this[0]
	
	
	s = python_lib_Codecs.open(file, "r", "utf-8", "ignore")
	src_with_comments = s.read()
	src = hxsublime_tools_HxSrcTools.strip_comments(src_with_comments)
	bundle = hxsublime_tools_HxSrcTools.get_types_from_src(src, module_name, file, src_with_comments)
	hxsublime_Types.file_type_cache.set(file, (mtime, bundle))
	return bundle
	
hxsublime_Types.extract_types_from_file = Types_statics_extract_types_from_file


hxsublime_Types._hx_class = hxsublime_Types
hxsublime_Types._hx_class_name = "hxsublime.Types"
_hx_classes['hxsublime.Types'] = hxsublime_Types
hxsublime_Types._hx_fields = []
hxsublime_Types._hx_props = []
hxsublime_Types._hx_methods = []
hxsublime_Types._hx_statics = ["find_types","valid_package","is_valid_package","extract_types","file_type_cache","extract_types_from_file"]
hxsublime_Types._hx_interfaces = []

# print hxsublime.build.HxmlBuild.HxmlBuild
class hxsublime_build_HxmlBuild:


	def __init__(self,hxml,build_file):
		self.show_times = False
		self._std_bundle = hxsublime_tools_HxSrcTools.empty_type_bundle()
		self._args = []
		self.main = None
		self._target = None
		self.output = "dummy.js"
		self._hxml = hxml
		self._build_file = build_file
		self._classpaths = []
		self.libs = []
		self.type_bundle = None
		self._update_time = None
		self.mode_completion = False
		self.defines = []
		self.name = None
	
	# var show_times
	# var _std_bundle
	# var _args
	# var main
	# var _target
	# var output
	# var _hxml
	# var _build_file
	# var _classpaths
	# var libs
	# var type_bundle
	# var _update_time
	# var mode_completion
	# var defines
	# var name
	def std_bundle(self):
		return self._std_bundle

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

	def build_file(self):
		return self._build_file

	def add_define(self,define):
		_this = self.defines
		_this.append(define)
		__builtin__.len(_this)
		
	

	def set_main(self,main):
		self.main = main

	def get_name(self):
		n = None
		if self.name is not None:
			n = self.name
		elif self.main is None:
			n = "[No Main]"
		else:
			n = self.main
		return n
	

	def set_std_bundle(self,std_bundle):
		self._std_bundle = std_bundle

	def args(self):
		return self._args

	def equals(self,other):
		return self.args() == other._args() and self.main == other.main and self.name == other.name and self._target == other._target and self.output == other.output and self.hxml == other.hxml and self.classpaths == other.classpaths and self.libs == other.libs and self.show_times == other.show_times and self.mode_completion == other.mode_completion and self.defines == other.defines and self._build_file == other._build_file

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
		self.get_types()
		hb = hxsublime_build_HxmlBuild(self._hxml, self.build_file())
		_this = self.args()
		hb._args = __builtin__.list(_this)
		
		hb.main = self.main
		hb.name = self.name
		hb._target = self._target
		hb.output = self.output
		hb.defines = __builtin__.list(self.defines)
		hb._std_bundle = self._std_bundle
		hb._classpaths = __builtin__.list(self._classpaths)
		hb.libs = __builtin__.list(self.libs)
		hb.type_bundle = self.type_bundle
		hb._update_time = self._update_time
		hb.show_times = self.show_times
		hb.mode_completion = self.mode_completion
		return hb
	

	def add_arg(self,arg):
		_this = self._args
		_this.append(arg)
		__builtin__.len(_this)
		
	

	def get_build_folder(self):
		if self.build_file is not None:
			return python_lib_os_Path.dirname(self.build_file())
		else:
			return None

	def set_build_cwd(self):
		self.set_cwd(self.get_build_folder())

	def align_drive_letter(self,path):
		is_win = sublime_Sublime.platform() == "windows"
		if is_win:
			reg = python_lib_Re.compile("^([a-z]):(.*)$")
			match = python_lib_Re.match(reg, path)
			if match is not None:
				def _hx_local_2():
					def _hx_local_1():
						def _hx_local_0():
							_this = match.group(1)
							return _this.upper()
						
						return _hx_local_0() + ":"
					
					return _hx_local_1() + match.group(2)
				
				path = _hx_local_2()
			
			
		
		
		return path
	

	def add_classpath(self,cp):
		cp1 = self.align_drive_letter(cp)
		if not Lambda.has(self._classpaths, cp1):
			_this = self._classpaths
			_this.append(cp1)
			__builtin__.len(_this)
			
			
			_this = self._args
			x = ("-cp", cp1)
			_this.append(x)
			__builtin__.len(_this)
			
			
		
		
	

	def add_lib(self,lib):
		_this = self.libs
		_this.append(lib)
		__builtin__.len(_this)
		
		
		self.add_arg(("-lib", lib.name))
	

	def get_classpath_of_file(self,file):
		file1 = self.align_drive_letter(file)
		cps = __builtin__.list(self._classpaths)
		build_folder = self.get_build_folder()
		if build_folder is not None and not Lambda.has(cps, build_folder):
			haxe_Log.trace("add build folder to classpaths: " + build_folder + ", classpaths: " + Std.string(cps), _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 230 ,className = "hxsublime.build.HxmlBuild" ,methodName = "get_classpath_of_file" ))
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
	

	def is_file_in_classpath(self,file):
		file = self.align_drive_letter(file)
		return self.get_classpath_of_file(file) is not None
	

	def get_relative_path(self,file):
		file = self.align_drive_letter(file)
		cp = self.get_classpath_of_file(file)
		haxe_Log.trace(file, _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 258 ,className = "hxsublime.build.HxmlBuild" ,methodName = "get_relative_path" ))
		haxe_Log.trace(StringTools.replace(file, cp, ""), _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 259 ,className = "hxsublime.build.HxmlBuild" ,methodName = "get_relative_path" ))
		def _hx_local_0():
			_this = StringTools.replace(file, cp, "")
			return python_Tools.substr(_this, 1, None)
		
		haxe_Log.trace(_hx_local_0(), _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 260 ,className = "hxsublime.build.HxmlBuild" ,methodName = "get_relative_path" ))
		if cp is not None:
			_this = StringTools.replace(file, cp, "")
			return python_Tools.substr(_this, 1, None)
		
		else:
			return None
	

	def target_to_string(self):
		target = None
		if self._target is None:
			target = "js"
		else:
			target = self._target
			if target == "js" and Lambda.has(self.defines, "nodejs"):
				target = "node.js"
			
		
		return target
	

	def to_string(self):
		out = python_lib_os_Path.basename(self.output)
		main = self.get_name()
		target = self.target_to_string()
		return "" + main + " (" + target + " - " + out + ")"
	

	def make_hxml(self):
		outp = "# Autogenerated " + Std.string(self.hxml) + "\n\n"
		outp = outp + "# " + self.to_string() + "\n"
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
	

	def set_cwd(self,cwd):
		_this = self._args
		x = ("--cwd", cwd)
		_this.append(x)
		__builtin__.len(_this)
		
	

	def set_times(self):
		self.show_times = True
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
		
		
	

	def set_server_mode(self,server_port = 6000):
		if server_port is None:
			server_port = 6000
		
		_this = self._args
		x = None
		b = Std.string(server_port)
		x = ("--connect", b)
		
		_this.append(x)
		__builtin__.len(_this)
		
	

	def get_command_args(self,haxe_path):
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
	

	def set_auto_completion(self,display,macro_completion = False,no_output = True):
		if macro_completion is None:
			macro_completion = False
		
		if no_output is None:
			no_output = True
		
		self.mode_completion = True
		args = self._args
		self.main = None
		def _hx_local_0(x):
			return x[0] != "-cs" and x[0] != "-x" and x[0] != "-js" and x[0] != "-php" and x[0] != "-cpp" and x[0] != "-swf" and x[0] != "-java"
		filterTargets = _hx_local_0
		if macro_completion:
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
		filter_commands_and_dce = _hx_local_2
		args = __builtin__.list(__builtin__.filter(filter_commands_and_dce, args))
		if not self.show_times:
			def _hx_local_3(x):
				return x[0] != "--times"
			filter_times = _hx_local_3
			_this = __builtin__.list(__builtin__.filter(filter_times, args))
			args = __builtin__.list(_this)
			
		
		
		if macro_completion:
			x = ("-neko", "__temp.n")
			args.append(x)
			__builtin__.len(args)
			
		
		
		x = ("--display", display)
		args.append(x)
		__builtin__.len(args)
		
		
		if no_output:
			x = ("--no-output", "")
			args.append(x)
			__builtin__.len(args)
			
		
		
		self._args = args
	

	def _update_types(self):
		haxe_Log.trace("update types for classpaths:" + Std.string(self._classpaths), _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 415 ,className = "hxsublime.build.HxmlBuild" ,methodName = "_update_types" ))
		haxe_Log.trace("update types for libs:" + Std.string(self.libs), _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 416 ,className = "hxsublime.build.HxmlBuild" ,methodName = "_update_types" ))
		self.type_bundle = hxsublime_Types.find_types(self._classpaths, self.libs, self.get_build_folder(), [], [], False)
	

	def _should_refresh_types(self,now):
		return self.type_bundle is None or self._update_time is None or now - self._update_time > 10

	def get_types(self):
		now = python_lib_Time.time()
		if self._should_refresh_types(now):
			haxe_Log.trace("UPDATE THE TYPES NOW", _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 437 ,className = "hxsublime.build.HxmlBuild" ,methodName = "get_types" ))
			self._update_time = now
			self._update_types()
		
		
		return self.type_bundle
	

	def prepare_check_cmd(self,project,server_mode,view):
		r = self.prepare_build_cmd(project, server_mode, view)
		cmd = r[0]
		build_folder = r[1]
		cmd.append("--no-output")
		__builtin__.len(cmd)
		
		return (cmd, build_folder)
	

	def absolute_output(self):
		if python_lib_os_Path.isabs(self.output):
			return self.output
		else:
			return self.get_build_folder() + "/" + self.output

	def prepare_run_cmd(self,project,server_mode,view):
		r = self._prepare_run(project, view, server_mode)
		cmd = r[0]
		build_folder = r[1]
		nekox_file = r[2]
		haxe_Log.trace(self.args, _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 471 ,className = "hxsublime.build.HxmlBuild" ,methodName = "prepare_run_cmd" ))
		haxe_Log.trace(cmd, _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 472 ,className = "hxsublime.build.HxmlBuild" ,methodName = "prepare_run_cmd" ))
		haxe_Log.trace(build_folder, _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 473 ,className = "hxsublime.build.HxmlBuild" ,methodName = "prepare_run_cmd" ))
		haxe_Log.trace(nekox_file, _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 474 ,className = "hxsublime.build.HxmlBuild" ,methodName = "prepare_run_cmd" ))
		default_open_ext = hxsublime_Settings.open_with_default_app()
		if nekox_file is not None:
			cmd.extend(["-cmd", "neko " + nekox_file])
		elif self._target == "swf" and default_open_ext is not None:
			x = ["-cmd", default_open_ext + " " + self.absolute_output()]
			cmd.extend(x)
		
		elif self._target == "neko":
			x = ["-cmd", "neko " + self.absolute_output()]
			cmd.extend(x)
		
		elif self._target == "cpp":
			sep_index = self.main.rfind(".", None)
			exe = None
			if sep_index > -1:
				exe = python_Tools.substr(self.main, sep_index + 1, None)
			else:
				exe = self.main
			x = ["-cmd", python_lib_os_Path.join(self.absolute_output(), exe) + "-debug"]
			cmd.extend(x)
			
		
		elif self._target == "js" and Lambda.has(self.defines, "nodejs"):
			x = ["-cmd", "nodejs " + self.absolute_output()]
			cmd.extend(x)
		
		elif self._target == "java":
			sep_index = None
			_this = self.absolute_output()
			sep_index = _this.rfind(python_lib_os_Path.sep, None)
			
			jar = None
			if sep_index == -1:
				jar = self.absolute_output() + ".jar"
			else:
				def _hx_local_1():
					def _hx_local_0():
						_this = self.absolute_output()
						return python_Tools.substr(_this, sep_index + 1, None)
					
					return _hx_local_0() + ".jar"
				
				jar = _hx_local_1()
			
			x = ["-cmd", "java -jar " + python_lib_os_Path.join(self.absolute_output(), jar)]
			cmd.extend(x)
			
		
		elif self._target == "cs":
			x = ["-cmd", "cd " + self.absolute_output()]
			cmd.extend(x)
			
			cmd.extend(["-cmd", "gmcs -recurse:*.cs -main:" + self.main + " -out:" + self.main + ".exe-debug"])
			x = ["-cmd", python_lib_os_Path.join(".", self.main + ".exe-debug")]
			cmd.extend(x)
			
		
		
		return (cmd, build_folder)
	

	def prepare_build_cmd(self,project,server_mode,view):
		r = self._prepare_run(project, view, server_mode)
		cmd = r[0]
		build_folder = r[1]
		return (cmd, build_folder)
	

	def _prepare_run(self,project,view,server_mode = None):
		if server_mode is None:
			server_mode = None
		
		if server_mode is None:
			server_mode = project.is_server_mode()
		else:
			server_mode = server_mode
		run_exec = self._get_run_exec(project, view)
		b = self.copy()
		nekox_file_name = None
		_g1 = 0
		_g = __builtin__.len(b._args)
		while _g1 < _g:
			def _hx_local_0():
				nonlocal _g1
				_hx_r = _g1
				_g1 = _g1 + 1
				return _hx_r
				
			
			i = _hx_local_0()
			a = b._args[i]
			if a[0] == "-x":
				nekox_file_name = a[1] + ".n"
				b._args[i] = ("-neko", nekox_file_name)
			
			
		
		
		if server_mode:
			project.start_server(view)
			b.set_server_mode(project.server.get_server_port())
		
		
		b.set_build_cwd()
		cmd = b.get_command_args(run_exec)
		b1 = self.get_build_folder()
		return (cmd, b1, nekox_file_name)
		
	

	def _get_run_exec(self,project,view):
		return project.haxe_exec(view)

	def escape_cmd(self,cmd):
		print_cmd = __builtin__.list(cmd)
		l = __builtin__.len(print_cmd)
		_g = 0
		while _g < l:
			def _hx_local_0():
				nonlocal _g
				_hx_r = _g
				_g = _g + 1
				return _hx_r
				
			
			i = _hx_local_0()
			e = print_cmd[i]
			if e == "--macro" and i < l - 1:
				print_cmd[i + 1] = "'" + print_cmd[i + 1] + "'"
			
		
		
		return print_cmd
	

	def _run_async(self,project,view,callback,server_mode = None):
		if server_mode is None:
			server_mode = None
		
		_g = self
		env = project.haxe_env(view)
		r = self._prepare_run(project, view, server_mode)
		cmd = r[0]
		build_folder = r[1]
		nekox_file_name = r[2]
		print_cmd = __builtin__.list(cmd)
		_g1 = 0
		_g2 = __builtin__.len(print_cmd)
		while _g1 < _g2:
			def _hx_local_0():
				nonlocal _g1
				_hx_r = _g1
				_g1 = _g1 + 1
				return _hx_r
				
			
			i = _hx_local_0()
			e = print_cmd[i]
			if e == "--macro" and i < __builtin__.len(print_cmd) - 1:
				print_cmd[i + 1] = "'" + print_cmd[i + 1] + "'"
			
		
		
		def _hx_local_1(out,err):
			_g._on_run_complete(out, err, build_folder, nekox_file_name)
			callback(out, err)
		
		cb = _hx_local_1
		hxsublime_Execute.run_cmd_async(cmd, cb, "", build_folder, env)
	

	def _run_sync(self,project,view,server_mode = None):
		if server_mode is None:
			server_mode = None
		
		env = project.haxe_env(view)
		r = self._prepare_run(project, view, server_mode)
		cmd = r[0]
		build_folder = r[1]
		nekox_file_name = r[2]
		haxe_Log.trace(" ".join(cmd), _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 608 ,className = "hxsublime.build.HxmlBuild" ,methodName = "_run_sync" ))
		r1 = hxsublime_Execute.run_cmd(cmd, "", build_folder, env)
		out = r1[0]
		err = r1[1]
		self._on_run_complete(out, err, build_folder, nekox_file_name)
		return (out, err)
	

	def _on_run_complete(self,out,err,build_folder,nekox_file_name):
		haxe_Log.trace("---------------cmd-------------------", _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 620 ,className = "hxsublime.build.HxmlBuild" ,methodName = "_on_run_complete" ))
		haxe_Log.trace("out:" + out, _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 621 ,className = "hxsublime.build.HxmlBuild" ,methodName = "_on_run_complete" ))
		haxe_Log.trace("err:" + err, _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 622 ,className = "hxsublime.build.HxmlBuild" ,methodName = "_on_run_complete" ))
		haxe_Log.trace("---------compiler-output-------------", _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 623 ,className = "hxsublime.build.HxmlBuild" ,methodName = "_on_run_complete" ))
		if nekox_file_name is not None:
			self._run_neko_x(build_folder, nekox_file_name)
		
	

	def _run_neko_x(self,build_folder,neko_file_name):
		neko_file = python_lib_os_Path.join(build_folder, neko_file_name)
		haxe_Log.trace("run nekox: " + neko_file, _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 634 ,className = "hxsublime.build.HxmlBuild" ,methodName = "_run_neko_x" ))
		r = hxsublime_Execute.run_cmd(["neko", neko_file])
		out = r[0]
		err = r[1]
		hxsublime_panel_Base_Panels.default_panel().writeln(out)
		hxsublime_panel_Base_Panels.default_panel().writeln(err)
	

	def run(self,project,view,async,callback,server_mode = None):
		if server_mode is None:
			server_mode = None
		
		if async:
			haxe_Log.trace("RUN ASYNC COMPLETION", _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 644 ,className = "hxsublime.build.HxmlBuild" ,methodName = "run" ))
			self._run_async(project, view, callback, server_mode)
		
		else:
			haxe_Log.trace("RUN SYNC COMPLETION", _Hx_AnonObject(fileName = "HxmlBuild.hx" ,lineNumber = 648 ,className = "hxsublime.build.HxmlBuild" ,methodName = "run" ))
			r = self._run_sync(project, view, server_mode)
			out = r[0]
			err = r[1]
			callback(out, err)
		
	

	def is_type_available(self,type):
		pack = type.toplevel_pack()
		return pack is None or self.is_pack_available(pack)
	

	def is_pack_available(self,pack):
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
	





hxsublime_build_HxmlBuild.__meta__ = _Hx_AnonObject(fields = _Hx_AnonObject(title = _Hx_AnonObject(property = None ) ,build_file = _Hx_AnonObject(property = None ) ,absolute_output = _Hx_AnonObject(property = None ) ) )


hxsublime_build_HxmlBuild._hx_class = hxsublime_build_HxmlBuild
hxsublime_build_HxmlBuild._hx_class_name = "hxsublime.build.HxmlBuild"
_hx_classes['hxsublime.build.HxmlBuild'] = hxsublime_build_HxmlBuild
hxsublime_build_HxmlBuild._hx_fields = ["show_times","_std_bundle","_args","main","_target","output","_hxml","_build_file","_classpaths","libs","type_bundle","_update_time","mode_completion","defines","name"]
hxsublime_build_HxmlBuild._hx_props = []
hxsublime_build_HxmlBuild._hx_methods = ["std_bundle","target","classpaths","hxml","title","setHxml","build_file","add_define","set_main","get_name","set_std_bundle","args","equals","merge","copy","add_arg","get_build_folder","set_build_cwd","align_drive_letter","add_classpath","add_lib","get_classpath_of_file","is_file_in_classpath","get_relative_path","target_to_string","to_string","make_hxml","set_cwd","set_times","set_server_mode","get_command_args","set_auto_completion","_update_types","_should_refresh_types","get_types","prepare_check_cmd","absolute_output","prepare_run_cmd","prepare_build_cmd","_prepare_run","_get_run_exec","escape_cmd","_run_async","_run_sync","_on_run_complete","_run_neko_x","run","is_type_available","is_pack_available"]
hxsublime_build_HxmlBuild._hx_statics = ["__meta__"]
hxsublime_build_HxmlBuild._hx_interfaces = []

# print hxsublime.build.NmeBuild.NmeBuild
class hxsublime_build_NmeBuild:


	def __init__(self,project,title,nmml,target,cb = None):
		if cb is None:
			cb = None
		
		self._title = title
		self._target = target
		self.nmml = nmml
		self._hxml_build = cb
		self.project = project
	
	# var _title
	# var _target
	# var _hxml_build
	# var nmml
	# var project
	def setHxml(self,hxml):
		self.hxml_build().setHxml(hxml)

	def make_hxml(self):
		return self.hxml_build().make_hxml()

	def title(self):
		return self._title

	def build_file(self):
		return self.nmml

	def target(self):
		return self._target

	def plattform(self):
		return self._target.plattform

	def _get_hxml_build_with_nme_display(self):
		view = sublime_Sublime.active_window().active_view()
		display_cmd = None
		_this = self.get_build_command(self.project, view)
		display_cmd = __builtin__.list(_this)
		
		display_cmd.append("display")
		__builtin__.len(display_cmd)
		
		return hxsublime_build_Tools.create_haxe_build_from_nmml(self.project, self._target, self.nmml, display_cmd)
	

	def hxml_build(self):
		haxe_Log.trace("create hxml build", _Hx_AnonObject(fileName = "NmeBuild.hx" ,lineNumber = 81 ,className = "hxsublime.build.NmeBuild" ,methodName = "hxml_build" ))
		if self._hxml_build is None:
			self._hxml_build = self._get_hxml_build_with_nme_display()
		
		return self._hxml_build
	

	def to_string(self):
		title = self.title()
		target = self.target().name
		return "" + title + " (NME - " + target + ")"
	

	def set_std_bundle(self,std_bundle):
		self.hxml_build().set_std_bundle(std_bundle)

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
	

	def get_types(self):
		bundle = self.hxml_build().get_types()
		return bundle
	

	def std_bundle(self):
		return self.hxml_build().std_bundle()

	def add_arg(self,arg):
		self.hxml_build().add_arg(arg)

	def copy(self):
		hxml_copy = None
		if self._hxml_build is not None:
			hxml_copy = self.hxml_build().copy()
		else:
			hxml_copy = None
		return hxsublime_build_NmeBuild(self.project, self.title(), self.nmml, self._target, hxml_copy)
	

	def get_relative_path(self,file):
		return self.hxml_build().get_relative_path(file)

	def get_build_folder(self):
		r = None
		if self.nmml is not None:
			r = python_lib_os_Path.dirname(self.nmml)
		
		haxe_Log.trace("build_folder: " + Std.string(r), _Hx_AnonObject(fileName = "NmeBuild.hx" ,lineNumber = 150 ,className = "hxsublime.build.NmeBuild" ,methodName = "get_build_folder" ))
		haxe_Log.trace("nmml: " + Std.string(self.nmml), _Hx_AnonObject(fileName = "NmeBuild.hx" ,lineNumber = 151 ,className = "hxsublime.build.NmeBuild" ,methodName = "get_build_folder" ))
		return r
	

	def set_auto_completion(self,display,macro_completion = False,no_output = True):
		if macro_completion is None:
			macro_completion = False
		
		if no_output is None:
			no_output = True
		
		self.hxml_build().set_auto_completion(display, macro_completion, no_output)
	

	def set_times(self):
		self.hxml_build().set_times()

	def add_define(self,define):
		self.hxml_build().add_define(define)

	def add_classpath(self,cp):
		self.hxml_build().add_classpath(cp)

	def run(self,project,view,async,on_result,server_mode = None):
		if server_mode is None:
			server_mode = None
		
		self.hxml_build().run(project, view, async, on_result, server_mode)
	

	def _get_run_exec(self,project,view):
		return project.nme_exec(view)

	def get_build_command(self,project,view):
		_this = self._get_run_exec(project, view)
		return __builtin__.list(_this)
	

	def escape_cmd(self,cmd):
		return self.hxml_build().escape_cmd(cmd)

	def prepare_check_cmd(self,project,server_mode,view):
		r = self.prepare_build_cmd(project, server_mode, view)
		cmd = r[0]
		folder = r[1]
		cmd.append("--no-output")
		__builtin__.len(cmd)
		
		return (cmd, folder)
	

	def prepare_build_cmd(self,project,server_mode,view):
		return self._prepare_cmd(project, server_mode, view, "build")

	def prepare_run_cmd(self,project,server_mode,view):
		return self._prepare_cmd(project, server_mode, view, "test")

	def _prepare_cmd(self,project,server_mode,view,command):
		cmd = self.get_build_command(project, view)
		cmd.append(command)
		__builtin__.len(cmd)
		
		x = self.build_file()
		cmd.append(x)
		__builtin__.len(cmd)
		
		
		cmd.append(self.target().plattform)
		__builtin__.len(cmd)
		
		cmd.extend(self.target().args)
		if server_mode:
			x = ["--connect", Std.string(project.server.get_server_port())]
			cmd.extend(x)
		
		
		b = self.get_build_folder()
		return (cmd, b)
		
	

	def _prepare_run(self,project,view,server_mode):
		return self.hxml_build()._prepare_run(project, view, server_mode)

	def classpaths(self):
		return self.hxml_build().classpaths()

	def args(self):
		return self.hxml_build().args()

	def is_type_available(self,type):
		pack = type.toplevel_pack()
		return pack is None or self.is_pack_available(pack)
	

	def is_pack_available(self,pack):
		if pack == "":
			return True
		
		pack1 = pack.split(".")[0]
		target = self.hxml_build().target
		tp = __builtin__.list(hxsublime_Config.target_packages)
		tp.extend(["native", "browser", "nme"])
		no_target_pack = not Lambda.has(tp, pack1)
		is_nme_pack = pack1 == "nme"
		available = target is None or no_target_pack or is_nme_pack
		return available
	





hxsublime_build_NmeBuild.__meta__ = _Hx_AnonObject(fields = _Hx_AnonObject(title = _Hx_AnonObject(property = None ) ,build_file = _Hx_AnonObject(property = None ) ,target = _Hx_AnonObject(property = None ) ,plattform = _Hx_AnonObject(property = None ) ,hxml_build = _Hx_AnonObject(property = None ) ,std_bundle = _Hx_AnonObject(property = None ) ,classpaths = _Hx_AnonObject(property = None ) ,args = _Hx_AnonObject(property = None ) ) )


hxsublime_build_NmeBuild._hx_class = hxsublime_build_NmeBuild
hxsublime_build_NmeBuild._hx_class_name = "hxsublime.build.NmeBuild"
_hx_classes['hxsublime.build.NmeBuild'] = hxsublime_build_NmeBuild
hxsublime_build_NmeBuild._hx_fields = ["_title","_target","_hxml_build","nmml","project"]
hxsublime_build_NmeBuild._hx_props = []
hxsublime_build_NmeBuild._hx_methods = ["setHxml","make_hxml","title","build_file","target","plattform","_get_hxml_build_with_nme_display","hxml_build","to_string","set_std_bundle","_filter_platform_specific","get_types","std_bundle","add_arg","copy","get_relative_path","get_build_folder","set_auto_completion","set_times","add_define","add_classpath","run","_get_run_exec","get_build_command","escape_cmd","prepare_check_cmd","prepare_build_cmd","prepare_run_cmd","_prepare_cmd","_prepare_run","classpaths","args","is_type_available","is_pack_available"]
hxsublime_build_NmeBuild._hx_statics = ["__meta__"]
hxsublime_build_NmeBuild._hx_interfaces = []

# print hxsublime.build.OpenFlBuild.OpenFlBuild
class hxsublime_build_OpenFlBuild(hxsublime_build_NmeBuild):


	def __init__(self,project,title,openfl_xml,target,cb = None):
		if cb is None:
			cb = None
		
		super().__init__(project, title, openfl_xml, target, cb)
	
	def copy(self):
		hxml_copy = None
		if self._hxml_build is not None:
			hxml_copy = self.hxml_build().copy()
		else:
			hxml_copy = None
		r = hxsublime_build_OpenFlBuild(self.project, self.title(), self.nmml, self.target(), hxml_copy)
		return r
	

	def _get_run_exec(self,project,view):
		return project.openfl_exec(view)

	def filter_platform_specific(self,packs_or_classes):
		res = []
		_g = 0
		while _g < len(packs_or_classes):
			c = packs_or_classes[_g]
			_g = _g + 1
			if not hxsublime_tools_StringTools.startsWithAny(c, ["native", "browser", "nme"]):
				res.append(c)
				__builtin__.len(res)
			
			
		
		
		return res
	

	def to_string(self):
		out = self.title()
		target = self.target().name
		return "" + out + " (OpenFL - " + target + ")"
	

	def is_type_available(self,type):
		pack = type.toplevel_pack()
		return pack is None or self.is_pack_available(pack)
	

	def is_pack_available(self,pack):
		if pack == "":
			return True
		
		pack1 = pack.split(".")[0]
		target = self.hxml_build().target
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
hxsublime_build_OpenFlBuild._hx_methods = ["copy","_get_run_exec","filter_platform_specific","to_string","is_type_available","is_pack_available"]
hxsublime_build_OpenFlBuild._hx_statics = []
hxsublime_build_OpenFlBuild._hx_interfaces = []
hxsublime_build_OpenFlBuild._hx_super = hxsublime_build_NmeBuild

# print hxsublime.build.Tools.Tools
class hxsublime_build_Tools:

	pass




hxsublime_build_Tools._extract_tag = python_lib_Re.compile("<([a-z0-9_-]+).*?\\s(name|main|title|file)=\"([ a-z0-9_./-]+)\"", python_lib_Re.I)
def Tools_statics__hxml_buffer_to_builds(project,hxml_buffer,folder,build_path,build_file = None,hxml = None):
	if build_file is None:
		build_file = None
	
	if hxml is None:
		hxml = None
	
	builds = []
	current_build = hxsublime_build_HxmlBuild(hxml, build_file)
	f = hxml_buffer
	while True:
		l = f.readline()
		if l == "":
			break
		
		if l == "\n":
			continue
		
		l = l.strip(None)
		if StringTools.startsWith(l, "#build-name="):
			current_build.name = python_Tools.substr(l, 12, None)
			continue
		
		
		if StringTools.startsWith(l, "#"):
			continue
		
		if StringTools.startsWith(l, "--next"):
			if __builtin__.len(current_build._classpaths) == 0:
				haxe_Log.trace("no classpaths", _Hx_AnonObject(fileName = "Tools.hx" ,lineNumber = 71 ,className = "hxsublime.build.Tools" ,methodName = "_hxml_buffer_to_builds" ))
				current_build.add_classpath(build_path)
			
			
			builds.append(current_build)
			__builtin__.len(builds)
			
			current_build = hxsublime_build_HxmlBuild(hxml, build_file)
			continue
		
		
		if StringTools.endsWith(l, ".hxml"):
			haxe_Log.trace("found ref of hxml file:" + l, _Hx_AnonObject(fileName = "Tools.hx" ,lineNumber = 83 ,className = "hxsublime.build.Tools" ,methodName = "_hxml_buffer_to_builds" ))
			path = python_lib_os_Path.dirname(hxml)
			sub_builds = hxsublime_build_Tools._hxml_to_builds(project, path + python_lib_Os.sep + l, folder)
			if __builtin__.len(sub_builds) == 1:
				b = sub_builds[0]
				current_build.merge(b)
			
			
		
		
		if StringTools.startsWith(l, "-main"):
			spl = l.split(" ")
			if __builtin__.len(spl) == 2:
				current_build.main = spl[1]
			else:
				sublime_Sublime.status_message("Invalid build.hxml : no Main class")
		
		
		if StringTools.startsWith(l, "-lib"):
			spl = l.split(" ")
			if __builtin__.len(spl) == 2:
				lib = project.haxelib_manager().get(spl[1])
				if lib is not None:
					current_build.add_lib(lib)
				else:
					current_build.add_arg(("-lib", spl[1]))
					hxsublime_panel_Base_Panels.default_panel().writeln("Error: haxelib library " + Std.string(spl[1]) + " is not installed")
				
			
			else:
				sublime_Sublime.status_message("Invalid build.hxml : lib not found")
		
		
		if StringTools.startsWith(l, "-cmd"):
			spl = l.split(" ")
			def _hx_local_0():
				b = None
				_this = spl[1:None]
				b = " ".join(_this)
				
				return ("-cmd", b)
			
			current_build.add_arg(_hx_local_0())
		
		
		if StringTools.startsWith(l, "--macro"):
			spl = l.split(" ")
			def _hx_local_1():
				b = None
				_this = spl[1:None]
				b = " ".join(_this)
				
				return ("--macro", b)
			
			current_build.add_arg(_hx_local_1())
		
		
		if StringTools.startsWith(l, "-D"):
			x = l.split(" ")
			tup = (x[0], x[1])
			current_build.add_arg(tup)
			current_build.add_define(tup[1])
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
				current_build.add_arg((x[0], p2))
				break
			
			
		
		
		_g = 0
		_g1 = ["resource", "xml", "x", "swf-lib", "java-lib"]
		while _g < len(_g1):
			flag = _g1[_g]
			_g = _g + 1
			if StringTools.startsWith(l, "-" + flag):
				spl = l.split(" ")
				def _hx_local_2():
					_this = spl[1:None]
					return " ".join(_this)
				
				outp = python_lib_os_Path.join(folder, _hx_local_2())
				current_build.add_arg(("-" + flag, outp))
				if flag == "x":
					current_build._target = "neko"
				
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
				current_build.add_arg(("-" + flag, outp))
				current_build._target = flag
				current_build.output = outp
				break
			
			
		
		
		if StringTools.startsWith(l, "-cp "):
			cp = l.split(" ")
			cp.pop(0)
			classpath = " ".join(cp)
			abs_classpath = hxsublime_tools_PathTools.joinNorm(build_path, classpath)
			current_build.add_classpath(abs_classpath)
		
		
	
	if __builtin__.len(current_build._classpaths) == 0:
		current_build.add_classpath(build_path)
	
	builds.append(current_build)
	__builtin__.len(builds)
	
	return builds
	
hxsublime_build_Tools._hxml_buffer_to_builds = Tools_statics__hxml_buffer_to_builds
def Tools_statics__find_build_files_in_folder(folder,extension):
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
		def _hx_local_1(f):
			def _hx_local_2(x1):
				return (x1, f[0])
			return _hx_local_2
		
		x = __builtin__.list(__builtin__.map((_hx_local_1)(f), _this))
		
		files.extend(x)
	
	
	return files
	
hxsublime_build_Tools._find_build_files_in_folder = Tools_statics__find_build_files_in_folder
def Tools_statics__hxml_to_builds(project,hxml,folder):
	build_path = python_lib_os_Path.dirname(hxml)
	hxml_buffer = python_lib_Codecs.open(hxml, "r+", "utf-8", "ignore")
	def _hx_local_1():
		def _hx_local_0():
			return hxml_buffer.readline()
		return hxsublime_build_Tools._hxml_buffer_to_builds(project, _Hx_AnonObject(readline = _hx_local_0 ), folder, build_path, hxml, hxml)
	
	return _hx_local_1()
	
hxsublime_build_Tools._hxml_to_builds = Tools_statics__hxml_to_builds
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
def Tools_statics_create_haxe_build_from_nmml(project,target,nmml,display_cmd):
	cmd = __builtin__.list(display_cmd)
	cmd.append(nmml)
	__builtin__.len(cmd)
	
	cmd.append(target.plattform)
	__builtin__.len(cmd)
	
	cmd.extend(target.args)
	nmml_dir = python_lib_os_Path.dirname(nmml)
	r = hxsublime_Execute.run_cmd(cmd, None, nmml_dir)
	out = r[0]
	err = r[1]
	io = python_lib_io_StringIO(out)
	def _hx_local_1():
		def _hx_local_0():
			return io.readline()
		return hxsublime_build_Tools._hxml_buffer_to_builds(project, _Hx_AnonObject(readline = _hx_local_0 ), nmml_dir, nmml_dir, nmml, None)[0]
	
	return _hx_local_1()
	
hxsublime_build_Tools.create_haxe_build_from_nmml = Tools_statics_create_haxe_build_from_nmml
def Tools_statics_find_hxml_projects(project,folder):
	builds = []
	found = hxsublime_build_Tools._find_build_files_in_folder(folder, "hxml")
	_g = 0
	while _g < len(found):
		build = found[_g]
		_g = _g + 1
		hxml_file = build[0]
		hxml_folder = build[1]
		b = hxsublime_build_Tools._hxml_to_builds(project, hxml_file, hxml_folder)
		builds.extend(b)
	
	
	return builds
	
hxsublime_build_Tools.find_hxml_projects = Tools_statics_find_hxml_projects
def Tools_statics_find_nme_projects(project,folder):
	found = hxsublime_build_Tools._find_build_files_in_folder(folder, "nmml")
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
	
hxsublime_build_Tools.find_nme_projects = Tools_statics_find_nme_projects
def Tools_statics_find_openfl_projects(project,folder):
	found = hxsublime_build_Tools._find_build_files_in_folder(folder, "xml")
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
	
hxsublime_build_Tools.find_openfl_projects = Tools_statics_find_openfl_projects


hxsublime_build_Tools._hx_class = hxsublime_build_Tools
hxsublime_build_Tools._hx_class_name = "hxsublime.build.Tools"
_hx_classes['hxsublime.build.Tools'] = hxsublime_build_Tools
hxsublime_build_Tools._hx_fields = []
hxsublime_build_Tools._hx_props = []
hxsublime_build_Tools._hx_methods = []
hxsublime_build_Tools._hx_statics = ["_extract_tag","_hxml_buffer_to_builds","_find_build_files_in_folder","_hxml_to_builds","_find_nme_project_title","create_haxe_build_from_nmml","find_hxml_projects","find_nme_projects","find_openfl_projects"]
hxsublime_build_Tools._hx_interfaces = []

# print sublime.Command.Command
from sublime_plugin import Command as sublime_Command
# print sublime.TextCommand.TextCommand
from sublime_plugin import TextCommand as sublime_TextCommand
# print hxsublime.commands.Build.HaxeSaveAllAndRunCommand
class hxsublime_commands_Build_HaxeSaveAllAndRunCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**args):
		if args is None:
			args = None
		
		haxe_Log.trace("run HaxeSaveAllAndRunCommand", _Hx_AnonObject(fileName = "Build.hx" ,lineNumber = 20 ,className = "hxsublime.commands.HaxeSaveAllAndRunCommand" ,methodName = "run" ))
		view = self.view
		view.window().run_command("save_all")
		hxsublime_project_Base_Projects.current_project(self.view).run_build(view)
	







hxsublime_commands_Build_HaxeSaveAllAndRunCommand._hx_class = hxsublime_commands_Build_HaxeSaveAllAndRunCommand
hxsublime_commands_Build_HaxeSaveAllAndRunCommand._hx_class_name = "hxsublime.commands.HaxeSaveAllAndRunCommand"
_hx_classes['hxsublime.commands.HaxeSaveAllAndRunCommand'] = hxsublime_commands_Build_HaxeSaveAllAndRunCommand
hxsublime_commands_Build_HaxeSaveAllAndRunCommand._hx_fields = []
hxsublime_commands_Build_HaxeSaveAllAndRunCommand._hx_props = []
hxsublime_commands_Build_HaxeSaveAllAndRunCommand._hx_methods = ["run"]
hxsublime_commands_Build_HaxeSaveAllAndRunCommand._hx_statics = []
hxsublime_commands_Build_HaxeSaveAllAndRunCommand._hx_interfaces = []
hxsublime_commands_Build_HaxeSaveAllAndRunCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.Build.HaxeSaveAllAndCheckCommand
class hxsublime_commands_Build_HaxeSaveAllAndCheckCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**args):
		if args is None:
			args = None
		
		edit1 = python_lib_Types_KwArgs_Impl_.get(args, "edit", None)
		haxe_Log.trace("run HaxeSaveAllAndCheckCommand", _Hx_AnonObject(fileName = "Build.hx" ,lineNumber = 32 ,className = "hxsublime.commands.HaxeSaveAllAndCheckCommand" ,methodName = "run" ))
		view = self.view
		view.window().run_command("save_all")
		hxsublime_project_Base_Projects.current_project(self.view).check_build(view)
	







hxsublime_commands_Build_HaxeSaveAllAndCheckCommand._hx_class = hxsublime_commands_Build_HaxeSaveAllAndCheckCommand
hxsublime_commands_Build_HaxeSaveAllAndCheckCommand._hx_class_name = "hxsublime.commands.HaxeSaveAllAndCheckCommand"
_hx_classes['hxsublime.commands.HaxeSaveAllAndCheckCommand'] = hxsublime_commands_Build_HaxeSaveAllAndCheckCommand
hxsublime_commands_Build_HaxeSaveAllAndCheckCommand._hx_fields = []
hxsublime_commands_Build_HaxeSaveAllAndCheckCommand._hx_props = []
hxsublime_commands_Build_HaxeSaveAllAndCheckCommand._hx_methods = ["run"]
hxsublime_commands_Build_HaxeSaveAllAndCheckCommand._hx_statics = []
hxsublime_commands_Build_HaxeSaveAllAndCheckCommand._hx_interfaces = []
hxsublime_commands_Build_HaxeSaveAllAndCheckCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.Build.HaxeSaveAllAndBuildCommand
class hxsublime_commands_Build_HaxeSaveAllAndBuildCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**args):
		if args is None:
			args = None
		
		haxe_Log.trace("run HaxeSaveAllAndBuildCommand", _Hx_AnonObject(fileName = "Build.hx" ,lineNumber = 43 ,className = "hxsublime.commands.HaxeSaveAllAndBuildCommand" ,methodName = "run" ))
		view = self.view
		view.window().run_command("save_all")
		hxsublime_project_Base_Projects.current_project(self.view).just_build(view)
	







hxsublime_commands_Build_HaxeSaveAllAndBuildCommand._hx_class = hxsublime_commands_Build_HaxeSaveAllAndBuildCommand
hxsublime_commands_Build_HaxeSaveAllAndBuildCommand._hx_class_name = "hxsublime.commands.HaxeSaveAllAndBuildCommand"
_hx_classes['hxsublime.commands.HaxeSaveAllAndBuildCommand'] = hxsublime_commands_Build_HaxeSaveAllAndBuildCommand
hxsublime_commands_Build_HaxeSaveAllAndBuildCommand._hx_fields = []
hxsublime_commands_Build_HaxeSaveAllAndBuildCommand._hx_props = []
hxsublime_commands_Build_HaxeSaveAllAndBuildCommand._hx_methods = ["run"]
hxsublime_commands_Build_HaxeSaveAllAndBuildCommand._hx_statics = []
hxsublime_commands_Build_HaxeSaveAllAndBuildCommand._hx_interfaces = []
hxsublime_commands_Build_HaxeSaveAllAndBuildCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.Build.HaxeRunBuildCommand
class hxsublime_commands_Build_HaxeRunBuildCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**args):
		if args is None:
			args = None
		
		view = self.view
		haxe_Log.trace("run HaxeRunBuildCommand", _Hx_AnonObject(fileName = "Build.hx" ,lineNumber = 55 ,className = "hxsublime.commands.HaxeRunBuildCommand" ,methodName = "run" ))
		project = hxsublime_project_Base_Projects.current_project(self.view)
		if project.has_build():
			project.run_build(view)
		else:
			haxe_Log.trace("no builds selected", _Hx_AnonObject(fileName = "Build.hx" ,lineNumber = 64 ,className = "hxsublime.commands.HaxeRunBuildCommand" ,methodName = "run" ))
			project.extract_build_args(view, True)
		
	







hxsublime_commands_Build_HaxeRunBuildCommand._hx_class = hxsublime_commands_Build_HaxeRunBuildCommand
hxsublime_commands_Build_HaxeRunBuildCommand._hx_class_name = "hxsublime.commands.HaxeRunBuildCommand"
_hx_classes['hxsublime.commands.HaxeRunBuildCommand'] = hxsublime_commands_Build_HaxeRunBuildCommand
hxsublime_commands_Build_HaxeRunBuildCommand._hx_fields = []
hxsublime_commands_Build_HaxeRunBuildCommand._hx_props = []
hxsublime_commands_Build_HaxeRunBuildCommand._hx_methods = ["run"]
hxsublime_commands_Build_HaxeRunBuildCommand._hx_statics = []
hxsublime_commands_Build_HaxeRunBuildCommand._hx_interfaces = []
hxsublime_commands_Build_HaxeRunBuildCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.Build.HaxeSelectBuildCommand
class hxsublime_commands_Build_HaxeSelectBuildCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**args):
		if args is None:
			args = None
		
		haxe_Log.trace("run HaxeSelectBuildCommand", _Hx_AnonObject(fileName = "Build.hx" ,lineNumber = 74 ,className = "hxsublime.commands.HaxeSelectBuildCommand" ,methodName = "run" ))
		view = self.view
		hxsublime_project_Base_Projects.current_project(self.view).select_build(view)
	







hxsublime_commands_Build_HaxeSelectBuildCommand._hx_class = hxsublime_commands_Build_HaxeSelectBuildCommand
hxsublime_commands_Build_HaxeSelectBuildCommand._hx_class_name = "hxsublime.commands.HaxeSelectBuildCommand"
_hx_classes['hxsublime.commands.HaxeSelectBuildCommand'] = hxsublime_commands_Build_HaxeSelectBuildCommand
hxsublime_commands_Build_HaxeSelectBuildCommand._hx_fields = []
hxsublime_commands_Build_HaxeSelectBuildCommand._hx_props = []
hxsublime_commands_Build_HaxeSelectBuildCommand._hx_methods = ["run"]
hxsublime_commands_Build_HaxeSelectBuildCommand._hx_statics = []
hxsublime_commands_Build_HaxeSelectBuildCommand._hx_interfaces = []
hxsublime_commands_Build_HaxeSelectBuildCommand._hx_super = sublime_TextCommand

# print sublime.EventListener.EventListener
from sublime_plugin import EventListener as sublime_EventListener
# print hxsublime.commands.Build.HaxeBuildOnSaveListener
class hxsublime_commands_Build_HaxeBuildOnSaveListener(sublime_EventListener):

	def on_post_save(self,view):
		haxe_Log.trace("on_post_save", _Hx_AnonObject(fileName = "Build.hx" ,lineNumber = 83 ,className = "hxsublime.commands.HaxeBuildOnSaveListener" ,methodName = "on_post_save" ))
		if view is not None and view.file_name() is not None:
			if hxsublime_tools_ViewTools.isSupported(view) or StringTools.endsWith(view.file_name(), ".erazor.html"):
				if hxsublime_Settings.check_on_save():
					project = hxsublime_project_Base_Projects.current_project(view)
					if project.has_build():
						project.check_build(view)
					
		
				
			
		
	







hxsublime_commands_Build_HaxeBuildOnSaveListener._hx_class = hxsublime_commands_Build_HaxeBuildOnSaveListener
hxsublime_commands_Build_HaxeBuildOnSaveListener._hx_class_name = "hxsublime.commands.HaxeBuildOnSaveListener"
_hx_classes['hxsublime.commands.HaxeBuildOnSaveListener'] = hxsublime_commands_Build_HaxeBuildOnSaveListener
hxsublime_commands_Build_HaxeBuildOnSaveListener._hx_fields = []
hxsublime_commands_Build_HaxeBuildOnSaveListener._hx_props = []
hxsublime_commands_Build_HaxeBuildOnSaveListener._hx_methods = ["on_post_save"]
hxsublime_commands_Build_HaxeBuildOnSaveListener._hx_statics = []
hxsublime_commands_Build_HaxeBuildOnSaveListener._hx_interfaces = []
hxsublime_commands_Build_HaxeBuildOnSaveListener._hx_super = sublime_EventListener

# print hxsublime.commands.Completion.HaxeAsyncTriggeredCompletionCommand
class hxsublime_commands_Completion_HaxeAsyncTriggeredCompletionCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**kwArgs):
		if kwArgs is None:
			kwArgs = None
		
		options = hxsublime_completion_hx_Types_CompletionOptions(3, 2, 1)
		hxsublime_completion_hx_Base.trigger_completion(self.view, options)
	







hxsublime_commands_Completion_HaxeAsyncTriggeredCompletionCommand._hx_class = hxsublime_commands_Completion_HaxeAsyncTriggeredCompletionCommand
hxsublime_commands_Completion_HaxeAsyncTriggeredCompletionCommand._hx_class_name = "hxsublime.commands.HaxeAsyncTriggeredCompletionCommand"
_hx_classes['hxsublime.commands.HaxeAsyncTriggeredCompletionCommand'] = hxsublime_commands_Completion_HaxeAsyncTriggeredCompletionCommand
hxsublime_commands_Completion_HaxeAsyncTriggeredCompletionCommand._hx_fields = []
hxsublime_commands_Completion_HaxeAsyncTriggeredCompletionCommand._hx_props = []
hxsublime_commands_Completion_HaxeAsyncTriggeredCompletionCommand._hx_methods = ["run"]
hxsublime_commands_Completion_HaxeAsyncTriggeredCompletionCommand._hx_statics = []
hxsublime_commands_Completion_HaxeAsyncTriggeredCompletionCommand._hx_interfaces = []
hxsublime_commands_Completion_HaxeAsyncTriggeredCompletionCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.Completion.HaxeDisplayCompletionCommand
class hxsublime_commands_Completion_HaxeDisplayCompletionCommand(sublime_TextCommand):


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
						d = python_lib_Types_Dict()
						_g = 0
						_g1 = Reflect.fields(x)
						while _g < len(_g1):
							f = _g1[_g]
							_g = _g + 1
							val = None
							v = None
							try:
								v = __builtin__.getattr(x, f)
							except Exception as _hx_e:
								_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
								if True:
									e = _hx_e1
									None
								else:
									raise _hx_e
							val = v
							
							python_lib_Types_DictImpl.set(d, f, val)
							
						
						
						return d
					
					return _hx_local_1()
				
				return _hx_local_2()
			
			self.view.run_command("insert", _hx_local_0())
		
		
		haxe_Log.trace("RUN - HaxeDisplayCompletionCommand", _Hx_AnonObject(fileName = "Completion.hx" ,lineNumber = 41 ,className = "hxsublime.commands.HaxeDisplayCompletionCommand" ,methodName = "run" ))
		if hxsublime_commands_Completion_Helper.is_valid_completion(self.view, edit, input_char):
			options = hxsublime_completion_hx_Types_CompletionOptions(1, 2, 1)
			hxsublime_completion_hx_Base.trigger_completion(self.view, options)
		
		
	







hxsublime_commands_Completion_HaxeDisplayCompletionCommand._hx_class = hxsublime_commands_Completion_HaxeDisplayCompletionCommand
hxsublime_commands_Completion_HaxeDisplayCompletionCommand._hx_class_name = "hxsublime.commands.HaxeDisplayCompletionCommand"
_hx_classes['hxsublime.commands.HaxeDisplayCompletionCommand'] = hxsublime_commands_Completion_HaxeDisplayCompletionCommand
hxsublime_commands_Completion_HaxeDisplayCompletionCommand._hx_fields = []
hxsublime_commands_Completion_HaxeDisplayCompletionCommand._hx_props = []
hxsublime_commands_Completion_HaxeDisplayCompletionCommand._hx_methods = ["run"]
hxsublime_commands_Completion_HaxeDisplayCompletionCommand._hx_statics = []
hxsublime_commands_Completion_HaxeDisplayCompletionCommand._hx_interfaces = []
hxsublime_commands_Completion_HaxeDisplayCompletionCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.Completion.HaxeDisplayMacroCompletionCommand
class hxsublime_commands_Completion_HaxeDisplayMacroCompletionCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**kwArgs):
		if kwArgs is None:
			kwArgs = None
		
		haxe_Log.trace("RUN - HaxeDisplayMacroCompletionCommand", _Hx_AnonObject(fileName = "Completion.hx" ,lineNumber = 57 ,className = "hxsublime.commands.HaxeDisplayMacroCompletionCommand" ,methodName = "run" ))
		options = hxsublime_completion_hx_Types_CompletionOptions(1, 2, 1)
		hxsublime_completion_hx_Base.trigger_completion(self.view, options)
	







hxsublime_commands_Completion_HaxeDisplayMacroCompletionCommand._hx_class = hxsublime_commands_Completion_HaxeDisplayMacroCompletionCommand
hxsublime_commands_Completion_HaxeDisplayMacroCompletionCommand._hx_class_name = "hxsublime.commands.HaxeDisplayMacroCompletionCommand"
_hx_classes['hxsublime.commands.HaxeDisplayMacroCompletionCommand'] = hxsublime_commands_Completion_HaxeDisplayMacroCompletionCommand
hxsublime_commands_Completion_HaxeDisplayMacroCompletionCommand._hx_fields = []
hxsublime_commands_Completion_HaxeDisplayMacroCompletionCommand._hx_props = []
hxsublime_commands_Completion_HaxeDisplayMacroCompletionCommand._hx_methods = ["run"]
hxsublime_commands_Completion_HaxeDisplayMacroCompletionCommand._hx_statics = []
hxsublime_commands_Completion_HaxeDisplayMacroCompletionCommand._hx_interfaces = []
hxsublime_commands_Completion_HaxeDisplayMacroCompletionCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.Completion.HaxeHintDisplayCompletionCommand
class hxsublime_commands_Completion_HaxeHintDisplayCompletionCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**kwArgs):
		if kwArgs is None:
			kwArgs = None
		
		haxe_Log.trace("RUN - HaxeHintDisplayCompletionCommand", _Hx_AnonObject(fileName = "Completion.hx" ,lineNumber = 72 ,className = "hxsublime.commands.HaxeHintDisplayCompletionCommand" ,methodName = "run" ))
		options = hxsublime_completion_hx_Types_CompletionOptions(1, 2, 2)
		hxsublime_completion_hx_Base.trigger_completion(self.view, options)
	







hxsublime_commands_Completion_HaxeHintDisplayCompletionCommand._hx_class = hxsublime_commands_Completion_HaxeHintDisplayCompletionCommand
hxsublime_commands_Completion_HaxeHintDisplayCompletionCommand._hx_class_name = "hxsublime.commands.HaxeHintDisplayCompletionCommand"
_hx_classes['hxsublime.commands.HaxeHintDisplayCompletionCommand'] = hxsublime_commands_Completion_HaxeHintDisplayCompletionCommand
hxsublime_commands_Completion_HaxeHintDisplayCompletionCommand._hx_fields = []
hxsublime_commands_Completion_HaxeHintDisplayCompletionCommand._hx_props = []
hxsublime_commands_Completion_HaxeHintDisplayCompletionCommand._hx_methods = ["run"]
hxsublime_commands_Completion_HaxeHintDisplayCompletionCommand._hx_statics = []
hxsublime_commands_Completion_HaxeHintDisplayCompletionCommand._hx_interfaces = []
hxsublime_commands_Completion_HaxeHintDisplayCompletionCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.Completion.HaxeMacroHintDisplayCompletionCommand
class hxsublime_commands_Completion_HaxeMacroHintDisplayCompletionCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**kwArgs):
		if kwArgs is None:
			kwArgs = None
		
		haxe_Log.trace("RUN - HaxeMacroHintDisplayCompletionCommand", _Hx_AnonObject(fileName = "Completion.hx" ,lineNumber = 87 ,className = "hxsublime.commands.HaxeMacroHintDisplayCompletionCommand" ,methodName = "run" ))
		options = hxsublime_completion_hx_Types_CompletionOptions(1, 1, 2)
		hxsublime_completion_hx_Base.trigger_completion(self.view, options)
	







hxsublime_commands_Completion_HaxeMacroHintDisplayCompletionCommand._hx_class = hxsublime_commands_Completion_HaxeMacroHintDisplayCompletionCommand
hxsublime_commands_Completion_HaxeMacroHintDisplayCompletionCommand._hx_class_name = "hxsublime.commands.HaxeMacroHintDisplayCompletionCommand"
_hx_classes['hxsublime.commands.HaxeMacroHintDisplayCompletionCommand'] = hxsublime_commands_Completion_HaxeMacroHintDisplayCompletionCommand
hxsublime_commands_Completion_HaxeMacroHintDisplayCompletionCommand._hx_fields = []
hxsublime_commands_Completion_HaxeMacroHintDisplayCompletionCommand._hx_props = []
hxsublime_commands_Completion_HaxeMacroHintDisplayCompletionCommand._hx_methods = ["run"]
hxsublime_commands_Completion_HaxeMacroHintDisplayCompletionCommand._hx_statics = []
hxsublime_commands_Completion_HaxeMacroHintDisplayCompletionCommand._hx_interfaces = []
hxsublime_commands_Completion_HaxeMacroHintDisplayCompletionCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.Completion.Helper
class hxsublime_commands_Completion_Helper:

	pass




def Helper_statics_is_valid_completion(view,edit,input_char):
	valid = True
	if input_char == "(":
		src = hxsublime_tools_ViewTools.getContentUntilFirstCursor(view)
		if hxsublime_commands_Completion_Helper.is_open_parenthesis_after_function_definition(src):
			haxe_Log.trace("Invalid Completion is open par after function", _Hx_AnonObject(fileName = "Completion.hx" ,lineNumber = 110 ,className = "hxsublime.commands.Helper" ,methodName = "is_valid_completion" ))
			valid = False
		
		
	
	
	if input_char == ",":
		src = hxsublime_tools_ViewTools.getContentUntilFirstCursor(view)
		if hxsublime_commands_Completion_Helper.is_comma_after_open_parenthesis_of_function_definition(src):
			haxe_Log.trace("Invalid Completion is open par after function", _Hx_AnonObject(fileName = "Completion.hx" ,lineNumber = 120 ,className = "hxsublime.commands.Helper" ,methodName = "is_valid_completion" ))
			valid = False
		
		
	
	
	return valid
	
hxsublime_commands_Completion_Helper.is_valid_completion = Helper_statics_is_valid_completion
hxsublime_commands_Completion_Helper.anon_func = python_lib_Re.compile("^function(\\s+[a-zA-Z0-9$_]*\\s+)?\\s*\\($")
def Helper_statics_is_open_parenthesis_after_function_definition(src):
	last_function = src.rfind("function", None)
	src_part = python_Tools.substr(src, last_function, None)
	match = python_lib_Re.match(hxsublime_commands_Completion_Helper.anon_func, src_part)
	haxe_Log.trace(Std.string(match), _Hx_AnonObject(fileName = "Completion.hx" ,lineNumber = 136 ,className = "hxsublime.commands.Helper" ,methodName = "is_open_parenthesis_after_function_definition" ))
	haxe_Log.trace(src_part, _Hx_AnonObject(fileName = "Completion.hx" ,lineNumber = 137 ,className = "hxsublime.commands.Helper" ,methodName = "is_open_parenthesis_after_function_definition" ))
	return match is not None
	
hxsublime_commands_Completion_Helper.is_open_parenthesis_after_function_definition = Helper_statics_is_open_parenthesis_after_function_definition
def Helper_statics_is_comma_after_open_parenthesis_of_function_definition(src):
	haxe_Log.trace("src_full:" + src, _Hx_AnonObject(fileName = "Completion.hx" ,lineNumber = 144 ,className = "hxsublime.commands.Helper" ,methodName = "is_comma_after_open_parenthesis_of_function_definition" ))
	found = hxsublime_tools_HxSrcTools.reverse_search_next_char_on_same_nesting_level(src, ["("], __builtin__.len(src) - 1)
	haxe_Log.trace("match:" + Std.string(found), _Hx_AnonObject(fileName = "Completion.hx" ,lineNumber = 148 ,className = "hxsublime.commands.Helper" ,methodName = "is_comma_after_open_parenthesis_of_function_definition" ))
	res = False
	if found is not None:
		src_until_comma = None
		endIndex = found[0] + 1
		src_until_comma = python_Tools.substring(src, 0, endIndex)
		
		haxe_Log.trace("src_until_comma: " + src_until_comma, _Hx_AnonObject(fileName = "Completion.hx" ,lineNumber = 154 ,className = "hxsublime.commands.Helper" ,methodName = "is_comma_after_open_parenthesis_of_function_definition" ))
		res = hxsublime_commands_Completion_Helper.is_open_parenthesis_after_function_definition(src_until_comma)
	
	
	return res
	
hxsublime_commands_Completion_Helper.is_comma_after_open_parenthesis_of_function_definition = Helper_statics_is_comma_after_open_parenthesis_of_function_definition


hxsublime_commands_Completion_Helper._hx_class = hxsublime_commands_Completion_Helper
hxsublime_commands_Completion_Helper._hx_class_name = "hxsublime.commands.Helper"
_hx_classes['hxsublime.commands.Helper'] = hxsublime_commands_Completion_Helper
hxsublime_commands_Completion_Helper._hx_fields = []
hxsublime_commands_Completion_Helper._hx_props = []
hxsublime_commands_Completion_Helper._hx_methods = []
hxsublime_commands_Completion_Helper._hx_statics = ["is_valid_completion","anon_func","is_open_parenthesis_after_function_definition","is_comma_after_open_parenthesis_of_function_definition"]
hxsublime_commands_Completion_Helper._hx_interfaces = []

# print sublime.WindowCommand.WindowCommand
from sublime_plugin import WindowCommand as sublime_WindowCommand
# print hxsublime.commands.CompletionServer.HaxeRestartServerCommand
class hxsublime_commands_CompletionServer_HaxeRestartServerCommand(sublime_WindowCommand):


	def __init__(self,w):
		super().__init__(w)
	def run(self,**kwArgs):
		haxe_Log.trace("run HaxeRestartServerCommand", _Hx_AnonObject(fileName = "CompletionServer.hx" ,lineNumber = 14 ,className = "hxsublime.commands.HaxeRestartServerCommand" ,methodName = "run" ))
		view = sublime_Sublime.active_window().active_view()
		project = hxsublime_project_Base_Projects.current_project(view)
		project.restart_server(view)
	







hxsublime_commands_CompletionServer_HaxeRestartServerCommand._hx_class = hxsublime_commands_CompletionServer_HaxeRestartServerCommand
hxsublime_commands_CompletionServer_HaxeRestartServerCommand._hx_class_name = "hxsublime.commands.HaxeRestartServerCommand"
_hx_classes['hxsublime.commands.HaxeRestartServerCommand'] = hxsublime_commands_CompletionServer_HaxeRestartServerCommand
hxsublime_commands_CompletionServer_HaxeRestartServerCommand._hx_fields = []
hxsublime_commands_CompletionServer_HaxeRestartServerCommand._hx_props = []
hxsublime_commands_CompletionServer_HaxeRestartServerCommand._hx_methods = ["run"]
hxsublime_commands_CompletionServer_HaxeRestartServerCommand._hx_statics = []
hxsublime_commands_CompletionServer_HaxeRestartServerCommand._hx_interfaces = []
hxsublime_commands_CompletionServer_HaxeRestartServerCommand._hx_super = sublime_WindowCommand

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
class hxsublime_commands_CreateType_HaxeCreateTypeCommand(sublime_WindowCommand):


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
		project = hxsublime_project_Base_Projects.current_project(view)
		builds = __builtin__.list(project.builds)
		if project.has_build():
			builds.insert(0, project.get_build(view))
		
		pack = []
		if __builtin__.len(builds) == 0 and view is not None and view.file_name() is not None:
			haxe_Log.trace(view.file_name(), _Hx_AnonObject(fileName = "CreateType.hx" ,lineNumber = 65 ,className = "hxsublime.commands.HaxeCreateTypeCommand" ,methodName = "run" ))
			project.extract_build_args(view)
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
				haxe_Log.trace("build file: " + Std.string(b.build_file), _Hx_AnonObject(fileName = "CreateType.hx" ,lineNumber = 91 ,className = "hxsublime.commands.HaxeCreateTypeCommand" ,methodName = "run" ))
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
			if hxsublime_tools_HxSrcTools_Regex.is_type.match(p) is not None:
				cl = p
				break
			
			else:
				pack.append(p)
				__builtin__.len(pack)
			
		
		if __builtin__.len(parts) > 0:
			cl = parts[0]
		
		fn = fn + ".hx"
		src = "\npackage " + ".".join(pack) + ";\n\n" + cur_type + " " + cl + " "
		if cur_type == "typedef":
			src = src + "= "
		
		src = src + "{\n\n\t\n\n}"
		hxsublime_commands_CreateType_State.current_create_type_info.set(fn, src)
		sublime_Sublime.active_window().open_file(fn)
	

	def onChange(self,inp):
		haxe_Log.trace(inp, _Hx_AnonObject(fileName = "CreateType.hx" ,lineNumber = 211 ,className = "hxsublime.commands.HaxeCreateTypeCommand" ,methodName = "onChange" ))

	def onCancel(self):
		haxe_Log.trace("cancel", _Hx_AnonObject(fileName = "CreateType.hx" ,lineNumber = 216 ,className = "hxsublime.commands.HaxeCreateTypeCommand" ,methodName = "onCancel" ))







hxsublime_commands_CreateType_HaxeCreateTypeCommand._hx_class = hxsublime_commands_CreateType_HaxeCreateTypeCommand
hxsublime_commands_CreateType_HaxeCreateTypeCommand._hx_class_name = "hxsublime.commands.HaxeCreateTypeCommand"
_hx_classes['hxsublime.commands.HaxeCreateTypeCommand'] = hxsublime_commands_CreateType_HaxeCreateTypeCommand
hxsublime_commands_CreateType_HaxeCreateTypeCommand._hx_fields = ["classpath","win"]
hxsublime_commands_CreateType_HaxeCreateTypeCommand._hx_props = []
hxsublime_commands_CreateType_HaxeCreateTypeCommand._hx_methods = ["run","onDone","onChange","onCancel"]
hxsublime_commands_CreateType_HaxeCreateTypeCommand._hx_statics = []
hxsublime_commands_CreateType_HaxeCreateTypeCommand._hx_interfaces = []
hxsublime_commands_CreateType_HaxeCreateTypeCommand._hx_super = sublime_WindowCommand

# print hxsublime.commands.CreateType.HaxeCreateTypeListener
class hxsublime_commands_CreateType_HaxeCreateTypeListener(sublime_EventListener):

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
	







hxsublime_commands_CreateType_HaxeCreateTypeListener._hx_class = hxsublime_commands_CreateType_HaxeCreateTypeListener
hxsublime_commands_CreateType_HaxeCreateTypeListener._hx_class_name = "hxsublime.commands.HaxeCreateTypeListener"
_hx_classes['hxsublime.commands.HaxeCreateTypeListener'] = hxsublime_commands_CreateType_HaxeCreateTypeListener
hxsublime_commands_CreateType_HaxeCreateTypeListener._hx_fields = []
hxsublime_commands_CreateType_HaxeCreateTypeListener._hx_props = []
hxsublime_commands_CreateType_HaxeCreateTypeListener._hx_methods = ["on_load","create_file"]
hxsublime_commands_CreateType_HaxeCreateTypeListener._hx_statics = []
hxsublime_commands_CreateType_HaxeCreateTypeListener._hx_interfaces = []
hxsublime_commands_CreateType_HaxeCreateTypeListener._hx_super = sublime_EventListener

# print hxsublime.commands.Execute.Helper
class hxsublime_commands_Execute_Helper:

	pass




def Helper_statics_escape_cmd(cmd):
	print_cmd = __builtin__.list(cmd)
	l = __builtin__.len(print_cmd)
	_g = 0
	while _g < l:
		def _hx_local_0():
			nonlocal _g
			_hx_r = _g
			_g = _g + 1
			return _hx_r
			
		
		i = _hx_local_0()
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
class hxsublime_commands_Execute_HaxeExecCommand(sublime_WindowCommand):


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
		env = python_lib_Types_KwArgs_Impl_.get(kwArgs, "env", python_lib_Types_Dict())
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
			def _hx_local_0(a):
				a1 = None
				_this = a.split("\"")
				a1 = "\\\"".join(_this)
				
				if __builtin__.len(a1) >= 2:
					if StringTools.startsWith(a1, "\\\""):
						a1 = "\"" + python_Tools.substr(a1, 2, None)
					else:
						a1 = a1
					if StringTools.endsWith(a1, "\\\""):
						def _hx_local_2():
							def _hx_local_1():
								endIndex = __builtin__.len(a1) - 2
								return python_Tools.substring(a1, 0, endIndex)
							
							return _hx_local_1() + "\""
						
						a1 = _hx_local_2()
					
					else:
						a1 = a1
				
				
				return a1
			
			escape_arg = _hx_local_0
			def _hx_local_4():
				def _hx_local_3():
					_this = __builtin__.list(__builtin__.map(escape_arg, cmd))
					return " ".join(_this)
				
				return "Running Command : " + _hx_local_3()
			
			haxe_Log.trace(_hx_local_4(), _Hx_AnonObject(fileName = "Execute.hx" ,lineNumber = 135 ,className = "hxsublime.commands.HaxeExecCommand" ,methodName = "run" ))
			sublime_Sublime.status_message("Building")
		
		
		show_panel_on_build = sublime_Sublime.load_settings("Preferences.sublime-settings").get("show_panel_on_build", True)
		if show_panel_on_build:
			def _hx_local_5():
				x = _Hx_AnonObject(panel = "output.exec" )
				def _hx_local_7():
					def _hx_local_6():
						d = python_lib_Types_Dict()
						_g = 0
						_g1 = Reflect.fields(x)
						while _g < len(_g1):
							f = _g1[_g]
							_g = _g + 1
							val = None
							v = None
							try:
								v = __builtin__.getattr(x, f)
							except Exception as _hx_e:
								_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
								if True:
									e = _hx_e1
									None
								else:
									raise _hx_e
							val = v
							
							python_lib_Types_DictImpl.set(d, f, val)
							
						
						
						return d
					
					return _hx_local_6()
				
				return _hx_local_7()
			
			self.window.run_command("show_panel", _hx_local_5())
		
		
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
			if python_lib_Types_DictImpl.hasKey(d, "working_dir"):
				python_lib_Types_DictImpl.remove(d, "working_dir")
			
			if python_lib_Types_DictImpl.hasKey(d, "file_regex"):
				python_lib_Types_DictImpl.remove(d, "file_regex")
			
			if python_lib_Types_DictImpl.hasKey(d, "line_regex"):
				python_lib_Types_DictImpl.remove(d, "line_regex")
			
			if python_lib_Types_DictImpl.hasKey(d, "encoding"):
				python_lib_Types_DictImpl.remove(d, "encoding")
			
			if python_lib_Types_DictImpl.hasKey(d, "is_check_run"):
				python_lib_Types_DictImpl.remove(d, "is_check_run")
			
			if python_lib_Types_DictImpl.hasKey(d, "env"):
				python_lib_Types_DictImpl.remove(d, "env")
			
			if python_lib_Types_DictImpl.hasKey(d, "cmd"):
				python_lib_Types_DictImpl.remove(d, "cmd")
			
			self.proc = sublime_def_exec_AsyncProcess(cmd, None, merged_env, self, **kwArgs)
			def _hx_local_10():
				def _hx_local_9():
					def _hx_local_8():
						_this = hxsublime_commands_Execute_Helper.escape_cmd(cmd)
						return " ".join(_this)
					
					return "Running Command: " + _hx_local_8()
				
				return _hx_local_9() + "\n"
			
			self.append_data(self.proc, python_lib_StringTools.encode(_hx_local_10(), "utf-8"))
		
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			if True:
				e = _hx_e1
				self.append_data_str(None, Std.string(e) + "\n")
				self.append_data_str(None, "[cmd:  " + Std.string(cmd) + "]\n")
				self.append_data_str(None, "[dir:  " + python_lib_Os.getcwdb().decode("utf-8") + "]\n")
				if python_lib_Types_DictImpl.hasKey(merged_env, "PATH"):
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
				self.append_data_str(proc, "[Finished in " + Std.string(elapsed) + " with exit code " + exit_code + "]")
		
		
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
	







hxsublime_commands_Execute_HaxeExecCommand._hx_class = hxsublime_commands_Execute_HaxeExecCommand
hxsublime_commands_Execute_HaxeExecCommand._hx_class_name = "hxsublime.commands.HaxeExecCommand"
_hx_classes['hxsublime.commands.HaxeExecCommand'] = hxsublime_commands_Execute_HaxeExecCommand
hxsublime_commands_Execute_HaxeExecCommand._hx_fields = ["is_check_run","output_view","proc","encoding","quiet"]
hxsublime_commands_Execute_HaxeExecCommand._hx_props = []
hxsublime_commands_Execute_HaxeExecCommand._hx_methods = ["run","is_enabled","append_data_str","append_data","finish","on_data","on_finished"]
hxsublime_commands_Execute_HaxeExecCommand._hx_statics = []
hxsublime_commands_Execute_HaxeExecCommand._hx_interfaces = [sublime_def_exec_ProcessListener]
hxsublime_commands_Execute_HaxeExecCommand._hx_super = sublime_WindowCommand

# print hxsublime.commands.FindDeclaration.HaxeFindDeclarationCommand
class hxsublime_commands_FindDeclaration_HaxeFindDeclarationCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**_):
		if _ is None:
			_ = None
		
		self.run1(True)
	

	def helper_method(self):
		return "hxsublime.FindDeclaration.__sublimeFindDecl"

	def run1(self,use_display,order = 1):
		if order is None:
			order = 1
		
		_g = self
		haxe_Log.trace("run HaxeFindDeclarationCommand", _Hx_AnonObject(fileName = "FindDeclaration.hx" ,lineNumber = 44 ,className = "hxsublime.commands.HaxeFindDeclarationCommand" ,methodName = "run1" ))
		view = self.view
		file_name = view.file_name()
		if file_name is None:
			return
		
		project = hxsublime_project_Base_Projects.current_project(view)
		if not project.has_build():
			project.extract_build_args(view, False)
		
		if not project.has_build():
			project.extract_build_args(view, True)
			return
		
		
		helper_method = self.helper_method()
		src = hxsublime_tools_ViewTools.getContent(view)
		file_name1 = python_lib_os_Path.basename(view.file_name())
		package_match = python_lib_Re.match(hxsublime_tools_HxSrcTools_Regex.package_line, src)
		using_pos = None
		if package_match is None:
			using_pos = 0
		else:
			using_pos = package_match.end(0)
		using_insert = "using hxsublime.FindDeclaration;"
		src_before_using = python_Tools.substring(src, 0, using_pos)
		src_after_using = python_Tools.substr(src, using_pos, None)
		sel = view.sel()[0]
		pos = sel.begin()
		expr_end = None
		expr_start = None
		if sel.end() == pos:
			r = hxsublime_commands_FindDeclaration_Helper.get_word_at(view, src, pos)
			word_str = r[0]
			word_start = r[1]
			word_end = r[2]
			chars = ["{", "+", "-", "(", "[", "*", "/", "=", ";", ":"]
			res = hxsublime_tools_HxSrcTools.reverse_search_next_char_on_same_nesting_level(src, chars, word_end - 1)
			res = hxsublime_tools_HxSrcTools.skip_whitespace_or_comments(src, res[0] + 1)
			expr_end = word_end
			expr_start = res[0]
		
		else:
			expr_start = pos
			expr_end = sel.end()
		
		src_before_expr = python_Tools.substring(src, using_pos, expr_start)
		src_after_expr = python_Tools.substr(src, expr_end, None)
		expr_string = python_Tools.substring(src, expr_start, expr_end)
		display_str = None
		if use_display:
			display_str = ".|"
		else:
			display_str = ""
		insert_before = helper_method + "("
		order_str = Std.string(order)
		insert_after = ", " + order_str + ")" + display_str
		new_src = src_before_using + using_insert + src_before_expr + insert_before + expr_string + insert_after + src_after_expr
		r = hxsublime_commands_FindDeclaration_Helper.prepare_build(view, project, use_display, new_src)
		build = r[0]
		temp_path = r[1]
		temp_file = r[2]
		def _hx_local_0(out,err):
			hxsublime_Temp.remove_path(temp_path)
			file_pos = python_lib_Re.compile("\\|\\|\\|\\|\\|([^|]+)\\|\\|\\|\\|\\|", python_lib_Re.I)
			res = python_lib_Re.search(file_pos, out)
			if res is not None:
				json_str = res.group(1)
				json_res = python_lib_Json.loads(json_str)
				if python_lib_Types_DictImpl.hasKey(json_res, "error"):
					error = json_res.get("error", None)
					haxe_Log.trace("nothing found (1), cannot find declaration", _Hx_AnonObject(fileName = "FindDeclaration.hx" ,lineNumber = 153 ,className = "hxsublime.commands.HaxeFindDeclarationCommand" ,methodName = "run1" ))
					if order == 1 and use_display:
						_g.run1(True, 2)
					elif order == 2 and use_display:
						_g.run1(True, 3)
					
				
				else:
					_g.handle_successfull_result(view, json_res, using_insert, insert_before, insert_after, expr_end, build, temp_path, temp_file)
			
			elif order == 1 and use_display:
				_g.run1(True, 2)
			elif order == 2 and use_display:
				_g.run1(True, 3)
			elif use_display:
				haxe_Log.trace("nothing found yet (2), try again without display (workaround)", _Hx_AnonObject(fileName = "FindDeclaration.hx" ,lineNumber = 180 ,className = "hxsublime.commands.HaxeFindDeclarationCommand" ,methodName = "run1" ))
				_g.run1(False)
			
			else:
				hxsublime_panel_Base_Panels.default_panel().writeln("Cannot find declaration for expression " + expr_string.strip(None))
				haxe_Log.trace("nothing found (3), cannot find declaration", _Hx_AnonObject(fileName = "FindDeclaration.hx" ,lineNumber = 186 ,className = "hxsublime.commands.HaxeFindDeclarationCommand" ,methodName = "run1" ))
			
		
		cb = _hx_local_0
		build.run(project, view, False, cb)
	

	def handle_successfull_result(self,view,json_res,using_insert,insert_before,insert_after,expr_end,build,temp_path,temp_file):
		file = json_res.get("file", None)
		min = json_res.get("min", 0)
		max = json_res.get("max", 0)
		abs_path = hxsublime_tools_PathTools.joinNorm(build.get_build_folder(), file)
		abs_path_temp = hxsublime_tools_PathTools.joinNorm(build.get_build_folder(), build.get_relative_path(python_lib_os_Path.join(temp_path, temp_file)))
		if abs_path == temp_file:
			if min > expr_end:
				min = min - __builtin__.len(insert_after)
				min = min - __builtin__.len(insert_before)
			
			
			min = min - __builtin__.len(using_insert)
		
		else:
			f = python_lib_Codecs.open(abs_path, "r", "utf-8")
			real_source = f.read()
			f.close()
			offset = 0
			_g = 0
			while _g < min:
				def _hx_local_0():
					nonlocal _g
					_hx_r = _g
					_g = _g + 1
					return _hx_r
					
				
				i = _hx_local_0()
				if real_source[i] == "\r":
					offset = offset + 1
				
			
			
			haxe_Log.trace("offset: " + Std.string(offset), _Hx_AnonObject(fileName = "FindDeclaration.hx" ,lineNumber = 235 ,className = "hxsublime.commands.HaxeFindDeclarationCommand" ,methodName = "handle_successfull_result" ))
			min = min - offset
		
		if abs_path == temp_file:
			target_view = view
			haxe_Log.trace("line ending: " + Std.string(view.settings().get("line_ending")), _Hx_AnonObject(fileName = "FindDeclaration.hx" ,lineNumber = 247 ,className = "hxsublime.commands.HaxeFindDeclarationCommand" ,methodName = "handle_successfull_result" ))
			target_view.sel().clear()
			target_view.sel().add(sublime_Region(min))
			target_view.show(sublime_Region(min))
		
		else:
			hxsublime_commands_FindDeclaration_State.find_decl_file = abs_path
			hxsublime_commands_FindDeclaration_State.find_decl_pos = min
			view.window().open_file(abs_path)
		
	







hxsublime_commands_FindDeclaration_HaxeFindDeclarationCommand._hx_class = hxsublime_commands_FindDeclaration_HaxeFindDeclarationCommand
hxsublime_commands_FindDeclaration_HaxeFindDeclarationCommand._hx_class_name = "hxsublime.commands.HaxeFindDeclarationCommand"
_hx_classes['hxsublime.commands.HaxeFindDeclarationCommand'] = hxsublime_commands_FindDeclaration_HaxeFindDeclarationCommand
hxsublime_commands_FindDeclaration_HaxeFindDeclarationCommand._hx_fields = []
hxsublime_commands_FindDeclaration_HaxeFindDeclarationCommand._hx_props = []
hxsublime_commands_FindDeclaration_HaxeFindDeclarationCommand._hx_methods = ["run","helper_method","run1","handle_successfull_result"]
hxsublime_commands_FindDeclaration_HaxeFindDeclarationCommand._hx_statics = []
hxsublime_commands_FindDeclaration_HaxeFindDeclarationCommand._hx_interfaces = []
hxsublime_commands_FindDeclaration_HaxeFindDeclarationCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.FindDeclaration.State
class hxsublime_commands_FindDeclaration_State:

	pass




hxsublime_commands_FindDeclaration_State.find_decl_file = None
hxsublime_commands_FindDeclaration_State.find_decl_pos = None


hxsublime_commands_FindDeclaration_State._hx_class = hxsublime_commands_FindDeclaration_State
hxsublime_commands_FindDeclaration_State._hx_class_name = "hxsublime.commands._FindDeclaration._FindDeclaration.State"
_hx_classes['hxsublime.commands._FindDeclaration._FindDeclaration.State'] = hxsublime_commands_FindDeclaration_State
hxsublime_commands_FindDeclaration_State._hx_fields = []
hxsublime_commands_FindDeclaration_State._hx_props = []
hxsublime_commands_FindDeclaration_State._hx_methods = []
hxsublime_commands_FindDeclaration_State._hx_statics = ["find_decl_file","find_decl_pos"]
hxsublime_commands_FindDeclaration_State._hx_interfaces = []

# print python.lib.os.Path.Path
from os import path as python_lib_os_Path
# print hxsublime.commands.FindDeclaration.Helper
class hxsublime_commands_FindDeclaration_Helper:

	pass




hxsublime_commands_FindDeclaration_Helper.plugin_path = hxsublime_Plugin.plugin_base_dir()
def Helper_statics_get_word_at(view,src,pos):
	word = view.word(pos)
	word_start = word.a
	word_end = word.b
	word_str = python_Tools.substring(src, word_start, word_end)
	return (word_str, word_start, word_end)
	
hxsublime_commands_FindDeclaration_Helper.get_word_at = Helper_statics_get_word_at
def Helper_statics_prepare_build(view,project,use_display,new_src):
	build = project.get_build(view).copy()
	build.add_arg(("-D", "no-inline"))
	r = hxsublime_Temp.create_temp_path_and_file(build, view.file_name(), new_src)
	temp_path = r[0]
	temp_file = r[1]
	build.add_classpath(temp_path)
	build.add_classpath(python_lib_os_Path.join(hxsublime_commands_FindDeclaration_Helper.plugin_path, "haxetools"))
	haxe_Log.trace(build.classpaths, _Hx_AnonObject(fileName = "FindDeclaration.hx" ,lineNumber = 301 ,className = "hxsublime.commands._FindDeclaration.Helper" ,methodName = "prepare_build" ))
	build.add_arg(("-dce", "no"))
	if use_display:
		build.set_auto_completion(temp_file + "@0", False)
	
	return (build, temp_path, temp_file)
	
hxsublime_commands_FindDeclaration_Helper.prepare_build = Helper_statics_prepare_build


hxsublime_commands_FindDeclaration_Helper._hx_class = hxsublime_commands_FindDeclaration_Helper
hxsublime_commands_FindDeclaration_Helper._hx_class_name = "hxsublime.commands._FindDeclaration._FindDeclaration.Helper"
_hx_classes['hxsublime.commands._FindDeclaration._FindDeclaration.Helper'] = hxsublime_commands_FindDeclaration_Helper
hxsublime_commands_FindDeclaration_Helper._hx_fields = []
hxsublime_commands_FindDeclaration_Helper._hx_props = []
hxsublime_commands_FindDeclaration_Helper._hx_methods = []
hxsublime_commands_FindDeclaration_Helper._hx_statics = ["plugin_path","get_word_at","prepare_build"]
hxsublime_commands_FindDeclaration_Helper._hx_interfaces = []

# print hxsublime.commands.FindDeclaration.HaxeFindDeclarationListener
class hxsublime_commands_FindDeclaration_HaxeFindDeclarationListener(sublime_EventListener):

	def on_activated(self,view):
		if view is not None and view.file_name() is not None:
			if view.file_name() == hxsublime_commands_FindDeclaration_State.find_decl_file:
				view.sel().clear()
				min = hxsublime_commands_FindDeclaration_State.find_decl_pos
				view.sel().add(sublime_Region(min))
				def _hx_local_0():
					view.show_at_center(sublime_Region(min))
				show = _hx_local_0
				sublime_Sublime.set_timeout(show, 70)
			
			
			hxsublime_commands_FindDeclaration_State.find_decl_file = None
			hxsublime_commands_FindDeclaration_State.find_decl_pos = None
	
		







hxsublime_commands_FindDeclaration_HaxeFindDeclarationListener._hx_class = hxsublime_commands_FindDeclaration_HaxeFindDeclarationListener
hxsublime_commands_FindDeclaration_HaxeFindDeclarationListener._hx_class_name = "hxsublime.commands.HaxeFindDeclarationListener"
_hx_classes['hxsublime.commands.HaxeFindDeclarationListener'] = hxsublime_commands_FindDeclaration_HaxeFindDeclarationListener
hxsublime_commands_FindDeclaration_HaxeFindDeclarationListener._hx_fields = []
hxsublime_commands_FindDeclaration_HaxeFindDeclarationListener._hx_props = []
hxsublime_commands_FindDeclaration_HaxeFindDeclarationListener._hx_methods = ["on_activated"]
hxsublime_commands_FindDeclaration_HaxeFindDeclarationListener._hx_statics = []
hxsublime_commands_FindDeclaration_HaxeFindDeclarationListener._hx_interfaces = []
hxsublime_commands_FindDeclaration_HaxeFindDeclarationListener._hx_super = sublime_EventListener

# print hxsublime.commands.GenerateImport.HaxeGenerateUsingCommand
class hxsublime_commands_GenerateImport_HaxeGenerateUsingCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**kwArgs):
		if kwArgs is None:
			kwArgs = None
		
		haxe_Log.trace("run HaxeGenerateUsingCommand", _Hx_AnonObject(fileName = "GenerateImport.hx" ,lineNumber = 15 ,className = "hxsublime.commands.HaxeGenerateUsingCommand" ,methodName = "run" ))
		hxsublime_Codegen_HaxeImportGenerator.generate_using(self.view, edit)
	







hxsublime_commands_GenerateImport_HaxeGenerateUsingCommand._hx_class = hxsublime_commands_GenerateImport_HaxeGenerateUsingCommand
hxsublime_commands_GenerateImport_HaxeGenerateUsingCommand._hx_class_name = "hxsublime.commands.HaxeGenerateUsingCommand"
_hx_classes['hxsublime.commands.HaxeGenerateUsingCommand'] = hxsublime_commands_GenerateImport_HaxeGenerateUsingCommand
hxsublime_commands_GenerateImport_HaxeGenerateUsingCommand._hx_fields = []
hxsublime_commands_GenerateImport_HaxeGenerateUsingCommand._hx_props = []
hxsublime_commands_GenerateImport_HaxeGenerateUsingCommand._hx_methods = ["run"]
hxsublime_commands_GenerateImport_HaxeGenerateUsingCommand._hx_statics = []
hxsublime_commands_GenerateImport_HaxeGenerateUsingCommand._hx_interfaces = []
hxsublime_commands_GenerateImport_HaxeGenerateUsingCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.GenerateImport.HaxeGenerateImportCommand
class hxsublime_commands_GenerateImport_HaxeGenerateImportCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**kwArgs):
		if kwArgs is None:
			kwArgs = None
		
		haxe_Log.trace("run HaxeGenerateImportCommand", _Hx_AnonObject(fileName = "GenerateImport.hx" ,lineNumber = 24 ,className = "hxsublime.commands.HaxeGenerateImportCommand" ,methodName = "run" ))
		hxsublime_Codegen_HaxeImportGenerator.generate_import(self.view, edit)
	







hxsublime_commands_GenerateImport_HaxeGenerateImportCommand._hx_class = hxsublime_commands_GenerateImport_HaxeGenerateImportCommand
hxsublime_commands_GenerateImport_HaxeGenerateImportCommand._hx_class_name = "hxsublime.commands.HaxeGenerateImportCommand"
_hx_classes['hxsublime.commands.HaxeGenerateImportCommand'] = hxsublime_commands_GenerateImport_HaxeGenerateImportCommand
hxsublime_commands_GenerateImport_HaxeGenerateImportCommand._hx_fields = []
hxsublime_commands_GenerateImport_HaxeGenerateImportCommand._hx_props = []
hxsublime_commands_GenerateImport_HaxeGenerateImportCommand._hx_methods = ["run"]
hxsublime_commands_GenerateImport_HaxeGenerateImportCommand._hx_statics = []
hxsublime_commands_GenerateImport_HaxeGenerateImportCommand._hx_interfaces = []
hxsublime_commands_GenerateImport_HaxeGenerateImportCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.GetExprType.HaxeGetTypeOfExprCommand
class hxsublime_commands_GetExprType_HaxeGetTypeOfExprCommand(hxsublime_commands_FindDeclaration_HaxeFindDeclarationCommand):


	def __init__(self,v):
		super().__init__(v)
	def helper_method(self):
		return "hxsublime.FindDeclaration.__getType"

	def handle_successfull_result(self,view,json_res,using_insert,insert_before,insert_after,expr_end,build,temp_path,temp_file):
		t = json_res.get("type", None)
		e = json_res.get("expr", None)
		msg = "Expr: " + e + "\n" + "Type: " + t
		hxsublime_panel_Base_Panels.slide_panel().writeln(msg, None, False)
	







hxsublime_commands_GetExprType_HaxeGetTypeOfExprCommand._hx_class = hxsublime_commands_GetExprType_HaxeGetTypeOfExprCommand
hxsublime_commands_GetExprType_HaxeGetTypeOfExprCommand._hx_class_name = "hxsublime.commands.HaxeGetTypeOfExprCommand"
_hx_classes['hxsublime.commands.HaxeGetTypeOfExprCommand'] = hxsublime_commands_GetExprType_HaxeGetTypeOfExprCommand
hxsublime_commands_GetExprType_HaxeGetTypeOfExprCommand._hx_fields = []
hxsublime_commands_GetExprType_HaxeGetTypeOfExprCommand._hx_props = []
hxsublime_commands_GetExprType_HaxeGetTypeOfExprCommand._hx_methods = ["helper_method","handle_successfull_result"]
hxsublime_commands_GetExprType_HaxeGetTypeOfExprCommand._hx_statics = []
hxsublime_commands_GetExprType_HaxeGetTypeOfExprCommand._hx_interfaces = []
hxsublime_commands_GetExprType_HaxeGetTypeOfExprCommand._hx_super = hxsublime_commands_FindDeclaration_HaxeFindDeclarationCommand

# print hxsublime.commands.GotoBase.HaxeGotoBaseCommand
class hxsublime_commands_GotoBase_HaxeGotoBaseCommand(sublime_TextCommand):


	def __init__(self,v):
		self.selecting_build = False
		super().__init__(v)
	
	# var selecting_build
	def get_entries(self,types):
		raise _HxException("abstract method")

	def get_data(self,types):
		raise _HxException("abstract method")

	def get_file(self,data_entry):
		raise _HxException("abstract method")

	def get_src_pos(self,data_entry):
		raise _HxException("abstract method")

	def run(self,edit,**kwArgs):
		if kwArgs is None:
			kwArgs = None
		
		_g = self
		haxe_Log.trace("run HaxeListBuildFieldsCommand", _Hx_AnonObject(fileName = "GotoBase.hx" ,lineNumber = 51 ,className = "hxsublime.commands.HaxeGotoBaseCommand" ,methodName = "run" ))
		view = self.view
		project = hxsublime_project_Base_Projects.current_project(view)
		if not project.has_build():
			project.extract_build_args(view, False)
		
		if not project.has_build():
			project.extract_build_args(view, True)
			return
		
		
		build = project.get_build(view)
		bundle = build.get_types().merge(build.std_bundle())
		bundle_types = bundle.all_types_and_enum_constructors_with_info()
		filtered_types = haxe_ds_StringMap()
		_it = bundle_types.keys()
		while _it.hasNext():
			k = _it.next()
			t = bundle_types.get(k)
			if build.is_type_available(t):
				filtered_types.set(k, t)
			
			
		
		
		function_list = self.get_entries(filtered_types)
		function_list_data = self.get_data(filtered_types)
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
		def _hx_local_0(i):
			hxsublime_commands_GotoBase_State._is_open = False
			hxsublime_commands_GotoBase_State._init_text = ""
			if i >= 0:
				selected_type = function_list_data[i]
				haxe_Log.trace("selected field: " + Std.string(selected_type[0]), _Hx_AnonObject(fileName = "GotoBase.hx" ,lineNumber = 127 ,className = "hxsublime.commands.HaxeGotoBaseCommand" ,methodName = "run" ))
				src_pos = _g.get_src_pos(selected_type[1])
				goto_file = _g.get_file(selected_type[1])
				hxsublime_commands_GotoBase_State._find_decl_file = goto_file
				haxe_Log.trace("find_decl_file: " + Std.string(hxsublime_commands_GotoBase_State._find_decl_file), _Hx_AnonObject(fileName = "GotoBase.hx" ,lineNumber = 135 ,className = "hxsublime.commands.HaxeGotoBaseCommand" ,methodName = "run" ))
				if src_pos is not None:
					hxsublime_commands_GotoBase_State._find_decl_pos = src_pos
					haxe_Log.trace("src_pos" + Std.string(src_pos), _Hx_AnonObject(fileName = "GotoBase.hx" ,lineNumber = 139 ,className = "hxsublime.commands.HaxeGotoBaseCommand" ,methodName = "run" ))
				
				else:
					hxsublime_commands_GotoBase_State._find_decl_pos = 0
				def _hx_local_1():
					win.open_file(goto_file)
				show = _hx_local_1
				sublime_Sublime.set_timeout(show, 130)
			
			
		
		on_selected = _hx_local_0
		hxsublime_commands_GotoBase_State._is_open = True
		win.show_quick_panel(function_list, on_selected, sublime_Sublime.MONOSPACE_FONT)
	







hxsublime_commands_GotoBase_HaxeGotoBaseCommand._hx_class = hxsublime_commands_GotoBase_HaxeGotoBaseCommand
hxsublime_commands_GotoBase_HaxeGotoBaseCommand._hx_class_name = "hxsublime.commands.HaxeGotoBaseCommand"
_hx_classes['hxsublime.commands.HaxeGotoBaseCommand'] = hxsublime_commands_GotoBase_HaxeGotoBaseCommand
hxsublime_commands_GotoBase_HaxeGotoBaseCommand._hx_fields = ["selecting_build"]
hxsublime_commands_GotoBase_HaxeGotoBaseCommand._hx_props = []
hxsublime_commands_GotoBase_HaxeGotoBaseCommand._hx_methods = ["get_entries","get_data","get_file","get_src_pos","run"]
hxsublime_commands_GotoBase_HaxeGotoBaseCommand._hx_statics = []
hxsublime_commands_GotoBase_HaxeGotoBaseCommand._hx_interfaces = []
hxsublime_commands_GotoBase_HaxeGotoBaseCommand._hx_super = sublime_TextCommand

# print hxsublime.commands.GotoAnything.HaxeGotoAnythingCommand
class hxsublime_commands_GotoAnything_HaxeGotoAnythingCommand(hxsublime_commands_GotoBase_HaxeGotoBaseCommand):


	def __init__(self,v):
		super().__init__(v)
	def get_entries(self,types):
		fields = None
		_g = []
		_it = types.keys()
		while _it.hasNext():
			k = _it.next()
			_g1 = 0
			_g2 = types.get(k).all_fields_list()
			while _g1 < len(_g2):
				p = _g2[_g1]
				_g1 = _g1 + 1
				x = [p.toString() + " - " + p.kind, p.type.file()]
				_g.append(x)
				__builtin__.len(_g)
				
			
			
		
		
		fields = _g
		
		types1 = None
		_g1 = []
		_it = types.keys()
		while _it.hasNext():
			k = _it.next()
			x = [k, types.get(k).file()]
			_g1.append(x)
			__builtin__.len(_g1)
			
			
		
		
		types1 = _g1
		
		fields.extend(types1)
		return fields
	

	def toEntry(self,e):
		return e

	def get_data(self,types):
		fields = None
		_g = []
		_it = types.keys()
		while _it.hasNext():
			k = _it.next()
			_g1 = 0
			_g2 = types.get(k).all_fields_list()
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
	

	def get_file(self,data_entry):
		return data_entry.file()

	def get_src_pos(self,data_entry):
		return data_entry.src_pos()







hxsublime_commands_GotoAnything_HaxeGotoAnythingCommand._hx_class = hxsublime_commands_GotoAnything_HaxeGotoAnythingCommand
hxsublime_commands_GotoAnything_HaxeGotoAnythingCommand._hx_class_name = "hxsublime.commands.HaxeGotoAnythingCommand"
_hx_classes['hxsublime.commands.HaxeGotoAnythingCommand'] = hxsublime_commands_GotoAnything_HaxeGotoAnythingCommand
hxsublime_commands_GotoAnything_HaxeGotoAnythingCommand._hx_fields = []
hxsublime_commands_GotoAnything_HaxeGotoAnythingCommand._hx_props = []
hxsublime_commands_GotoAnything_HaxeGotoAnythingCommand._hx_methods = ["get_entries","toEntry","get_data","get_file","get_src_pos"]
hxsublime_commands_GotoAnything_HaxeGotoAnythingCommand._hx_statics = []
hxsublime_commands_GotoAnything_HaxeGotoAnythingCommand._hx_interfaces = []
hxsublime_commands_GotoAnything_HaxeGotoAnythingCommand._hx_super = hxsublime_commands_GotoBase_HaxeGotoBaseCommand

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
class hxsublime_commands_GotoBase_HaxeGotoBaseListener(sublime_EventListener):

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
		
			
		
	







hxsublime_commands_GotoBase_HaxeGotoBaseListener._hx_class = hxsublime_commands_GotoBase_HaxeGotoBaseListener
hxsublime_commands_GotoBase_HaxeGotoBaseListener._hx_class_name = "hxsublime.commands.HaxeGotoBaseListener"
_hx_classes['hxsublime.commands.HaxeGotoBaseListener'] = hxsublime_commands_GotoBase_HaxeGotoBaseListener
hxsublime_commands_GotoBase_HaxeGotoBaseListener._hx_fields = []
hxsublime_commands_GotoBase_HaxeGotoBaseListener._hx_props = []
hxsublime_commands_GotoBase_HaxeGotoBaseListener._hx_methods = ["on_activated"]
hxsublime_commands_GotoBase_HaxeGotoBaseListener._hx_statics = []
hxsublime_commands_GotoBase_HaxeGotoBaseListener._hx_interfaces = []
hxsublime_commands_GotoBase_HaxeGotoBaseListener._hx_super = sublime_EventListener

# print hxsublime.commands.GotoBuildFields.HaxeGotoBuildFieldsCommand
class hxsublime_commands_GotoBuildFields_HaxeGotoBuildFieldsCommand(hxsublime_commands_GotoBase_HaxeGotoBaseCommand):


	def __init__(self,v):
		super().__init__(v)
	def get_entries(self,types):
		_g = []
		_it = types.keys()
		while _it.hasNext():
			k = _it.next()
			_g1 = 0
			_g2 = types.get(k).all_fields_list()
			while _g1 < len(_g2):
				p = _g2[_g1]
				_g1 = _g1 + 1
				x = [p.toString() + " - " + p.kind, p.type.file()]
				_g.append(x)
				__builtin__.len(_g)
				
			
			
		
		
		return _g
	

	def get_data(self,types):
		_g = []
		_it = types.keys()
		while _it.hasNext():
			k = _it.next()
			_g1 = 0
			_g2 = types.get(k).all_fields_list()
			while _g1 < len(_g2):
				p = _g2[_g1]
				_g1 = _g1 + 1
				x = (k + "." + p.name, p)
				_g.append(x)
				__builtin__.len(_g)
				
			
			
		
		
		return _g
	

	def get_file(self,data_entry):
		return data_entry.type.file()

	def get_src_pos(self,data_entry):
		return data_entry.src_pos()







hxsublime_commands_GotoBuildFields_HaxeGotoBuildFieldsCommand._hx_class = hxsublime_commands_GotoBuildFields_HaxeGotoBuildFieldsCommand
hxsublime_commands_GotoBuildFields_HaxeGotoBuildFieldsCommand._hx_class_name = "hxsublime.commands.HaxeGotoBuildFieldsCommand"
_hx_classes['hxsublime.commands.HaxeGotoBuildFieldsCommand'] = hxsublime_commands_GotoBuildFields_HaxeGotoBuildFieldsCommand
hxsublime_commands_GotoBuildFields_HaxeGotoBuildFieldsCommand._hx_fields = []
hxsublime_commands_GotoBuildFields_HaxeGotoBuildFieldsCommand._hx_props = []
hxsublime_commands_GotoBuildFields_HaxeGotoBuildFieldsCommand._hx_methods = ["get_entries","get_data","get_file","get_src_pos"]
hxsublime_commands_GotoBuildFields_HaxeGotoBuildFieldsCommand._hx_statics = []
hxsublime_commands_GotoBuildFields_HaxeGotoBuildFieldsCommand._hx_interfaces = []
hxsublime_commands_GotoBuildFields_HaxeGotoBuildFieldsCommand._hx_super = hxsublime_commands_GotoBase_HaxeGotoBaseCommand

# print hxsublime.commands.GotoBuildTypes.HaxeGotoBuildTypesCommand
class hxsublime_commands_GotoBuildTypes_HaxeGotoBuildTypesCommand(hxsublime_commands_GotoBase_HaxeGotoBaseCommand):


	def __init__(self,v):
		super().__init__(v)
	def get_entries(self,types):
		_g = []
		_it = types.keys()
		while _it.hasNext():
			k = _it.next()
			x = [k, types.get(k).file()]
			_g.append(x)
			__builtin__.len(_g)
			
			
		
		
		return _g
	

	def get_data(self,types):
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
	

	def get_file(self,data_entry):
		return data_entry.file()

	def get_src_pos(self,data_entry):
		return data_entry.src_pos()







hxsublime_commands_GotoBuildTypes_HaxeGotoBuildTypesCommand._hx_class = hxsublime_commands_GotoBuildTypes_HaxeGotoBuildTypesCommand
hxsublime_commands_GotoBuildTypes_HaxeGotoBuildTypesCommand._hx_class_name = "hxsublime.commands.HaxeGotoBuildTypesCommand"
_hx_classes['hxsublime.commands.HaxeGotoBuildTypesCommand'] = hxsublime_commands_GotoBuildTypes_HaxeGotoBuildTypesCommand
hxsublime_commands_GotoBuildTypes_HaxeGotoBuildTypesCommand._hx_fields = []
hxsublime_commands_GotoBuildTypes_HaxeGotoBuildTypesCommand._hx_props = []
hxsublime_commands_GotoBuildTypes_HaxeGotoBuildTypesCommand._hx_methods = ["get_entries","get_data","get_file","get_src_pos"]
hxsublime_commands_GotoBuildTypes_HaxeGotoBuildTypesCommand._hx_statics = []
hxsublime_commands_GotoBuildTypes_HaxeGotoBuildTypesCommand._hx_interfaces = []
hxsublime_commands_GotoBuildTypes_HaxeGotoBuildTypesCommand._hx_super = hxsublime_commands_GotoBase_HaxeGotoBaseCommand

# print hxsublime.commands.Haxelib.HaxeInstallLibCommand
class hxsublime_commands_Haxelib_HaxeInstallLibCommand(sublime_WindowCommand):


	def __init__(self,w):
		super().__init__(w)
	def run(self,**_):
		view = sublime_Sublime.active_window().active_view()
		project = hxsublime_project_Base_Projects.current_project(view)
		if project is not None:
			manager = project.haxelib_manager()
			libs = manager.search_libs()
			menu = self._prepare_menu(libs, manager)
			on_selected = None
			f = self._entry_selected
			a1 = libs
			a2 = manager
			def _hx_local_0(i):
				return f(a1, a2, i)
			on_selected = _hx_local_0
			
			haxe_Log.trace(libs, _Hx_AnonObject(fileName = "Haxelib.hx" ,lineNumber = 29 ,className = "hxsublime.commands.HaxeInstallLibCommand" ,methodName = "run" ))
			self.window.show_quick_panel(menu, on_selected)
		
		
	

	def _prepare_menu(self,libs,manager):
		menu = []
		_g = 0
		while _g < len(libs):
			l = libs[_g]
			_g = _g + 1
			if manager.is_lib_installed(l):
				menu.append([l + " [" + manager.get_lib(l).version + "]", "Remove"])
				__builtin__.len(menu)
			
			else:
				menu.append([l, "Install"])
				__builtin__.len(menu)
			
		
		
		menu.append(["Upgrade libraries", "Upgrade installed libraries"])
		__builtin__.len(menu)
		
		menu.append(["Haxelib Selfupdate", "Updates Haxelib itself"])
		__builtin__.len(menu)
		
		return menu
	

	def _entry_selected(self,libs,manager,i):
		haxe_Log.trace("install lib command selected " + Std.string(i), _Hx_AnonObject(fileName = "Haxelib.hx" ,lineNumber = 56 ,className = "hxsublime.commands.HaxeInstallLibCommand" ,methodName = "_entry_selected" ))
		if i < 0:
			return
		
		if i == __builtin__.len(libs):
			haxe_Log.trace("upgrade all", _Hx_AnonObject(fileName = "Haxelib.hx" ,lineNumber = 62 ,className = "hxsublime.commands.HaxeInstallLibCommand" ,methodName = "_entry_selected" ))
			manager.upgrade_all()
		
		
		if i == __builtin__.len(libs) + 1:
			haxe_Log.trace("self update", _Hx_AnonObject(fileName = "Haxelib.hx" ,lineNumber = 68 ,className = "hxsublime.commands.HaxeInstallLibCommand" ,methodName = "_entry_selected" ))
			manager.self_update()
		
		else:
			lib = libs[i]
			if manager.available().exists(lib):
				haxe_Log.trace("remove " + lib, _Hx_AnonObject(fileName = "Haxelib.hx" ,lineNumber = 76 ,className = "hxsublime.commands.HaxeInstallLibCommand" ,methodName = "_entry_selected" ))
				manager.remove_lib(lib)
			
			else:
				haxe_Log.trace("install " + lib, _Hx_AnonObject(fileName = "Haxelib.hx" ,lineNumber = 81 ,className = "hxsublime.commands.HaxeInstallLibCommand" ,methodName = "_entry_selected" ))
				manager.install_lib(lib)
			
		
	







hxsublime_commands_Haxelib_HaxeInstallLibCommand._hx_class = hxsublime_commands_Haxelib_HaxeInstallLibCommand
hxsublime_commands_Haxelib_HaxeInstallLibCommand._hx_class_name = "hxsublime.commands.HaxeInstallLibCommand"
_hx_classes['hxsublime.commands.HaxeInstallLibCommand'] = hxsublime_commands_Haxelib_HaxeInstallLibCommand
hxsublime_commands_Haxelib_HaxeInstallLibCommand._hx_fields = []
hxsublime_commands_Haxelib_HaxeInstallLibCommand._hx_props = []
hxsublime_commands_Haxelib_HaxeInstallLibCommand._hx_methods = ["run","_prepare_menu","_entry_selected"]
hxsublime_commands_Haxelib_HaxeInstallLibCommand._hx_statics = []
hxsublime_commands_Haxelib_HaxeInstallLibCommand._hx_interfaces = []
hxsublime_commands_Haxelib_HaxeInstallLibCommand._hx_super = sublime_WindowCommand

# print hxsublime.commands.ShowDoc.HaxeShowDocCommand
class hxsublime_commands_ShowDoc_HaxeShowDocCommand(hxsublime_commands_FindDeclaration_HaxeFindDeclarationCommand):


	def __init__(self,v):
		super().__init__(v)
	def helper_method(self):
		return "hxsublime.FindDeclaration.__sublimeShowDoc"

	def handle_successfull_result(self,view,json_res,using_insert,insert_before,insert_after,expr_end,build,temp_path,temp_file):
		doc = None
		if python_lib_Types_DictImpl.hasKey(json_res, "doc"):
			doc = json_res.get("doc", None)
		else:
			doc = "No documentation found"
		haxe_Log.trace("json: " + Std.string(json_res), _Hx_AnonObject(fileName = "ShowDoc.hx" ,lineNumber = 27 ,className = "hxsublime.commands.HaxeShowDocCommand" ,methodName = "handle_successfull_result" ))
		haxe_Log.trace("doc: " + Std.string(doc), _Hx_AnonObject(fileName = "ShowDoc.hx" ,lineNumber = 28 ,className = "hxsublime.commands.HaxeShowDocCommand" ,methodName = "handle_successfull_result" ))
		hxsublime_panel_Base_Panels.slide_panel().writeln(doc, None, False)
	







hxsublime_commands_ShowDoc_HaxeShowDocCommand._hx_class = hxsublime_commands_ShowDoc_HaxeShowDocCommand
hxsublime_commands_ShowDoc_HaxeShowDocCommand._hx_class_name = "hxsublime.commands.HaxeShowDocCommand"
_hx_classes['hxsublime.commands.HaxeShowDocCommand'] = hxsublime_commands_ShowDoc_HaxeShowDocCommand
hxsublime_commands_ShowDoc_HaxeShowDocCommand._hx_fields = []
hxsublime_commands_ShowDoc_HaxeShowDocCommand._hx_props = []
hxsublime_commands_ShowDoc_HaxeShowDocCommand._hx_methods = ["helper_method","handle_successfull_result"]
hxsublime_commands_ShowDoc_HaxeShowDocCommand._hx_statics = []
hxsublime_commands_ShowDoc_HaxeShowDocCommand._hx_interfaces = []
hxsublime_commands_ShowDoc_HaxeShowDocCommand._hx_super = hxsublime_commands_FindDeclaration_HaxeFindDeclarationCommand

# print hxsublime.compiler.Output.CompletionEntry
class hxsublime_compiler_Output_CompletionEntry:


	def __init__(self,hint,insert,doc):
		self.hint = hint
		self.insert = insert
		self.doc = doc
	
	# var hint
	# var insert
	# var doc






hxsublime_compiler_Output_CompletionEntry._hx_class = hxsublime_compiler_Output_CompletionEntry
hxsublime_compiler_Output_CompletionEntry._hx_class_name = "hxsublime.compiler.CompletionEntry"
_hx_classes['hxsublime.compiler.CompletionEntry'] = hxsublime_compiler_Output_CompletionEntry
hxsublime_compiler_Output_CompletionEntry._hx_fields = ["hint","insert","doc"]
hxsublime_compiler_Output_CompletionEntry._hx_props = []
hxsublime_compiler_Output_CompletionEntry._hx_methods = []
hxsublime_compiler_Output_CompletionEntry._hx_statics = []
hxsublime_compiler_Output_CompletionEntry._hx_interfaces = []

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
	_g = 0
	_g1 = __builtin__.list(types)
	while _g < len(_g1):
		i = _g1[_g]
		_g = _g + 1
		haxe_Log.trace(i, _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 59 ,className = "hxsublime.compiler.Output" ,methodName = "get_type_hint" ))
		hint = i.text.strip(None)
		hint_types = hxsublime_tools_HxSrcTools.split_function_signature(hint)
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
	haxe_Log.trace(type_param_list, _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 105 ,className = "hxsublime.compiler.Output" ,methodName = "get_function_type_params" ))
	haxe_Log.trace(new_args, _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 106 ,className = "hxsublime.compiler.Output" ,methodName = "get_function_type_params" ))
	return (new_args, type_param_list)
	
hxsublime_compiler_Output.get_function_type_params = Output_statics_get_function_type_params
def Output_statics_completion_field_to_entry(name,sig,doc):
	insert = name
	label = name
	smart_snippets = hxsublime_Settings.smart_snippets_on_completion()
	not_smart = not smart_snippets
	if sig is not None:
		types = hxsublime_tools_HxSrcTools.split_function_signature(sig)
		haxe_Log.trace(types, _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 125 ,className = "hxsublime.compiler.Output" ,methodName = "completion_field_to_entry" ))
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
					label = name + params_sig + "()" + signature_separator + ret
				else:
					label = name + "()" + signature_separator + ret
				if not_smart:
					insert = name
				else:
					insert = "" + name + "${1:()}"
		
			else:
				def _hx_local_0(x):
					return StringTools.replace(StringTools.replace(x, "}", "\\}"), "{", "\\{")
				escape_type = _hx_local_0
				params = "( " + ", ".join(types1) + " )"
				label = name + params_sig + params + signature_separator + ret
				new_types = __builtin__.list(types1)
				_g1 = 0
				_g = __builtin__.len(new_types)
				while _g1 < _g:
					def _hx_local_1():
						nonlocal _g1
						_hx_r = _g1
						_g1 = _g1 + 1
						return _hx_r
						
					
					i = _hx_local_1()
					new_types[i] = "${" + Std.string(i + 2) + ":" + escape_type(new_types[i]) + "}"
				
				
				if not_smart:
					insert = name
				else:
					insert = name + "${1:( " + ", ".join(new_types) + " )}"
		
		else:
			label = name + params_sig + signature_separator + ret
	
	elif python_lib_Re.match("^[A-Z]", name) is not None:
		label = name + "\tclass"
	else:
		label = name + "\tpackage"
	res = hxsublime_compiler_Output_CompletionEntry(label, insert, doc)
	return res
	
hxsublime_compiler_Output.completion_field_to_entry = Output_statics_completion_field_to_entry
def Output_statics_collect_completion_fields(li):
	comps = []
	if li is not None:
		_g = 0
		_g1 = __builtin__.list(li.iter("i"))
		while _g < len(_g1):
			i = _g1[_g]
			_g = _g + 1
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
	def _hx_local_1():
		def _hx_local_0():
			_this = python_lib_Re_RegexHelper.findallDynamic(hxsublime_compiler_Output.no_classes_found, str, None, None)
			return __builtin__.len(_this)
		
		return _hx_local_0() > 0
	
	if _hx_local_1():
		errors = []
	else:
		_g = 0
		_g1 = None
		_this = python_lib_Re_RegexHelper.findallDynamic(hxsublime_compiler_Output.compiler_output, str, None, None)
		def _hx_local_2(t):
			return __builtin__.list(t)
		_g1 = __builtin__.list(__builtin__.map(_hx_local_2, _this))
		
		while _g < len(_g1):
			infos = _g1[_g]
			_g = _g + 1
			infos1 = __builtin__.list(infos)
			f = infos1.pop(0)
			l = None
			def _hx_local_6():
				def _hx_local_3():
					x = infos1.pop(0)
					def _hx_local_5():
						def _hx_local_4():
							x1 = float(x)
							return int(x1)
						
						return _hx_local_4()
					
					return _hx_local_5()
				
				return _hx_local_3() - 1
			
			l = _hx_local_6()
			left = None
			x = infos1.pop(0)
			x1 = float(x)
			left = int(x1)
			
			
			right = infos1.pop(0)
			rightInt = 0
			if right != "":
				x = float(right)
				rightInt = int(x)
			
			else:
				rightInt = left + 1
			m = infos1.pop(0)
			if m != "Unexpected |":
				errors.append(_Hx_AnonObject(file = f ,line = l ,_hx_from = left ,to = rightInt ,message = m ))
				__builtin__.len(errors)
			
			
		
	
	if __builtin__.len(errors) > 0:
		haxe_Log.trace("should show panel", _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 268 ,className = "hxsublime.compiler.Output" ,methodName = "extract_errors" ))
		hxsublime_panel_Base_Panels.slide_panel().writeln(errors[0].message)
		sublime_Sublime.status_message(errors[0].message)
	
	
	return errors
	
hxsublime_compiler_Output.extract_errors = Output_statics_extract_errors
def Output_statics_get_completion_output(temp_file,orig_file,output,commas):
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
	
hxsublime_compiler_Output.get_completion_output = Output_statics_get_completion_output
def Output_statics_parse_completion_output(temp_file,orig_file,output):
	tree = None
	try:
		x = "<root>" + output + "</root>"
		tree = python_lib_xml_etree_ElementTree.XML(x)
	
	except Exception as _hx_e:
		_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
		if isinstance(_hx_e1, Exception):
			e = _hx_e1
			haxe_Log.trace("invalid xml - error: " + Std.string(e), _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 313 ,className = "hxsublime.compiler.Output" ,methodName = "parse_completion_output" ))
		else:
			raise _hx_e
	hints = None
	comps = None
	if tree is not None:
		hints = hxsublime_compiler_Output.get_type_hint(tree.iter("type"))
		comps = hxsublime_compiler_Output.collect_completion_fields(tree.find("list"))
		haxe_Log.trace("hints:" + Std.string(hints), _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 327 ,className = "hxsublime.compiler.Output" ,methodName = "parse_completion_output" ))
		haxe_Log.trace("comps:" + Std.string(comps), _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 328 ,className = "hxsublime.compiler.Output" ,methodName = "parse_completion_output" ))
	
	else:
		hints = []
		comps = []
	
	def _hx_local_1():
		def _hx_local_0():
			_this = hxsublime_compiler_Output.no_classes_found_in_trace.findall(output, 0)
			return __builtin__.len(_this)
		
		return _hx_local_0() > 0
	
	if _hx_local_1():
		smart_snippets = hxsublime_Settings.smart_snippets_on_completion()
		insert = None
		if smart_snippets:
			insert = "${1:value:Dynamic}"
		else:
			insert = "${0}"
		x = hxsublime_compiler_Output_CompletionEntry("value:Dynamic", insert, "")
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
	haxe_Log.trace("output:" + output, _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 372 ,className = "hxsublime.compiler.Output" ,methodName = "parse_completion_errors" ))
	haxe_Log.trace("status:" + status, _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 373 ,className = "hxsublime.compiler.Output" ,methodName = "parse_completion_errors" ))
	haxe_Log.trace("orig_file:" + orig_file, _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 374 ,className = "hxsublime.compiler.Output" ,methodName = "parse_completion_errors" ))
	haxe_Log.trace("temp_file:" + temp_file, _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 375 ,className = "hxsublime.compiler.Output" ,methodName = "parse_completion_errors" ))
	sep = python_lib_Os.sep
	haxe_Log.trace("sep: " + sep, _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 380 ,className = "hxsublime.compiler.Output" ,methodName = "parse_completion_errors" ))
	if sep == "\\":
		def _hx_local_0(match_obj):
			haxe_Log.trace("matched", _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 383 ,className = "hxsublime.compiler.Output" ,methodName = "parse_completion_errors" ))
			_this = match_obj.group(0).split("/")
			return sep.join(_this)
			
		
		slash_replace = _hx_local_0
		output = python_lib_Re.sub("[A-Za-z]:(.*)[.]hx", slash_replace, output)
	
	
	output = StringTools.replace(output, temp_file, orig_file)
	haxe_Log.trace("output after replace: " + output, _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 392 ,className = "hxsublime.compiler.Output" ,methodName = "parse_completion_errors" ))
	output = python_lib_Re.sub("\\(display(.*)\\)", "", output)
	lines = output.split("\n")
	l = lines[0].strip(None)
	status1 = None
	if __builtin__.len(l) > 0:
		if l == "<list>":
			status1 = "No autocompletion available"
		elif python_lib_Re.match(hxsublime_compiler_Output.haxe_compiler_line, l) is None:
			status1 = l
			haxe_Log.trace(l, _Hx_AnonObject(fileName = "Output.hx" ,lineNumber = 407 ,className = "hxsublime.compiler.Output" ,methodName = "parse_completion_errors" ))
	
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
hxsublime_compiler_Output._hx_statics = ["compiler_output","no_classes_found","no_classes_found_in_trace","haxe_compiler_line","type_parameter_name","get_type_hint","get_function_type_params","completion_field_to_entry","collect_completion_fields","extract_errors","get_completion_output","parse_completion_output","get_completion_status_and_errors","parse_completion_errors"]
hxsublime_compiler_Output._hx_interfaces = []

# print hxsublime.compiler.Server.Server
class hxsublime_compiler_Server:


	def __init__(self,port):
		self._use_wrapper = hxsublime_Settings.use_haxe_servermode_wrapper()
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
						
						return python_Lib_HaxeIterator(p)
					
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
						python_lib_Types_DictImpl.set(full_env, k, val1)
						
						
					
				
				
				haxe_Log.trace("server env:" + Std.string(full_env), _Hx_AnonObject(fileName = "Server.hx" ,lineNumber = 106 ,className = "hxsublime.compiler.Server" ,methodName = "start" ))
				o = _Hx_AnonObject(cwd = cwd ,env = full_env ,stdin = python_lib_Subprocess.PIPE ,stdout = python_lib_Subprocess.PIPE ,startupinfo = hxsublime_Plugin.startupInfo() )
				if __builtin__.hasattr(o, "bufsize"):
					o.bufsize = o.bufsize
				else:
					o.bufsize = 0
				if __builtin__.hasattr(o, "executable"):
					o.executable = o.executable
				else:
					o.executable = None
				if __builtin__.hasattr(o, "stdin"):
					o.stdin = o.stdin
				else:
					o.stdin = None
				if __builtin__.hasattr(o, "stdout"):
					o.stdout = o.stdout
				else:
					o.stdout = None
				if __builtin__.hasattr(o, "stderr"):
					o.stderr = o.stderr
				else:
					o.stderr = None
				if __builtin__.hasattr(o, "preexec_fn"):
					o.preexec_fn = o.preexec_fn
				else:
					o.preexec_fn = None
				if __builtin__.hasattr(o, "close_fds"):
					o.close_fds = o.close_fds
				else:
					o.close_fds = None
				if __builtin__.hasattr(o, "shell"):
					o.shell = o.shell
				else:
					o.shell = None
				if __builtin__.hasattr(o, "cwd"):
					o.cwd = o.cwd
				else:
					o.cwd = None
				if __builtin__.hasattr(o, "env"):
					o.env = o.env
				else:
					o.env = None
				if __builtin__.hasattr(o, "universal_newlines"):
					o.universal_newlines = o.universal_newlines
				else:
					o.universal_newlines = None
				if __builtin__.hasattr(o, "startupinfo"):
					o.startupinfo = o.startupinfo
				else:
					o.startupinfo = None
				if __builtin__.hasattr(o, "creationflags"):
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
				elif True:
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
			else:
				raise _hx_e
		if completeCallback is not None:
			hxsublime_panel_Base_Panels.default_panel().writeln("stopping server on port: " + Std.string(old_port))
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

# print hxsublime.completion.Base.CompletionListener
class hxsublime_completion_Base_CompletionListener(sublime_EventListener):

	def on_query_completions(self,view,prefix,locations):
		project = hxsublime_project_Base_Projects.current_project(view)
		return hxsublime_completion_Base_Completion.dispatch_auto_complete(project, view, prefix, locations[0])
	







hxsublime_completion_Base_CompletionListener._hx_class = hxsublime_completion_Base_CompletionListener
hxsublime_completion_Base_CompletionListener._hx_class_name = "hxsublime.completion.CompletionListener"
_hx_classes['hxsublime.completion.CompletionListener'] = hxsublime_completion_Base_CompletionListener
hxsublime_completion_Base_CompletionListener._hx_fields = []
hxsublime_completion_Base_CompletionListener._hx_props = []
hxsublime_completion_Base_CompletionListener._hx_methods = ["on_query_completions"]
hxsublime_completion_Base_CompletionListener._hx_statics = []
hxsublime_completion_Base_CompletionListener._hx_interfaces = []
hxsublime_completion_Base_CompletionListener._hx_super = sublime_EventListener

# print hxsublime.completion.Base.Completion
class hxsublime_completion_Base_Completion:

	pass




def Completion_statics_get_completion_scopes(view,location):
	return hxsublime_tools_ViewTools.getScopesAt(view, location)
hxsublime_completion_Base_Completion.get_completion_scopes = Completion_statics_get_completion_scopes
def Completion_statics_get_completion_offset(location,prefix):
	return location - __builtin__.len(prefix)
hxsublime_completion_Base_Completion.get_completion_offset = Completion_statics_get_completion_offset
def Completion_statics_can_run_completion(offset,scopes):
	if offset == 0:
		return False
	else:
		return hxsublime_completion_Base_Completion.is_supported_scope(scopes)
hxsublime_completion_Base_Completion.can_run_completion = Completion_statics_can_run_completion
def Completion_statics_is_supported_scope(scopes):
	return not hxsublime_tools_ScopeTools.containsStringOrComment(scopes)
hxsublime_completion_Base_Completion.is_supported_scope = Completion_statics_is_supported_scope
def Completion_statics_empty_handler(project,view,offset,prefix):
	return []
hxsublime_completion_Base_Completion.empty_handler = Completion_statics_empty_handler
def Completion_statics_get_auto_complete_handler(view,scopes):
	handler = None
	if Lambda.has(scopes, hxsublime_Config.SOURCE_HXML):
		handler = hxsublime_completion_hxml_Base.auto_complete
	elif Lambda.has(scopes, hxsublime_Config.SOURCE_HAXE):
		if hxsublime_tools_ViewTools.isHxsl(view):
			handler = hxsublime_completion_hxsl_Base.auto_complete
		else:
			handler = hxsublime_completion_hx_Base.auto_complete
	else:
		handler = hxsublime_completion_Base_Completion.empty_handler
	return handler
	
hxsublime_completion_Base_Completion.get_auto_complete_handler = Completion_statics_get_auto_complete_handler
def Completion_statics_dispatch_auto_complete(project,view,prefix,location):
	start_time = python_lib_Time.time()
	offset = hxsublime_completion_Base_Completion.get_completion_offset(location, prefix)
	scopes = hxsublime_completion_Base_Completion.get_completion_scopes(view, location)
	comps = None
	haxe_Log.trace("pre handler", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 81 ,className = "hxsublime.completion.Completion" ,methodName = "dispatch_auto_complete" ))
	if hxsublime_completion_Base_Completion.can_run_completion(offset, scopes):
		haxe_Log.trace("run handler", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 83 ,className = "hxsublime.completion.Completion" ,methodName = "dispatch_auto_complete" ))
		handler = hxsublime_completion_Base_Completion.get_auto_complete_handler(view, scopes)
		comps = handler(project, view, offset, prefix)
	
	else:
		haxe_Log.trace("no handler", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 88 ,className = "hxsublime.completion.Completion" ,methodName = "dispatch_auto_complete" ))
		comps = []
	
	haxe_Log.trace("do log info", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 92 ,className = "hxsublime.completion.Completion" ,methodName = "dispatch_auto_complete" ))
	hxsublime_completion_Base_Completion.log_completion_info(start_time, python_lib_Time.time(), comps)
	return comps
	
hxsublime_completion_Base_Completion.dispatch_auto_complete = Completion_statics_dispatch_auto_complete
def Completion_statics_log_completion_info(start_time,end_time,comps):
	run_time = end_time - start_time
	haxe_Log.trace("on_query_completion time: " + Std.string(run_time), _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 101 ,className = "hxsublime.completion.Completion" ,methodName = "log_completion_info" ))
	haxe_Log.trace("number of completions: " + Std.string(__builtin__.len(comps)), _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 102 ,className = "hxsublime.completion.Completion" ,methodName = "log_completion_info" ))
	
hxsublime_completion_Base_Completion.log_completion_info = Completion_statics_log_completion_info


hxsublime_completion_Base_Completion._hx_class = hxsublime_completion_Base_Completion
hxsublime_completion_Base_Completion._hx_class_name = "hxsublime.completion.Completion"
_hx_classes['hxsublime.completion.Completion'] = hxsublime_completion_Base_Completion
hxsublime_completion_Base_Completion._hx_fields = []
hxsublime_completion_Base_Completion._hx_props = []
hxsublime_completion_Base_Completion._hx_methods = []
hxsublime_completion_Base_Completion._hx_statics = ["get_completion_scopes","get_completion_offset","can_run_completion","is_supported_scope","empty_handler","get_auto_complete_handler","dispatch_auto_complete","log_completion_info"]
hxsublime_completion_Base_Completion._hx_interfaces = []

# print hxsublime.completion.hx.Base.Base
class hxsublime_completion_hx_Base:

	pass




def Base_statics_trigger_completion(view,options,show_top_level_snippets = False):
	if show_top_level_snippets is None:
		show_top_level_snippets = False
	
	def _hx_local_0():
		project = hxsublime_project_Base_Projects.current_project(view)
		if not project.has_build():
			project.extract_build_args(view, False)
		
		if project.has_build():
			project.completion_context.set_trigger(view, options)
			def _hx_local_1():
				x = _Hx_AnonObject(api_completions_only = not show_top_level_snippets ,disable_auto_insert = True ,next_completion_if_showing = True ,auto_complete_commit_on_tab = True )
				def _hx_local_3():
					def _hx_local_2():
						d = python_lib_Types_Dict()
						_g = 0
						_g1 = Reflect.fields(x)
						while _g < len(_g1):
							f = _g1[_g]
							_g = _g + 1
							val = None
							v = None
							try:
								v = __builtin__.getattr(x, f)
							except Exception as _hx_e:
								_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
								if True:
									e = _hx_e1
									None
								else:
									raise _hx_e
							val = v
							
							python_lib_Types_DictImpl.set(d, f, val)
							
						
						
						return d
					
					return _hx_local_2()
				
				return _hx_local_3()
			
			view.run_command("auto_complete", _hx_local_1())
		
		else:
			project.extract_build_args(view, True)
	
	run = _hx_local_0
	view.run_command("hide_auto_complete")
	sublime_Sublime.set_timeout(run, 0)
	
hxsublime_completion_hx_Base.trigger_completion = Base_statics_trigger_completion
def Base_statics_get_available_async_completions(comp_result,view):
	ctx = comp_result.ctx
	has_results = comp_result.has_results()
	discard_results = not has_results and ctx.options.types().has_hint()
	if discard_results:
		return hxsublime_completion_hx_Base.cancel_completion(view)
	else:
		return hxsublime_completion_hx_Base.combine_hints_and_comps(comp_result)
	
hxsublime_completion_hx_Base.get_available_async_completions = Base_statics_get_available_async_completions
def Base_statics_completion_result_with_smart_snippets(view,comps,result,options):
	use_snippets = hxsublime_Settings.smart_snippets(view)
	prefix_is_whitespace = hxsublime_tools_StringTools.isWhitespaceOrEmpty(result.ctx.prefix)
	has_one_hint = options.types().has_hint() and __builtin__.len(result.hints) == 1
	same_cursor_pos = hxsublime_tools_ViewTools.getFirstCursorPos(view) == result.ctx.view_pos
	line_after_offset = None
	s = result.ctx.line_after_offset()
	line_after_offset = s.strip(None)
	
	really_insert = None
	def _hx_local_2():
		def _hx_local_1():
			def _hx_local_0():
				str = line_after_offset[0]
				return "),".find(str)
			
			return _hx_local_0() > -1
		
		return __builtin__.len(line_after_offset) == 0 or _hx_local_1()
	
	really_insert = _hx_local_2()
	if really_insert and prefix_is_whitespace and use_snippets and has_one_hint and same_cursor_pos:
		only_hint = comps[0]
		hxsublime_tools_ViewTools.insertSnippet(view, only_hint[1])
		comps = hxsublime_completion_hx_Base.cancel_completion(view)
	
	
	return comps
	
hxsublime_completion_hx_Base.completion_result_with_smart_snippets = Base_statics_completion_result_with_smart_snippets
def Base_statics_auto_complete(project,view,offset,prefix):
	haxe_Log.trace("run auto_complete", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 103 ,className = "hxsublime.completion.hx.Base" ,methodName = "auto_complete" ))
	options = project.completion_context.get_and_delete_trigger(view)
	res = None
	if options is not None and options.async_trigger():
		haxe_Log.trace("run auto_complete 1", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 110 ,className = "hxsublime.completion.hx.Base" ,methodName = "auto_complete" ))
		async_result = project.completion_context.get_and_delete_async(view)
		use_async_results = async_result is not None and async_result.has_results()
		if use_async_results:
			haxe_Log.trace("run auto_complete 2", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 115 ,className = "hxsublime.completion.hx.Base" ,methodName = "auto_complete" ))
			res = hxsublime_completion_hx_Base.get_available_async_completions(async_result, view)
			res = hxsublime_completion_hx_Base.completion_result_with_smart_snippets(view, res, async_result, options)
			haxe_Log.trace(res, _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 118 ,className = "hxsublime.completion.hx.Base" ,methodName = "auto_complete" ))
		
		else:
			haxe_Log.trace("run auto_complete 3", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 122 ,className = "hxsublime.completion.hx.Base" ,methodName = "auto_complete" ))
			res = hxsublime_completion_hx_Base.cancel_completion(view)
		
	
	else:
		haxe_Log.trace("create comps", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 127 ,className = "hxsublime.completion.hx.Base" ,methodName = "auto_complete" ))
		res = hxsublime_completion_hx_Base.create_new_completions(project, view, offset, options, prefix)
		haxe_Log.trace("after create comps", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 130 ,className = "hxsublime.completion.hx.Base" ,methodName = "auto_complete" ))
	
	return res
	
hxsublime_completion_hx_Base.auto_complete = Base_statics_auto_complete
def Base_statics_create_new_completions(project,view,offset,options,prefix):
	cache = project.completion_context.current
	haxe_Log.trace("------- COMPLETION START -----------", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 142 ,className = "hxsublime.completion.hx.Base" ,methodName = "create_new_completions" ))
	ctx = hxsublime_completion_hx_Base.create_completion_context(project, view, offset, options, prefix)
	res = None
	haxe_Log.trace("MANUAL COMPLETION: " + Std.string(ctx.options.manual_completion), _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 148 ,className = "hxsublime.completion.hx.Base" ,methodName = "create_new_completions" ))
	if hxsublime_completion_hx_Base.is_equivalent_completion_already_running(ctx):
		haxe_Log.trace("create_new_completions9", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 155 ,className = "hxsublime.completion.hx.Base" ,methodName = "create_new_completions" ))
		haxe_Log.trace("cancel completion, same is running", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 156 ,className = "hxsublime.completion.hx.Base" ,methodName = "create_new_completions" ))
		res = hxsublime_completion_hx_Base.cancel_completion(ctx.view)
	
	elif not ctx.options.manual_completion():
		haxe_Log.trace("create_new_completions7", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 160 ,className = "hxsublime.completion.hx.Base" ,methodName = "create_new_completions" ))
		hxsublime_completion_hx_Base.trigger_manual_completion(ctx.view, ctx.options.copy_as_manual())
		res = hxsublime_completion_hx_Base.cancel_completion(ctx.view)
	
	elif hxsublime_completion_hx_Base.is_after_int_iterator(ctx.src(), ctx.offset):
		haxe_Log.trace("create_new_completions8", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 165 ,className = "hxsublime.completion.hx.Base" ,methodName = "create_new_completions" ))
		res = hxsublime_completion_hx_Base.cancel_completion(ctx.view)
	
	elif hxsublime_completion_hx_Base.is_iterator_completion(ctx.src(), ctx.offset):
		haxe_Log.trace("create_new_completions10", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 169 ,className = "hxsublime.completion.hx.Base" ,methodName = "create_new_completions" ))
		haxe_Log.trace("iterator completion", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 170 ,className = "hxsublime.completion.hx.Base" ,methodName = "create_new_completions" ))
		res = [(".\tint iterator", "..")]
	
	else:
		haxe_Log.trace("create_new_completions11", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 174 ,className = "hxsublime.completion.hx.Base" ,methodName = "create_new_completions" ))
		if hxsublime_completion_hx_Base.is_hint_completion(ctx):
			haxe_Log.trace("ADD HINT", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 176 ,className = "hxsublime.completion.hx.Base" ,methodName = "create_new_completions" ))
			ctx.options.types().add_hint()
		
		
		is_directly_after_control_struct = ctx.complete_char_is_after_control_struct()
		only_top_level = ctx.is_new() or is_directly_after_control_struct
		haxe_Log.trace("only_top_level: " + Std.string(only_top_level), _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 185 ,className = "hxsublime.completion.hx.Base" ,methodName = "create_new_completions" ))
		if only_top_level:
			res = hxsublime_completion_hx_Base.get_toplevel_completions(ctx)
		else:
			last_ctx = cache.input
			if hxsublime_completion_hx_Base.use_completion_cache(ctx, last_ctx):
				haxe_Log.trace("USE COMPLETION CACHE", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 197 ,className = "hxsublime.completion.hx.Base" ,methodName = "create_new_completions" ))
				out = cache.output
				hxsublime_completion_hx_Base.update_completion_cache(cache, out)
				project.completion_context.add_completion_result(out)
				res = hxsublime_completion_hx_Base.cancel_completion(view)
				hxsublime_completion_hx_Base.trigger_async_completion(view, ctx.options, out.show_top_level_snippets())
			
			elif hxsublime_completion_hx_Base.supported_compiler_completion_char(ctx.complete_char()):
				haxe_Log.trace("supported char", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 208 ,className = "hxsublime.completion.hx.Base" ,methodName = "create_new_completions" ))
				comp_build = hxsublime_completion_hx_Base.create_completion_build(ctx)
				if comp_build is not None:
					def _hx_local_0(out,err):
						hxsublime_completion_hx_Base.completion_finished(ctx, comp_build, out, err)
					hxsublime_completion_hx_Base.run_compiler_completion(comp_build, _hx_local_0)
				
				else:
					haxe_Log.trace("couldn't create temp path && files which are neccessary for completion", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 214 ,className = "hxsublime.completion.hx.Base" ,methodName = "create_new_completions" ))
				res = hxsublime_completion_hx_Base.cancel_completion(view, True)
			
			else:
				haxe_Log.trace("whatever", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 221 ,className = "hxsublime.completion.hx.Base" ,methodName = "create_new_completions" ))
				def _hx_local_1():
					return hxsublime_completion_hx_Base.get_toplevel_completions(ctx)
				comp_result = hxsublime_completion_hx_Types_CompletionResult.empty_result(ctx, _hx_local_1)
				hxsublime_completion_hx_Base.update_completion_cache(cache, comp_result)
				project.completion_context.add_completion_result(comp_result)
				res = hxsublime_completion_hx_Base.cancel_completion(view)
				hxsublime_completion_hx_Base.trigger_async_completion(view, ctx.options, comp_result.show_top_level_snippets())
			
		
	
	return res
	
hxsublime_completion_hx_Base.create_new_completions = Base_statics_create_new_completions
def Base_statics_create_completion_build(ctx):
	tmp_src = ctx.temp_completion_src()
	r = hxsublime_Temp.create_temp_path_and_file(ctx.build(), ctx.orig_file(), tmp_src)
	temp_path = r[0]
	temp_file = r[1]
	temp_creation_success = temp_path is not None and temp_file is not None
	def _hx_local_0():
		comp_build = hxsublime_completion_hx_Types_CompletionBuild(ctx, temp_path, temp_file)
		build = comp_build.build
		display = comp_build.display()
		macro_completion = ctx.options.macro_completion()
		build.set_auto_completion(display, macro_completion)
		if ctx.settings.show_completion_times(comp_build.ctx.view):
			build.set_times()
		
		return comp_build
	
	mk_build = _hx_local_0
	if temp_creation_success:
		return mk_build()
	else:
		return None
	
hxsublime_completion_hx_Base.create_completion_build = Base_statics_create_completion_build
def Base_statics_run_compiler_completion(comp_build,callback):
	start_time = python_lib_Time.time()
	ctx = comp_build.ctx
	project = ctx.project
	build = comp_build.build
	view = ctx.view
	async = ctx.settings.is_async_completion()
	def _hx_local_0(out,err):
		def _hx_local_1():
			run_time = python_lib_Time.time() - start_time
			haxe_Log.trace("completion time: " + Std.string(run_time), _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 276 ,className = "hxsublime.completion.hx.Base" ,methodName = "run_compiler_completion" ))
			hxsublime_Temp.remove_path(comp_build.temp_path)
			callback(out, err)
		
		run = _hx_local_1
		project.completion_context.run_if_still_up_to_date(ctx.id, run)
	
	in_main = _hx_local_0
	def _hx_local_2(out1,err1):
		def _hx_local_3():
			in_main(out1, err1)
		sublime_Sublime.set_timeout(_hx_local_3, 2)
	
	on_result = _hx_local_2
	project.completion_context.set_new_completion(ctx)
	build.run(project, view, async, on_result)
	
hxsublime_completion_hx_Base.run_compiler_completion = Base_statics_run_compiler_completion
def Base_statics_completion_finished(ctx,comp_build,out,err):
	ctx1 = comp_build.ctx
	temp_file = comp_build.temp_file
	cache = comp_build.cache
	project = ctx1.project
	view = ctx1.view
	def _hx_local_0():
		return hxsublime_completion_hx_Base.get_toplevel_completions(ctx1)
	comp_result = hxsublime_completion_hx_Base.output_to_result(ctx1, temp_file, err, out, _hx_local_0)
	has_results = comp_result.has_results()
	if has_results:
		hxsublime_completion_hx_Base.update_completion_cache(cache, comp_result)
		project.completion_context.add_completion_result(comp_result)
		show_top_level_snippets = comp_result.show_top_level_snippets()
		hxsublime_completion_hx_Base.trigger_async_completion(view, ctx1.options, show_top_level_snippets)
	
	else:
		haxe_Log.trace("ignore background completion on finished", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 318 ,className = "hxsublime.completion.hx.Base" ,methodName = "completion_finished" ))
	
hxsublime_completion_hx_Base.completion_finished = Base_statics_completion_finished
def Base_statics_hints_to_sublime_completions(hints):
	def _hx_local_0(h):
		hint_is_only_type = __builtin__.len(h) == 1
		res = None
		if hint_is_only_type:
			res = (h[0] + " - No Completion", "${}")
		else:
			function_has_no_params = __builtin__.len(h) == 2 and h[0] == "Void"
			insert = None
			show = None
			if function_has_no_params:
				insert = ")"
				show = "Void"
			
			else:
				def _hx_local_1(p):
					_this = p.split("}")
					return "\\}".join(_this)
				
				param_escape = _hx_local_1
				last_index = __builtin__.len(h) - 1
				params = h[0:last_index]
				show = ", ".join(params)
				if hxsublime_Settings.smart_snippets_just_current():
					first = param_escape(params[0])
					if __builtin__.len(params) == 1:
						insert = "${1:" + first + "})${0}"
					else:
						insert = "${0:" + first + "}"
				
				else:
					def _hx_local_2(list_index):
						return Std.string(list_index + 1)
					get_snippet_index = _hx_local_2
					def _hx_local_3(param,index):
						return "${" + get_snippet_index(index) + ":" + param_escape(param) + "}"
					param_snippet = _hx_local_3
					snippet_list = None
					_g = []
					_g2 = 0
					_g1 = __builtin__.len(params)
					while _g2 < _g1:
						def _hx_local_4():
							nonlocal _g2
							_hx_r = _g2
							_g2 = _g2 + 1
							return _hx_r
							
						
						index = _hx_local_4()
						x = param_snippet(params[index], index)
						_g.append(x)
						__builtin__.len(_g)
						
					
					
					snippet_list = _g
					
					insert = ",".join(snippet_list) + ")${0}"
				
			
			res = (show, insert)
		
		return res
	
	make_hint_comp = _hx_local_0
	_g = []
	_g1 = 0
	while _g1 < len(hints):
		h = hints[_g1]
		_g1 = _g1 + 1
		x = make_hint_comp(h)
		_g.append(x)
		__builtin__.len(_g)
		
	
	
	return _g
	
	
hxsublime_completion_hx_Base.hints_to_sublime_completions = Base_statics_hints_to_sublime_completions
def Base_statics_combine_hints_and_comps(comp_result):
	all_comps = hxsublime_completion_hx_Base.hints_to_sublime_completions(comp_result.hints)
	if not comp_result.ctx.options.types().has_hint() or __builtin__.len(comp_result.hints) == 0:
		haxe_Log.trace("TAKE TOP LEVEL COMPS", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 402 ,className = "hxsublime.completion.hx.Base" ,methodName = "combine_hints_and_comps" ))
		x = comp_result.all_comps()
		all_comps.extend(x)
		
	
	elif __builtin__.len(comp_result.hints) == 1:
		sublime_Sublime.status_message("signature: " + "->".join(comp_result.hints[0]))
	
	return all_comps
	
hxsublime_completion_hx_Base.combine_hints_and_comps = Base_statics_combine_hints_and_comps
def Base_statics_is_iterator_completion(src,offset):
	o = offset
	s = src
	return o > 3 and s[o] == "\n" and s[o - 1] == "." and s[o - 2] == "." and s[o - 3] != "."
	
hxsublime_completion_hx_Base.is_iterator_completion = Base_statics_is_iterator_completion
def Base_statics_is_after_int_iterator(src,offset):
	o = offset
	s = src
	return o > 3 and s[o] == "\n" and s[o - 1] == "." and s[o - 2] == "." and s[o - 3] == "."
	
hxsublime_completion_hx_Base.is_after_int_iterator = Base_statics_is_after_int_iterator
def Base_statics_is_hint_completion(ctx):
	whitespace_re = python_lib_Re.compile("^\\s*$")
	def _hx_local_3():
		def _hx_local_2():
			def _hx_local_1():
				def _hx_local_0():
					str = ctx.complete_char()
					return "(,".find(str)
				
				return _hx_local_0() > -1
			
			return _hx_local_1() and python_lib_Re.match(whitespace_re, ctx.prefix) is not None
		
		return _hx_local_2()
	
	return _hx_local_3()
	
hxsublime_completion_hx_Base.is_hint_completion = Base_statics_is_hint_completion
def Base_statics_is_equivalent_completion_already_running(ctx):
	return ctx.project.completion_context.is_equivalent_completion_already_running(ctx)
hxsublime_completion_hx_Base.is_equivalent_completion_already_running = Base_statics_is_equivalent_completion_already_running
def Base_statics_should_include_top_level_completion(ctx):
	haxe_Log.trace("complete Char: '" + ctx.complete_char() + "'", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 445 ,className = "hxsublime.completion.hx.Base" ,methodName = "should_include_top_level_completion" ))
	toplevel_complete = None
	def _hx_local_3():
		def _hx_local_2():
			def _hx_local_1():
				def _hx_local_0():
					str = ctx.complete_char()
					return ":(,{;})".find(str)
				
				return _hx_local_0() > -1
			
			return _hx_local_1() or ctx.in_control_struct()
		
		return _hx_local_2() or ctx.is_new()
	
	toplevel_complete = _hx_local_3()
	haxe_Log.trace("should include: " + Std.string(toplevel_complete), _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 448 ,className = "hxsublime.completion.hx.Base" ,methodName = "should_include_top_level_completion" ))
	return toplevel_complete
	
hxsublime_completion_hx_Base.should_include_top_level_completion = Base_statics_should_include_top_level_completion
def Base_statics_get_toplevel_completions(ctx):
	haxe_Log.trace("get top level completions", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 456 ,className = "hxsublime.completion.hx.Base" ,methodName = "get_toplevel_completions" ))
	comps = None
	if hxsublime_completion_hx_Base.should_include_top_level_completion(ctx):
		comps = hxsublime_completion_hx_Toplevel_TopLevel.get_toplevel_completion_filtered(ctx)
	else:
		haxe_Log.trace("should not", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 462 ,className = "hxsublime.completion.hx.Base" ,methodName = "get_toplevel_completions" ))
		comps = []
	
	return comps
	
hxsublime_completion_hx_Base.get_toplevel_completions = Base_statics_get_toplevel_completions
def Base_statics_create_completion_context(project,view,offset,options,prefix):
	haxe_Log.trace("OPTIONS:" + Std.string(options), _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 475 ,className = "hxsublime.completion.hx.Base" ,methodName = "create_completion_context" ))
	if options is None:
		options = hxsublime_completion_hx_Types_CompletionOptions(2)
	
	haxe_Log.trace(options, _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 481 ,className = "hxsublime.completion.hx.Base" ,methodName = "create_completion_context" ))
	settings = hxsublime_completion_hx_Types_CompletionSettings(hxsublime_Settings)
	ctx = hxsublime_completion_hx_Types_CompletionContext(view, project, offset, options, settings, prefix)
	return ctx
	
hxsublime_completion_hx_Base.create_completion_context = Base_statics_create_completion_context
def Base_statics_update_completion_cache(cache,comp_result):
	cache.output = comp_result
	cache.input = comp_result.ctx
	
hxsublime_completion_hx_Base.update_completion_cache = Base_statics_update_completion_cache
def Base_statics_log_completion_status(status,comps,hints):
	if status != "":
		if comps.length > 0 or hints.length > 0:
			haxe_Log.trace(status, _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 498 ,className = "hxsublime.completion.hx.Base" ,methodName = "log_completion_status" ))
		else:
			hxsublime_panel_Base_Panels.default_panel().writeln(status)
	
hxsublime_completion_hx_Base.log_completion_status = Base_statics_log_completion_status
def Base_statics_output_to_result(ctx,temp_file,err,ret,retrieve_tl_comps):
	r = hxsublime_compiler_Output.get_completion_output(temp_file, ctx.orig_file(), err, ctx.commas())
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
	
	ctx.project.completion_context.set_errors(errors)
	hxsublime_completion_hx_Base.highlight_errors(errors, ctx.view)
	return hxsublime_completion_hx_Types_CompletionResult(ret, comps2, status, hints, ctx, retrieve_tl_comps)
	
hxsublime_completion_hx_Base.output_to_result = Base_statics_output_to_result
def Base_statics_use_completion_cache(last_input,current_input):
	return last_input.eq(current_input)
hxsublime_completion_hx_Base.use_completion_cache = Base_statics_use_completion_cache
def Base_statics_supported_compiler_completion_char(char):
	return "(.,".find(char) > -1
hxsublime_completion_hx_Base.supported_compiler_completion_char = Base_statics_supported_compiler_completion_char
def Base_statics_highlight_errors(errors,view):
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
		
		hxsublime_panel_Base_Panels.default_panel().status("Error", e.file + ":" + Std.string(l) + ": characters " + Std.string(left) + "-" + Std.string(right) + ": " + e.message)
	
	
	view.add_regions("haxe-error", regions, "invalid", "dot")
	
hxsublime_completion_hx_Base.highlight_errors = Base_statics_highlight_errors
def Base_statics_cancel_completion(view,hide_complete = True):
	if hide_complete is None:
		hide_complete = True
	
	if hide_complete:
		view.run_command("hide_auto_complete")
	
	return [("  ...  ", "")]
	
hxsublime_completion_hx_Base.cancel_completion = Base_statics_cancel_completion
def Base_statics_trigger_async_completion(view,options,show_top_level_snippets = False):
	if show_top_level_snippets is None:
		show_top_level_snippets = False
	
	async_options = options.copy_as_async()
	def _hx_local_0():
		hxsublime_completion_hx_Base.trigger_completion(view, async_options, show_top_level_snippets)
	run_complete = _hx_local_0
	sublime_Sublime.set_timeout(run_complete, 2)
	
hxsublime_completion_hx_Base.trigger_async_completion = Base_statics_trigger_async_completion
def Base_statics_trigger_manual_completion(view,options):
	hint = options.types().has_hint()
	macroComp = options.macro_completion()
	def _hx_local_0():
		if hint and macroComp:
			view.run_command("haxe_hint_display_macro_completion")
		elif hint:
			view.run_command("haxe_hint_display_completion")
		elif macroComp:
			view.run_command("haxe_display_macro_completion")
		else:
			view.run_command("haxe_display_completion")
	run_complete = _hx_local_0
	sublime_Sublime.set_timeout(run_complete, 2)
	
hxsublime_completion_hx_Base.trigger_manual_completion = Base_statics_trigger_manual_completion


hxsublime_completion_hx_Base._hx_class = hxsublime_completion_hx_Base
hxsublime_completion_hx_Base._hx_class_name = "hxsublime.completion.hx.Base"
_hx_classes['hxsublime.completion.hx.Base'] = hxsublime_completion_hx_Base
hxsublime_completion_hx_Base._hx_fields = []
hxsublime_completion_hx_Base._hx_props = []
hxsublime_completion_hx_Base._hx_methods = []
hxsublime_completion_hx_Base._hx_statics = ["trigger_completion","get_available_async_completions","completion_result_with_smart_snippets","auto_complete","create_new_completions","create_completion_build","run_compiler_completion","completion_finished","hints_to_sublime_completions","combine_hints_and_comps","is_iterator_completion","is_after_int_iterator","is_hint_completion","is_equivalent_completion_already_running","should_include_top_level_completion","get_toplevel_completions","create_completion_context","update_completion_cache","log_completion_status","output_to_result","use_completion_cache","supported_compiler_completion_char","highlight_errors","cancel_completion","trigger_async_completion","trigger_manual_completion"]
hxsublime_completion_hx_Base._hx_interfaces = []

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

# print hxsublime.completion.hx.Toplevel.TopLevel
class hxsublime_completion_hx_Toplevel_TopLevel:

	pass




hxsublime_completion_hx_Toplevel_TopLevel.TOP_LEVEL_KEYWORDS = [("trace\ttoplevel", "trace"), ("this\ttoplevel", "this"), ("super\ttoplevel", "super")]
def TopLevel_statics_get_toplevel_keywords(ctx):
	if ctx.is_new():
		return []
	else:
		return hxsublime_completion_hx_Toplevel_TopLevel.TOP_LEVEL_KEYWORDS
hxsublime_completion_hx_Toplevel_TopLevel.get_toplevel_keywords = TopLevel_statics_get_toplevel_keywords
def TopLevel_statics_get_build_target(ctx):
	if ctx.options.macro_completion():
		return "neko"
	else:
		return ctx.build().target().plattform
hxsublime_completion_hx_Toplevel_TopLevel.get_build_target = TopLevel_statics_get_build_target
def TopLevel_statics_get_local_vars(ctx):
	comps = []
	def _hx_local_0():
		p = hxsublime_tools_HxSrcTools_Regex.variables.finditer(ctx.src())
		return python_Lib_HaxeIterator(p)
	
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
	
hxsublime_completion_hx_Toplevel_TopLevel.get_local_vars = TopLevel_statics_get_local_vars
def TopLevel_statics_get_local_functions(ctx):
	comps = []
	def _hx_local_0():
		p = hxsublime_tools_HxSrcTools_Regex.named_functions.finditer(ctx.src())
		return python_Lib_HaxeIterator(p)
	
	_it = _hx_local_0()
	while _it.hasNext():
		i = _it.next()
		f = i.group(1)
		if f != "new":
			x = (f + "\tfunction", f)
			comps.append(x)
			__builtin__.len(comps)
			
		
		
		
	
	
	return comps
	
hxsublime_completion_hx_Toplevel_TopLevel.get_local_functions = TopLevel_statics_get_local_functions
def TopLevel_statics_get_local_function_params(ctx):
	comps = []
	_g = 0
	_g1 = None
	string = ctx.src()
	_g1 = python_lib_Re_RegexHelper.findallDynamic(hxsublime_tools_HxSrcTools_Regex.function_params, string, None, None)
	
	while _g < len(_g1):
		params_text = _g1[_g]
		_g = _g + 1
		cleaned_params_text = python_lib_Re.sub(hxsublime_tools_HxSrcTools_Regex.param_default, "", params_text)
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
	
hxsublime_completion_hx_Toplevel_TopLevel.get_local_function_params = TopLevel_statics_get_local_function_params
def TopLevel_statics_get_local_vars_and_functions(ctx):
	comps = []
	x = hxsublime_completion_hx_Toplevel_TopLevel.get_local_vars(ctx)
	comps.extend(x)
	
	x = hxsublime_completion_hx_Toplevel_TopLevel.get_local_functions(ctx)
	comps.extend(x)
	
	x = hxsublime_completion_hx_Toplevel_TopLevel.get_local_function_params(ctx)
	comps.extend(x)
	
	return comps
	
hxsublime_completion_hx_Toplevel_TopLevel.get_local_vars_and_functions = TopLevel_statics_get_local_vars_and_functions
def TopLevel_statics_get_imports(ctx):
	imports = None
	string = ctx.src()
	imports = python_lib_Re_RegexHelper.findallDynamic(hxsublime_tools_HxSrcTools_Regex.import_line, string, None, None)
	
	imported = []
	_g = 0
	while _g < len(imports):
		i = imports[_g]
		_g = _g + 1
		imp = i[1]
		imported.append(imp)
		__builtin__.len(imported)
		
	
	
	return imported
	
hxsublime_completion_hx_Toplevel_TopLevel.get_imports = TopLevel_statics_get_imports
def TopLevel_statics_get_usings(ctx):
	usings = None
	string = ctx.src()
	usings = python_lib_Re_RegexHelper.findallDynamic(hxsublime_tools_HxSrcTools_Regex.using_line, string, None, None)
	
	used = []
	_g = 0
	while _g < len(usings):
		i = usings[_g]
		_g = _g + 1
		imp = i[1]
		used.append(imp)
		__builtin__.len(used)
		
	
	
	return used
	
hxsublime_completion_hx_Toplevel_TopLevel.get_usings = TopLevel_statics_get_usings
def TopLevel_statics_get_imports_and_usings(ctx):
	res = hxsublime_completion_hx_Toplevel_TopLevel.get_imports(ctx)
	a = hxsublime_completion_hx_Toplevel_TopLevel.get_usings(ctx)
	res = res + a
	
	return res
	
hxsublime_completion_hx_Toplevel_TopLevel.get_imports_and_usings = TopLevel_statics_get_imports_and_usings
def TopLevel_statics_haxe_type_as_completion(type):
	insert = type.full_pack_with_optional_module_type_and_enum_value
	display = type.type_name_with_optional_enum_value
	display = display + "\t" + type.get_type_hint
	return (display, insert)
	
hxsublime_completion_hx_Toplevel_TopLevel.haxe_type_as_completion = TopLevel_statics_haxe_type_as_completion
def TopLevel_statics_get_type_comps(ctx,bundle,imported):
	build_target = hxsublime_completion_hx_Toplevel_TopLevel.get_build_target(ctx)
	comps = []
	_g = 0
	_g1 = bundle.all_types()
	while _g < len(_g1):
		t = _g1[_g]
		_g = _g + 1
		if ctx.build().is_type_available(t):
			snippets = t.to_snippets(imported, ctx.orig_file())
			comps = comps + snippets
		
		
	
	
	_g = 0
	_g1 = bundle.packs()
	while _g < len(_g1):
		p = _g1[_g]
		_g = _g + 1
		if ctx.build().is_pack_available(p):
			cm = (p + "\tpackage", p)
			comps.append(cm)
			__builtin__.len(comps)
			
		
		
	
	
	return comps
	
hxsublime_completion_hx_Toplevel_TopLevel.get_type_comps = TopLevel_statics_get_type_comps
def TopLevel_statics_get_toplevel_completion(ctx):
	start_time = python_lib_Time.time()
	comps = []
	if not ctx.is_new():
		x = hxsublime_completion_hx_Toplevel_TopLevel.get_toplevel_keywords(ctx)
		comps.extend(x)
		
		x = hxsublime_completion_hx_Toplevel_TopLevel.get_local_vars_and_functions(ctx)
		comps.extend(x)
		
	
	
	imported = hxsublime_completion_hx_Toplevel_TopLevel.get_imports_and_usings(ctx)
	run_time1 = python_lib_Time.time() - start_time
	build_bundle = ctx.build().get_types()
	run_time2 = python_lib_Time.time() - start_time
	std_bundle = ctx.build().std_bundle()
	def _hx_local_0(t):
		return not t.is_private or t.file() == ctx.orig_file()
	filter_privates = _hx_local_0
	merged_bundle = std_bundle.merge(build_bundle).filter(filter_privates)
	run_time3 = python_lib_Time.time() - start_time
	comps1 = hxsublime_completion_hx_Toplevel_TopLevel.get_type_comps(ctx, merged_bundle, imported)
	run_time4 = python_lib_Time.time() - start_time
	comps = comps + comps1
	run_time = python_lib_Time.time() - start_time
	haxe_Log.trace("TOP LEVEL COMPLETION TIME1:" + Std.string(run_time1), _Hx_AnonObject(fileName = "Toplevel.hx" ,lineNumber = 206 ,className = "hxsublime.completion.hx.TopLevel" ,methodName = "get_toplevel_completion" ))
	haxe_Log.trace("TOP LEVEL COMPLETION TIME2:" + Std.string(run_time2), _Hx_AnonObject(fileName = "Toplevel.hx" ,lineNumber = 207 ,className = "hxsublime.completion.hx.TopLevel" ,methodName = "get_toplevel_completion" ))
	haxe_Log.trace("TOP LEVEL COMPLETION TIME3:" + Std.string(run_time3), _Hx_AnonObject(fileName = "Toplevel.hx" ,lineNumber = 208 ,className = "hxsublime.completion.hx.TopLevel" ,methodName = "get_toplevel_completion" ))
	haxe_Log.trace("TOP LEVEL COMPLETION TIME4:" + Std.string(run_time4), _Hx_AnonObject(fileName = "Toplevel.hx" ,lineNumber = 209 ,className = "hxsublime.completion.hx.TopLevel" ,methodName = "get_toplevel_completion" ))
	haxe_Log.trace("TOP LEVEL COMPLETION TIME END:" + Std.string(run_time), _Hx_AnonObject(fileName = "Toplevel.hx" ,lineNumber = 210 ,className = "hxsublime.completion.hx.TopLevel" ,methodName = "get_toplevel_completion" ))
	return comps
	
hxsublime_completion_hx_Toplevel_TopLevel.get_toplevel_completion = TopLevel_statics_get_toplevel_completion
def TopLevel_statics_get_toplevel_completion_filtered(ctx):
	comps = hxsublime_completion_hx_Toplevel_TopLevel.get_toplevel_completion(ctx)
	return hxsublime_completion_hx_Toplevel_TopLevel.filter_top_level_completions(ctx.offset_char(), comps)
	
hxsublime_completion_hx_Toplevel_TopLevel.get_toplevel_completion_filtered = TopLevel_statics_get_toplevel_completion_filtered
def TopLevel_statics_filter_top_level_completions(offset_char,all_comps):
	comps = []
	is_lower = "abcdefghijklmnopqrstuvwxyz".find(offset_char) >= 0
	is_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(offset_char) >= 0
	is_digit = "0123456789".find(offset_char) >= 0
	is_special = "$_#".find(offset_char) >= 0
	if is_lower or is_upper or is_digit or is_special:
		offset_upper = offset_char.upper()
		offset_lower = offset_char.lower()
		_g = 0
		while _g < len(all_comps):
			c = all_comps[_g]
			_g = _g + 1
			id = c[1]
			if id.find(offset_char) >= 0 or is_upper and id.find(offset_lower) >= 0 or is_lower and id.find(offset_upper) >= 0:
				comps.append(c)
				__builtin__.len(comps)
			
			
		
		
	
	else:
		comps = __builtin__.list(all_comps)
	haxe_Log.trace("number of top level completions (all: " + Std.string(__builtin__.len(all_comps)) + ", filtered: " + Std.string(__builtin__.len(comps)) + ")", _Hx_AnonObject(fileName = "Toplevel.hx" ,lineNumber = 253 ,className = "hxsublime.completion.hx.TopLevel" ,methodName = "filter_top_level_completions" ))
	return comps
	
hxsublime_completion_hx_Toplevel_TopLevel.filter_top_level_completions = TopLevel_statics_filter_top_level_completions


hxsublime_completion_hx_Toplevel_TopLevel._hx_class = hxsublime_completion_hx_Toplevel_TopLevel
hxsublime_completion_hx_Toplevel_TopLevel._hx_class_name = "hxsublime.completion.hx.TopLevel"
_hx_classes['hxsublime.completion.hx.TopLevel'] = hxsublime_completion_hx_Toplevel_TopLevel
hxsublime_completion_hx_Toplevel_TopLevel._hx_fields = []
hxsublime_completion_hx_Toplevel_TopLevel._hx_props = []
hxsublime_completion_hx_Toplevel_TopLevel._hx_methods = []
hxsublime_completion_hx_Toplevel_TopLevel._hx_statics = ["TOP_LEVEL_KEYWORDS","get_toplevel_keywords","get_build_target","get_local_vars","get_local_functions","get_local_function_params","get_local_vars_and_functions","get_imports","get_usings","get_imports_and_usings","haxe_type_as_completion","get_type_comps","get_toplevel_completion","get_toplevel_completion_filtered","filter_top_level_completions"]
hxsublime_completion_hx_Toplevel_TopLevel._hx_interfaces = []

# print hxsublime.completion.hx.Types.CompletionResult
class hxsublime_completion_hx_Types_CompletionResult:


	def __init__(self,ret,comps,status,hints,ctx,retrieve_toplevel_comps):
		self._lazy_toplevel_comps = None
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
	
	# var ret
	# var comps
	# var status
	# var hints
	# var ctx
	# var retrieve_toplevel_comps
	# var _lazy_toplevel_comps
	def _toplevel_comps(self):
		if self._lazy_toplevel_comps is None:
			self._lazy_toplevel_comps = self.retrieve_toplevel_comps()
		
		return self._lazy_toplevel_comps
	

	def has_hints(self):
		return __builtin__.len(self.hints) > 0

	def has_compiler_results(self):
		return __builtin__.len(self.comps) > 0

	def has_results(self):
		def _hx_local_4():
			def _hx_local_3():
				def _hx_local_2():
					def _hx_local_1():
						def _hx_local_0():
							_this = self._toplevel_comps()
							return __builtin__.len(_this)
						
						return _hx_local_0() > 0
					
					return self.requires_toplevel_comps() and _hx_local_1()
				
				return __builtin__.len(self.comps) > 0 or __builtin__.len(self.hints) > 0 or _hx_local_2()
			
			return _hx_local_3()
		
		return _hx_local_4()
	

	def show_top_level_snippets(self):
		req = self.requires_toplevel_comps()
		r = req and not self.ctx.is_new()
		return r
	

	def requires_toplevel_comps(self):
		prefix_is_whitespace = hxsublime_tools_StringTools.isWhitespaceOrEmpty(self.ctx.prefix)
		haxe_Log.trace("prefix_is_whitespace:" + Std.string(prefix_is_whitespace), _Hx_AnonObject(fileName = "Types.hx" ,lineNumber = 101 ,className = "hxsublime.completion.hx.CompletionResult" ,methodName = "requires_toplevel_comps" ))
		haxe_Log.trace("has_hints:" + Std.string(self.has_hints()), _Hx_AnonObject(fileName = "Types.hx" ,lineNumber = 102 ,className = "hxsublime.completion.hx.CompletionResult" ,methodName = "requires_toplevel_comps" ))
		haxe_Log.trace("has_hint:" + Std.string(self.ctx.options.types().has_hint()), _Hx_AnonObject(fileName = "Types.hx" ,lineNumber = 103 ,className = "hxsublime.completion.hx.CompletionResult" ,methodName = "requires_toplevel_comps" ))
		haxe_Log.trace("has_compiler_results:" + Std.string(self.has_compiler_results()), _Hx_AnonObject(fileName = "Types.hx" ,lineNumber = 104 ,className = "hxsublime.completion.hx.CompletionResult" ,methodName = "requires_toplevel_comps" ))
		r = not (prefix_is_whitespace and self.has_hints() and self.ctx.options.types().has_hint() or self.has_compiler_results())
		haxe_Log.trace("requires_toplevel_comps:" + Std.string(r), _Hx_AnonObject(fileName = "Types.hx" ,lineNumber = 106 ,className = "hxsublime.completion.hx.CompletionResult" ,methodName = "requires_toplevel_comps" ))
		return r
	

	def all_comps(self):
		res = []
		if self.requires_toplevel_comps():
			x = self._toplevel_comps()
			res.extend(x)
		
		
		res.extend(self.comps)
		def _hx_local_0(s1,s2):
			if s1[0] < s2[0]:
				return -1
			elif s1[0] > s2[0]:
				return 1
			else:
				return 0
		res.sort(key=python_lib_FuncTools.cmp_to_key(_hx_local_0))
		return res
	





hxsublime_completion_hx_Types_CompletionResult.__meta__ = _Hx_AnonObject(fields = _Hx_AnonObject(_toplevel_comps = _Hx_AnonObject(lazyprop = None ) ) )
def CompletionResult_statics_empty_result(ctx,retrieve_toplevel_comps = None):
	if retrieve_toplevel_comps is None:
		retrieve_toplevel_comps = None
	
	return hxsublime_completion_hx_Types_CompletionResult("", [], "", [], ctx, retrieve_toplevel_comps)
	
hxsublime_completion_hx_Types_CompletionResult.empty_result = CompletionResult_statics_empty_result


hxsublime_completion_hx_Types_CompletionResult._hx_class = hxsublime_completion_hx_Types_CompletionResult
hxsublime_completion_hx_Types_CompletionResult._hx_class_name = "hxsublime.completion.hx.CompletionResult"
_hx_classes['hxsublime.completion.hx.CompletionResult'] = hxsublime_completion_hx_Types_CompletionResult
hxsublime_completion_hx_Types_CompletionResult._hx_fields = ["ret","comps","status","hints","ctx","retrieve_toplevel_comps","_lazy_toplevel_comps"]
hxsublime_completion_hx_Types_CompletionResult._hx_props = []
hxsublime_completion_hx_Types_CompletionResult._hx_methods = ["_toplevel_comps","has_hints","has_compiler_results","has_results","show_top_level_snippets","requires_toplevel_comps","all_comps"]
hxsublime_completion_hx_Types_CompletionResult._hx_statics = ["__meta__","empty_result"]
hxsublime_completion_hx_Types_CompletionResult._hx_interfaces = []

# print hxsublime.completion.hx.Types.CompletionBuild
class hxsublime_completion_hx_Types_CompletionBuild:


	def __init__(self,ctx,temp_path,temp_file):
		self.build = ctx.build().copy()
		self.build.add_classpath(temp_path)
		self.ctx = ctx
		self.temp_path = temp_path
		self.temp_file = temp_file
		self.cache = ctx.project.completion_context.current
	
	# var build
	# var ctx
	# var temp_path
	# var temp_file
	# var cache
	def display(self):
		pos = None
		if not hxsublime_Settings.use_offset_completion():
			pos = "0"
		else:
			pos = Std.string(self.ctx.complete_offset_in_bytes)
		return self.temp_file + "@" + pos
	





hxsublime_completion_hx_Types_CompletionBuild.__meta__ = _Hx_AnonObject(fields = _Hx_AnonObject(display = _Hx_AnonObject(lazyprop = None ) ) )


hxsublime_completion_hx_Types_CompletionBuild._hx_class = hxsublime_completion_hx_Types_CompletionBuild
hxsublime_completion_hx_Types_CompletionBuild._hx_class_name = "hxsublime.completion.hx.CompletionBuild"
_hx_classes['hxsublime.completion.hx.CompletionBuild'] = hxsublime_completion_hx_Types_CompletionBuild
hxsublime_completion_hx_Types_CompletionBuild._hx_fields = ["build","ctx","temp_path","temp_file","cache"]
hxsublime_completion_hx_Types_CompletionBuild._hx_props = []
hxsublime_completion_hx_Types_CompletionBuild._hx_methods = ["display"]
hxsublime_completion_hx_Types_CompletionBuild._hx_statics = ["__meta__"]
hxsublime_completion_hx_Types_CompletionBuild._hx_interfaces = []

# print hxsublime.completion.hx.Types.CompletionOptions
class hxsublime_completion_hx_Types_CompletionOptions:


	def __init__(self,trigger,context = 2,types = 1,toplevel = 4):
		if context is None:
			context = 2
		
		if types is None:
			types = 1
		
		if toplevel is None:
			toplevel = 4
		
		self._types = hxsublime_completion_hx_Types_CompletionTypes(types)
		self._toplevel = hxsublime_completion_hx_Types_TopLevelOptions(toplevel)
		self._context = context
		self._trigger = trigger
	
	# var _types
	# var _toplevel
	# var _context
	# var _trigger
	def copy_as_manual(self):
		return hxsublime_completion_hx_Types_CompletionOptions(1, self._context, self.types().val(), self._toplevel.val())

	def copy_as_async(self):
		return hxsublime_completion_hx_Types_CompletionOptions(3, self._context, self.types().val(), self._toplevel.val())

	def types(self):
		return self._types

	def async_trigger(self):
		return self._trigger == 3

	def manual_completion(self):
		return self._trigger == 1

	def macro_completion(self):
		return self._context == 1

	def regular_completion(self):
		return self._context == 2

	def eq(self,other):
		return self._trigger == other._trigger and self._types.eq(other._types) and self._toplevel.eq(other._toplevel) and self._context == other._context





hxsublime_completion_hx_Types_CompletionOptions.__meta__ = _Hx_AnonObject(fields = _Hx_AnonObject(types = _Hx_AnonObject(property = None ) ,async_trigger = _Hx_AnonObject(lazyprop = None ) ,manual_completion = _Hx_AnonObject(lazyprop = None ) ,macro_completion = _Hx_AnonObject(lazyprop = None ) ,regular_completion = _Hx_AnonObject(lazyprop = None ) ) )


hxsublime_completion_hx_Types_CompletionOptions._hx_class = hxsublime_completion_hx_Types_CompletionOptions
hxsublime_completion_hx_Types_CompletionOptions._hx_class_name = "hxsublime.completion.hx.CompletionOptions"
_hx_classes['hxsublime.completion.hx.CompletionOptions'] = hxsublime_completion_hx_Types_CompletionOptions
hxsublime_completion_hx_Types_CompletionOptions._hx_fields = ["_types","_toplevel","_context","_trigger"]
hxsublime_completion_hx_Types_CompletionOptions._hx_props = []
hxsublime_completion_hx_Types_CompletionOptions._hx_methods = ["copy_as_manual","copy_as_async","types","async_trigger","manual_completion","macro_completion","regular_completion","eq"]
hxsublime_completion_hx_Types_CompletionOptions._hx_statics = ["__meta__"]
hxsublime_completion_hx_Types_CompletionOptions._hx_interfaces = []

# print hxsublime.completion.hx.Types.CompletionTypes
class hxsublime_completion_hx_Types_CompletionTypes:


	def __init__(self,val = 1):
		if val is None:
			val = 1
		
		self._opt = val
	
	# var _opt
	def val(self):
		return self._opt

	def add(self,val):
		self._opt = self._opt | val

	def add_hint(self):
		self._opt = self._opt | 2

	def has_regular(self):
		return (self._opt & 1) > 0

	def has_hint(self):
		return (self._opt & 2) > 0

	def has_toplevel(self):
		return (self._opt & 4) > 0

	def has_toplevel_forced(self):
		return (self._opt & 12) > 0

	def eq(self,other):
		return self._opt == other._opt







hxsublime_completion_hx_Types_CompletionTypes._hx_class = hxsublime_completion_hx_Types_CompletionTypes
hxsublime_completion_hx_Types_CompletionTypes._hx_class_name = "hxsublime.completion.hx.CompletionTypes"
_hx_classes['hxsublime.completion.hx.CompletionTypes'] = hxsublime_completion_hx_Types_CompletionTypes
hxsublime_completion_hx_Types_CompletionTypes._hx_fields = ["_opt"]
hxsublime_completion_hx_Types_CompletionTypes._hx_props = []
hxsublime_completion_hx_Types_CompletionTypes._hx_methods = ["val","add","add_hint","has_regular","has_hint","has_toplevel","has_toplevel_forced","eq"]
hxsublime_completion_hx_Types_CompletionTypes._hx_statics = []
hxsublime_completion_hx_Types_CompletionTypes._hx_interfaces = []

# print hxsublime.completion.hx.Types.TopLevelOptions
class hxsublime_completion_hx_Types_TopLevelOptions:


	def __init__(self,val = 0):
		if val is None:
			val = 0
		
		self._opt = val
	
	# var _opt
	def val(self):
		return self._opt

	def set(self,val):
		self._opt = self._opt | val

	def has_types(self):
		return (self._opt & 1) > 0

	def has_locals(self):
		return (self._opt & 2) > 0

	def has_keywords(self):
		return (self._opt & 4) > 0

	def eq(self,other):
		return self._opt == other._opt







hxsublime_completion_hx_Types_TopLevelOptions._hx_class = hxsublime_completion_hx_Types_TopLevelOptions
hxsublime_completion_hx_Types_TopLevelOptions._hx_class_name = "hxsublime.completion.hx.TopLevelOptions"
_hx_classes['hxsublime.completion.hx.TopLevelOptions'] = hxsublime_completion_hx_Types_TopLevelOptions
hxsublime_completion_hx_Types_TopLevelOptions._hx_fields = ["_opt"]
hxsublime_completion_hx_Types_TopLevelOptions._hx_props = []
hxsublime_completion_hx_Types_TopLevelOptions._hx_methods = ["val","set","has_types","has_locals","has_keywords","eq"]
hxsublime_completion_hx_Types_TopLevelOptions._hx_statics = []
hxsublime_completion_hx_Types_TopLevelOptions._hx_interfaces = []

# print hxsublime.completion.hx.Types.CompletionSettings
class hxsublime_completion_hx_Types_CompletionSettings:


	def __init__(self,settings):
		self.settings = settings
	# var settings
	def no_fuzzy_completion(self):
		return self.settings.no_fuzzy_completion()

	def top_level_completions_only_on_demand(self):
		return self.settings.top_level_completions_on_demand()

	def is_async_completion(self):
		return self.settings.is_async_completion()

	def show_only_async_completions(self):
		return self.settings.show_only_async_completions()

	def get_completion_delays(self):
		return self.settings.get_completion_delays()

	def show_completion_times(self,view):
		return self.settings.show_completion_times(view)





hxsublime_completion_hx_Types_CompletionSettings.__meta__ = _Hx_AnonObject(fields = _Hx_AnonObject(no_fuzzy_completion = _Hx_AnonObject(lazyprop = None ) ,top_level_completions_only_on_demand = _Hx_AnonObject(lazyprop = None ) ,is_async_completion = _Hx_AnonObject(lazyprop = None ) ,show_only_async_completions = _Hx_AnonObject(lazyprop = None ) ,get_completion_delays = _Hx_AnonObject(lazyprop = None ) ) )


hxsublime_completion_hx_Types_CompletionSettings._hx_class = hxsublime_completion_hx_Types_CompletionSettings
hxsublime_completion_hx_Types_CompletionSettings._hx_class_name = "hxsublime.completion.hx.CompletionSettings"
_hx_classes['hxsublime.completion.hx.CompletionSettings'] = hxsublime_completion_hx_Types_CompletionSettings
hxsublime_completion_hx_Types_CompletionSettings._hx_fields = ["settings"]
hxsublime_completion_hx_Types_CompletionSettings._hx_props = []
hxsublime_completion_hx_Types_CompletionSettings._hx_methods = ["no_fuzzy_completion","top_level_completions_only_on_demand","is_async_completion","show_only_async_completions","get_completion_delays","show_completion_times"]
hxsublime_completion_hx_Types_CompletionSettings._hx_statics = ["__meta__"]
hxsublime_completion_hx_Types_CompletionSettings._hx_interfaces = []

# print hxsublime.completion.hx.Types.Types
class hxsublime_completion_hx_Types:

	pass




hxsublime_completion_hx_Types.control_struct = python_lib_Re.compile("\\s+(if|switch|for|while)\\s*\\($")


hxsublime_completion_hx_Types._hx_class = hxsublime_completion_hx_Types
hxsublime_completion_hx_Types._hx_class_name = "hxsublime.completion.hx.Types"
_hx_classes['hxsublime.completion.hx.Types'] = hxsublime_completion_hx_Types
hxsublime_completion_hx_Types._hx_fields = []
hxsublime_completion_hx_Types._hx_props = []
hxsublime_completion_hx_Types._hx_methods = []
hxsublime_completion_hx_Types._hx_statics = ["control_struct"]
hxsublime_completion_hx_Types._hx_interfaces = []

# print hxsublime.completion.hx.Types.CompletionContext
class hxsublime_completion_hx_Types_CompletionContext:


	def __init__(self,view,project,offset,options,settings,prefix):
		self.lazyCompleteChar = None
		self._lazy_src = None
		self.lazyBuild = None
		self.view = view
		self.prefix = prefix
		self.offset = offset
		self.project = project
		self.options = options
		self.settings = settings
		self.view_id = view.id()
		self.id = hxsublime_completion_hx_Types_CompletionContext.get_completion_id()
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
	# var lazyCompleteOffsetInBytes
	def complete_offset_in_bytes(self):
		if self.lazyCompleteOffsetInBytes is None:
			s = self.src_until_complete_offset()
			s_bytes = python_lib_StringTools.encode(s)
			self.lazyCompleteOffsetInBytes = __builtin__.len(s_bytes)
		
		
		return self.lazyCompleteOffsetInBytes
	

	def orig_file(self):
		return self.view.file_name()

	# var lazyBuild
	def build(self):
		if self.lazyBuild is None:
			if not self.project.has_build():
				self.project.extract_build_args()
			
			self.lazyBuild = self.project.get_build(self.view).copy()
		
		
		return self.lazyBuild
	

	def complete_char_is_after_control_struct(self):
		return self.in_control_struct() and self.complete_char() == "("

	def in_control_struct(self):
		return hxsublime_completion_hx_Types.control_struct.search(self.src_until_complete_offset()) is not None

	def src_until_complete_offset(self):
		_this = self.src()
		endIndex = self.complete_offset()
		return python_Tools.substring(_this, 0, endIndex)
	

	def line_after_offset(self):
		line_end = None
		_this = self.src()
		startIndex = self.offset
		if startIndex is None:
			line_end = _this.find("\n")
		else:
			line_end = _this.find("\n", startIndex)
		
		_this = self.src()
		return python_Tools.substring(_this, self.offset, line_end)
		
	

	# var _lazy_src
	def src(self):
		if self._lazy_src is None:
			self._lazy_src = hxsublime_tools_ViewTools.getContent(self.view)
		
		return self._lazy_src
	

	# var lazyCompleteChar
	def complete_char(self):
		if self.lazyCompleteChar is None:
			_this = self.src()
			index = self.complete_offset() - 1
			self.lazyCompleteChar = _this[index]
		
		
		return self.lazyCompleteChar
	

	def src_from_complete_to_offset(self):
		_this = self.src()
		startIndex = self.complete_offset()
		return python_Tools.substring(_this, startIndex, self.offset)
	

	def src_from_complete_to_prefix_end(self):
		rest = None
		_this = self.src()
		startIndex = self.complete_offset() + 1
		endIndex = self.offset + 1 + __builtin__.len(self.prefix)
		rest = python_Tools.substring(_this, startIndex, endIndex)
		
		return rest
	

	def offset_char(self):
		_this = self.src()
		return _this[self.offset]
	

	def _completion_info(self):
		return hxsublime_completion_hx_Types_CompletionContext.get_completion_info(self.view, self.offset, self.src())

	def commas(self):
		_this = self._completion_info()
		return _this[0]
	

	def prev_symbol_is_comma(self):
		_this = self._completion_info()
		return _this[2]
	

	def complete_offset(self):
		_this = self._completion_info()
		return _this[1]
	

	def is_new(self):
		_this = self._completion_info()
		return _this[3]
	

	def src_until_offset(self):
		_this = self.src()
		return python_Tools.substring(_this, 0, self.offset - 1)
	

	def temp_completion_src(self):
		def _hx_local_4():
			def _hx_local_3():
				def _hx_local_2():
					def _hx_local_1():
						_this = self.src()
						len = self.complete_offset()
						return python_Tools.substr(_this, 0, len)
					
					return _hx_local_1() + "|"
				
				def _hx_local_0():
					_this = self.src()
					pos = self.complete_offset()
					return python_Tools.substr(_this, pos, None)
				
				return _hx_local_2() + _hx_local_0()
			
			return _hx_local_3()
		
		return _hx_local_4()
	

	def prefix_is_whitespace(self):
		return hxsublime_tools_StringTools.isWhitespaceOrEmpty(self.prefix)

	def eq(self,other):
		_g = self
		def _hx_local_0():
			prefix_same = True
			if _g.options.types().has_hint():
				prefix_same = _g.prefix == other.prefix or _g.prefix_is_whitespace() and other.prefix_is_whitespace()
			
			haxe_Log.trace("same PREFIX:" + Std.string(prefix_same), _Hx_AnonObject(fileName = "Types.hx" ,lineNumber = 556 ,className = "hxsublime.completion.hx.CompletionContext" ,methodName = "eq" ))
			haxe_Log.trace("PREFIXES:" + _g.prefix + " - " + other.prefix, _Hx_AnonObject(fileName = "Types.hx" ,lineNumber = 557 ,className = "hxsublime.completion.hx.CompletionContext" ,methodName = "eq" ))
			return prefix_same
		
		prefix_check = _hx_local_0
		return other is not None and self.orig_file == other.orig_file and self.offset == other.offset and self.commas == other.commas and self.src_until_offset == other.src_until_offset and self.options.eq(other.options) and self.complete_char == other.complete_char and self.line_after_offset == other.line_after_offset and prefix_check()
	





hxsublime_completion_hx_Types_CompletionContext.__meta__ = _Hx_AnonObject(fields = _Hx_AnonObject(complete_offset_in_bytes = _Hx_AnonObject(lazyprop = None ) ,orig_file = _Hx_AnonObject(lazyprop = None ) ,build = _Hx_AnonObject(lazyprop = None ) ,complete_char_is_after_control_struct = _Hx_AnonObject(lazyprop = None ) ,in_control_struct = _Hx_AnonObject(lazyprop = None ) ,src_until_complete_offset = _Hx_AnonObject(lazyprop = None ) ,line_after_offset = _Hx_AnonObject(lazyprop = None ) ,src = _Hx_AnonObject(lazyprop = None ) ,complete_char = _Hx_AnonObject(lazyprop = None ) ,src_from_complete_to_offset = _Hx_AnonObject(lazyprop = None ) ,src_from_complete_to_prefix_end = _Hx_AnonObject(lazyprop = None ) ,offset_char = _Hx_AnonObject(lazyprop = None ) ,_completion_info = _Hx_AnonObject(lazyprop = None ) ,commas = _Hx_AnonObject(lazyprop = None ) ,prev_symbol_is_comma = _Hx_AnonObject(lazyprop = None ) ,complete_offset = _Hx_AnonObject(lazyprop = None ) ,is_new = _Hx_AnonObject(lazyprop = None ) ,src_until_offset = _Hx_AnonObject(lazyprop = None ) ,temp_completion_src = _Hx_AnonObject(lazyprop = None ) ,prefix_is_whitespace = _Hx_AnonObject(lazyprop = None ) ) )
def CompletionContext_statics_get_completion_id():
	return python_lib_Time.time()
hxsublime_completion_hx_Types_CompletionContext.get_completion_id = CompletionContext_statics_get_completion_id
def CompletionContext_statics_count_commas_and_complete_offset(src,prev_comma,complete_offset):
	commas = 0
	closed_pars = 0
	closed_braces = 0
	closed_brackets = 0
	_g = 0
	while _g < prev_comma:
		def _hx_local_0():
			nonlocal _g
			_hx_r = _g
			_g = _g + 1
			return _hx_r
			
		
		j = _hx_local_0()
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
	
hxsublime_completion_hx_Types_CompletionContext.count_commas_and_complete_offset = CompletionContext_statics_count_commas_and_complete_offset
def CompletionContext_statics_get_completion_info(view,offset,src):
	prev = src[offset - 1]
	commas = 0
	complete_offset = offset
	is_new = False
	prev_symbol_is_comma = False
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
			r = hxsublime_completion_hx_Types_CompletionContext.count_commas_and_complete_offset(src, prev_comma, complete_offset)
			commas = r[0]
			complete_offset = r[1]
			prev_symbol_is_comma = True
		
		else:
			complete_offset = __builtin__.max(prev_dot + 1, prev_par + 1, prev_colon + 1, prev_brace + 1, prev_semi + 1)
	
	
	return (commas, complete_offset, prev_symbol_is_comma, is_new)
	
hxsublime_completion_hx_Types_CompletionContext.get_completion_info = CompletionContext_statics_get_completion_info


hxsublime_completion_hx_Types_CompletionContext._hx_class = hxsublime_completion_hx_Types_CompletionContext
hxsublime_completion_hx_Types_CompletionContext._hx_class_name = "hxsublime.completion.hx.CompletionContext"
_hx_classes['hxsublime.completion.hx.CompletionContext'] = hxsublime_completion_hx_Types_CompletionContext
hxsublime_completion_hx_Types_CompletionContext._hx_fields = ["prefix","view","view_id","id","options","settings","offset","project","view_pos","lazyCompleteOffsetInBytes","lazyBuild","_lazy_src","lazyCompleteChar"]
hxsublime_completion_hx_Types_CompletionContext._hx_props = []
hxsublime_completion_hx_Types_CompletionContext._hx_methods = ["complete_offset_in_bytes","orig_file","build","complete_char_is_after_control_struct","in_control_struct","src_until_complete_offset","line_after_offset","src","complete_char","src_from_complete_to_offset","src_from_complete_to_prefix_end","offset_char","_completion_info","commas","prev_symbol_is_comma","complete_offset","is_new","src_until_offset","temp_completion_src","prefix_is_whitespace","eq"]
hxsublime_completion_hx_Types_CompletionContext._hx_statics = ["__meta__","get_completion_id","count_commas_and_complete_offset","get_completion_info"]
hxsublime_completion_hx_Types_CompletionContext._hx_interfaces = []

# print hxsublime.completion.hxml.Base.Base
class hxsublime_completion_hxml_Base:

	pass




hxsublime_completion_hxml_Base.lib_flag = python_lib_Re.compile("-lib\\s+(.*?)")
def Base_statics_auto_complete(project,view,offset,prefix):
	src = view.substr(sublime_Region(0, offset))
	current_line = None
	startIndex = src.find("\n") + 1
	current_line = python_Tools.substring(src, startIndex, offset)
	
	m = hxsublime_completion_hxml_Base.lib_flag.match(current_line)
	if m is not None:
		return project.haxelib_manager().get_completions()
	else:
		return []
	
hxsublime_completion_hxml_Base.auto_complete = Base_statics_auto_complete


hxsublime_completion_hxml_Base._hx_class = hxsublime_completion_hxml_Base
hxsublime_completion_hxml_Base._hx_class_name = "hxsublime.completion.hxml.Base"
_hx_classes['hxsublime.completion.hxml.Base'] = hxsublime_completion_hxml_Base
hxsublime_completion_hxml_Base._hx_fields = []
hxsublime_completion_hxml_Base._hx_props = []
hxsublime_completion_hxml_Base._hx_methods = []
hxsublime_completion_hxml_Base._hx_statics = ["lib_flag","auto_complete"]
hxsublime_completion_hxml_Base._hx_interfaces = []

# print hxsublime.completion.hxsl.Base.Base
class hxsublime_completion_hxsl_Base:

	pass




def Base_statics_auto_complete(project,view,offset,prefix):
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
	
hxsublime_completion_hxsl_Base.auto_complete = Base_statics_auto_complete


hxsublime_completion_hxsl_Base._hx_class = hxsublime_completion_hxsl_Base
hxsublime_completion_hxsl_Base._hx_class_name = "hxsublime.completion.hxsl.Base"
_hx_classes['hxsublime.completion.hxsl.Base'] = hxsublime_completion_hxsl_Base
hxsublime_completion_hxsl_Base._hx_fields = []
hxsublime_completion_hxsl_Base._hx_props = []
hxsublime_completion_hxsl_Base._hx_methods = []
hxsublime_completion_hxsl_Base._hx_statics = ["auto_complete"]
hxsublime_completion_hxsl_Base._hx_interfaces = []

# print hxsublime.panel.Base.PanelCloseListener
class hxsublime_panel_Base_PanelCloseListener(sublime_EventListener):

	def on_close(self,view):
		win = view.window()
		if win is None:
			win = sublime_Sublime.active_window()
		
		win_id = win.id()
		view_id = view.id()
		if python_lib_Types_DictImpl.hasKey(hxsublime_panel_Base_Panels._slide_panel.h, win_id):
			panel = hxsublime_panel_Base_Panels.slide_panel(win)
			if panel.output_view is not None and view_id == panel.output_view.id():
				panel.output_view = None
			
		
		
		panel_win_id = view.settings().get("haxe_panel_win_id")
		if panel_win_id is not None:
			_g = 0
			_g1 = [hxsublime_panel_Base_Panels._tab_panel, hxsublime_panel_Base_Panels._debug_panel]
			while _g < len(_g1):
				p = _g1[_g]
				_g = _g + 1
				panel = p.get_or_default(panel_win_id, None)
				if panel is not None and panel.output_view is not None and view_id == panel.output_view_id:
					haxe_Log.trace("panel safely removed", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 43 ,className = "hxsublime.panel.PanelCloseListener" ,methodName = "on_close" ))
					panel.output_view = None
					panel.output_view_id = None
				
				
			
		
		
	







hxsublime_panel_Base_PanelCloseListener._hx_class = hxsublime_panel_Base_PanelCloseListener
hxsublime_panel_Base_PanelCloseListener._hx_class_name = "hxsublime.panel.PanelCloseListener"
_hx_classes['hxsublime.panel.PanelCloseListener'] = hxsublime_panel_Base_PanelCloseListener
hxsublime_panel_Base_PanelCloseListener._hx_fields = []
hxsublime_panel_Base_PanelCloseListener._hx_props = []
hxsublime_panel_Base_PanelCloseListener._hx_methods = ["on_close"]
hxsublime_panel_Base_PanelCloseListener._hx_statics = []
hxsublime_panel_Base_PanelCloseListener._hx_interfaces = []
hxsublime_panel_Base_PanelCloseListener._hx_super = sublime_EventListener

# print hxsublime.tools.Cache.Cache
class hxsublime_tools_Cache:


	def __init__(self,cache_time = -1,data = None):
		if cache_time is None:
			cache_time = -1
		
		if data is None:
			data = None
		
		self.data = data
		self.cache_time = cache_time
		self.time_driven = cache_time != -1
	
	# var time_driven
	# var cache_time
	# var data
	def insert(self,id,value):
		self.data.set(id, _Hx_AnonObject(time = python_lib_Time.time() ,val = value ))

	def exists(self,id):
		return self.get_or_default(id, None) is not None

	def get_or_insert(self,id,creator):
		res = None
		if self.data.exists(id):
			res = self._get_val(id)
		else:
			res = creator()
			self.insert(id, res)
		
		return res
	

	def _get_val(self,id):
		return self.data.get(id).val

	def _cache_invalid(self,id):
		return not self._cache_valid(id)

	def _cache_valid(self,id):
		now = python_lib_Time.time()
		return now - self.data.get(id).time <= self.cache_time
	

	def get_or_default(self,id,defaultVal = None):
		if defaultVal is None:
			defaultVal = None
		
		res = defaultVal
		if self.data.exists(id):
			if self.time_driven and self._cache_invalid(id):
				self.data.remove(id)
			else:
				res = self._get_val(id)
		
		return res
	

	def get_and_delete(self,id,defaultVal = None):
		if defaultVal is None:
			defaultVal = None
		
		val = defaultVal
		if self.data.exists(id):
			if not self.time_driven or self._cache_valid(id):
				val = self._get_val(id)
			
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
hxsublime_tools_Cache._hx_methods = ["insert","exists","get_or_insert","_get_val","_cache_invalid","_cache_valid","get_or_default","get_and_delete","delete"]
hxsublime_tools_Cache._hx_statics = []
hxsublime_tools_Cache._hx_interfaces = []

# print hxsublime.panel.Base.Panels
class hxsublime_panel_Base_Panels:

	pass




hxsublime_panel_Base_Panels._tab_panel = hxsublime_tools_Cache(None, haxe_ds_IntMap())
hxsublime_panel_Base_Panels._debug_panel = hxsublime_tools_Cache(None, haxe_ds_IntMap())
hxsublime_panel_Base_Panels._slide_panel = haxe_ds_IntMap()
def Panels_statics_tab_panel(win = None):
	if win is None:
		win = None
	
	if win is None:
		win = sublime_Sublime.active_window()
	
	def _hx_local_1():
		def _hx_local_0():
			return hxsublime_panel_TabPanel(win, "Haxe Output")
		return hxsublime_panel_Base_Panels._tab_panel.get_or_insert(win.id(), _hx_local_0)
	
	return _hx_local_1()
	
hxsublime_panel_Base_Panels.tab_panel = Panels_statics_tab_panel
def Panels_statics_debug_panel(win = None):
	if win is None:
		win = None
	
	if win is None:
		win = sublime_Sublime.active_window()
	
	def _hx_local_1():
		def _hx_local_0():
			return hxsublime_panel_TabPanel(win, "Haxe Plugin Debug Panel")
		return hxsublime_panel_Base_Panels._debug_panel.get_or_insert(win.id(), _hx_local_0)
	
	return _hx_local_1()
	
hxsublime_panel_Base_Panels.debug_panel = Panels_statics_debug_panel
def Panels_statics___slide_panel(win = None):
	if win is None:
		win = None
	
	return hxsublime_panel_Base_Panels.tab_panel(win)
	
hxsublime_panel_Base_Panels.__slide_panel = Panels_statics___slide_panel
def Panels_statics_default_panel(win = None):
	if win is None:
		win = None
	
	if hxsublime_Settings.use_slide_panel():
		return hxsublime_panel_Base_Panels.slide_panel(win)
	else:
		return hxsublime_panel_Base_Panels.tab_panel(win)
	
hxsublime_panel_Base_Panels.default_panel = Panels_statics_default_panel
def Panels_statics_slide_panel(win = None):
	if win is None:
		win = None
	
	if win is None:
		win = sublime_Sublime.active_window()
	
	win_id = win.id()
	if not python_lib_Types_DictImpl.hasKey(hxsublime_panel_Base_Panels._slide_panel.h, win_id):
		hxsublime_panel_Base_Panels._slide_panel.set(win_id, hxsublime_panel_SlidePanel(win))
	
	return hxsublime_panel_Base_Panels._slide_panel.h.get(win_id, None)
	
hxsublime_panel_Base_Panels.slide_panel = Panels_statics_slide_panel


hxsublime_panel_Base_Panels._hx_class = hxsublime_panel_Base_Panels
hxsublime_panel_Base_Panels._hx_class_name = "hxsublime.panel.Panels"
_hx_classes['hxsublime.panel.Panels'] = hxsublime_panel_Base_Panels
hxsublime_panel_Base_Panels._hx_fields = []
hxsublime_panel_Base_Panels._hx_props = []
hxsublime_panel_Base_Panels._hx_methods = []
hxsublime_panel_Base_Panels._hx_statics = ["_tab_panel","_debug_panel","_slide_panel","tab_panel","debug_panel","__slide_panel","default_panel","slide_panel"]
hxsublime_panel_Base_Panels._hx_interfaces = []

# print hxsublime.panel.SlidePanel.SlidePanel
class hxsublime_panel_SlidePanel:


	def __init__(self,win):
		self.win = win
		self.output_view = None
	
	# var win
	# var output_view
	# var output_view_id
	def clear(self):
		self.output_view = self.win.create_output_panel("haxe")

	def write(self,text,scope = None,show_timestamp = True):
		if scope is None:
			scope = None
		
		if show_timestamp is None:
			show_timestamp = True
		
		win = self.win
		if self.output_view is None:
			self.output_view = win.create_output_panel("haxe")
		
		self.output_view.settings().set("result_file_regex", hxsublime_panel_Tools.haxe_file_regex())
		win.create_output_panel("haxe")
		panel = self.output_view
		if show_timestamp:
			text = hxsublime_panel_Tools.timestamp_msg(text)
		
		def _hx_local_0():
			x = _Hx_AnonObject(panel = "output.haxe" )
			def _hx_local_2():
				def _hx_local_1():
					d = python_lib_Types_Dict()
					_g = 0
					_g1 = Reflect.fields(x)
					while _g < len(_g1):
						f = _g1[_g]
						_g = _g + 1
						val = None
						v = None
						try:
							v = __builtin__.getattr(x, f)
						except Exception as _hx_e:
							_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
							if True:
								e = _hx_e1
								None
							else:
								raise _hx_e
						val = v
						
						python_lib_Types_DictImpl.set(d, f, val)
						
					
					
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
		
		if hxsublime_panel_Tools.valid_message(msg):
			self.write(msg + "\n", scope, show_timestamp)
		
	

	def status(self,title,msg):
		if hxsublime_panel_Tools.valid_message(msg):
			self.writeln(title + ": " + msg)
		







hxsublime_panel_SlidePanel._hx_class = hxsublime_panel_SlidePanel
hxsublime_panel_SlidePanel._hx_class_name = "hxsublime.panel.SlidePanel"
_hx_classes['hxsublime.panel.SlidePanel'] = hxsublime_panel_SlidePanel
hxsublime_panel_SlidePanel._hx_fields = ["win","output_view","output_view_id"]
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
		self.output_view = None
		self.output_view_id = None
		self.all = []
		self.panel_name = panel_name
		self.panel_syntax = panel_syntax
	
	# var win
	# var output_view
	# var output_view_id
	# var all
	# var panel_name
	# var panel_syntax
	def clear(self):
		None

	def write(self,msg,scope = None,show_timestamp = True):
		if scope is None:
			scope = None
		
		if show_timestamp is None:
			show_timestamp = True
		
		_g = self
		def _hx_local_0():
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
					_hx_r = _g2
					_g2 = _g2 + 1
					return _hx_r
					
				
				i = _hx_local_1()
				_g1.append(_g.all[i])
				__builtin__.len(_g1)
			
			
			_g.all = _g1
			
			msg1 = None
			if show_timestamp:
				msg1 = hxsublime_panel_Tools.timestamp_msg(msg)
			else:
				msg1 = msg
			if hxsublime_panel_Tools.valid_message(msg):
				_g.all = [msg1] + _g.all
				v = _g.output_view
				if v is None:
					v = hxsublime_tools_ViewTools.find_view_by_name(_g.panel_name)
					if v is None:
						v = hxsublime_panel_TabPanel.make_tab_panel(_g.win, _g.panel_name, _g.panel_syntax)
						hxsublime_tools_ViewTools.replaceContent(v, "".join(_g.all))
					
					
					_g.output_view = v
					_g.output_view_id = v.id()
				
				
				if v is not None:
					def _hx_local_2(v1,edit):
						v1.insert(edit, 0, msg1)
					do_edit = _hx_local_2
					hxsublime_tools_ViewTools.asyncEdit(v, do_edit)
				
				
			
			
		
		f = _hx_local_0
		sublime_Sublime.set_timeout(f, 40)
	

	def writeln(self,msg,scope = None,show_timestamp = True):
		if scope is None:
			scope = None
		
		if show_timestamp is None:
			show_timestamp = True
		
		self.write(msg + "\n")
	

	def status(self,title,msg):
		if hxsublime_panel_Tools.valid_message(msg):
			self.writeln(title + ": " + msg)
		





def TabPanel_statics_make_tab_panel(win,name,syntax):
	active = win.active_view()
	v = win.new_file()
	v.set_name(name)
	v.settings().set("word_wrap", True)
	v.settings().set("result_file_regex", hxsublime_panel_Tools.haxe_file_regex())
	v.settings().set("haxe_panel_win_id", win.id())
	v.set_scratch(True)
	v.set_syntax_file(syntax)
	last_group = win.num_groups() - 1
	win.set_view_index(v, last_group, 0)
	win.focus_view(active)
	return v
	
hxsublime_panel_TabPanel.make_tab_panel = TabPanel_statics_make_tab_panel


hxsublime_panel_TabPanel._hx_class = hxsublime_panel_TabPanel
hxsublime_panel_TabPanel._hx_class_name = "hxsublime.panel.TabPanel"
_hx_classes['hxsublime.panel.TabPanel'] = hxsublime_panel_TabPanel
hxsublime_panel_TabPanel._hx_fields = ["win","output_view","output_view_id","all","panel_name","panel_syntax"]
hxsublime_panel_TabPanel._hx_props = []
hxsublime_panel_TabPanel._hx_methods = ["clear","write","writeln","status"]
hxsublime_panel_TabPanel._hx_statics = ["make_tab_panel"]
hxsublime_panel_TabPanel._hx_interfaces = []

# print hxsublime.panel.Tools.Tools
class hxsublime_panel_Tools:

	pass




def Tools_statics_haxe_file_regex():
	return "^[0-9]{2}:[0-9]{2}:[0-9]{2}[ ]Error:[ ]" + python_Tools.substr(hxsublime_project_Tools.haxe_file_regex, 1, None)
hxsublime_panel_Tools.haxe_file_regex = Tools_statics_haxe_file_regex
def Tools_statics_timestamp_msg(msg):
	return python_lib_datetime_DateTime.now().strftime("%H:%M:%S") + " " + msg
hxsublime_panel_Tools.timestamp_msg = Tools_statics_timestamp_msg
def Tools_statics_valid_message(msg):
	return msg is not None and msg != "" and msg != "\n"
hxsublime_panel_Tools.valid_message = Tools_statics_valid_message


hxsublime_panel_Tools._hx_class = hxsublime_panel_Tools
hxsublime_panel_Tools._hx_class_name = "hxsublime.panel.Tools"
_hx_classes['hxsublime.panel.Tools'] = hxsublime_panel_Tools
hxsublime_panel_Tools._hx_fields = []
hxsublime_panel_Tools._hx_props = []
hxsublime_panel_Tools._hx_methods = []
hxsublime_panel_Tools._hx_statics = ["haxe_file_regex","timestamp_msg","valid_message"]
hxsublime_panel_Tools._hx_interfaces = []

# print hxsublime.project.Base.Projects
class hxsublime_project_Base_Projects:

	pass




hxsublime_project_Base_Projects.projects = hxsublime_tools_Cache(None, haxe_ds_StringMap())
hxsublime_project_Base_Projects.userHome = python_lib_os_Path.expanduser("~")
hxsublime_project_Base_Projects.logFile = python_lib_os_Path.join(hxsublime_project_Base_Projects.userHome, "st3_haxe_log.txt")
hxsublime_project_Base_Projects.nextServerPort = 6000
def Projects_statics_fileLog(msg):
	f = __builtin__.open(hxsublime_project_Base_Projects.logFile, "a+")
	f.write(Std.string(msg) + "\n")
	f.close()
	
hxsublime_project_Base_Projects.fileLog = Projects_statics_fileLog
def Projects_statics_cleanup_projects():
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
	_it = hxsublime_project_Base_Projects.projects.data.keys()
	while _it.hasNext():
		p = _it.next()
		proj = hxsublime_project_Base_Projects.projects.get_or_default(p, None)
		if proj is not None and not Lambda.has(win_ids, proj.win_id):
			remove.append(p)
			__builtin__.len(remove)
		
		
		
	
	
	haxe_Log.trace(remove, _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 44 ,className = "hxsublime.project.Projects" ,methodName = "cleanup_projects" ))
	_g1 = 0
	while _g1 < len(remove):
		pid = remove[_g1]
		_g1 = _g1 + 1
		haxe_Log.trace(pid, _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 46 ,className = "hxsublime.project.Projects" ,methodName = "cleanup_projects" ))
		project = hxsublime_project_Base_Projects.projects.data.get(pid).val
		project.destroy()
		haxe_Log.trace("delete project from memory", _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 49 ,className = "hxsublime.project.Projects" ,methodName = "cleanup_projects" ))
		hxsublime_project_Base_Projects.projects.data.remove(pid)
	
	
	
hxsublime_project_Base_Projects.cleanup_projects = Projects_statics_cleanup_projects
def Projects_statics_get_project_id(file,win):
	id = None
	if file is None:
		id = "global" + Std.string(win.id())
	else:
		id = file
	return id
	
hxsublime_project_Base_Projects.get_project_id = Projects_statics_get_project_id
def Projects_statics_get_window(view = None):
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
	
hxsublime_project_Base_Projects.get_window = Projects_statics_get_window
def Projects_statics_current_project(view = None):
	if view is None:
		view = None
	
	hxsublime_project_Base_Projects.cleanup_projects()
	file = hxsublime_tools_SublimeTools.getProjectFile()
	win = hxsublime_project_Base_Projects.get_window(view)
	id = hxsublime_project_Base_Projects.get_project_id(file, win)
	haxe_Log.trace("project id:" + id, _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 85 ,className = "hxsublime.project.Projects" ,methodName = "current_project" ))
	haxe_Log.trace("win.id:" + Std.string(win.id()), _Hx_AnonObject(fileName = "Base.hx" ,lineNumber = 87 ,className = "hxsublime.project.Projects" ,methodName = "current_project" ))
	def _hx_local_0():
		id1 = id
		a1 = file
		a2 = win
		def _hx_local_1():
			return hxsublime_project_Base_Projects.create_project(id1, a1, a2)
		return _hx_local_1
	
	res = hxsublime_project_Base_Projects.projects.get_or_insert(id, _hx_local_0())
	return res
	
hxsublime_project_Base_Projects.current_project = Projects_statics_current_project
def Projects_statics_create_project(id,file,win):
	p = hxsublime_project_Project(id, file, win.id(), hxsublime_project_Base_Projects.nextServerPort)
	hxsublime_project_Base_Projects.nextServerPort = hxsublime_project_Base_Projects.nextServerPort + 20
	return p
	
hxsublime_project_Base_Projects.create_project = Projects_statics_create_project


hxsublime_project_Base_Projects._hx_class = hxsublime_project_Base_Projects
hxsublime_project_Base_Projects._hx_class_name = "hxsublime.project.Projects"
_hx_classes['hxsublime.project.Projects'] = hxsublime_project_Base_Projects
hxsublime_project_Base_Projects._hx_fields = []
hxsublime_project_Base_Projects._hx_props = []
hxsublime_project_Base_Projects._hx_methods = []
hxsublime_project_Base_Projects._hx_statics = ["projects","userHome","logFile","nextServerPort","fileLog","cleanup_projects","get_project_id","get_window","current_project","create_project"]
hxsublime_project_Base_Projects._hx_interfaces = []

# print hxsublime.project.CompletionState.ProjectCompletionState
class hxsublime_project_CompletionState_ProjectCompletionState:


	def __init__(self):
		self.running = hxsublime_tools_Cache(None, haxe_ds_IntMap())
		self.trigger = hxsublime_tools_Cache(1000, haxe_ds_IntMap())
		self.current_id = None
		self.errors = []
		self.async = hxsublime_tools_Cache(1000, haxe_ds_IntMap())
		self.current = _Hx_AnonObject(input = None ,output = None )
	
	# var running
	# var trigger
	# var current_id
	# var errors
	# var async
	# var current
	def add_completion_result(self,comp_result):
		self.async.insert(comp_result.ctx.view_id, comp_result)

	def is_equivalent_completion_already_running(self,ctx):
		complete_offset = ctx.complete_offset
		view_id = ctx.view_id
		last_completion_id = self.current_id
		running_completion = self.running.get_or_default(last_completion_id, None)
		return running_completion is not None and running_completion[0] == complete_offset() and running_completion[1] == view_id
	

	def run_if_still_up_to_date(self,comp_id,run):
		self.running.delete(comp_id)
		if self.current_id == comp_id:
			run()
		
	

	def set_new_completion(self,ctx):
		def _hx_local_0():
			a = ctx.complete_offset()
			return (a, ctx.view_id)
		
		self.running.insert(ctx.id, _hx_local_0())
		self.current_id = ctx.id
		self.set_errors([])
	

	def set_trigger(self,view,options):
		haxe_Log.trace("SET TRIGGER", _Hx_AnonObject(fileName = "CompletionState.hx" ,lineNumber = 75 ,className = "hxsublime.project.ProjectCompletionState" ,methodName = "set_trigger" ))
		self.trigger.insert(view.id(), options)
	

	def clear_completion(self):
		self.current = _Hx_AnonObject(input = None ,output = None )

	def set_errors(self,errors):
		self.errors = errors

	def get_and_delete_trigger(self,view):
		return self.trigger.get_and_delete(view.id(), None)

	def get_and_delete_async(self,view):
		return self.async.get_and_delete(view.id(), None)

	def get_async(self,view):
		return self.async.get_or_default(view.id(), None)

	def delete_async(self,view):
		return self.async.delete(view.id())







hxsublime_project_CompletionState_ProjectCompletionState._hx_class = hxsublime_project_CompletionState_ProjectCompletionState
hxsublime_project_CompletionState_ProjectCompletionState._hx_class_name = "hxsublime.project.ProjectCompletionState"
_hx_classes['hxsublime.project.ProjectCompletionState'] = hxsublime_project_CompletionState_ProjectCompletionState
hxsublime_project_CompletionState_ProjectCompletionState._hx_fields = ["running","trigger","current_id","errors","async","current"]
hxsublime_project_CompletionState_ProjectCompletionState._hx_props = []
hxsublime_project_CompletionState_ProjectCompletionState._hx_methods = ["add_completion_result","is_equivalent_completion_already_running","run_if_still_up_to_date","set_new_completion","set_trigger","clear_completion","set_errors","get_and_delete_trigger","get_and_delete_async","get_async","delete_async"]
hxsublime_project_CompletionState_ProjectCompletionState._hx_statics = []
hxsublime_project_CompletionState_ProjectCompletionState._hx_interfaces = []

# print hxsublime.project.Project.Project
class hxsublime_project_Project:


	def __init__(self,id,file,win_id,server_port):
		self.completion_context = hxsublime_project_CompletionState_ProjectCompletionState()
		self._haxelib_manager = hxsublime_Haxelib_HaxeLibManager(self)
		self.current_build = None
		self.selecting_build = False
		self.builds = []
		self.win_id = win_id
		self.server = hxsublime_compiler_Server(server_port)
		self.project_file = file
		self.project_id = id
		if self.project_file is not None:
			self.project_path = python_lib_os_Path.normpath(python_lib_os_Path.dirname(self.project_file))
		else:
			self.project_path = None
		self._update_compiler_info()
	
	# var completion_context
	# var _haxelib_manager
	# var current_build
	# var selecting_build
	# var builds
	# var win_id
	# var server
	# var project_file
	# var project_id
	# var project_path
	# var std_bundle
	# var std_paths
	# var server_mode
	def haxelib_manager(self):
		return self._haxelib_manager

	def project_dir(self,defaultVal):
		if self.project_path is not None:
			return self.project_path
		else:
			return defaultVal

	def nme_exec(self,view = None):
		if view is None:
			view = None
		
		return [hxsublime_Settings.haxelib_exec(), "run", "nme"]
	

	def openfl_exec(self,view = None):
		if view is None:
			view = None
		
		return [hxsublime_Settings.haxelib_exec(), "run", "openfl"]
	

	def haxelib_exec(self,view = None):
		if view is None:
			view = None
		
		return [hxsublime_Settings.haxelib_exec()]
	

	def haxe_exec(self,view = None):
		if view is None:
			view = None
		
		haxe_exec = hxsublime_Settings.haxe_exec(view)
		if not python_lib_os_Path.isabs(haxe_exec) and haxe_exec != "haxe":
			cwd = self.project_dir(".")
			def _hx_local_0():
				_this = python_lib_os_Path.join(cwd, hxsublime_Settings.haxe_exec(view)).split("/")
				return python_lib_Os.sep.join(_this)
			
			haxe_exec = python_lib_os_Path.normpath(_hx_local_0())
		
		
		return [haxe_exec]
	

	def haxe_env(self,view = None):
		if view is None:
			view = None
		
		return hxsublime_project_Project._haxe_build_env(self.project_dir("."))
	

	def start_server(self,view):
		cwd = self.project_dir(".")
		haxe_exec = self.haxe_exec(view)[0]
		env = self.haxe_env()
		self.server.start(haxe_exec, cwd, env)
	

	def restart_server(self,view):
		def _hx_local_0():
			f = self.start_server
			a1 = view
			def _hx_local_1():
				return f(a1)
			return _hx_local_1
		
		self.server.stop(_hx_local_0())
	

	def is_server_mode(self):
		return self.server_mode and hxsublime_Settings.use_haxe_servermode()

	def is_server_mode_for_builds(self):
		return self.is_server_mode() and hxsublime_Settings.use_haxe_servermode_for_builds()

	def generate_build(self,view):
		_g = self
		fn = view.file_name()
		def _hx_local_0():
			return Std._hx_is(_g.current_build, hxsublime_build_HxmlBuild)
		is_hxml_build = _hx_local_0
		if self.current_build is not None and is_hxml_build() and fn == self.current_build.build_file() and view.size() == 0:
			def _hx_local_1(v,e):
				hxml_src = _g.current_build.make_hxml()
				v.insert(e, 0, hxml_src)
			
			run_edit = _hx_local_1
			hxsublime_tools_ViewTools.asyncEdit(view, run_edit)
		
		
	

	def select_build(self,view):
		scopes = view.scope_name(view.sel()[0].end()).split(" ")
		if Lambda.has(scopes, "source.hxml"):
			view.run_command("save")
		
		self.extract_build_args(view, True)
	

	def extract_build_args(self,view = None,force_panel = False):
		if view is None:
			view = None
		
		if force_panel is None:
			force_panel = False
		
		if view is None:
			view = sublime_Sublime.active_window().active_view()
		
		folders = self._get_folders(view)
		self.builds = self._find_builds_in_folders(folders)
		num_builds = __builtin__.len(self.builds)
		view_build_id = view.settings().get("haxe-current-build-id")
		if view_build_id is not None and view_build_id < num_builds and not force_panel:
			self._set_current_build(view, view_build_id)
		elif num_builds == 1:
			if force_panel:
				sublime_Sublime.status_message("There is only one build")
			
			self._set_current_build(view, 0)
		
		elif num_builds == 0 and force_panel:
			sublime_Sublime.status_message("No build files found (e.g. hxml, nmml, xml)")
			self._create_new_hxml(view, folders[0])
		
		elif num_builds > 1 and force_panel:
			self._show_build_selection_panel(view)
		else:
			self._set_current_build(view, 0)
	

	def has_build(self):
		return self.current_build is not None

	def check_build(self,view):
		self._build(view, "check")

	def just_build(self,view):
		self._build(view, "build")

	def run_build(self,view):
		self._build(view, "run")

	def _update_compiler_info(self):
		info = hxsublime_project_Project._collect_compiler_info(self.haxe_exec(), self.project_path)
		bundle = info[0]
		ver = info[1]
		std_paths = info[2]
		self.server_mode = ver is None or ver >= 209
		self.std_bundle = bundle
		self.std_paths = std_paths
	

	def _find_builds_in_folders(self,folders):
		builds = []
		haxe_Log.trace("find builds start", _Hx_AnonObject(fileName = "Project.hx" ,lineNumber = 238 ,className = "hxsublime.project.Project" ,methodName = "_find_builds_in_folders" ))
		_g = 0
		while _g < len(folders):
			f = folders[_g]
			_g = _g + 1
			x = None
			_this = hxsublime_build_Tools.find_hxml_projects(self, f)
			def _hx_local_0(x1):
				return x1
			x = __builtin__.list(__builtin__.map(_hx_local_0, _this))
			
			builds.extend(x)
			
			x = None
			_this = hxsublime_build_Tools.find_nme_projects(self, f)
			def _hx_local_1(x1):
				return x1
			x = __builtin__.list(__builtin__.map(_hx_local_1, _this))
			
			builds.extend(x)
			
			x = None
			_this = hxsublime_build_Tools.find_openfl_projects(self, f)
			def _hx_local_2(x1):
				return x1
			x = __builtin__.list(__builtin__.map(_hx_local_2, _this))
			
			builds.extend(x)
			
		
		
		haxe_Log.trace("find builds end", _Hx_AnonObject(fileName = "Project.hx" ,lineNumber = 246 ,className = "hxsublime.project.Project" ,methodName = "_find_builds_in_folders" ))
		return builds
	

	def _get_view_file_name(self,view):
		if view is None:
			view = sublime_Sublime.active_window().active_view()
		
		return view.file_name()
	

	def _get_current_window(self,view):
		return hxsublime_project_Tools.get_window(view)

	def _get_folders(self,view):
		win = self._get_current_window(view)
		folders = win.folders()
		return folders
	

	def _create_new_hxml(self,view,folder):
		win = sublime_Sublime.active_window()
		f = python_lib_os_Path.join(folder, "build.hxml")
		self.current_build = None
		self.get_build(view)
		self.current_build.setHxml(f)
		win.open_file(f, sublime_Sublime.TRANSIENT)
		self._set_current_build(view, 0)
	

	def _show_build_selection_panel(self,view):
		_g1 = self
		buildsView = None
		_g = []
		_g11 = 0
		_g2 = self.builds
		while _g11 < len(_g2):
			b = _g2[_g11]
			_g11 = _g11 + 1
			x = [b.to_string(), python_lib_os_Path.basename(b.build_file())]
			_g.append(x)
			__builtin__.len(_g)
			
		
		
		buildsView = _g
		
		self.selecting_build = True
		sublime_Sublime.status_message("Please select your build")
		def _hx_local_0(i):
			_g1.selecting_build = False
			_g1._set_current_build(view, i)
		
		on_selected = _hx_local_0
		win = sublime_Sublime.active_window()
		win.show_quick_panel(buildsView, on_selected, sublime_Sublime.MONOSPACE_FONT)
	

	def _set_current_build(self,view,id):
		haxe_Log.trace("_set_current_build", _Hx_AnonObject(fileName = "Project.hx" ,lineNumber = 305 ,className = "hxsublime.project.Project" ,methodName = "_set_current_build" ))
		if id < 0 or id >= __builtin__.len(self.builds):
			id = 0
		
		if __builtin__.len(self.builds) > 0:
			view.settings().set("haxe-current-build-id", id)
			self.current_build = self.builds[id]
			self.current_build.set_std_bundle(self.std_bundle)
			view.set_status("haxe-build", self.current_build.to_string())
		
		else:
			view.set_status("haxe-build", "No build found/selected")
	

	def _build(self,view,type = "run"):
		if type is None:
			type = "run"
		
		if view is None:
			view = sublime_Sublime.active_window().active_view()
		
		win = view.window()
		env = hxsublime_project_Project._haxe_build_env(self.project_dir("."))
		build = None
		if self.has_build():
			build = self.get_original_build(view)
		else:
			self.extract_build_args(view)
			build = self.get_original_build(view)
		
		r = None
		if type == "run":
			r = build.prepare_run_cmd(self, self.is_server_mode_for_builds(), view)
		elif type == "build":
			r = build.prepare_build_cmd(self, self.is_server_mode_for_builds(), view)
		else:
			r = build.prepare_check_cmd(self, self.is_server_mode(), view)
		cmd = r[0]
		build_folder = r[1]
		escaped_cmd = build.escape_cmd(cmd)
		hxsublime_panel_Base_Panels.default_panel().writeln("running: " + " ".join(escaped_cmd))
		def _hx_local_0():
			x = _Hx_AnonObject(cmd = cmd ,is_check_run = type == "check" ,working_dir = build_folder ,file_regex = hxsublime_project_Tools.haxe_file_regex ,env = env )
			def _hx_local_2():
				def _hx_local_1():
					d = python_lib_Types_Dict()
					_g = 0
					_g1 = Reflect.fields(x)
					while _g < len(_g1):
						f = _g1[_g]
						_g = _g + 1
						val = None
						v = None
						try:
							v = __builtin__.getattr(x, f)
						except Exception as _hx_e:
							_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
							if True:
								e = _hx_e1
								None
							else:
								raise _hx_e
						val = v
						
						python_lib_Types_DictImpl.set(d, f, val)
						
					
					
					return d
				
				return _hx_local_1()
			
			return _hx_local_2()
		
		win.run_command("hxsublime_commands__execute__haxe_exec", _hx_local_0())
	

	def clear_build(self):
		self.current_build = None
		self.completion_context.clear_completion()
	

	def destroy(self):
		self.server.stop()

	def _create_default_build(self,view):
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
		_g1 = python_lib_Re_RegexHelper.findallDynamic(hxsublime_tools_HxSrcTools_Regex.package_line, src, None, None)
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
		build.add_arg(("-cp", src_dir))
		build.add_arg(("-js", build.output))
		build.setHxml(python_lib_os_Path.join(src_dir, "build.hxml"))
		return build
	

	def get_original_build(self,view):
		if self.current_build is None and view.score_selector(0, "source.haxe.2") > 0:
			self.current_build = self._create_default_build(view)
		
		return self.current_build
	

	def get_build(self,view):
		return self.get_original_build(view).copy()





def Project_statics__haxe_build_env(project_dir):
	lib_path = hxsublime_Settings.haxe_library_path()
	haxe_inst_path = hxsublime_Settings.haxe_inst_path()
	neko_inst_path = hxsublime_Settings.neko_inst_path()
	env = python_lib_Os.environ.copy()
	env_path = python_lib_Os.environ.copy().get("PATH", "")
	paths = []
	def _hx_local_0(s):
		return s
	do_encode = _hx_local_0
	path = None
	if lib_path is not None:
		if hxsublime_tools_PathTools.is_abs_path(lib_path):
			path = lib_path
		else:
			path = python_lib_os_Path.normpath(python_lib_os_Path.join(project_dir, lib_path))
		def _hx_local_1():
			_this = path.split("/")
			return python_lib_Os.sep.join(_this)
		
		val = do_encode(_hx_local_1())
		python_lib_Types_DictImpl.set(env, "HAXE_LIBRARY_PATH", val)
		
		def _hx_local_2():
			_this = path.split("/")
			return python_lib_Os.sep.join(_this)
		
		val = do_encode(_hx_local_2())
		python_lib_Types_DictImpl.set(env, "HAXE_STD_PATH", val)
		
	
	
	if haxe_inst_path is not None:
		if hxsublime_tools_PathTools.is_abs_path(haxe_inst_path):
			path = haxe_inst_path
		else:
			path = python_lib_os_Path.normpath(python_lib_os_Path.join(project_dir, haxe_inst_path))
		def _hx_local_3():
			_this = path.split("/")
			return python_lib_Os.sep.join(_this)
		
		val = do_encode(_hx_local_3())
		python_lib_Types_DictImpl.set(env, "HAXEPATH", val)
		
		def _hx_local_4():
			_this = path.split("/")
			return python_lib_Os.sep.join(_this)
		
		x = do_encode(_hx_local_4())
		paths.append(x)
		__builtin__.len(paths)
		
		
	
	
	if neko_inst_path is not None:
		path = python_lib_os_Path.normpath(python_lib_os_Path.join(project_dir, neko_inst_path))
		def _hx_local_5():
			_this = path.split("/")
			return python_lib_Os.sep.join(_this)
		
		val = do_encode(_hx_local_5())
		python_lib_Types_DictImpl.set(env, "NEKO_INSTPATH", val)
		
		def _hx_local_6():
			_this = path.split("/")
			return python_lib_Os.sep.join(_this)
		
		x = do_encode(_hx_local_6())
		paths.append(x)
		
	
	
	if __builtin__.len(paths) > 0:
		val = python_lib_Os.pathsep.join(paths) + python_lib_Os.pathsep + env_path
		python_lib_Types_DictImpl.set(env, "PATH", val)
	
	
	return env
	
hxsublime_project_Project._haxe_build_env = Project_statics__haxe_build_env
def Project_statics__get_compiler_info_env(project_path):
	return hxsublime_project_Project._haxe_build_env(project_path)
hxsublime_project_Project._get_compiler_info_env = Project_statics__get_compiler_info_env
def Project_statics__collect_compiler_info(haxe_exec,project_path):
	env = hxsublime_project_Project._get_compiler_info_env(project_path)
	cmd = haxe_exec
	cmd.extend(["-main", "Nothing", "-v", "--no-output"])
	r = hxsublime_Execute.run_cmd(cmd, None, None, env)
	out = r[0]
	err = r[1]
	std_classpaths = hxsublime_project_Project._extract_std_classpaths(out)
	bundle = hxsublime_project_Project._collect_std_classes_and_packs(std_classpaths)
	ver = hxsublime_project_Project._extract_haxe_version(out)
	return (bundle, ver, std_classpaths)
	
hxsublime_project_Project._collect_compiler_info = Project_statics__collect_compiler_info
def Project_statics__extract_haxe_version(out):
	ver = python_lib_Re.search(hxsublime_project_Project._haxe_version, out)
	if ver is not None:
		x = ver.group(1)
		x1 = float(x)
		return int(x1)
		
	
	else:
		return None
	
hxsublime_project_Project._extract_haxe_version = Project_statics__extract_haxe_version
def Project_statics__remove_trailing_path_sep(path):
	if __builtin__.len(path) > 1:
		last_pos = __builtin__.len(path) - 1
		last_char = path[last_pos]
		if last_char == "/" or last_char == "\\" or last_char == python_lib_os_Path.sep:
			path = python_Tools.substring(path, 0, last_pos)
		
	
	
	return path
	
hxsublime_project_Project._remove_trailing_path_sep = Project_statics__remove_trailing_path_sep
def Project_statics__is_valid_classpath(path):
	return __builtin__.len(path) > 1 and python_lib_os_Path.exists(path) and python_lib_os_Path.isdir(path)
hxsublime_project_Project._is_valid_classpath = Project_statics__is_valid_classpath
def Project_statics__extract_std_classpaths(out):
	m = hxsublime_project_Project._classpath_line.match(out)
	std_classpaths = []
	all_paths = m.group(1).split(";")
	ignored_paths = [".", "./"]
	std_paths = None
	if m is not None:
		_this = python_lib_Types_Set(all_paths)
		other = python_lib_Types_Set(ignored_paths)
		std_paths = _this - other
	
	else:
		std_paths = python_lib_Types_Set()
	def _hx_local_0():
		p = std_paths.__iter__()
		return python_Lib_HaxeIterator(p)
	
	_it = _hx_local_0()
	while _it.hasNext():
		p = _it.next()
		p1 = python_lib_os_Path.normpath(p)
		p1 = hxsublime_project_Project._remove_trailing_path_sep(p1)
		if hxsublime_project_Project._is_valid_classpath(p1):
			std_classpaths.append(p1)
		
		
	
	
	return std_classpaths
	
hxsublime_project_Project._extract_std_classpaths = Project_statics__extract_std_classpaths
def Project_statics__collect_std_classes_and_packs(std_cps):
	bundle = hxsublime_tools_HxSrcTools.empty_type_bundle()
	_g = 0
	while _g < len(std_cps):
		p = std_cps[_g]
		_g = _g + 1
		bundle1 = hxsublime_Types.extract_types(p, [], [], 0, [], False)
		bundle = bundle.merge(bundle1)
	
	
	return bundle
	
hxsublime_project_Project._collect_std_classes_and_packs = Project_statics__collect_std_classes_and_packs
hxsublime_project_Project._classpath_line = python_lib_Re.compile("Classpath : (.*)")
hxsublime_project_Project._haxe_version = python_lib_Re.compile("haxe_([0-9]{3})", python_lib_Re.M)


hxsublime_project_Project._hx_class = hxsublime_project_Project
hxsublime_project_Project._hx_class_name = "hxsublime.project.Project"
_hx_classes['hxsublime.project.Project'] = hxsublime_project_Project
hxsublime_project_Project._hx_fields = ["completion_context","_haxelib_manager","current_build","selecting_build","builds","win_id","server","project_file","project_id","project_path","std_bundle","std_paths","server_mode"]
hxsublime_project_Project._hx_props = []
hxsublime_project_Project._hx_methods = ["haxelib_manager","project_dir","nme_exec","openfl_exec","haxelib_exec","haxe_exec","haxe_env","start_server","restart_server","is_server_mode","is_server_mode_for_builds","generate_build","select_build","extract_build_args","has_build","check_build","just_build","run_build","_update_compiler_info","_find_builds_in_folders","_get_view_file_name","_get_current_window","_get_folders","_create_new_hxml","_show_build_selection_panel","_set_current_build","_build","clear_build","destroy","_create_default_build","get_original_build","get_build"]
hxsublime_project_Project._hx_statics = ["_haxe_build_env","_get_compiler_info_env","_collect_compiler_info","_extract_haxe_version","_remove_trailing_path_sep","_is_valid_classpath","_extract_std_classpaths","_collect_std_classes_and_packs","_classpath_line","_haxe_version"]
hxsublime_project_Project._hx_interfaces = []

# print hxsublime.project.Tools.Tools
class hxsublime_project_Tools:

	pass




def Tools_statics_get_window(view):
	win = None
	if view is not None:
		win = view.window()
		if win is None:
			win = sublime_Sublime.active_window()
		
	
	else:
		win = sublime_Sublime.active_window()
	return win
	
hxsublime_project_Tools.get_window = Tools_statics_get_window
hxsublime_project_Tools._win_start = "(?:(?:[A-Za-z][:])"
hxsublime_project_Tools._unix_start = "(?:[/]?)"
hxsublime_project_Tools.haxe_file_regex = "^(" + hxsublime_project_Tools._win_start + "|" + hxsublime_project_Tools._unix_start + ")?(?:[^:]*)):([0-9]+): (?:character(?:s?)|line(?:s?))? ([0-9]+)-?[0-9]*\\s?:(.*)$"


hxsublime_project_Tools._hx_class = hxsublime_project_Tools
hxsublime_project_Tools._hx_class_name = "hxsublime.project.Tools"
_hx_classes['hxsublime.project.Tools'] = hxsublime_project_Tools
hxsublime_project_Tools._hx_fields = []
hxsublime_project_Tools._hx_props = []
hxsublime_project_Tools._hx_methods = []
hxsublime_project_Tools._hx_statics = ["get_window","_win_start","_unix_start","haxe_file_regex"]
hxsublime_project_Tools._hx_interfaces = []

# print hxsublime.tools.HxSrcTools.Regex
class hxsublime_tools_HxSrcTools_Regex:

	pass




hxsublime_tools_HxSrcTools_Regex.compact_func = python_lib_Re.compile("\\(.*\\)")
hxsublime_tools_HxSrcTools_Regex.compact_prop = python_lib_Re.compile(":.*\\.([a-z_0-9]+)", python_lib_Re.I)
hxsublime_tools_HxSrcTools_Regex.space_chars = python_lib_Re.compile("\\s")
hxsublime_tools_HxSrcTools_Regex.word_chars = python_lib_Re.compile("[a-z0-9._]", python_lib_Re.I)
hxsublime_tools_HxSrcTools_Regex.import_line = python_lib_Re.compile("^([ \t]*)import\\s+([a-z0-9._]+);", python_lib_Re.I | python_lib_Re.M)
hxsublime_tools_HxSrcTools_Regex.using_line = python_lib_Re.compile("^([ \t]*)using\\s+([a-z0-9._]+);", python_lib_Re.I | python_lib_Re.M)
hxsublime_tools_HxSrcTools_Regex.package_line = python_lib_Re.compile("\\s*package\\s*([a-z0-9.]*)\\s*;", python_lib_Re.I)
hxsublime_tools_HxSrcTools_Regex.type_decl_with_scope = python_lib_Re.compile("(private\\s+)?(?:extern\\s+)?(class|typedef|enum|interface|abstract)\\s+([A-Z][a-zA-Z0-9_]*)\\s*(<[a-zA-Z0-9_,]+>)?", python_lib_Re.M)
hxsublime_tools_HxSrcTools_Regex.type_decl = python_lib_Re.compile("(class|typedef|enum|interface|abstract)\\s+([A-Z][a-zA-Z0-9_]*)\\s*(<[a-zA-Z0-9_,]+>)?", python_lib_Re.M)
hxsublime_tools_HxSrcTools_Regex.enum_start_decl = python_lib_Re.compile("enum\\s+([A-Z][a-zA-Z0-9_]*)\\s*(<[a-zA-Z0-9_,]+>)?", python_lib_Re.M)
hxsublime_tools_HxSrcTools_Regex.skippable = python_lib_Re.compile("^[a-zA-Z0-9_\\s]*$")
hxsublime_tools_HxSrcTools_Regex.in_anonymous = python_lib_Re.compile("[{,]\\s*([a-zA-Z0-9_\"']+)\\s*:\\s*$", python_lib_Re.M | python_lib_Re.U)
hxsublime_tools_HxSrcTools_Regex.variables = python_lib_Re.compile("var\\s+([^:;\\s]*)", python_lib_Re.I)
hxsublime_tools_HxSrcTools_Regex.functions = python_lib_Re.compile("function\\s+([^;\\.\\(\\)\\s]*)", python_lib_Re.I)
hxsublime_tools_HxSrcTools_Regex.named_functions = python_lib_Re.compile("function\\s+([a-zA-Z0-9_]+)\\s*", python_lib_Re.I)
hxsublime_tools_HxSrcTools_Regex.function_params = python_lib_Re.compile("function\\s+[a-zA-Z0-9_]+\\s*\\(([^\\)]*)", python_lib_Re.M)
hxsublime_tools_HxSrcTools_Regex.param_default = python_lib_Re.compile("(=\\s*\"*[^\"]*\")", python_lib_Re.M)
hxsublime_tools_HxSrcTools_Regex.is_type = python_lib_Re.compile("^[A-Z][a-zA-Z0-9_]*$")
hxsublime_tools_HxSrcTools_Regex.comments = python_lib_Re.compile("(//[^\n\r]*?[\n\r]|/\\*(.*?)\\*/)", python_lib_Re.MULTILINE | python_lib_Re.DOTALL)
hxsublime_tools_HxSrcTools_Regex._field = python_lib_Re.compile("((?:(?:public|static|inline|private)\\s+)*)(var|function)\\s+([a-zA-Z_][a-zA-Z0-9_]*)", python_lib_Re.MULTILINE)
hxsublime_tools_HxSrcTools_Regex._type_decl_with_scope = python_lib_Re.compile("(private\\s+)?(extern\\s+)?(class|typedef|enum|interface|abstract)\\s+([A-Z][a-zA-Z0-9_]*)\\s*(<[a-zA-Z0-9,_]+>)?(:?\\{|\\s+)", python_lib_Re.M)
hxsublime_tools_HxSrcTools_Regex.enum_constructor_start_decl = python_lib_Re.compile("\\s+([a-zA-Z_]+)", python_lib_Re.M)


hxsublime_tools_HxSrcTools_Regex._hx_class = hxsublime_tools_HxSrcTools_Regex
hxsublime_tools_HxSrcTools_Regex._hx_class_name = "hxsublime.tools.Regex"
_hx_classes['hxsublime.tools.Regex'] = hxsublime_tools_HxSrcTools_Regex
hxsublime_tools_HxSrcTools_Regex._hx_fields = []
hxsublime_tools_HxSrcTools_Regex._hx_props = []
hxsublime_tools_HxSrcTools_Regex._hx_methods = []
hxsublime_tools_HxSrcTools_Regex._hx_statics = ["compact_func","compact_prop","space_chars","word_chars","import_line","using_line","package_line","type_decl_with_scope","type_decl","enum_start_decl","skippable","in_anonymous","variables","functions","named_functions","function_params","param_default","is_type","comments","_field","_type_decl_with_scope","enum_constructor_start_decl"]
hxsublime_tools_HxSrcTools_Regex._hx_interfaces = []

# print hxsublime.tools.HxSrcTools.HxSrcTools
class hxsublime_tools_HxSrcTools:

	pass




def HxSrcTools_statics_get_types_from_src(src,module_name,file,src_with_comments):
	if module_name is None:
		_this = python_lib_os_Path.splitext(python_lib_os_Path.basename(file))
		module_name = _this[0]
	
	
	pack = hxsublime_tools_HxSrcTools.get_package(src)
	res = haxe_ds_StringMap()
	def _hx_local_0():
		p = hxsublime_tools_HxSrcTools_Regex._type_decl_with_scope.finditer(src)
		return python_Lib_HaxeIterator(p)
	
	_it = _hx_local_0()
	while _it.hasNext():
		decl = _it.next()
		is_private = decl.group(1) is not None
		type_name = decl.group(4)
		if type_name == "NME_":
			haxe_Log.trace(Std.string(decl.group(0)), _Hx_AnonObject(fileName = "HxSrcTools.hx" ,lineNumber = 69 ,className = "hxsublime.tools.HxSrcTools" ,methodName = "get_types_from_src" ))
		
		kind = decl.group(3)
		is_extern = decl.group(2) is not None
		is_module_type = type_name == module_name
		is_std_type = module_name == "StdTypes"
		full_type = hxsublime_tools_HxSrcTools_HaxeType(pack, module_name, type_name, kind, is_private, is_module_type, is_std_type, is_extern, file, src, src_with_comments, decl)
		if full_type.is_enum():
			full_type._enum_constructors = hxsublime_tools_HxSrcTools._extract_enum_constructors_from_src(src, decl.end(4))
		
		if not res.exists(full_type.full_qualified_name()):
			res.set(full_type.full_qualified_name(), full_type)
		
		
	
	
	return hxsublime_tools_HxSrcTools_HaxeTypeBundle(res)
	
hxsublime_tools_HxSrcTools.get_types_from_src = HxSrcTools_statics_get_types_from_src
def HxSrcTools_statics__extract_enum_constructors_from_src(src,start_pos):
	constructors = None
	start = hxsublime_tools_HxSrcTools.search_next_char_on_same_nesting_level(src, ["{"], start_pos)
	if start is not None:
		end = hxsublime_tools_HxSrcTools.search_next_char_on_same_nesting_level(src, ["}"], start[0] + 1)
		if end is not None:
			def _hx_local_0():
				startIndex = start[0] + 1
				endIndex = end[0] - 1
				return python_Tools.substring(src, startIndex, endIndex)
			
			constructors = hxsublime_tools_HxSrcTools._extract_enum_constructors_from_enum(_hx_local_0())
		
		
	
	
	return constructors
	
hxsublime_tools_HxSrcTools._extract_enum_constructors_from_src = HxSrcTools_statics__extract_enum_constructors_from_src
def HxSrcTools_statics__extract_enum_constructors_from_enum(enumStr):
	constructors = []
	start = 0
	while True:
		m = hxsublime_tools_HxSrcTools_Regex.enum_constructor_start_decl.match(enumStr, start)
		if m is not None:
			constructor = m.group(1)
			constructors.append(constructor)
			__builtin__.len(constructors)
			
			end = hxsublime_tools_HxSrcTools.search_next_char_on_same_nesting_level(enumStr, [";"], m.end(1))
			if end is not None:
				start = end[0] + 1
			else:
				break
		
		else:
			break
	
	return constructors
	
hxsublime_tools_HxSrcTools._extract_enum_constructors_from_enum = HxSrcTools_statics__extract_enum_constructors_from_enum
def HxSrcTools_statics_skip_whitespace_or_comments(hx_src_section,start_pos):
	in_single_comment = False
	in_multi_comment = False
	count = __builtin__.len(hx_src_section)
	pos = start_pos
	while True:
		if pos > count - 1:
			break
		
		c = hx_src_section[pos]
		next = None
		if pos < count - 1:
			next = hx_src_section[pos + 1]
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
			b = python_Tools.substring(hx_src_section, start_pos, pos)
			return (pos, b)
		
	
	return None
	
hxsublime_tools_HxSrcTools.skip_whitespace_or_comments = HxSrcTools_statics_skip_whitespace_or_comments
def HxSrcTools_statics_is_same_nesting_level_at_pos(hx_src_section,end_pos,start_pos):
	if end_pos < start_pos:
		return False
	
	open_pars = 0
	open_braces = 0
	open_brackets = 0
	open_angle_brackets = 0
	in_string = False
	string_char = None
	in_regexp = False
	count = __builtin__.len(hx_src_section)
	cur = ""
	pos = start_pos
	while True:
		if pos == end_pos or pos > count - 1:
			return open_pars == 0 and open_braces == 0 and open_brackets == 0 and open_angle_brackets == 0 and not in_string and not in_regexp
		
		c = hx_src_section[pos]
		next = None
		if pos < count - 1:
			next = hx_src_section[pos + 1]
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
		
	
	return False
	
hxsublime_tools_HxSrcTools.is_same_nesting_level_at_pos = HxSrcTools_statics_is_same_nesting_level_at_pos
def HxSrcTools_statics_search_next_char_on_same_nesting_level(hx_src_section,chars,start_pos):
	open_pars = 0
	open_braces = 0
	open_brackets = 0
	open_angle_brackets = 0
	in_string = False
	string_char = None
	in_regexp = False
	count = __builtin__.len(hx_src_section)
	cur = ""
	pos = start_pos
	while True:
		if pos > count - 1:
			break
		
		c = hx_src_section[pos]
		next = None
		if pos < count - 1:
			next = hx_src_section[pos + 1]
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
		
		
		if c in chars and open_pars == 0 and open_braces == 0 and open_brackets == 0 and open_angle_brackets == 0:
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
	
hxsublime_tools_HxSrcTools.search_next_char_on_same_nesting_level = HxSrcTools_statics_search_next_char_on_same_nesting_level
def HxSrcTools_statics_reverse_search_next_char_on_same_nesting_level(hx_src_section,chars,start_pos):
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
		
		c = hx_src_section[pos]
		next = None
		if pos > 0:
			next = hx_src_section[pos - 1]
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
		
		
		if c in chars and open_pars == 0 and open_braces == 0 and open_brackets == 0 and open_angle_brackets == 0:
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
def HxSrcTools_statics_strip_comments(src):
	return hxsublime_tools_HxSrcTools_Regex.comments.sub("", src)
hxsublime_tools_HxSrcTools.strip_comments = HxSrcTools_statics_strip_comments
def HxSrcTools_statics_get_package(src):
	pack = ""
	all = python_lib_Re_RegexHelper.findallDynamic(hxsublime_tools_HxSrcTools_Regex.package_line, src, None, None)
	_g = 0
	while _g < len(all):
		ps = all[_g]
		_g = _g + 1
		pack = ps
	
	
	return pack
	
hxsublime_tools_HxSrcTools.get_package = HxSrcTools_statics_get_package
def HxSrcTools_statics_split_function_signature(signature):
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
	
hxsublime_tools_HxSrcTools.split_function_signature = HxSrcTools_statics_split_function_signature
def HxSrcTools_statics_empty_type_bundle():
	return hxsublime_tools_HxSrcTools_HaxeTypeBundle(haxe_ds_StringMap())
hxsublime_tools_HxSrcTools.empty_type_bundle = HxSrcTools_statics_empty_type_bundle


hxsublime_tools_HxSrcTools._hx_class = hxsublime_tools_HxSrcTools
hxsublime_tools_HxSrcTools._hx_class_name = "hxsublime.tools.HxSrcTools"
_hx_classes['hxsublime.tools.HxSrcTools'] = hxsublime_tools_HxSrcTools
hxsublime_tools_HxSrcTools._hx_fields = []
hxsublime_tools_HxSrcTools._hx_props = []
hxsublime_tools_HxSrcTools._hx_methods = []
hxsublime_tools_HxSrcTools._hx_statics = ["get_types_from_src","_extract_enum_constructors_from_src","_extract_enum_constructors_from_enum","skip_whitespace_or_comments","is_same_nesting_level_at_pos","search_next_char_on_same_nesting_level","reverse_search_next_char_on_same_nesting_level","strip_comments","get_package","split_function_signature","empty_type_bundle"]
hxsublime_tools_HxSrcTools._hx_interfaces = []

# print hxsublime.tools.HxSrcTools.HaxeModule
class hxsublime_tools_HxSrcTools_HaxeModule:


	def __init__(self,pack,name,file):
		self.pack = pack
		self.name = name
		self.file = file
	
	# var pack
	# var name
	# var file






hxsublime_tools_HxSrcTools_HaxeModule._hx_class = hxsublime_tools_HxSrcTools_HaxeModule
hxsublime_tools_HxSrcTools_HaxeModule._hx_class_name = "hxsublime.tools.HaxeModule"
_hx_classes['hxsublime.tools.HaxeModule'] = hxsublime_tools_HxSrcTools_HaxeModule
hxsublime_tools_HxSrcTools_HaxeModule._hx_fields = ["pack","name","file"]
hxsublime_tools_HxSrcTools_HaxeModule._hx_props = []
hxsublime_tools_HxSrcTools_HaxeModule._hx_methods = []
hxsublime_tools_HxSrcTools_HaxeModule._hx_statics = []
hxsublime_tools_HxSrcTools_HaxeModule._hx_interfaces = []

# print hxsublime.tools.HxSrcTools.HaxeTypeBundle
class hxsublime_tools_HxSrcTools_HaxeTypeBundle:


	def __init__(self,types):
		self._types = types
	# var _types
	def toString(self):
		return "HaxeTypeBundle(\n" + self._types.toString() + "\n)"

	def merge(self,other):
		res = None
		_g = haxe_ds_StringMap()
		_it = self._types.keys()
		while _it.hasNext():
			k = _it.next()
			value = self._types.get(k)
			_g.set(k, value)
			
		
		
		res = _g
		
		_it = other._types.keys()
		while _it.hasNext():
			k = _it.next()
			res.set(k, other._types.get(k))
		
		
		return hxsublime_tools_HxSrcTools_HaxeTypeBundle(res)
	

	def packs(self):
		res = haxe_ds_StringMap()
		_it = self._types.keys()
		while _it.hasNext():
			k = _it.next()
			p = self._types.get(k).pack
			if p != "":
				res.set(p, None)
			
			
		
		
		def _hx_local_1():
			def _hx_local_0():
				return res.keys()
			return Lambda.array(_Hx_AnonObject(iterator = _hx_local_0 ))
		
		return _hx_local_1()
	

	def all_modules(self):
		res = haxe_ds_StringMap()
		_it = self._types.keys()
		while _it.hasNext():
			k = _it.next()
			t = self._types.get(k)
			res.set(t.full_pack_with_module(), hxsublime_tools_HxSrcTools_HaxeModule(t.pack, t.module, t.file()))
			
		
		
		return res
	

	def all_modules_list(self):
		mods = self.all_modules()
		_g = []
		_it = HxOverrides_iterator(mods)
		while _it.hasNext():
			m = _it.next()
			_g.append(m)
			__builtin__.len(_g)
			
		
		
		return _g
		
	

	def all_types_and_enum_constructors_with_info(self):
		res = haxe_ds_StringMap()
		_it = self._types.keys()
		while _it.hasNext():
			k = _it.next()
			t = self._types.get(k)
			if t.is_enum():
				_g = 0
				_g1 = t.full_qualified_enum_constructors_with_optional_module()
				while _g < len(_g1):
					ec = _g1[_g]
					_g = _g + 1
					res.set(ec, t)
				
			
			
			fq_name = t.full_qualified_name_with_optional_module()
			res.set(fq_name, t)
			
		
		
		return res
	

	def all_types_and_enum_constructors(self):
		res = self.all_types_and_enum_constructors_with_info()
		_g = []
		_it = res.keys()
		while _it.hasNext():
			k = _it.next()
			_g.append(k)
			__builtin__.len(_g)
			
		
		
		return _g
		
	

	def all_types(self):
		_g = []
		_it = HxOverrides_iterator(self._types)
		while _it.hasNext():
			v = _it.next()
			_g.append(v)
			__builtin__.len(_g)
			
		
		
		return _g
	

	def filter(self,fn):
		res = haxe_ds_StringMap()
		_it = self._types.keys()
		while _it.hasNext():
			k = _it.next()
			t = self._types.get(k)
			if fn(t):
				res.set(k, t)
			
			
		
		
		return hxsublime_tools_HxSrcTools_HaxeTypeBundle(res)
	

	def filter_by_classpath(self,cp):
		def _hx_local_1():
			def _hx_local_0(p):
				return p.classpath() == cp
			return self.filter(_hx_local_0)
		
		return _hx_local_1()
	

	def filter_by_classpaths(self,cps):
		def _hx_local_1():
			def _hx_local_0(p):
				return Lambda.has(cps, p.classpath())
			return self.filter(_hx_local_0)
		
		return _hx_local_1()
	







hxsublime_tools_HxSrcTools_HaxeTypeBundle._hx_class = hxsublime_tools_HxSrcTools_HaxeTypeBundle
hxsublime_tools_HxSrcTools_HaxeTypeBundle._hx_class_name = "hxsublime.tools.HaxeTypeBundle"
_hx_classes['hxsublime.tools.HaxeTypeBundle'] = hxsublime_tools_HxSrcTools_HaxeTypeBundle
hxsublime_tools_HxSrcTools_HaxeTypeBundle._hx_fields = ["_types"]
hxsublime_tools_HxSrcTools_HaxeTypeBundle._hx_props = []
hxsublime_tools_HxSrcTools_HaxeTypeBundle._hx_methods = ["toString","merge","packs","all_modules","all_modules_list","all_types_and_enum_constructors_with_info","all_types_and_enum_constructors","all_types","filter","filter_by_classpath","filter_by_classpaths"]
hxsublime_tools_HxSrcTools_HaxeTypeBundle._hx_statics = []
hxsublime_tools_HxSrcTools_HaxeTypeBundle._hx_interfaces = []

# print hxsublime.tools.HxSrcTools.EnumConstructor
class hxsublime_tools_HxSrcTools_EnumConstructor:


	def __init__(self,name,enum_type):
		self.name = name
		self.enumType = enum_type
	
	# var name
	# var enumType
	def to_snippet_insert(self,import_list,insert_file):
		_g = 0
		while _g < len(import_list):
			i = import_list[_g]
			_g = _g + 1
			if self.enumType.file() == insert_file or i == self.enumType.full_qualified_name_with_optional_module() or i == self.enumType.full_pack_with_module() or i == self.enumType.full_qualified_name_with_optional_module() + "." + self.name:
				return self.name
			
		
		
		return self.enumType.full_qualified_name_with_optional_module() + "." + self.name
	

	def type_hint(self):
		return "enum value"

	def to_snippet(self,insert_file,import_list):
		location = None
		def _hx_local_1():
			def _hx_local_0():
				_this = self.enumType.full_pack_with_optional_module()
				return __builtin__.len(_this)
			
			return _hx_local_0() > 0
		
		if _hx_local_1():
			location = " (" + self.enumType.full_pack_with_optional_module() + ")"
		else:
			location = ""
		display = self.enumType.name + "." + self.name + location + "\t" + self.type_hint()
		insert = self.to_snippet_insert(import_list, insert_file)
		return (display, insert)
	

	def toString(self):
		return self.name







hxsublime_tools_HxSrcTools_EnumConstructor._hx_class = hxsublime_tools_HxSrcTools_EnumConstructor
hxsublime_tools_HxSrcTools_EnumConstructor._hx_class_name = "hxsublime.tools.EnumConstructor"
_hx_classes['hxsublime.tools.EnumConstructor'] = hxsublime_tools_HxSrcTools_EnumConstructor
hxsublime_tools_HxSrcTools_EnumConstructor._hx_fields = ["name","enumType"]
hxsublime_tools_HxSrcTools_EnumConstructor._hx_props = []
hxsublime_tools_HxSrcTools_EnumConstructor._hx_methods = ["to_snippet_insert","type_hint","to_snippet","toString"]
hxsublime_tools_HxSrcTools_EnumConstructor._hx_statics = []
hxsublime_tools_HxSrcTools_EnumConstructor._hx_interfaces = []

# print hxsublime.tools.HxSrcTools.HaxeField
class hxsublime_tools_HxSrcTools_HaxeField:


	def __init__(self,type,name,kind,is_static,is_public,is_inline,is_private,match_decl):
		self._is_function = None
		self._file = None
		self._src_pos = None
		self.type = type
		self.name = name
		self.kind = kind
		self.is_static = is_static
		self.is_public = is_public
		self.is_inline = is_inline
		self.is_private = is_private
		self.match_decl = match_decl
	
	# var type
	# var name
	# var kind
	# var is_static
	# var is_public
	# var is_inline
	# var is_private
	# var match_decl
	# var _src_pos
	def src_pos(self):
		if self._src_pos is None:
			def _hx_local_0():
				p = hxsublime_tools_HxSrcTools_Regex._field.finditer(self.type.src_with_comments)
				return python_Lib_HaxeIterator(p)
			
			_it = _hx_local_0()
			while _it.hasNext():
				decl = _it.next()
				if decl.group(0) == self.match_decl.group(0):
					self._src_pos = decl.start(0)
					return self._src_pos
				
				
			
		
		
		return self._src_pos
	

	# var _is_var
	def is_var(self):
		if self._is_var is None:
			self._is_var = self.kind == "var"
		
		return self._is_var
	

	# var _file
	def file(self):
		if self._file is None:
			self._file = self.type.file()
		
		return self._file
	

	# var _is_function
	def is_function(self):
		if self._is_function is None:
			self._is_function = self.kind == "function"
		
		return self._is_function
	

	def toString(self):
		def _hx_local_3():
			def _hx_local_2():
				def _hx_local_1():
					def _hx_local_0():
						return "::" if self.is_static or self.name == "new" else "."
					return self.type.full_qualified_name_with_optional_module() + (_hx_local_0())
				
				return _hx_local_1() + self.name
			
			return _hx_local_2()
		
		return _hx_local_3()
	

	def to_expression(self):
		return self.type.full_qualified_name_with_optional_module() + "." + self.name





hxsublime_tools_HxSrcTools_HaxeField.__meta__ = _Hx_AnonObject(fields = _Hx_AnonObject(src_pos = _Hx_AnonObject(lazyprop = None ) ,is_var = _Hx_AnonObject(lazyprop = None ) ,file = _Hx_AnonObject(property = None ) ,is_function = _Hx_AnonObject(lazyprop = None ) ) )


hxsublime_tools_HxSrcTools_HaxeField._hx_class = hxsublime_tools_HxSrcTools_HaxeField
hxsublime_tools_HxSrcTools_HaxeField._hx_class_name = "hxsublime.tools.HaxeField"
_hx_classes['hxsublime.tools.HaxeField'] = hxsublime_tools_HxSrcTools_HaxeField
hxsublime_tools_HxSrcTools_HaxeField._hx_fields = ["type","name","kind","is_static","is_public","is_inline","is_private","match_decl","_src_pos","_is_var","_file","_is_function"]
hxsublime_tools_HxSrcTools_HaxeField._hx_props = []
hxsublime_tools_HxSrcTools_HaxeField._hx_methods = ["src_pos","is_var","file","is_function","toString","to_expression"]
hxsublime_tools_HxSrcTools_HaxeField._hx_statics = ["__meta__"]
hxsublime_tools_HxSrcTools_HaxeField._hx_interfaces = []

# print hxsublime.tools.HxSrcTools.HaxeType
class hxsublime_tools_HxSrcTools_HaxeType:


	def __init__(self,pack,module,name,kind,is_private,is_module_type,is_std_type,is_extern,file,src,src_with_comments,match_decl):
		self._full_qualified_name = None
		self._classpath = None
		self._full_qualified_enum_constructors_with_optional_module = None
		self._lazy_enum_constructors = None
		self._full_qualified_name_with_optional_module = None
		self._pack_suffix = None
		self._pack_list = None
		self._full_pack_with_module = None
		self._full_pack_with_optional_module = None
		self._toplevel_pack = None
		self._toplevel_pack_set = False
		self._src_pos_set = False
		self._src_pos = None
		self._stripped_end_decl_pos_set = False
		self._stripped_end_decl_pos = None
		self._class_body_start_set = False
		self._class_body_start = None
		self._public_static_functions = None
		self._public_static_vars = None
		self._all_fields_list = None
		self._all_fields = None
		self._public_static_fields = None
		self._class_body = None
		self._stripped_start_decl_pos = None
		self._src = src
		self.src_with_comments = src_with_comments
		self.match_decl = match_decl
		self.is_private = is_private
		self.pack = pack
		self.module = module
		self.kind = kind
		self.name = name
		self.is_module_type = is_module_type
		self.is_std_type = is_std_type
		self.is_extern = is_extern
		self._file = file
		self._enum_constructors = None
	
	# var _src
	# var src_with_comments
	# var match_decl
	# var is_private
	# var pack
	# var module
	# var kind
	# var name
	# var is_module_type
	# var is_std_type
	# var is_extern
	# var _file
	# var _enum_constructors
	def src(self):
		return self._src

	def file(self):
		return self._file

	# var _stripped_start_decl_pos
	def stripped_start_decl_pos(self):
		if self._stripped_start_decl_pos is None:
			self._stripped_start_decl_pos = self.match_decl.start(0)
		
		return self._stripped_start_decl_pos
	

	# var _class_body
	def class_body(self):
		if self._class_body is None:
			res = None
			if self.stripped_end_decl_pos is None:
				res = ""
			else:
				_this = self.src()
				startIndex = self.stripped_start_decl_pos()
				endIndex = self.stripped_end_decl_pos()
				res = python_Tools.substring(_this, startIndex, endIndex)
			
			self._class_body = res
		
		
		return self._class_body
	

	# var _public_static_fields
	def public_static_fields(self):
		if self._public_static_fields is None:
			res = []
			x = self.public_static_vars()
			res.extend(x)
			
			x = self.public_static_functions()
			res.extend(x)
			
			self._public_static_fields = res
		
		
		return self._public_static_fields
	

	# var _all_fields
	def all_fields(self):
		if self._all_fields is None:
			res = haxe_ds_StringMap()
			if self.class_body is not None:
				def _hx_local_0():
					p = hxsublime_tools_HxSrcTools_Regex._field.finditer(self.class_body())
					return python_Lib_HaxeIterator(p)
				
				_it = _hx_local_0()
				while _it.hasNext():
					decl = _it.next()
					modifiers = decl.group(1)
					is_static = modifiers is not None and modifiers.find("static") > -1
					is_inline = modifiers is not None and modifiers.find("inline") > -1
					is_private = modifiers is not None and modifiers.find("private") > -1
					is_public = modifiers is not None and modifiers.find("public") > -1
					kind = decl.group(2)
					name = decl.group(3)
					if name == "WAIT_END_RET":
						haxe_Log.trace(modifiers, _Hx_AnonObject(fileName = "HxSrcTools.hx" ,lineNumber = 1082 ,className = "hxsublime.tools.HaxeType" ,methodName = "all_fields" ))
					
					def _hx_local_2():
						def _hx_local_1():
							_this = self.class_body_start()
							return _this[0]
						
						return is_private or is_public or is_static or self.is_extern or hxsublime_tools_HxSrcTools.is_same_nesting_level_at_pos(self.class_body(), decl.start(0), _hx_local_1())
					
					if _hx_local_2():
						res.set(name, hxsublime_tools_HxSrcTools_HaxeField(self, name, kind, is_static, is_public, is_inline, is_private, decl))
					
					
				
			
			
			self._all_fields = res
		
		
		return self._all_fields
	

	# var _all_fields_list
	def all_fields_list(self):
		if self._all_fields_list is None:
			all = self.all_fields()
			_g = []
			_it = all.keys()
			while _it.hasNext():
				k = _it.next()
				x = all.get(k)
				_g.append(x)
				__builtin__.len(_g)
				
				
			
			
			self._all_fields_list = _g
			
		
		
		return self._all_fields_list
	

	# var _public_static_vars
	def public_static_vars(self):
		if self._public_static_vars is None:
			all = self.all_fields()
			_g = []
			_it = all.keys()
			while _it.hasNext():
				k = _it.next()
				if all.get(k).is_static and all.get(k).is_var():
					x = all.get(k)
					_g.append(x)
					__builtin__.len(_g)
					
				
				
			
			
			self._public_static_vars = _g
			
		
		
		return self._public_static_vars
	

	# var _public_static_functions
	def public_static_functions(self):
		if self._public_static_functions is None:
			all = self.all_fields()
			_g = []
			_it = all.keys()
			while _it.hasNext():
				k = _it.next()
				if all.get(k).is_static and all.get(k).is_function():
					x = all.get(k)
					_g.append(x)
					__builtin__.len(_g)
					
				
				
			
			
			self._public_static_functions = _g
			
		
		
		return self._public_static_functions
	

	# var _class_body_start
	# var _class_body_start_set
	def class_body_start(self):
		if not self._class_body_start_set:
			self._class_body_start_set = True
			start = self.match_decl.start(0)
			if self.is_abstract() or self.is_class():
				self._class_body_start = hxsublime_tools_HxSrcTools.search_next_char_on_same_nesting_level(self.src(), ["{"], start)
			else:
				self._class_body_start = (0, "")
		
		
		return self._class_body_start
	

	# var _stripped_end_decl_pos
	# var _stripped_end_decl_pos_set
	def stripped_end_decl_pos(self):
		if not self._stripped_end_decl_pos_set:
			self._stripped_end_decl_pos_set = True
			class_body_start = self.class_body_start()
			res = None
			if class_body_start is not None:
				class_body_end = hxsublime_tools_HxSrcTools.search_next_char_on_same_nesting_level(self.src(), ["}"], class_body_start[0] + 1)
				if class_body_end is not None:
					res = class_body_end[0]
				else:
					res = None
			
			else:
				res = None
			self._stripped_end_decl_pos = res
		
		
		return self._stripped_end_decl_pos
	

	# var _src_pos
	# var _src_pos_set
	def src_pos(self):
		if not self._src_pos_set:
			self._src_pos_set = True
			def _hx_local_0():
				p = hxsublime_tools_HxSrcTools_Regex.type_decl_with_scope.finditer(self.src_with_comments)
				return python_Lib_HaxeIterator(p)
			
			_it = _hx_local_0()
			while _it.hasNext():
				decl = _it.next()
				if decl.group(0) == self.match_decl.group(0):
					self._src_pos = decl.start(0)
					return self._src_pos
				
				
			
			
		
		
		return self._src_pos
	

	def to_snippet(self,insert_file,import_list):
		location = None
		def _hx_local_1():
			def _hx_local_0():
				_this = self.full_pack_with_optional_module()
				return __builtin__.len(_this)
			
			return _hx_local_0() > 0
		
		if _hx_local_1():
			location = " (" + self.full_pack_with_optional_module() + ")"
		else:
			location = ""
		display = self.name + location + "\t" + self.type_hint()
		insert = self.to_snippet_insert(import_list, insert_file)
		return (display, insert)
	

	def to_snippets(self,import_list,insert_file):
		res = [self.to_snippet(insert_file, import_list)]
		if self.is_enum() and self._enum_constructors is not None:
			x = None
			_g = []
			_g1 = 0
			_g2 = self.enum_constructors()
			while _g1 < len(_g2):
				ev = _g2[_g1]
				_g1 = _g1 + 1
				x1 = ev.to_snippet(insert_file, import_list)
				_g.append(x1)
				__builtin__.len(_g)
				
			
			
			x = _g
			
			res.extend(x)
		
		
		return res
	

	def to_snippet_insert(self,import_list,insert_file):
		_g = 0
		while _g < len(import_list):
			i = import_list[_g]
			_g = _g + 1
			if self._file == insert_file or i == self.full_pack_with_module() or i == self.full_qualified_name_with_optional_module() or i == self.full_qualified_name():
				return self.name
			
		
		
		return self.full_qualified_name_with_optional_module()
	

	# var _toplevel_pack_set
	# var _toplevel_pack
	def toplevel_pack(self):
		if not self._toplevel_pack_set:
			self._toplevel_pack_set = True
			pl = self.pack_list()
			if __builtin__.len(pl) > 0:
				self._toplevel_pack = pl[0]
			
		
		
		return self._toplevel_pack
	

	def type_hint(self):
		return self.kind

	# var _full_pack_with_optional_module
	def full_pack_with_optional_module(self):
		if self._full_pack_with_optional_module is None:
			mod = None
			if self.is_module_type or self.is_std_type:
				mod = ""
			else:
				mod = self.pack_suffix() + self.module
			self._full_pack_with_optional_module = self.pack + mod
		
		
		return self._full_pack_with_optional_module
	

	# var _full_pack_with_module
	def full_pack_with_module(self):
		if self._full_pack_with_module is None:
			self._full_pack_with_module = self.pack + self.pack_suffix() + self.module
		
		return self._full_pack_with_module
	

	def is_enum(self):
		return self.kind == "enum"

	def is_class(self):
		return self.kind == "class"

	def is_abstract(self):
		return self.kind == "abstract"

	def __repr__(self):
		return self.toString()

	# var _pack_list
	def pack_list(self):
		if self._pack_list is None:
			if __builtin__.len(self.pack) > 0:
				self._pack_list = self.pack.split(".")
			else:
				self._pack_list = []
		
		return self._pack_list
	

	# var _pack_suffix
	def pack_suffix(self):
		if self._pack_suffix is None:
			if __builtin__.len(self.pack) == 0:
				self._pack_suffix = ""
			else:
				self._pack_suffix = "."
		
		return self._pack_suffix
	

	# var _full_qualified_name_with_optional_module
	def full_qualified_name_with_optional_module(self):
		if self._full_qualified_name_with_optional_module is None:
			mod = None
			if self.is_module_type or self.is_std_type:
				mod = ""
			else:
				mod = self.module + "."
			self._full_qualified_name_with_optional_module = self.pack + self.pack_suffix() + mod + self.name
		
		
		return self._full_qualified_name_with_optional_module
	

	# var _lazy_enum_constructors
	def enum_constructors(self):
		if self._lazy_enum_constructors is None:
			res = None
			if self.is_enum() and self._enum_constructors is not None:
				_g = []
				_g1 = 0
				_g2 = self._enum_constructors
				while _g1 < len(_g2):
					e = _g2[_g1]
					_g1 = _g1 + 1
					x = hxsublime_tools_HxSrcTools_EnumConstructor(e, self)
					_g.append(x)
					__builtin__.len(_g)
					
				
				
				res = _g
			
			else:
				res = []
			self._lazy_enum_constructors = res
		
		
		return self._lazy_enum_constructors
	

	# var _full_qualified_enum_constructors_with_optional_module
	def full_qualified_enum_constructors_with_optional_module(self):
		if self._full_qualified_enum_constructors_with_optional_module is None:
			res = None
			if not self.is_enum() or self._enum_constructors is None:
				res = []
			else:
				fqName = self.full_qualified_name_with_optional_module()
				_g = []
				_g1 = 0
				_g2 = self._enum_constructors
				while _g1 < len(_g2):
					e = _g2[_g1]
					_g1 = _g1 + 1
					_g.append(fqName + "." + e)
					__builtin__.len(_g)
				
				
				res = _g
				
			
			self._full_qualified_enum_constructors_with_optional_module = res
		
		
		return self._full_qualified_enum_constructors_with_optional_module
	

	# var _classpath
	def classpath(self):
		if self._classpath is None:
			path_append = None
			_g = []
			_g1 = 0
			_g2 = self.pack_list()
			while _g1 < len(_g2):
				_ = _g2[_g1]
				_g1 = _g1 + 1
				_g.append("..")
				__builtin__.len(_g)
			
			
			path_append = _g
			
			mod_dir = python_lib_os_Path.dirname(self._file)
			fp = [mod_dir]
			fp.extend(path_append)
			full_dir = python_lib_Os.sep.join(fp)
			self._classpath = python_lib_os_Path.normpath(full_dir)
		
		
		return self._classpath
	

	# var _full_qualified_name
	def full_qualified_name(self):
		if self._full_qualified_name is None:
			self._full_qualified_name = self.pack + self.pack_suffix() + self.module + "." + self.name
		
		return self._full_qualified_name
	

	def toString(self):
		def _hx_local_24():
			def _hx_local_23():
				def _hx_local_22():
					def _hx_local_21():
						def _hx_local_20():
							def _hx_local_19():
								def _hx_local_18():
									def _hx_local_17():
										def _hx_local_16():
											def _hx_local_15():
												def _hx_local_14():
													def _hx_local_13():
														def _hx_local_12():
															def _hx_local_11():
																def _hx_local_10():
																	def _hx_local_9():
																		def _hx_local_8():
																			def _hx_local_7():
																				def _hx_local_6():
																					def _hx_local_5():
																						def _hx_local_4():
																							def _hx_local_3():
																								def _hx_local_0():
																									_this = self.enum_constructors()
																									def _hx_local_2():
																										def _hx_local_1(ec):
																											return ec.toString()
																										return __builtin__.list(__builtin__.map(_hx_local_1, _this))
																									
																									return _hx_local_2()
																								
																								return "{" + " pack:" + Std.string(self.pack) + ", " + " module:" + Std.string(self.module) + ", " + " name:" + Std.string(self.name) + ", " + " kind:" + Std.string(self.kind) + ", " + " enum_constructors:" + Std.string(_hx_local_0())
																							
																							return _hx_local_3() + ", "
																						
																						return _hx_local_4() + " is_private:"
																					
																					return _hx_local_5() + Std.string(self.is_private)
																				
																				return _hx_local_6() + ", "
																			
																			return _hx_local_7() + " is_module_type:"
																		
																		return _hx_local_8() + Std.string(self.is_module_type)
																	
																	return _hx_local_9() + ", "
																
																return _hx_local_10() + " is_std_type:"
															
															return _hx_local_11() + Std.string(self.is_std_type)
														
														return _hx_local_12() + ", "
													
													return _hx_local_13() + " is_extern:"
												
												return _hx_local_14() + Std.string(self.is_extern)
											
											return _hx_local_15() + ", "
										
										return _hx_local_16() + " file:'"
									
									return _hx_local_17() + Std.string(self.file())
								
								return _hx_local_18() + "'"
							
							return _hx_local_19() + " classpath:'"
						
						return _hx_local_20() + Std.string(self.classpath())
					
					return _hx_local_21() + "'"
				
				return _hx_local_22() + " }"
			
			return _hx_local_23()
		
		return _hx_local_24()
	





hxsublime_tools_HxSrcTools_HaxeType.__meta__ = _Hx_AnonObject(fields = _Hx_AnonObject(stripped_start_decl_pos = _Hx_AnonObject(lazyprop = None ) ,class_body = _Hx_AnonObject(lazyprop = None ) ,public_static_fields = _Hx_AnonObject(lazyprop = None ) ,all_fields = _Hx_AnonObject(lazyprop = None ) ,all_fields_list = _Hx_AnonObject(lazyprop = None ) ,public_static_vars = _Hx_AnonObject(lazyprop = None ) ,public_static_functions = _Hx_AnonObject(lazyprop = None ) ,class_body_start = _Hx_AnonObject(lazyprop = None ) ,stripped_end_decl_pos = _Hx_AnonObject(lazyprop = None ) ,src_pos = _Hx_AnonObject(lazyprop = None ) ,toplevel_pack = _Hx_AnonObject(lazyprop = None ) ,type_hint = _Hx_AnonObject(lazyprop = None ) ,full_pack_with_optional_module = _Hx_AnonObject(lazyprop = None ) ,full_pack_with_module = _Hx_AnonObject(lazyprop = None ) ,is_enum = _Hx_AnonObject(lazyprop = None ) ,is_class = _Hx_AnonObject(lazyprop = None ) ,is_abstract = _Hx_AnonObject(lazyprop = None ) ,pack_list = _Hx_AnonObject(lazyprop = None ) ,pack_suffix = _Hx_AnonObject(lazyprop = None ) ,full_qualified_name_with_optional_module = _Hx_AnonObject(lazyprop = None ) ,enum_constructors = _Hx_AnonObject(lazyprop = None ) ,full_qualified_enum_constructors_with_optional_module = _Hx_AnonObject(lazyprop = None ) ,classpath = _Hx_AnonObject(lazyprop = None ) ,full_qualified_name = _Hx_AnonObject(lazyprop = None ) ) )


hxsublime_tools_HxSrcTools_HaxeType._hx_class = hxsublime_tools_HxSrcTools_HaxeType
hxsublime_tools_HxSrcTools_HaxeType._hx_class_name = "hxsublime.tools.HaxeType"
_hx_classes['hxsublime.tools.HaxeType'] = hxsublime_tools_HxSrcTools_HaxeType
hxsublime_tools_HxSrcTools_HaxeType._hx_fields = ["_src","src_with_comments","match_decl","is_private","pack","module","kind","name","is_module_type","is_std_type","is_extern","_file","_enum_constructors","_stripped_start_decl_pos","_class_body","_public_static_fields","_all_fields","_all_fields_list","_public_static_vars","_public_static_functions","_class_body_start","_class_body_start_set","_stripped_end_decl_pos","_stripped_end_decl_pos_set","_src_pos","_src_pos_set","_toplevel_pack_set","_toplevel_pack","_full_pack_with_optional_module","_full_pack_with_module","_pack_list","_pack_suffix","_full_qualified_name_with_optional_module","_lazy_enum_constructors","_full_qualified_enum_constructors_with_optional_module","_classpath","_full_qualified_name"]
hxsublime_tools_HxSrcTools_HaxeType._hx_props = []
hxsublime_tools_HxSrcTools_HaxeType._hx_methods = ["src","file","stripped_start_decl_pos","class_body","public_static_fields","all_fields","all_fields_list","public_static_vars","public_static_functions","class_body_start","stripped_end_decl_pos","src_pos","to_snippet","to_snippets","to_snippet_insert","toplevel_pack","type_hint","full_pack_with_optional_module","full_pack_with_module","is_enum","is_class","is_abstract","__repr__","pack_list","pack_suffix","full_qualified_name_with_optional_module","enum_constructors","full_qualified_enum_constructors_with_optional_module","classpath","full_qualified_name","toString"]
hxsublime_tools_HxSrcTools_HaxeType._hx_statics = ["__meta__"]
hxsublime_tools_HxSrcTools_HaxeType._hx_interfaces = []

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
def PathTools_statics_is_abs_path(path):
	return python_lib_os_Path.normpath(path) == python_lib_os_Path.abspath(path)
hxsublime_tools_PathTools.is_abs_path = PathTools_statics_is_abs_path


hxsublime_tools_PathTools._hx_class = hxsublime_tools_PathTools
hxsublime_tools_PathTools._hx_class_name = "hxsublime.tools.PathTools"
_hx_classes['hxsublime.tools.PathTools'] = hxsublime_tools_PathTools
hxsublime_tools_PathTools._hx_fields = []
hxsublime_tools_PathTools._hx_props = []
hxsublime_tools_PathTools._hx_methods = []
hxsublime_tools_PathTools._hx_statics = ["removeDir","joinNorm","is_abs_path"]
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
def StringTools_statics_reverse(s):
	return s[::-1]
hxsublime_tools_StringTools.reverse = StringTools_statics_reverse
def StringTools_statics_isWhitespaceOrEmpty(s):
	return python_lib_Re.match(hxsublime_tools_StringTools._whitespace, s) is not None
hxsublime_tools_StringTools.isWhitespaceOrEmpty = StringTools_statics_isWhitespaceOrEmpty
def StringTools_statics_unicodeToStr(s,encoding,errors = ""):
	if errors is None:
		errors = ""
	
	return s.decode(encoding, errors)
	
hxsublime_tools_StringTools.unicodeToStr = StringTools_statics_unicodeToStr
def StringTools_statics_strToUnicodeToStr(s,encoding1,encoding2):
	return hxsublime_tools_StringTools.unicodeToStr(python_lib_StringTools.encode(s, encoding1), encoding2)
hxsublime_tools_StringTools.strToUnicodeToStr = StringTools_statics_strToUnicodeToStr
def StringTools_statics_strToUnicode(s,encoding,errors = ""):
	if errors is None:
		errors = ""
	
	return python_lib_StringTools.encode(s, encoding, errors)
	
hxsublime_tools_StringTools.strToUnicode = StringTools_statics_strToUnicode
def StringTools_statics_toUnicode(s):
	res = None
	if s is None:
		return None
	else:
		try:
			res = hxsublime_tools_StringTools.strToUnicode(s, "utf-8", "ignore")
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			if True:
				e = _hx_e1
				try:
					res = hxsublime_tools_StringTools.strToUnicode(s, "ascii")
				except Exception as _hx_e:
					_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
					if True:
						e1 = _hx_e1
						try:
							res = hxsublime_tools_StringTools.strToUnicode(s, "iso-8859-1")
						except Exception as _hx_e:
							_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
							if True:
								e2 = _hx_e1
								try:
									res = hxsublime_tools_StringTools.strToUnicode(s, "ascii")
								except Exception as _hx_e:
									_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
									if True:
										e3 = _hx_e1
										raise _HxException("cannot decode str")
									else:
										raise _hx_e
							else:
								raise _hx_e
					else:
						raise _hx_e
			else:
				raise _hx_e
	return res
	
hxsublime_tools_StringTools.toUnicode = StringTools_statics_toUnicode
def StringTools_statics_st3EncodeUtf8(s):
	return hxsublime_tools_StringTools.encodeUtf8(s)
hxsublime_tools_StringTools.st3EncodeUtf8 = StringTools_statics_st3EncodeUtf8
def StringTools_statics_st2EncodeUtf8(s):
	return s
hxsublime_tools_StringTools.st2EncodeUtf8 = StringTools_statics_st2EncodeUtf8
def StringTools_statics_st2ToUnicode(s):
	return s
hxsublime_tools_StringTools.st2ToUnicode = StringTools_statics_st2ToUnicode
def StringTools_statics_encodeUtf8Bytes(s):
	return s.decode("utf-8", "ignore")
hxsublime_tools_StringTools.encodeUtf8Bytes = StringTools_statics_encodeUtf8Bytes
def StringTools_statics_encodeUtf8(s):
	if s is None:
		return None
	
	res = None
	try:
		res = hxsublime_tools_StringTools.strToUnicodeToStr(s, "ascii", "utf-8")
	except Exception as _hx_e:
		_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
		if True:
			e = _hx_e1
			try:
				res = hxsublime_tools_StringTools.strToUnicodeToStr(s, "iso-8859-1", "utf-8")
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				if True:
					e1 = _hx_e1
					raise _HxException("cannot decode str")
				else:
					raise _hx_e
		else:
			raise _hx_e
	return res
	
hxsublime_tools_StringTools.encodeUtf8 = StringTools_statics_encodeUtf8


hxsublime_tools_StringTools._hx_class = hxsublime_tools_StringTools
hxsublime_tools_StringTools._hx_class_name = "hxsublime.tools.StringTools"
_hx_classes['hxsublime.tools.StringTools'] = hxsublime_tools_StringTools
hxsublime_tools_StringTools._hx_fields = []
hxsublime_tools_StringTools._hx_props = []
hxsublime_tools_StringTools._hx_methods = []
hxsublime_tools_StringTools._hx_statics = ["_whitespace","startsWithAny","reverse","isWhitespaceOrEmpty","unicodeToStr","strToUnicodeToStr","strToUnicode","toUnicode","st3EncodeUtf8","st2EncodeUtf8","st2ToUnicode","encodeUtf8Bytes","encodeUtf8"]
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
from builtins import dict as python_lib_Types_Dict
# print hxsublime.tools.ViewTools.AsyncEdit
class hxsublime_tools_ViewTools_AsyncEdit:

	pass




hxsublime_tools_ViewTools_AsyncEdit.dict = python_lib_Types_Dict()
hxsublime_tools_ViewTools_AsyncEdit.id = 0


hxsublime_tools_ViewTools_AsyncEdit._hx_class = hxsublime_tools_ViewTools_AsyncEdit
hxsublime_tools_ViewTools_AsyncEdit._hx_class_name = "hxsublime.tools.AsyncEdit"
_hx_classes['hxsublime.tools.AsyncEdit'] = hxsublime_tools_ViewTools_AsyncEdit
hxsublime_tools_ViewTools_AsyncEdit._hx_fields = []
hxsublime_tools_ViewTools_AsyncEdit._hx_props = []
hxsublime_tools_ViewTools_AsyncEdit._hx_methods = []
hxsublime_tools_ViewTools_AsyncEdit._hx_statics = ["dict","id"]
hxsublime_tools_ViewTools_AsyncEdit._hx_interfaces = []

# print hxsublime.tools.ViewTools.HaxeTextEditCommand
class hxsublime_tools_ViewTools_HaxeTextEditCommand(sublime_TextCommand):


	def __init__(self,v):
		super().__init__(v)
	def run(self,edit,**args):
		if args is None:
			args = None
		
		d = args
		id = d.get("id", None)
		haxe_Log.trace(id, _Hx_AnonObject(fileName = "ViewTools.hx" ,lineNumber = 37 ,className = "hxsublime.tools.HaxeTextEditCommand" ,methodName = "run" ))
		if python_lib_Types_DictImpl.hasKey(hxsublime_tools_ViewTools_AsyncEdit.dict, id):
			fun = hxsublime_tools_ViewTools_AsyncEdit.dict.get(id, None)
			python_lib_Types_DictImpl.remove(hxsublime_tools_ViewTools_AsyncEdit.dict, id)
			fun(self.view, edit)
		
		
	





hxsublime_tools_ViewTools_HaxeTextEditCommand._async_edit_dict = None;


hxsublime_tools_ViewTools_HaxeTextEditCommand._hx_class = hxsublime_tools_ViewTools_HaxeTextEditCommand
hxsublime_tools_ViewTools_HaxeTextEditCommand._hx_class_name = "hxsublime.tools.HaxeTextEditCommand"
_hx_classes['hxsublime.tools.HaxeTextEditCommand'] = hxsublime_tools_ViewTools_HaxeTextEditCommand
hxsublime_tools_ViewTools_HaxeTextEditCommand._hx_fields = []
hxsublime_tools_ViewTools_HaxeTextEditCommand._hx_props = []
hxsublime_tools_ViewTools_HaxeTextEditCommand._hx_methods = ["run"]
hxsublime_tools_ViewTools_HaxeTextEditCommand._hx_statics = ["_async_edit_dict"]
hxsublime_tools_ViewTools_HaxeTextEditCommand._hx_interfaces = []
hxsublime_tools_ViewTools_HaxeTextEditCommand._hx_super = sublime_TextCommand

# print hxsublime.tools.ViewTools.ViewTools
class hxsublime_tools_ViewTools:

	pass




def ViewTools_statics_insertSnippet(view,snippet):
	def _hx_local_0():
		x = _Hx_AnonObject(contents = snippet )
		def _hx_local_2():
			def _hx_local_1():
				d = python_lib_Types_Dict()
				_g = 0
				_g1 = Reflect.fields(x)
				while _g < len(_g1):
					f = _g1[_g]
					_g = _g + 1
					val = None
					v = None
					try:
						v = __builtin__.getattr(x, f)
					except Exception as _hx_e:
						_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
						if True:
							e = _hx_e1
							None
						else:
							raise _hx_e
					val = v
					
					python_lib_Types_DictImpl.set(d, f, val)
					
				
				
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
	def _hx_local_0():
		id = hxsublime_tools_ViewTools_AsyncEdit.id
		if hxsublime_tools_ViewTools_AsyncEdit.id > 1000000:
			hxsublime_tools_ViewTools_AsyncEdit.id = 0
		else:
			hxsublime_tools_ViewTools_AsyncEdit.id = hxsublime_tools_ViewTools_AsyncEdit.id + 1
		python_lib_Types_DictImpl.set(hxsublime_tools_ViewTools_AsyncEdit.dict, id, doEdit)
		def _hx_local_1():
			x = _Hx_AnonObject(id = id )
			def _hx_local_3():
				def _hx_local_2():
					d = python_lib_Types_Dict()
					_g = 0
					_g1 = Reflect.fields(x)
					while _g < len(_g1):
						f = _g1[_g]
						_g = _g + 1
						val = None
						v = None
						try:
							v = __builtin__.getattr(x, f)
						except Exception as _hx_e:
							_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
							if True:
								e = _hx_e1
								None
							else:
								raise _hx_e
						val = v
						
						python_lib_Types_DictImpl.set(d, f, val)
						
					
					
					return d
				
				return _hx_local_2()
			
			return _hx_local_3()
		
		view.run_command("hxsublime_tools__view_tools__haxe_text_edit", _hx_local_1())
	
	start = _hx_local_0
	sublime_Sublime.set_timeout(start, 10)
	
hxsublime_tools_ViewTools.asyncEdit = ViewTools_statics_asyncEdit
def ViewTools_statics_find_view_by_name(name):
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
	
hxsublime_tools_ViewTools.find_view_by_name = ViewTools_statics_find_view_by_name
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
hxsublime_tools_ViewTools._hx_statics = ["insertSnippet","insertAtCursor","getFirstCursorPos","asyncEdit","find_view_by_name","createMissingFolders","getContentUntilFirstCursor","getContentUntil","getContent","isHxsl","isSupported","isUnsupported","getScopesAt","isHaxe","isHxml","isErazor","isNmml","replaceContent","inHaxeCode","inHaxeString","inHaxeComments"]
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
			def _hx_local_0():
				nonlocal _g
				_hx_r = _g
				_g = _g + 1
				return _hx_r
				
			
			i = _hx_local_0()
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
					def _hx_local_2():
						def _hx_local_1():
							v = None
							try:
								v = __builtin__.getattr(o, f)
							except Exception as _hx_e:
								_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
								if True:
									e = _hx_e1
									None
								else:
									raise _hx_e
							return v
						
						return "" + f + " : " + python_Boot.__string_rec(_hx_local_1(), s + "\t")
					
					x = _hx_local_2()
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
						_hx_r = _g
						_g = _g + 1
						return _hx_r
						
					
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
				def _hx_local_5():
					def _hx_local_4():
						v = None
						try:
							v = __builtin__.getattr(o, f)
						except Exception as _hx_e:
							_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
							if True:
								e = _hx_e1
								None
							else:
								raise _hx_e
						return v
					
					return "" + f + " : " + python_Boot.__string_rec(_hx_local_4(), s + "\t")
				
				x = _hx_local_5()
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
				def _hx_local_7():
					def _hx_local_6():
						v = None
						try:
							v = __builtin__.getattr(o, f)
						except Exception as _hx_e:
							_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
							if True:
								e = _hx_e1
								None
							else:
								raise _hx_e
						return v
					
					return "" + f + " : " + python_Boot.__string_rec(_hx_local_6(), s + "\t")
				
				x = _hx_local_7()
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
			def _hx_local_8(_):
				return True
			python_lib_Inspect.getmembers(o, _hx_local_8)
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
class python_Lib_HaxeIterable:


	def __init__(self,x):
		self.x = x
	# var x
	def iterator(self):
		return python_Lib_HaxeIterator(self.x.__iter__())







python_Lib_HaxeIterable._hx_class = python_Lib_HaxeIterable
python_Lib_HaxeIterable._hx_class_name = "python.HaxeIterable"
_hx_classes['python.HaxeIterable'] = python_Lib_HaxeIterable
python_Lib_HaxeIterable._hx_fields = ["x"]
python_Lib_HaxeIterable._hx_props = []
python_Lib_HaxeIterable._hx_methods = ["iterator"]
python_Lib_HaxeIterable._hx_statics = []
python_Lib_HaxeIterable._hx_interfaces = []

# print python.Lib.HaxeIterator
class python_Lib_HaxeIterator:


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
	







python_Lib_HaxeIterator._hx_class = python_Lib_HaxeIterator
python_Lib_HaxeIterator._hx_class_name = "python.HaxeIterator"
_hx_classes['python.HaxeIterator'] = python_Lib_HaxeIterator
python_Lib_HaxeIterator._hx_fields = ["it","x","checked"]
python_Lib_HaxeIterator._hx_props = []
python_Lib_HaxeIterator._hx_methods = ["next","hasNext"]
python_Lib_HaxeIterator._hx_statics = []
python_Lib_HaxeIterator._hx_interfaces = []

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
		def _hx_local_0():
			it1 = HxOverrides_iterator(it)
			self = None
			def _hx_local_1():
				if it1.hasNext():
					return it1.next()
				else:
					raise _HxException(StopIteration())
			def _hx_local_2():
				return self
			self = _Hx_AnonObject(__next__ = _hx_local_1 ,__iter__ = _hx_local_2 )
			return self
		
		return _Hx_AnonObject(__iter__ = _hx_local_0 )
	
	return _hx_local_3()
	
python_Lib.toPythonIterable = Lib_statics_toPythonIterable
def Lib_statics_toHaxeIterable(it):
	return python_Lib_HaxeIterable(it)
python_Lib.toHaxeIterable = Lib_statics_toHaxeIterable
def Lib_statics_toHaxeIterator(it):
	return python_Lib_HaxeIterator(it)
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
	return python_Lib_HaxeIterator(it)
	
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
# print python.lib.Random._hx_random
import random as _hx_random
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
	return python_Lib_HaxeIterator(p)
python_lib_Types_PyIterator_Impl_.toHaxeIterator = PyIterator_Impl__statics_toHaxeIterator
def PyIterator_Impl__statics_toPyIterable(p):
	return p
python_lib_Types_PyIterator_Impl_.toPyIterable = PyIterator_Impl__statics_toPyIterable


python_lib_Types_PyIterator_Impl_._hx_class = python_lib_Types_PyIterator_Impl_
python_lib_Types_PyIterator_Impl_._hx_class_name = "python.lib._Types._Types.PyIterator_Impl_"
_hx_classes['python.lib._Types._Types.PyIterator_Impl_'] = python_lib_Types_PyIterator_Impl_
python_lib_Types_PyIterator_Impl_._hx_fields = []
python_lib_Types_PyIterator_Impl_._hx_props = []
python_lib_Types_PyIterator_Impl_._hx_methods = []
python_lib_Types_PyIterator_Impl_._hx_statics = ["_new","toHaxeIterator","toPyIterable"]
python_lib_Types_PyIterator_Impl_._hx_interfaces = []

# print python.lib.Types.PyIterable_Impl_
class python_lib_Types_PyIterable_Impl_:

	pass




def PyIterable_Impl__statics_toHaxeIterable(p):
	return python_Lib_HaxeIterable(p)
python_lib_Types_PyIterable_Impl_.toHaxeIterable = PyIterable_Impl__statics_toHaxeIterable
def PyIterable_Impl__statics_iterator(this1):
	_this_x = this1
	return python_Lib_HaxeIterator(_this_x.__iter__())
	
python_lib_Types_PyIterable_Impl_.iterator = PyIterable_Impl__statics_iterator


python_lib_Types_PyIterable_Impl_._hx_class = python_lib_Types_PyIterable_Impl_
python_lib_Types_PyIterable_Impl_._hx_class_name = "python.lib._Types._Types.PyIterable_Impl_"
_hx_classes['python.lib._Types._Types.PyIterable_Impl_'] = python_lib_Types_PyIterable_Impl_
python_lib_Types_PyIterable_Impl_._hx_fields = []
python_lib_Types_PyIterable_Impl_._hx_props = []
python_lib_Types_PyIterable_Impl_._hx_methods = []
python_lib_Types_PyIterable_Impl_._hx_statics = ["toHaxeIterable","iterator"]
python_lib_Types_PyIterable_Impl_._hx_interfaces = []

# print python.lib.Types.IterHelper
class python_lib_Types_IterHelper:

	pass




def IterHelper_statics_iterableToIterator(it):
	_this_x = it
	return python_Lib_HaxeIterator(_this_x.__iter__())
	
python_lib_Types_IterHelper.iterableToIterator = IterHelper_statics_iterableToIterator


python_lib_Types_IterHelper._hx_class = python_lib_Types_IterHelper
python_lib_Types_IterHelper._hx_class_name = "python.lib.IterHelper"
_hx_classes['python.lib.IterHelper'] = python_lib_Types_IterHelper
python_lib_Types_IterHelper._hx_fields = []
python_lib_Types_IterHelper._hx_props = []
python_lib_Types_IterHelper._hx_methods = []
python_lib_Types_IterHelper._hx_statics = ["iterableToIterator"]
python_lib_Types_IterHelper._hx_interfaces = []

# print python.lib.Types.FileDescriptor
# print python.lib.Types.Set
from builtins import set as python_lib_Types_Set
# print python.lib.Types.DictView
# print python.lib.Types.DictImpl
class python_lib_Types_DictImpl:

	pass




def DictImpl_statics_fromObject(x):
	d = python_lib_Types_Dict()
	_g = 0
	_g1 = Reflect.fields(x)
	while _g < len(_g1):
		f = _g1[_g]
		_g = _g + 1
		val = None
		v = None
		try:
			v = __builtin__.getattr(x, f)
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			if True:
				e = _hx_e1
				None
			else:
				raise _hx_e
		val = v
		
		python_lib_Types_DictImpl.set(d, f, val)
		
	
	
	return d
	
python_lib_Types_DictImpl.fromObject = DictImpl_statics_fromObject
def DictImpl_statics_hasKey(d,key):
	return key in d
python_lib_Types_DictImpl.hasKey = DictImpl_statics_hasKey
def DictImpl_statics_remove(d,key):
	del d[key]
python_lib_Types_DictImpl.remove = DictImpl_statics_remove
def DictImpl_statics_set(d,key,val):
	d[key] = val
python_lib_Types_DictImpl.set = DictImpl_statics_set


python_lib_Types_DictImpl._hx_class = python_lib_Types_DictImpl
python_lib_Types_DictImpl._hx_class_name = "python.lib.DictImpl"
_hx_classes['python.lib.DictImpl'] = python_lib_Types_DictImpl
python_lib_Types_DictImpl._hx_fields = []
python_lib_Types_DictImpl._hx_props = []
python_lib_Types_DictImpl._hx_methods = []
python_lib_Types_DictImpl._hx_statics = ["fromObject","hasKey","remove","set"]
python_lib_Types_DictImpl._hx_interfaces = []

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
from xml.etree.ElementTree import Element as python_lib_xml_etree_ElementTree_Element
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
