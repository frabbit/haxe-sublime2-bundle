from datetime import datetime as python_lib_datetime_Datetime
from datetime import tzinfo as python_lib_datetime_Tzinfo
from datetime import timezone as python_lib_datetime_Timezone
import math as python_lib_Math
import math as Math
import os as python_lib_Os
import re as python_lib_Re
from sublime_plugin import Command as sublime_Command
from sublime_plugin import TextCommand as sublime_TextCommand
from sublime_plugin import EventListener as sublime_EventListener
from sublime_plugin import WindowCommand as sublime_WindowCommand
from Default.exec import ProcessListener as sublime_def_exec_ProcessListener
from os import path as python_lib_os_Path
import builtins as python_lib_Builtins
import codecs as python_lib_Codecs
import functools as python_lib_Functools
import glob as python_lib_Glob
import inspect as python_lib_Inspect
import json as python_lib_Json
try:
	import msvcrt as python_lib_Msvcrt
except:
	pass
import pprint as python_lib_Pprint
import random as python_lib_Random
import shutil as python_lib_Shutil
import subprocess as python_lib_Subprocess
import sys as python_lib_Sys
import tempfile as python_lib_Tempfile
try:
	import termios as python_lib_Termios
except:
	pass
import _thread as python_lib_ThreadLowLevel
import time as python_lib_Time
try:
	import tty as python_lib_Tty
except:
	pass
from codecs import Codec as python_lib_codecs_Codec
from codecs import StreamReader as python_lib_codecs_StreamReader
from codecs import StreamReaderWriter as python_lib_codecs_StreamReaderWriter
from codecs import StreamWriter as python_lib_codecs_StreamWriter
from datetime import timedelta as python_lib_datetime_Timedelta
from io import IOBase as python_lib_io_IOBase
from io import BufferedIOBase as python_lib_io_BufferedIOBase
from io import BufferedReader as python_lib_io_BufferedReader
from io import RawIOBase as python_lib_io_RawIOBase
from io import FileIO as python_lib_io_FileIO
from io import TextIOBase as python_lib_io_TextIOBase
from io import StringIO as python_lib_io_StringIO
from json import JSONEncoder as python_lib_json_JSONEncoder
from subprocess import Popen as python_lib_subprocess_Popen
import urllib.parse as python_lib_urllib_Parse
from xml.etree.ElementTree import Element as python_lib_xml_etree_Element
import xml.etree.ElementTree as python_lib_xml_etree_ElementTree
from sublime import Edit as sublime_Edit
from sublime import Region as sublime_Region
from sublime import Selection as sublime_Selection
from sublime import Settings as sublime_Settings
import sublime as sublime_Sublime
from sublime import View as sublime_View
from sublime import Window as sublime_Window
from Default.exec import AsyncProcess as sublime_def_exec_AsyncProcess


class _hx_AnonObject:
	def __init__(self, fields):
		self.__dict__ = fields


_hx_classes = {}


class python_Boot:
	_hx_class_name = "python.Boot"
	_hx_statics = ["keywords", "arrayJoin", "safeJoin", "isPyBool", "isPyInt", "isPyFloat", "isClass", "isAnonObject", "_add_dynamic", "toString", "toString1", "isMetaType", "fields", "isString", "isArray", "simpleField", "field", "getInstanceFields", "getSuperClass", "getClassFields", "unsafeFastCodeAt", "handleKeywords", "prefixLength", "unhandleKeywords"]

	@staticmethod
	def arrayJoin(x,sep):
		# /opt/haxe-git/std/python/Boot.hx:50
		return sep.join([python_Boot.toString1(x1,'') for x1 in x])

	@staticmethod
	def safeJoin(x,sep):
		# /opt/haxe-git/std/python/Boot.hx:54
		return sep.join([x1 for x1 in x])

	@staticmethod
	def isPyBool(o):
		# /opt/haxe-git/std/python/Boot.hx:58
		return isinstance(o,bool)

	@staticmethod
	def isPyInt(o):
		# /opt/haxe-git/std/python/Boot.hx:62
		return isinstance(o,int)

	@staticmethod
	def isPyFloat(o):
		# /opt/haxe-git/std/python/Boot.hx:66
		return isinstance(o,float)

	@staticmethod
	def isClass(o):
		# /opt/haxe-git/std/python/Boot.hx:70
		return ((o is not None) and ((HxOverrides.eq(o,str) or python_lib_Inspect.isclass(o))))

	@staticmethod
	def isAnonObject(o):
		# /opt/haxe-git/std/python/Boot.hx:74
		return isinstance(o,_hx_AnonObject)

	@staticmethod
	def _add_dynamic(a,b):
		# /opt/haxe-git/std/python/Boot.hx:78
		if (isinstance(a,str) and isinstance(b,str)):
			return (a + b)
		# /opt/haxe-git/std/python/Boot.hx:81
		if (isinstance(a,str) or isinstance(b,str)):
			return (python_Boot.toString1(a,"") + python_Boot.toString1(b,""))
		# /opt/haxe-git/std/python/Boot.hx:84
		return (a + b)

	@staticmethod
	def toString(o):
		# /opt/haxe-git/std/python/Boot.hx:88
		return python_Boot.toString1(o,"")

	@staticmethod
	def toString1(o,s):
		# /opt/haxe-git/std/python/Boot.hx:93
		if (o is None):
			return "null"
		# /opt/haxe-git/std/python/Boot.hx:95
		if isinstance(o,str):
			return o
		# /opt/haxe-git/std/python/Boot.hx:97
		if (s is None):
			s = ""
		# /opt/haxe-git/std/python/Boot.hx:98
		if (len(s) >= 5):
			return "<...>"
		# /opt/haxe-git/std/python/Boot.hx:100
		if isinstance(o,bool):
			if o:
				return "true"
			else:
				return "false"
		# /opt/haxe-git/std/python/Boot.hx:103
		if isinstance(o,int):
			return str(o)
		# /opt/haxe-git/std/python/Boot.hx:107
		if isinstance(o,float):
			try:
				if (o == int(o)):
					# /opt/haxe-git/std/python/Boot.hx:110
					def _hx_local_1():
						# /opt/haxe-git/std/python/Boot.hx:110
						def _hx_local_0():
							# /opt/haxe-git/std/python/Boot.hx:110
							v = o
							return Math.floor((v + 0.5))
						return str(_hx_local_0())
					return _hx_local_1()
				else:
					return str(o)
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				e = _hx_e1
				return str(o)
		# /opt/haxe-git/std/python/Boot.hx:119
		if isinstance(o,list):
			# /opt/haxe-git/std/python/Boot.hx:121
			o1 = o
			# /opt/haxe-git/std/python/Boot.hx:123
			l = len(o1)
			# /opt/haxe-git/std/python/Boot.hx:125
			st = "["
			# /opt/haxe-git/std/python/Boot.hx:126
			s = (("null" if s is None else s) + "\t")
			# /opt/haxe-git/std/python/Boot.hx:127
			# /opt/haxe-git/std/python/Boot.hx:127
			_g = 0
			while (_g < l):
				i = _g
				_g = (_g + 1)
				# /opt/haxe-git/std/python/Boot.hx:128
				prefix = ""
				# /opt/haxe-git/std/python/Boot.hx:129
				if (i > 0):
					prefix = ","
				# /opt/haxe-git/std/python/Boot.hx:132
				st = (("null" if st is None else st) + HxOverrides.stringOrNull(((("null" if prefix is None else prefix) + HxOverrides.stringOrNull(python_Boot.toString1((o1[i] if i >= 0 and i < len(o1) else None),s))))))
			# /opt/haxe-git/std/python/Boot.hx:134
			st = (("null" if st is None else st) + "]")
			# /opt/haxe-git/std/python/Boot.hx:135
			return st
		# /opt/haxe-git/std/python/Boot.hx:138
		try:
			if hasattr(o,"toString"):
				return o.toString()
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			pass
		# /opt/haxe-git/std/python/Boot.hx:144
		if (python_lib_Inspect.isfunction(o) or python_lib_Inspect.ismethod(o)):
			return "<function>"
		# /opt/haxe-git/std/python/Boot.hx:146
		if hasattr(o,"__class__"):
			# /opt/haxe-git/std/python/Boot.hx:149
			if isinstance(o,_hx_AnonObject):
				# /opt/haxe-git/std/python/Boot.hx:151
				toStr = None
				# /opt/haxe-git/std/python/Boot.hx:152
				try:
					# /opt/haxe-git/std/python/Boot.hx:154
					fields = python_Boot.fields(o)
					# /opt/haxe-git/std/python/Boot.hx:155
					fieldsStr = None
					_g1 = []
					_g11 = 0
					while (_g11 < len(fields)):
						f = (fields[_g11] if _g11 >= 0 and _g11 < len(fields) else None)
						_g11 = (_g11 + 1)
						x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
						_g1.append(x)
					fieldsStr = _g1
					# /opt/haxe-git/std/python/Boot.hx:156
					toStr = (("{ " + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " }")
				except Exception as _hx_e:
					_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
					e2 = _hx_e1
					return "{ ... }"
				# /opt/haxe-git/std/python/Boot.hx:162
				if (toStr is None):
					return "{ ... }"
				else:
					return toStr
			# /opt/haxe-git/std/python/Boot.hx:172
			if isinstance(o,Enum):
				# /opt/haxe-git/std/python/Boot.hx:174
				o2 = o
				# /opt/haxe-git/std/python/Boot.hx:176
				l1 = len(o2.params)
				# /opt/haxe-git/std/python/Boot.hx:177
				hasParams = (l1 > 0)
				# /opt/haxe-git/std/python/Boot.hx:178
				if hasParams:
					# /opt/haxe-git/std/python/Boot.hx:179
					paramsStr = ""
					# /opt/haxe-git/std/python/Boot.hx:180
					# /opt/haxe-git/std/python/Boot.hx:180
					_g2 = 0
					while (_g2 < l1):
						i1 = _g2
						_g2 = (_g2 + 1)
						# /opt/haxe-git/std/python/Boot.hx:181
						prefix1 = ""
						# /opt/haxe-git/std/python/Boot.hx:182
						if (i1 > 0):
							prefix1 = ","
						# /opt/haxe-git/std/python/Boot.hx:185
						paramsStr = (("null" if paramsStr is None else paramsStr) + HxOverrides.stringOrNull(((("null" if prefix1 is None else prefix1) + HxOverrides.stringOrNull(python_Boot.toString1((o2.params[i1] if i1 >= 0 and i1 < len(o2.params) else None),s))))))
					# /opt/haxe-git/std/python/Boot.hx:187
					return (((HxOverrides.stringOrNull(o2.tag) + "(") + ("null" if paramsStr is None else paramsStr)) + ")")
				else:
					return o2.tag
			# /opt/haxe-git/std/python/Boot.hx:193
			if hasattr(o,"_hx_class_name"):
				if (o.__class__.__name__ != "type"):
					# /opt/haxe-git/std/python/Boot.hx:195
					fields1 = python_Boot.getInstanceFields(o)
					# /opt/haxe-git/std/python/Boot.hx:196
					fieldsStr1 = None
					_g3 = []
					_g12 = 0
					while (_g12 < len(fields1)):
						f1 = (fields1[_g12] if _g12 >= 0 and _g12 < len(fields1) else None)
						_g12 = (_g12 + 1)
						x1 = ((("" + ("null" if f1 is None else f1)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f1),(("null" if s is None else s) + "\t"))))
						_g3.append(x1)
					fieldsStr1 = _g3
					# /opt/haxe-git/std/python/Boot.hx:198
					toStr1 = (((HxOverrides.stringOrNull(o._hx_class_name) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr1]))) + " )")
					# /opt/haxe-git/std/python/Boot.hx:199
					return toStr1
				else:
					# /opt/haxe-git/std/python/Boot.hx:201
					fields2 = python_Boot.getClassFields(o)
					# /opt/haxe-git/std/python/Boot.hx:202
					fieldsStr2 = None
					_g4 = []
					_g13 = 0
					while (_g13 < len(fields2)):
						f2 = (fields2[_g13] if _g13 >= 0 and _g13 < len(fields2) else None)
						_g13 = (_g13 + 1)
						x2 = ((("" + ("null" if f2 is None else f2)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f2),(("null" if s is None else s) + "\t"))))
						_g4.append(x2)
					fieldsStr2 = _g4
					# /opt/haxe-git/std/python/Boot.hx:203
					toStr2 = (((("#" + HxOverrides.stringOrNull(o._hx_class_name)) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr2]))) + " )")
					# /opt/haxe-git/std/python/Boot.hx:204
					return toStr2
			# /opt/haxe-git/std/python/Boot.hx:208
			if (o == str):
				return "#String"
			# /opt/haxe-git/std/python/Boot.hx:212
			if (o == list):
				return "#Array"
			# /opt/haxe-git/std/python/Boot.hx:216
			if callable(o):
				return "function"
			# /opt/haxe-git/std/python/Boot.hx:219
			try:
				if hasattr(o,"__repr__"):
					return o.__repr__()
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				pass
			# /opt/haxe-git/std/python/Boot.hx:225
			if hasattr(o,"__str__"):
				return o.__str__([])
			# /opt/haxe-git/std/python/Boot.hx:229
			if hasattr(o,"__name__"):
				return o.__name__
			# /opt/haxe-git/std/python/Boot.hx:232
			return "???"
		else:
			return str(o)

	@staticmethod
	def isMetaType(v,t):
		# /opt/haxe-git/std/python/Boot.hx:239
		return (v == t)

	@staticmethod
	def fields(o):
		# /opt/haxe-git/std/python/Boot.hx:244
		a = []
		# /opt/haxe-git/std/python/Boot.hx:245
		if (o is not None):
			# /opt/haxe-git/std/python/Boot.hx:246
			if hasattr(o,"_hx_fields"):
				# /opt/haxe-git/std/python/Boot.hx:247
				fields = o._hx_fields
				# /opt/haxe-git/std/python/Boot.hx:248
				return list(fields)
			# /opt/haxe-git/std/python/Boot.hx:250
			if isinstance(o,_hx_AnonObject):
				# /opt/haxe-git/std/python/Boot.hx:252
				d = o.__dict__
				# /opt/haxe-git/std/python/Boot.hx:253
				keys = d.keys()
				# /opt/haxe-git/std/python/Boot.hx:254
				handler = python_Boot.unhandleKeywords
				# /opt/haxe-git/std/python/Boot.hx:256
				for k in keys:
				# /opt/haxe-git/std/python/Boot.hx:257
					a.append(handler(k))
			elif hasattr(o,"__dict__"):
				# /opt/haxe-git/std/python/Boot.hx:260
				a1 = []
				# /opt/haxe-git/std/python/Boot.hx:261
				d1 = o.__dict__
				# /opt/haxe-git/std/python/Boot.hx:262
				keys1 = d1.keys()
				# /opt/haxe-git/std/python/Boot.hx:263
				for k in keys1:
				# /opt/haxe-git/std/python/Boot.hx:264
					a.append(k)
		# /opt/haxe-git/std/python/Boot.hx:268
		return a

	@staticmethod
	def isString(o):
		# /opt/haxe-git/std/python/Boot.hx:272
		return isinstance(o,str)

	@staticmethod
	def isArray(o):
		# /opt/haxe-git/std/python/Boot.hx:276
		return isinstance(o,list)

	@staticmethod
	def simpleField(o,field):
		# /opt/haxe-git/std/python/Boot.hx:280
		if (field is None):
			return None
		# /opt/haxe-git/std/python/Boot.hx:282
		field1 = None
		if field in python_Boot.keywords:
			field1 = ("_hx_" + field)
		elif ((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95))):
			field1 = ("_hx_" + field)
		else:
			field1 = field
		# /opt/haxe-git/std/python/Boot.hx:283
		if hasattr(o,field1):
			return getattr(o,field1)
		else:
			return None

	@staticmethod
	def field(o,field):
		# /opt/haxe-git/std/python/Boot.hx:287
		if (field is None):
			return None
		# /opt/haxe-git/std/python/Boot.hx:289
		# /opt/haxe-git/std/python/Boot.hx:289
		_hx_local_0 = len(field)
		# /opt/haxe-git/std/python/Boot.hx:294
		if (_hx_local_0 == 10):
			if (field == "charCodeAt"):
				if isinstance(o,str):
					# /opt/haxe-git/std/python/Boot.hx:294
					s4 = o
					def _hx_local_1(a11):
						return HxString.charCodeAt(s4,a11)
					return _hx_local_1
		elif (_hx_local_0 == 11):
			if (field == "toLowerCase"):
				if isinstance(o,str):
					# /opt/haxe-git/std/python/Boot.hx:291
					s1 = o
					def _hx_local_2():
						return HxString.toLowerCase(s1)
					return _hx_local_2
			elif (field == "toUpperCase"):
				if isinstance(o,str):
					# /opt/haxe-git/std/python/Boot.hx:292
					s2 = o
					def _hx_local_3():
						return HxString.toUpperCase(s2)
					return _hx_local_3
			elif (field == "lastIndexOf"):
				if isinstance(o,str):
					# /opt/haxe-git/std/python/Boot.hx:296
					s6 = o
					def _hx_local_4(a13):
						return HxString.lastIndexOf(s6,a13)
					return _hx_local_4
				elif isinstance(o,list):
					# /opt/haxe-git/std/python/Boot.hx:314
					a2 = o
					def _hx_local_5(x2):
						return python_internal_ArrayImpl.lastIndexOf(a2,x2)
					return _hx_local_5
		elif (_hx_local_0 == 9):
			if (field == "substring"):
				if isinstance(o,str):
					# /opt/haxe-git/std/python/Boot.hx:299
					s9 = o
					def _hx_local_6(a15):
						return HxString.substring(s9,a15)
					return _hx_local_6
		elif (_hx_local_0 == 5):
			if (field == "split"):
				if isinstance(o,str):
					# /opt/haxe-git/std/python/Boot.hx:297
					s7 = o
					def _hx_local_7(d):
						return HxString.split(s7,d)
					return _hx_local_7
			elif (field == "shift"):
				if isinstance(o,list):
					# /opt/haxe-git/std/python/Boot.hx:317
					x14 = o
					def _hx_local_8():
						return python_internal_ArrayImpl.shift(x14)
					return _hx_local_8
			elif (field == "slice"):
				if isinstance(o,list):
					# /opt/haxe-git/std/python/Boot.hx:318
					x15 = o
					def _hx_local_9(a18):
						return python_internal_ArrayImpl.slice(x15,a18)
					return _hx_local_9
		elif (_hx_local_0 == 4):
			if (field == "copy"):
				if isinstance(o,list):
					# /opt/haxe-git/std/python/Boot.hx:305
					def _hx_local_10():
						# /opt/haxe-git/std/python/Boot.hx:305
						x6 = o
						return list(x6)
					return _hx_local_10
			elif (field == "join"):
				if isinstance(o,list):
					# /opt/haxe-git/std/python/Boot.hx:308
					def _hx_local_11(sep):
						# /opt/haxe-git/std/python/Boot.hx:308
						x9 = o
						return sep.join([python_Boot.toString1(x1,'') for x1 in x9])
					return _hx_local_11
			elif (field == "push"):
				if isinstance(o,list):
					# /opt/haxe-git/std/python/Boot.hx:311
					x11 = o
					def _hx_local_12(e):
						return python_internal_ArrayImpl.push(x11,e)
					return _hx_local_12
			elif (field == "sort"):
				if isinstance(o,list):
					# /opt/haxe-git/std/python/Boot.hx:319
					x16 = o
					def _hx_local_13(f2):
						python_internal_ArrayImpl.sort(x16,f2)
					return _hx_local_13
		elif (_hx_local_0 == 7):
			if (field == "indexOf"):
				if isinstance(o,str):
					# /opt/haxe-git/std/python/Boot.hx:295
					s5 = o
					def _hx_local_14(a12):
						return HxString.indexOf(s5,a12)
					return _hx_local_14
				elif isinstance(o,list):
					# /opt/haxe-git/std/python/Boot.hx:313
					a = o
					def _hx_local_15(x1):
						return python_internal_ArrayImpl.indexOf(a,x1)
					return _hx_local_15
			elif (field == "unshift"):
				if isinstance(o,list):
					# /opt/haxe-git/std/python/Boot.hx:312
					x12 = o
					def _hx_local_16(e1):
						python_internal_ArrayImpl.unshift(x12,e1)
					return _hx_local_16
			elif (field == "reverse"):
				if isinstance(o,list):
					# /opt/haxe-git/std/python/Boot.hx:316
					a4 = o
					def _hx_local_17():
						python_internal_ArrayImpl.reverse(a4)
					return _hx_local_17
		elif (_hx_local_0 == 3):
			if (field == "map"):
				if isinstance(o,list):
					# /opt/haxe-git/std/python/Boot.hx:302
					x4 = o
					def _hx_local_18(f):
						return python_internal_ArrayImpl.map(x4,f)
					return _hx_local_18
			elif (field == "pop"):
				if isinstance(o,list):
					# /opt/haxe-git/std/python/Boot.hx:310
					x10 = o
					def _hx_local_19():
						return python_internal_ArrayImpl.pop(x10)
					return _hx_local_19
		elif (_hx_local_0 == 8):
			if (field == "toString"):
				if isinstance(o,str):
					# /opt/haxe-git/std/python/Boot.hx:300
					s10 = o
					def _hx_local_20():
						return HxString.toString(s10)
					return _hx_local_20
				elif isinstance(o,list):
					# /opt/haxe-git/std/python/Boot.hx:309
					x3 = o
					def _hx_local_21():
						return python_internal_ArrayImpl.toString(x3)
					return _hx_local_21
			elif (field == "iterator"):
				if isinstance(o,list):
					# /opt/haxe-git/std/python/Boot.hx:306
					x7 = o
					def _hx_local_22():
						return python_internal_ArrayImpl.iterator(x7)
					return _hx_local_22
		elif (_hx_local_0 == 6):
			if (field == "length"):
				if isinstance(o,str):
					# /opt/haxe-git/std/python/Boot.hx:290
					s = o
					return len(s)
				elif isinstance(o,list):
					# /opt/haxe-git/std/python/Boot.hx:301
					x = o
					return len(x)
			elif (field == "charAt"):
				if isinstance(o,str):
					# /opt/haxe-git/std/python/Boot.hx:293
					s3 = o
					def _hx_local_23(a1):
						return HxString.charAt(s3,a1)
					return _hx_local_23
			elif (field == "substr"):
				if isinstance(o,str):
					# /opt/haxe-git/std/python/Boot.hx:298
					s8 = o
					def _hx_local_24(a14):
						return HxString.substr(s8,a14)
					return _hx_local_24
			elif (field == "filter"):
				if isinstance(o,list):
					# /opt/haxe-git/std/python/Boot.hx:303
					x5 = o
					def _hx_local_25(f1):
						return python_internal_ArrayImpl.filter(x5,f1)
					return _hx_local_25
			elif (field == "concat"):
				if isinstance(o,list):
					# /opt/haxe-git/std/python/Boot.hx:304
					a16 = o
					def _hx_local_26(a21):
						return python_internal_ArrayImpl.concat(a16,a21)
					return _hx_local_26
			elif (field == "insert"):
				if isinstance(o,list):
					# /opt/haxe-git/std/python/Boot.hx:307
					a3 = o
					def _hx_local_27(a17,x8):
						python_internal_ArrayImpl.insert(a3,a17,x8)
					return _hx_local_27
			elif (field == "remove"):
				if isinstance(o,list):
					# /opt/haxe-git/std/python/Boot.hx:315
					x13 = o
					def _hx_local_28(e2):
						return python_internal_ArrayImpl.remove(x13,e2)
					return _hx_local_28
			elif (field == "splice"):
				if isinstance(o,list):
					# /opt/haxe-git/std/python/Boot.hx:320
					x17 = o
					def _hx_local_29(a19,a22):
						return python_internal_ArrayImpl.splice(x17,a19,a22)
					return _hx_local_29
		else:
			pass
		# /opt/haxe-git/std/python/Boot.hx:324
		field1 = None
		if field in python_Boot.keywords:
			field1 = ("_hx_" + field)
		elif ((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95))):
			field1 = ("_hx_" + field)
		else:
			field1 = field
		# /opt/haxe-git/std/python/Boot.hx:325
		if hasattr(o,field1):
			return getattr(o,field1)
		else:
			return None

	@staticmethod
	def getInstanceFields(c):
		# /opt/haxe-git/std/python/Boot.hx:330
		f = None
		if hasattr(c,"_hx_fields"):
			f = c._hx_fields
		else:
			f = []
		# /opt/haxe-git/std/python/Boot.hx:331
		if hasattr(c,"_hx_methods"):
			# /opt/haxe-git/std/python/Boot.hx:332
			a = c._hx_methods
			f = (f + a)
		# /opt/haxe-git/std/python/Boot.hx:334
		sc = python_Boot.getSuperClass(c)
		# /opt/haxe-git/std/python/Boot.hx:336
		if (sc is None):
			return f
		else:
			# /opt/haxe-git/std/python/Boot.hx:340
			scArr = python_Boot.getInstanceFields(sc)
			# /opt/haxe-git/std/python/Boot.hx:341
			scMap = set(scArr)
			# /opt/haxe-git/std/python/Boot.hx:343
			res = []
			# /opt/haxe-git/std/python/Boot.hx:344
			# /opt/haxe-git/std/python/Boot.hx:344
			_g = 0
			while (_g < len(f)):
				f1 = (f[_g] if _g >= 0 and _g < len(f) else None)
				_g = (_g + 1)
				# /opt/haxe-git/std/python/Boot.hx:345
				if (not f1 in scMap):
					# /opt/haxe-git/std/python/Boot.hx:346
					scArr.append(f1)
			# /opt/haxe-git/std/python/Boot.hx:350
			return scArr

	@staticmethod
	def getSuperClass(c):
		# /opt/haxe-git/std/python/Boot.hx:355
		if (c is None):
			return None
		# /opt/haxe-git/std/python/Boot.hx:358
		try:
			# /opt/haxe-git/std/python/Boot.hx:359
			if hasattr(c,"_hx_super"):
				return c._hx_super
			# /opt/haxe-git/std/python/Boot.hx:362
			return None
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			pass
		# /opt/haxe-git/std/python/Boot.hx:366
		return None

	@staticmethod
	def getClassFields(c):
		# /opt/haxe-git/std/python/Boot.hx:371
		if hasattr(c,"_hx_statics"):
			# /opt/haxe-git/std/python/Boot.hx:372
			x = c._hx_statics
			# /opt/haxe-git/std/python/Boot.hx:373
			return list(x)
		else:
			return []

	@staticmethod
	def unsafeFastCodeAt(s,index):
		# /opt/haxe-git/std/python/Boot.hx:382
		return ord(s[index])

	@staticmethod
	def handleKeywords(name):
		# /opt/haxe-git/std/python/Boot.hx:386
		if name in python_Boot.keywords:
			return ("_hx_" + name)
		elif ((((len(name) > 2) and ((ord(name[0]) == 95))) and ((ord(name[1]) == 95))) and ((ord(name[(len(name) - 1)]) != 95))):
			return ("_hx_" + name)
		else:
			return name

	@staticmethod
	def unhandleKeywords(name):
		# /opt/haxe-git/std/python/Boot.hx:397
		if (HxString.substr(name,0,python_Boot.prefixLength) == "_hx_"):
			# /opt/haxe-git/std/python/Boot.hx:398
			real = HxString.substr(name,python_Boot.prefixLength,None)
			# /opt/haxe-git/std/python/Boot.hx:399
			if real in python_Boot.keywords:
				return real
		# /opt/haxe-git/std/python/Boot.hx:401
		return name
python_Boot._hx_class = python_Boot
_hx_classes["python.Boot"] = python_Boot


class Enum:
	_hx_class_name = "Enum"
	_hx_fields = ["tag", "index", "params"]
	_hx_methods = ["__str__"]

	def __init__(self,tag,index,params):
		# /opt/haxe-git/std/python/internal/EnumImpl.hx:28
		self.tag = None
		# /opt/haxe-git/std/python/internal/EnumImpl.hx:31
		self.index = None
		# /opt/haxe-git/std/python/internal/EnumImpl.hx:34
		self.params = None
		# /opt/haxe-git/std/python/internal/EnumImpl.hx:38
		self.tag = tag
		# /opt/haxe-git/std/python/internal/EnumImpl.hx:39
		self.index = index
		# /opt/haxe-git/std/python/internal/EnumImpl.hx:40
		self.params = params

	def __str__(self):
		# /opt/haxe-git/std/python/internal/EnumImpl.hx:45
		if (self.params is None):
			return self.tag
		else:
			return (((HxOverrides.stringOrNull(self.tag) + "(") + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in self.params]))) + ")")

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.tag = None
		_hx_o.index = None
		_hx_o.params = None
Enum._hx_class = Enum
_hx_classes["Enum"] = Enum


class HxOverrides:
	_hx_class_name = "HxOverrides"
	_hx_statics = ["iterator", "eq", "stringOrNull", "shift", "pop", "push", "join", "filter", "map", "toUpperCase", "toLowerCase", "rshift", "modf", "mod", "arrayGet", "arraySet", "mapKwArgs", "reverseMapKwArgs"]

	@staticmethod
	def iterator(x):
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:39
		if isinstance(x,list):
			return python_HaxeIterator(x.__iter__())
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:42
		return x.iterator()

	@staticmethod
	def eq(a,b):
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:46
		if (isinstance(a,list) or isinstance(b,list)):
			return a is b
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:49
		return (a == b)

	@staticmethod
	def stringOrNull(s):
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:53
		if (s is None):
			return "null"
		else:
			return s

	@staticmethod
	def shift(x):
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:58
		if isinstance(x,list):
			# /opt/haxe-git/std/python/internal/HxOverrides.hx:59
			_this = x
			return (None if ((len(_this) == 0)) else _this.pop(0))
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:61
		return x.shift()

	@staticmethod
	def pop(x):
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:66
		if isinstance(x,list):
			# /opt/haxe-git/std/python/internal/HxOverrides.hx:67
			_this = x
			return (None if ((len(_this) == 0)) else _this.pop())
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:69
		return x.pop()

	@staticmethod
	def push(x,e):
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:74
		if isinstance(x,list):
			# /opt/haxe-git/std/python/internal/HxOverrides.hx:75
			_this = x
			_this.append(e)
			return len(_this)
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:77
		return x.push(e)

	@staticmethod
	def join(x,sep):
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:82
		if isinstance(x,list):
			return sep.join([python_Boot.toString1(x1,'') for x1 in x])
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:85
		return x.join(sep)

	@staticmethod
	def filter(x,f):
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:90
		if isinstance(x,list):
			return list(filter(f,x))
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:93
		return x.filter(f)

	@staticmethod
	def map(x,f):
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:98
		if isinstance(x,list):
			return list(map(f,x))
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:101
		return x.map(f)

	@staticmethod
	def toUpperCase(x):
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:106
		if isinstance(x,str):
			return x.upper()
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:109
		return x.toUpperCase()

	@staticmethod
	def toLowerCase(x):
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:114
		if isinstance(x,str):
			return x.lower()
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:117
		return x.toLowerCase()

	@staticmethod
	def rshift(val,n):
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:122
		return ((val % 0x100000000) >> n)

	@staticmethod
	def modf(a,b):
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:127
		return float('nan') if (b == 0.0) else a % b if a >= 0 else -(-a % b)

	@staticmethod
	def mod(a,b):
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:131
		return a % b if a >= 0 else -(-a % b)

	@staticmethod
	def arrayGet(a,i):
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:136
		if isinstance(a,list):
			# /opt/haxe-git/std/python/internal/HxOverrides.hx:137
			x = a
			if ((i > -1) and ((i < len(x)))):
				return x[i]
			else:
				return None
		else:
			return a[i]

	@staticmethod
	def arraySet(a,i,v):
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:145
		if isinstance(a,list):
			# /opt/haxe-git/std/python/internal/HxOverrides.hx:146
			x = a
			v1 = v
			l = len(x)
			while (l < i):
				x.append(None)
				l = (l + 1)
			if (l == i):
				x.append(v1)
			else:
				x[i] = v1
			return v1
		else:
			# /opt/haxe-git/std/python/internal/HxOverrides.hx:148
			a[i] = v
			# /opt/haxe-git/std/python/internal/HxOverrides.hx:149
			return v

	@staticmethod
	def mapKwArgs(a,v):
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:156
		a1 = python_Lib.dictAsAnon(python_Lib.anonToDict(a))
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:157
		def _hx_local_0():
			# /opt/haxe-git/std/python/internal/HxOverrides.hx:157
			_this = v.keys()
			def _hx_local_2():
				def _hx_local_1():
					this1 = iter(_this)
					return python_HaxeIterator(this1)
				return _hx_local_1()
			return _hx_local_2()
		_hx_local_3 = _hx_local_0()
		while _hx_local_3.hasNext():
			k = _hx_local_3.next()
			# /opt/haxe-git/std/python/internal/HxOverrides.hx:158
			val = v.get(k)
			# /opt/haxe-git/std/python/internal/HxOverrides.hx:159
			if hasattr(a1,k):
				# /opt/haxe-git/std/python/internal/HxOverrides.hx:160
				x = getattr(a1,k)
				# /opt/haxe-git/std/python/internal/HxOverrides.hx:161
				setattr(a1,val,x)
				# /opt/haxe-git/std/python/internal/HxOverrides.hx:162
				delattr(a1,k)
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:165
		return a1

	@staticmethod
	def reverseMapKwArgs(a,v):
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:171
		a1 = a.copy()
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:172
		def _hx_local_0():
			# /opt/haxe-git/std/python/internal/HxOverrides.hx:172
			_this = v.keys()
			def _hx_local_2():
				def _hx_local_1():
					this1 = iter(_this)
					return python_HaxeIterator(this1)
				return _hx_local_1()
			return _hx_local_2()
		_hx_local_3 = _hx_local_0()
		while _hx_local_3.hasNext():
			k = _hx_local_3.next()
			# /opt/haxe-git/std/python/internal/HxOverrides.hx:174
			val = v.get(k)
			# /opt/haxe-git/std/python/internal/HxOverrides.hx:175
			if val in a1:
				# /opt/haxe-git/std/python/internal/HxOverrides.hx:176
				x = a1.get(val,None)
				# /opt/haxe-git/std/python/internal/HxOverrides.hx:177
				a1[k] = x
				# /opt/haxe-git/std/python/internal/HxOverrides.hx:178
				del a1[val]
		# /opt/haxe-git/std/python/internal/HxOverrides.hx:181
		return a1
HxOverrides._hx_class = HxOverrides
_hx_classes["HxOverrides"] = HxOverrides


class Class:
	_hx_class_name = "Class"
Class._hx_class = Class
_hx_classes["Class"] = Class


class Date:
	_hx_class_name = "Date"
	_hx_fields = ["epoch", "date"]
	_hx_methods = ["getTime", "getHours", "getMinutes", "getSeconds", "getFullYear", "getMonth", "getDate", "getDay", "toString"]
	_hx_statics = ["EPOCH_UTC", "EPOCH_LOCAL", "now", "fromTime", "UTC", "datetimeTimestamp", "fromString"]

	def __init__(self,year,month,day,hour,_hx_min,sec):
		# /opt/haxe-git/std/python/_std/Date.hx:31
		self.epoch = None
		# /opt/haxe-git/std/python/_std/Date.hx:33
		self.date = None
		# /opt/haxe-git/std/python/_std/Date.hx:37
		if (year < python_lib_datetime_Datetime.min.year):
			year = python_lib_datetime_Datetime.min.year
		# /opt/haxe-git/std/python/_std/Date.hx:38
		if (day == 0):
			day = 1
		# /opt/haxe-git/std/python/_std/Date.hx:39
		self.date = python_lib_datetime_Datetime(year, (month + 1), day, hour, _hx_min, sec, 0)

	def getTime(self):
		# /opt/haxe-git/std/python/_std/Date.hx:44
		return Date.datetimeTimestamp(self.date,Date.EPOCH_LOCAL)

	def getHours(self):
		# /opt/haxe-git/std/python/_std/Date.hx:49
		return self.date.hour

	def getMinutes(self):
		# /opt/haxe-git/std/python/_std/Date.hx:54
		return self.date.minute

	def getSeconds(self):
		# /opt/haxe-git/std/python/_std/Date.hx:59
		return self.date.second

	def getFullYear(self):
		# /opt/haxe-git/std/python/_std/Date.hx:64
		return self.date.year

	def getMonth(self):
		# /opt/haxe-git/std/python/_std/Date.hx:69
		return (self.date.month - 1)

	def getDate(self):
		# /opt/haxe-git/std/python/_std/Date.hx:74
		return self.date.day

	def getDay(self):
		# /opt/haxe-git/std/python/_std/Date.hx:79
		return self.date.isoweekday()

	def toString(self):
		# /opt/haxe-git/std/python/_std/Date.hx:86
		m = ((self.date.month - 1) + 1)
		# /opt/haxe-git/std/python/_std/Date.hx:87
		d = self.date.day
		# /opt/haxe-git/std/python/_std/Date.hx:88
		h = self.date.hour
		# /opt/haxe-git/std/python/_std/Date.hx:89
		mi = self.date.minute
		# /opt/haxe-git/std/python/_std/Date.hx:90
		s = self.date.second
		# /opt/haxe-git/std/python/_std/Date.hx:91
		return ((((((((((Std.string(self.date.year) + "-") + HxOverrides.stringOrNull(((("0" + Std.string(m)) if ((m < 10)) else ("" + Std.string(m)))))) + "-") + HxOverrides.stringOrNull(((("0" + Std.string(d)) if ((d < 10)) else ("" + Std.string(d)))))) + " ") + HxOverrides.stringOrNull(((("0" + Std.string(h)) if ((h < 10)) else ("" + Std.string(h)))))) + ":") + HxOverrides.stringOrNull(((("0" + Std.string(mi)) if ((mi < 10)) else ("" + Std.string(mi)))))) + ":") + HxOverrides.stringOrNull(((("0" + Std.string(s)) if ((s < 10)) else ("" + Std.string(s))))))

	@staticmethod
	def now():
		# /opt/haxe-git/std/python/_std/Date.hx:101
		d = Date(1970, 0, 1, 0, 0, 0)
		# /opt/haxe-git/std/python/_std/Date.hx:102
		d.date = python_lib_datetime_Datetime.now()
		# /opt/haxe-git/std/python/_std/Date.hx:103
		return d

	@staticmethod
	def fromTime(t):
		# /opt/haxe-git/std/python/_std/Date.hx:108
		d = Date(1970, 0, 1, 0, 0, 0)
		# /opt/haxe-git/std/python/_std/Date.hx:109
		d.date = python_lib_datetime_Datetime.fromtimestamp((t / 1000.0))
		# /opt/haxe-git/std/python/_std/Date.hx:110
		return d

	@staticmethod
	def UTC(year,month,day,hour,_hx_min,sec):
		# /opt/haxe-git/std/python/_std/Date.hx:116
		dt = python_lib_datetime_Datetime(year, (month + 1), day, hour, _hx_min, sec, 0, python_lib_datetime_Timezone.utc)
		# /opt/haxe-git/std/python/_std/Date.hx:117
		return Date.datetimeTimestamp(dt,Date.EPOCH_UTC)

	@staticmethod
	def datetimeTimestamp(dt,epoch):
		# /opt/haxe-git/std/python/_std/Date.hx:122
		return ((dt - epoch).total_seconds() * 1000)

	@staticmethod
	def fromString(s):
		# /opt/haxe-git/std/python/_std/Date.hx:127
		_g = len(s)
		# /opt/haxe-git/std/python/_std/Date.hx:129
		if (_g == 8):
			# /opt/haxe-git/std/python/_std/Date.hx:130
			k = s.split(":")
			# /opt/haxe-git/std/python/_std/Date.hx:131
			d = Date(0, 0, 0, Std.parseInt((k[0] if 0 < len(k) else None)), Std.parseInt((k[1] if 1 < len(k) else None)), Std.parseInt((k[2] if 2 < len(k) else None)))
			# /opt/haxe-git/std/python/_std/Date.hx:132
			return d
		elif (_g == 10):
			# /opt/haxe-git/std/python/_std/Date.hx:134
			k1 = s.split("-")
			# /opt/haxe-git/std/python/_std/Date.hx:135
			return Date(Std.parseInt((k1[0] if 0 < len(k1) else None)), (Std.parseInt((k1[1] if 1 < len(k1) else None)) - 1), Std.parseInt((k1[2] if 2 < len(k1) else None)), 0, 0, 0)
		elif (_g == 19):
			# /opt/haxe-git/std/python/_std/Date.hx:137
			k2 = s.split(" ")
			# /opt/haxe-git/std/python/_std/Date.hx:138
			y = None
			_this = (k2[0] if 0 < len(k2) else None)
			y = _this.split("-")
			# /opt/haxe-git/std/python/_std/Date.hx:139
			t = None
			_this1 = (k2[1] if 1 < len(k2) else None)
			t = _this1.split(":")
			# /opt/haxe-git/std/python/_std/Date.hx:140
			return Date(Std.parseInt((y[0] if 0 < len(y) else None)), (Std.parseInt((y[1] if 1 < len(y) else None)) - 1), Std.parseInt((y[2] if 2 < len(y) else None)), Std.parseInt((t[0] if 0 < len(t) else None)), Std.parseInt((t[1] if 1 < len(t) else None)), Std.parseInt((t[2] if 2 < len(t) else None)))
		else:
			raise _HxException(("Invalid date format : " + ("null" if s is None else s)))

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.epoch = None
		_hx_o.date = None
Date._hx_class = Date
_hx_classes["Date"] = Date


class EReg:
	_hx_class_name = "EReg"
	_hx_fields = ["pattern", "matchObj", "global"]
	_hx_methods = ["match", "matched", "matchedLeft", "matchedRight", "matchedPos", "matchSub", "split", "replace", "map"]

	def __init__(self,r,opt):
		# /opt/haxe-git/std/python/_std/EReg.hx:38
		self.pattern = None
		# /opt/haxe-git/std/python/_std/EReg.hx:39
		self.matchObj = None
		# /opt/haxe-git/std/python/_std/EReg.hx:40
		self._hx_global = None
		# /opt/haxe-git/std/python/_std/EReg.hx:43
		self._hx_global = False
		# /opt/haxe-git/std/python/_std/EReg.hx:44
		options = 0
		# /opt/haxe-git/std/python/_std/EReg.hx:45
		# /opt/haxe-git/std/python/_std/EReg.hx:45
		_g1 = 0
		_g = len(opt)
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			# /opt/haxe-git/std/python/_std/EReg.hx:46
			c = None
			if (i >= len(opt)):
				c = -1
			else:
				c = ord(opt[i])
			# /opt/haxe-git/std/python/_std/EReg.hx:47
			if (c == 109):
				options = (options | python_lib_Re.M)
			# /opt/haxe-git/std/python/_std/EReg.hx:48
			if (c == 105):
				options = (options | python_lib_Re.I)
			# /opt/haxe-git/std/python/_std/EReg.hx:49
			if (c == 115):
				options = (options | python_lib_Re.S)
			# /opt/haxe-git/std/python/_std/EReg.hx:50
			if (c == 117):
				options = (options | python_lib_Re.U)
			# /opt/haxe-git/std/python/_std/EReg.hx:51
			if (c == 103):
				self._hx_global = True
		# /opt/haxe-git/std/python/_std/EReg.hx:53
		self.pattern = python_lib_Re.compile(r,options)

	def match(self,s):
		# /opt/haxe-git/std/python/_std/EReg.hx:64
		self.matchObj = python_lib_Re.search(self.pattern,s)
		# /opt/haxe-git/std/python/_std/EReg.hx:65
		return (self.matchObj is not None)

	def matched(self,n):
		# /opt/haxe-git/std/python/_std/EReg.hx:80
		return self.matchObj.group(n)

	def matchedLeft(self):
		# /opt/haxe-git/std/python/_std/EReg.hx:95
		_hx_len = self.matchObj.start()
		return HxString.substr(self.matchObj.string,0,_hx_len)

	def matchedRight(self):
		# /opt/haxe-git/std/python/_std/EReg.hx:110
		pos = self.matchObj.end()
		return HxString.substr(self.matchObj.string,pos,None)

	def matchedPos(self):
		# /opt/haxe-git/std/python/_std/EReg.hx:125
		return _hx_AnonObject({'pos': self.matchObj.start(), 'len': (self.matchObj.end() - self.matchObj.start())})

	def matchSub(self,s,pos,_hx_len = -1):
		# /opt/haxe-git/std/python/_std/EReg.hx:139
		if (_hx_len is None):
			_hx_len = -1
		# /opt/haxe-git/std/python/_std/EReg.hx:140
		if (_hx_len != -1):
			self.matchObj = self.pattern.search(s,pos,(pos + _hx_len))
		else:
			self.matchObj = self.pattern.search(s,pos)
		# /opt/haxe-git/std/python/_std/EReg.hx:146
		return (self.matchObj is not None)

	def split(self,s):
		# /opt/haxe-git/std/python/_std/EReg.hx:169
		if self._hx_global:
			# /opt/haxe-git/std/python/_std/EReg.hx:170
			ret = []
			# /opt/haxe-git/std/python/_std/EReg.hx:171
			lastEnd = 0
			# /opt/haxe-git/std/python/_std/EReg.hx:173
			def _hx_local_0():
				# /opt/haxe-git/std/python/_std/EReg.hx:173
				this1 = python_lib_Re.finditer(self.pattern,s)
				return python_HaxeIterator(this1)
			_hx_local_1 = _hx_local_0()
			while _hx_local_1.hasNext():
				x = _hx_local_1.next()
				# /opt/haxe-git/std/python/_std/EReg.hx:175
				# /opt/haxe-git/std/python/_std/EReg.hx:175
				x1 = None
				endIndex = x.start()
				x1 = HxString.substring(s,lastEnd,endIndex)
				ret.append(x1)
				# /opt/haxe-git/std/python/_std/EReg.hx:176
				lastEnd = x.end()
			# /opt/haxe-git/std/python/_std/EReg.hx:178
			# /opt/haxe-git/std/python/_std/EReg.hx:178
			x2 = HxString.substr(s,lastEnd,None)
			ret.append(x2)
			# /opt/haxe-git/std/python/_std/EReg.hx:169
			return ret
		else:
			# /opt/haxe-git/std/python/_std/EReg.hx:181
			# /opt/haxe-git/std/python/_std/EReg.hx:181
			self.matchObj = python_lib_Re.search(self.pattern,s)
			(self.matchObj is not None)
			# /opt/haxe-git/std/python/_std/EReg.hx:182
			if (self.matchObj is None):
				return [s]
			else:
				# /opt/haxe-git/std/python/_std/EReg.hx:169
				def _hx_local_4():
					# /opt/haxe-git/std/python/_std/EReg.hx:185
					def _hx_local_2():
						# /opt/haxe-git/std/python/_std/EReg.hx:185
						endIndex1 = self.matchObj.start()
						return HxString.substring(s,0,endIndex1)
					def _hx_local_3():
						pos = self.matchObj.end()
						return HxString.substr(s,pos,None)
					return [_hx_local_2(), _hx_local_3()]
				return _hx_local_4()

	def replace(self,s,by):
		# /opt/haxe-git/std/python/_std/EReg.hx:207
		by1 = None
		_this = by.split("$$")
		by1 = "_hx_#repl#__".join([python_Boot.toString1(x1,'') for x1 in _this])
		# /opt/haxe-git/std/python/_std/EReg.hx:208
		def _hx_local_0(x):
			# /opt/haxe-git/std/python/_std/EReg.hx:209
			res = by1
			# /opt/haxe-git/std/python/_std/EReg.hx:210
			g = x.groups()
			# /opt/haxe-git/std/python/_std/EReg.hx:211
			# /opt/haxe-git/std/python/_std/EReg.hx:211
			_g1 = 0
			_g = len(g)
			while (_g1 < _g):
				i = _g1
				_g1 = (_g1 + 1)
				# /opt/haxe-git/std/python/_std/EReg.hx:213
				# /opt/haxe-git/std/python/_std/EReg.hx:213
				_this1 = None
				delimiter = ("$" + HxOverrides.stringOrNull(str((i + 1))))
				if (delimiter == ""):
					_this1 = list(res)
				else:
					_this1 = res.split(delimiter)
				res = g[i].join([python_Boot.toString1(x1,'') for x1 in _this1])
			# /opt/haxe-git/std/python/_std/EReg.hx:215
			# /opt/haxe-git/std/python/_std/EReg.hx:215
			_this2 = res.split("_hx_#repl#__")
			res = "$".join([python_Boot.toString1(x1,'') for x1 in _this2])
			# /opt/haxe-git/std/python/_std/EReg.hx:216
			return res
		replace = _hx_local_0
		# /opt/haxe-git/std/python/_std/EReg.hx:218
		return python_lib_Re.sub(self.pattern,replace,s,(0 if (self._hx_global) else 1))

	def map(self,s,f):
		# /opt/haxe-git/std/python/_std/EReg.hx:228
		buf_b = python_lib_io_StringIO()
		# /opt/haxe-git/std/python/_std/EReg.hx:229
		pos = 0
		# /opt/haxe-git/std/python/_std/EReg.hx:230
		right = s
		# /opt/haxe-git/std/python/_std/EReg.hx:232
		cur = self
		# /opt/haxe-git/std/python/_std/EReg.hx:233
		while (pos < len(s)):
			# /opt/haxe-git/std/python/_std/EReg.hx:235
			if (self.matchObj is None):
				self.matchObj = python_lib_Re.search(self.pattern,s)
			else:
				self.matchObj = self.matchObj.re.search(s,pos)
			# /opt/haxe-git/std/python/_std/EReg.hx:241
			if (self.matchObj is None):
				break
			# /opt/haxe-git/std/python/_std/EReg.hx:246
			pos1 = self.matchObj.end()
			# /opt/haxe-git/std/python/_std/EReg.hx:248
			curPos_pos = cur.matchObj.start()
			curPos_len = (cur.matchObj.end() - cur.matchObj.start())
			# /opt/haxe-git/std/python/_std/EReg.hx:251
			# /opt/haxe-git/std/python/_std/EReg.hx:251
			x = None
			_this = None
			_hx_len = cur.matchObj.start()
			_this = HxString.substr(cur.matchObj.string,0,_hx_len)
			x = HxString.substr(_this,pos,None)
			buf_b.write(Std.string(x))
			# /opt/haxe-git/std/python/_std/EReg.hx:252
			# /opt/haxe-git/std/python/_std/EReg.hx:252
			x1 = f(cur)
			buf_b.write(Std.string(x1))
			# /opt/haxe-git/std/python/_std/EReg.hx:254
			# /opt/haxe-git/std/python/_std/EReg.hx:254
			pos2 = cur.matchObj.end()
			right = HxString.substr(cur.matchObj.string,pos2,None)
			# /opt/haxe-git/std/python/_std/EReg.hx:258
			if (not self._hx_global):
				# /opt/haxe-git/std/python/_std/EReg.hx:259
				buf_b.write(Std.string(right))
				# /opt/haxe-git/std/python/_std/EReg.hx:260
				return buf_b.getvalue()
			# /opt/haxe-git/std/python/_std/EReg.hx:263
			if (curPos_len == 0):
				# /opt/haxe-git/std/python/_std/EReg.hx:264
				# /opt/haxe-git/std/python/_std/EReg.hx:264
				x2 = None
				if ((pos1 < 0) or ((pos1 >= len(s)))):
					x2 = ""
				else:
					x2 = s[pos1]
				buf_b.write(Std.string(x2))
				# /opt/haxe-git/std/python/_std/EReg.hx:265
				right = HxString.substr(right,1,None)
				# /opt/haxe-git/std/python/_std/EReg.hx:266
				pos = (pos1 + 1)
			else:
				pos = pos1
		# /opt/haxe-git/std/python/_std/EReg.hx:273
		buf_b.write(Std.string(right))
		# /opt/haxe-git/std/python/_std/EReg.hx:274
		return buf_b.getvalue()

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.pattern = None
		_hx_o.matchObj = None
		_hx_o._hx_global = None
EReg._hx_class = EReg
_hx_classes["EReg"] = EReg


class EnumValue:
	_hx_class_name = "EnumValue"
EnumValue._hx_class = EnumValue
_hx_classes["EnumValue"] = EnumValue


class IntIterator:
	_hx_class_name = "IntIterator"
	_hx_fields = ["min", "max"]
	_hx_methods = ["hasNext", "next"]

	def __init__(self,_hx_min,_hx_max):
		# /opt/haxe-git/std/IntIterator.hx:36
		self.min = None
		# /opt/haxe-git/std/IntIterator.hx:37
		self.max = None
		# /opt/haxe-git/std/IntIterator.hx:45
		self.min = _hx_min
		# /opt/haxe-git/std/IntIterator.hx:46
		self.max = _hx_max

	def hasNext(self):
		# /opt/haxe-git/std/IntIterator.hx:53
		return (self.min < self.max)

	def next(self):
		# /opt/haxe-git/std/IntIterator.hx:62
		def _hx_local_3():
			# /opt/haxe-git/std/IntIterator.hx:62
			def _hx_local_2():
				# /opt/haxe-git/std/IntIterator.hx:62
				_hx_local_0 = self
				_hx_local_1 = _hx_local_0.min
				_hx_local_0.min = (_hx_local_1 + 1)
				return _hx_local_1
			return _hx_local_2()
		return _hx_local_3()

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.min = None
		_hx_o.max = None
IntIterator._hx_class = IntIterator
_hx_classes["IntIterator"] = IntIterator


class Lambda:
	_hx_class_name = "Lambda"
	_hx_statics = ["array", "list", "map", "mapi", "has", "exists", "foreach", "iter", "filter", "fold", "count", "empty", "indexOf", "find", "concat"]

	@staticmethod
	def array(it):
		# /opt/haxe-git/std/Lambda.hx:43
		a = list()
		# /opt/haxe-git/std/Lambda.hx:44
		_hx_local_0 = HxOverrides.iterator(it)
		while _hx_local_0.hasNext():
			i = _hx_local_0.next()
			# /opt/haxe-git/std/Lambda.hx:45
			a.append(i)
		# /opt/haxe-git/std/Lambda.hx:46
		return a

	@staticmethod
	def list(it):
		# /opt/haxe-git/std/Lambda.hx:55
		l = List()
		# /opt/haxe-git/std/Lambda.hx:56
		_hx_local_0 = HxOverrides.iterator(it)
		while _hx_local_0.hasNext():
			i = _hx_local_0.next()
			# /opt/haxe-git/std/Lambda.hx:57
			l.add(i)
		# /opt/haxe-git/std/Lambda.hx:58
		return l

	@staticmethod
	def map(it,f):
		# /opt/haxe-git/std/Lambda.hx:69
		l = List()
		# /opt/haxe-git/std/Lambda.hx:70
		_hx_local_0 = HxOverrides.iterator(it)
		while _hx_local_0.hasNext():
			x = _hx_local_0.next()
			# /opt/haxe-git/std/Lambda.hx:71
			l.add(f(x))
		# /opt/haxe-git/std/Lambda.hx:72
		return l

	@staticmethod
	def mapi(it,f):
		# /opt/haxe-git/std/Lambda.hx:83
		l = List()
		# /opt/haxe-git/std/Lambda.hx:84
		i = 0
		# /opt/haxe-git/std/Lambda.hx:85
		_hx_local_2 = HxOverrides.iterator(it)
		while _hx_local_2.hasNext():
			x = _hx_local_2.next()
			# /opt/haxe-git/std/Lambda.hx:86
			def _hx_local_1():
				# /opt/haxe-git/std/Lambda.hx:86
				nonlocal i
				_hx_local_0 = i
				i = (i + 1)
				return _hx_local_0
			l.add(f(_hx_local_1(),x))
		# /opt/haxe-git/std/Lambda.hx:87
		return l

	@staticmethod
	def has(it,elt):
		# /opt/haxe-git/std/Lambda.hx:99
		_hx_local_0 = HxOverrides.iterator(it)
		while _hx_local_0.hasNext():
			x = _hx_local_0.next()
			# /opt/haxe-git/std/Lambda.hx:100
			if (x == elt):
				return True
		# /opt/haxe-git/std/Lambda.hx:102
		return False

	@staticmethod
	def exists(it,f):
		# /opt/haxe-git/std/Lambda.hx:116
		_hx_local_0 = HxOverrides.iterator(it)
		while _hx_local_0.hasNext():
			x = _hx_local_0.next()
			# /opt/haxe-git/std/Lambda.hx:117
			if f(x):
				return True
		# /opt/haxe-git/std/Lambda.hx:119
		return False

	@staticmethod
	def foreach(it,f):
		# /opt/haxe-git/std/Lambda.hx:135
		_hx_local_0 = HxOverrides.iterator(it)
		while _hx_local_0.hasNext():
			x = _hx_local_0.next()
			# /opt/haxe-git/std/Lambda.hx:136
			if (not f(x)):
				return False
		# /opt/haxe-git/std/Lambda.hx:138
		return True

	@staticmethod
	def iter(it,f):
		# /opt/haxe-git/std/Lambda.hx:147
		_hx_local_0 = HxOverrides.iterator(it)
		while _hx_local_0.hasNext():
			x = _hx_local_0.next()
			# /opt/haxe-git/std/Lambda.hx:148
			f(x)

	@staticmethod
	def filter(it,f):
		# /opt/haxe-git/std/Lambda.hx:160
		l = List()
		# /opt/haxe-git/std/Lambda.hx:161
		_hx_local_0 = HxOverrides.iterator(it)
		while _hx_local_0.hasNext():
			x = _hx_local_0.next()
			# /opt/haxe-git/std/Lambda.hx:162
			if f(x):
				l.add(x)
		# /opt/haxe-git/std/Lambda.hx:164
		return l

	@staticmethod
	def fold(it,f,first):
		# /opt/haxe-git/std/Lambda.hx:180
		_hx_local_0 = HxOverrides.iterator(it)
		while _hx_local_0.hasNext():
			x = _hx_local_0.next()
			# /opt/haxe-git/std/Lambda.hx:181
			first = f(x,first)
		# /opt/haxe-git/std/Lambda.hx:182
		return first

	@staticmethod
	def count(it,pred = None):
		# /opt/haxe-git/std/Lambda.hx:192
		n = 0
		# /opt/haxe-git/std/Lambda.hx:193
		if (pred is None):
			# /opt/haxe-git/std/Lambda.hx:194
			_hx_local_1 = HxOverrides.iterator(it)
			while _hx_local_1.hasNext():
				_ = _hx_local_1.next()
				# /opt/haxe-git/std/Lambda.hx:195
				n = (n + 1)
		else:
			# /opt/haxe-git/std/Lambda.hx:197
			_hx_local_3 = HxOverrides.iterator(it)
			while _hx_local_3.hasNext():
				x = _hx_local_3.next()
				# /opt/haxe-git/std/Lambda.hx:198
				if pred(x):
					n = (n + 1)
		# /opt/haxe-git/std/Lambda.hx:200
		return n

	@staticmethod
	def empty(it):
		# /opt/haxe-git/std/Lambda.hx:207
		return (not HxOverrides.iterator(it).hasNext())

	@staticmethod
	def indexOf(it,v):
		# /opt/haxe-git/std/Lambda.hx:218
		i = 0
		# /opt/haxe-git/std/Lambda.hx:219
		_hx_local_1 = HxOverrides.iterator(it)
		while _hx_local_1.hasNext():
			v2 = _hx_local_1.next()
			# /opt/haxe-git/std/Lambda.hx:220
			if (v == v2):
				return i
			# /opt/haxe-git/std/Lambda.hx:222
			i = (i + 1)
		# /opt/haxe-git/std/Lambda.hx:224
		return -1

	@staticmethod
	def find(it,f):
		# /opt/haxe-git/std/Lambda.hx:238
		_hx_local_0 = HxOverrides.iterator(it)
		while _hx_local_0.hasNext():
			v = _hx_local_0.next()
			# /opt/haxe-git/std/Lambda.hx:239
			if f(v):
				return v
		# /opt/haxe-git/std/Lambda.hx:241
		return None

	@staticmethod
	def concat(a,b):
		# /opt/haxe-git/std/Lambda.hx:251
		l = List()
		# /opt/haxe-git/std/Lambda.hx:252
		_hx_local_0 = HxOverrides.iterator(a)
		while _hx_local_0.hasNext():
			x = _hx_local_0.next()
			# /opt/haxe-git/std/Lambda.hx:253
			l.add(x)
		# /opt/haxe-git/std/Lambda.hx:254
		_hx_local_1 = HxOverrides.iterator(b)
		while _hx_local_1.hasNext():
			x1 = _hx_local_1.next()
			# /opt/haxe-git/std/Lambda.hx:255
			l.add(x1)
		# /opt/haxe-git/std/Lambda.hx:256
		return l
Lambda._hx_class = Lambda
_hx_classes["Lambda"] = Lambda


class List:
	_hx_class_name = "List"
	_hx_fields = ["h", "q", "length"]
	_hx_methods = ["add", "push", "first", "last", "pop", "isEmpty", "clear", "remove", "iterator", "toString", "join", "filter", "map"]

	def __init__(self):
		# /opt/haxe-git/std/List.hx:29
		self.h = None
		# /opt/haxe-git/std/List.hx:30
		self.q = None
		# /opt/haxe-git/std/List.hx:35
		self.length = None
		# /opt/haxe-git/std/List.hx:41
		self.length = 0

	def add(self,item):
		# /opt/haxe-git/std/List.hx:50
		x = [item]
		# /opt/haxe-git/std/List.hx:51
		if (self.h is None):
			self.h = x
		else:
			python_internal_ArrayImpl._set(self.q, 1, x)
		# /opt/haxe-git/std/List.hx:55
		self.q = x
		# /opt/haxe-git/std/List.hx:56
		# /opt/haxe-git/std/List.hx:56
		_hx_local_0 = self
		_hx_local_1 = _hx_local_0.length
		_hx_local_0.length = (_hx_local_1 + 1)
		_hx_local_1

	def push(self,item):
		# /opt/haxe-git/std/List.hx:68
		x = [item, self.h]
		# /opt/haxe-git/std/List.hx:70
		self.h = x
		# /opt/haxe-git/std/List.hx:71
		if (self.q is None):
			self.q = x
		# /opt/haxe-git/std/List.hx:73
		# /opt/haxe-git/std/List.hx:73
		_hx_local_0 = self
		_hx_local_1 = _hx_local_0.length
		_hx_local_0.length = (_hx_local_1 + 1)
		_hx_local_1

	def first(self):
		# /opt/haxe-git/std/List.hx:82
		if (self.h is None):
			return None
		else:
			return (self.h[0] if 0 < len(self.h) else None)

	def last(self):
		# /opt/haxe-git/std/List.hx:91
		if (self.q is None):
			return None
		else:
			return (self.q[0] if 0 < len(self.q) else None)

	def pop(self):
		# /opt/haxe-git/std/List.hx:101
		if (self.h is None):
			return None
		# /opt/haxe-git/std/List.hx:103
		x = (self.h[0] if 0 < len(self.h) else None)
		# /opt/haxe-git/std/List.hx:104
		self.h = (self.h[1] if 1 < len(self.h) else None)
		# /opt/haxe-git/std/List.hx:105
		if (self.h is None):
			self.q = None
		# /opt/haxe-git/std/List.hx:107
		# /opt/haxe-git/std/List.hx:107
		_hx_local_0 = self
		_hx_local_1 = _hx_local_0.length
		_hx_local_0.length = (_hx_local_1 - 1)
		_hx_local_1
		# /opt/haxe-git/std/List.hx:108
		return x

	def isEmpty(self):
		# /opt/haxe-git/std/List.hx:115
		return (self.h is None)

	def clear(self):
		# /opt/haxe-git/std/List.hx:125
		self.h = None
		# /opt/haxe-git/std/List.hx:126
		self.q = None
		# /opt/haxe-git/std/List.hx:127
		self.length = 0

	def remove(self,v):
		# /opt/haxe-git/std/List.hx:139
		prev = None
		# /opt/haxe-git/std/List.hx:140
		l = self.h
		# /opt/haxe-git/std/List.hx:141
		while (l is not None):
			# /opt/haxe-git/std/List.hx:142
			if ((l[0] if 0 < len(l) else None) == v):
				# /opt/haxe-git/std/List.hx:143
				if (prev is None):
					self.h = (l[1] if 1 < len(l) else None)
				else:
					python_internal_ArrayImpl._set(prev, 1, (l[1] if 1 < len(l) else None))
				# /opt/haxe-git/std/List.hx:147
				if (self.q is l):
					self.q = prev
				# /opt/haxe-git/std/List.hx:149
				# /opt/haxe-git/std/List.hx:149
				_hx_local_0 = self
				_hx_local_1 = _hx_local_0.length
				_hx_local_0.length = (_hx_local_1 - 1)
				_hx_local_1
				# /opt/haxe-git/std/List.hx:150
				return True
			# /opt/haxe-git/std/List.hx:152
			prev = l
			# /opt/haxe-git/std/List.hx:153
			l = (l[1] if 1 < len(l) else None)
		# /opt/haxe-git/std/List.hx:155
		return False

	def iterator(self):
		# /opt/haxe-git/std/List.hx:162
		return _List_ListIterator(self.h)

	def toString(self):
		# /opt/haxe-git/std/List.hx:172
		s_b = python_lib_io_StringIO()
		# /opt/haxe-git/std/List.hx:173
		first = True
		# /opt/haxe-git/std/List.hx:174
		l = self.h
		# /opt/haxe-git/std/List.hx:175
		s_b.write("{")
		# /opt/haxe-git/std/List.hx:176
		while (l is not None):
			# /opt/haxe-git/std/List.hx:177
			if first:
				first = False
			else:
				s_b.write(", ")
			# /opt/haxe-git/std/List.hx:181
			s_b.write(Std.string(Std.string((l[0] if 0 < len(l) else None))))
			# /opt/haxe-git/std/List.hx:182
			l = (l[1] if 1 < len(l) else None)
		# /opt/haxe-git/std/List.hx:184
		s_b.write("}")
		# /opt/haxe-git/std/List.hx:185
		return s_b.getvalue()

	def join(self,sep):
		# /opt/haxe-git/std/List.hx:193
		s_b = python_lib_io_StringIO()
		# /opt/haxe-git/std/List.hx:194
		first = True
		# /opt/haxe-git/std/List.hx:195
		l = self.h
		# /opt/haxe-git/std/List.hx:196
		while (l is not None):
			# /opt/haxe-git/std/List.hx:197
			if first:
				first = False
			else:
				s_b.write(Std.string(sep))
			# /opt/haxe-git/std/List.hx:201
			# /opt/haxe-git/std/List.hx:201
			x = (l[0] if 0 < len(l) else None)
			s_b.write(Std.string(x))
			# /opt/haxe-git/std/List.hx:202
			l = (l[1] if 1 < len(l) else None)
		# /opt/haxe-git/std/List.hx:204
		return s_b.getvalue()

	def filter(self,f):
		# /opt/haxe-git/std/List.hx:212
		l2 = List()
		# /opt/haxe-git/std/List.hx:213
		l = self.h
		# /opt/haxe-git/std/List.hx:214
		while (l is not None):
			# /opt/haxe-git/std/List.hx:215
			v = (l[0] if 0 < len(l) else None)
			# /opt/haxe-git/std/List.hx:216
			l = (l[1] if 1 < len(l) else None)
			# /opt/haxe-git/std/List.hx:217
			if f(v):
				l2.add(v)
		# /opt/haxe-git/std/List.hx:220
		return l2

	def map(self,f):
		# /opt/haxe-git/std/List.hx:228
		b = List()
		# /opt/haxe-git/std/List.hx:229
		l = self.h
		# /opt/haxe-git/std/List.hx:230
		while (l is not None):
			# /opt/haxe-git/std/List.hx:231
			v = (l[0] if 0 < len(l) else None)
			# /opt/haxe-git/std/List.hx:232
			l = (l[1] if 1 < len(l) else None)
			# /opt/haxe-git/std/List.hx:233
			b.add(f(v))
		# /opt/haxe-git/std/List.hx:235
		return b

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.h = None
		_hx_o.q = None
		_hx_o.length = None
List._hx_class = List
_hx_classes["List"] = List


class _List_ListIterator:
	_hx_class_name = "_List.ListIterator"
	_hx_fields = ["head", "val"]
	_hx_methods = ["hasNext", "next"]

	def __init__(self,head):
		# /opt/haxe-git/std/List.hx:241
		self.head = None
		# /opt/haxe-git/std/List.hx:242
		self.val = None
		# /opt/haxe-git/std/List.hx:245
		self.head = head
		# /opt/haxe-git/std/List.hx:246
		self.val = None

	def hasNext(self):
		# /opt/haxe-git/std/List.hx:250
		return (self.head is not None)

	def next(self):
		# /opt/haxe-git/std/List.hx:254
		self.val = (self.head[0] if 0 < len(self.head) else None)
		# /opt/haxe-git/std/List.hx:255
		self.head = (self.head[1] if 1 < len(self.head) else None)
		# /opt/haxe-git/std/List.hx:256
		return self.val

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.head = None
		_hx_o.val = None
_List_ListIterator._hx_class = _List_ListIterator
_hx_classes["_List.ListIterator"] = _List_ListIterator


class _Map_Map_Impl_:
	_hx_class_name = "_Map.Map_Impl_"
	_hx_statics = ["_new", "set", "get", "exists", "remove", "keys", "iterator", "toString", "arrayWrite", "toStringMap", "toIntMap", "toEnumValueMapMap", "toObjectMap", "fromStringMap", "fromIntMap", "fromObjectMap"]
	_new = None

	@staticmethod
	def set(this1,key,value):
		# /opt/haxe-git/std/Map.hx:71
		this1.set(key,value)

	@staticmethod
	def get(this1,key):
		# /opt/haxe-git/std/Map.hx:88
		return this1.get(key)

	@staticmethod
	def exists(this1,key):
		# /opt/haxe-git/std/Map.hx:95
		return this1.exists(key)

	@staticmethod
	def remove(this1,key):
		# /opt/haxe-git/std/Map.hx:103
		return this1.remove(key)

	@staticmethod
	def keys(this1):
		# /opt/haxe-git/std/Map.hx:111
		return this1.keys()

	@staticmethod
	def iterator(this1):
		# /opt/haxe-git/std/Map.hx:120
		return this1.iterator()

	@staticmethod
	def toString(this1):
		# /opt/haxe-git/std/Map.hx:129
		return this1.toString()

	@staticmethod
	def arrayWrite(this1,k,v):
		# /opt/haxe-git/std/Map.hx:133
		this1.set(k,v)
		# /opt/haxe-git/std/Map.hx:134
		return v

	@staticmethod
	def toStringMap(t):
		# /opt/haxe-git/std/Map.hx:138
		return haxe_ds_StringMap()

	@staticmethod
	def toIntMap(t):
		# /opt/haxe-git/std/Map.hx:142
		return haxe_ds_IntMap()

	@staticmethod
	def toEnumValueMapMap(t):
		# /opt/haxe-git/std/Map.hx:146
		return haxe_ds_EnumValueMap()

	@staticmethod
	def toObjectMap(t):
		# /opt/haxe-git/std/Map.hx:150
		return haxe_ds_ObjectMap()

	@staticmethod
	def fromStringMap(_hx_map):
		# /opt/haxe-git/std/Map.hx:154
		return _hx_map

	@staticmethod
	def fromIntMap(_hx_map):
		# /opt/haxe-git/std/Map.hx:158
		return _hx_map

	@staticmethod
	def fromObjectMap(_hx_map):
		# /opt/haxe-git/std/Map.hx:162
		return _hx_map
_Map_Map_Impl_._hx_class = _Map_Map_Impl_
_hx_classes["_Map.Map_Impl_"] = _Map_Map_Impl_


class Reflect:
	_hx_class_name = "Reflect"
	_hx_statics = ["hasField", "field", "setField", "getProperty", "setProperty", "callMethod", "fields", "isFunction", "compare", "compareMethods", "isObject", "isEnumValue", "deleteField", "copy", "makeVarArgs"]

	@staticmethod
	def hasField(o,field):
		# /opt/haxe-git/std/python/_std/Reflect.hx:38
		return hasattr(o,(("_hx_" + field) if (field in python_Boot.keywords) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)))

	@staticmethod
	def field(o,field):
		# /opt/haxe-git/std/python/_std/Reflect.hx:44
		return python_Boot.field(o,field)

	@staticmethod
	def setField(o,field,value):
		# /opt/haxe-git/std/python/_std/Reflect.hx:49
		setattr(o,(("_hx_" + field) if (field in python_Boot.keywords) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)),value)

	@staticmethod
	def getProperty(o,field):
		# /opt/haxe-git/std/python/_std/Reflect.hx:54
		if (o is None):
			return None
		# /opt/haxe-git/std/python/_std/Reflect.hx:57
		if field in python_Boot.keywords:
			field = ("_hx_" + field)
		elif ((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95))):
			field = ("_hx_" + field)
		else:
			field = field
		# /opt/haxe-git/std/python/_std/Reflect.hx:58
		tmp = Reflect.field(o,("get_" + ("null" if field is None else field)))
		# /opt/haxe-git/std/python/_std/Reflect.hx:59
		if ((tmp is not None) and callable(tmp)):
			return tmp()
		else:
			return Reflect.field(o,field)

	@staticmethod
	def setProperty(o,field,value):
		# /opt/haxe-git/std/python/_std/Reflect.hx:67
		field1 = None
		if field in python_Boot.keywords:
			field1 = ("_hx_" + field)
		elif ((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95))):
			field1 = ("_hx_" + field)
		else:
			field1 = field
		# /opt/haxe-git/std/python/_std/Reflect.hx:68
		if hasattr(o,("set_" + ("null" if field1 is None else field1))):
			getattr(o,("set_" + ("null" if field1 is None else field1)))(value)
		else:
			setattr(o,field1,value)

	@staticmethod
	def callMethod(o,func,args):
		# /opt/haxe-git/std/python/_std/Reflect.hx:76
		if callable(func):
			return func(*args)
		else:
			return None

	@staticmethod
	def fields(o):
		# /opt/haxe-git/std/python/_std/Reflect.hx:81
		return python_Boot.fields(o)

	@staticmethod
	def isFunction(f):
		# /opt/haxe-git/std/python/_std/Reflect.hx:86
		return ((python_lib_Inspect.isfunction(f) or python_lib_Inspect.ismethod(f)) or hasattr(f,"func_code"))

	@staticmethod
	def compare(a,b):
		# /opt/haxe-git/std/python/_std/Reflect.hx:90
		if ((a is None) and ((b is None))):
			return 0
		# /opt/haxe-git/std/python/_std/Reflect.hx:92
		if (a is None):
			return 1
		elif (b is None):
			return -1
		elif (a == b):
			return 0
		elif (a > b):
			return 1
		else:
			return -1

	@staticmethod
	def compareMethods(f1,f2):
		# /opt/haxe-git/std/python/_std/Reflect.hx:97
		if HxOverrides.eq(f1,f2):
			return True
		# /opt/haxe-git/std/python/_std/Reflect.hx:99
		if ((not Reflect.isFunction(f1)) or (not Reflect.isFunction(f2))):
			return False
		# /opt/haxe-git/std/python/_std/Reflect.hx:102
		return False

	@staticmethod
	def isObject(v):
		# /opt/haxe-git/std/python/_std/Reflect.hx:106
		# /opt/haxe-git/std/python/_std/Reflect.hx:106
		_g = Type.typeof(v)
		if (((_g.index) == 6) or (((_g.index) == 4))):
			return True
		else:
			return False

	@staticmethod
	def isEnumValue(v):
		# /opt/haxe-git/std/python/_std/Reflect.hx:113
		return (not HxOverrides.eq(v,Enum) and isinstance(v,Enum))

	@staticmethod
	def deleteField(o,field):
		# /opt/haxe-git/std/python/_std/Reflect.hx:117
		if (not hasattr(o,(("_hx_" + field) if (field in python_Boot.keywords) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)))):
			return False
		# /opt/haxe-git/std/python/_std/Reflect.hx:118
		o.__delattr__(field)
		# /opt/haxe-git/std/python/_std/Reflect.hx:119
		return True

	@staticmethod
	def copy(o):
		# /opt/haxe-git/std/python/_std/Reflect.hx:123
		o2 = _hx_AnonObject({})
		# /opt/haxe-git/std/python/_std/Reflect.hx:124
		# /opt/haxe-git/std/python/_std/Reflect.hx:124
		_g = 0
		_g1 = python_Boot.fields(o)
		while (_g < len(_g1)):
			f = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
			_g = (_g + 1)
			# /opt/haxe-git/std/python/_std/Reflect.hx:125
			value = Reflect.field(o,f)
			setattr(o2,(("_hx_" + f) if (f in python_Boot.keywords) else (("_hx_" + f) if (((((len(f) > 2) and ((ord(f[0]) == 95))) and ((ord(f[1]) == 95))) and ((ord(f[(len(f) - 1)]) != 95)))) else f)),value)
		# /opt/haxe-git/std/python/_std/Reflect.hx:126
		return o2

	@staticmethod
	def makeVarArgs(f):
		# /opt/haxe-git/std/python/_std/Reflect.hx:131
		def _hx_local_0(*v):
			# /opt/haxe-git/std/python/_std/Reflect.hx:132
			return f((list(v) if ((not Std._hx_is(v,list))) else v))
		return _hx_local_0
Reflect._hx_class = Reflect
_hx_classes["Reflect"] = Reflect


class Std:
	_hx_class_name = "Std"
	_hx_statics = ["instance", "isMetaType", "is", "string", "int", "parseInt", "shortenPossibleNumber", "parseFloat", "random"]

	@staticmethod
	def instance(value,c):
		# /opt/haxe-git/std/python/_std/Std.hx:35
		try:
			if isinstance(value,c):
				return value
			else:
				return None
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			e = _hx_e1
			return None

	@staticmethod
	def isMetaType(v,t):
		# /opt/haxe-git/std/python/_std/Std.hx:44
		return (v == t)

	@staticmethod
	def _hx_is(v,t):
		# /opt/haxe-git/std/python/_std/Std.hx:50
		if ((v is None) and ((t is None))):
			return False
		# /opt/haxe-git/std/python/_std/Std.hx:53
		if (t is None):
			return False
		# /opt/haxe-git/std/python/_std/Std.hx:57
		if (t == Dynamic):
			return True
		# /opt/haxe-git/std/python/_std/Std.hx:60
		isBool = isinstance(v,bool)
		# /opt/haxe-git/std/python/_std/Std.hx:62
		if ((t == Bool) and isBool):
			return True
		# /opt/haxe-git/std/python/_std/Std.hx:65
		if ((((not isBool) and (not (t == Bool))) and (t == Int)) and isinstance(v,int)):
			return True
		# /opt/haxe-git/std/python/_std/Std.hx:68
		vIsFloat = isinstance(v,float)
		# /opt/haxe-git/std/python/_std/Std.hx:70
		def _hx_local_0():
			# /opt/haxe-git/std/python/_std/Std.hx:70
			f = v
			return (((f != Math.POSITIVE_INFINITY) and ((f != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(f)))
		def _hx_local_1():
			x = v
			def _hx_local_4():
				def _hx_local_3():
					_hx_local_2 = None
					try:
						_hx_local_2 = int(x)
					except Exception as _hx_e:
						_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
						e = _hx_e1
						_hx_local_2 = None
					return _hx_local_2
				return _hx_local_3()
			return _hx_local_4()
		if (((((((not isBool) and vIsFloat) and (t == Int)) and _hx_local_0()) and ((v == _hx_local_1()))) and ((v <= 2147483647))) and ((v >= -2147483648))):
			return True
		# /opt/haxe-git/std/python/_std/Std.hx:75
		if (((not isBool) and (t == Float)) and isinstance(v,(float, int))):
			return True
		# /opt/haxe-git/std/python/_std/Std.hx:79
		if (t == str):
			return isinstance(v,str)
		# /opt/haxe-git/std/python/_std/Std.hx:82
		isEnumType = (t == Enum)
		# /opt/haxe-git/std/python/_std/Std.hx:83
		if ((isEnumType and python_lib_Inspect.isclass(v)) and hasattr(v,"_hx_constructs")):
			return True
		# /opt/haxe-git/std/python/_std/Std.hx:85
		if isEnumType:
			return False
		# /opt/haxe-git/std/python/_std/Std.hx:87
		isClassType = (t == Class)
		# /opt/haxe-git/std/python/_std/Std.hx:88
		if ((((isClassType and (not isinstance(v,Enum))) and python_lib_Inspect.isclass(v)) and hasattr(v,"_hx_class_name")) and (not hasattr(v,"_hx_constructs"))):
			return True
		# /opt/haxe-git/std/python/_std/Std.hx:90
		if isClassType:
			return False
		# /opt/haxe-git/std/python/_std/Std.hx:92
		def _hx_local_6():
			# /opt/haxe-git/std/python/_std/Std.hx:92
			_hx_local_5 = None
			try:
				_hx_local_5 = isinstance(v,t)
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				e1 = _hx_e1
				_hx_local_5 = False
			return _hx_local_5
		if _hx_local_6():
			return True
		# /opt/haxe-git/std/python/_std/Std.hx:96
		if python_lib_Inspect.isclass(t):
			# /opt/haxe-git/std/python/_std/Std.hx:98
			loop = None
			loop1 = None
			# /opt/haxe-git/std/python/_std/Std.hx:99
			def _hx_local_8(intf):
				# /opt/haxe-git/std/python/_std/Std.hx:100
				f1 = None
				if hasattr(intf,"_hx_interfaces"):
					f1 = intf._hx_interfaces
				else:
					f1 = []
				# /opt/haxe-git/std/python/_std/Std.hx:101
				if (f1 is not None):
					# /opt/haxe-git/std/python/_std/Std.hx:102
					# /opt/haxe-git/std/python/_std/Std.hx:102
					_g = 0
					while (_g < len(f1)):
						i = (f1[_g] if _g >= 0 and _g < len(f1) else None)
						_g = (_g + 1)
						# /opt/haxe-git/std/python/_std/Std.hx:103
						if HxOverrides.eq(i,t):
							return True
						else:
							# /opt/haxe-git/std/python/_std/Std.hx:106
							l = loop1(i)
							# /opt/haxe-git/std/python/_std/Std.hx:107
							if l:
								return True
					# /opt/haxe-git/std/python/_std/Std.hx:112
					return False
				else:
					return False
			# /opt/haxe-git/std/python/_std/Std.hx:98
			loop1 = _hx_local_8
			loop = loop1
			# /opt/haxe-git/std/python/_std/Std.hx:117
			currentClass = v.__class__
			# /opt/haxe-git/std/python/_std/Std.hx:118
			while (currentClass is not None):
				# /opt/haxe-git/std/python/_std/Std.hx:119
				if loop(currentClass):
					return True
				# /opt/haxe-git/std/python/_std/Std.hx:122
				currentClass = python_Boot.getSuperClass(currentClass)
			# /opt/haxe-git/std/python/_std/Std.hx:124
			return False
		else:
			return False

	@staticmethod
	def string(s):
		# /opt/haxe-git/std/python/_std/Std.hx:133
		return python_Boot.toString1(s,"")

	@staticmethod
	def int(x):
		# /opt/haxe-git/std/python/_std/Std.hx:138
		try:
			return int(x)
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			e = _hx_e1
			return None

	@staticmethod
	def parseInt(x):
		# /opt/haxe-git/std/python/_std/Std.hx:146
		if (x is None):
			return None
		# /opt/haxe-git/std/python/_std/Std.hx:147
		try:
			return int(x)
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			e = _hx_e1
			try:
				# /opt/haxe-git/std/python/_std/Std.hx:151
				prefix = None
				_this = HxString.substr(x,0,2)
				prefix = _this.lower()
				# /opt/haxe-git/std/python/_std/Std.hx:153
				if (prefix == "0x"):
					return int(x,16)
				# /opt/haxe-git/std/python/_std/Std.hx:156
				raise _HxException("fail")
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				e1 = _hx_e1
				# /opt/haxe-git/std/python/_std/Std.hx:159
				r = None
				x1 = Std.parseFloat(x)
				try:
					r = int(x1)
				except Exception as _hx_e:
					_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
					e2 = _hx_e1
					r = None
				# /opt/haxe-git/std/python/_std/Std.hx:161
				if (r is None):
					# /opt/haxe-git/std/python/_std/Std.hx:162
					r1 = Std.shortenPossibleNumber(x)
					# /opt/haxe-git/std/python/_std/Std.hx:163
					if (r1 != x):
						return Std.parseInt(r1)
					else:
						return None
				# /opt/haxe-git/std/python/_std/Std.hx:169
				return r

	@staticmethod
	def shortenPossibleNumber(x):
		# /opt/haxe-git/std/python/_std/Std.hx:176
		r = ""
		# /opt/haxe-git/std/python/_std/Std.hx:177
		# /opt/haxe-git/std/python/_std/Std.hx:177
		_g1 = 0
		_g = len(x)
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			# /opt/haxe-git/std/python/_std/Std.hx:178
			c = None
			if ((i < 0) or ((i >= len(x)))):
				c = ""
			else:
				c = x[i]
			# /opt/haxe-git/std/python/_std/Std.hx:179
			# /opt/haxe-git/std/python/_std/Std.hx:179
			_g2 = HxString.charCodeAt(c,0)
			if (_g2 is not None):
				if (((((((((((_g2 == 46) or ((_g2 == 57))) or ((_g2 == 56))) or ((_g2 == 55))) or ((_g2 == 54))) or ((_g2 == 53))) or ((_g2 == 52))) or ((_g2 == 51))) or ((_g2 == 50))) or ((_g2 == 49))) or ((_g2 == 48))):
					r = (("null" if r is None else r) + ("null" if c is None else c))
				else:
					break
			else:
				break
		# /opt/haxe-git/std/python/_std/Std.hx:194
		return r

	@staticmethod
	def parseFloat(x):
		# /opt/haxe-git/std/python/_std/Std.hx:199
		try:
			return float(x)
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			e = _hx_e1
			# /opt/haxe-git/std/python/_std/Std.hx:203
			if (x is not None):
				# /opt/haxe-git/std/python/_std/Std.hx:204
				r1 = Std.shortenPossibleNumber(x)
				# /opt/haxe-git/std/python/_std/Std.hx:205
				if (r1 != x):
					return Std.parseFloat(r1)
			# /opt/haxe-git/std/python/_std/Std.hx:209
			return Math.NaN

	@staticmethod
	def random(x):
		# /opt/haxe-git/std/python/_std/Std.hx:214
		if (x <= 0):
			return 0
		else:
			# /opt/haxe-git/std/python/_std/Std.hx:217
			x1 = (python_lib_Random.random() * x)
			try:
				return int(x1)
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				e = _hx_e1
				return None
Std._hx_class = Std
_hx_classes["Std"] = Std


class Float:
	_hx_class_name = "Float"
Float._hx_class = Float
_hx_classes["Float"] = Float


class Int:
	_hx_class_name = "Int"
Int._hx_class = Int
_hx_classes["Int"] = Int


class Bool:
	_hx_class_name = "Bool"
Bool._hx_class = Bool
_hx_classes["Bool"] = Bool


class Dynamic:
	_hx_class_name = "Dynamic"
Dynamic._hx_class = Dynamic
_hx_classes["Dynamic"] = Dynamic


class StringBuf:
	_hx_class_name = "StringBuf"
	_hx_fields = ["b"]
	_hx_methods = ["get_length", "add", "add1", "addChar", "addSub", "toString"]

	def __init__(self):
		# /opt/haxe-git/std/python/_std/StringBuf.hx:48
		self.b = None
		# /opt/haxe-git/std/python/_std/StringBuf.hx:51
		self.b = python_lib_io_StringIO()

	def get_length(self):
		# /opt/haxe-git/std/python/_std/StringBuf.hx:57
		pos = self.b.tell()
		# /opt/haxe-git/std/python/_std/StringBuf.hx:58
		self.b.seek(0,2)
		# /opt/haxe-git/std/python/_std/StringBuf.hx:59
		_hx_len = self.b.tell()
		# /opt/haxe-git/std/python/_std/StringBuf.hx:60
		self.b.seek(pos,0)
		# /opt/haxe-git/std/python/_std/StringBuf.hx:61
		return _hx_len

	def add(self,x):
		# /opt/haxe-git/std/python/_std/StringBuf.hx:74
		self.b.write(Std.string(x))

	def add1(self,s):
		# /opt/haxe-git/std/python/_std/StringBuf.hx:78
		self.b.write(s)

	def addChar(self,c):
		# /opt/haxe-git/std/python/_std/StringBuf.hx:88
		s = "".join(map(chr,[c]))
		self.b.write(s)

	def addSub(self,s,pos,_hx_len = None):
		# /opt/haxe-git/std/python/_std/StringBuf.hx:104
		s1 = None
		if (_hx_len is None):
			s1 = HxString.substr(s,pos,None)
		else:
			s1 = HxString.substr(s,pos,_hx_len)
		self.b.write(s1)

	def toString(self):
		# /opt/haxe-git/std/python/_std/StringBuf.hx:113
		return self.b.getvalue()

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.b = None
StringBuf._hx_class = StringBuf
_hx_classes["StringBuf"] = StringBuf


class StringTools:
	_hx_class_name = "StringTools"
	_hx_statics = ["urlEncode", "urlDecode", "htmlEscape", "htmlUnescape", "startsWith", "endsWith", "isSpace", "ltrim", "rtrim", "trim", "lpad", "rpad", "replace", "hex", "fastCodeAt", "isEof"]

	@staticmethod
	def urlEncode(s):
		# /opt/haxe-git/std/StringTools.hx:52
		return python_lib_urllib_Parse.quote(s,"")

	@staticmethod
	def urlDecode(s):
		# /opt/haxe-git/std/StringTools.hx:77
		return python_lib_urllib_Parse.unquote(s)

	@staticmethod
	def htmlEscape(s,quotes = None):
		# /opt/haxe-git/std/StringTools.hx:98
		# /opt/haxe-git/std/StringTools.hx:98
		_this = None
		_this1 = None
		_this2 = None
		_this3 = None
		_this4 = s.split("&")
		_this3 = "&amp;".join([python_Boot.toString1(x1,'') for x1 in _this4])
		_this2 = _this3.split("<")
		_this1 = "&lt;".join([python_Boot.toString1(x1,'') for x1 in _this2])
		_this = _this1.split(">")
		s = "&gt;".join([python_Boot.toString1(x1,'') for x1 in _this])
		# /opt/haxe-git/std/StringTools.hx:99
		if quotes:
			# /opt/haxe-git/std/StringTools.hx:99
			_this5 = None
			_this6 = None
			_this7 = s.split("\"")
			_this6 = "&quot;".join([python_Boot.toString1(x1,'') for x1 in _this7])
			_this5 = _this6.split("'")
			return "&#039;".join([python_Boot.toString1(x1,'') for x1 in _this5])
		else:
			return s

	@staticmethod
	def htmlUnescape(s):
		# /opt/haxe-git/std/StringTools.hx:117
		_this = None
		_this1 = None
		_this2 = None
		_this3 = None
		_this4 = None
		_this5 = None
		_this6 = None
		_this7 = None
		_this8 = s.split("&gt;")
		_this7 = ">".join([python_Boot.toString1(x1,'') for x1 in _this8])
		_this6 = _this7.split("&lt;")
		_this5 = "<".join([python_Boot.toString1(x1,'') for x1 in _this6])
		_this4 = _this5.split("&quot;")
		_this3 = "\"".join([python_Boot.toString1(x1,'') for x1 in _this4])
		_this2 = _this3.split("&#039;")
		_this1 = "'".join([python_Boot.toString1(x1,'') for x1 in _this2])
		_this = _this1.split("&amp;")
		return "&".join([python_Boot.toString1(x1,'') for x1 in _this])

	@staticmethod
	def startsWith(s,start):
		# /opt/haxe-git/std/StringTools.hx:142
		return ((len(s) >= len(start)) and ((HxString.substr(s,0,len(start)) == start)))

	@staticmethod
	def endsWith(s,end):
		# /opt/haxe-git/std/StringTools.hx:168
		elen = len(end)
		# /opt/haxe-git/std/StringTools.hx:169
		slen = len(s)
		# /opt/haxe-git/std/StringTools.hx:170
		return ((slen >= elen) and ((HxString.substr(s,(slen - elen),elen) == end)))

	@staticmethod
	def isSpace(s,pos):
		# /opt/haxe-git/std/StringTools.hx:185
		if (((len(s) == 0) or ((pos < 0))) or ((pos >= len(s)))):
			return False
		# /opt/haxe-git/std/StringTools.hx:187
		c = HxString.charCodeAt(s,pos)
		# /opt/haxe-git/std/StringTools.hx:188
		return (((c > 8) and ((c < 14))) or ((c == 32)))

	@staticmethod
	def ltrim(s):
		# /opt/haxe-git/std/StringTools.hx:204
		l = len(s)
		# /opt/haxe-git/std/StringTools.hx:205
		r = 0
		# /opt/haxe-git/std/StringTools.hx:206
		while ((r < l) and StringTools.isSpace(s,r)):
			r = (r + 1)
		# /opt/haxe-git/std/StringTools.hx:209
		if (r > 0):
			return HxString.substr(s,r,(l - r))
		else:
			return s

	@staticmethod
	def rtrim(s):
		# /opt/haxe-git/std/StringTools.hx:229
		l = len(s)
		# /opt/haxe-git/std/StringTools.hx:230
		r = 0
		# /opt/haxe-git/std/StringTools.hx:231
		while ((r < l) and StringTools.isSpace(s,((l - r) - 1))):
			r = (r + 1)
		# /opt/haxe-git/std/StringTools.hx:234
		if (r > 0):
			return HxString.substr(s,0,(l - r))
		else:
			return s

	@staticmethod
	def trim(s):
		# /opt/haxe-git/std/StringTools.hx:253
		return StringTools.ltrim(StringTools.rtrim(s))

	@staticmethod
	def lpad(s,c,l):
		# /opt/haxe-git/std/StringTools.hx:270
		if (len(c) <= 0):
			return s
		# /opt/haxe-git/std/StringTools.hx:273
		while (len(s) < l):
			s = (("null" if c is None else c) + ("null" if s is None else s))
		# /opt/haxe-git/std/StringTools.hx:276
		return s

	@staticmethod
	def rpad(s,c,l):
		# /opt/haxe-git/std/StringTools.hx:292
		if (len(c) <= 0):
			return s
		# /opt/haxe-git/std/StringTools.hx:295
		while (len(s) < l):
			s = (("null" if s is None else s) + ("null" if c is None else c))
		# /opt/haxe-git/std/StringTools.hx:298
		return s

	@staticmethod
	def replace(s,sub,by):
		# /opt/haxe-git/std/StringTools.hx:324
		_this = None
		if (sub == ""):
			_this = list(s)
		else:
			_this = s.split(sub)
		return by.join([python_Boot.toString1(x1,'') for x1 in _this])

	@staticmethod
	def hex(n,digits = None):
		# /opt/haxe-git/std/StringTools.hx:340
		s = ""
		# /opt/haxe-git/std/StringTools.hx:341
		hexChars = "0123456789ABCDEF"
		# /opt/haxe-git/std/StringTools.hx:342
		while True:
			# /opt/haxe-git/std/StringTools.hx:343
			def _hx_local_0():
				# /opt/haxe-git/std/StringTools.hx:343
				index = (n & 15)
				return ("" if (((index < 0) or ((index >= len(hexChars))))) else hexChars[index])
			s = (HxOverrides.stringOrNull(_hx_local_0()) + ("null" if s is None else s))
			# /opt/haxe-git/std/StringTools.hx:344
			n = HxOverrides.rshift(n, 4)
			# /opt/haxe-git/std/StringTools.hx:345
			if (not ((n > 0))):
				break
		# /opt/haxe-git/std/StringTools.hx:348
		if ((digits is not None) and ((len(s) < digits))):
			# /opt/haxe-git/std/StringTools.hx:349
			diff = (digits - len(s))
			# /opt/haxe-git/std/StringTools.hx:350
			# /opt/haxe-git/std/StringTools.hx:350
			_g = 0
			while (_g < diff):
				_ = _g
				_g = (_g + 1)
				# /opt/haxe-git/std/StringTools.hx:351
				s = ("0" + ("null" if s is None else s))
		# /opt/haxe-git/std/StringTools.hx:359
		return s

	@staticmethod
	def fastCodeAt(s,index):
		# /opt/haxe-git/std/StringTools.hx:390
		if (index >= len(s)):
			return -1
		else:
			return ord(s[index])

	@staticmethod
	def isEof(c):
		# /opt/haxe-git/std/StringTools.hx:411
		return (c == -1)
StringTools._hx_class = StringTools
_hx_classes["StringTools"] = StringTools


class haxe_IMap:
	_hx_class_name = "haxe.IMap"
	_hx_methods = ["get", "set", "exists", "remove", "keys", "iterator", "toString"]
haxe_IMap._hx_class = haxe_IMap
_hx_classes["haxe.IMap"] = haxe_IMap


class haxe_ds_StringMap:
	_hx_class_name = "haxe.ds.StringMap"
	_hx_fields = ["h"]
	_hx_methods = ["set", "get", "exists", "remove", "keys", "iterator", "toString"]
	_hx_interfaces = [haxe_IMap]

	def __init__(self):
		# /opt/haxe-git/std/python/_std/haxe/ds/StringMap.hx:29
		self.h = None
		# /opt/haxe-git/std/python/_std/haxe/ds/StringMap.hx:32
		self.h = dict()

	def set(self,key,value):
		# /opt/haxe-git/std/python/_std/haxe/ds/StringMap.hx:36
		self.h[key] = value

	def get(self,key):
		# /opt/haxe-git/std/python/_std/haxe/ds/StringMap.hx:40
		return self.h.get(key,None)

	def exists(self,key):
		# /opt/haxe-git/std/python/_std/haxe/ds/StringMap.hx:44
		return key in self.h

	def remove(self,key):
		# /opt/haxe-git/std/python/_std/haxe/ds/StringMap.hx:48
		has = key in self.h
		# /opt/haxe-git/std/python/_std/haxe/ds/StringMap.hx:49
		if has:
			del self.h[key]
		# /opt/haxe-git/std/python/_std/haxe/ds/StringMap.hx:50
		return has

	def keys(self):
		# /opt/haxe-git/std/python/_std/haxe/ds/StringMap.hx:54
		# /opt/haxe-git/std/python/_std/haxe/ds/StringMap.hx:54
		this1 = None
		_this = self.h.keys()
		this1 = iter(_this)
		return python_HaxeIterator(this1)

	def iterator(self):
		# /opt/haxe-git/std/python/_std/haxe/ds/StringMap.hx:58
		# /opt/haxe-git/std/python/_std/haxe/ds/StringMap.hx:58
		this1 = None
		_this = self.h.values()
		this1 = iter(_this)
		return python_HaxeIterator(this1)

	def toString(self):
		# /opt/haxe-git/std/python/_std/haxe/ds/StringMap.hx:63
		s_b = python_lib_io_StringIO()
		# /opt/haxe-git/std/python/_std/haxe/ds/StringMap.hx:65
		s_b.write("{")
		# /opt/haxe-git/std/python/_std/haxe/ds/StringMap.hx:66
		it = self.keys()
		# /opt/haxe-git/std/python/_std/haxe/ds/StringMap.hx:67
		_hx_local_0 = it
		while _hx_local_0.hasNext():
			i = _hx_local_0.next()
			# /opt/haxe-git/std/python/_std/haxe/ds/StringMap.hx:68
			s_b.write(Std.string(i))
			# /opt/haxe-git/std/python/_std/haxe/ds/StringMap.hx:69
			s_b.write(" => ")
			# /opt/haxe-git/std/python/_std/haxe/ds/StringMap.hx:70
			# /opt/haxe-git/std/python/_std/haxe/ds/StringMap.hx:70
			x = Std.string(self.h.get(i,None))
			s_b.write(Std.string(x))
			# /opt/haxe-git/std/python/_std/haxe/ds/StringMap.hx:71
			if it.hasNext():
				s_b.write(", ")
		# /opt/haxe-git/std/python/_std/haxe/ds/StringMap.hx:74
		s_b.write("}")
		# /opt/haxe-git/std/python/_std/haxe/ds/StringMap.hx:75
		return s_b.getvalue()

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.h = None
haxe_ds_StringMap._hx_class = haxe_ds_StringMap
_hx_classes["haxe.ds.StringMap"] = haxe_ds_StringMap


class python_HaxeIterator:
	_hx_class_name = "python.HaxeIterator"
	_hx_fields = ["it", "x", "has", "checked"]
	_hx_methods = ["next", "hasNext"]

	def __init__(self,it):
		# /opt/haxe-git/std/python/HaxeIterator.hx:28
		self.it = None
		# /opt/haxe-git/std/python/HaxeIterator.hx:29
		self.x = None
		# /opt/haxe-git/std/python/HaxeIterator.hx:30
		self.has = None
		# /opt/haxe-git/std/python/HaxeIterator.hx:31
		self.checked = None
		self.checked = False
		# /opt/haxe-git/std/python/HaxeIterator.hx:30
		self.has = False
		# /opt/haxe-git/std/python/HaxeIterator.hx:29
		self.x = None
		# /opt/haxe-git/std/python/HaxeIterator.hx:34
		self.it = it

	def next(self):
		# /opt/haxe-git/std/python/HaxeIterator.hx:38
		if (not self.checked):
			self.hasNext()
		# /opt/haxe-git/std/python/HaxeIterator.hx:39
		self.checked = False
		# /opt/haxe-git/std/python/HaxeIterator.hx:40
		return self.x

	def hasNext(self):
		# /opt/haxe-git/std/python/HaxeIterator.hx:44
		if (not self.checked):
			# /opt/haxe-git/std/python/HaxeIterator.hx:45
			try:
				# /opt/haxe-git/std/python/HaxeIterator.hx:46
				self.x = self.it.__next__()
				# /opt/haxe-git/std/python/HaxeIterator.hx:47
				self.has = True
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				if isinstance(_hx_e1, StopIteration):
					s = _hx_e1
					# /opt/haxe-git/std/python/HaxeIterator.hx:49
					self.has = False
					# /opt/haxe-git/std/python/HaxeIterator.hx:50
					self.x = None
				else:
					raise _hx_e
			# /opt/haxe-git/std/python/HaxeIterator.hx:52
			self.checked = True
		# /opt/haxe-git/std/python/HaxeIterator.hx:54
		return self.has

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.it = None
		_hx_o.x = None
		_hx_o.has = None
		_hx_o.checked = None
python_HaxeIterator._hx_class = python_HaxeIterator
_hx_classes["python.HaxeIterator"] = python_HaxeIterator


class Sys:
	_hx_class_name = "Sys"
	_hx_statics = ["environ", "time", "exit", "print", "println", "args", "getEnv", "putEnv", "environment", "sleep", "setTimeLocale", "getCwd", "setCwd", "systemName", "command", "cpuTime", "executablePath", "getChar", "stdin", "stdout", "stderr"]

	@staticmethod
	def time():
		# /opt/haxe-git/std/python/_std/Sys.hx:42
		return python_lib_Time.time()

	@staticmethod
	def exit(code):
		# /opt/haxe-git/std/python/_std/Sys.hx:46
		python_lib_Sys.exit(code)

	@staticmethod
	def print(v):
		# /opt/haxe-git/std/python/_std/Sys.hx:50
		python_Lib.print(v)

	@staticmethod
	def println(v):
		# /opt/haxe-git/std/python/_std/Sys.hx:54
		python_Lib.println(v)

	@staticmethod
	def args():
		# /opt/haxe-git/std/python/_std/Sys.hx:58
		argv = python_lib_Sys.argv
		# /opt/haxe-git/std/python/_std/Sys.hx:59
		return argv[1:None]

	@staticmethod
	def getEnv(s):
		# /opt/haxe-git/std/python/_std/Sys.hx:63
		return Sys.environ.h.get(s,None)

	@staticmethod
	def putEnv(s,v):
		# /opt/haxe-git/std/python/_std/Sys.hx:67
		python_lib_Os.putenv(s,v)
		# /opt/haxe-git/std/python/_std/Sys.hx:68
		Sys.environ.h[s] = v

	@staticmethod
	def environment():
		# /opt/haxe-git/std/python/_std/Sys.hx:72
		return Sys.environ

	@staticmethod
	def sleep(seconds):
		# /opt/haxe-git/std/python/_std/Sys.hx:76
		python_lib_Time.sleep(seconds)

	@staticmethod
	def setTimeLocale(loc):
		# /opt/haxe-git/std/python/_std/Sys.hx:80
		return False

	@staticmethod
	def getCwd():
		# /opt/haxe-git/std/python/_std/Sys.hx:84
		return python_lib_Os.getcwd()

	@staticmethod
	def setCwd(s):
		# /opt/haxe-git/std/python/_std/Sys.hx:88
		python_lib_Os.chdir(s)

	@staticmethod
	def systemName():
		# /opt/haxe-git/std/python/_std/Sys.hx:92
		_g = python_lib_Sys.platform
		x = _g
		# /opt/haxe-git/std/python/_std/Sys.hx:93
		if StringTools.startsWith(x,"linux"):
			return "Linux"
		else:
			_hx_local_0 = len(_g)
			if (_hx_local_0 == 5):
				if (_g == "win32"):
					return "Windows"
				else:
					raise _HxException("not supported platform")
			elif (_hx_local_0 == 6):
				if (_g == "darwin"):
					return "Mac"
				elif (_g == "cygwin"):
					return "Windows"
				else:
					raise _HxException("not supported platform")
			else:
				raise _HxException("not supported platform")

	@staticmethod
	def command(cmd,args = None):
		# /opt/haxe-git/std/python/_std/Sys.hx:103
		args1 = None
		if (args is None):
			args1 = [cmd]
		else:
			args1 = ([cmd] + args)
		# /opt/haxe-git/std/python/_std/Sys.hx:104
		return python_lib_Subprocess.call(args1)

	@staticmethod
	def cpuTime():
		# /opt/haxe-git/std/python/_std/Sys.hx:108
		return python_lib_Time.clock()

	@staticmethod
	def executablePath():
		# /opt/haxe-git/std/python/_std/Sys.hx:112
		return python_internal_ArrayImpl._get(python_lib_Sys.argv, 0)

	@staticmethod
	def getChar(echo):
		# /opt/haxe-git/std/python/_std/Sys.hx:117
		ch = None
		_g = Sys.systemName()
		x = _g
		_hx_local_0 = len(_g)
		# /opt/haxe-git/std/python/_std/Sys.hx:118
		if (_hx_local_0 == 5):
			if (_g == "Linux"):
				# /opt/haxe-git/std/python/_std/Sys.hx:119
				fd = python_lib_Sys.stdin.fileno()
				# /opt/haxe-git/std/python/_std/Sys.hx:120
				old = python_lib_Termios.tcgetattr(fd)
				# /opt/haxe-git/std/python/_std/Sys.hx:122
				restore = None
				a1 = fd
				a3 = old
				def _hx_local_1():
					python_lib_Termios.tcsetattr(a1,python_lib_Termios.TCSADRAIN,a3)
				restore = _hx_local_1
				# /opt/haxe-git/std/python/_std/Sys.hx:124
				try:
					# /opt/haxe-git/std/python/_std/Sys.hx:125
					python_lib_Tty.setraw(fd)
					# /opt/haxe-git/std/python/_std/Sys.hx:126
					x1 = python_lib_Sys.stdin.read(1)
					# /opt/haxe-git/std/python/_std/Sys.hx:127
					restore()
					# /opt/haxe-git/std/python/_std/Sys.hx:128
					ch = HxString.charCodeAt(x1,0)
				except Exception as _hx_e:
					_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
					e = _hx_e1
					# /opt/haxe-git/std/python/_std/Sys.hx:130
					restore()
					# /opt/haxe-git/std/python/_std/Sys.hx:131
					raise _HxException(e)
			else:
				raise _HxException((("platform " + ("null" if x is None else x)) + " not supported"))
		elif (_hx_local_0 == 3):
			if (_g == "Mac"):
				# /opt/haxe-git/std/python/_std/Sys.hx:119
				fd = python_lib_Sys.stdin.fileno()
				# /opt/haxe-git/std/python/_std/Sys.hx:120
				old = python_lib_Termios.tcgetattr(fd)
				# /opt/haxe-git/std/python/_std/Sys.hx:122
				restore = None
				a1 = fd
				a3 = old
				def _hx_local_2():
					python_lib_Termios.tcsetattr(a1,python_lib_Termios.TCSADRAIN,a3)
				restore = _hx_local_2
				# /opt/haxe-git/std/python/_std/Sys.hx:124
				try:
					# /opt/haxe-git/std/python/_std/Sys.hx:125
					python_lib_Tty.setraw(fd)
					# /opt/haxe-git/std/python/_std/Sys.hx:126
					x1 = python_lib_Sys.stdin.read(1)
					# /opt/haxe-git/std/python/_std/Sys.hx:127
					restore()
					# /opt/haxe-git/std/python/_std/Sys.hx:128
					ch = HxString.charCodeAt(x1,0)
				except Exception as _hx_e:
					_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
					e = _hx_e1
					# /opt/haxe-git/std/python/_std/Sys.hx:130
					restore()
					# /opt/haxe-git/std/python/_std/Sys.hx:131
					raise _HxException(e)
			else:
				raise _HxException((("platform " + ("null" if x is None else x)) + " not supported"))
		elif (_hx_local_0 == 7):
			if (_g == "Windows"):
				# /opt/haxe-git/std/python/_std/Sys.hx:135
				_this = python_lib_Msvcrt.getch().decode("utf-8")
				ch = HxString.charCodeAt(_this,0)
			else:
				raise _HxException((("platform " + ("null" if x is None else x)) + " not supported"))
		else:
			raise _HxException((("platform " + ("null" if x is None else x)) + " not supported"))
		# /opt/haxe-git/std/python/_std/Sys.hx:139
		if echo:
			python_Lib.print("".join(map(chr,[ch])))
		# /opt/haxe-git/std/python/_std/Sys.hx:142
		return ch

	@staticmethod
	def stdin():
		# /opt/haxe-git/std/python/_std/Sys.hx:146
		return python_io_IoTools.createFileInputFromText(python_lib_Sys.stdin)

	@staticmethod
	def stdout():
		# /opt/haxe-git/std/python/_std/Sys.hx:150
		return python_io_IoTools.createFileOutputFromText(python_lib_Sys.stdout)

	@staticmethod
	def stderr():
		# /opt/haxe-git/std/python/_std/Sys.hx:154
		return python_io_IoTools.createFileOutputFromText(python_lib_Sys.stderr)
Sys._hx_class = Sys
_hx_classes["Sys"] = Sys

class ValueType(Enum):
	_hx_class_name = "ValueType"
	_hx_constructs = ["TNull", "TInt", "TFloat", "TBool", "TObject", "TFunction", "TClass", "TEnum", "TUnknown"]

	@staticmethod
	def TClass(c):
		return ValueType("TClass", 6, [c])

	@staticmethod
	def TEnum(e):
		return ValueType("TEnum", 7, [e])
ValueType.TNull = ValueType("TNull", 0, list())
ValueType.TInt = ValueType("TInt", 1, list())
ValueType.TFloat = ValueType("TFloat", 2, list())
ValueType.TBool = ValueType("TBool", 3, list())
ValueType.TObject = ValueType("TObject", 4, list())
ValueType.TFunction = ValueType("TFunction", 5, list())
ValueType.TUnknown = ValueType("TUnknown", 8, list())
ValueType._hx_class = ValueType
_hx_classes["ValueType"] = ValueType


class Type:
	_hx_class_name = "Type"
	_hx_statics = ["getClass", "getEnum", "getSuperClass", "getClassName", "getEnumName", "resolveClass", "resolveEnum", "createInstance", "createEmptyInstance", "createEnum", "createEnumIndex", "getInstanceFields", "getClassFields", "getEnumConstructs", "typeof", "asEnumImpl", "enumEq", "enumConstructor", "enumParameters", "enumIndex", "allEnums"]

	@staticmethod
	def getClass(o):
		# /opt/haxe-git/std/python/_std/Type.hx:46
		if (o is None):
			return None
		# /opt/haxe-git/std/python/_std/Type.hx:49
		if ((o is not None) and (((o == str) or python_lib_Inspect.isclass(o)))):
			return None
		# /opt/haxe-git/std/python/_std/Type.hx:51
		if isinstance(o,_hx_AnonObject):
			return None
		# /opt/haxe-git/std/python/_std/Type.hx:53
		if hasattr(o,"_hx_class"):
			return o._hx_class
		# /opt/haxe-git/std/python/_std/Type.hx:56
		if hasattr(o,"__class__"):
			return o.__class__
		else:
			return None

	@staticmethod
	def getEnum(o):
		# /opt/haxe-git/std/python/_std/Type.hx:64
		if (o is None):
			return None
		# /opt/haxe-git/std/python/_std/Type.hx:66
		return o.__class__

	@staticmethod
	def getSuperClass(c):
		# /opt/haxe-git/std/python/_std/Type.hx:70
		return python_Boot.getSuperClass(c)

	@staticmethod
	def getClassName(c):
		# /opt/haxe-git/std/python/_std/Type.hx:75
		if hasattr(c,"_hx_class_name"):
			return c._hx_class_name
		else:
			# /opt/haxe-git/std/python/_std/Type.hx:79
			if (c == list):
				return "Array"
			# /opt/haxe-git/std/python/_std/Type.hx:80
			if (c == Math):
				return "Math"
			# /opt/haxe-git/std/python/_std/Type.hx:81
			if (c == str):
				return "String"
			# /opt/haxe-git/std/python/_std/Type.hx:83
			try:
				s = c.__name__
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				pass
		# /opt/haxe-git/std/python/_std/Type.hx:87
		res = None
		# /opt/haxe-git/std/python/_std/Type.hx:89
		return res

	@staticmethod
	def getEnumName(e):
		# /opt/haxe-git/std/python/_std/Type.hx:93
		return e._hx_class_name

	@staticmethod
	def resolveClass(name):
		# /opt/haxe-git/std/python/_std/Type.hx:98
		if (name == "Array"):
			return list
		# /opt/haxe-git/std/python/_std/Type.hx:99
		if (name == "Math"):
			return Math
		# /opt/haxe-git/std/python/_std/Type.hx:100
		if (name == "String"):
			return str
		# /opt/haxe-git/std/python/_std/Type.hx:102
		cl = _hx_classes.get(name,None)
		# /opt/haxe-git/std/python/_std/Type.hx:104
		if ((cl is None) or (not (((cl is not None) and (((cl == str) or python_lib_Inspect.isclass(cl))))))):
			return None
		# /opt/haxe-git/std/python/_std/Type.hx:106
		return cl

	@staticmethod
	def resolveEnum(name):
		# /opt/haxe-git/std/python/_std/Type.hx:110
		if (name == "Bool"):
			return Bool
		# /opt/haxe-git/std/python/_std/Type.hx:111
		o = Type.resolveClass(name)
		# /opt/haxe-git/std/python/_std/Type.hx:112
		if hasattr(o,"_hx_constructs"):
			return o
		else:
			return None

	@staticmethod
	def createInstance(cl,args):
		# /opt/haxe-git/std/python/_std/Type.hx:117
		l = len(args)
		# /opt/haxe-git/std/python/_std/Type.hx:121
		if (l == 0):
			return cl()
		elif (l == 1):
			return cl((args[0] if 0 < len(args) else None))
		elif (l == 2):
			return cl((args[0] if 0 < len(args) else None), (args[1] if 1 < len(args) else None))
		elif (l == 3):
			return cl((args[0] if 0 < len(args) else None), (args[1] if 1 < len(args) else None), (args[2] if 2 < len(args) else None))
		elif (l == 4):
			return cl((args[0] if 0 < len(args) else None), (args[1] if 1 < len(args) else None), (args[2] if 2 < len(args) else None), (args[3] if 3 < len(args) else None))
		elif (l == 5):
			return cl((args[0] if 0 < len(args) else None), (args[1] if 1 < len(args) else None), (args[2] if 2 < len(args) else None), (args[3] if 3 < len(args) else None), (args[4] if 4 < len(args) else None))
		elif (l == 6):
			return cl((args[0] if 0 < len(args) else None), (args[1] if 1 < len(args) else None), (args[2] if 2 < len(args) else None), (args[3] if 3 < len(args) else None), (args[4] if 4 < len(args) else None), (args[5] if 5 < len(args) else None))
		elif (l == 7):
			return cl((args[0] if 0 < len(args) else None), (args[1] if 1 < len(args) else None), (args[2] if 2 < len(args) else None), (args[3] if 3 < len(args) else None), (args[4] if 4 < len(args) else None), (args[5] if 5 < len(args) else None), (args[6] if 6 < len(args) else None))
		elif (l == 8):
			return cl((args[0] if 0 < len(args) else None), (args[1] if 1 < len(args) else None), (args[2] if 2 < len(args) else None), (args[3] if 3 < len(args) else None), (args[4] if 4 < len(args) else None), (args[5] if 5 < len(args) else None), (args[6] if 6 < len(args) else None), (args[7] if 7 < len(args) else None))
		else:
			raise _HxException("Too many arguments")

	@staticmethod
	def createEmptyInstance(cl):
		# /opt/haxe-git/std/python/_std/Type.hx:145
		i = cl.__new__(cl)
		# /opt/haxe-git/std/python/_std/Type.hx:147
		callInit = None
		callInit1 = None
		def _hx_local_0(cl1):
			# /opt/haxe-git/std/python/_std/Type.hx:148
			sc = Type.getSuperClass(cl1)
			# /opt/haxe-git/std/python/_std/Type.hx:149
			if (sc is not None):
				callInit1(sc)
			# /opt/haxe-git/std/python/_std/Type.hx:152
			if hasattr(cl1,"_hx_empty_init"):
				cl1._hx_empty_init(i)
		callInit1 = _hx_local_0
		callInit = callInit1
		# /opt/haxe-git/std/python/_std/Type.hx:156
		callInit(cl)
		# /opt/haxe-git/std/python/_std/Type.hx:158
		return i

	@staticmethod
	def createEnum(e,constr,params = None):
		# /opt/haxe-git/std/python/_std/Type.hx:163
		f = Reflect.field(e,constr)
		# /opt/haxe-git/std/python/_std/Type.hx:164
		if (f is None):
			raise _HxException(("No such constructor " + ("null" if constr is None else constr)))
		# /opt/haxe-git/std/python/_std/Type.hx:165
		if Reflect.isFunction(f):
			# /opt/haxe-git/std/python/_std/Type.hx:166
			if (params is None):
				raise _HxException((("Constructor " + ("null" if constr is None else constr)) + " need parameters"))
			# /opt/haxe-git/std/python/_std/Type.hx:168
			return Reflect.callMethod(e,f,params)
		# /opt/haxe-git/std/python/_std/Type.hx:170
		if ((params is not None) and ((len(params) != 0))):
			raise _HxException((("Constructor " + ("null" if constr is None else constr)) + " does not need parameters"))
		# /opt/haxe-git/std/python/_std/Type.hx:172
		return f

	@staticmethod
	def createEnumIndex(e,index,params = None):
		# /opt/haxe-git/std/python/_std/Type.hx:177
		c = python_internal_ArrayImpl._get(e._hx_constructs, index)
		# /opt/haxe-git/std/python/_std/Type.hx:178
		if (c is None):
			raise _HxException((Std.string(index) + " is not a valid enum constructor index"))
		# /opt/haxe-git/std/python/_std/Type.hx:179
		return Type.createEnum(e,c,params)

	@staticmethod
	def getInstanceFields(c):
		# /opt/haxe-git/std/python/_std/Type.hx:183
		return python_Boot.getInstanceFields(c)

	@staticmethod
	def getClassFields(c):
		# /opt/haxe-git/std/python/_std/Type.hx:187
		return python_Boot.getClassFields(c)

	@staticmethod
	def getEnumConstructs(e):
		# /opt/haxe-git/std/python/_std/Type.hx:191
		if hasattr(e,"_hx_constructs"):
			# /opt/haxe-git/std/python/_std/Type.hx:192
			x = e._hx_constructs
			# /opt/haxe-git/std/python/_std/Type.hx:193
			return list(x)
		else:
			return []

	@staticmethod
	def typeof(v):
		# /opt/haxe-git/std/python/_std/Type.hx:202
		if (v is None):
			return ValueType.TNull
		elif isinstance(v,bool):
			return ValueType.TBool
		elif isinstance(v,int):
			return ValueType.TInt
		elif isinstance(v,float):
			return ValueType.TFloat
		elif isinstance(v,str):
			return ValueType.TClass(str)
		elif isinstance(v,list):
			return ValueType.TClass(list)
		elif (isinstance(v,_hx_AnonObject) or python_lib_Inspect.isclass(v)):
			return ValueType.TObject
		elif isinstance(v,Enum):
			return ValueType.TEnum(v.__class__)
		elif (isinstance(v,type) or hasattr(v,"_hx_class")):
			return ValueType.TClass(v.__class__)
		elif callable(v):
			return ValueType.TFunction
		else:
			return ValueType.TUnknown

	@staticmethod
	def asEnumImpl(x):
		# /opt/haxe-git/std/python/_std/Type.hx:230
		return x

	@staticmethod
	def enumEq(a,b):
		# /opt/haxe-git/std/python/_std/Type.hx:234
		if (a == b):
			return True
		# /opt/haxe-git/std/python/_std/Type.hx:236
		try:
			# /opt/haxe-git/std/python/_std/Type.hx:237
			if ((b is None) and ((a != b))):
				return False
			# /opt/haxe-git/std/python/_std/Type.hx:238
			if (a.tag != b.tag):
				return False
			# /opt/haxe-git/std/python/_std/Type.hx:240
			p1 = a.params
			# /opt/haxe-git/std/python/_std/Type.hx:241
			p2 = b.params
			# /opt/haxe-git/std/python/_std/Type.hx:242
			if (len(p1) != len(p2)):
				return False
			# /opt/haxe-git/std/python/_std/Type.hx:244
			# /opt/haxe-git/std/python/_std/Type.hx:244
			_g1 = 0
			_g = len(p1)
			while (_g1 < _g):
				i = _g1
				_g1 = (_g1 + 1)
				# /opt/haxe-git/std/python/_std/Type.hx:245
				if (not Type.enumEq((p1[i] if i >= 0 and i < len(p1) else None),(p2[i] if i >= 0 and i < len(p2) else None))):
					return False
			# /opt/haxe-git/std/python/_std/Type.hx:248
			if (a._hx_class != b._hx_class):
				return False
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			e = _hx_e1
			return False
		# /opt/haxe-git/std/python/_std/Type.hx:253
		return True

	@staticmethod
	def enumConstructor(e):
		# /opt/haxe-git/std/python/_std/Type.hx:257
		return e.tag

	@staticmethod
	def enumParameters(e):
		# /opt/haxe-git/std/python/_std/Type.hx:261
		return e.params

	@staticmethod
	def enumIndex(e):
		# /opt/haxe-git/std/python/_std/Type.hx:265
		return e.index

	@staticmethod
	def allEnums(e):
		# /opt/haxe-git/std/python/_std/Type.hx:270
		ctors = Type.getEnumConstructs(e)
		# /opt/haxe-git/std/python/_std/Type.hx:271
		ret = []
		# /opt/haxe-git/std/python/_std/Type.hx:272
		# /opt/haxe-git/std/python/_std/Type.hx:272
		_g = 0
		while (_g < len(ctors)):
			ctor = (ctors[_g] if _g >= 0 and _g < len(ctors) else None)
			_g = (_g + 1)
			# /opt/haxe-git/std/python/_std/Type.hx:274
			v = Reflect.field(e,ctor)
			# /opt/haxe-git/std/python/_std/Type.hx:275
			if Std._hx_is(v,e):
				# /opt/haxe-git/std/python/_std/Type.hx:276
				ret.append(v)
		# /opt/haxe-git/std/python/_std/Type.hx:279
		return ret
Type._hx_class = Type
_hx_classes["Type"] = Type


class haxe__Int32_Int32_Impl_:
	_hx_class_name = "haxe._Int32.Int32_Impl_"
	_hx_statics = ["preIncrement", "postIncrement", "preDecrement", "postDecrement", "add", "addInt", "sub", "subInt", "intSub", "mul", "mulInt", "shl", "shlInt", "intShl", "toFloat", "ucompare", "clamp"]

	@staticmethod
	def preIncrement(this1):
		# /opt/haxe-git/std/haxe/Int32.hx:32
		def _hx_local_3():
			# /opt/haxe-git/std/haxe/Int32.hx:32
			def _hx_local_0():
				# /opt/haxe-git/std/haxe/Int32.hx:32
				nonlocal this1
				this1 = (this1 + 1)
				x = this1
				def _hx_local_2():
					def _hx_local_1():
						nonlocal this1
						this1 = ((x + (2 ** 31)) % (2 ** 32) - (2 ** 31))
						return this1
					return _hx_local_1()
				return _hx_local_2()
			return _hx_local_0()
		return _hx_local_3()

	@staticmethod
	def postIncrement(this1):
		# /opt/haxe-git/std/haxe/Int32.hx:35
		ret = this1
		this1 = (this1 + 1)
		# /opt/haxe-git/std/haxe/Int32.hx:36
		this1 = ((this1 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		# /opt/haxe-git/std/haxe/Int32.hx:37
		return ret

	@staticmethod
	def preDecrement(this1):
		# /opt/haxe-git/std/haxe/Int32.hx:41
		def _hx_local_3():
			# /opt/haxe-git/std/haxe/Int32.hx:41
			def _hx_local_0():
				# /opt/haxe-git/std/haxe/Int32.hx:41
				nonlocal this1
				this1 = (this1 - 1)
				x = this1
				def _hx_local_2():
					def _hx_local_1():
						nonlocal this1
						this1 = ((x + (2 ** 31)) % (2 ** 32) - (2 ** 31))
						return this1
					return _hx_local_1()
				return _hx_local_2()
			return _hx_local_0()
		return _hx_local_3()

	@staticmethod
	def postDecrement(this1):
		# /opt/haxe-git/std/haxe/Int32.hx:44
		ret = this1
		this1 = (this1 - 1)
		# /opt/haxe-git/std/haxe/Int32.hx:45
		this1 = ((this1 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		# /opt/haxe-git/std/haxe/Int32.hx:46
		return ret

	@staticmethod
	def add(a,b):
		# /opt/haxe-git/std/haxe/Int32.hx:50
		return (((a + b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

	@staticmethod
	def addInt(a,b):
		# /opt/haxe-git/std/haxe/Int32.hx:53
		return (((a + b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

	@staticmethod
	def sub(a,b):
		# /opt/haxe-git/std/haxe/Int32.hx:58
		return (((a - b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

	@staticmethod
	def subInt(a,b):
		# /opt/haxe-git/std/haxe/Int32.hx:61
		return (((a - b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

	@staticmethod
	def intSub(a,b):
		# /opt/haxe-git/std/haxe/Int32.hx:64
		return (((a - b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

	@staticmethod
	def mul(a,b):
		# /opt/haxe-git/std/haxe/Int32.hx:73
		x = ((a * ((b & 65535))) + ((((((a * (HxOverrides.rshift(b, 16))) << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))))
		return ((x + (2 ** 31)) % (2 ** 32) - (2 ** 31))

	@staticmethod
	def mulInt(a,b):
		# /opt/haxe-git/std/haxe/Int32.hx:76
		return haxe__Int32_Int32_Impl_.mul(a,b)

	@staticmethod
	def shl(a,b):
		# /opt/haxe-git/std/haxe/Int32.hx:155
		return ((((a << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

	@staticmethod
	def shlInt(a,b):
		# /opt/haxe-git/std/haxe/Int32.hx:158
		return ((((a << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

	@staticmethod
	def intShl(a,b):
		# /opt/haxe-git/std/haxe/Int32.hx:161
		return ((((a << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

	@staticmethod
	def toFloat(this1):
		# /opt/haxe-git/std/haxe/Int32.hx:172
		return this1

	@staticmethod
	def ucompare(a,b):
		# /opt/haxe-git/std/haxe/Int32.hx:178
		if (a < 0):
			if (b < 0):
				return (((~b - ~a) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
			else:
				return 1
		# /opt/haxe-git/std/haxe/Int32.hx:180
		if (b < 0):
			return -1
		else:
			return (((a - b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

	@staticmethod
	def clamp(x):
		# /opt/haxe-git/std/haxe/Int32.hx:195
		return ((x + (2 ** 31)) % (2 ** 32) - (2 ** 31))
haxe__Int32_Int32_Impl_._hx_class = haxe__Int32_Int32_Impl_
_hx_classes["haxe._Int32.Int32_Impl_"] = haxe__Int32_Int32_Impl_


class haxe__Int64_Int64_Impl_:
	_hx_class_name = "haxe._Int64.Int64_Impl_"
	_hx_statics = ["_new", "copy", "make", "ofInt", "toInt", "is", "getHigh", "getLow", "isNeg", "isZero", "compare", "ucompare", "toStr", "toString", "divMod", "neg", "preIncrement", "postIncrement", "preDecrement", "postDecrement", "add", "addInt", "sub", "subInt", "intSub", "mul", "mulInt", "div", "divInt", "intDiv", "mod", "modInt", "intMod", "eq", "eqInt", "neq", "neqInt", "lt", "ltInt", "intLt", "lte", "lteInt", "intLte", "gt", "gtInt", "intGt", "gte", "gteInt", "intGte", "complement", "and", "or", "xor", "shl", "shr", "ushr", "get_high", "set_high", "get_low", "set_low"]
	high = None
	low = None

	@staticmethod
	def _new(x):
		# /opt/haxe-git/std/haxe/Int64.hx:36
		return x

	@staticmethod
	def copy(this1):
		# /opt/haxe-git/std/haxe/Int64.hx:42
		x = haxe__Int64____Int64(this1.high, this1.low)
		return x

	@staticmethod
	def make(high,low):
		# /opt/haxe-git/std/haxe/Int64.hx:48
		x = haxe__Int64____Int64(high, low)
		return x

	@staticmethod
	def ofInt(x):
		# /opt/haxe-git/std/haxe/Int64.hx:55
		x1 = haxe__Int64____Int64((x >> 31), x)
		return x1

	@staticmethod
	def toInt(x):
		# /opt/haxe-git/std/haxe/Int64.hx:62
		if (x.high != (x.low >> 31)):
			raise _HxException("Overflow")
		# /opt/haxe-git/std/haxe/Int64.hx:65
		return x.low

	@staticmethod
	def _hx_is(val):
		# /opt/haxe-git/std/haxe/Int64.hx:72
		return Std._hx_is(val,haxe__Int64____Int64)

	@staticmethod
	def getHigh(x):
		# /opt/haxe-git/std/haxe/Int64.hx:79
		return x.high

	@staticmethod
	def getLow(x):
		# /opt/haxe-git/std/haxe/Int64.hx:86
		return x.low

	@staticmethod
	def isNeg(x):
		# /opt/haxe-git/std/haxe/Int64.hx:92
		return (x.high < 0)

	@staticmethod
	def isZero(x):
		# /opt/haxe-git/std/haxe/Int64.hx:98
		b = None
		x1 = haxe__Int64____Int64(0, 0)
		b = x1
		return ((x.high == b.high) and (x.low == b.low))

	@staticmethod
	def compare(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:106
		v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		# /opt/haxe-git/std/haxe/Int64.hx:107
		if (v != 0):
			v = v
		else:
			v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
		# /opt/haxe-git/std/haxe/Int64.hx:108
		if (a.high < 0):
			if (b.high < 0):
				return v
			else:
				return -1
		elif (b.high >= 0):
			return v
		else:
			return 1

	@staticmethod
	def ucompare(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:117
		v = haxe__Int32_Int32_Impl_.ucompare(a.high,b.high)
		# /opt/haxe-git/std/haxe/Int64.hx:118
		if (v != 0):
			return v
		else:
			return haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)

	@staticmethod
	def toStr(x):
		# /opt/haxe-git/std/haxe/Int64.hx:125
		return haxe__Int64_Int64_Impl_.toString(x)

	@staticmethod
	def toString(this1):
		# /opt/haxe-git/std/haxe/Int64.hx:129
		i = this1
		# /opt/haxe-git/std/haxe/Int64.hx:130
		def _hx_local_0():
			# /opt/haxe-git/std/haxe/Int64.hx:130
			b = None
			x = haxe__Int64____Int64(0, 0)
			b = x
			return ((i.high == b.high) and (i.low == b.low))
		if _hx_local_0():
			return "0"
		# /opt/haxe-git/std/haxe/Int64.hx:132
		_hx_str = ""
		# /opt/haxe-git/std/haxe/Int64.hx:133
		neg = False
		# /opt/haxe-git/std/haxe/Int64.hx:134
		if (i.high < 0):
			# /opt/haxe-git/std/haxe/Int64.hx:135
			neg = True
			# /opt/haxe-git/std/haxe/Int64.hx:136
			# /opt/haxe-git/std/haxe/Int64.hx:136
			high = ~i.high
			low = -i.low
			if (low == 0):
				ret = high
				high = (high + 1)
				high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
				ret
			x1 = haxe__Int64____Int64(high, low)
			i = x1
		# /opt/haxe-git/std/haxe/Int64.hx:138
		ten = None
		x2 = haxe__Int64____Int64(0, 10)
		ten = x2
		# /opt/haxe-git/std/haxe/Int64.hx:139
		def _hx_local_1():
			# /opt/haxe-git/std/haxe/Int64.hx:139
			b1 = None
			x3 = haxe__Int64____Int64(0, 0)
			b1 = x3
			return ((i.high != b1.high) or (i.low != b1.low))
		while _hx_local_1():
			# /opt/haxe-git/std/haxe/Int64.hx:140
			r = haxe__Int64_Int64_Impl_.divMod(i,ten)
			# /opt/haxe-git/std/haxe/Int64.hx:141
			_hx_str = (Std.string(r.modulus.low) + ("null" if _hx_str is None else _hx_str))
			# /opt/haxe-git/std/haxe/Int64.hx:142
			i = r.quotient
		# /opt/haxe-git/std/haxe/Int64.hx:144
		if neg:
			_hx_str = ("-" + ("null" if _hx_str is None else _hx_str))
		# /opt/haxe-git/std/haxe/Int64.hx:145
		return _hx_str

	@staticmethod
	def divMod(dividend,divisor):
		# /opt/haxe-git/std/haxe/Int64.hx:155
		if (divisor.high == 0):
			# /opt/haxe-git/std/haxe/Int64.hx:157
			_g = divisor.low
			# /opt/haxe-git/std/haxe/Int64.hx:158
			if (_g == 0):
				raise _HxException("divide by zero")
			elif (_g == 1):
				# /opt/haxe-git/std/haxe/Int64.hx:159
				def _hx_local_2():
					# /opt/haxe-git/std/haxe/Int64.hx:159
					def _hx_local_0():
						# /opt/haxe-git/std/haxe/Int64.hx:159
						x = haxe__Int64____Int64(dividend.high, dividend.low)
						return x
					def _hx_local_1():
						x1 = haxe__Int64____Int64(0, 0)
						return x1
					return _hx_AnonObject({'quotient': _hx_local_0(), 'modulus': _hx_local_1()})
				return _hx_local_2()
			else:
				pass
		# /opt/haxe-git/std/haxe/Int64.hx:163
		divSign = ((dividend.high < 0) != (divisor.high < 0))
		# /opt/haxe-git/std/haxe/Int64.hx:165
		modulus = None
		if (dividend.high < 0):
			high = ~dividend.high
			low = -dividend.low
			if (low == 0):
				ret = high
				high = (high + 1)
				high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
				ret
			x2 = haxe__Int64____Int64(high, low)
			modulus = x2
		else:
			x3 = haxe__Int64____Int64(dividend.high, dividend.low)
			modulus = x3
		# /opt/haxe-git/std/haxe/Int64.hx:166
		if (divisor.high < 0):
			# /opt/haxe-git/std/haxe/Int64.hx:166
			high1 = ~divisor.high
			low1 = -divisor.low
			if (low1 == 0):
				ret1 = high1
				high1 = (high1 + 1)
				high1 = ((high1 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
				ret1
			x4 = haxe__Int64____Int64(high1, low1)
			divisor = x4
		else:
			divisor = divisor
		# /opt/haxe-git/std/haxe/Int64.hx:168
		quotient = None
		x5 = haxe__Int64____Int64(0, 0)
		quotient = x5
		# /opt/haxe-git/std/haxe/Int64.hx:169
		mask = None
		x6 = haxe__Int64____Int64(0, 1)
		mask = x6
		# /opt/haxe-git/std/haxe/Int64.hx:171
		while (not ((divisor.high < 0))):
			# /opt/haxe-git/std/haxe/Int64.hx:172
			cmp = None
			v = haxe__Int32_Int32_Impl_.ucompare(divisor.high,modulus.high)
			if (v != 0):
				cmp = v
			else:
				cmp = haxe__Int32_Int32_Impl_.ucompare(divisor.low,modulus.low)
			# /opt/haxe-git/std/haxe/Int64.hx:173
			# /opt/haxe-git/std/haxe/Int64.hx:173
			b = 1
			b = (b & 63)
			if (b == 0):
				x7 = haxe__Int64____Int64(divisor.high, divisor.low)
				divisor = x7
			elif (b < 32):
				high2 = (((((divisor.high << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(divisor.low, ((32 - b))))
				low2 = ((((divisor.low << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
				x8 = haxe__Int64____Int64(high2, low2)
				divisor = x8
			else:
				high3 = ((((divisor.low << (b - 32))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
				x9 = haxe__Int64____Int64(high3, 0)
				divisor = x9
			# /opt/haxe-git/std/haxe/Int64.hx:174
			# /opt/haxe-git/std/haxe/Int64.hx:174
			b1 = 1
			b1 = (b1 & 63)
			if (b1 == 0):
				x10 = haxe__Int64____Int64(mask.high, mask.low)
				mask = x10
			elif (b1 < 32):
				high4 = (((((mask.high << b1)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(mask.low, ((32 - b1))))
				low3 = ((((mask.low << b1)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
				x11 = haxe__Int64____Int64(high4, low3)
				mask = x11
			else:
				high5 = ((((mask.low << (b1 - 32))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
				x12 = haxe__Int64____Int64(high5, 0)
				mask = x12
			# /opt/haxe-git/std/haxe/Int64.hx:175
			if (cmp >= 0):
				break
		# /opt/haxe-git/std/haxe/Int64.hx:178
		def _hx_local_5():
			# /opt/haxe-git/std/haxe/Int64.hx:178
			b2 = None
			x13 = haxe__Int64____Int64(0, 0)
			b2 = x13
			return ((mask.high != b2.high) or (mask.low != b2.low))
		while _hx_local_5():
			# /opt/haxe-git/std/haxe/Int64.hx:179
			def _hx_local_6():
				# /opt/haxe-git/std/haxe/Int64.hx:179
				v1 = haxe__Int32_Int32_Impl_.ucompare(modulus.high,divisor.high)
				return (v1 if ((v1 != 0)) else haxe__Int32_Int32_Impl_.ucompare(modulus.low,divisor.low))
			if (_hx_local_6() >= 0):
				# /opt/haxe-git/std/haxe/Int64.hx:180
				# /opt/haxe-git/std/haxe/Int64.hx:180
				x14 = haxe__Int64____Int64((quotient.high | mask.high), (quotient.low | mask.low))
				quotient = x14
				# /opt/haxe-git/std/haxe/Int64.hx:181
				# /opt/haxe-git/std/haxe/Int64.hx:181
				high6 = (((modulus.high - divisor.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
				low4 = (((modulus.low - divisor.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
				if (haxe__Int32_Int32_Impl_.ucompare(modulus.low,divisor.low) < 0):
					ret2 = high6
					high6 = (high6 - 1)
					high6 = ((high6 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
					ret2
				x15 = haxe__Int64____Int64(high6, low4)
				modulus = x15
			# /opt/haxe-git/std/haxe/Int64.hx:183
			# /opt/haxe-git/std/haxe/Int64.hx:183
			b3 = 1
			b3 = (b3 & 63)
			if (b3 == 0):
				x16 = haxe__Int64____Int64(mask.high, mask.low)
				mask = x16
			elif (b3 < 32):
				low5 = (((((mask.high << (32 - b3))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(mask.low, b3))
				x17 = haxe__Int64____Int64(HxOverrides.rshift(mask.high, b3), low5)
				mask = x17
			else:
				x18 = haxe__Int64____Int64(0, HxOverrides.rshift(mask.high, ((b3 - 32))))
				mask = x18
			# /opt/haxe-git/std/haxe/Int64.hx:184
			# /opt/haxe-git/std/haxe/Int64.hx:184
			b4 = 1
			b4 = (b4 & 63)
			if (b4 == 0):
				x19 = haxe__Int64____Int64(divisor.high, divisor.low)
				divisor = x19
			elif (b4 < 32):
				low6 = (((((divisor.high << (32 - b4))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(divisor.low, b4))
				x20 = haxe__Int64____Int64(HxOverrides.rshift(divisor.high, b4), low6)
				divisor = x20
			else:
				x21 = haxe__Int64____Int64(0, HxOverrides.rshift(divisor.high, ((b4 - 32))))
				divisor = x21
		# /opt/haxe-git/std/haxe/Int64.hx:187
		if divSign:
			# /opt/haxe-git/std/haxe/Int64.hx:187
			high7 = ~quotient.high
			low7 = -quotient.low
			if (low7 == 0):
				ret3 = high7
				high7 = (high7 + 1)
				high7 = ((high7 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
				ret3
			x22 = haxe__Int64____Int64(high7, low7)
			quotient = x22
		# /opt/haxe-git/std/haxe/Int64.hx:188
		if (dividend.high < 0):
			# /opt/haxe-git/std/haxe/Int64.hx:188
			high8 = ~modulus.high
			low8 = -modulus.low
			if (low8 == 0):
				ret4 = high8
				high8 = (high8 + 1)
				high8 = ((high8 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
				ret4
			x23 = haxe__Int64____Int64(high8, low8)
			modulus = x23
		# /opt/haxe-git/std/haxe/Int64.hx:190
		return _hx_AnonObject({'quotient': quotient, 'modulus': modulus})

	@staticmethod
	def neg(x):
		# /opt/haxe-git/std/haxe/Int64.hx:200
		high = ~x.high
		# /opt/haxe-git/std/haxe/Int64.hx:201
		low = -x.low
		# /opt/haxe-git/std/haxe/Int64.hx:202
		if (low == 0):
			# /opt/haxe-git/std/haxe/Int64.hx:203
			ret = high
			high = (high + 1)
			high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
			ret
		# /opt/haxe-git/std/haxe/Int64.hx:204
		# /opt/haxe-git/std/haxe/Int64.hx:204
		x1 = haxe__Int64____Int64(high, low)
		return x1

	@staticmethod
	def preIncrement(this1):
		# /opt/haxe-git/std/haxe/Int64.hx:208
		# /opt/haxe-git/std/haxe/Int64.hx:208
		def _hx_local_1():
			# /opt/haxe-git/std/haxe/Int64.hx:208
			_hx_local_0 = this1.low
			this1.low = (this1.low + 1)
			return _hx_local_0
		ret = _hx_local_1()
		this1.low = ((this1.low + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		ret
		# /opt/haxe-git/std/haxe/Int64.hx:209
		if (this1.low == 0):
			# /opt/haxe-git/std/haxe/Int64.hx:209
			def _hx_local_3():
				# /opt/haxe-git/std/haxe/Int64.hx:209
				_hx_local_2 = this1.high
				this1.high = (this1.high + 1)
				return _hx_local_2
			ret1 = _hx_local_3()
			this1.high = ((this1.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
			ret1
		# /opt/haxe-git/std/haxe/Int64.hx:210
		return this1

	@staticmethod
	def postIncrement(this1):
		# /opt/haxe-git/std/haxe/Int64.hx:214
		ret = None
		x = haxe__Int64____Int64(this1.high, this1.low)
		ret = x
		# /opt/haxe-git/std/haxe/Int64.hx:215
		# /opt/haxe-git/std/haxe/Int64.hx:215
		# /opt/haxe-git/std/haxe/Int64.hx:215
		def _hx_local_2():
			# /opt/haxe-git/std/haxe/Int64.hx:215
			_hx_local_0 = this1
			_hx_local_1 = _hx_local_0.low
			_hx_local_0.low = (_hx_local_1 + 1)
			return _hx_local_1
		ret1 = _hx_local_2()
		this1.low = ((this1.low + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		ret1
		if (this1.low == 0):
			def _hx_local_5():
				_hx_local_3 = this1
				_hx_local_4 = _hx_local_3.high
				_hx_local_3.high = (_hx_local_4 + 1)
				return _hx_local_4
			ret2 = _hx_local_5()
			this1.high = ((this1.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
			ret2
		this1
		# /opt/haxe-git/std/haxe/Int64.hx:216
		return ret

	@staticmethod
	def preDecrement(this1):
		# /opt/haxe-git/std/haxe/Int64.hx:220
		if (this1.low == 0):
			# /opt/haxe-git/std/haxe/Int64.hx:220
			def _hx_local_1():
				# /opt/haxe-git/std/haxe/Int64.hx:220
				_hx_local_0 = this1.high
				this1.high = (this1.high - 1)
				return _hx_local_0
			ret = _hx_local_1()
			this1.high = ((this1.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
			ret
		# /opt/haxe-git/std/haxe/Int64.hx:221
		# /opt/haxe-git/std/haxe/Int64.hx:221
		def _hx_local_3():
			# /opt/haxe-git/std/haxe/Int64.hx:221
			_hx_local_2 = this1.low
			this1.low = (this1.low - 1)
			return _hx_local_2
		ret1 = _hx_local_3()
		this1.low = ((this1.low + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		ret1
		# /opt/haxe-git/std/haxe/Int64.hx:222
		return this1

	@staticmethod
	def postDecrement(this1):
		# /opt/haxe-git/std/haxe/Int64.hx:226
		ret = None
		x = haxe__Int64____Int64(this1.high, this1.low)
		ret = x
		# /opt/haxe-git/std/haxe/Int64.hx:227
		# /opt/haxe-git/std/haxe/Int64.hx:227
		if (this1.low == 0):
			# /opt/haxe-git/std/haxe/Int64.hx:227
			def _hx_local_2():
				# /opt/haxe-git/std/haxe/Int64.hx:227
				_hx_local_0 = this1
				_hx_local_1 = _hx_local_0.high
				_hx_local_0.high = (_hx_local_1 - 1)
				return _hx_local_1
			ret1 = _hx_local_2()
			this1.high = ((this1.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
			ret1
		def _hx_local_5():
			_hx_local_3 = this1
			_hx_local_4 = _hx_local_3.low
			_hx_local_3.low = (_hx_local_4 - 1)
			return _hx_local_4
		ret2 = _hx_local_5()
		this1.low = ((this1.low + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		ret2
		this1
		# /opt/haxe-git/std/haxe/Int64.hx:228
		return ret

	@staticmethod
	def add(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:235
		high = (((a.high + b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		# /opt/haxe-git/std/haxe/Int64.hx:236
		low = (((a.low + b.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		# /opt/haxe-git/std/haxe/Int64.hx:237
		if (haxe__Int32_Int32_Impl_.ucompare(low,a.low) < 0):
			# /opt/haxe-git/std/haxe/Int64.hx:237
			ret = high
			high = (high + 1)
			high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
			ret
		# /opt/haxe-git/std/haxe/Int64.hx:238
		# /opt/haxe-git/std/haxe/Int64.hx:238
		x = haxe__Int64____Int64(high, low)
		return x

	@staticmethod
	def addInt(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:242
		b1 = None
		x = haxe__Int64____Int64((b >> 31), b)
		b1 = x
		high = (((a.high + b1.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		low = (((a.low + b1.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		if (haxe__Int32_Int32_Impl_.ucompare(low,a.low) < 0):
			ret = high
			high = (high + 1)
			high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
			ret
		x1 = haxe__Int64____Int64(high, low)
		return x1

	@staticmethod
	def sub(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:248
		high = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		# /opt/haxe-git/std/haxe/Int64.hx:249
		low = (((a.low - b.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		# /opt/haxe-git/std/haxe/Int64.hx:250
		if (haxe__Int32_Int32_Impl_.ucompare(a.low,b.low) < 0):
			# /opt/haxe-git/std/haxe/Int64.hx:250
			ret = high
			high = (high - 1)
			high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
			ret
		# /opt/haxe-git/std/haxe/Int64.hx:251
		# /opt/haxe-git/std/haxe/Int64.hx:251
		x = haxe__Int64____Int64(high, low)
		return x

	@staticmethod
	def subInt(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:255
		b1 = None
		x = haxe__Int64____Int64((b >> 31), b)
		b1 = x
		high = (((a.high - b1.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		low = (((a.low - b1.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		if (haxe__Int32_Int32_Impl_.ucompare(a.low,b1.low) < 0):
			ret = high
			high = (high - 1)
			high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
			ret
		x1 = haxe__Int64____Int64(high, low)
		return x1

	@staticmethod
	def intSub(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:258
		a1 = None
		x = haxe__Int64____Int64((a >> 31), a)
		a1 = x
		high = (((a1.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		low = (((a1.low - b.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		if (haxe__Int32_Int32_Impl_.ucompare(a1.low,b.low) < 0):
			ret = high
			high = (high - 1)
			high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
			ret
		x1 = haxe__Int64____Int64(high, low)
		return x1

	@staticmethod
	def mul(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:264
		mask = 65535
		# /opt/haxe-git/std/haxe/Int64.hx:265
		al = (a.low & mask)
		ah = HxOverrides.rshift(a.low, 16)
		# /opt/haxe-git/std/haxe/Int64.hx:266
		bl = (b.low & mask)
		bh = HxOverrides.rshift(b.low, 16)
		# /opt/haxe-git/std/haxe/Int64.hx:267
		p00 = haxe__Int32_Int32_Impl_.mul(al,bl)
		# /opt/haxe-git/std/haxe/Int64.hx:268
		p10 = haxe__Int32_Int32_Impl_.mul(ah,bl)
		# /opt/haxe-git/std/haxe/Int64.hx:269
		p01 = haxe__Int32_Int32_Impl_.mul(al,bh)
		# /opt/haxe-git/std/haxe/Int64.hx:270
		p11 = haxe__Int32_Int32_Impl_.mul(ah,bh)
		# /opt/haxe-git/std/haxe/Int64.hx:271
		low = p00
		# /opt/haxe-git/std/haxe/Int64.hx:272
		high = None
		a1 = (((p11 + (HxOverrides.rshift(p01, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		high = (((a1 + (HxOverrides.rshift(p10, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		# /opt/haxe-git/std/haxe/Int64.hx:273
		p01 = ((((p01 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		# /opt/haxe-git/std/haxe/Int64.hx:274
		low = (((low + p01) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		# /opt/haxe-git/std/haxe/Int64.hx:275
		if (haxe__Int32_Int32_Impl_.ucompare(low,p01) < 0):
			# /opt/haxe-git/std/haxe/Int64.hx:275
			ret = high
			high = (high + 1)
			high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
			ret
		# /opt/haxe-git/std/haxe/Int64.hx:276
		p10 = ((((p10 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		# /opt/haxe-git/std/haxe/Int64.hx:277
		low = (((low + p10) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		# /opt/haxe-git/std/haxe/Int64.hx:278
		if (haxe__Int32_Int32_Impl_.ucompare(low,p10) < 0):
			# /opt/haxe-git/std/haxe/Int64.hx:278
			ret1 = high
			high = (high + 1)
			high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
			ret1
		# /opt/haxe-git/std/haxe/Int64.hx:279
		# /opt/haxe-git/std/haxe/Int64.hx:279
		b1 = None
		a2 = haxe__Int32_Int32_Impl_.mul(a.low,b.high)
		b2 = haxe__Int32_Int32_Impl_.mul(a.high,b.low)
		b1 = (((a2 + b2) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		high = (((high + b1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		# /opt/haxe-git/std/haxe/Int64.hx:280
		# /opt/haxe-git/std/haxe/Int64.hx:280
		x = haxe__Int64____Int64(high, low)
		return x

	@staticmethod
	def mulInt(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:284
		b1 = None
		x = haxe__Int64____Int64((b >> 31), b)
		b1 = x
		mask = 65535
		al = (a.low & mask)
		ah = HxOverrides.rshift(a.low, 16)
		bl = (b1.low & mask)
		bh = HxOverrides.rshift(b1.low, 16)
		p00 = haxe__Int32_Int32_Impl_.mul(al,bl)
		p10 = haxe__Int32_Int32_Impl_.mul(ah,bl)
		p01 = haxe__Int32_Int32_Impl_.mul(al,bh)
		p11 = haxe__Int32_Int32_Impl_.mul(ah,bh)
		low = p00
		high = None
		a1 = (((p11 + (HxOverrides.rshift(p01, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		high = (((a1 + (HxOverrides.rshift(p10, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		p01 = ((((p01 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		low = (((low + p01) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		if (haxe__Int32_Int32_Impl_.ucompare(low,p01) < 0):
			ret = high
			high = (high + 1)
			high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
			ret
		p10 = ((((p10 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		low = (((low + p10) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		if (haxe__Int32_Int32_Impl_.ucompare(low,p10) < 0):
			ret1 = high
			high = (high + 1)
			high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
			ret1
		b2 = None
		a2 = haxe__Int32_Int32_Impl_.mul(a.low,b1.high)
		b3 = haxe__Int32_Int32_Impl_.mul(a.high,b1.low)
		b2 = (((a2 + b3) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		high = (((high + b2) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
		x1 = haxe__Int64____Int64(high, low)
		return x1

	@staticmethod
	def div(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:290
		return haxe__Int64_Int64_Impl_.divMod(a,b).quotient

	@staticmethod
	def divInt(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:293
		b1 = None
		x = haxe__Int64____Int64((b >> 31), b)
		b1 = x
		return haxe__Int64_Int64_Impl_.divMod(a,b1).quotient

	@staticmethod
	def intDiv(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:296
		# /opt/haxe-git/std/haxe/Int64.hx:296
		x = None
		x1 = None
		a1 = None
		x2 = haxe__Int64____Int64((a >> 31), a)
		a1 = x2
		x1 = haxe__Int64_Int64_Impl_.divMod(a1,b).quotient
		if (x1.high != (x1.low >> 31)):
			raise _HxException("Overflow")
		x = x1.low
		x3 = haxe__Int64____Int64((x >> 31), x)
		return x3

	@staticmethod
	def mod(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:302
		return haxe__Int64_Int64_Impl_.divMod(a,b).modulus

	@staticmethod
	def modInt(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:305
		# /opt/haxe-git/std/haxe/Int64.hx:305
		x = None
		x1 = None
		b1 = None
		x2 = haxe__Int64____Int64((b >> 31), b)
		b1 = x2
		x1 = haxe__Int64_Int64_Impl_.divMod(a,b1).modulus
		if (x1.high != (x1.low >> 31)):
			raise _HxException("Overflow")
		x = x1.low
		x3 = haxe__Int64____Int64((x >> 31), x)
		return x3

	@staticmethod
	def intMod(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:308
		# /opt/haxe-git/std/haxe/Int64.hx:308
		x = None
		x1 = None
		a1 = None
		x2 = haxe__Int64____Int64((a >> 31), a)
		a1 = x2
		x1 = haxe__Int64_Int64_Impl_.divMod(a1,b).modulus
		if (x1.high != (x1.low >> 31)):
			raise _HxException("Overflow")
		x = x1.low
		x3 = haxe__Int64____Int64((x >> 31), x)
		return x3

	@staticmethod
	def eq(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:314
		return ((a.high == b.high) and (a.low == b.low))

	@staticmethod
	def eqInt(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:317
		b1 = None
		x = haxe__Int64____Int64((b >> 31), b)
		b1 = x
		return ((a.high == b1.high) and (a.low == b1.low))

	@staticmethod
	def neq(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:323
		return ((a.high != b.high) or (a.low != b.low))

	@staticmethod
	def neqInt(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:326
		b1 = None
		x = haxe__Int64____Int64((b >> 31), b)
		b1 = x
		return ((a.high != b1.high) or (a.low != b1.low))

	@staticmethod
	def lt(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:329
		def _hx_local_1():
			# /opt/haxe-git/std/haxe/Int64.hx:329
			def _hx_local_0():
				# /opt/haxe-git/std/haxe/Int64.hx:329
				v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
				if (v != 0):
					v = v
				else:
					v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
				return ((v if ((b.high < 0)) else -1) if ((a.high < 0)) else (v if ((b.high >= 0)) else 1))
			return (_hx_local_0() < 0)
		return _hx_local_1()

	@staticmethod
	def ltInt(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:332
		b1 = None
		x = haxe__Int64____Int64((b >> 31), b)
		b1 = x
		def _hx_local_1():
			def _hx_local_0():
				v = (((a.high - b1.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
				if (v != 0):
					v = v
				else:
					v = haxe__Int32_Int32_Impl_.ucompare(a.low,b1.low)
				return ((v if ((b1.high < 0)) else -1) if ((a.high < 0)) else (v if ((b1.high >= 0)) else 1))
			return (_hx_local_0() < 0)
		return _hx_local_1()

	@staticmethod
	def intLt(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:335
		a1 = None
		x = haxe__Int64____Int64((a >> 31), a)
		a1 = x
		def _hx_local_1():
			def _hx_local_0():
				v = (((a1.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
				if (v != 0):
					v = v
				else:
					v = haxe__Int32_Int32_Impl_.ucompare(a1.low,b.low)
				return ((v if ((b.high < 0)) else -1) if ((a1.high < 0)) else (v if ((b.high >= 0)) else 1))
			return (_hx_local_0() < 0)
		return _hx_local_1()

	@staticmethod
	def lte(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:338
		def _hx_local_1():
			# /opt/haxe-git/std/haxe/Int64.hx:338
			def _hx_local_0():
				# /opt/haxe-git/std/haxe/Int64.hx:338
				v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
				if (v != 0):
					v = v
				else:
					v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
				return ((v if ((b.high < 0)) else -1) if ((a.high < 0)) else (v if ((b.high >= 0)) else 1))
			return (_hx_local_0() <= 0)
		return _hx_local_1()

	@staticmethod
	def lteInt(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:341
		b1 = None
		x = haxe__Int64____Int64((b >> 31), b)
		b1 = x
		def _hx_local_1():
			def _hx_local_0():
				v = (((a.high - b1.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
				if (v != 0):
					v = v
				else:
					v = haxe__Int32_Int32_Impl_.ucompare(a.low,b1.low)
				return ((v if ((b1.high < 0)) else -1) if ((a.high < 0)) else (v if ((b1.high >= 0)) else 1))
			return (_hx_local_0() <= 0)
		return _hx_local_1()

	@staticmethod
	def intLte(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:344
		a1 = None
		x = haxe__Int64____Int64((a >> 31), a)
		a1 = x
		def _hx_local_1():
			def _hx_local_0():
				v = (((a1.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
				if (v != 0):
					v = v
				else:
					v = haxe__Int32_Int32_Impl_.ucompare(a1.low,b.low)
				return ((v if ((b.high < 0)) else -1) if ((a1.high < 0)) else (v if ((b.high >= 0)) else 1))
			return (_hx_local_0() <= 0)
		return _hx_local_1()

	@staticmethod
	def gt(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:347
		def _hx_local_1():
			# /opt/haxe-git/std/haxe/Int64.hx:347
			def _hx_local_0():
				# /opt/haxe-git/std/haxe/Int64.hx:347
				v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
				if (v != 0):
					v = v
				else:
					v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
				return ((v if ((b.high < 0)) else -1) if ((a.high < 0)) else (v if ((b.high >= 0)) else 1))
			return (_hx_local_0() > 0)
		return _hx_local_1()

	@staticmethod
	def gtInt(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:350
		b1 = None
		x = haxe__Int64____Int64((b >> 31), b)
		b1 = x
		def _hx_local_1():
			def _hx_local_0():
				v = (((a.high - b1.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
				if (v != 0):
					v = v
				else:
					v = haxe__Int32_Int32_Impl_.ucompare(a.low,b1.low)
				return ((v if ((b1.high < 0)) else -1) if ((a.high < 0)) else (v if ((b1.high >= 0)) else 1))
			return (_hx_local_0() > 0)
		return _hx_local_1()

	@staticmethod
	def intGt(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:353
		a1 = None
		x = haxe__Int64____Int64((a >> 31), a)
		a1 = x
		def _hx_local_1():
			def _hx_local_0():
				v = (((a1.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
				if (v != 0):
					v = v
				else:
					v = haxe__Int32_Int32_Impl_.ucompare(a1.low,b.low)
				return ((v if ((b.high < 0)) else -1) if ((a1.high < 0)) else (v if ((b.high >= 0)) else 1))
			return (_hx_local_0() > 0)
		return _hx_local_1()

	@staticmethod
	def gte(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:356
		def _hx_local_1():
			# /opt/haxe-git/std/haxe/Int64.hx:356
			def _hx_local_0():
				# /opt/haxe-git/std/haxe/Int64.hx:356
				v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
				if (v != 0):
					v = v
				else:
					v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
				return ((v if ((b.high < 0)) else -1) if ((a.high < 0)) else (v if ((b.high >= 0)) else 1))
			return (_hx_local_0() >= 0)
		return _hx_local_1()

	@staticmethod
	def gteInt(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:359
		b1 = None
		x = haxe__Int64____Int64((b >> 31), b)
		b1 = x
		def _hx_local_1():
			def _hx_local_0():
				v = (((a.high - b1.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
				if (v != 0):
					v = v
				else:
					v = haxe__Int32_Int32_Impl_.ucompare(a.low,b1.low)
				return ((v if ((b1.high < 0)) else -1) if ((a.high < 0)) else (v if ((b1.high >= 0)) else 1))
			return (_hx_local_0() >= 0)
		return _hx_local_1()

	@staticmethod
	def intGte(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:362
		a1 = None
		x = haxe__Int64____Int64((a >> 31), a)
		a1 = x
		def _hx_local_1():
			def _hx_local_0():
				v = (((a1.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
				if (v != 0):
					v = v
				else:
					v = haxe__Int32_Int32_Impl_.ucompare(a1.low,b.low)
				return ((v if ((b.high < 0)) else -1) if ((a1.high < 0)) else (v if ((b.high >= 0)) else 1))
			return (_hx_local_0() >= 0)
		return _hx_local_1()

	@staticmethod
	def complement(a):
		# /opt/haxe-git/std/haxe/Int64.hx:368
		x = haxe__Int64____Int64(~a.high, ~a.low)
		return x

	@staticmethod
	def _hx_and(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:374
		x = haxe__Int64____Int64((a.high & b.high), (a.low & b.low))
		return x

	@staticmethod
	def _hx_or(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:380
		x = haxe__Int64____Int64((a.high | b.high), (a.low | b.low))
		return x

	@staticmethod
	def xor(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:386
		x = haxe__Int64____Int64((a.high ^ b.high), (a.low ^ b.low))
		return x

	@staticmethod
	def shl(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:392
		b = (b & 63)
		# /opt/haxe-git/std/haxe/Int64.hx:393
		if (b == 0):
			# /opt/haxe-git/std/haxe/Int64.hx:393
			x = haxe__Int64____Int64(a.high, a.low)
			return x
		elif (b < 32):
			# /opt/haxe-git/std/haxe/Int64.hx:394
			high = (((((a.high << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(a.low, ((32 - b))))
			low = ((((a.low << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
			x1 = haxe__Int64____Int64(high, low)
			# /opt/haxe-git/std/haxe/Int64.hx:393
			return x1
		else:
			# /opt/haxe-git/std/haxe/Int64.hx:395
			high1 = ((((a.low << (b - 32))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
			x2 = haxe__Int64____Int64(high1, 0)
			# /opt/haxe-git/std/haxe/Int64.hx:393
			return x2

	@staticmethod
	def shr(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:403
		b = (b & 63)
		# /opt/haxe-git/std/haxe/Int64.hx:404
		if (b == 0):
			# /opt/haxe-git/std/haxe/Int64.hx:404
			x = haxe__Int64____Int64(a.high, a.low)
			return x
		elif (b < 32):
			# /opt/haxe-git/std/haxe/Int64.hx:405
			low = (((((a.high << (32 - b))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(a.low, b))
			x1 = haxe__Int64____Int64((a.high >> b), low)
			# /opt/haxe-git/std/haxe/Int64.hx:404
			return x1
		else:
			# /opt/haxe-git/std/haxe/Int64.hx:406
			x2 = haxe__Int64____Int64((a.high >> 31), (a.high >> ((b - 32))))
			# /opt/haxe-git/std/haxe/Int64.hx:404
			return x2

	@staticmethod
	def ushr(a,b):
		# /opt/haxe-git/std/haxe/Int64.hx:414
		b = (b & 63)
		# /opt/haxe-git/std/haxe/Int64.hx:415
		if (b == 0):
			# /opt/haxe-git/std/haxe/Int64.hx:415
			x = haxe__Int64____Int64(a.high, a.low)
			return x
		elif (b < 32):
			# /opt/haxe-git/std/haxe/Int64.hx:416
			low = (((((a.high << (32 - b))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(a.low, b))
			x1 = haxe__Int64____Int64(HxOverrides.rshift(a.high, b), low)
			# /opt/haxe-git/std/haxe/Int64.hx:415
			return x1
		else:
			# /opt/haxe-git/std/haxe/Int64.hx:417
			x2 = haxe__Int64____Int64(0, HxOverrides.rshift(a.high, ((b - 32))))
			# /opt/haxe-git/std/haxe/Int64.hx:415
			return x2

	@staticmethod
	def get_high(this1):
		# /opt/haxe-git/std/haxe/Int64.hx:421
		return this1.high

	@staticmethod
	def set_high(this1,x):
		# /opt/haxe-git/std/haxe/Int64.hx:422
		def _hx_local_1():
			# /opt/haxe-git/std/haxe/Int64.hx:422
			def _hx_local_0():
				# /opt/haxe-git/std/haxe/Int64.hx:422
				this1.high = x
				return this1.high
			return _hx_local_0()
		return _hx_local_1()

	@staticmethod
	def get_low(this1):
		# /opt/haxe-git/std/haxe/Int64.hx:425
		return this1.low

	@staticmethod
	def set_low(this1,x):
		# /opt/haxe-git/std/haxe/Int64.hx:426
		def _hx_local_1():
			# /opt/haxe-git/std/haxe/Int64.hx:426
			def _hx_local_0():
				# /opt/haxe-git/std/haxe/Int64.hx:426
				this1.low = x
				return this1.low
			return _hx_local_0()
		return _hx_local_1()
haxe__Int64_Int64_Impl_._hx_class = haxe__Int64_Int64_Impl_
_hx_classes["haxe._Int64.Int64_Impl_"] = haxe__Int64_Int64_Impl_


class haxe__Int64____Int64:
	_hx_class_name = "haxe._Int64.___Int64"
	_hx_fields = ["high", "low"]
	_hx_methods = ["toString"]

	def __init__(self,high,low):
		# /opt/haxe-git/std/haxe/Int64.hx:437
		self.high = None
		# /opt/haxe-git/std/haxe/Int64.hx:438
		self.low = None
		# /opt/haxe-git/std/haxe/Int64.hx:441
		self.high = high
		# /opt/haxe-git/std/haxe/Int64.hx:442
		self.low = low

	def toString(self):
		# /opt/haxe-git/std/haxe/Int64.hx:451
		return haxe__Int64_Int64_Impl_.toString(self)

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.high = None
		_hx_o.low = None
haxe__Int64____Int64._hx_class = haxe__Int64____Int64
_hx_classes["haxe._Int64.___Int64"] = haxe__Int64____Int64


class haxe_Log:
	_hx_class_name = "haxe.Log"
	_hx_statics = ["trace"]

	@staticmethod
	def trace(v,infos = None):
		# /opt/haxe-git/std/haxe/Log.hx:98
		_hx_str = None
		# /opt/haxe-git/std/haxe/Log.hx:99
		if (infos is not None):
			# /opt/haxe-git/std/haxe/Log.hx:100
			_hx_str = ((((HxOverrides.stringOrNull(infos.fileName) + ":") + Std.string(infos.lineNumber)) + ": ") + Std.string(v))
			# /opt/haxe-git/std/haxe/Log.hx:101
			if (Reflect.field(infos,"customParams") is not None):
				_hx_str = (("null" if _hx_str is None else _hx_str) + HxOverrides.stringOrNull((("," + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in Reflect.field(infos,"customParams")]))))))
		else:
			_hx_str = v
		# /opt/haxe-git/std/haxe/Log.hx:107
		python_Lib.println(_hx_str)
haxe_Log._hx_class = haxe_Log
_hx_classes["haxe.Log"] = haxe_Log


class haxe_Timer:
	_hx_class_name = "haxe.Timer"
	_hx_methods = ["stop", "run"]
	_hx_statics = ["delay", "measure", "stamp"]

	def __init__(self,time_ms):
		pass

	def stop(self):
		pass

	def run(self):
		pass

	@staticmethod
	def delay(f,time_ms):
		# /opt/haxe-git/std/haxe/Timer.hx:122
		t = haxe_Timer(time_ms)
		# /opt/haxe-git/std/haxe/Timer.hx:123
		def _hx_local_0():
			# /opt/haxe-git/std/haxe/Timer.hx:124
			t.stop()
			# /opt/haxe-git/std/haxe/Timer.hx:125
			f()
		t.run = _hx_local_0
		# /opt/haxe-git/std/haxe/Timer.hx:127
		return t

	@staticmethod
	def measure(f,pos = None):
		# /opt/haxe-git/std/haxe/Timer.hx:144
		t0 = haxe_Timer.stamp()
		# /opt/haxe-git/std/haxe/Timer.hx:145
		r = f()
		# /opt/haxe-git/std/haxe/Timer.hx:146
		haxe_Log.trace((Std.string((haxe_Timer.stamp() - t0)) + "s"),pos)
		# /opt/haxe-git/std/haxe/Timer.hx:147
		return r

	@staticmethod
	def stamp():
		# /opt/haxe-git/std/haxe/Timer.hx:166
		return Sys.time()

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
haxe_Timer._hx_class = haxe_Timer
_hx_classes["haxe.Timer"] = haxe_Timer


class haxe_Unserializer:
	_hx_class_name = "haxe.Unserializer"
	_hx_fields = ["buf", "pos", "length", "cache", "scache", "resolver"]
	_hx_methods = ["setResolver", "getResolver", "get", "readDigits", "readFloat", "unserializeObject", "unserializeEnum", "unserialize"]
	_hx_statics = ["DEFAULT_RESOLVER", "BASE64", "CODES", "initCodes", "run"]

	def __init__(self,buf):
		# /opt/haxe-git/std/haxe/Unserializer.hx:80
		self.buf = None
		# /opt/haxe-git/std/haxe/Unserializer.hx:81
		self.pos = None
		# /opt/haxe-git/std/haxe/Unserializer.hx:82
		self.length = None
		# /opt/haxe-git/std/haxe/Unserializer.hx:83
		self.cache = None
		# /opt/haxe-git/std/haxe/Unserializer.hx:84
		self.scache = None
		# /opt/haxe-git/std/haxe/Unserializer.hx:85
		self.resolver = None
		# /opt/haxe-git/std/haxe/Unserializer.hx:100
		self.buf = buf
		# /opt/haxe-git/std/haxe/Unserializer.hx:101
		self.length = len(buf)
		# /opt/haxe-git/std/haxe/Unserializer.hx:102
		self.pos = 0
		# /opt/haxe-git/std/haxe/Unserializer.hx:106
		self.scache = list()
		# /opt/haxe-git/std/haxe/Unserializer.hx:107
		self.cache = list()
		# /opt/haxe-git/std/haxe/Unserializer.hx:108
		r = haxe_Unserializer.DEFAULT_RESOLVER
		# /opt/haxe-git/std/haxe/Unserializer.hx:109
		if (r is None):
			# /opt/haxe-git/std/haxe/Unserializer.hx:110
			r = Type
			# /opt/haxe-git/std/haxe/Unserializer.hx:111
			haxe_Unserializer.DEFAULT_RESOLVER = r
		# /opt/haxe-git/std/haxe/Unserializer.hx:113
		self.setResolver(r)

	def setResolver(self,r):
		# /opt/haxe-git/std/haxe/Unserializer.hx:125
		if (r is None):
			# /opt/haxe-git/std/haxe/Unserializer.hx:127
			def _hx_local_0(_):
				# /opt/haxe-git/std/haxe/Unserializer.hx:127
				return None
			# /opt/haxe-git/std/haxe/Unserializer.hx:128
			def _hx_local_1(_1):
				# /opt/haxe-git/std/haxe/Unserializer.hx:128
				return None
			# /opt/haxe-git/std/haxe/Unserializer.hx:126
			self.resolver = _hx_AnonObject({'resolveClass': _hx_local_0, 'resolveEnum': _hx_local_1})
		else:
			self.resolver = r

	def getResolver(self):
		# /opt/haxe-git/std/haxe/Unserializer.hx:140
		return self.resolver

	def get(self,p):
		# /opt/haxe-git/std/haxe/Unserializer.hx:144
		s = self.buf
		if (p >= len(s)):
			return -1
		else:
			return ord(s[p])

	def readDigits(self):
		# /opt/haxe-git/std/haxe/Unserializer.hx:148
		k = 0
		# /opt/haxe-git/std/haxe/Unserializer.hx:149
		s = False
		# /opt/haxe-git/std/haxe/Unserializer.hx:150
		fpos = self.pos
		# /opt/haxe-git/std/haxe/Unserializer.hx:151
		while True:
			# /opt/haxe-git/std/haxe/Unserializer.hx:152
			c = None
			p = self.pos
			s1 = self.buf
			if (p >= len(s1)):
				c = -1
			else:
				c = ord(s1[p])
			# /opt/haxe-git/std/haxe/Unserializer.hx:153
			if (c == -1):
				break
			# /opt/haxe-git/std/haxe/Unserializer.hx:155
			if (c == 45):
				# /opt/haxe-git/std/haxe/Unserializer.hx:156
				if (self.pos != fpos):
					break
				# /opt/haxe-git/std/haxe/Unserializer.hx:158
				s = True
				# /opt/haxe-git/std/haxe/Unserializer.hx:159
				# /opt/haxe-git/std/haxe/Unserializer.hx:159
				_hx_local_0 = self
				_hx_local_1 = _hx_local_0.pos
				_hx_local_0.pos = (_hx_local_1 + 1)
				_hx_local_1
				# /opt/haxe-git/std/haxe/Unserializer.hx:160
				continue
			# /opt/haxe-git/std/haxe/Unserializer.hx:162
			if ((c < 48) or ((c > 57))):
				break
			# /opt/haxe-git/std/haxe/Unserializer.hx:164
			k = ((k * 10) + ((c - 48)))
			# /opt/haxe-git/std/haxe/Unserializer.hx:165
			# /opt/haxe-git/std/haxe/Unserializer.hx:165
			_hx_local_2 = self
			_hx_local_3 = _hx_local_2.pos
			_hx_local_2.pos = (_hx_local_3 + 1)
			_hx_local_3
		# /opt/haxe-git/std/haxe/Unserializer.hx:167
		if s:
			k = (k * -1)
		# /opt/haxe-git/std/haxe/Unserializer.hx:169
		return k

	def readFloat(self):
		# /opt/haxe-git/std/haxe/Unserializer.hx:173
		p1 = self.pos
		# /opt/haxe-git/std/haxe/Unserializer.hx:174
		while True:
			# /opt/haxe-git/std/haxe/Unserializer.hx:175
			c = None
			p = self.pos
			s = self.buf
			if (p >= len(s)):
				c = -1
			else:
				c = ord(s[p])
			# /opt/haxe-git/std/haxe/Unserializer.hx:177
			if ((((c >= 43) and ((c < 58))) or ((c == 101))) or ((c == 69))):
				# /opt/haxe-git/std/haxe/Unserializer.hx:178
				_hx_local_0 = self
				_hx_local_1 = _hx_local_0.pos
				_hx_local_0.pos = (_hx_local_1 + 1)
				_hx_local_1
			else:
				break
		# /opt/haxe-git/std/haxe/Unserializer.hx:182
		return Std.parseFloat(HxString.substr(self.buf,p1,(self.pos - p1)))

	def unserializeObject(self,o):
		# /opt/haxe-git/std/haxe/Unserializer.hx:186
		while True:
			# /opt/haxe-git/std/haxe/Unserializer.hx:187
			if (self.pos >= self.length):
				raise _HxException("Invalid object")
			# /opt/haxe-git/std/haxe/Unserializer.hx:189
			def _hx_local_0():
				# /opt/haxe-git/std/haxe/Unserializer.hx:189
				p = self.pos
				def _hx_local_2():
					def _hx_local_1():
						s = self.buf
						return (-1 if ((p >= len(s))) else ord(s[p]))
					return _hx_local_1()
				return _hx_local_2()
			if (_hx_local_0() == 103):
				break
			# /opt/haxe-git/std/haxe/Unserializer.hx:191
			k = self.unserialize()
			# /opt/haxe-git/std/haxe/Unserializer.hx:192
			if (not Std._hx_is(k,str)):
				raise _HxException("Invalid object key")
			# /opt/haxe-git/std/haxe/Unserializer.hx:194
			v = self.unserialize()
			# /opt/haxe-git/std/haxe/Unserializer.hx:195
			setattr(o,(("_hx_" + k) if (k in python_Boot.keywords) else (("_hx_" + k) if (((((len(k) > 2) and ((ord(k[0]) == 95))) and ((ord(k[1]) == 95))) and ((ord(k[(len(k) - 1)]) != 95)))) else k)),v)
		# /opt/haxe-git/std/haxe/Unserializer.hx:197
		# /opt/haxe-git/std/haxe/Unserializer.hx:197
		_hx_local_3 = self
		_hx_local_4 = _hx_local_3.pos
		_hx_local_3.pos = (_hx_local_4 + 1)
		_hx_local_4

	def unserializeEnum(self,edecl,tag):
		# /opt/haxe-git/std/haxe/Unserializer.hx:201
		def _hx_local_0():
			# /opt/haxe-git/std/haxe/Unserializer.hx:201
			p = self.pos
			self.pos = (self.pos + 1)
			def _hx_local_2():
				def _hx_local_1():
					s = self.buf
					return (-1 if ((p >= len(s))) else ord(s[p]))
				return _hx_local_1()
			return _hx_local_2()
		if (_hx_local_0() != 58):
			raise _HxException("Invalid enum format")
		# /opt/haxe-git/std/haxe/Unserializer.hx:203
		nargs = self.readDigits()
		# /opt/haxe-git/std/haxe/Unserializer.hx:204
		if (nargs == 0):
			return Type.createEnum(edecl,tag)
		# /opt/haxe-git/std/haxe/Unserializer.hx:206
		args = list()
		# /opt/haxe-git/std/haxe/Unserializer.hx:207
		def _hx_local_4():
			# /opt/haxe-git/std/haxe/Unserializer.hx:207
			nonlocal nargs
			_hx_local_3 = nargs
			nargs = (nargs - 1)
			return _hx_local_3
		while (_hx_local_4() > 0):
			# /opt/haxe-git/std/haxe/Unserializer.hx:208
			x = self.unserialize()
			args.append(x)
		# /opt/haxe-git/std/haxe/Unserializer.hx:209
		return Type.createEnum(edecl,tag,args)

	def unserialize(self):
		# /opt/haxe-git/std/haxe/Unserializer.hx:233
		# /opt/haxe-git/std/haxe/Unserializer.hx:233
		_g = None
		p = self.pos
		self.pos = (self.pos + 1)
		s = self.buf
		if (p >= len(s)):
			_g = -1
		else:
			_g = ord(s[p])
		# /opt/haxe-git/std/haxe/Unserializer.hx:235
		if (_g == 110):
			return None
		elif (_g == 116):
			return True
		elif (_g == 102):
			return False
		elif (_g == 122):
			return 0
		elif (_g == 105):
			return self.readDigits()
		elif (_g == 100):
			return self.readFloat()
		elif (_g == 121):
			# /opt/haxe-git/std/haxe/Unserializer.hx:247
			_hx_len = self.readDigits()
			# /opt/haxe-git/std/haxe/Unserializer.hx:248
			def _hx_local_0():
				# /opt/haxe-git/std/haxe/Unserializer.hx:248
				p1 = self.pos
				self.pos = (self.pos + 1)
				def _hx_local_2():
					def _hx_local_1():
						s1 = self.buf
						return (-1 if ((p1 >= len(s1))) else ord(s1[p1]))
					return _hx_local_1()
				return _hx_local_2()
			if ((_hx_local_0() != 58) or (((self.length - self.pos) < _hx_len))):
				raise _HxException("Invalid string length")
			# /opt/haxe-git/std/haxe/Unserializer.hx:250
			s2 = HxString.substr(self.buf,self.pos,_hx_len)
			# /opt/haxe-git/std/haxe/Unserializer.hx:251
			# /opt/haxe-git/std/haxe/Unserializer.hx:251
			_hx_local_3 = self
			_hx_local_4 = _hx_local_3.pos
			_hx_local_3.pos = (_hx_local_4 + _hx_len)
			_hx_local_3.pos
			# /opt/haxe-git/std/haxe/Unserializer.hx:252
			s2 = python_lib_urllib_Parse.unquote(s2)
			# /opt/haxe-git/std/haxe/Unserializer.hx:253
			# /opt/haxe-git/std/haxe/Unserializer.hx:253
			_this = self.scache
			_this.append(s2)
			# /opt/haxe-git/std/haxe/Unserializer.hx:254
			return s2
		elif (_g == 107):
			return Math.NaN
		elif (_g == 109):
			return Math.NEGATIVE_INFINITY
		elif (_g == 112):
			return Math.POSITIVE_INFINITY
		elif (_g == 97):
			# /opt/haxe-git/std/haxe/Unserializer.hx:262
			buf = self.buf
			# /opt/haxe-git/std/haxe/Unserializer.hx:263
			a = list()
			# /opt/haxe-git/std/haxe/Unserializer.hx:264
			# /opt/haxe-git/std/haxe/Unserializer.hx:264
			_this1 = self.cache
			_this1.append(a)
			# /opt/haxe-git/std/haxe/Unserializer.hx:265
			while True:
				# /opt/haxe-git/std/haxe/Unserializer.hx:266
				c = None
				p2 = self.pos
				s3 = self.buf
				if (p2 >= len(s3)):
					c = -1
				else:
					c = ord(s3[p2])
				# /opt/haxe-git/std/haxe/Unserializer.hx:267
				if (c == 104):
					# /opt/haxe-git/std/haxe/Unserializer.hx:268
					# /opt/haxe-git/std/haxe/Unserializer.hx:268
					_hx_local_5 = self
					_hx_local_6 = _hx_local_5.pos
					_hx_local_5.pos = (_hx_local_6 + 1)
					_hx_local_6
					# /opt/haxe-git/std/haxe/Unserializer.hx:269
					break
				# /opt/haxe-git/std/haxe/Unserializer.hx:271
				if (c == 117):
					# /opt/haxe-git/std/haxe/Unserializer.hx:272
					# /opt/haxe-git/std/haxe/Unserializer.hx:272
					_hx_local_7 = self
					_hx_local_8 = _hx_local_7.pos
					_hx_local_7.pos = (_hx_local_8 + 1)
					_hx_local_8
					# /opt/haxe-git/std/haxe/Unserializer.hx:273
					n = self.readDigits()
					# /opt/haxe-git/std/haxe/Unserializer.hx:274
					python_internal_ArrayImpl._set(a, ((len(a) + n) - 1), None)
				else:
					# /opt/haxe-git/std/haxe/Unserializer.hx:276
					x = self.unserialize()
					a.append(x)
			# /opt/haxe-git/std/haxe/Unserializer.hx:278
			return a
		elif (_g == 111):
			# /opt/haxe-git/std/haxe/Unserializer.hx:280
			o = _hx_AnonObject({})
			# /opt/haxe-git/std/haxe/Unserializer.hx:281
			# /opt/haxe-git/std/haxe/Unserializer.hx:281
			_this2 = self.cache
			_this2.append(o)
			# /opt/haxe-git/std/haxe/Unserializer.hx:282
			self.unserializeObject(o)
			# /opt/haxe-git/std/haxe/Unserializer.hx:283
			return o
		elif (_g == 114):
			# /opt/haxe-git/std/haxe/Unserializer.hx:285
			n1 = self.readDigits()
			# /opt/haxe-git/std/haxe/Unserializer.hx:286
			if ((n1 < 0) or ((n1 >= len(self.cache)))):
				raise _HxException("Invalid reference")
			# /opt/haxe-git/std/haxe/Unserializer.hx:288
			return (self.cache[n1] if n1 >= 0 and n1 < len(self.cache) else None)
		elif (_g == 82):
			# /opt/haxe-git/std/haxe/Unserializer.hx:290
			n2 = self.readDigits()
			# /opt/haxe-git/std/haxe/Unserializer.hx:291
			if ((n2 < 0) or ((n2 >= len(self.scache)))):
				raise _HxException("Invalid string reference")
			# /opt/haxe-git/std/haxe/Unserializer.hx:293
			return (self.scache[n2] if n2 >= 0 and n2 < len(self.scache) else None)
		elif (_g == 120):
			raise _HxException(self.unserialize())
		elif (_g == 99):
			# /opt/haxe-git/std/haxe/Unserializer.hx:297
			name = self.unserialize()
			# /opt/haxe-git/std/haxe/Unserializer.hx:298
			cl = self.resolver.resolveClass(name)
			# /opt/haxe-git/std/haxe/Unserializer.hx:299
			if (cl is None):
				raise _HxException(("Class not found " + ("null" if name is None else name)))
			# /opt/haxe-git/std/haxe/Unserializer.hx:301
			o1 = Type.createEmptyInstance(cl)
			# /opt/haxe-git/std/haxe/Unserializer.hx:302
			# /opt/haxe-git/std/haxe/Unserializer.hx:302
			_this3 = self.cache
			_this3.append(o1)
			# /opt/haxe-git/std/haxe/Unserializer.hx:303
			self.unserializeObject(o1)
			# /opt/haxe-git/std/haxe/Unserializer.hx:304
			return o1
		elif (_g == 119):
			# /opt/haxe-git/std/haxe/Unserializer.hx:306
			name1 = self.unserialize()
			# /opt/haxe-git/std/haxe/Unserializer.hx:307
			edecl = self.resolver.resolveEnum(name1)
			# /opt/haxe-git/std/haxe/Unserializer.hx:308
			if (edecl is None):
				raise _HxException(("Enum not found " + ("null" if name1 is None else name1)))
			# /opt/haxe-git/std/haxe/Unserializer.hx:310
			e = self.unserializeEnum(edecl,self.unserialize())
			# /opt/haxe-git/std/haxe/Unserializer.hx:311
			# /opt/haxe-git/std/haxe/Unserializer.hx:311
			_this4 = self.cache
			_this4.append(e)
			# /opt/haxe-git/std/haxe/Unserializer.hx:312
			return e
		elif (_g == 106):
			# /opt/haxe-git/std/haxe/Unserializer.hx:314
			name2 = self.unserialize()
			# /opt/haxe-git/std/haxe/Unserializer.hx:315
			edecl1 = self.resolver.resolveEnum(name2)
			# /opt/haxe-git/std/haxe/Unserializer.hx:316
			if (edecl1 is None):
				raise _HxException(("Enum not found " + ("null" if name2 is None else name2)))
			# /opt/haxe-git/std/haxe/Unserializer.hx:318
			# /opt/haxe-git/std/haxe/Unserializer.hx:318
			_hx_local_9 = self
			_hx_local_10 = _hx_local_9.pos
			_hx_local_9.pos = (_hx_local_10 + 1)
			_hx_local_10
			# /opt/haxe-git/std/haxe/Unserializer.hx:319
			index = self.readDigits()
			# /opt/haxe-git/std/haxe/Unserializer.hx:320
			tag = python_internal_ArrayImpl._get(Type.getEnumConstructs(edecl1), index)
			# /opt/haxe-git/std/haxe/Unserializer.hx:321
			if (tag is None):
				raise _HxException(((("Unknown enum index " + ("null" if name2 is None else name2)) + "@") + Std.string(index)))
			# /opt/haxe-git/std/haxe/Unserializer.hx:323
			e1 = self.unserializeEnum(edecl1,tag)
			# /opt/haxe-git/std/haxe/Unserializer.hx:324
			# /opt/haxe-git/std/haxe/Unserializer.hx:324
			_this5 = self.cache
			_this5.append(e1)
			# /opt/haxe-git/std/haxe/Unserializer.hx:325
			return e1
		elif (_g == 108):
			# /opt/haxe-git/std/haxe/Unserializer.hx:327
			l = List()
			# /opt/haxe-git/std/haxe/Unserializer.hx:328
			# /opt/haxe-git/std/haxe/Unserializer.hx:328
			_this6 = self.cache
			_this6.append(l)
			# /opt/haxe-git/std/haxe/Unserializer.hx:329
			buf1 = self.buf
			# /opt/haxe-git/std/haxe/Unserializer.hx:330
			def _hx_local_11():
				# /opt/haxe-git/std/haxe/Unserializer.hx:330
				p3 = self.pos
				def _hx_local_13():
					def _hx_local_12():
						s4 = self.buf
						return (-1 if ((p3 >= len(s4))) else ord(s4[p3]))
					return _hx_local_12()
				return _hx_local_13()
			while (_hx_local_11() != 104):
				l.add(self.unserialize())
			# /opt/haxe-git/std/haxe/Unserializer.hx:332
			# /opt/haxe-git/std/haxe/Unserializer.hx:332
			_hx_local_14 = self
			_hx_local_15 = _hx_local_14.pos
			_hx_local_14.pos = (_hx_local_15 + 1)
			_hx_local_15
			# /opt/haxe-git/std/haxe/Unserializer.hx:333
			return l
		elif (_g == 98):
			# /opt/haxe-git/std/haxe/Unserializer.hx:335
			h = haxe_ds_StringMap()
			# /opt/haxe-git/std/haxe/Unserializer.hx:336
			# /opt/haxe-git/std/haxe/Unserializer.hx:336
			_this7 = self.cache
			_this7.append(h)
			# /opt/haxe-git/std/haxe/Unserializer.hx:337
			buf2 = self.buf
			# /opt/haxe-git/std/haxe/Unserializer.hx:338
			def _hx_local_16():
				# /opt/haxe-git/std/haxe/Unserializer.hx:338
				p4 = self.pos
				def _hx_local_18():
					def _hx_local_17():
						s5 = self.buf
						return (-1 if ((p4 >= len(s5))) else ord(s5[p4]))
					return _hx_local_17()
				return _hx_local_18()
			while (_hx_local_16() != 104):
				# /opt/haxe-git/std/haxe/Unserializer.hx:339
				s6 = self.unserialize()
				# /opt/haxe-git/std/haxe/Unserializer.hx:340
				# /opt/haxe-git/std/haxe/Unserializer.hx:340
				value = self.unserialize()
				h.h[s6] = value
			# /opt/haxe-git/std/haxe/Unserializer.hx:342
			# /opt/haxe-git/std/haxe/Unserializer.hx:342
			_hx_local_19 = self
			_hx_local_20 = _hx_local_19.pos
			_hx_local_19.pos = (_hx_local_20 + 1)
			_hx_local_20
			# /opt/haxe-git/std/haxe/Unserializer.hx:343
			return h
		elif (_g == 113):
			# /opt/haxe-git/std/haxe/Unserializer.hx:345
			h1 = haxe_ds_IntMap()
			# /opt/haxe-git/std/haxe/Unserializer.hx:346
			# /opt/haxe-git/std/haxe/Unserializer.hx:346
			_this8 = self.cache
			_this8.append(h1)
			# /opt/haxe-git/std/haxe/Unserializer.hx:347
			buf3 = self.buf
			# /opt/haxe-git/std/haxe/Unserializer.hx:348
			c1 = None
			p5 = self.pos
			self.pos = (self.pos + 1)
			s7 = self.buf
			if (p5 >= len(s7)):
				c1 = -1
			else:
				c1 = ord(s7[p5])
			# /opt/haxe-git/std/haxe/Unserializer.hx:349
			while (c1 == 58):
				# /opt/haxe-git/std/haxe/Unserializer.hx:350
				i = self.readDigits()
				# /opt/haxe-git/std/haxe/Unserializer.hx:351
				h1.set(i,self.unserialize())
				# /opt/haxe-git/std/haxe/Unserializer.hx:352
				# /opt/haxe-git/std/haxe/Unserializer.hx:352
				p6 = self.pos
				self.pos = (self.pos + 1)
				s8 = self.buf
				if (p6 >= len(s8)):
					c1 = -1
				else:
					c1 = ord(s8[p6])
			# /opt/haxe-git/std/haxe/Unserializer.hx:354
			if (c1 != 104):
				raise _HxException("Invalid IntMap format")
			# /opt/haxe-git/std/haxe/Unserializer.hx:356
			return h1
		elif (_g == 77):
			# /opt/haxe-git/std/haxe/Unserializer.hx:358
			h2 = haxe_ds_ObjectMap()
			# /opt/haxe-git/std/haxe/Unserializer.hx:359
			# /opt/haxe-git/std/haxe/Unserializer.hx:359
			_this9 = self.cache
			_this9.append(h2)
			# /opt/haxe-git/std/haxe/Unserializer.hx:360
			buf4 = self.buf
			# /opt/haxe-git/std/haxe/Unserializer.hx:361
			def _hx_local_21():
				# /opt/haxe-git/std/haxe/Unserializer.hx:361
				p7 = self.pos
				def _hx_local_23():
					def _hx_local_22():
						s9 = self.buf
						return (-1 if ((p7 >= len(s9))) else ord(s9[p7]))
					return _hx_local_22()
				return _hx_local_23()
			while (_hx_local_21() != 104):
				# /opt/haxe-git/std/haxe/Unserializer.hx:362
				s10 = self.unserialize()
				# /opt/haxe-git/std/haxe/Unserializer.hx:363
				h2.set(s10,self.unserialize())
			# /opt/haxe-git/std/haxe/Unserializer.hx:365
			# /opt/haxe-git/std/haxe/Unserializer.hx:365
			_hx_local_24 = self
			_hx_local_25 = _hx_local_24.pos
			_hx_local_24.pos = (_hx_local_25 + 1)
			_hx_local_25
			# /opt/haxe-git/std/haxe/Unserializer.hx:366
			return h2
		elif (_g == 118):
			# /opt/haxe-git/std/haxe/Unserializer.hx:368
			d = None
			# /opt/haxe-git/std/haxe/Unserializer.hx:369
			def _hx_local_26():
				# /opt/haxe-git/std/haxe/Unserializer.hx:369
				p8 = self.pos
				def _hx_local_28():
					def _hx_local_27():
						s11 = self.buf
						return (-1 if ((p8 >= len(s11))) else ord(s11[p8]))
					return _hx_local_27()
				return _hx_local_28()
			def _hx_local_29():
				p9 = self.pos
				def _hx_local_31():
					def _hx_local_30():
						s12 = self.buf
						return (-1 if ((p9 >= len(s12))) else ord(s12[p9]))
					return _hx_local_30()
				return _hx_local_31()
			# /opt/haxe-git/std/haxe/Unserializer.hx:370
			def _hx_local_32():
				# /opt/haxe-git/std/haxe/Unserializer.hx:370
				p10 = (self.pos + 1)
				def _hx_local_34():
					def _hx_local_33():
						s13 = self.buf
						return (-1 if ((p10 >= len(s13))) else ord(s13[p10]))
					return _hx_local_33()
				return _hx_local_34()
			def _hx_local_35():
				p11 = (self.pos + 1)
				def _hx_local_37():
					def _hx_local_36():
						s14 = self.buf
						return (-1 if ((p11 >= len(s14))) else ord(s14[p11]))
					return _hx_local_36()
				return _hx_local_37()
			# /opt/haxe-git/std/haxe/Unserializer.hx:371
			def _hx_local_38():
				# /opt/haxe-git/std/haxe/Unserializer.hx:371
				p12 = (self.pos + 2)
				def _hx_local_40():
					def _hx_local_39():
						s15 = self.buf
						return (-1 if ((p12 >= len(s15))) else ord(s15[p12]))
					return _hx_local_39()
				return _hx_local_40()
			def _hx_local_41():
				p13 = (self.pos + 2)
				def _hx_local_43():
					def _hx_local_42():
						s16 = self.buf
						return (-1 if ((p13 >= len(s16))) else ord(s16[p13]))
					return _hx_local_42()
				return _hx_local_43()
			# /opt/haxe-git/std/haxe/Unserializer.hx:372
			def _hx_local_44():
				# /opt/haxe-git/std/haxe/Unserializer.hx:372
				p14 = (self.pos + 3)
				def _hx_local_46():
					def _hx_local_45():
						s17 = self.buf
						return (-1 if ((p14 >= len(s17))) else ord(s17[p14]))
					return _hx_local_45()
				return _hx_local_46()
			def _hx_local_47():
				p15 = (self.pos + 3)
				def _hx_local_49():
					def _hx_local_48():
						s18 = self.buf
						return (-1 if ((p15 >= len(s18))) else ord(s18[p15]))
					return _hx_local_48()
				return _hx_local_49()
			# /opt/haxe-git/std/haxe/Unserializer.hx:373
			def _hx_local_50():
				# /opt/haxe-git/std/haxe/Unserializer.hx:373
				p16 = (self.pos + 4)
				def _hx_local_52():
					def _hx_local_51():
						s19 = self.buf
						return (-1 if ((p16 >= len(s19))) else ord(s19[p16]))
					return _hx_local_51()
				return _hx_local_52()
			# /opt/haxe-git/std/haxe/Unserializer.hx:369
			if (((((((((_hx_local_26() >= 48) and ((_hx_local_29() <= 57))) and ((_hx_local_32() >= 48))) and ((_hx_local_35() <= 57))) and ((_hx_local_38() >= 48))) and ((_hx_local_41() <= 57))) and ((_hx_local_44() >= 48))) and ((_hx_local_47() <= 57))) and ((_hx_local_50() == 45))):
				# /opt/haxe-git/std/haxe/Unserializer.hx:376
				d = Date.fromString(HxString.substr(self.buf,self.pos,19))
				# /opt/haxe-git/std/haxe/Unserializer.hx:377
				# /opt/haxe-git/std/haxe/Unserializer.hx:377
				_hx_local_53 = self
				_hx_local_54 = _hx_local_53.pos
				_hx_local_53.pos = (_hx_local_54 + 19)
				_hx_local_53.pos
			else:
				d = Date.fromTime(self.readFloat())
			# /opt/haxe-git/std/haxe/Unserializer.hx:380
			# /opt/haxe-git/std/haxe/Unserializer.hx:380
			_this10 = self.cache
			_this10.append(d)
			# /opt/haxe-git/std/haxe/Unserializer.hx:381
			return d
		elif (_g == 115):
			# /opt/haxe-git/std/haxe/Unserializer.hx:383
			len1 = self.readDigits()
			# /opt/haxe-git/std/haxe/Unserializer.hx:384
			buf5 = self.buf
			# /opt/haxe-git/std/haxe/Unserializer.hx:385
			def _hx_local_55():
				# /opt/haxe-git/std/haxe/Unserializer.hx:385
				p17 = self.pos
				self.pos = (self.pos + 1)
				def _hx_local_57():
					def _hx_local_56():
						s20 = self.buf
						return (-1 if ((p17 >= len(s20))) else ord(s20[p17]))
					return _hx_local_56()
				return _hx_local_57()
			if ((_hx_local_55() != 58) or (((self.length - self.pos) < len1))):
				raise _HxException("Invalid bytes length")
			# /opt/haxe-git/std/haxe/Unserializer.hx:390
			codes = haxe_Unserializer.CODES
			# /opt/haxe-git/std/haxe/Unserializer.hx:391
			if (codes is None):
				# /opt/haxe-git/std/haxe/Unserializer.hx:392
				codes = haxe_Unserializer.initCodes()
				# /opt/haxe-git/std/haxe/Unserializer.hx:393
				haxe_Unserializer.CODES = codes
			# /opt/haxe-git/std/haxe/Unserializer.hx:395
			i1 = self.pos
			# /opt/haxe-git/std/haxe/Unserializer.hx:396
			rest = (len1 & 3)
			# /opt/haxe-git/std/haxe/Unserializer.hx:397
			size = None
			size = ((((len1 >> 2)) * 3) + (((rest - 1) if ((rest >= 2)) else 0)))
			# /opt/haxe-git/std/haxe/Unserializer.hx:398
			_hx_max = (i1 + ((len1 - rest)))
			# /opt/haxe-git/std/haxe/Unserializer.hx:399
			_hx_bytes = haxe_io_Bytes.alloc(size)
			# /opt/haxe-git/std/haxe/Unserializer.hx:400
			bpos = 0
			# /opt/haxe-git/std/haxe/Unserializer.hx:401
			while (i1 < _hx_max):
				# /opt/haxe-git/std/haxe/Unserializer.hx:402
				def _hx_local_58():
					# /opt/haxe-git/std/haxe/Unserializer.hx:402
					nonlocal i1
					index1 = i1
					i1 = (i1 + 1)
					return (-1 if ((index1 >= len(buf5))) else ord(buf5[index1]))
				c11 = python_internal_ArrayImpl._get(codes, _hx_local_58())
				# /opt/haxe-git/std/haxe/Unserializer.hx:403
				def _hx_local_59():
					# /opt/haxe-git/std/haxe/Unserializer.hx:403
					nonlocal i1
					index2 = i1
					i1 = (i1 + 1)
					return (-1 if ((index2 >= len(buf5))) else ord(buf5[index2]))
				c2 = python_internal_ArrayImpl._get(codes, _hx_local_59())
				# /opt/haxe-git/std/haxe/Unserializer.hx:404
				# /opt/haxe-git/std/haxe/Unserializer.hx:404
				pos = bpos
				bpos = (bpos + 1)
				_hx_bytes.b[pos] = ((((c11 << 2) | ((c2 >> 4)))) & 255)
				# /opt/haxe-git/std/haxe/Unserializer.hx:405
				def _hx_local_60():
					# /opt/haxe-git/std/haxe/Unserializer.hx:405
					nonlocal i1
					index3 = i1
					i1 = (i1 + 1)
					return (-1 if ((index3 >= len(buf5))) else ord(buf5[index3]))
				c3 = python_internal_ArrayImpl._get(codes, _hx_local_60())
				# /opt/haxe-git/std/haxe/Unserializer.hx:406
				# /opt/haxe-git/std/haxe/Unserializer.hx:406
				pos1 = bpos
				bpos = (bpos + 1)
				_hx_bytes.b[pos1] = ((((c2 << 4) | ((c3 >> 2)))) & 255)
				# /opt/haxe-git/std/haxe/Unserializer.hx:407
				def _hx_local_61():
					# /opt/haxe-git/std/haxe/Unserializer.hx:407
					nonlocal i1
					index4 = i1
					i1 = (i1 + 1)
					return (-1 if ((index4 >= len(buf5))) else ord(buf5[index4]))
				c4 = python_internal_ArrayImpl._get(codes, _hx_local_61())
				# /opt/haxe-git/std/haxe/Unserializer.hx:408
				# /opt/haxe-git/std/haxe/Unserializer.hx:408
				pos2 = bpos
				bpos = (bpos + 1)
				_hx_bytes.b[pos2] = ((((c3 << 6) | c4)) & 255)
			# /opt/haxe-git/std/haxe/Unserializer.hx:410
			if (rest >= 2):
				# /opt/haxe-git/std/haxe/Unserializer.hx:411
				def _hx_local_62():
					# /opt/haxe-git/std/haxe/Unserializer.hx:411
					nonlocal i1
					index5 = i1
					i1 = (i1 + 1)
					return (-1 if ((index5 >= len(buf5))) else ord(buf5[index5]))
				c12 = python_internal_ArrayImpl._get(codes, _hx_local_62())
				# /opt/haxe-git/std/haxe/Unserializer.hx:412
				def _hx_local_63():
					# /opt/haxe-git/std/haxe/Unserializer.hx:412
					nonlocal i1
					index6 = i1
					i1 = (i1 + 1)
					return (-1 if ((index6 >= len(buf5))) else ord(buf5[index6]))
				c21 = python_internal_ArrayImpl._get(codes, _hx_local_63())
				# /opt/haxe-git/std/haxe/Unserializer.hx:413
				# /opt/haxe-git/std/haxe/Unserializer.hx:413
				pos3 = bpos
				bpos = (bpos + 1)
				_hx_bytes.b[pos3] = ((((c12 << 2) | ((c21 >> 4)))) & 255)
				# /opt/haxe-git/std/haxe/Unserializer.hx:414
				if (rest == 3):
					# /opt/haxe-git/std/haxe/Unserializer.hx:415
					def _hx_local_64():
						# /opt/haxe-git/std/haxe/Unserializer.hx:415
						nonlocal i1
						index7 = i1
						i1 = (i1 + 1)
						return (-1 if ((index7 >= len(buf5))) else ord(buf5[index7]))
					c31 = python_internal_ArrayImpl._get(codes, _hx_local_64())
					# /opt/haxe-git/std/haxe/Unserializer.hx:416
					# /opt/haxe-git/std/haxe/Unserializer.hx:416
					pos4 = bpos
					bpos = (bpos + 1)
					_hx_bytes.b[pos4] = ((((c21 << 4) | ((c31 >> 2)))) & 255)
			# /opt/haxe-git/std/haxe/Unserializer.hx:420
			# /opt/haxe-git/std/haxe/Unserializer.hx:420
			_hx_local_65 = self
			_hx_local_66 = _hx_local_65.pos
			_hx_local_65.pos = (_hx_local_66 + len1)
			_hx_local_65.pos
			# /opt/haxe-git/std/haxe/Unserializer.hx:421
			# /opt/haxe-git/std/haxe/Unserializer.hx:421
			_this11 = self.cache
			_this11.append(_hx_bytes)
			# /opt/haxe-git/std/haxe/Unserializer.hx:422
			return _hx_bytes
		elif (_g == 67):
			# /opt/haxe-git/std/haxe/Unserializer.hx:424
			name3 = self.unserialize()
			# /opt/haxe-git/std/haxe/Unserializer.hx:425
			cl1 = self.resolver.resolveClass(name3)
			# /opt/haxe-git/std/haxe/Unserializer.hx:426
			if (cl1 is None):
				raise _HxException(("Class not found " + ("null" if name3 is None else name3)))
			# /opt/haxe-git/std/haxe/Unserializer.hx:428
			o2 = Type.createEmptyInstance(cl1)
			# /opt/haxe-git/std/haxe/Unserializer.hx:429
			# /opt/haxe-git/std/haxe/Unserializer.hx:429
			_this12 = self.cache
			x1 = o2
			_this12.append(x1)
			# /opt/haxe-git/std/haxe/Unserializer.hx:430
			Reflect.field(o2,"hxUnserialize")(self)
			# /opt/haxe-git/std/haxe/Unserializer.hx:431
			def _hx_local_67():
				# /opt/haxe-git/std/haxe/Unserializer.hx:431
				p18 = self.pos
				self.pos = (self.pos + 1)
				def _hx_local_69():
					def _hx_local_68():
						s21 = self.buf
						return (-1 if ((p18 >= len(s21))) else ord(s21[p18]))
					return _hx_local_68()
				return _hx_local_69()
			if (_hx_local_67() != 103):
				raise _HxException("Invalid custom data")
			# /opt/haxe-git/std/haxe/Unserializer.hx:433
			return o2
		elif (_g == 65):
			# /opt/haxe-git/std/haxe/Unserializer.hx:435
			name4 = self.unserialize()
			# /opt/haxe-git/std/haxe/Unserializer.hx:436
			cl2 = self.resolver.resolveClass(name4)
			# /opt/haxe-git/std/haxe/Unserializer.hx:437
			if (cl2 is None):
				raise _HxException(("Class not found " + ("null" if name4 is None else name4)))
			# /opt/haxe-git/std/haxe/Unserializer.hx:439
			return cl2
		elif (_g == 66):
			# /opt/haxe-git/std/haxe/Unserializer.hx:441
			name5 = self.unserialize()
			# /opt/haxe-git/std/haxe/Unserializer.hx:442
			e2 = self.resolver.resolveEnum(name5)
			# /opt/haxe-git/std/haxe/Unserializer.hx:443
			if (e2 is None):
				raise _HxException(("Enum not found " + ("null" if name5 is None else name5)))
			# /opt/haxe-git/std/haxe/Unserializer.hx:445
			return e2
		else:
			pass
		# /opt/haxe-git/std/haxe/Unserializer.hx:448
		# /opt/haxe-git/std/haxe/Unserializer.hx:448
		_hx_local_70 = self
		_hx_local_71 = _hx_local_70.pos
		_hx_local_70.pos = (_hx_local_71 - 1)
		_hx_local_71
		# /opt/haxe-git/std/haxe/Unserializer.hx:449
		def _hx_local_72():
			# /opt/haxe-git/std/haxe/Unserializer.hx:449
			_this13 = self.buf
			index8 = self.pos
			return ("" if (((index8 < 0) or ((index8 >= len(_this13))))) else _this13[index8])
		raise _HxException(((("Invalid char " + HxOverrides.stringOrNull(_hx_local_72())) + " at position ") + Std.string(self.pos)))

	@staticmethod
	def initCodes():
		# /opt/haxe-git/std/haxe/Unserializer.hx:72
		codes = list()
		# /opt/haxe-git/std/haxe/Unserializer.hx:74
		# /opt/haxe-git/std/haxe/Unserializer.hx:74
		_g1 = 0
		_g = len(haxe_Unserializer.BASE64)
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			# /opt/haxe-git/std/haxe/Unserializer.hx:75
			def _hx_local_0():
				# /opt/haxe-git/std/haxe/Unserializer.hx:75
				s = haxe_Unserializer.BASE64
				return (-1 if ((i >= len(s))) else ord(s[i]))
			python_internal_ArrayImpl._set(codes, _hx_local_0(), i)
		# /opt/haxe-git/std/haxe/Unserializer.hx:76
		return codes

	@staticmethod
	def run(v):
		# /opt/haxe-git/std/haxe/Unserializer.hx:460
		return haxe_Unserializer(v).unserialize()

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.buf = None
		_hx_o.pos = None
		_hx_o.length = None
		_hx_o.cache = None
		_hx_o.scache = None
		_hx_o.resolver = None
haxe_Unserializer._hx_class = haxe_Unserializer
_hx_classes["haxe.Unserializer"] = haxe_Unserializer


class haxe_ds_BalancedTree:
	_hx_class_name = "haxe.ds.BalancedTree"
	_hx_fields = ["root"]
	_hx_methods = ["set", "get", "remove", "exists", "iterator", "keys", "setLoop", "removeLoop", "iteratorLoop", "keysLoop", "merge", "minBinding", "removeMinBinding", "balance", "compare", "toString"]

	def __init__(self):
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:36
		self.root = None

	def set(self,key,value):
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:51
		self.root = self.setLoop(key,value,self.root)

	def get(self,key):
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:62
		node = self.root
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:63
		while (node is not None):
			# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:64
			c = self.compare(key,node.key)
			# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:65
			if (c == 0):
				return node.value
			# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:66
			if (c < 0):
				node = node.left
			else:
				node = node.right
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:69
		return None

	def remove(self,key):
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:83
		try:
			# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:84
			self.root = self.removeLoop(key,self.root)
			# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:85
			return True
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			if isinstance(_hx_e1, str):
				e = _hx_e1
				return False
			else:
				raise _hx_e

	def exists(self,key):
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:100
		node = self.root
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:101
		while (node is not None):
			# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:102
			c = self.compare(key,node.key)
			# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:103
			if (c == 0):
				return True
			elif (c < 0):
				node = node.left
			else:
				node = node.right
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:107
		return False

	def iterator(self):
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:116
		ret = []
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:117
		self.iteratorLoop(self.root,ret)
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:118
		return python_HaxeIterator(ret.__iter__())

	def keys(self):
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:127
		ret = []
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:128
		self.keysLoop(self.root,ret)
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:129
		return python_HaxeIterator(ret.__iter__())

	def setLoop(self,k,v,node):
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:133
		if (node is None):
			return haxe_ds_TreeNode(None, k, v, None)
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:134
		c = self.compare(k,node.key)
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:135
		if (c == 0):
			return haxe_ds_TreeNode(node.left, k, v, node.right, (0 if ((node is None)) else node._height))
		elif (c < 0):
			# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:137
			nl = self.setLoop(k,v,node.left)
			# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:135
			return self.balance(nl,node.key,node.value,node.right)
		else:
			# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:140
			nr = self.setLoop(k,v,node.right)
			# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:135
			return self.balance(node.left,node.key,node.value,nr)

	def removeLoop(self,k,node):
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:146
		if (node is None):
			raise _HxException("Not_found")
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:147
		c = self.compare(k,node.key)
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:148
		if (c == 0):
			return self.merge(node.left,node.right)
		elif (c < 0):
			return self.balance(self.removeLoop(k,node.left),node.key,node.value,node.right)
		else:
			return self.balance(node.left,node.key,node.value,self.removeLoop(k,node.right))

	def iteratorLoop(self,node,acc):
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:154
		if (node is not None):
			# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:155
			self.iteratorLoop(node.left,acc)
			# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:156
			# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:156
			acc.append(node.value)
			# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:157
			self.iteratorLoop(node.right,acc)

	def keysLoop(self,node,acc):
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:162
		if (node is not None):
			# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:163
			self.keysLoop(node.left,acc)
			# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:164
			# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:164
			acc.append(node.key)
			# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:165
			self.keysLoop(node.right,acc)

	def merge(self,t1,t2):
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:170
		if (t1 is None):
			return t2
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:171
		if (t2 is None):
			return t1
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:172
		t = self.minBinding(t2)
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:173
		return self.balance(t1,t.key,t.value,self.removeMinBinding(t2))

	def minBinding(self,t):
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:177
		if (t is None):
			raise _HxException("Not_found")
		elif (t.left is None):
			return t
		else:
			return self.minBinding(t.left)

	def removeMinBinding(self,t):
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:183
		if (t.left is None):
			return t.right
		else:
			return self.balance(self.removeMinBinding(t.left),t.key,t.value,t.right)

	def balance(self,l,k,v,r):
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:188
		hl = None
		if (l is None):
			hl = 0
		else:
			hl = l._height
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:189
		hr = None
		if (r is None):
			hr = 0
		else:
			hr = r._height
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:190
		if (hl > ((hr + 2))):
			# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:191
			def _hx_local_0():
				# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:191
				_this = l.left
				return (0 if ((_this is None)) else _this._height)
			def _hx_local_1():
				_this1 = l.right
				return (0 if ((_this1 is None)) else _this1._height)
			if (_hx_local_0() >= _hx_local_1()):
				return haxe_ds_TreeNode(l.left, l.key, l.value, haxe_ds_TreeNode(l.right, k, v, r))
			else:
				return haxe_ds_TreeNode(haxe_ds_TreeNode(l.left, l.key, l.value, l.right.left), l.right.key, l.right.value, haxe_ds_TreeNode(l.right.right, k, v, r))
		elif (hr > ((hl + 2))):
			# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:194
			def _hx_local_2():
				# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:194
				_this2 = r.right
				return (0 if ((_this2 is None)) else _this2._height)
			def _hx_local_3():
				_this3 = r.left
				return (0 if ((_this3 is None)) else _this3._height)
			if (_hx_local_2() > _hx_local_3()):
				return haxe_ds_TreeNode(haxe_ds_TreeNode(l, k, v, r.left), r.key, r.value, r.right)
			else:
				return haxe_ds_TreeNode(haxe_ds_TreeNode(l, k, v, r.left.left), r.left.key, r.left.value, haxe_ds_TreeNode(r.left.right, r.key, r.value, r.right))
		else:
			return haxe_ds_TreeNode(l, k, v, r, (((hl if ((hl > hr)) else hr)) + 1))

	def compare(self,k1,k2):
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:202
		return Reflect.compare(k1,k2)

	def toString(self):
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:206
		if (self.root is None):
			return "{}"
		else:
			return (("{" + HxOverrides.stringOrNull(self.root.toString())) + "}")

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.root = None
haxe_ds_BalancedTree._hx_class = haxe_ds_BalancedTree
_hx_classes["haxe.ds.BalancedTree"] = haxe_ds_BalancedTree


class haxe_ds_TreeNode:
	_hx_class_name = "haxe.ds.TreeNode"
	_hx_fields = ["left", "right", "key", "value", "_height"]
	_hx_methods = ["toString"]

	def __init__(self,l,k,v,r,h = -1):
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:220
		if (h is None):
			h = -1
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:211
		self.left = None
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:212
		self.right = None
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:213
		self.key = None
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:214
		self.value = None
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:218
		self._height = None
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:221
		self.left = l
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:222
		self.key = k
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:223
		self.value = v
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:224
		self.right = r
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:225
		if (h == -1):
			# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:226
			def _hx_local_4():
				# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:226
				def _hx_local_0():
					# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:226
					_this = self.left
					return (0 if ((_this is None)) else _this._height)
				def _hx_local_1():
					_this1 = self.right
					return (0 if ((_this1 is None)) else _this1._height)
				def _hx_local_2():
					_this2 = self.left
					return (0 if ((_this2 is None)) else _this2._height)
				def _hx_local_3():
					_this3 = self.right
					return (0 if ((_this3 is None)) else _this3._height)
				return _hx_local_2() if (_hx_local_0() > _hx_local_1()) else _hx_local_3()
			self._height = ((_hx_local_4()) + 1)
		else:
			self._height = h

	def toString(self):
		# /opt/haxe-git/std/haxe/ds/BalancedTree.hx:234
		return ((HxOverrides.stringOrNull((("" if ((self.left is None)) else (HxOverrides.stringOrNull(self.left.toString()) + ", ")))) + (((("" + Std.string(self.key)) + "=") + Std.string(self.value)))) + HxOverrides.stringOrNull((("" if ((self.right is None)) else (", " + HxOverrides.stringOrNull(self.right.toString()))))))

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.left = None
		_hx_o.right = None
		_hx_o.key = None
		_hx_o.value = None
		_hx_o._height = None
haxe_ds_TreeNode._hx_class = haxe_ds_TreeNode
_hx_classes["haxe.ds.TreeNode"] = haxe_ds_TreeNode


class haxe_ds_EnumValueMap(haxe_ds_BalancedTree):
	_hx_class_name = "haxe.ds.EnumValueMap"
	_hx_fields = []
	_hx_methods = ["compare", "compareArgs", "compareArg"]
	_hx_statics = []
	_hx_interfaces = [haxe_IMap]
	_hx_super = haxe_ds_BalancedTree


	def __init__(self):
		# /opt/haxe-git/std/haxe/ds/EnumValueMap.hx:31
		super().__init__()

	def compare(self,k1,k2):
		# /opt/haxe-git/std/haxe/ds/EnumValueMap.hx:34
		d = (k1.index - k2.index)
		# /opt/haxe-git/std/haxe/ds/EnumValueMap.hx:35
		if (d != 0):
			return d
		# /opt/haxe-git/std/haxe/ds/EnumValueMap.hx:36
		p1 = k1.params
		# /opt/haxe-git/std/haxe/ds/EnumValueMap.hx:37
		p2 = k2.params
		# /opt/haxe-git/std/haxe/ds/EnumValueMap.hx:38
		if ((len(p1) == 0) and ((len(p2) == 0))):
			return 0
		# /opt/haxe-git/std/haxe/ds/EnumValueMap.hx:39
		return self.compareArgs(p1,p2)

	def compareArgs(self,a1,a2):
		# /opt/haxe-git/std/haxe/ds/EnumValueMap.hx:43
		ld = (len(a1) - len(a2))
		# /opt/haxe-git/std/haxe/ds/EnumValueMap.hx:44
		if (ld != 0):
			return ld
		# /opt/haxe-git/std/haxe/ds/EnumValueMap.hx:45
		# /opt/haxe-git/std/haxe/ds/EnumValueMap.hx:45
		_g1 = 0
		_g = len(a1)
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			# /opt/haxe-git/std/haxe/ds/EnumValueMap.hx:46
			d = self.compareArg((a1[i] if i >= 0 and i < len(a1) else None),(a2[i] if i >= 0 and i < len(a2) else None))
			# /opt/haxe-git/std/haxe/ds/EnumValueMap.hx:47
			if (d != 0):
				return d
		# /opt/haxe-git/std/haxe/ds/EnumValueMap.hx:49
		return 0

	def compareArg(self,v1,v2):
		# /opt/haxe-git/std/haxe/ds/EnumValueMap.hx:53
		if (Reflect.isEnumValue(v1) and Reflect.isEnumValue(v2)):
			return self.compare(v1,v2)
		elif (Std._hx_is(v1,list) and Std._hx_is(v2,list)):
			return self.compareArgs(v1,v2)
		else:
			return Reflect.compare(v1,v2)

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
haxe_ds_EnumValueMap._hx_class = haxe_ds_EnumValueMap
_hx_classes["haxe.ds.EnumValueMap"] = haxe_ds_EnumValueMap


class haxe_ds__HashMap_HashMap_Impl_:
	_hx_class_name = "haxe.ds._HashMap.HashMap_Impl_"
	_hx_statics = ["_new", "set", "get", "exists", "remove", "keys", "iterator"]

	@staticmethod
	def _new():
		# /opt/haxe-git/std/haxe/ds/HashMap.hx:26
		return haxe_ds__HashMap_HashMapData()

	@staticmethod
	def set(this1,k,v):
		# /opt/haxe-git/std/haxe/ds/HashMap.hx:29
		this1.keys.set(k.hashCode(),k)
		# /opt/haxe-git/std/haxe/ds/HashMap.hx:30
		this1.values.set(k.hashCode(),v)

	@staticmethod
	def get(this1,k):
		# /opt/haxe-git/std/haxe/ds/HashMap.hx:33
		key = k.hashCode()
		return this1.values.h.get(key,None)

	@staticmethod
	def exists(this1,k):
		# /opt/haxe-git/std/haxe/ds/HashMap.hx:36
		key = k.hashCode()
		return key in this1.values.h

	@staticmethod
	def remove(this1,k):
		# /opt/haxe-git/std/haxe/ds/HashMap.hx:39
		this1.values.remove(k.hashCode())
		# /opt/haxe-git/std/haxe/ds/HashMap.hx:40
		return this1.keys.remove(k.hashCode())

	@staticmethod
	def keys(this1):
		# /opt/haxe-git/std/haxe/ds/HashMap.hx:43
		return this1.keys.iterator()

	@staticmethod
	def iterator(this1):
		# /opt/haxe-git/std/haxe/ds/HashMap.hx:46
		return this1.values.iterator()
haxe_ds__HashMap_HashMap_Impl_._hx_class = haxe_ds__HashMap_HashMap_Impl_
_hx_classes["haxe.ds._HashMap.HashMap_Impl_"] = haxe_ds__HashMap_HashMap_Impl_


class haxe_ds__HashMap_HashMapData:
	_hx_class_name = "haxe.ds._HashMap.HashMapData"
	_hx_fields = ["keys", "values"]

	def __init__(self):
		# /opt/haxe-git/std/haxe/ds/HashMap.hx:51
		self.keys = None
		# /opt/haxe-git/std/haxe/ds/HashMap.hx:52
		self.values = None
		# /opt/haxe-git/std/haxe/ds/HashMap.hx:54
		self.keys = haxe_ds_IntMap()
		# /opt/haxe-git/std/haxe/ds/HashMap.hx:55
		self.values = haxe_ds_IntMap()

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.keys = None
		_hx_o.values = None
haxe_ds__HashMap_HashMapData._hx_class = haxe_ds__HashMap_HashMapData
_hx_classes["haxe.ds._HashMap.HashMapData"] = haxe_ds__HashMap_HashMapData


class haxe_ds_IntMap:
	_hx_class_name = "haxe.ds.IntMap"
	_hx_fields = ["h"]
	_hx_methods = ["set", "get", "exists", "remove", "keys", "iterator", "toString"]
	_hx_interfaces = [haxe_IMap]

	def __init__(self):
		# /opt/haxe-git/std/python/_std/haxe/ds/IntMap.hx:28
		self.h = None
		# /opt/haxe-git/std/python/_std/haxe/ds/IntMap.hx:31
		self.h = dict()

	def set(self,key,value):
		# /opt/haxe-git/std/python/_std/haxe/ds/IntMap.hx:35
		self.h[key] = value

	def get(self,key):
		# /opt/haxe-git/std/python/_std/haxe/ds/IntMap.hx:39
		return self.h.get(key,None)

	def exists(self,key):
		# /opt/haxe-git/std/python/_std/haxe/ds/IntMap.hx:43
		return key in self.h

	def remove(self,key):
		# /opt/haxe-git/std/python/_std/haxe/ds/IntMap.hx:48
		if (not key in self.h):
			return False
		# /opt/haxe-git/std/python/_std/haxe/ds/IntMap.hx:49
		del self.h[key]
		# /opt/haxe-git/std/python/_std/haxe/ds/IntMap.hx:50
		return True

	def keys(self):
		# /opt/haxe-git/std/python/_std/haxe/ds/IntMap.hx:54
		# /opt/haxe-git/std/python/_std/haxe/ds/IntMap.hx:54
		this1 = None
		_this = self.h.keys()
		this1 = iter(_this)
		return python_HaxeIterator(this1)

	def iterator(self):
		# /opt/haxe-git/std/python/_std/haxe/ds/IntMap.hx:58
		# /opt/haxe-git/std/python/_std/haxe/ds/IntMap.hx:58
		this1 = None
		_this = self.h.values()
		this1 = iter(_this)
		return python_HaxeIterator(this1)

	def toString(self):
		# /opt/haxe-git/std/python/_std/haxe/ds/IntMap.hx:62
		s_b = python_lib_io_StringIO()
		# /opt/haxe-git/std/python/_std/haxe/ds/IntMap.hx:63
		s_b.write("{")
		# /opt/haxe-git/std/python/_std/haxe/ds/IntMap.hx:64
		it = self.keys()
		# /opt/haxe-git/std/python/_std/haxe/ds/IntMap.hx:65
		_hx_local_0 = it
		while _hx_local_0.hasNext():
			i = _hx_local_0.next()
			# /opt/haxe-git/std/python/_std/haxe/ds/IntMap.hx:66
			s_b.write(Std.string(i))
			# /opt/haxe-git/std/python/_std/haxe/ds/IntMap.hx:67
			s_b.write(" => ")
			# /opt/haxe-git/std/python/_std/haxe/ds/IntMap.hx:68
			# /opt/haxe-git/std/python/_std/haxe/ds/IntMap.hx:68
			x = Std.string(self.h.get(i,None))
			s_b.write(Std.string(x))
			# /opt/haxe-git/std/python/_std/haxe/ds/IntMap.hx:69
			if it.hasNext():
				s_b.write(", ")
		# /opt/haxe-git/std/python/_std/haxe/ds/IntMap.hx:72
		s_b.write("}")
		# /opt/haxe-git/std/python/_std/haxe/ds/IntMap.hx:73
		return s_b.getvalue()

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.h = None
haxe_ds_IntMap._hx_class = haxe_ds_IntMap
_hx_classes["haxe.ds.IntMap"] = haxe_ds_IntMap


class haxe_ds_ObjectMap:
	_hx_class_name = "haxe.ds.ObjectMap"
	_hx_fields = ["h"]
	_hx_methods = ["set", "get", "exists", "remove", "keys", "iterator", "toString"]
	_hx_interfaces = [haxe_IMap]

	def __init__(self):
		# /opt/haxe-git/std/python/_std/haxe/ds/ObjectMap.hx:28
		self.h = None
		# /opt/haxe-git/std/python/_std/haxe/ds/ObjectMap.hx:32
		self.h = dict()

	def set(self,key,value):
		# /opt/haxe-git/std/python/_std/haxe/ds/ObjectMap.hx:36
		self.h[key] = value

	def get(self,key):
		# /opt/haxe-git/std/python/_std/haxe/ds/ObjectMap.hx:40
		return self.h.get(key,None)

	def exists(self,key):
		# /opt/haxe-git/std/python/_std/haxe/ds/ObjectMap.hx:44
		return key in self.h

	def remove(self,key):
		# /opt/haxe-git/std/python/_std/haxe/ds/ObjectMap.hx:49
		r = key in self.h
		# /opt/haxe-git/std/python/_std/haxe/ds/ObjectMap.hx:50
		if r:
			del self.h[key]
		# /opt/haxe-git/std/python/_std/haxe/ds/ObjectMap.hx:51
		return r

	def keys(self):
		# /opt/haxe-git/std/python/_std/haxe/ds/ObjectMap.hx:55
		# /opt/haxe-git/std/python/_std/haxe/ds/ObjectMap.hx:55
		this1 = None
		_this = self.h.keys()
		this1 = iter(_this)
		return python_HaxeIterator(this1)

	def iterator(self):
		# /opt/haxe-git/std/python/_std/haxe/ds/ObjectMap.hx:59
		# /opt/haxe-git/std/python/_std/haxe/ds/ObjectMap.hx:59
		this1 = None
		_this = self.h.values()
		this1 = iter(_this)
		return python_HaxeIterator(this1)

	def toString(self):
		# /opt/haxe-git/std/python/_std/haxe/ds/ObjectMap.hx:63
		s_b = python_lib_io_StringIO()
		# /opt/haxe-git/std/python/_std/haxe/ds/ObjectMap.hx:64
		s_b.write("{")
		# /opt/haxe-git/std/python/_std/haxe/ds/ObjectMap.hx:65
		it = self.keys()
		# /opt/haxe-git/std/python/_std/haxe/ds/ObjectMap.hx:66
		_hx_local_0 = it
		while _hx_local_0.hasNext():
			i = _hx_local_0.next()
			# /opt/haxe-git/std/python/_std/haxe/ds/ObjectMap.hx:67
			s_b.write(Std.string(Std.string(i)))
			# /opt/haxe-git/std/python/_std/haxe/ds/ObjectMap.hx:68
			s_b.write(" => ")
			# /opt/haxe-git/std/python/_std/haxe/ds/ObjectMap.hx:69
			# /opt/haxe-git/std/python/_std/haxe/ds/ObjectMap.hx:69
			x = Std.string(self.h.get(i,None))
			s_b.write(Std.string(x))
			# /opt/haxe-git/std/python/_std/haxe/ds/ObjectMap.hx:70
			if it.hasNext():
				s_b.write(", ")
		# /opt/haxe-git/std/python/_std/haxe/ds/ObjectMap.hx:73
		s_b.write("}")
		# /opt/haxe-git/std/python/_std/haxe/ds/ObjectMap.hx:74
		return s_b.getvalue()

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.h = None
haxe_ds_ObjectMap._hx_class = haxe_ds_ObjectMap
_hx_classes["haxe.ds.ObjectMap"] = haxe_ds_ObjectMap

class haxe_ds_Option(Enum):
	_hx_class_name = "haxe.ds.Option"
	_hx_constructs = ["Some", "None"]

	@staticmethod
	def Some(v):
		return haxe_ds_Option("Some", 0, [v])
haxe_ds_Option._hx_None = haxe_ds_Option("None", 1, list())
haxe_ds_Option._hx_class = haxe_ds_Option
_hx_classes["haxe.ds.Option"] = haxe_ds_Option


class haxe_ds_WeakMap:
	_hx_class_name = "haxe.ds.WeakMap"
	_hx_methods = ["set", "get", "exists", "remove", "keys", "iterator", "toString"]
	_hx_interfaces = [haxe_IMap]

	def __init__(self):
		# /opt/haxe-git/std/haxe/ds/WeakMap.hx:38
		raise _HxException("Not implemented for this platform")

	def set(self,key,value):
		pass

	def get(self,key):
		# /opt/haxe-git/std/haxe/ds/WeakMap.hx:51
		return None

	def exists(self,key):
		# /opt/haxe-git/std/haxe/ds/WeakMap.hx:58
		return False

	def remove(self,key):
		# /opt/haxe-git/std/haxe/ds/WeakMap.hx:65
		return False

	def keys(self):
		# /opt/haxe-git/std/haxe/ds/WeakMap.hx:72
		return None

	def iterator(self):
		# /opt/haxe-git/std/haxe/ds/WeakMap.hx:79
		return None

	def toString(self):
		# /opt/haxe-git/std/haxe/ds/WeakMap.hx:86
		return None

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
haxe_ds_WeakMap._hx_class = haxe_ds_WeakMap
_hx_classes["haxe.ds.WeakMap"] = haxe_ds_WeakMap


class haxe_io_Bytes:
	_hx_class_name = "haxe.io.Bytes"
	_hx_fields = ["length", "b"]
	_hx_methods = ["get", "set", "blit", "fill", "sub", "compare", "getDouble", "getFloat", "setDouble", "setFloat", "getUInt16", "setUInt16", "getInt32", "getInt64", "setInt32", "setInt64", "getString", "readString", "toString", "toHex", "getData"]
	_hx_statics = ["alloc", "ofString", "ofData", "fastGet"]

	def __init__(self,length,b):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:30
		self.length = None
		# /opt/haxe-git/std/haxe/io/Bytes.hx:31
		self.b = None
		# /opt/haxe-git/std/haxe/io/Bytes.hx:34
		self.length = length
		# /opt/haxe-git/std/haxe/io/Bytes.hx:35
		self.b = b

	def get(self,pos):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:53
		return self.b[pos]

	def set(self,pos,v):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:73
		self.b[pos] = (v & 255)

	def blit(self,pos,src,srcpos,_hx_len):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:81
		if (((((pos < 0) or ((srcpos < 0))) or ((_hx_len < 0))) or (((pos + _hx_len) > self.length))) or (((srcpos + _hx_len) > src.length))):
			raise _HxException(haxe_io_Error.OutsideBounds)
		# /opt/haxe-git/std/haxe/io/Bytes.hx:95
		self.b[pos:pos+_hx_len] = src.b[srcpos:srcpos+_hx_len]

	def fill(self,pos,_hx_len,value):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:128
		_g = 0
		while (_g < _hx_len):
			i = _g
			_g = (_g + 1)
			# /opt/haxe-git/std/haxe/io/Bytes.hx:129
			pos1 = pos
			pos = (pos + 1)
			self.b[pos1] = (value & 255)

	def sub(self,pos,_hx_len):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:135
		if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > self.length))):
			raise _HxException(haxe_io_Error.OutsideBounds)
		# /opt/haxe-git/std/haxe/io/Bytes.hx:155
		return haxe_io_Bytes(_hx_len, self.b[pos:(pos + _hx_len)])

	def compare(self,other):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:197
		b1 = self.b
		# /opt/haxe-git/std/haxe/io/Bytes.hx:198
		b2 = other.b
		# /opt/haxe-git/std/haxe/io/Bytes.hx:199
		_hx_len = None
		if (self.length < other.length):
			_hx_len = self.length
		else:
			_hx_len = other.length
		# /opt/haxe-git/std/haxe/io/Bytes.hx:200
		# /opt/haxe-git/std/haxe/io/Bytes.hx:200
		_g = 0
		while (_g < _hx_len):
			i = _g
			_g = (_g + 1)
			# /opt/haxe-git/std/haxe/io/Bytes.hx:201
			if (b1[i] != b2[i]):
				return (b1[i] - b2[i])
		# /opt/haxe-git/std/haxe/io/Bytes.hx:203
		return (self.length - other.length)

	def getDouble(self,pos):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:223
		def _hx_local_2():
			# /opt/haxe-git/std/haxe/io/Bytes.hx:223
			def _hx_local_0():
				# /opt/haxe-git/std/haxe/io/Bytes.hx:223
				v = (((self.b[pos] | ((self.b[(pos + 1)] << 8))) | ((self.b[(pos + 2)] << 16))) | ((self.b[(pos + 3)] << 24)))
				return ((v | -2147483648) if ((((v & -2147483648)) != 0)) else v)
			def _hx_local_1():
				pos1 = (pos + 4)
				v1 = (((self.b[pos1] | ((self.b[(pos1 + 1)] << 8))) | ((self.b[(pos1 + 2)] << 16))) | ((self.b[(pos1 + 3)] << 24)))
				return ((v1 | -2147483648) if ((((v1 & -2147483648)) != 0)) else v1)
			return haxe_io_FPHelper.i64ToDouble(_hx_local_0(),_hx_local_1())
		return _hx_local_2()

	def getFloat(self,pos):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:242
		b = haxe_io_BytesInput(self, pos, 4)
		# /opt/haxe-git/std/haxe/io/Bytes.hx:243
		return b.readFloat()

	def setDouble(self,pos,v):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:264
		i = haxe_io_FPHelper.doubleToI64(v)
		# /opt/haxe-git/std/haxe/io/Bytes.hx:265
		# /opt/haxe-git/std/haxe/io/Bytes.hx:265
		v1 = i.low
		self.b[pos] = (v1 & 255)
		self.b[(pos + 1)] = ((v1 >> 8) & 255)
		self.b[(pos + 2)] = ((v1 >> 16) & 255)
		self.b[(pos + 3)] = (HxOverrides.rshift(v1, 24) & 255)
		# /opt/haxe-git/std/haxe/io/Bytes.hx:266
		# /opt/haxe-git/std/haxe/io/Bytes.hx:266
		pos1 = (pos + 4)
		v2 = i.high
		self.b[pos1] = (v2 & 255)
		self.b[(pos1 + 1)] = ((v2 >> 8) & 255)
		self.b[(pos1 + 2)] = ((v2 >> 16) & 255)
		self.b[(pos1 + 3)] = (HxOverrides.rshift(v2, 24) & 255)

	def setFloat(self,pos,v):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:287
		v1 = haxe_io_FPHelper.floatToI32(v)
		self.b[pos] = (v1 & 255)
		self.b[(pos + 1)] = ((v1 >> 8) & 255)
		self.b[(pos + 2)] = ((v1 >> 16) & 255)
		self.b[(pos + 3)] = (HxOverrides.rshift(v1, 24) & 255)

	def getUInt16(self,pos):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:298
		return (self.b[pos] | ((self.b[(pos + 1)] << 8)))

	def setUInt16(self,pos,v):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:309
		self.b[pos] = (v & 255)
		# /opt/haxe-git/std/haxe/io/Bytes.hx:310
		self.b[(pos + 1)] = ((v >> 8) & 255)

	def getInt32(self,pos):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:321
		v = (((self.b[pos] | ((self.b[(pos + 1)] << 8))) | ((self.b[(pos + 2)] << 16))) | ((self.b[(pos + 3)] << 24)))
		# /opt/haxe-git/std/haxe/io/Bytes.hx:322
		if (((v & -2147483648)) != 0):
			return (v | -2147483648)
		else:
			return v

	def getInt64(self,pos):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:332
		high = None
		pos1 = (pos + 4)
		v = (((self.b[pos1] | ((self.b[(pos1 + 1)] << 8))) | ((self.b[(pos1 + 2)] << 16))) | ((self.b[(pos1 + 3)] << 24)))
		if (((v & -2147483648)) != 0):
			high = (v | -2147483648)
		else:
			high = v
		low = None
		v1 = (((self.b[pos] | ((self.b[(pos + 1)] << 8))) | ((self.b[(pos + 2)] << 16))) | ((self.b[(pos + 3)] << 24)))
		if (((v1 & -2147483648)) != 0):
			low = (v1 | -2147483648)
		else:
			low = v1
		x = haxe__Int64____Int64(high, low)
		return x

	def setInt32(self,pos,v):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:342
		self.b[pos] = (v & 255)
		# /opt/haxe-git/std/haxe/io/Bytes.hx:343
		self.b[(pos + 1)] = ((v >> 8) & 255)
		# /opt/haxe-git/std/haxe/io/Bytes.hx:344
		self.b[(pos + 2)] = ((v >> 16) & 255)
		# /opt/haxe-git/std/haxe/io/Bytes.hx:345
		self.b[(pos + 3)] = (HxOverrides.rshift(v, 24) & 255)

	def setInt64(self,pos,v):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:353
		# /opt/haxe-git/std/haxe/io/Bytes.hx:353
		v1 = v.low
		self.b[pos] = (v1 & 255)
		self.b[(pos + 1)] = ((v1 >> 8) & 255)
		self.b[(pos + 2)] = ((v1 >> 16) & 255)
		self.b[(pos + 3)] = (HxOverrides.rshift(v1, 24) & 255)
		# /opt/haxe-git/std/haxe/io/Bytes.hx:354
		# /opt/haxe-git/std/haxe/io/Bytes.hx:354
		pos1 = (pos + 4)
		v2 = v.high
		self.b[pos1] = (v2 & 255)
		self.b[(pos1 + 1)] = ((v2 >> 8) & 255)
		self.b[(pos1 + 2)] = ((v2 >> 16) & 255)
		self.b[(pos1 + 3)] = (HxOverrides.rshift(v2, 24) & 255)

	def getString(self,pos,_hx_len):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:359
		if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > self.length))):
			raise _HxException(haxe_io_Error.OutsideBounds)
		# /opt/haxe-git/std/haxe/io/Bytes.hx:379
		return self.b[pos:pos+_hx_len].decode('UTF-8','replace')

	def readString(self,pos,_hx_len):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:413
		return self.getString(pos,_hx_len)

	def toString(self):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:433
		return self.getString(0,self.length)

	def toHex(self):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:438
		s_b = python_lib_io_StringIO()
		# /opt/haxe-git/std/haxe/io/Bytes.hx:439
		chars = []
		# /opt/haxe-git/std/haxe/io/Bytes.hx:440
		_hx_str = "0123456789abcdef"
		# /opt/haxe-git/std/haxe/io/Bytes.hx:441
		# /opt/haxe-git/std/haxe/io/Bytes.hx:441
		_g1 = 0
		_g = len(_hx_str)
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			# /opt/haxe-git/std/haxe/io/Bytes.hx:442
			x = HxString.charCodeAt(_hx_str,i)
			chars.append(x)
		# /opt/haxe-git/std/haxe/io/Bytes.hx:443
		# /opt/haxe-git/std/haxe/io/Bytes.hx:443
		_g11 = 0
		_g2 = self.length
		while (_g11 < _g2):
			i1 = _g11
			_g11 = (_g11 + 1)
			# /opt/haxe-git/std/haxe/io/Bytes.hx:444
			c = self.b[i1]
			# /opt/haxe-git/std/haxe/io/Bytes.hx:445
			# /opt/haxe-git/std/haxe/io/Bytes.hx:445
			s = "".join(map(chr,[python_internal_ArrayImpl._get(chars, (c >> 4))]))
			s_b.write(s)
			# /opt/haxe-git/std/haxe/io/Bytes.hx:446
			# /opt/haxe-git/std/haxe/io/Bytes.hx:446
			s1 = "".join(map(chr,[python_internal_ArrayImpl._get(chars, (c & 15))]))
			s_b.write(s1)
		# /opt/haxe-git/std/haxe/io/Bytes.hx:448
		return s_b.getvalue()

	def getData(self):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:452
		return self.b

	@staticmethod
	def alloc(length):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:473
		return haxe_io_Bytes(length, bytearray(length))

	@staticmethod
	def ofString(s):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:508
		b = bytearray(s, "UTF-8")
		# /opt/haxe-git/std/haxe/io/Bytes.hx:509
		return haxe_io_Bytes(len(b), b)

	@staticmethod
	def ofData(b):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:550
		return haxe_io_Bytes(len(b), b)

	@staticmethod
	def fastGet(b,pos):
		# /opt/haxe-git/std/haxe/io/Bytes.hx:570
		return b[pos]

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.length = None
		_hx_o.b = None
haxe_io_Bytes._hx_class = haxe_io_Bytes
_hx_classes["haxe.io.Bytes"] = haxe_io_Bytes


class haxe_io_BytesBuffer:
	_hx_class_name = "haxe.io.BytesBuffer"
	_hx_fields = ["b"]
	_hx_methods = ["get_length", "addByte", "add", "addString", "addInt32", "addInt64", "addFloat", "addDouble", "addBytes", "getBytes"]

	def __init__(self):
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:39
		self.b = None
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:60
		self.b = list()

	def get_length(self):
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:72
		return len(self.b)

	def addByte(self,byte):
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:90
		_this = self.b
		_this.append(byte)

	def add(self,src):
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:111
		b1 = self.b
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:112
		b2 = src.b
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:113
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:113
		_g1 = 0
		_g = src.length
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:114
			_this = self.b
			_this.append(b2[i])

	def addString(self,v):
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:124
		src = haxe_io_Bytes.ofString(v)
		b1 = self.b
		b2 = src.b
		_g1 = 0
		_g = src.length
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			_this = self.b
			_this.append(b2[i])

	def addInt32(self,v):
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:132
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:132
		_this = self.b
		_this.append((v & 255))
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:133
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:133
		_this1 = self.b
		_this1.append(((v >> 8) & 255))
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:134
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:134
		_this2 = self.b
		_this2.append(((v >> 16) & 255))
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:135
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:135
		_this3 = self.b
		_this3.append(HxOverrides.rshift(v, 24))

	def addInt64(self,v):
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:140
		self.addInt32(v.low)
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:141
		self.addInt32(v.high)

	def addFloat(self,v):
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:148
		self.addInt32(haxe_io_FPHelper.floatToI32(v))

	def addDouble(self,v):
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:156
		self.addInt64(haxe_io_FPHelper.doubleToI64(v))

	def addBytes(self,src,pos,_hx_len):
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:162
		if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > src.length))):
			raise _HxException(haxe_io_Error.OutsideBounds)
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:180
		b1 = self.b
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:181
		b2 = src.b
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:182
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:182
		_g1 = pos
		_g = (pos + _hx_len)
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:183
			_this = self.b
			_this.append(b2[i])

	def getBytes(self):
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:207
		buf = bytearray(self.b)
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:208
		_hx_bytes = haxe_io_Bytes(len(buf), buf)
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:214
		self.b = None
		# /opt/haxe-git/std/haxe/io/BytesBuffer.hx:215
		return _hx_bytes

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.b = None
haxe_io_BytesBuffer._hx_class = haxe_io_BytesBuffer
_hx_classes["haxe.io.BytesBuffer"] = haxe_io_BytesBuffer


class haxe_io_Input:
	_hx_class_name = "haxe.io.Input"
	_hx_fields = ["bigEndian"]
	_hx_methods = ["readByte", "readBytes", "close", "set_bigEndian", "readAll", "readFullBytes", "read", "readUntil", "readLine", "readFloat", "readDouble", "readInt8", "readInt16", "readUInt16", "readInt24", "readUInt24", "readInt32", "readString", "getDoubleSig"]

	def readByte(self):
		# /opt/haxe-git/std/haxe/io/Input.hx:50
		raise _HxException("Not implemented")

	def readBytes(self,s,pos,_hx_len):
		# /opt/haxe-git/std/haxe/io/Input.hx:62
		k = _hx_len
		# /opt/haxe-git/std/haxe/io/Input.hx:63
		b = s.b
		# /opt/haxe-git/std/haxe/io/Input.hx:64
		if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > s.length))):
			raise _HxException(haxe_io_Error.OutsideBounds)
		# /opt/haxe-git/std/haxe/io/Input.hx:66
		while (k > 0):
			# /opt/haxe-git/std/haxe/io/Input.hx:74
			b[pos] = self.readByte()
			# /opt/haxe-git/std/haxe/io/Input.hx:76
			pos = (pos + 1)
			# /opt/haxe-git/std/haxe/io/Input.hx:77
			k = (k - 1)
		# /opt/haxe-git/std/haxe/io/Input.hx:79
		return _hx_len

	def close(self):
		pass

	def set_bigEndian(self,b):
		# /opt/haxe-git/std/haxe/io/Input.hx:91
		self.bigEndian = b
		# /opt/haxe-git/std/haxe/io/Input.hx:92
		return b

	def readAll(self,bufsize = None):
		# /opt/haxe-git/std/haxe/io/Input.hx:104
		if (bufsize is None):
			bufsize = 16384
		# /opt/haxe-git/std/haxe/io/Input.hx:111
		buf = haxe_io_Bytes.alloc(bufsize)
		# /opt/haxe-git/std/haxe/io/Input.hx:112
		total = haxe_io_BytesBuffer()
		# /opt/haxe-git/std/haxe/io/Input.hx:113
		try:
			while True:
				# /opt/haxe-git/std/haxe/io/Input.hx:115
				_hx_len = self.readBytes(buf,0,bufsize)
				# /opt/haxe-git/std/haxe/io/Input.hx:116
				if (_hx_len == 0):
					raise _HxException(haxe_io_Error.Blocked)
				# /opt/haxe-git/std/haxe/io/Input.hx:118
				# /opt/haxe-git/std/haxe/io/Input.hx:118
				if ((_hx_len < 0) or ((_hx_len > buf.length))):
					raise _HxException(haxe_io_Error.OutsideBounds)
				b1 = total.b
				b2 = buf.b
				_g1 = 0
				_g = _hx_len
				while (_g1 < _g):
					i = _g1
					_g1 = (_g1 + 1)
					_this = total.b
					_this.append(b2[i])
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			if isinstance(_hx_e1, haxe_io_Eof):
					pass
			else:
				raise _hx_e
		# /opt/haxe-git/std/haxe/io/Input.hx:122
		return total.getBytes()

	def readFullBytes(self,s,pos,_hx_len):
		# /opt/haxe-git/std/haxe/io/Input.hx:131
		while (_hx_len > 0):
			# /opt/haxe-git/std/haxe/io/Input.hx:132
			k = self.readBytes(s,pos,_hx_len)
			# /opt/haxe-git/std/haxe/io/Input.hx:133
			pos = (pos + k)
			# /opt/haxe-git/std/haxe/io/Input.hx:134
			_hx_len = (_hx_len - k)

	def read(self,nbytes):
		# /opt/haxe-git/std/haxe/io/Input.hx:142
		s = haxe_io_Bytes.alloc(nbytes)
		# /opt/haxe-git/std/haxe/io/Input.hx:143
		p = 0
		# /opt/haxe-git/std/haxe/io/Input.hx:144
		while (nbytes > 0):
			# /opt/haxe-git/std/haxe/io/Input.hx:145
			k = self.readBytes(s,p,nbytes)
			# /opt/haxe-git/std/haxe/io/Input.hx:146
			if (k == 0):
				raise _HxException(haxe_io_Error.Blocked)
			# /opt/haxe-git/std/haxe/io/Input.hx:147
			p = (p + k)
			# /opt/haxe-git/std/haxe/io/Input.hx:148
			nbytes = (nbytes - k)
		# /opt/haxe-git/std/haxe/io/Input.hx:150
		return s

	def readUntil(self,end):
		# /opt/haxe-git/std/haxe/io/Input.hx:159
		buf_b = python_lib_io_StringIO()
		# /opt/haxe-git/std/haxe/io/Input.hx:160
		last = None
		# /opt/haxe-git/std/haxe/io/Input.hx:161
		def _hx_local_0():
			# /opt/haxe-git/std/haxe/io/Input.hx:161
			nonlocal last
			last = self.readByte()
			return last
		while ((_hx_local_0()) != end):
			# /opt/haxe-git/std/haxe/io/Input.hx:162
			s = "".join(map(chr,[last]))
			buf_b.write(s)
		# /opt/haxe-git/std/haxe/io/Input.hx:163
		return buf_b.getvalue()

	def readLine(self):
		# /opt/haxe-git/std/haxe/io/Input.hx:172
		buf_b = python_lib_io_StringIO()
		# /opt/haxe-git/std/haxe/io/Input.hx:173
		last = None
		# /opt/haxe-git/std/haxe/io/Input.hx:174
		s = None
		# /opt/haxe-git/std/haxe/io/Input.hx:175
		try:
			# /opt/haxe-git/std/haxe/io/Input.hx:176
			def _hx_local_0():
				# /opt/haxe-git/std/haxe/io/Input.hx:176
				nonlocal last
				last = self.readByte()
				return last
			while ((_hx_local_0()) != 10):
				# /opt/haxe-git/std/haxe/io/Input.hx:177
				s1 = "".join(map(chr,[last]))
				buf_b.write(s1)
			# /opt/haxe-git/std/haxe/io/Input.hx:178
			s = buf_b.getvalue()
			# /opt/haxe-git/std/haxe/io/Input.hx:179
			if (HxString.charCodeAt(s,(len(s) - 1)) == 13):
				s = HxString.substr(s,0,-1)
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			if isinstance(_hx_e1, haxe_io_Eof):
				e = _hx_e1
				# /opt/haxe-git/std/haxe/io/Input.hx:181
				s = buf_b.getvalue()
				# /opt/haxe-git/std/haxe/io/Input.hx:182
				if (len(s) == 0):
					raise _HxException(e)
			else:
				raise _hx_e
		# /opt/haxe-git/std/haxe/io/Input.hx:185
		return s

	def readFloat(self):
		# /opt/haxe-git/std/haxe/io/Input.hx:194
		return haxe_io_FPHelper.i32ToFloat(self.readInt32())

	def readDouble(self):
		# /opt/haxe-git/std/haxe/io/Input.hx:203
		i1 = self.readInt32()
		# /opt/haxe-git/std/haxe/io/Input.hx:204
		i2 = self.readInt32()
		# /opt/haxe-git/std/haxe/io/Input.hx:205
		if self.bigEndian:
			return haxe_io_FPHelper.i64ToDouble(i2,i1)
		else:
			return haxe_io_FPHelper.i64ToDouble(i1,i2)

	def readInt8(self):
		# /opt/haxe-git/std/haxe/io/Input.hx:212
		n = self.readByte()
		# /opt/haxe-git/std/haxe/io/Input.hx:213
		if (n >= 128):
			return (n - 256)
		# /opt/haxe-git/std/haxe/io/Input.hx:215
		return n

	def readInt16(self):
		# /opt/haxe-git/std/haxe/io/Input.hx:224
		ch1 = self.readByte()
		# /opt/haxe-git/std/haxe/io/Input.hx:225
		ch2 = self.readByte()
		# /opt/haxe-git/std/haxe/io/Input.hx:226
		n = None
		if self.bigEndian:
			n = (ch2 | ((ch1 << 8)))
		else:
			n = (ch1 | ((ch2 << 8)))
		# /opt/haxe-git/std/haxe/io/Input.hx:227
		if (((n & 32768)) != 0):
			return (n - 65536)
		# /opt/haxe-git/std/haxe/io/Input.hx:229
		return n

	def readUInt16(self):
		# /opt/haxe-git/std/haxe/io/Input.hx:238
		ch1 = self.readByte()
		# /opt/haxe-git/std/haxe/io/Input.hx:239
		ch2 = self.readByte()
		# /opt/haxe-git/std/haxe/io/Input.hx:240
		if self.bigEndian:
			return (ch2 | ((ch1 << 8)))
		else:
			return (ch1 | ((ch2 << 8)))

	def readInt24(self):
		# /opt/haxe-git/std/haxe/io/Input.hx:249
		ch1 = self.readByte()
		# /opt/haxe-git/std/haxe/io/Input.hx:250
		ch2 = self.readByte()
		# /opt/haxe-git/std/haxe/io/Input.hx:251
		ch3 = self.readByte()
		# /opt/haxe-git/std/haxe/io/Input.hx:252
		n = None
		if self.bigEndian:
			n = ((ch3 | ((ch2 << 8))) | ((ch1 << 16)))
		else:
			n = ((ch1 | ((ch2 << 8))) | ((ch3 << 16)))
		# /opt/haxe-git/std/haxe/io/Input.hx:253
		if (((n & 8388608)) != 0):
			return (n - 16777216)
		# /opt/haxe-git/std/haxe/io/Input.hx:255
		return n

	def readUInt24(self):
		# /opt/haxe-git/std/haxe/io/Input.hx:264
		ch1 = self.readByte()
		# /opt/haxe-git/std/haxe/io/Input.hx:265
		ch2 = self.readByte()
		# /opt/haxe-git/std/haxe/io/Input.hx:266
		ch3 = self.readByte()
		# /opt/haxe-git/std/haxe/io/Input.hx:267
		if self.bigEndian:
			return ((ch3 | ((ch2 << 8))) | ((ch1 << 16)))
		else:
			return ((ch1 | ((ch2 << 8))) | ((ch3 << 16)))

	def readInt32(self):
		# /opt/haxe-git/std/haxe/io/Input.hx:276
		ch1 = self.readByte()
		# /opt/haxe-git/std/haxe/io/Input.hx:277
		ch2 = self.readByte()
		# /opt/haxe-git/std/haxe/io/Input.hx:278
		ch3 = self.readByte()
		# /opt/haxe-git/std/haxe/io/Input.hx:279
		ch4 = self.readByte()
		# /opt/haxe-git/std/haxe/io/Input.hx:282
		n = None
		if self.bigEndian:
			n = (((ch4 | ((ch3 << 8))) | ((ch2 << 16))) | ((ch1 << 24)))
		else:
			n = (((ch1 | ((ch2 << 8))) | ((ch3 << 16))) | ((ch4 << 24)))
		# /opt/haxe-git/std/haxe/io/Input.hx:283
		if (((n & -2147483648)) != 0):
			return (n | -2147483648)
		else:
			return n

	def readString(self,_hx_len):
		# /opt/haxe-git/std/haxe/io/Input.hx:295
		b = haxe_io_Bytes.alloc(_hx_len)
		# /opt/haxe-git/std/haxe/io/Input.hx:296
		self.readFullBytes(b,0,_hx_len)
		# /opt/haxe-git/std/haxe/io/Input.hx:300
		return b.toString()

	def getDoubleSig(self,_hx_bytes):
		# /opt/haxe-git/std/haxe/io/Input.hx:318
		return ((((((((((_hx_bytes[1] if 1 < len(_hx_bytes) else None) & 15)) << 16) | (((_hx_bytes[2] if 2 < len(_hx_bytes) else None) << 8))) | (_hx_bytes[3] if 3 < len(_hx_bytes) else None))) * 4294967296.) + (((((_hx_bytes[4] if 4 < len(_hx_bytes) else None) >> 7)) * 2147483648))) + ((((((((_hx_bytes[4] if 4 < len(_hx_bytes) else None) & 127)) << 24) | (((_hx_bytes[5] if 5 < len(_hx_bytes) else None) << 16))) | (((_hx_bytes[6] if 6 < len(_hx_bytes) else None) << 8))) | (_hx_bytes[7] if 7 < len(_hx_bytes) else None))))

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.bigEndian = None
haxe_io_Input._hx_class = haxe_io_Input
_hx_classes["haxe.io.Input"] = haxe_io_Input


class haxe_io_BytesInput(haxe_io_Input):
	_hx_class_name = "haxe.io.BytesInput"
	_hx_fields = ["b", "pos", "len", "totlen"]
	_hx_methods = ["get_position", "get_length", "set_position", "readByte", "readBytes"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = haxe_io_Input


	def __init__(self,b,pos = None,_hx_len = None):
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:25
		self.b = None
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:27
		self.pos = None
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:28
		self.len = None
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:29
		self.totlen = None
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:39
		if (pos is None):
			pos = 0
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:40
		if (_hx_len is None):
			_hx_len = (b.length - pos)
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:41
		if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > b.length))):
			raise _HxException(haxe_io_Error.OutsideBounds)
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:53
		self.b = b.b
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:54
		self.pos = pos
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:55
		self.len = _hx_len
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:56
		self.totlen = _hx_len
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:59
		self.set_bigEndian(False)

	def get_position(self):
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:67
		return self.pos

	def get_length(self):
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:75
		return self.totlen

	def set_position(self,p):
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:80
		if (p < 0):
			p = 0
		elif (p > self.totlen):
			p = self.totlen
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:85
		self.len = (self.totlen - p)
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:86
		def _hx_local_1():
			# /opt/haxe-git/std/haxe/io/BytesInput.hx:86
			def _hx_local_0():
				# /opt/haxe-git/std/haxe/io/BytesInput.hx:86
				self.pos = p
				return self.pos
			return _hx_local_0()
		return _hx_local_1()

	def readByte(self):
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:94
		if (self.len == 0):
			raise _HxException(haxe_io_Eof())
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:96
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:96
		_hx_local_0 = self
		_hx_local_1 = _hx_local_0.len
		_hx_local_0.len = (_hx_local_1 - 1)
		_hx_local_1
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:106
		def _hx_local_5():
			# /opt/haxe-git/std/haxe/io/BytesInput.hx:106
			def _hx_local_4():
				# /opt/haxe-git/std/haxe/io/BytesInput.hx:106
				_hx_local_2 = self
				_hx_local_3 = _hx_local_2.pos
				_hx_local_2.pos = (_hx_local_3 + 1)
				return _hx_local_3
			return self.b[_hx_local_4()]
		return _hx_local_5()

	def readBytes(self,buf,pos,_hx_len):
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:113
		if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > buf.length))):
			raise _HxException(haxe_io_Error.OutsideBounds)
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:137
		if ((self.len == 0) and ((_hx_len > 0))):
			raise _HxException(haxe_io_Eof())
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:139
		if (self.len < _hx_len):
			_hx_len = self.len
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:146
		b1 = self.b
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:147
		b2 = buf.b
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:148
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:148
		_g = 0
		while (_g < _hx_len):
			i = _g
			_g = (_g + 1)
			# /opt/haxe-git/std/haxe/io/BytesInput.hx:149
			b2[(pos + i)] = b1[(self.pos + i)]
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:151
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:151
		_hx_local_0 = self
		_hx_local_1 = _hx_local_0.pos
		_hx_local_0.pos = (_hx_local_1 + _hx_len)
		_hx_local_0.pos
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:152
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:152
		_hx_local_2 = self
		_hx_local_3 = _hx_local_2.len
		_hx_local_2.len = (_hx_local_3 - _hx_len)
		_hx_local_2.len
		# /opt/haxe-git/std/haxe/io/BytesInput.hx:154
		return _hx_len

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.b = None
		_hx_o.pos = None
		_hx_o.len = None
		_hx_o.totlen = None
haxe_io_BytesInput._hx_class = haxe_io_BytesInput
_hx_classes["haxe.io.BytesInput"] = haxe_io_BytesInput


class haxe_io_Eof:
	_hx_class_name = "haxe.io.Eof"
	_hx_methods = ["toString"]

	def __init__(self):
		pass

	def toString(self):
		# /opt/haxe-git/std/haxe/io/Eof.hx:31
		return "Eof"

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
haxe_io_Eof._hx_class = haxe_io_Eof
_hx_classes["haxe.io.Eof"] = haxe_io_Eof

class haxe_io_Error(Enum):
	_hx_class_name = "haxe.io.Error"
	_hx_constructs = ["Blocked", "Overflow", "OutsideBounds", "Custom"]

	@staticmethod
	def Custom(e):
		return haxe_io_Error("Custom", 3, [e])
haxe_io_Error.Blocked = haxe_io_Error("Blocked", 0, list())
haxe_io_Error.Overflow = haxe_io_Error("Overflow", 1, list())
haxe_io_Error.OutsideBounds = haxe_io_Error("OutsideBounds", 2, list())
haxe_io_Error._hx_class = haxe_io_Error
_hx_classes["haxe.io.Error"] = haxe_io_Error


class haxe_io_FPHelper:
	_hx_class_name = "haxe.io.FPHelper"
	_hx_statics = ["i64tmp", "LN2", "i32ToFloat", "floatToI32", "i64ToDouble", "doubleToI64"]

	@staticmethod
	def i32ToFloat(i):
		# /opt/haxe-git/std/haxe/io/FPHelper.hx:99
		sign = (1 - ((HxOverrides.rshift(i, 31) << 1)))
		# /opt/haxe-git/std/haxe/io/FPHelper.hx:100
		exp = (HxOverrides.rshift(i, 23) & 255)
		# /opt/haxe-git/std/haxe/io/FPHelper.hx:101
		sig = (i & 8388607)
		# /opt/haxe-git/std/haxe/io/FPHelper.hx:102
		if ((sig == 0) and ((exp == 0))):
			return 0.0
		# /opt/haxe-git/std/haxe/io/FPHelper.hx:104
		return ((sign * ((1 + ((Math.pow(2,-23) * sig))))) * Math.pow(2,(exp - 127)))

	@staticmethod
	def floatToI32(f):
		# /opt/haxe-git/std/haxe/io/FPHelper.hx:139
		if (f == 0):
			return 0
		# /opt/haxe-git/std/haxe/io/FPHelper.hx:140
		af = None
		if (f < 0):
			af = -f
		else:
			af = f
		# /opt/haxe-git/std/haxe/io/FPHelper.hx:141
		exp = Math.floor((((Math.NEGATIVE_INFINITY if ((af == 0.0)) else (Math.NaN if ((af < 0.0)) else python_lib_Math.log(af)))) / 0.6931471805599453))
		# /opt/haxe-git/std/haxe/io/FPHelper.hx:142
		if (exp < -127):
			exp = -127
		elif (exp > 128):
			exp = 128
		# /opt/haxe-git/std/haxe/io/FPHelper.hx:143
		sig = None
		def _hx_local_0():
			v = ((((af / Math.pow(2,exp)) - 1)) * 8388608)
			return Math.floor((v + 0.5))
		sig = (_hx_local_0() & 8388607)
		# /opt/haxe-git/std/haxe/io/FPHelper.hx:144
		return ((((-2147483648 if ((f < 0)) else 0)) | (((exp + 127) << 23))) | sig)

	@staticmethod
	def i64ToDouble(low,high):
		# /opt/haxe-git/std/haxe/io/FPHelper.hx:194
		sign = (1 - ((HxOverrides.rshift(high, 31) << 1)))
		# /opt/haxe-git/std/haxe/io/FPHelper.hx:195
		exp = ((((high >> 20) & 2047)) - 1023)
		# /opt/haxe-git/std/haxe/io/FPHelper.hx:196
		sig = (((((high & 1048575)) * 4294967296.) + (((HxOverrides.rshift(low, 31)) * 2147483648.))) + ((low & 2147483647)))
		# /opt/haxe-git/std/haxe/io/FPHelper.hx:197
		if ((sig == 0) and ((exp == -1023))):
			return 0.0
		# /opt/haxe-git/std/haxe/io/FPHelper.hx:199
		return ((sign * ((1.0 + ((Math.pow(2,-52) * sig))))) * Math.pow(2,exp))

	@staticmethod
	def doubleToI64(v):
		# /opt/haxe-git/std/haxe/io/FPHelper.hx:273
		i64 = haxe_io_FPHelper.i64tmp
		# /opt/haxe-git/std/haxe/io/FPHelper.hx:274
		if (v == 0):
			# /opt/haxe-git/std/haxe/io/FPHelper.hx:276
			i64.low = 0
			# /opt/haxe-git/std/haxe/io/FPHelper.hx:277
			i64.high = 0
		else:
			# /opt/haxe-git/std/haxe/io/FPHelper.hx:280
			av = None
			if (v < 0):
				av = -v
			else:
				av = v
			# /opt/haxe-git/std/haxe/io/FPHelper.hx:281
			exp = Math.floor((((Math.NEGATIVE_INFINITY if ((av == 0.0)) else (Math.NaN if ((av < 0.0)) else python_lib_Math.log(av)))) / 0.6931471805599453))
			# /opt/haxe-git/std/haxe/io/FPHelper.hx:282
			sig = None
			v1 = ((((av / Math.pow(2,exp)) - 1)) * 4503599627370496.)
			if ((v1 == Math.POSITIVE_INFINITY) or ((v1 == Math.NEGATIVE_INFINITY))):
				sig = v1
			elif python_lib_Math.isnan(v1):
				sig = Math.NaN
			else:
				sig = Math.floor((v1 + 0.5))
			# /opt/haxe-git/std/haxe/io/FPHelper.hx:283
			sig_l = None
			def _hx_local_1():
				_hx_local_0 = None
				try:
					_hx_local_0 = int(sig)
				except Exception as _hx_e:
					_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
					e = _hx_e1
					_hx_local_0 = None
				return _hx_local_0
			sig_l = _hx_local_1()
			# /opt/haxe-git/std/haxe/io/FPHelper.hx:284
			sig_h = None
			def _hx_local_3():
				_hx_local_2 = None
				try:
					_hx_local_2 = int((sig / 4294967296.0))
				except Exception as _hx_e:
					_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
					e1 = _hx_e1
					_hx_local_2 = None
				return _hx_local_2
			sig_h = _hx_local_3()
			# /opt/haxe-git/std/haxe/io/FPHelper.hx:285
			# /opt/haxe-git/std/haxe/io/FPHelper.hx:286
			i64.low = sig_l
			# /opt/haxe-git/std/haxe/io/FPHelper.hx:287
			i64.high = ((((-2147483648 if ((v < 0)) else 0)) | (((exp + 1023) << 20))) | sig_h)
		# /opt/haxe-git/std/haxe/io/FPHelper.hx:290
		return i64
haxe_io_FPHelper._hx_class = haxe_io_FPHelper
_hx_classes["haxe.io.FPHelper"] = haxe_io_FPHelper


class haxe_io_Output:
	_hx_class_name = "haxe.io.Output"
	_hx_fields = ["bigEndian"]
	_hx_methods = ["writeByte", "writeBytes", "flush", "close", "set_bigEndian", "write", "writeFullBytes", "writeFloat", "writeDouble", "writeInt8", "writeInt16", "writeUInt16", "writeInt24", "writeUInt24", "writeInt32", "prepare", "writeInput", "writeString"]

	def writeByte(self,c):
		# /opt/haxe-git/std/haxe/io/Output.hx:47
		raise _HxException("Not implemented")

	def writeBytes(self,s,pos,_hx_len):
		# /opt/haxe-git/std/haxe/io/Output.hx:58
		k = _hx_len
		# /opt/haxe-git/std/haxe/io/Output.hx:59
		b = s.b
		# /opt/haxe-git/std/haxe/io/Output.hx:61
		if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > s.length))):
			raise _HxException(haxe_io_Error.OutsideBounds)
		# /opt/haxe-git/std/haxe/io/Output.hx:64
		while (k > 0):
			# /opt/haxe-git/std/haxe/io/Output.hx:72
			self.writeByte(b[pos])
			# /opt/haxe-git/std/haxe/io/Output.hx:74
			pos = (pos + 1)
			# /opt/haxe-git/std/haxe/io/Output.hx:75
			k = (k - 1)
		# /opt/haxe-git/std/haxe/io/Output.hx:77
		return _hx_len

	def flush(self):
		pass

	def close(self):
		pass

	def set_bigEndian(self,b):
		# /opt/haxe-git/std/haxe/io/Output.hx:95
		self.bigEndian = b
		# /opt/haxe-git/std/haxe/io/Output.hx:96
		return b

	def write(self,s):
		# /opt/haxe-git/std/haxe/io/Output.hx:105
		l = s.length
		# /opt/haxe-git/std/haxe/io/Output.hx:106
		p = 0
		# /opt/haxe-git/std/haxe/io/Output.hx:107
		while (l > 0):
			# /opt/haxe-git/std/haxe/io/Output.hx:108
			k = self.writeBytes(s,p,l)
			# /opt/haxe-git/std/haxe/io/Output.hx:109
			if (k == 0):
				raise _HxException(haxe_io_Error.Blocked)
			# /opt/haxe-git/std/haxe/io/Output.hx:110
			p = (p + k)
			# /opt/haxe-git/std/haxe/io/Output.hx:111
			l = (l - k)

	def writeFullBytes(self,s,pos,_hx_len):
		# /opt/haxe-git/std/haxe/io/Output.hx:121
		while (_hx_len > 0):
			# /opt/haxe-git/std/haxe/io/Output.hx:122
			k = self.writeBytes(s,pos,_hx_len)
			# /opt/haxe-git/std/haxe/io/Output.hx:123
			pos = (pos + k)
			# /opt/haxe-git/std/haxe/io/Output.hx:124
			_hx_len = (_hx_len - k)

	def writeFloat(self,x):
		# /opt/haxe-git/std/haxe/io/Output.hx:134
		self.writeInt32(haxe_io_FPHelper.floatToI32(x))

	def writeDouble(self,x):
		# /opt/haxe-git/std/haxe/io/Output.hx:143
		i64 = haxe_io_FPHelper.doubleToI64(x)
		# /opt/haxe-git/std/haxe/io/Output.hx:144
		if self.bigEndian:
			# /opt/haxe-git/std/haxe/io/Output.hx:145
			self.writeInt32(i64.high)
			# /opt/haxe-git/std/haxe/io/Output.hx:146
			self.writeInt32(i64.low)
		else:
			# /opt/haxe-git/std/haxe/io/Output.hx:148
			self.writeInt32(i64.low)
			# /opt/haxe-git/std/haxe/io/Output.hx:149
			self.writeInt32(i64.high)

	def writeInt8(self,x):
		# /opt/haxe-git/std/haxe/io/Output.hx:157
		if ((x < -128) or ((x >= 128))):
			raise _HxException(haxe_io_Error.Overflow)
		# /opt/haxe-git/std/haxe/io/Output.hx:159
		self.writeByte((x & 255))

	def writeInt16(self,x):
		# /opt/haxe-git/std/haxe/io/Output.hx:168
		if ((x < -32768) or ((x >= 32768))):
			raise _HxException(haxe_io_Error.Overflow)
		# /opt/haxe-git/std/haxe/io/Output.hx:169
		self.writeUInt16((x & 65535))

	def writeUInt16(self,x):
		# /opt/haxe-git/std/haxe/io/Output.hx:178
		if ((x < 0) or ((x >= 65536))):
			raise _HxException(haxe_io_Error.Overflow)
		# /opt/haxe-git/std/haxe/io/Output.hx:179
		if self.bigEndian:
			# /opt/haxe-git/std/haxe/io/Output.hx:180
			self.writeByte((x >> 8))
			# /opt/haxe-git/std/haxe/io/Output.hx:181
			self.writeByte((x & 255))
		else:
			# /opt/haxe-git/std/haxe/io/Output.hx:183
			self.writeByte((x & 255))
			# /opt/haxe-git/std/haxe/io/Output.hx:184
			self.writeByte((x >> 8))

	def writeInt24(self,x):
		# /opt/haxe-git/std/haxe/io/Output.hx:194
		if ((x < -8388608) or ((x >= 8388608))):
			raise _HxException(haxe_io_Error.Overflow)
		# /opt/haxe-git/std/haxe/io/Output.hx:195
		self.writeUInt24((x & 16777215))

	def writeUInt24(self,x):
		# /opt/haxe-git/std/haxe/io/Output.hx:204
		if ((x < 0) or ((x >= 16777216))):
			raise _HxException(haxe_io_Error.Overflow)
		# /opt/haxe-git/std/haxe/io/Output.hx:205
		if self.bigEndian:
			# /opt/haxe-git/std/haxe/io/Output.hx:206
			self.writeByte((x >> 16))
			# /opt/haxe-git/std/haxe/io/Output.hx:207
			self.writeByte(((x >> 8) & 255))
			# /opt/haxe-git/std/haxe/io/Output.hx:208
			self.writeByte((x & 255))
		else:
			# /opt/haxe-git/std/haxe/io/Output.hx:210
			self.writeByte((x & 255))
			# /opt/haxe-git/std/haxe/io/Output.hx:211
			self.writeByte(((x >> 8) & 255))
			# /opt/haxe-git/std/haxe/io/Output.hx:212
			self.writeByte((x >> 16))

	def writeInt32(self,x):
		# /opt/haxe-git/std/haxe/io/Output.hx:222
		if self.bigEndian:
			# /opt/haxe-git/std/haxe/io/Output.hx:223
			self.writeByte(HxOverrides.rshift(x, 24))
			# /opt/haxe-git/std/haxe/io/Output.hx:224
			self.writeByte(((x >> 16) & 255))
			# /opt/haxe-git/std/haxe/io/Output.hx:225
			self.writeByte(((x >> 8) & 255))
			# /opt/haxe-git/std/haxe/io/Output.hx:226
			self.writeByte((x & 255))
		else:
			# /opt/haxe-git/std/haxe/io/Output.hx:228
			self.writeByte((x & 255))
			# /opt/haxe-git/std/haxe/io/Output.hx:229
			self.writeByte(((x >> 8) & 255))
			# /opt/haxe-git/std/haxe/io/Output.hx:230
			self.writeByte(((x >> 16) & 255))
			# /opt/haxe-git/std/haxe/io/Output.hx:231
			self.writeByte(HxOverrides.rshift(x, 24))

	def prepare(self,nbytes):
		pass

	def writeInput(self,i,bufsize = None):
		# /opt/haxe-git/std/haxe/io/Output.hx:252
		if (bufsize is None):
			bufsize = 4096
		# /opt/haxe-git/std/haxe/io/Output.hx:254
		buf = haxe_io_Bytes.alloc(bufsize)
		# /opt/haxe-git/std/haxe/io/Output.hx:255
		try:
			while True:
				# /opt/haxe-git/std/haxe/io/Output.hx:257
				_hx_len = i.readBytes(buf,0,bufsize)
				# /opt/haxe-git/std/haxe/io/Output.hx:258
				if (_hx_len == 0):
					raise _HxException(haxe_io_Error.Blocked)
				# /opt/haxe-git/std/haxe/io/Output.hx:260
				p = 0
				# /opt/haxe-git/std/haxe/io/Output.hx:261
				while (_hx_len > 0):
					# /opt/haxe-git/std/haxe/io/Output.hx:262
					k = self.writeBytes(buf,p,_hx_len)
					# /opt/haxe-git/std/haxe/io/Output.hx:263
					if (k == 0):
						raise _HxException(haxe_io_Error.Blocked)
					# /opt/haxe-git/std/haxe/io/Output.hx:265
					p = (p + k)
					# /opt/haxe-git/std/haxe/io/Output.hx:266
					_hx_len = (_hx_len - k)
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			if isinstance(_hx_e1, haxe_io_Eof):
					pass
			else:
				raise _hx_e

	def writeString(self,s):
		# /opt/haxe-git/std/haxe/io/Output.hx:280
		b = haxe_io_Bytes.ofString(s)
		# /opt/haxe-git/std/haxe/io/Output.hx:282
		self.writeFullBytes(b,0,b.length)

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.bigEndian = None
haxe_io_Output._hx_class = haxe_io_Output
_hx_classes["haxe.io.Output"] = haxe_io_Output

class haxe_macro_Constant(Enum):
	_hx_class_name = "haxe.macro.Constant"
	_hx_constructs = ["CInt", "CFloat", "CString", "CIdent", "CRegexp"]

	@staticmethod
	def CInt(v):
		return haxe_macro_Constant("CInt", 0, [v])

	@staticmethod
	def CFloat(f):
		return haxe_macro_Constant("CFloat", 1, [f])

	@staticmethod
	def CString(s):
		return haxe_macro_Constant("CString", 2, [s])

	@staticmethod
	def CIdent(s):
		return haxe_macro_Constant("CIdent", 3, [s])

	@staticmethod
	def CRegexp(r,opt):
		return haxe_macro_Constant("CRegexp", 4, [r,opt])
haxe_macro_Constant._hx_class = haxe_macro_Constant
_hx_classes["haxe.macro.Constant"] = haxe_macro_Constant

class haxe_macro_Binop(Enum):
	_hx_class_name = "haxe.macro.Binop"
	_hx_constructs = ["OpAdd", "OpMult", "OpDiv", "OpSub", "OpAssign", "OpEq", "OpNotEq", "OpGt", "OpGte", "OpLt", "OpLte", "OpAnd", "OpOr", "OpXor", "OpBoolAnd", "OpBoolOr", "OpShl", "OpShr", "OpUShr", "OpMod", "OpAssignOp", "OpInterval", "OpArrow"]

	@staticmethod
	def OpAssignOp(op):
		return haxe_macro_Binop("OpAssignOp", 20, [op])
haxe_macro_Binop.OpAdd = haxe_macro_Binop("OpAdd", 0, list())
haxe_macro_Binop.OpMult = haxe_macro_Binop("OpMult", 1, list())
haxe_macro_Binop.OpDiv = haxe_macro_Binop("OpDiv", 2, list())
haxe_macro_Binop.OpSub = haxe_macro_Binop("OpSub", 3, list())
haxe_macro_Binop.OpAssign = haxe_macro_Binop("OpAssign", 4, list())
haxe_macro_Binop.OpEq = haxe_macro_Binop("OpEq", 5, list())
haxe_macro_Binop.OpNotEq = haxe_macro_Binop("OpNotEq", 6, list())
haxe_macro_Binop.OpGt = haxe_macro_Binop("OpGt", 7, list())
haxe_macro_Binop.OpGte = haxe_macro_Binop("OpGte", 8, list())
haxe_macro_Binop.OpLt = haxe_macro_Binop("OpLt", 9, list())
haxe_macro_Binop.OpLte = haxe_macro_Binop("OpLte", 10, list())
haxe_macro_Binop.OpAnd = haxe_macro_Binop("OpAnd", 11, list())
haxe_macro_Binop.OpOr = haxe_macro_Binop("OpOr", 12, list())
haxe_macro_Binop.OpXor = haxe_macro_Binop("OpXor", 13, list())
haxe_macro_Binop.OpBoolAnd = haxe_macro_Binop("OpBoolAnd", 14, list())
haxe_macro_Binop.OpBoolOr = haxe_macro_Binop("OpBoolOr", 15, list())
haxe_macro_Binop.OpShl = haxe_macro_Binop("OpShl", 16, list())
haxe_macro_Binop.OpShr = haxe_macro_Binop("OpShr", 17, list())
haxe_macro_Binop.OpUShr = haxe_macro_Binop("OpUShr", 18, list())
haxe_macro_Binop.OpMod = haxe_macro_Binop("OpMod", 19, list())
haxe_macro_Binop.OpInterval = haxe_macro_Binop("OpInterval", 21, list())
haxe_macro_Binop.OpArrow = haxe_macro_Binop("OpArrow", 22, list())
haxe_macro_Binop._hx_class = haxe_macro_Binop
_hx_classes["haxe.macro.Binop"] = haxe_macro_Binop

class haxe_macro_Unop(Enum):
	_hx_class_name = "haxe.macro.Unop"
	_hx_constructs = ["OpIncrement", "OpDecrement", "OpNot", "OpNeg", "OpNegBits"]
haxe_macro_Unop.OpIncrement = haxe_macro_Unop("OpIncrement", 0, list())
haxe_macro_Unop.OpDecrement = haxe_macro_Unop("OpDecrement", 1, list())
haxe_macro_Unop.OpNot = haxe_macro_Unop("OpNot", 2, list())
haxe_macro_Unop.OpNeg = haxe_macro_Unop("OpNeg", 3, list())
haxe_macro_Unop.OpNegBits = haxe_macro_Unop("OpNegBits", 4, list())
haxe_macro_Unop._hx_class = haxe_macro_Unop
_hx_classes["haxe.macro.Unop"] = haxe_macro_Unop

class haxe_macro_ExprDef(Enum):
	_hx_class_name = "haxe.macro.ExprDef"
	_hx_constructs = ["EConst", "EArray", "EBinop", "EField", "EParenthesis", "EObjectDecl", "EArrayDecl", "ECall", "ENew", "EUnop", "EVars", "EFunction", "EBlock", "EFor", "EIn", "EIf", "EWhile", "ESwitch", "ETry", "EReturn", "EBreak", "EContinue", "EUntyped", "EThrow", "ECast", "EDisplay", "EDisplayNew", "ETernary", "ECheckType", "EMeta"]

	@staticmethod
	def EConst(c):
		return haxe_macro_ExprDef("EConst", 0, [c])

	@staticmethod
	def EArray(e1,e2):
		return haxe_macro_ExprDef("EArray", 1, [e1,e2])

	@staticmethod
	def EBinop(op,e1,e2):
		return haxe_macro_ExprDef("EBinop", 2, [op,e1,e2])

	@staticmethod
	def EField(e,field):
		return haxe_macro_ExprDef("EField", 3, [e,field])

	@staticmethod
	def EParenthesis(e):
		return haxe_macro_ExprDef("EParenthesis", 4, [e])

	@staticmethod
	def EObjectDecl(fields):
		return haxe_macro_ExprDef("EObjectDecl", 5, [fields])

	@staticmethod
	def EArrayDecl(values):
		return haxe_macro_ExprDef("EArrayDecl", 6, [values])

	@staticmethod
	def ECall(e,params):
		return haxe_macro_ExprDef("ECall", 7, [e,params])

	@staticmethod
	def ENew(t,params):
		return haxe_macro_ExprDef("ENew", 8, [t,params])

	@staticmethod
	def EUnop(op,postFix,e):
		return haxe_macro_ExprDef("EUnop", 9, [op,postFix,e])

	@staticmethod
	def EVars(vars):
		return haxe_macro_ExprDef("EVars", 10, [vars])

	@staticmethod
	def EFunction(name,f):
		return haxe_macro_ExprDef("EFunction", 11, [name,f])

	@staticmethod
	def EBlock(exprs):
		return haxe_macro_ExprDef("EBlock", 12, [exprs])

	@staticmethod
	def EFor(it,expr):
		return haxe_macro_ExprDef("EFor", 13, [it,expr])

	@staticmethod
	def EIn(e1,e2):
		return haxe_macro_ExprDef("EIn", 14, [e1,e2])

	@staticmethod
	def EIf(econd,eif,eelse):
		return haxe_macro_ExprDef("EIf", 15, [econd,eif,eelse])

	@staticmethod
	def EWhile(econd,e,normalWhile):
		return haxe_macro_ExprDef("EWhile", 16, [econd,e,normalWhile])

	@staticmethod
	def ESwitch(e,cases,edef):
		return haxe_macro_ExprDef("ESwitch", 17, [e,cases,edef])

	@staticmethod
	def ETry(e,catches):
		return haxe_macro_ExprDef("ETry", 18, [e,catches])

	@staticmethod
	def EReturn(e = None):
		return haxe_macro_ExprDef("EReturn", 19, [e])

	@staticmethod
	def EUntyped(e):
		return haxe_macro_ExprDef("EUntyped", 22, [e])

	@staticmethod
	def EThrow(e):
		return haxe_macro_ExprDef("EThrow", 23, [e])

	@staticmethod
	def ECast(e,t):
		return haxe_macro_ExprDef("ECast", 24, [e,t])

	@staticmethod
	def EDisplay(e,isCall):
		return haxe_macro_ExprDef("EDisplay", 25, [e,isCall])

	@staticmethod
	def EDisplayNew(t):
		return haxe_macro_ExprDef("EDisplayNew", 26, [t])

	@staticmethod
	def ETernary(econd,eif,eelse):
		return haxe_macro_ExprDef("ETernary", 27, [econd,eif,eelse])

	@staticmethod
	def ECheckType(e,t):
		return haxe_macro_ExprDef("ECheckType", 28, [e,t])

	@staticmethod
	def EMeta(s,e):
		return haxe_macro_ExprDef("EMeta", 29, [s,e])
haxe_macro_ExprDef.EBreak = haxe_macro_ExprDef("EBreak", 20, list())
haxe_macro_ExprDef.EContinue = haxe_macro_ExprDef("EContinue", 21, list())
haxe_macro_ExprDef._hx_class = haxe_macro_ExprDef
_hx_classes["haxe.macro.ExprDef"] = haxe_macro_ExprDef

class haxe_macro_ComplexType(Enum):
	_hx_class_name = "haxe.macro.ComplexType"
	_hx_constructs = ["TPath", "TFunction", "TAnonymous", "TParent", "TExtend", "TOptional"]

	@staticmethod
	def TPath(p):
		return haxe_macro_ComplexType("TPath", 0, [p])

	@staticmethod
	def TFunction(args,ret):
		return haxe_macro_ComplexType("TFunction", 1, [args,ret])

	@staticmethod
	def TAnonymous(fields):
		return haxe_macro_ComplexType("TAnonymous", 2, [fields])

	@staticmethod
	def TParent(t):
		return haxe_macro_ComplexType("TParent", 3, [t])

	@staticmethod
	def TExtend(p,fields):
		return haxe_macro_ComplexType("TExtend", 4, [p,fields])

	@staticmethod
	def TOptional(t):
		return haxe_macro_ComplexType("TOptional", 5, [t])
haxe_macro_ComplexType._hx_class = haxe_macro_ComplexType
_hx_classes["haxe.macro.ComplexType"] = haxe_macro_ComplexType

class haxe_macro_TypeParam(Enum):
	_hx_class_name = "haxe.macro.TypeParam"
	_hx_constructs = ["TPType", "TPExpr"]

	@staticmethod
	def TPType(t):
		return haxe_macro_TypeParam("TPType", 0, [t])

	@staticmethod
	def TPExpr(e):
		return haxe_macro_TypeParam("TPExpr", 1, [e])
haxe_macro_TypeParam._hx_class = haxe_macro_TypeParam
_hx_classes["haxe.macro.TypeParam"] = haxe_macro_TypeParam

class haxe_macro_Access(Enum):
	_hx_class_name = "haxe.macro.Access"
	_hx_constructs = ["APublic", "APrivate", "AStatic", "AOverride", "ADynamic", "AInline", "AMacro"]
haxe_macro_Access.APublic = haxe_macro_Access("APublic", 0, list())
haxe_macro_Access.APrivate = haxe_macro_Access("APrivate", 1, list())
haxe_macro_Access.AStatic = haxe_macro_Access("AStatic", 2, list())
haxe_macro_Access.AOverride = haxe_macro_Access("AOverride", 3, list())
haxe_macro_Access.ADynamic = haxe_macro_Access("ADynamic", 4, list())
haxe_macro_Access.AInline = haxe_macro_Access("AInline", 5, list())
haxe_macro_Access.AMacro = haxe_macro_Access("AMacro", 6, list())
haxe_macro_Access._hx_class = haxe_macro_Access
_hx_classes["haxe.macro.Access"] = haxe_macro_Access

class haxe_macro_FieldType(Enum):
	_hx_class_name = "haxe.macro.FieldType"
	_hx_constructs = ["FVar", "FFun", "FProp"]

	@staticmethod
	def FVar(t,e = None):
		return haxe_macro_FieldType("FVar", 0, [t,e])

	@staticmethod
	def FFun(f):
		return haxe_macro_FieldType("FFun", 1, [f])

	@staticmethod
	def FProp(get,set,t = None,e= None):
		return haxe_macro_FieldType("FProp", 2, [get,set,t,e])
haxe_macro_FieldType._hx_class = haxe_macro_FieldType
_hx_classes["haxe.macro.FieldType"] = haxe_macro_FieldType

class haxe_macro_TypeDefKind(Enum):
	_hx_class_name = "haxe.macro.TypeDefKind"
	_hx_constructs = ["TDEnum", "TDStructure", "TDClass", "TDAlias", "TDAbstract"]

	@staticmethod
	def TDClass(superClass = None,interfaces= None,isInterface= None):
		return haxe_macro_TypeDefKind("TDClass", 2, [superClass,interfaces,isInterface])

	@staticmethod
	def TDAlias(t):
		return haxe_macro_TypeDefKind("TDAlias", 3, [t])

	@staticmethod
	def TDAbstract(tthis,_hx_from = None,to= None):
		return haxe_macro_TypeDefKind("TDAbstract", 4, [tthis,_hx_from,to])
haxe_macro_TypeDefKind.TDEnum = haxe_macro_TypeDefKind("TDEnum", 0, list())
haxe_macro_TypeDefKind.TDStructure = haxe_macro_TypeDefKind("TDStructure", 1, list())
haxe_macro_TypeDefKind._hx_class = haxe_macro_TypeDefKind
_hx_classes["haxe.macro.TypeDefKind"] = haxe_macro_TypeDefKind


class haxe_macro_Error:
	_hx_class_name = "haxe.macro.Error"
	_hx_fields = ["message", "pos"]
	_hx_methods = ["toString"]

	def __init__(self,m,p):
		# /opt/haxe-git/std/haxe/macro/Expr.hx:327
		self.message = None
		# /opt/haxe-git/std/haxe/macro/Expr.hx:328
		self.pos = None
		# /opt/haxe-git/std/haxe/macro/Expr.hx:330
		self.message = m
		# /opt/haxe-git/std/haxe/macro/Expr.hx:331
		self.pos = p

	def toString(self):
		# /opt/haxe-git/std/haxe/macro/Expr.hx:334
		return self.message

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.message = None
		_hx_o.pos = None
haxe_macro_Error._hx_class = haxe_macro_Error
_hx_classes["haxe.macro.Error"] = haxe_macro_Error

class haxe_macro_ImportMode(Enum):
	_hx_class_name = "haxe.macro.ImportMode"
	_hx_constructs = ["INormal", "IAsName", "IAll"]

	@staticmethod
	def IAsName(alias):
		return haxe_macro_ImportMode("IAsName", 1, [alias])
haxe_macro_ImportMode.INormal = haxe_macro_ImportMode("INormal", 0, list())
haxe_macro_ImportMode.IAll = haxe_macro_ImportMode("IAll", 2, list())
haxe_macro_ImportMode._hx_class = haxe_macro_ImportMode
_hx_classes["haxe.macro.ImportMode"] = haxe_macro_ImportMode


class hxsublime_HaxeImportGenerator:
	_hx_class_name = "hxsublime.HaxeImportGenerator"
	_hx_fields = ["panel", "start", "size", "cname", "view"]
	_hx_methods = ["getEnd", "getStart", "isMemberName", "getClassName", "compactClassName", "getIndent", "insertStatement", "generateStatement"]
	_hx_statics = ["generateUsing", "generateImport"]

	def __init__(self,panel,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:33
		self.panel = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:34
		self.start = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:35
		self.size = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:36
		self.cname = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:39
		self.view = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:43
		self.view = view
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:44
		self.panel = panel
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:45
		self.start = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:46
		self.size = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:47
		self.cname = None

	def getEnd(self,src,offset):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:52
		end = len(src)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:53
		while (offset < end):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:55
			c = None
			if ((offset < 0) or ((offset >= len(src)))):
				c = ""
			else:
				c = src[offset]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:56
			offset = (offset + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:57
			if (hxsublime_tools_Regex.word_chars.match(c) is None):
				break
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:59
		return (offset - 1)

	def getStart(self,src,offset):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:64
		found_word = 0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:65
		offset = (offset - 1)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:66
		while (offset > 0):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:68
			c = None
			if ((offset < 0) or ((offset >= len(src)))):
				c = ""
			else:
				c = src[offset]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:69
			offset = (offset - 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:70
			if (found_word == 0):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:72
				if (hxsublime_tools_Regex.space_chars.match(c) is not None):
					continue
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:73
				found_word = 1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:75
			if (hxsublime_tools_Regex.word_chars.match(c) is None):
				break
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:78
		return (offset + 2)

	def isMemberName(self,token):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:83
		return (((("" if ((0 >= len(token))) else token[0])) >= "Z") or ((token == token.upper())))

	def getClassName(self,view,src):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:88
		loc = view.sel()[0]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:89
		end = python_lib_Builtins.max(loc.a,loc.b)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:90
		self.size = loc.size()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:91
		if (self.size == 0):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:93
			end = self.getEnd(src,end)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:94
			self.start = self.getStart(src,end)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:95
			self.size = (end - self.start)
		else:
			self.start = (end - self.size)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:102
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:102
		s = view.substr(sublime_Region(self.start, end))
		self.cname = s.rpartition(".")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:104
		while ((not ((self.cname[0] == ""))) and self.isMemberName(self.cname[2])):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:106
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:106
			_hx_local_0 = self
			_hx_local_1 = _hx_local_0.size
			_hx_local_0.size = (_hx_local_1 - ((1 + len(self.cname[2]))))
			_hx_local_0.size
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:107
			self.cname = self.cname[0].rpartition(".")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:110
		return self.cname

	def compactClassName(self,edit,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:115
		view.replace(edit,sublime_Region(self.start, (self.start + self.size)),self.cname[2])
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:116
		view.sel().clear()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:117
		loc = (self.start + len(self.cname[2]))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:118
		view.sel().add(sublime_Region(loc, loc))

	def getIndent(self,src,index):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:124
		if ((("" if (((index < 0) or ((index >= len(src))))) else src[index])) == "\n"):
			return (index + 1)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:125
		return index

	def insertStatement(self,edit,view,src,statement,regex):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:130
		cname = ((HxOverrides.stringOrNull(self.cname[0]) + HxOverrides.stringOrNull(self.cname[1])) + HxOverrides.stringOrNull(self.cname[2]))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:131
		clow = cname.lower()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:132
		last = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:134
		def _hx_local_0():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:134
			this1 = regex.finditer(src)
			return python_HaxeIterator(this1)
		_hx_local_2 = _hx_local_0()
		while _hx_local_2.hasNext():
			imp = _hx_local_2.next()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:136
			def _hx_local_1():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:136
				_this = imp.group(2)
				return _this.lower()
			if (clow < _hx_local_1()):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:139
				ins = hxsublime_support_StringTools.format("{0}{1} {2};\n",[imp.group(1), statement, cname])
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:140
				view.insert(edit,self.getIndent(src,imp.start(0)),ins)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:141
				return
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:143
			last = imp
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:146
		if (last is not None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:148
			haxe_Log.trace(last,_hx_AnonObject({'fileName': "Codegen.hx", 'lineNumber': 148, 'className': "hxsublime.HaxeImportGenerator", 'methodName': "insertStatement"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:149
			ins1 = hxsublime_support_StringTools.format(";\n{0}{1} {2}",[last.group(1), statement, cname])
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:150
			view.insert(edit,last.end(2),ins1)
		else:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:154
			pkg = hxsublime_tools_Regex.package_line.search(src)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:155
			if (pkg is not None):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:157
				ins2 = hxsublime_support_StringTools.format("\n\n{0} {1};",[statement, cname])
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:158
				view.insert(edit,pkg.end(0),ins2)
			else:
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:162
				ins3 = hxsublime_support_StringTools.format("{0} {1};\n\n",[statement, cname])
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:163
				view.insert(edit,0,ins3)

	def generateStatement(self,edit,statement,regex):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:171
		view = self.view
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:172
		src = view.substr(sublime_Region(0, view.size()))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:173
		cname = self.getClassName(view,src)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:175
		if ((cname[1] == "") and ((statement == "import"))):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:177
			sublime_Sublime.status_message(("Nothing to " + ("null" if statement is None else statement)))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:178
			self.panel.writeln(("Nothing to " + ("null" if statement is None else statement)))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:179
			return
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:182
		self.compactClassName(edit,view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:184
		fcname = ((HxOverrides.stringOrNull(cname[0]) + HxOverrides.stringOrNull(cname[1])) + HxOverrides.stringOrNull(cname[2]))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:186
		if (python_lib_Re.search((("null" if statement is None else statement) + "\\s+${fcname};"),src) is not None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:188
			info = None
			if (statement == "import"):
				info = "imported"
			else:
				info = "used"
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:189
			sublime_Sublime.status_message(("Already " + ("null" if info is None else info)))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:190
			self.panel.writeln(("Already " + ("null" if info is None else info)))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:191
			return
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:194
		self.insertStatement(edit,view,src,statement,regex)

	@staticmethod
	def generateUsing(view,edit):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:23
		p = hxsublime_HaxeImportGenerator(hxsublime_panel_Panels.defaultPanel(), view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:24
		p.generateStatement(edit,"using",hxsublime_tools_Regex.using_line)
		return

	@staticmethod
	def generateImport(view,edit):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:29
		p = hxsublime_HaxeImportGenerator(hxsublime_panel_Panels.defaultPanel(), view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Codegen.hx:30
		p.generateStatement(edit,"import",hxsublime_tools_Regex.import_line)
		return

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.panel = None
		_hx_o.start = None
		_hx_o.size = None
		_hx_o.cname = None
		_hx_o.view = None
hxsublime_HaxeImportGenerator._hx_class = hxsublime_HaxeImportGenerator
_hx_classes["hxsublime.HaxeImportGenerator"] = hxsublime_HaxeImportGenerator


class hxsublime_NmeTarget:
	_hx_class_name = "hxsublime.NmeTarget"
	_hx_fields = ["name", "plattform", "args"]

	def __init__(self,name,plattform,args):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Config.hx:102
		self.name = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Config.hx:103
		self.plattform = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Config.hx:104
		self.args = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Config.hx:108
		self.name = name
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Config.hx:109
		self.plattform = plattform
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Config.hx:110
		self.args = args

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.name = None
		_hx_o.plattform = None
		_hx_o.args = None
hxsublime_NmeTarget._hx_class = hxsublime_NmeTarget
_hx_classes["hxsublime.NmeTarget"] = hxsublime_NmeTarget


class hxsublime_OpenFlTarget:
	_hx_class_name = "hxsublime.OpenFlTarget"
	_hx_fields = ["name", "plattform", "args"]

	def __init__(self,name,plattform,args):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Config.hx:116
		self.name = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Config.hx:117
		self.plattform = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Config.hx:118
		self.args = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Config.hx:122
		self.name = name
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Config.hx:123
		self.plattform = plattform
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Config.hx:124
		self.args = args

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.name = None
		_hx_o.plattform = None
		_hx_o.args = None
hxsublime_OpenFlTarget._hx_class = hxsublime_OpenFlTarget
_hx_classes["hxsublime.OpenFlTarget"] = hxsublime_OpenFlTarget


class hxsublime_Config:
	_hx_class_name = "hxsublime.Config"
	_hx_statics = ["target_packages", "targets", "target_std_packages", "ignored_folders_list", "mk_ignored_folders", "ignored_folders", "ignored_packages_list", "mk_ignored_packages", "ignored_packages", "ignored_types", "nme_targets", "openfl_targets", "SOURCE_HAXE", "SOURCE_HXML", "SOURCE_NMML", "SOURCE_ERAZOR", "HXSL_SUFFIX"]

	@staticmethod
	def mk_ignored_folders():
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Config.hx:25
		x = haxe_ds_StringMap()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Config.hx:26
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Config.hx:26
		_g = 0
		_g1 = hxsublime_Config.ignored_folders_list
		while (_g < len(_g1)):
			p = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Config.hx:27
			x.h[p] = True
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Config.hx:24
		return x

	@staticmethod
	def mk_ignored_packages():
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Config.hx:37
		x = haxe_ds_StringMap()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Config.hx:38
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Config.hx:38
		_g = 0
		_g1 = hxsublime_Config.ignored_folders_list
		while (_g < len(_g1)):
			p = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Config.hx:39
			x.h[p] = True
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Config.hx:36
		return x
hxsublime_Config._hx_class = hxsublime_Config
_hx_classes["hxsublime.Config"] = hxsublime_Config


class hxsublime_ExtractBuildPathException(Exception):
	_hx_class_name = "hxsublime.ExtractBuildPathException"
	_hx_fields = []
	_hx_methods = []
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = Exception


	def __init__(self,build):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Exceptions.hx:9
		super().__init__(("Cannot ExtractBuildPath from build " + Std.string(build)))
hxsublime_ExtractBuildPathException._hx_class = hxsublime_ExtractBuildPathException
_hx_classes["hxsublime.ExtractBuildPathException"] = hxsublime_ExtractBuildPathException


class hxsublime_GetRelativePathException(Exception):
	_hx_class_name = "hxsublime.GetRelativePathException"
	_hx_fields = []
	_hx_methods = []
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = Exception


	def __init__(self,build,file):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Exceptions.hx:17
		super().__init__(((("Cannot get the relative path of " + Std.string(file)) + " for build ") + Std.string(build)))
hxsublime_GetRelativePathException._hx_class = hxsublime_GetRelativePathException
_hx_classes["hxsublime.GetRelativePathException"] = hxsublime_GetRelativePathException


class hxsublime_CreateTempFileOrFolderException(Exception):
	_hx_class_name = "hxsublime.CreateTempFileOrFolderException"
	_hx_fields = []
	_hx_methods = []
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = Exception


	def __init__(self,build,file_or_folder):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Exceptions.hx:26
		super().__init__((((("Cannot create temp file or folder (" + Std.string(file_or_folder)) + ") from build (") + Std.string(build)) + ")"))
hxsublime_CreateTempFileOrFolderException._hx_class = hxsublime_CreateTempFileOrFolderException
_hx_classes["hxsublime.CreateTempFileOrFolderException"] = hxsublime_CreateTempFileOrFolderException


class hxsublime_Execute:
	_hx_class_name = "hxsublime.Execute"
	_hx_statics = ["runCmdAsync", "runCmd"]

	@staticmethod
	def runCmdAsync(args,callback,input = None,cwd = None,env = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:22
		def _hx_local_2():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:23
			r = hxsublime_Execute.runCmd(args,input,cwd,env)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:24
			out = r[0]
			err = r[1]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:25
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:25
				f = callback
				a1 = out
				a2 = err
				def _hx_local_1():
					f(a1,a2)
				return _hx_local_1
			sublime_Sublime.set_timeout(_hx_local_0(),1)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:21
		inMainThread = _hx_local_2
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:27
		python_lib_ThreadLowLevel.start_new_thread(inMainThread,tuple())

	@staticmethod
	def runCmd(args,input = None,cwd = None,env = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:32
		if (cwd is None):
			cwd = "."
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:36
		try:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:38
			base_env = python_lib_Os.environ.copy()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:40
			if (env is not None):
				base_env.update(env)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:45
			env1 = base_env
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:47
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:47
				this1 = None
				_this = env1.keys()
				this1 = iter(_this)
				return python_HaxeIterator(this1)
			_hx_local_1 = _hx_local_0()
			while _hx_local_1.hasNext():
				k = _hx_local_1.next()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:49
				val = env1.get(k,None)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:50
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:50
				val1 = python_lib_os_Path.expandvars(val)
				env1[k] = val1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:54
			def _hx_local_2(s):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:54
				return (s != "")
			cmdArgs = list(filter(_hx_local_2,args))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:56
			p = None
			o = _hx_AnonObject({'cwd': cwd, 'stdout': python_lib_Subprocess.PIPE, 'stderr': python_lib_Subprocess.PIPE, 'stdin': python_lib_Subprocess.PIPE, 'startupinfo': hxsublime_Plugin.startupInfo(), 'env': env1})
			if hasattr(o,(("_hx_" + "bufsize") if ("bufsize" in python_Boot.keywords) else (("_hx_" + "bufsize") if (((((len("bufsize") > 2) and ((ord("bufsize"[0]) == 95))) and ((ord("bufsize"[1]) == 95))) and ((ord("bufsize"[(len("bufsize") - 1)]) != 95)))) else "bufsize"))):
				Reflect.setField(o,"bufsize",Reflect.field(o,"bufsize"))
			else:
				Reflect.setField(o,"bufsize",0)
			if hasattr(o,(("_hx_" + "executable") if ("executable" in python_Boot.keywords) else (("_hx_" + "executable") if (((((len("executable") > 2) and ((ord("executable"[0]) == 95))) and ((ord("executable"[1]) == 95))) and ((ord("executable"[(len("executable") - 1)]) != 95)))) else "executable"))):
				Reflect.setField(o,"executable",Reflect.field(o,"executable"))
			else:
				Reflect.setField(o,"executable",None)
			if hasattr(o,(("_hx_" + "stdin") if ("stdin" in python_Boot.keywords) else (("_hx_" + "stdin") if (((((len("stdin") > 2) and ((ord("stdin"[0]) == 95))) and ((ord("stdin"[1]) == 95))) and ((ord("stdin"[(len("stdin") - 1)]) != 95)))) else "stdin"))):
				Reflect.setField(o,"stdin",Reflect.field(o,"stdin"))
			else:
				Reflect.setField(o,"stdin",None)
			if hasattr(o,(("_hx_" + "stdout") if ("stdout" in python_Boot.keywords) else (("_hx_" + "stdout") if (((((len("stdout") > 2) and ((ord("stdout"[0]) == 95))) and ((ord("stdout"[1]) == 95))) and ((ord("stdout"[(len("stdout") - 1)]) != 95)))) else "stdout"))):
				Reflect.setField(o,"stdout",Reflect.field(o,"stdout"))
			else:
				Reflect.setField(o,"stdout",None)
			if hasattr(o,(("_hx_" + "stderr") if ("stderr" in python_Boot.keywords) else (("_hx_" + "stderr") if (((((len("stderr") > 2) and ((ord("stderr"[0]) == 95))) and ((ord("stderr"[1]) == 95))) and ((ord("stderr"[(len("stderr") - 1)]) != 95)))) else "stderr"))):
				Reflect.setField(o,"stderr",Reflect.field(o,"stderr"))
			else:
				Reflect.setField(o,"stderr",None)
			if hasattr(o,(("_hx_" + "preexec_fn") if ("preexec_fn" in python_Boot.keywords) else (("_hx_" + "preexec_fn") if (((((len("preexec_fn") > 2) and ((ord("preexec_fn"[0]) == 95))) and ((ord("preexec_fn"[1]) == 95))) and ((ord("preexec_fn"[(len("preexec_fn") - 1)]) != 95)))) else "preexec_fn"))):
				Reflect.setField(o,"preexec_fn",Reflect.field(o,"preexec_fn"))
			else:
				Reflect.setField(o,"preexec_fn",None)
			if hasattr(o,(("_hx_" + "close_fds") if ("close_fds" in python_Boot.keywords) else (("_hx_" + "close_fds") if (((((len("close_fds") > 2) and ((ord("close_fds"[0]) == 95))) and ((ord("close_fds"[1]) == 95))) and ((ord("close_fds"[(len("close_fds") - 1)]) != 95)))) else "close_fds"))):
				Reflect.setField(o,"close_fds",Reflect.field(o,"close_fds"))
			else:
				Reflect.setField(o,"close_fds",None)
			if hasattr(o,(("_hx_" + "shell") if ("shell" in python_Boot.keywords) else (("_hx_" + "shell") if (((((len("shell") > 2) and ((ord("shell"[0]) == 95))) and ((ord("shell"[1]) == 95))) and ((ord("shell"[(len("shell") - 1)]) != 95)))) else "shell"))):
				Reflect.setField(o,"shell",Reflect.field(o,"shell"))
			else:
				Reflect.setField(o,"shell",None)
			if hasattr(o,(("_hx_" + "cwd") if ("cwd" in python_Boot.keywords) else (("_hx_" + "cwd") if (((((len("cwd") > 2) and ((ord("cwd"[0]) == 95))) and ((ord("cwd"[1]) == 95))) and ((ord("cwd"[(len("cwd") - 1)]) != 95)))) else "cwd"))):
				Reflect.setField(o,"cwd",Reflect.field(o,"cwd"))
			else:
				Reflect.setField(o,"cwd",None)
			if hasattr(o,(("_hx_" + "env") if ("env" in python_Boot.keywords) else (("_hx_" + "env") if (((((len("env") > 2) and ((ord("env"[0]) == 95))) and ((ord("env"[1]) == 95))) and ((ord("env"[(len("env") - 1)]) != 95)))) else "env"))):
				Reflect.setField(o,"env",Reflect.field(o,"env"))
			else:
				Reflect.setField(o,"env",None)
			if hasattr(o,(("_hx_" + "universal_newlines") if ("universal_newlines" in python_Boot.keywords) else (("_hx_" + "universal_newlines") if (((((len("universal_newlines") > 2) and ((ord("universal_newlines"[0]) == 95))) and ((ord("universal_newlines"[1]) == 95))) and ((ord("universal_newlines"[(len("universal_newlines") - 1)]) != 95)))) else "universal_newlines"))):
				Reflect.setField(o,"universal_newlines",Reflect.field(o,"universal_newlines"))
			else:
				Reflect.setField(o,"universal_newlines",None)
			if hasattr(o,(("_hx_" + "startupinfo") if ("startupinfo" in python_Boot.keywords) else (("_hx_" + "startupinfo") if (((((len("startupinfo") > 2) and ((ord("startupinfo"[0]) == 95))) and ((ord("startupinfo"[1]) == 95))) and ((ord("startupinfo"[(len("startupinfo") - 1)]) != 95)))) else "startupinfo"))):
				Reflect.setField(o,"startupinfo",Reflect.field(o,"startupinfo"))
			else:
				Reflect.setField(o,"startupinfo",None)
			if hasattr(o,(("_hx_" + "creationflags") if ("creationflags" in python_Boot.keywords) else (("_hx_" + "creationflags") if (((((len("creationflags") > 2) and ((ord("creationflags"[0]) == 95))) and ((ord("creationflags"[1]) == 95))) and ((ord("creationflags"[(len("creationflags") - 1)]) != 95)))) else "creationflags"))):
				Reflect.setField(o,"creationflags",Reflect.field(o,"creationflags"))
			else:
				Reflect.setField(o,"creationflags",0)
			if (Sys.systemName() == "Windows"):
				p = python_lib_subprocess_Popen(cmdArgs, Reflect.field(o,"bufsize"), Reflect.field(o,"executable"), Reflect.field(o,"stdin"), Reflect.field(o,"stdout"), Reflect.field(o,"stderr"), Reflect.field(o,"preexec_fn"), Reflect.field(o,"close_fds"), Reflect.field(o,"shell"), Reflect.field(o,"cwd"), Reflect.field(o,"env"), Reflect.field(o,"universal_newlines"), Reflect.field(o,"startupinfo"), Reflect.field(o,"creationflags"))
			else:
				p = python_lib_subprocess_Popen(cmdArgs, Reflect.field(o,"bufsize"), Reflect.field(o,"executable"), Reflect.field(o,"stdin"), Reflect.field(o,"stdout"), Reflect.field(o,"stderr"), Reflect.field(o,"preexec_fn"), Reflect.field(o,"close_fds"), Reflect.field(o,"shell"), Reflect.field(o,"cwd"), Reflect.field(o,"env"), Reflect.field(o,"universal_newlines"), Reflect.field(o,"startupinfo"))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:58
			inputBytes = None
			if (input is not None):
				inputBytes = hxsublime_support_StringTools.encode(input,"utf-8")
			else:
				inputBytes = None
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:60
			r = p.communicate(inputBytes)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:61
			out = r[0]
			err = r[1]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:64
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:64
			a = out.decode("utf-8")
			b = err.decode("utf-8")
			return (a, b)
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			e = _hx_e1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:68
			haxe_Log.trace(e,_hx_AnonObject({'fileName': "Execute.hx", 'lineNumber': 68, 'className': "hxsublime.Execute", 'methodName': "runCmd"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:69
			p1 = (args[0] if 0 < len(args) else None)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:70
			err1 = (((((("Error while running " + ("null" if p1 is None else p1)) + ": in ") + ("null" if cwd is None else cwd)) + " (") + Std.string(e)) + ")")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Execute.hx:71
			return ("", err1)
hxsublime_Execute._hx_class = hxsublime_Execute
_hx_classes["hxsublime.Execute"] = hxsublime_Execute


class hxsublime_HaxeLibLibrary:
	_hx_class_name = "hxsublime.HaxeLibLibrary"
	_hx_fields = ["name", "dev", "version", "classes", "packages", "path"]
	_hx_methods = ["as_cmd_arg", "extract_types"]

	def __init__(self,manager,name,dev,version):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:18
		self.name = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:19
		self.dev = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:20
		self.version = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:21
		self.classes = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:22
		self.packages = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:23
		self.path = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:27
		self.name = name
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:28
		self.dev = dev
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:29
		self.version = version
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:30
		self.classes = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:31
		self.packages = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:33
		if dev:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:34
			self.path = version
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:35
			self.version = "dev"
		else:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:37
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:37
				_this = None
				_this1 = self.version
				_this = _this1.split(".")
				return ",".join([python_Boot.toString1(x1,'') for x1 in _this])
			self.path = python_lib_os_Path.join(manager.basePath,name,_hx_local_0())

	def as_cmd_arg(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:44
		return ((HxOverrides.stringOrNull(self.name) + ":") + HxOverrides.stringOrNull(self.version))

	def extract_types(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:49
		if (self.dev or (((self.classes is None) and ((self.packages is None))))):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:50
			t = hxsublime_Types.extractTypes(self.path)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:51
			self.classes = t.allTypes()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:52
			self.packages = t.packs()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:55
		return (self.classes, self.packages)

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.name = None
		_hx_o.dev = None
		_hx_o.version = None
		_hx_o.classes = None
		_hx_o.packages = None
		_hx_o.path = None
hxsublime_HaxeLibLibrary._hx_class = hxsublime_HaxeLibLibrary
_hx_classes["hxsublime.HaxeLibLibrary"] = hxsublime_HaxeLibLibrary


class hxsublime_HaxeLibManager:
	_hx_class_name = "hxsublime.HaxeLibManager"
	_hx_fields = ["_available", "project", "basePath", "scanned"]
	_hx_methods = ["available", "get", "getCompletions", "scan", "installLib", "removeLib", "upgradeAll", "selfUpdate", "searchLibs", "parseLibraries", "isLibInstalled", "getLib"]
	_hx_statics = ["__meta__", "libLine"]

	def __init__(self,project):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:67
		self._available = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:69
		self.project = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:71
		self.basePath = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:73
		self.scanned = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:76
		self._available = haxe_ds_StringMap()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:77
		self.basePath = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:78
		self.scanned = False
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:79
		self.project = project

	def available(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:85
		if (not self.scanned):
			self.scan()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:88
		return self._available

	def get(self,name):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:92
		def _hx_local_0():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:92
			_this = self.available()
			return name in _this.h
		if _hx_local_0():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:93
			_this1 = self.available()
			return _this1.h.get(name,None)
		else:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:95
			sublime_Sublime.status_message((("Haxelib : " + ("null" if name is None else name)) + " project not installed"))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:96
			return None

	def getCompletions(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:102
		comps = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:103
		_hx_local_0 = self.available().keys()
		while _hx_local_0.hasNext():
			k = _hx_local_0.next()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:105
			lib = None
			_this = self.available()
			lib = _this.h.get(k,None)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:106
			haxe_Log.trace(lib,_hx_AnonObject({'fileName': "Haxelib.hx", 'lineNumber': 106, 'className': "hxsublime.HaxeLibManager", 'methodName': "getCompletions"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:107
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:107
			x = ((((HxOverrides.stringOrNull(lib.name) + " [") + HxOverrides.stringOrNull(lib.version)) + "]"), lib.name)
			comps.append(x)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:110
		return comps

	def scan(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:117
		self.scanned = True
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:118
		env = self.project.haxeEnv()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:119
		cmd = self.project.haxelibExec()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:120
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:120
		cmd.append("config")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:121
		r = hxsublime_Execute.runCmd(cmd,None,None,env)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:122
		hlout = r[0]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:123
		hlerr = r[1]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:124
		self.basePath = hlout.strip(None)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:126
		self._available = haxe_ds_StringMap()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:128
		cmd1 = self.project.haxelibExec()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:129
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:129
		cmd1.append("list")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:131
		r1 = hxsublime_Execute.runCmd(cmd1,None,None,env)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:132
		hlout1 = r1[0]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:133
		hlerr1 = r1[1]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:136
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:136
		_g = 0
		_g1 = hlout1.split("\n")
		while (_g < len(_g1)):
			l = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:138
			found = hxsublime_HaxeLibManager.libLine.match(l)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:139
			if (found is not None):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:141
				g = found.groups(None)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:142
				if (g is not None):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:144
					name = g[0]
					dev = g[1]
					version = g[2]
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:145
					lib = hxsublime_HaxeLibLibrary(self, name, (dev is not None), version)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:147
					self._available.h[name] = lib

	def installLib(self,lib):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:155
		cmd = self.project.haxelibExec()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:156
		env = self.project.haxeEnv()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:157
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:157
		cmd.append("install")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:158
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:158
		cmd.append(lib)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:159
		haxe_Log.trace(Std.string(cmd),_hx_AnonObject({'fileName': "Haxelib.hx", 'lineNumber': 159, 'className': "hxsublime.HaxeLibManager", 'methodName': "installLib"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:160
		hxsublime_Execute.runCmd(cmd,None,None,env)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:161
		self.scan()

	def removeLib(self,lib):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:166
		cmd = self.project.haxelibExec()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:167
		env = self.project.haxeEnv()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:168
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:168
		cmd.append("remove")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:169
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:169
		cmd.append(lib)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:170
		haxe_Log.trace(Std.string(cmd),_hx_AnonObject({'fileName': "Haxelib.hx", 'lineNumber': 170, 'className': "hxsublime.HaxeLibManager", 'methodName': "removeLib"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:171
		hxsublime_Execute.runCmd(cmd,None,None,env)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:172
		self.scan()

	def upgradeAll(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:177
		cmd = self.project.haxelibExec()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:178
		env = self.project.haxeEnv()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:179
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:179
		cmd.append("upgrade")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:180
		haxe_Log.trace(Std.string(cmd),_hx_AnonObject({'fileName': "Haxelib.hx", 'lineNumber': 180, 'className': "hxsublime.HaxeLibManager", 'methodName': "upgradeAll"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:181
		hxsublime_Execute.runCmd(cmd,None,None,env)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:182
		self.scan()

	def selfUpdate(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:187
		cmd = self.project.haxelibExec()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:188
		env = self.project.haxeEnv()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:189
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:189
		cmd.append("thisupdate")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:190
		haxe_Log.trace(Std.string(cmd),_hx_AnonObject({'fileName': "Haxelib.hx", 'lineNumber': 190, 'className': "hxsublime.HaxeLibManager", 'methodName': "selfUpdate"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:191
		hxsublime_Execute.runCmd(cmd,None,None,env)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:192
		self.scan()

	def searchLibs(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:197
		cmd = self.project.haxelibExec()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:198
		env = self.project.haxeEnv()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:199
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:199
		cmd.append("search")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:200
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:200
		cmd.append("_")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:202
		res = hxsublime_Execute.runCmd(cmd,None,None,env)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:203
		out = res[0]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:204
		err = res[1]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:205
		return self.parseLibraries(out)

	def parseLibraries(self,out):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:210
		x = None
		_this = out.split("\n")
		def _hx_local_0(x1):
			return ((x1 != "") and ((x1.find("libraries found") == -1)))
		x = list(filter(_hx_local_0,_this))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:211
		x.reverse()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:212
		return x

	def isLibInstalled(self,lib):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:217
		_this = self.available()
		return lib in _this.h

	def getLib(self,lib):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Haxelib.hx:222
		_this = self.available()
		return _this.h.get(lib,None)

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o._available = None
		_hx_o.project = None
		_hx_o.basePath = None
		_hx_o.scanned = None
hxsublime_HaxeLibManager._hx_class = hxsublime_HaxeLibManager
_hx_classes["hxsublime.HaxeLibManager"] = hxsublime_HaxeLibManager


class hxsublime_Log:
	_hx_class_name = "hxsublime.Log"
	_hx_statics = ["debug", "log"]

	@staticmethod
	def debug(msg):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Log.hx:12
		hxsublime_Log.log(msg,False)

	@staticmethod
	def log(msg,to_file = False):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Log.hx:16
		if (to_file is None):
			to_file = False
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Log.hx:17
		msgStr = Std.string(msg)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Log.hx:18
		if to_file:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Log.hx:20
			f = None
			def _hx_local_0():
				_hx_local_0 = python_lib_Codecs.open("st3_haxe_log.txt","ab","utf-8","ignore")
				if Std._hx_is(_hx_local_0,python_lib_io_TextIOBase):
					_hx_local_0
				else:
					raise _HxException("Class cast error")
				return _hx_local_0
			f = _hx_local_0()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Log.hx:21
			f.write((("null" if msgStr is None else msgStr) + "\n"))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Log.hx:22
			f.close()
		else:
			try:
				haxe_Log.trace(msgStr,_hx_AnonObject({'fileName': "Log.hx", 'lineNumber': 26, 'className': "hxsublime.Log", 'methodName': "log"}))
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				pass
hxsublime_Log._hx_class = hxsublime_Log
_hx_classes["hxsublime.Log"] = hxsublime_Log


class hxsublime_Main:
	_hx_class_name = "hxsublime.Main"
	_hx_statics = ["main"]

	@staticmethod
	def main():
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Main.hx:61
		def _hx_local_0(msg,pos = None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Main.hx:62
			prefix = ((HxOverrides.stringOrNull(pos.fileName) + ":") + Std.string(pos.lineNumber))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Main.hx:63
			python_lib_Builtins.print(((("null" if prefix is None else prefix) + ":") + Std.string(msg)))
		haxe_Log.trace = _hx_local_0
hxsublime_Main._hx_class = hxsublime_Main
_hx_classes["hxsublime.Main"] = hxsublime_Main


class hxsublime_Plugin:
	_hx_class_name = "hxsublime.Plugin"
	_hx_statics = ["_startupInfo", "plugin_base_dir", "startupInfo"]

	@staticmethod
	def plugin_base_dir():
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Plugin.hx:13
		return python_lib_os_Path.abspath(python_lib_os_Path.join(python_lib_os_Path.dirname(__file__),"."))

	@staticmethod
	def startupInfo():
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Plugin.hx:18
		if (hxsublime_Plugin._startupInfo is not None):
			return hxsublime_Plugin._startupInfo
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Plugin.hx:19
		try:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Plugin.hx:20
			hxsublime_Plugin._startupInfo = python_lib_Subprocess.STARTUPINFO()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Plugin.hx:21
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Plugin.hx:21
			_hx_local_0 = hxsublime_Plugin._startupInfo
			_hx_local_1 = _hx_local_0.dwFlags
			_hx_local_0.dwFlags = (_hx_local_1 | python_lib_Subprocess.STARTF_USESHOWWINDOW)
			_hx_local_0.dwFlags
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Plugin.hx:22
			hxsublime_Plugin._startupInfo.wShowWindow = python_lib_Subprocess.SW_HIDE
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			if isinstance(_hx_e1, AttributeError):
				e = _hx_e1
				hxsublime_Plugin._startupInfo = None
			else:
				raise _hx_e
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Plugin.hx:27
		return hxsublime_Plugin._startupInfo
hxsublime_Plugin._hx_class = hxsublime_Plugin
_hx_classes["hxsublime.Plugin"] = hxsublime_Plugin


class hxsublime_Settings:
	_hx_class_name = "hxsublime.Settings"
	_hx_statics = ["pluginSettings", "getFromSettings", "get", "getBool", "getInt", "getString", "noFuzzyCompletion", "topLevelCompletionsOnDemand", "showOnlyAsyncCompletions", "isAsyncCompletion", "getCompletionDelays", "showCompletionTimes", "haxeExec", "useHaxeServermode", "useHaxeServermodeWrapper", "haxeSdkPath", "openWithDefaultApp", "haxeInstPath", "nekoInstPath", "haxeLibraryPath", "haxelibExec", "smartSnippets", "smartSnippetsOnCompletion", "smartSnippetsJustCurrent", "checkOnSave", "useSlidePanel", "useHaxeServermodeForBuilds", "useOffsetCompletion"]

	@staticmethod
	def pluginSettings():
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:13
		return sublime_Sublime.load_settings("Haxe.sublime-settings")

	@staticmethod
	def getFromSettings(id,settings,plugin):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:18
		prefix = None
		if plugin:
			prefix = "plugin_"
		else:
			prefix = ""
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:19
		res = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:20
		pf = sublime_Sublime.platform()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:21
		if settings.has((((("null" if prefix is None else prefix) + ("null" if id is None else id)) + "_") + ("null" if pf is None else pf))):
			res = settings.get((((("null" if prefix is None else prefix) + ("null" if id is None else id)) + "_") + ("null" if pf is None else pf)))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:25
		if ((res is None) and settings.has((("null" if prefix is None else prefix) + ("null" if id is None else id)))):
			res = settings.get((("null" if prefix is None else prefix) + ("null" if id is None else id)))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:29
		return res

	@staticmethod
	def get(id,view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:34
		if (view is None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:36
			win = sublime_Sublime.active_window()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:37
			if (win is not None):
				view = sublime_Sublime.active_window().active_view()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:43
		res = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:44
		if (view is not None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:46
			settings = view.settings()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:47
			res = hxsublime_Settings.getFromSettings(id,settings,False)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:50
		if (res is None):
			res = hxsublime_Settings.getFromSettings(id,hxsublime_Settings.pluginSettings(),True)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:55
		return res

	@staticmethod
	def getBool(id,defaultVal,view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:60
		r = hxsublime_Settings.get(id,view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:62
		if (r is None):
			return defaultVal
		elif Std._hx_is(r,Bool):
			return r
		else:
			return defaultVal

	@staticmethod
	def getInt(id,defaultVal,view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:70
		r = hxsublime_Settings.get(id,view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:72
		if (r is None):
			return defaultVal
		elif Std._hx_is(r,Int):
			return r
		else:
			return defaultVal

	@staticmethod
	def getString(id,defaultVal,view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:79
		r = hxsublime_Settings.get(id,view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:81
		if (r is None):
			return defaultVal
		elif Std._hx_is(r,str):
			return r
		else:
			return defaultVal

	@staticmethod
	def noFuzzyCompletion(view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:88
		return hxsublime_Settings.getBool("haxe_completion_no_fuzzy",False,view)

	@staticmethod
	def topLevelCompletionsOnDemand(view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:93
		return hxsublime_Settings.getBool("haxe_completions_top_level_only_on_demand",False,view)

	@staticmethod
	def showOnlyAsyncCompletions(view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:98
		return hxsublime_Settings.getBool("haxe_completions_show_only_async",True,view)

	@staticmethod
	def isAsyncCompletion(view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:103
		return hxsublime_Settings.getBool("haxe_completion_async",True,view)

	@staticmethod
	def getCompletionDelays(view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:109
		a = hxsublime_Settings.getInt("haxe_completion_async_timing_hide",60,view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:110
		b = hxsublime_Settings.getInt("haxe_completion_async_timing_show",150,view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:108
		return (a, b)

	@staticmethod
	def showCompletionTimes(view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:116
		return hxsublime_Settings.getBool("haxe_completion_show_times",False,view)

	@staticmethod
	def haxeExec(view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:122
		return hxsublime_Settings.getString("haxe_exec","haxe",view)

	@staticmethod
	def useHaxeServermode(view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:127
		return hxsublime_Settings.getBool("haxe_use_servermode",True,view)

	@staticmethod
	def useHaxeServermodeWrapper(view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:132
		return hxsublime_Settings.getBool("haxe_use_servermode_wrapper",False,view)

	@staticmethod
	def haxeSdkPath(view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:137
		return hxsublime_Settings.getString("haxe_sdk_path",None,view)

	@staticmethod
	def openWithDefaultApp(view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:142
		return hxsublime_Settings.getString("haxe_open_with_default_app",None,view)

	@staticmethod
	def haxeInstPath(view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:147
		tmp = hxsublime_Settings.haxeSdkPath(view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:148
		defaultVal = None
		if (tmp is not None):
			defaultVal = ((HxOverrides.stringOrNull(python_lib_os_Path.normpath(hxsublime_Settings.haxeSdkPath(view))) + HxOverrides.stringOrNull(python_lib_os_Path.sep)) + "haxe")
		else:
			defaultVal = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:149
		if ((tmp is None) and ((hxsublime_Settings.haxeExec(view) != "haxe"))):
			defaultVal = python_lib_os_Path.normpath(python_lib_os_Path.dirname(hxsublime_Settings.haxeExec(view)))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:154
		return hxsublime_Settings.getString("haxe_inst_path",defaultVal,view)

	@staticmethod
	def nekoInstPath(view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:159
		tmp = hxsublime_Settings.haxeSdkPath(view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:161
		defaultVal = None
		if (tmp is not None):
			defaultVal = ((HxOverrides.stringOrNull(python_lib_os_Path.normpath(hxsublime_Settings.haxeSdkPath(view))) + HxOverrides.stringOrNull(python_lib_os_Path.sep)) + "default")
		else:
			defaultVal = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:162
		return hxsublime_Settings.getString("neko_inst_path",defaultVal,view)

	@staticmethod
	def haxeLibraryPath(view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:167
		return hxsublime_Settings.getString("haxe_library_path",None,view)

	@staticmethod
	def haxelibExec(view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:172
		return hxsublime_Settings.getString("haxe_haxelib_exec","haxelib",view)

	@staticmethod
	def smartSnippets(view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:177
		return hxsublime_Settings.getBool("haxe_completion_smart_snippets",True,view)

	@staticmethod
	def smartSnippetsOnCompletion(view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:182
		return hxsublime_Settings.getBool("haxe_completion_smart_snippets_on_completion",False,view)

	@staticmethod
	def smartSnippetsJustCurrent(view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:187
		return hxsublime_Settings.getBool("haxe_completion_smart_snippets_just_current",False,view)

	@staticmethod
	def checkOnSave(view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:192
		return hxsublime_Settings.getBool("haxe_check_on_save",True,view)

	@staticmethod
	def useSlidePanel(view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:197
		return hxsublime_Settings.getBool("haxe_use_slide_panel",True,view)

	@staticmethod
	def useHaxeServermodeForBuilds(view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:202
		return hxsublime_Settings.getBool("haxe_use_servermode_for_builds",False,view)

	@staticmethod
	def useOffsetCompletion(view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Settings.hx:207
		return hxsublime_Settings.getBool("haxe_use_offset_completion",False,view)
hxsublime_Settings._hx_class = hxsublime_Settings
_hx_classes["hxsublime.Settings"] = hxsublime_Settings


class hxsublime_Temp:
	_hx_class_name = "hxsublime.Temp"
	_hx_statics = ["getTempPathId", "createTempPath", "createFile", "createTempPathAndFile", "removePath"]

	@staticmethod
	def getTempPathId(build):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Temp.hx:18
		path = build.getBuildFolder()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Temp.hx:20
		if (path is None):
			raise hxsublime_ExtractBuildPathException(build)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Temp.hx:25
		path1 = None
		_this = None
		_this1 = None
		_this2 = None
		delimiter = python_lib_Os.sep
		if (delimiter == ""):
			_this2 = list(path)
		else:
			_this2 = path.split(delimiter)
		_this1 = "_".join([python_Boot.toString1(x1,'') for x1 in _this2])
		_this = _this1.split(":")
		path1 = "_".join([python_Boot.toString1(x1,'') for x1 in _this])
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Temp.hx:27
		temp_path = python_lib_os_Path.join(python_lib_Tempfile.gettempdir(),(("haxe_sublime_hx" + ("null" if path1 is None else path1)) + "_"))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Temp.hx:29
		return temp_path

	@staticmethod
	def createTempPath(build):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Temp.hx:34
		temp_path = hxsublime_Temp.getTempPathId(build)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Temp.hx:37
		hxsublime_tools_PathTools.removeDir(temp_path)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Temp.hx:38
		python_lib_Os.makedirs(temp_path)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Temp.hx:40
		return temp_path

	@staticmethod
	def createFile(temp_path,build,orig_file,content):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Temp.hx:46
		relative = build.getRelativePath(orig_file)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Temp.hx:48
		if (relative is None):
			raise hxsublime_GetRelativePathException(build, orig_file)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Temp.hx:53
		new_file = python_lib_os_Path.join(temp_path,relative)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Temp.hx:54
		new_file_dir = python_lib_os_Path.dirname(new_file)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Temp.hx:55
		if (not python_lib_os_Path.exists(new_file_dir)):
			python_lib_Os.makedirs(new_file_dir)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Temp.hx:60
		f = python_lib_Codecs.open(new_file,"wb","utf-8","ignore")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Temp.hx:61
		f.write(content)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Temp.hx:63
		Reflect.field(f,"close")()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Temp.hx:65
		return new_file

	@staticmethod
	def createTempPathAndFile(build,orig_file,content):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Temp.hx:70
		temp_path = hxsublime_Temp.createTempPath(build)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Temp.hx:72
		temp_file = hxsublime_Temp.createFile(temp_path,build,orig_file,content)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Temp.hx:73
		return (temp_path, temp_file)

	@staticmethod
	def removePath(temp_path):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Temp.hx:78
		if (temp_path is not None):
			hxsublime_tools_PathTools.removeDir(temp_path)
hxsublime_Temp._hx_class = hxsublime_Temp
_hx_classes["hxsublime.Temp"] = hxsublime_Temp


class hxsublime_Types:
	_hx_class_name = "hxsublime.Types"
	_hx_statics = ["findTypes", "validPackageRegex", "isValidPackage", "extractTypes", "fileTypeCache", "extractTypesFromFile"]

	@staticmethod
	def findTypes(classpaths,libs,base_path,filtered_classes = None,filtered_packages = None,include_private_types = True):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:20
		if (include_private_types is None):
			include_private_types = True
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:21
		bundle = hxsublime_tools_HxSrcTools.emptyTypeBundle()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:23
		cp = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:24
		cp = (cp + classpaths)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:26
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:26
		_g = 0
		while (_g < len(libs)):
			lib = (libs[_g] if _g >= 0 and _g < len(libs) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:27
			if (lib is not None):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:28
				cp.append(lib.path)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:31
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:31
		_g1 = 0
		while (_g1 < len(cp)):
			path = (cp[_g1] if _g1 >= 0 and _g1 < len(cp) else None)
			_g1 = (_g1 + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:33
			p = python_lib_os_Path.join(base_path,path)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:35
			if python_lib_os_Path.exists(p):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:36
				b = hxsublime_Types.extractTypes(p,filtered_classes,filtered_packages,0,[],include_private_types)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:37
				bundle = bundle.merge(b)
			else:
				hxsublime_panel_Panels.defaultPanel().writeln((("Error: The classpath " + ("null" if p is None else p)) + " does not exist, in case of nme or openfl you need have to build (CTRL + ENTER) the project first (the build creates these paths)"))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:44
		return bundle

	@staticmethod
	def isValidPackage(pack):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:51
		return ((hxsublime_Types.validPackageRegex.match(pack) is not None) and ((pack != "_std")))

	@staticmethod
	def extractTypes(path,filtered_classes = None,filtered_packages = None,depth = 0,pack = None,include_private_types = True):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:55
		if (depth is None):
			depth = 0
		if (include_private_types is None):
			include_private_types = True
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:56
		if (pack is None):
			pack = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:57
		if (filtered_classes is None):
			filtered_classes = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:58
		if (filtered_packages is None):
			filtered_packages = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:60
		bundle = hxsublime_tools_HxSrcTools.emptyTypeBundle()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:62
		bundles = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:63
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:63
		_g = 0
		_g1 = python_lib_Glob.glob(python_lib_os_Path.join(path,"*.hx"))
		while (_g < len(_g1)):
			fullpath = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:65
			f = python_lib_os_Path.basename(fullpath)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:67
			r = python_lib_os_Path.splitext(f)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:68
			cl = r[0]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:69
			ext = r[1]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:71
			if (not Lambda.has(filtered_classes,cl)):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:73
				file = python_lib_os_Path.join(path,f)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:74
				if python_lib_os_Path.exists(file):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:76
					module_bundle = hxsublime_Types.extractTypesFromFile(file,cl,include_private_types)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:78
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:78
					bundles.append(module_bundle)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:83
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:83
		_g2 = 0
		_g11 = python_lib_Os.listdir(path)
		while (_g2 < len(_g11)):
			f1 = (_g11[_g2] if _g2 >= 0 and _g2 < len(_g11) else None)
			_g2 = (_g2 + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:85
			if hxsublime_Types.isValidPackage(f1):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:87
				r1 = python_lib_os_Path.splitext(f1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:88
				cl1 = r1[0]
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:89
				ext1 = r1[1]
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:91
				cur_pack_base = None
				if (len(pack) > 0):
					cur_pack_base = (HxOverrides.stringOrNull(".".join([python_Boot.toString1(x1,'') for x1 in pack])) + ".")
				else:
					cur_pack_base = ""
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:93
				cur_pack = (("null" if cur_pack_base is None else cur_pack_base) + ("null" if f1 is None else f1))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:95
				if ((python_lib_os_Path.isdir(python_lib_os_Path.join(path,f1)) and (not Lambda.has(filtered_packages,cur_pack))) and (not cur_pack in hxsublime_Config.ignored_packages.h)):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:97
					next_pack = list(pack)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:98
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:98
					next_pack.append(f1)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:100
					sub_bundle = hxsublime_Types.extractTypes(python_lib_os_Path.join(path,f1),filtered_classes,filtered_packages,(depth + 1),next_pack,include_private_types)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:101
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:101
					bundles.append(sub_bundle)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:105
		bundle = bundle.mergeAll(bundles)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:107
		return bundle

	@staticmethod
	def extractTypesFromFile(file,module_name = None,include_private_types = True):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:113
		if (include_private_types is None):
			include_private_types = True
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:114
		mtime = python_lib_os_Path.getmtime(file)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:115
		def _hx_local_0():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:115
			_this = hxsublime_Types.fileTypeCache.h.get(file,None)
			return _this[0]
		if (file in hxsublime_Types.fileTypeCache.h and ((_hx_local_0() == mtime))):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:117
			_this1 = hxsublime_Types.fileTypeCache.h.get(file,None)
			return _this1[1]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:122
		if (module_name is None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:124
			_this2 = python_lib_os_Path.splitext(python_lib_os_Path.basename(file))
			module_name = _this2[0]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:127
		s = python_lib_Codecs.open(file,"r","utf-8","ignore")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:128
		src_with_comments = s.read()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:130
		src = hxsublime_tools_HxSrcTools.stripComments(src_with_comments)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:132
		bundle = hxsublime_tools_HxSrcTools.getTypesFromSrc(src,module_name,file,src_with_comments)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:134
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:134
		value = (mtime, bundle)
		hxsublime_Types.fileTypeCache.h[file] = value
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Types.hx:136
		return bundle
hxsublime_Types._hx_class = hxsublime_Types
_hx_classes["hxsublime.Types"] = hxsublime_Types


class hxsublime_build_Build:
	_hx_class_name = "hxsublime.build.Build"
	_hx_methods = ["setHxml", "getRelativePath", "setStdBundle", "toString", "copy", "buildFile", "addClasspath", "makeHxml", "prepareCheckCmd", "prepareBuildCmd", "prepareRunCmd", "escapeCmd", "isTypeAvailable", "isPackAvailable", "getTypes", "getBuildFolder", "setAutoCompletion", "setTimes", "run", "stdBundle", "target", "classpaths", "args", "addArg"]
hxsublime_build_Build._hx_class = hxsublime_build_Build
_hx_classes["hxsublime.build.Build"] = hxsublime_build_Build


class hxsublime_build_HxmlBuild:
	_hx_class_name = "hxsublime.build.HxmlBuild"
	_hx_fields = ["_showTimes", "_stdBundle", "_args", "_hxml", "_buildFile", "libs", "_updateTime", "defines", "_classpaths", "typeBundle", "modeCompletion", "name", "main", "_target", "output"]
	_hx_methods = ["getClassPaths", "stdBundle", "target", "classpaths", "hxml", "title", "setHxml", "buildFile", "addDefine", "setMain", "getName", "setStdBundle", "args", "equals", "merge", "copy", "addArg", "getBuildFolder", "setBuildCwd", "alignDriveLetter", "addClasspath", "addLib", "getClasspathOfFile", "getRelativePath", "targetToString", "toString", "makeHxml", "setCwd", "setTimes", "setServerMode", "getCommandArgs", "setAutoCompletion", "updateTypes", "shouldRefreshTypes", "getTypes", "prepareCheckCmd", "absoluteOutput", "prepareRunCmd", "prepareBuildCmd", "prepareRun", "getExecutable", "escapeCmd", "runAsync", "runSync", "onRunComplete", "runNekoX", "run", "isTypeAvailable", "isPackAvailable"]
	_hx_interfaces = [hxsublime_build_Build]

	def __init__(self,hxml,build_file):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:27
		self._showTimes = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:28
		self._stdBundle = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:29
		self._args = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:31
		self._hxml = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:32
		self._buildFile = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:33
		self.libs = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:34
		self._updateTime = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:35
		self.defines = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:37
		self._classpaths = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:38
		self.typeBundle = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:39
		self.modeCompletion = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:41
		self.name = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:42
		self.main = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:43
		self._target = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:44
		self.output = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:54
		self._showTimes = False
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:55
		self._stdBundle = hxsublime_tools_HxSrcTools.emptyTypeBundle()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:56
		self._args = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:57
		self.main = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:58
		self._target = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:60
		self.output = "dummy.js"
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:61
		self._hxml = hxml
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:62
		self._buildFile = build_file
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:63
		self._classpaths = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:64
		self.libs = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:65
		self.typeBundle = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:66
		self._updateTime = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:67
		self.modeCompletion = False
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:68
		self.defines = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:69
		self.name = None

	def getClassPaths(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:48
		return self._classpaths

	def stdBundle(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:74
		return self._stdBundle

	def target(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:76
		return _hx_AnonObject({'name': self._target, 'plattform': self._target, 'args': []})

	def classpaths(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:78
		return self._classpaths

	def hxml(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:80
		return self._hxml

	def title(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:85
		return self.output

	def setHxml(self,hxml):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:90
		self._hxml = hxml

	def buildFile(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:95
		return self._buildFile

	def addDefine(self,define):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:100
		_this = self.defines
		_this.append(define)

	def setMain(self,main):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:106
		self.main = main

	def getName(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:114
		n = None
		if (self.name is not None):
			n = self.name
		elif (self.main is None):
			n = "[No Main]"
		else:
			n = self.main
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:117
		return n

	def setStdBundle(self,stdBundle):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:122
		self._stdBundle = stdBundle

	def args(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:125
		return self._args

	def equals(self,other):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:130
		return ((((((((((((self._args is other._args()) and ((self.main == other.main))) and ((self.name == other.name))) and ((self._target == other._target))) and ((self.output == other.output))) and ((self._hxml == other.hxml()))) and ((self._classpaths is other.classpaths()))) and ((self.libs is other.libs))) and ((self._showTimes == other._showTimes))) and ((self.modeCompletion == other.modeCompletion))) and ((self.defines is other.defines))) and ((self._buildFile == other._buildFile)))

	def merge(self,other_build):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:146
		ob = other_build
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:147
		self._args.extend(ob._args)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:149
		self._classpaths.extend(ob._classpaths)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:151
		self.libs.extend(ob.libs)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:152
		self.defines.extend(ob.defines)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:154
		if (self.main is None):
			self.main = ob.main
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:158
		if (self.name is None):
			self.name = ob.name

	def copy(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:167
		self.getTypes()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:169
		hb = hxsublime_build_HxmlBuild(self._hxml, self._buildFile)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:170
		hb._args = list(self._args)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:171
		hb.main = self.main
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:172
		hb.name = self.name
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:173
		hb._target = self._target
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:174
		hb.output = self.output
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:175
		hb.defines = list(self.defines)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:176
		hb._stdBundle = self._stdBundle
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:177
		hb._classpaths = list(self._classpaths)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:178
		hb.libs = list(self.libs)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:179
		hb.typeBundle = self.typeBundle
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:180
		hb._updateTime = self._updateTime
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:181
		hb._showTimes = self._showTimes
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:182
		hb.modeCompletion = self.modeCompletion
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:183
		return hb

	def addArg(self,arg):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:187
		_this = self._args
		_this.append(arg)

	def getBuildFolder(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:192
		if (self._buildFile is not None):
			return python_lib_os_Path.dirname(self._buildFile)
		else:
			return None

	def setBuildCwd(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:197
		self.setCwd(self.getBuildFolder())

	def alignDriveLetter(self,path):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:203
		is_win = (sublime_Sublime.platform() == "windows")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:205
		if is_win:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:206
			reg = python_lib_Re.compile("^([a-z]):(.*)$")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:207
			match = python_lib_Re.match(reg,path)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:208
			if (match is not None):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:209
				def _hx_local_0():
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:209
					_this = match.group(1)
					return _this.upper()
				path = ((HxOverrides.stringOrNull(_hx_local_0()) + ":") + HxOverrides.stringOrNull(match.group(2)))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:212
		return path

	def addClasspath(self,cp):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:217
		cp1 = self.alignDriveLetter(cp)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:218
		if (not Lambda.has(self._classpaths,cp1)):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:219
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:219
			_this = self._classpaths
			_this.append(cp1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:220
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:220
			_this1 = self._args
			x = ("-cp", cp1)
			_this1.append(x)

	def addLib(self,lib):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:227
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:227
		_this = self.libs
		_this.append(lib)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:228
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:228
		arg = ("-lib", lib.name)
		_this1 = self._args
		_this1.append(arg)

	def getClasspathOfFile(self,file):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:233
		file1 = self.alignDriveLetter(file)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:235
		cps = list(self._classpaths)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:237
		build_folder = self.getBuildFolder()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:238
		if ((build_folder is not None) and (not Lambda.has(cps,build_folder))):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:240
			haxe_Log.trace(((("add build folder to classpaths: " + ("null" if build_folder is None else build_folder)) + ", classpaths: ") + Std.string(cps)),_hx_AnonObject({'fileName': "HxmlBuild.hx", 'lineNumber': 240, 'className': "hxsublime.build.HxmlBuild", 'methodName': "getClasspathOfFile"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:241
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:241
			cps.append(build_folder)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:243
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:243
		_g = 0
		while (_g < len(cps)):
			cp = (cps[_g] if _g >= 0 and _g < len(cps) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:245
			prefix = python_lib_os_Path.commonprefix([cp, file1])
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:246
			if (prefix == cp):
				return cp
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:251
		return None

	def getRelativePath(self,file):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:256
		file = self.alignDriveLetter(file)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:258
		cp = self.getClasspathOfFile(file)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:260
		if (cp is not None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:260
			_this = StringTools.replace(file,cp,"")
			return HxString.substr(_this,1,None)
		else:
			return None

	def targetToString(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:265
		target = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:266
		if (self._target is None):
			target = "js"
		else:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:271
			target = self._target
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:272
			if ((target == "js") and Lambda.has(self.defines,"nodejs")):
				target = "node.js"
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:277
		return target

	def toString(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:282
		out = python_lib_os_Path.basename(self.output)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:283
		main = self.getName()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:284
		target = self.targetToString()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:285
		return (((((("" + ("null" if main is None else main)) + " (") + ("null" if target is None else target)) + " - ") + ("null" if out is None else out)) + ")")

	def makeHxml(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:290
		outp = (("# Autogenerated " + Std.string(self.hxml)) + "\n\n")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:291
		outp = (("null" if outp is None else outp) + HxOverrides.stringOrNull(((("# " + HxOverrides.stringOrNull(self.toString())) + "\n"))))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:292
		outp = (("null" if outp is None else outp) + HxOverrides.stringOrNull(((("-main " + HxOverrides.stringOrNull(self.main)) + "\n"))))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:293
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:293
		_g = 0
		_g1 = self._args
		while (_g < len(_g1)):
			a = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:294
			outp = (("null" if outp is None else outp) + HxOverrides.stringOrNull(((((HxOverrides.stringOrNull(a[0]) + " ") + HxOverrides.stringOrNull(a[1])) + "\n"))))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:297
		d = (HxOverrides.stringOrNull(python_lib_os_Path.dirname(self._hxml)) + "/")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:300
		outp = StringTools.replace(outp,d,"")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:301
		outp = StringTools.replace(outp,(("-cp " + HxOverrides.stringOrNull(python_lib_os_Path.dirname(self._hxml))) + "\n"),"")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:303
		outp = StringTools.replace(outp,"--no-output ","")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:304
		outp = StringTools.replace(outp,"-v","")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:306
		outp = StringTools.replace(outp,"dummy",self.main.lower())
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:308
		return outp.strip(None)

	def setCwd(self,cwd):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:313
		_this = self._args
		x = ("--cwd", cwd)
		_this.append(x)

	def setTimes(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:318
		self._showTimes = True
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:319
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:319
		_this = self._args
		x = ("--times", "")
		_this.append(x)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:320
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:320
		_this1 = self._args
		x1 = ("-D", "macro-times")
		_this1.append(x1)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:321
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:321
		_this2 = self._args
		x2 = ("-D", "macro_times")
		_this2.append(x2)

	def setServerMode(self,server_port = 6000):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:326
		if (server_port is None):
			server_port = 6000
		_this = self._args
		x = ("--connect", Std.string(server_port))
		_this.append(x)

	def getCommandArgs(self,haxe_path):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:331
		cmd = list(haxe_path)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:333
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:333
		_g = 0
		_g1 = self._args
		while (_g < len(_g1)):
			a = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:335
			cmd.extend([a[0], a[1]])
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:338
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:338
		_g2 = 0
		_g11 = self.libs
		while (_g2 < len(_g11)):
			l = (_g11[_g2] if _g2 >= 0 and _g2 < len(_g11) else None)
			_g2 = (_g2 + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:340
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:340
			cmd.append("-lib")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:341
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:341
			x = l.as_cmd_arg()
			cmd.append(x)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:344
		if (self.main is not None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:346
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:346
			cmd.append("-main")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:347
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:347
			cmd.append(self.main)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:349
		return cmd

	def setAutoCompletion(self,display,macroCompletion = False,noOutput = True):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:353
		if (macroCompletion is None):
			macroCompletion = False
		if (noOutput is None):
			noOutput = True
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:354
		self.modeCompletion = True
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:356
		args = self._args
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:358
		self.main = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:362
		def _hx_local_1(x):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:362
			_g = x[0]
			_hx_local_0 = len(_g)
			if (_hx_local_0 == 4):
				if (_g == "-php"):
					return False
				elif (_g == "-cpp"):
					return False
				elif (_g == "-swf"):
					return False
				else:
					return True
			elif (_hx_local_0 == 5):
				if (_g == "-java"):
					return False
				else:
					return True
			elif (_hx_local_0 == 7):
				if (_g == "-python"):
					return False
				else:
					return True
			elif (_hx_local_0 == 3):
				if (_g == "-cs"):
					return False
				elif (_g == "-js"):
					return False
				else:
					return True
			elif (_hx_local_0 == 2):
				if (_g == "-x"):
					return False
				else:
					return True
			else:
				return True
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:360
		filterTargets = _hx_local_1
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:369
		if macroCompletion:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:371
			_this = list(filter(filterTargets,args))
			args = list(_this)
		else:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:375
			def _hx_local_2(x1):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:375
				if (x1[0] == "-x"):
					return ("-neko", x1[1])
				else:
					return x1
			_this1 = list(map(_hx_local_2,args))
			args = list(_this1)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:380
		def _hx_local_3(x2):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:380
			_g1 = x2[0]
			if ((_g1 == "-dce") or ((_g1 == "-cmd"))):
				return False
			else:
				return True
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:378
		filterCommandsAndDce = _hx_local_3
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:387
		args = list(filter(filterCommandsAndDce,args))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:389
		if (not self._showTimes):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:393
			def _hx_local_4(x3):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:393
				return (x3[0] != "--times")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:391
			filterTimes = _hx_local_4
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:395
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:395
			_this2 = list(filter(filterTimes,args))
			args = list(_this2)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:398
		if macroCompletion:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:400
			x4 = ("-neko", "__temp.n")
			args.append(x4)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:404
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:404
		x5 = ("--display", display)
		args.append(x5)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:405
		if noOutput:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:407
			x6 = ("--no-output", "")
			args.append(x6)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:410
		self._args = args

	def updateTypes(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:417
		haxe_Log.trace(("update types for classpaths:" + Std.string(self._classpaths)),_hx_AnonObject({'fileName': "HxmlBuild.hx", 'lineNumber': 417, 'className': "hxsublime.build.HxmlBuild", 'methodName': "updateTypes"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:418
		haxe_Log.trace(("update types for libs:" + Std.string(self.libs)),_hx_AnonObject({'fileName': "HxmlBuild.hx", 'lineNumber': 418, 'className': "hxsublime.build.HxmlBuild", 'methodName': "updateTypes"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:419
		self.typeBundle = hxsublime_Types.findTypes(self._classpaths,self.libs,self.getBuildFolder(),[],[],False)

	def shouldRefreshTypes(self,now):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:427
		return (((self.typeBundle is None) or ((self._updateTime is None))) or (((now - self._updateTime) > 10)))

	def getTypes(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:432
		now = python_lib_Time.time()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:434
		if self.shouldRefreshTypes(now):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:436
			haxe_Log.trace("UPDATE THE TYPES NOW",_hx_AnonObject({'fileName': "HxmlBuild.hx", 'lineNumber': 436, 'className': "hxsublime.build.HxmlBuild", 'methodName': "getTypes"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:437
			self._updateTime = now
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:438
			self.updateTypes()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:439
			runTime = (python_lib_Time.time() - now)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:440
			haxe_Log.trace(("update types time: " + Std.string(runTime)),_hx_AnonObject({'fileName': "HxmlBuild.hx", 'lineNumber': 440, 'className': "hxsublime.build.HxmlBuild", 'methodName': "getTypes"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:443
		return self.typeBundle

	def prepareCheckCmd(self,project,server_mode,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:448
		r = self.prepareBuildCmd(project,server_mode,view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:449
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:449
		_this = r.cmd
		_this.append("--no-output")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:450
		return r

	def absoluteOutput(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:455
		if python_lib_os_Path.isabs(self.output):
			return self.output
		else:
			return python_lib_os_Path.join(self.getBuildFolder(),self.output)

	def prepareRunCmd(self,project,server_mode,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:465
		r = self.prepareRun(project,view,server_mode)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:466
		cmd = r[0]
		build_folder = r[1]
		nekox_file = r[2]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:468
		haxe_Log.trace(self.args,_hx_AnonObject({'fileName': "HxmlBuild.hx", 'lineNumber': 468, 'className': "hxsublime.build.HxmlBuild", 'methodName': "prepareRunCmd"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:469
		haxe_Log.trace(cmd,_hx_AnonObject({'fileName': "HxmlBuild.hx", 'lineNumber': 469, 'className': "hxsublime.build.HxmlBuild", 'methodName': "prepareRunCmd"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:470
		haxe_Log.trace(build_folder,_hx_AnonObject({'fileName': "HxmlBuild.hx", 'lineNumber': 470, 'className': "hxsublime.build.HxmlBuild", 'methodName': "prepareRunCmd"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:471
		haxe_Log.trace(nekox_file,_hx_AnonObject({'fileName': "HxmlBuild.hx", 'lineNumber': 471, 'className': "hxsublime.build.HxmlBuild", 'methodName': "prepareRunCmd"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:473
		default_open_ext = hxsublime_Settings.openWithDefaultApp()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:475
		if (nekox_file is not None):
			cmd.extend(["-cmd", ("neko " + ("null" if nekox_file is None else nekox_file))])
		elif ((self._target == "swf") and ((default_open_ext is not None))):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:481
			x = ["-cmd", ((("null" if default_open_ext is None else default_open_ext) + " ") + HxOverrides.stringOrNull(self.absoluteOutput()))]
			cmd.extend(x)
		elif (self._target == "neko"):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:485
			x1 = ["-cmd", ("neko " + HxOverrides.stringOrNull(self.absoluteOutput()))]
			cmd.extend(x1)
		elif (self._target == "cpp"):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:489
			sep_index = None
			_this = self.main
			sep_index = _this.rfind(".", 0, len(_this))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:490
			exe = None
			if (sep_index > -1):
				exe = HxString.substr(self.main,(sep_index + 1),None)
			else:
				exe = self.main
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:491
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:491
			x2 = ["-cmd", (HxOverrides.stringOrNull(python_lib_os_Path.join(self.absoluteOutput(),exe)) + "-debug")]
			cmd.extend(x2)
		elif ((self._target == "js") and Lambda.has(self.defines,"nodejs")):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:495
			x3 = ["-cmd", ("nodejs " + HxOverrides.stringOrNull(self.absoluteOutput()))]
			cmd.extend(x3)
		elif (self._target == "python"):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:499
			x4 = ["-cmd", ("python " + HxOverrides.stringOrNull(self.absoluteOutput()))]
			cmd.extend(x4)
		elif (self._target == "java"):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:503
			sep_index1 = None
			_this1 = self.absoluteOutput()
			_hx_str = python_lib_os_Path.sep
			sep_index1 = _this1.rfind(_hx_str, 0, len(_this1))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:504
			jar = None
			if (sep_index1 == -1):
				jar = (HxOverrides.stringOrNull(self.absoluteOutput()) + ".jar")
			else:
				def _hx_local_0():
					_this2 = self.absoluteOutput()
					return HxString.substr(_this2,(sep_index1 + 1),None)
				jar = (HxOverrides.stringOrNull(_hx_local_0()) + ".jar")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:505
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:505
			x5 = ["-cmd", ("java -jar " + HxOverrides.stringOrNull(python_lib_os_Path.join(self.absoluteOutput(),jar)))]
			cmd.extend(x5)
		elif (self._target == "cs"):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:509
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:509
			x6 = ["-cmd", ("cd " + HxOverrides.stringOrNull(self.absoluteOutput()))]
			cmd.extend(x6)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:510
			cmd.extend(["-cmd", (((("gmcs -recurse:*.cs -main:" + HxOverrides.stringOrNull(self.main)) + " -out:") + HxOverrides.stringOrNull(self.main)) + ".exe-debug")])
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:511
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:511
			x7 = ["-cmd", python_lib_os_Path.join(".",(HxOverrides.stringOrNull(self.main) + ".exe-debug"))]
			cmd.extend(x7)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:514
		return _hx_AnonObject({'cmd': cmd, 'folder': build_folder})

	def prepareBuildCmd(self,project,server_mode,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:519
		r = self.prepareRun(project,view,server_mode)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:520
		cmd = r[0]
		build_folder = r[1]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:521
		return _hx_AnonObject({'cmd': r[0], 'folder': build_folder})

	def prepareRun(self,project,view,server_mode = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:527
		if (server_mode is None):
			server_mode = project.isServerMode()
		else:
			server_mode = server_mode
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:529
		run_exec = self.getExecutable(project,view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:530
		b = self.copy()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:532
		nekoxFileName = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:534
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:534
		_g1 = 0
		_g = len(b._args)
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:536
			a = (b._args[i] if i >= 0 and i < len(b._args) else None)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:537
			if (a[0] == "-x"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:538
				nekoxFileName = (HxOverrides.stringOrNull(a[1]) + ".n")
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:539
				python_internal_ArrayImpl._set(b._args, i, ("-neko", nekoxFileName))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:543
		if server_mode:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:544
			project.startServer(view)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:545
			b.setServerMode(project.server.get_server_port())
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:549
		b.setCwd(b.getBuildFolder())
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:550
		cmd = b.getCommandArgs(run_exec)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:552
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:552
		b1 = self.getBuildFolder()
		return (cmd, b1, nekoxFileName)

	def getExecutable(self,project,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:557
		return project.haxeExec(view)

	def escapeCmd(self,cmd):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:562
		print_cmd = list(cmd)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:563
		l = len(print_cmd)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:564
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:564
		_g = 0
		while (_g < l):
			i = _g
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:566
			e = (print_cmd[i] if i >= 0 and i < len(print_cmd) else None)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:567
			if ((e == "--macro") and ((i < ((l - 1))))):
				python_internal_ArrayImpl._set(print_cmd, (i + 1), (("'" + HxOverrides.stringOrNull(python_internal_ArrayImpl._get(print_cmd, (i + 1)))) + "'"))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:572
		return print_cmd

	def runAsync(self,project,view,callback,server_mode = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:575
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:577
		env = project.haxeEnv(view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:578
		r = self.prepareRun(project,view,server_mode)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:579
		cmd = r[0]
		build_folder = r[1]
		nekox_file_name = r[2]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:580
		print_cmd = list(cmd)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:581
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:581
		_g1 = 0
		_g2 = len(print_cmd)
		while (_g1 < _g2):
			i = _g1
			_g1 = (_g1 + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:583
			e = (print_cmd[i] if i >= 0 and i < len(print_cmd) else None)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:584
			if ((e == "--macro") and ((i < ((len(print_cmd) - 1))))):
				python_internal_ArrayImpl._set(print_cmd, (i + 1), (("'" + HxOverrides.stringOrNull(python_internal_ArrayImpl._get(print_cmd, (i + 1)))) + "'"))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:591
		def _hx_local_0(out,err):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:592
			_g.onRunComplete(out,err,build_folder,nekox_file_name)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:593
			callback(out,err)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:590
		cb = _hx_local_0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:596
		hxsublime_Execute.runCmdAsync(cmd,cb,"",build_folder,env)

	def runSync(self,project,view,server_mode = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:601
		env = project.haxeEnv(view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:602
		r = self.prepareRun(project,view,server_mode)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:603
		cmd = r[0]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:604
		build_folder = r[1]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:605
		nekox_file_name = r[2]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:607
		haxe_Log.trace(" ".join([python_Boot.toString1(x1,'') for x1 in cmd]),_hx_AnonObject({'fileName': "HxmlBuild.hx", 'lineNumber': 607, 'className': "hxsublime.build.HxmlBuild", 'methodName': "runSync"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:608
		r1 = hxsublime_Execute.runCmd(cmd,"",build_folder,env)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:609
		out = r1[0]
		err = r1[1]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:611
		self.onRunComplete(out,err,build_folder,nekox_file_name)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:613
		return (out, err)

	def onRunComplete(self,out,err,build_folder,nekox_file_name):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:619
		haxe_Log.trace("---------------cmd-------------------",_hx_AnonObject({'fileName': "HxmlBuild.hx", 'lineNumber': 619, 'className': "hxsublime.build.HxmlBuild", 'methodName': "onRunComplete"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:620
		haxe_Log.trace(("out:" + ("null" if out is None else out)),_hx_AnonObject({'fileName': "HxmlBuild.hx", 'lineNumber': 620, 'className': "hxsublime.build.HxmlBuild", 'methodName': "onRunComplete"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:621
		haxe_Log.trace(("err:" + ("null" if err is None else err)),_hx_AnonObject({'fileName': "HxmlBuild.hx", 'lineNumber': 621, 'className': "hxsublime.build.HxmlBuild", 'methodName': "onRunComplete"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:622
		haxe_Log.trace("---------compiler-output-------------",_hx_AnonObject({'fileName': "HxmlBuild.hx", 'lineNumber': 622, 'className': "hxsublime.build.HxmlBuild", 'methodName': "onRunComplete"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:623
		if (nekox_file_name is not None):
			self.runNekoX(build_folder,nekox_file_name)

	def runNekoX(self,build_folder,neko_file_name):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:632
		neko_file = python_lib_os_Path.join(build_folder,neko_file_name)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:633
		haxe_Log.trace(("run nekox: " + ("null" if neko_file is None else neko_file)),_hx_AnonObject({'fileName': "HxmlBuild.hx", 'lineNumber': 633, 'className': "hxsublime.build.HxmlBuild", 'methodName': "runNekoX"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:634
		r = hxsublime_Execute.runCmd(["neko", neko_file])
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:635
		out = r[0]
		err = r[1]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:636
		hxsublime_panel_Panels.defaultPanel().writeln(out)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:637
		hxsublime_panel_Panels.defaultPanel().writeln(err)

	def run(self,project,view,async,callback,server_mode = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:642
		if async:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:644
			haxe_Log.trace("RUN ASYNC COMPLETION",_hx_AnonObject({'fileName': "HxmlBuild.hx", 'lineNumber': 644, 'className': "hxsublime.build.HxmlBuild", 'methodName': "run"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:645
			self.runAsync(project,view,callback,server_mode)
		else:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:649
			haxe_Log.trace("RUN SYNC COMPLETION",_hx_AnonObject({'fileName': "HxmlBuild.hx", 'lineNumber': 649, 'className': "hxsublime.build.HxmlBuild", 'methodName': "run"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:650
			r = self.runSync(project,view,server_mode)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:651
			out = r[0]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:652
			err = r[1]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:653
			callback(out,err)

	def isTypeAvailable(self,_hx_type):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:659
		pack = _hx_type.toplevelPack()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:660
		return ((pack is None) or self.isPackAvailable(pack))

	def isPackAvailable(self,pack):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:665
		if (pack == ""):
			return True
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:670
		pack = HxOverrides.arrayGet(pack.split("."), 0)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:671
		target = self._target
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:673
		available = True
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:675
		if (((pack is not None) and ((target is not None))) and Lambda.has(hxsublime_Config.target_packages,pack)):
			if target in hxsublime_Config.target_std_packages.h:
				if (not Lambda.has(hxsublime_Config.target_std_packages.h.get(target,None),pack)):
					available = False
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/HxmlBuild.hx:685
		return available

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o._showTimes = None
		_hx_o._stdBundle = None
		_hx_o._args = None
		_hx_o._hxml = None
		_hx_o._buildFile = None
		_hx_o.libs = None
		_hx_o._updateTime = None
		_hx_o.defines = None
		_hx_o._classpaths = None
		_hx_o.typeBundle = None
		_hx_o.modeCompletion = None
		_hx_o.name = None
		_hx_o.main = None
		_hx_o._target = None
		_hx_o.output = None
hxsublime_build_HxmlBuild._hx_class = hxsublime_build_HxmlBuild
_hx_classes["hxsublime.build.HxmlBuild"] = hxsublime_build_HxmlBuild


class hxsublime_macros_LazyFunctionSupport:
	_hx_class_name = "hxsublime.macros.LazyFunctionSupport"
hxsublime_macros_LazyFunctionSupport._hx_class = hxsublime_macros_LazyFunctionSupport
_hx_classes["hxsublime.macros.LazyFunctionSupport"] = hxsublime_macros_LazyFunctionSupport


class hxsublime_build_NmeBuild:
	_hx_class_name = "hxsublime.build.NmeBuild"
	_hx_fields = ["_title", "_target", "_hxmlBuild", "nmml", "project"]
	_hx_methods = ["setHxml", "makeHxml", "title", "buildFile", "target", "plattform", "getHxmlBuildWithNmeDisplay", "hxmlBuild", "toString", "setStdBundle", "_filter_platform_specific", "getTypes", "stdBundle", "addArg", "copy", "getRelativePath", "getBuildFolder", "setAutoCompletion", "setTimes", "addDefine", "addClasspath", "run", "getExecutable", "getBuildCommand", "escapeCmd", "prepareCheckCmd", "prepareBuildCmd", "prepareRunCmd", "prepareCmd", "classpaths", "args", "isTypeAvailable", "isPackAvailable"]
	_hx_statics = ["__meta__"]
	_hx_interfaces = [hxsublime_macros_LazyFunctionSupport, hxsublime_build_Build]

	def __init__(self,project,title,nmml,target,cb = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:23
		self._title = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:24
		self._target = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:25
		self._hxmlBuild = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:27
		self.nmml = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:28
		self.project = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:32
		self._title = title
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:33
		self._target = target
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:34
		self.nmml = nmml
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:35
		self._hxmlBuild = cb
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:36
		self.project = project

	def setHxml(self,hxml):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:40
		_this = self.hxmlBuild()
		_this._hxml = hxml

	def makeHxml(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:44
		return self.hxmlBuild().makeHxml()

	def title(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:50
		return self._title

	def buildFile(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:56
		return self.nmml

	def target(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:62
		return self._target

	def plattform(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:68
		return self._target.plattform

	def getHxmlBuildWithNmeDisplay(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:73
		view = sublime_Sublime.active_window().active_view()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:74
		display_cmd = None
		_this = self.getBuildCommand(self.project,view)
		display_cmd = list(_this)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:75
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:75
		display_cmd.append("display")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:77
		return hxsublime_build_Tools.createHaxeBuildFromNmml(self.project,self._target,self.nmml,display_cmd)

	def hxmlBuild(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:84
		if (self._hxmlBuild is None):
			self._hxmlBuild = self.getHxmlBuildWithNmeDisplay()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:89
		return self._hxmlBuild

	def toString(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:94
		title = self.title()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:95
		target = self.target().name
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:96
		return (((("" + ("null" if title is None else title)) + " (NME - ") + ("null" if target is None else target)) + ")")

	def setStdBundle(self,std_bundle):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:102
		_this = self.hxmlBuild()
		_this._stdBundle = std_bundle

	def _filter_platform_specific(self,packs_or_classes):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:107
		res = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:108
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:108
		_g = 0
		while (_g < len(packs_or_classes)):
			c = (packs_or_classes[_g] if _g >= 0 and _g < len(packs_or_classes) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:109
			if (((((not StringTools.startsWith(c,"native")) and (not StringTools.startsWith(c,"browser"))) and (not StringTools.startsWith(c,"flash"))) and (not StringTools.startsWith(c,"flash9"))) and (not StringTools.startsWith(c,"flash8"))):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:110
				res.append(c)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:113
		return res

	def getTypes(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:117
		bundle = self.hxmlBuild().getTypes()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:118
		return bundle

	def stdBundle(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:124
		_this = self.hxmlBuild()
		return _this._stdBundle

	def addArg(self,arg):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:129
		_this = self.hxmlBuild()
		_this1 = _this._args
		_this1.append(arg)

	def copy(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:134
		hxmlCopy = None
		if (self._hxmlBuild is not None):
			hxmlCopy = self.hxmlBuild().copy()
		else:
			hxmlCopy = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:136
		return hxsublime_build_NmeBuild(self.project, self.title(), self.nmml, self._target, hxmlCopy)

	def getRelativePath(self,file):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:141
		return self.hxmlBuild().getRelativePath(file)

	def getBuildFolder(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:146
		r = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:147
		if (self.nmml is not None):
			r = python_lib_os_Path.dirname(self.nmml)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:151
		haxe_Log.trace(("build_folder: " + Std.string(r)),_hx_AnonObject({'fileName': "NmeBuild.hx", 'lineNumber': 151, 'className': "hxsublime.build.NmeBuild", 'methodName': "getBuildFolder"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:152
		haxe_Log.trace(("nmml: " + Std.string(self.nmml)),_hx_AnonObject({'fileName': "NmeBuild.hx", 'lineNumber': 152, 'className': "hxsublime.build.NmeBuild", 'methodName': "getBuildFolder"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:153
		return r

	def setAutoCompletion(self,display,macro_completion = False,no_output = True):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:158
		if (macro_completion is None):
			macro_completion = False
		if (no_output is None):
			no_output = True
		self.hxmlBuild().setAutoCompletion(display,macro_completion,no_output)

	def setTimes(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:163
		self.hxmlBuild().setTimes()

	def addDefine(self,define):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:168
		_this = self.hxmlBuild()
		_this1 = _this.defines
		_this1.append(define)

	def addClasspath(self,cp):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:173
		self.hxmlBuild().addClasspath(cp)

	def run(self,project,view,async,on_result,server_mode = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:178
		self.hxmlBuild().run(project,view,async,on_result,server_mode)

	def getExecutable(self,project,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:183
		return project.nmeExec(view)

	def getBuildCommand(self,project,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:188
		_this = self.getExecutable(project,view)
		return list(_this)

	def escapeCmd(self,cmd):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:193
		return self.hxmlBuild().escapeCmd(cmd)

	def prepareCheckCmd(self,project,server_mode,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:198
		r = self.prepareBuildCmd(project,server_mode,view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:200
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:200
		_this = r.cmd
		_this.append("--no-output")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:201
		return r

	def prepareBuildCmd(self,project,server_mode,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:206
		return self.prepareCmd(project,server_mode,view,"build")

	def prepareRunCmd(self,project,server_mode,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:211
		return self.prepareCmd(project,server_mode,view,"test")

	def prepareCmd(self,project,server_mode,view,command):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:216
		cmd = self.getBuildCommand(project,view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:218
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:218
		cmd.append(command)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:219
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:219
		x = self.buildFile()
		cmd.append(x)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:220
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:220
		x1 = self.target().plattform
		cmd.append(x1)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:221
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:221
		x2 = self.target().args
		cmd.extend(x2)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:223
		if server_mode:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:225
			x3 = ["--connect", Std.string(project.server.get_server_port())]
			cmd.extend(x3)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:227
		return _hx_AnonObject({'cmd': cmd, 'folder': self.getBuildFolder()})

	def classpaths(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:234
		_this = self.hxmlBuild()
		return _this._classpaths

	def args(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:240
		_this = self.hxmlBuild()
		return _this._args

	def isTypeAvailable(self,_hx_type):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:245
		pack = _hx_type.toplevelPack()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:246
		return ((pack is None) or self.isPackAvailable(pack))

	def isPackAvailable(self,pack):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:251
		if (pack == ""):
			return True
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:256
		pack1 = HxOverrides.arrayGet(pack.split("."), 0)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:257
		target = self.hxmlBuild().target
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:259
		tp = (hxsublime_Config.target_packages + ["native", "browser", "nme"])
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:261
		noTargetPack = (not Lambda.has(tp,pack1))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:262
		isNmePack = (pack1 == "nme")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:264
		available = (((target is None) or noTargetPack) or isNmePack)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/NmeBuild.hx:266
		return available

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o._title = None
		_hx_o._target = None
		_hx_o._hxmlBuild = None
		_hx_o.nmml = None
		_hx_o.project = None
hxsublime_build_NmeBuild._hx_class = hxsublime_build_NmeBuild
_hx_classes["hxsublime.build.NmeBuild"] = hxsublime_build_NmeBuild


class hxsublime_build_OpenFlBuild(hxsublime_build_NmeBuild):
	_hx_class_name = "hxsublime.build.OpenFlBuild"
	_hx_fields = []
	_hx_methods = ["copy", "getExecutable", "toString", "isTypeAvailable", "isPackAvailable"]
	_hx_statics = []
	_hx_interfaces = [hxsublime_macros_LazyFunctionSupport]
	_hx_super = hxsublime_build_NmeBuild


	def __init__(self,project,title,openfl_xml,target,cb = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/OpenFlBuild.hx:16
		super().__init__(project,title,openfl_xml,target,cb)

	def copy(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/OpenFlBuild.hx:21
		hxml_copy = None
		if (self._hxmlBuild is not None):
			hxml_copy = self.hxmlBuild().copy()
		else:
			hxml_copy = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/OpenFlBuild.hx:22
		r = hxsublime_build_OpenFlBuild(self.project, self.title(), self.nmml, self.target(), hxml_copy)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/OpenFlBuild.hx:24
		return r

	def getExecutable(self,project,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/OpenFlBuild.hx:29
		return project.openflExec(view)

	def toString(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/OpenFlBuild.hx:48
		out = self.title()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/OpenFlBuild.hx:49
		target = self.target().name
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/OpenFlBuild.hx:50
		return (((("" + ("null" if out is None else out)) + " (OpenFL - ") + ("null" if target is None else target)) + ")")

	def isTypeAvailable(self,_hx_type):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/OpenFlBuild.hx:56
		pack = _hx_type.toplevelPack()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/OpenFlBuild.hx:57
		return ((pack is None) or self.isPackAvailable(pack))

	def isPackAvailable(self,pack):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/OpenFlBuild.hx:62
		if (pack == ""):
			return True
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/OpenFlBuild.hx:67
		pack1 = HxOverrides.arrayGet(pack.split("."), 0)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/OpenFlBuild.hx:68
		target = self.hxmlBuild().target
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/OpenFlBuild.hx:70
		tp = list(hxsublime_Config.target_packages)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/OpenFlBuild.hx:71
		tp.extend(["native", "browser", "nme"])
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/OpenFlBuild.hx:73
		no_target_pack = (not Lambda.has(tp,pack1))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/OpenFlBuild.hx:74
		is_flash_pack = (pack1 == "flash")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/OpenFlBuild.hx:76
		available = (((target is None) or no_target_pack) or is_flash_pack)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/OpenFlBuild.hx:78
		return available

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_build_OpenFlBuild._hx_class = hxsublime_build_OpenFlBuild
_hx_classes["hxsublime.build.OpenFlBuild"] = hxsublime_build_OpenFlBuild


class hxsublime_build_Tools:
	_hx_class_name = "hxsublime.build.Tools"
	_hx_statics = ["_extract_tag", "hxmlBufferToBuilds", "findBuildFiles", "hxmlToBuilds", "_find_nme_project_title", "createHaxeBuildFromNmml", "findHxmlProjects", "findNmeProjects", "findOpenflProjects"]

	@staticmethod
	def hxmlBufferToBuilds(project,hxml_buffer,folder,build_path,buildFile = None,hxml = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:38
		builds = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:40
		currentBuild = hxsublime_build_HxmlBuild(hxml, buildFile)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:42
		f = hxml_buffer
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:43
		while True:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:45
			l = f.readline()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:48
			if (l == ""):
				break
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:52
			if (l == "\n"):
				continue
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:56
			l = l.strip(None)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:58
			if StringTools.startsWith(l,"#build-name="):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:60
				currentBuild.name = HxString.substr(l,12,None)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:61
				continue
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:63
			if StringTools.startsWith(l,"#"):
				continue
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:68
			if StringTools.startsWith(l,"--next"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:70
				if (len(currentBuild.getClassPaths()) == 0):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:72
					haxe_Log.trace("no classpaths",_hx_AnonObject({'fileName': "Tools.hx", 'lineNumber': 72, 'className': "hxsublime.build.Tools", 'methodName': "hxmlBufferToBuilds"}))
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:73
					currentBuild.addClasspath(build_path)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:76
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:76
				builds.append(currentBuild)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:77
				currentBuild = hxsublime_build_HxmlBuild(hxml, buildFile)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:78
				continue
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:81
			if StringTools.endsWith(l,".hxml"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:84
				haxe_Log.trace(("found ref of hxml file:" + ("null" if l is None else l)),_hx_AnonObject({'fileName': "Tools.hx", 'lineNumber': 84, 'className': "hxsublime.build.Tools", 'methodName': "hxmlBufferToBuilds"}))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:85
				path = python_lib_os_Path.dirname(hxml)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:86
				subBuilds = hxsublime_build_Tools.hxmlToBuilds(project,((("null" if path is None else path) + HxOverrides.stringOrNull(python_lib_Os.sep)) + ("null" if l is None else l)),folder)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:87
				if (len(subBuilds) == 1):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:89
					b = (subBuilds[0] if 0 < len(subBuilds) else None)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:90
					currentBuild.merge(b)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:94
			if StringTools.startsWith(l,"-main"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:96
				spl = l.split(" ")
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:97
				if (len(spl) == 2):
					currentBuild.main = (spl[1] if 1 < len(spl) else None)
				else:
					sublime_Sublime.status_message("Invalid build.hxml : no Main class")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:106
			if StringTools.startsWith(l,"-lib"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:108
				spl1 = l.split(" ")
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:109
				if (len(spl1) == 2):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:111
					lib = project.haxelibManager().get((spl1[1] if 1 < len(spl1) else None))
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:112
					if (lib is not None):
						currentBuild.addLib(lib)
					else:
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:119
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:119
						arg = ("-lib", (spl1[1] if 1 < len(spl1) else None))
						_this = currentBuild._args
						_this.append(arg)
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:121
						hxsublime_panel_Panels.defaultPanel().writeln((("Error: haxelib library " + Std.string((spl1[1] if 1 < len(spl1) else None))) + " is not installed"))
				else:
					sublime_Sublime.status_message("Invalid build.hxml : lib not found")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:129
			if StringTools.startsWith(l,"-cmd"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:131
				spl2 = l.split(" ")
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:132
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:132
				arg1 = None
				b1 = None
				_this1 = spl2[1:None]
				b1 = " ".join([python_Boot.toString1(x1,'') for x1 in _this1])
				arg1 = ("-cmd", b1)
				_this2 = currentBuild._args
				_this2.append(arg1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:135
			if StringTools.startsWith(l,"--macro"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:137
				spl3 = l.split(" ")
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:138
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:138
				arg2 = None
				b2 = None
				_this3 = spl3[1:None]
				b2 = " ".join([python_Boot.toString1(x1,'') for x1 in _this3])
				arg2 = ("--macro", b2)
				_this4 = currentBuild._args
				_this4.append(arg2)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:141
			if StringTools.startsWith(l,"-D"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:143
				x = l.split(" ")
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:145
				tup = ((x[0] if 0 < len(x) else None), (x[1] if 1 < len(x) else None))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:146
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:146
				_this5 = currentBuild._args
				_this5.append(tup)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:147
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:147
				_this6 = currentBuild.defines
				_this6.append(tup[1])
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:148
				continue
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:151
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:151
			_g = 0
			_g1 = ["swf-version", "swf-header", "debug", "-no-traces", "-flash-use-stage", "-gen-hx-classes", "-remap", "-no-inline", "-no-opt", "-php-prefix", "-js-namespace", "-interp", "-dead-code-elimination", "-php-front", "-php-lib", "dce", "-js-modern", "-times"]
			while (_g < len(_g1)):
				flag = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
				_g = (_g + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:157
				if StringTools.startsWith(l,("-" + ("null" if flag is None else flag))):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:159
					x1 = l.split(" ")
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:161
					p2 = None
					if (len(x1) == 1):
						p2 = ""
					else:
						p2 = (x1[1] if 1 < len(x1) else None)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:162
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:162
					arg3 = ((x1[0] if 0 < len(x1) else None), p2)
					_this7 = currentBuild._args
					_this7.append(arg3)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:164
					break
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:168
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:168
			_g2 = 0
			_g11 = ["resource", "xml", "x", "swf-lib", "java-lib"]
			while (_g2 < len(_g11)):
				flag1 = (_g11[_g2] if _g2 >= 0 and _g2 < len(_g11) else None)
				_g2 = (_g2 + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:170
				if StringTools.startsWith(l,("-" + ("null" if flag1 is None else flag1))):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:172
					spl4 = l.split(" ")
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:173
					def _hx_local_2():
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:173
						_this8 = spl4[1:None]
						return " ".join([python_Boot.toString1(x1,'') for x1 in _this8])
					outp = python_lib_os_Path.join(folder,_hx_local_2())
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:174
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:174
					arg4 = (("-" + ("null" if flag1 is None else flag1)), outp)
					_this9 = currentBuild._args
					_this9.append(arg4)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:175
					if (flag1 == "x"):
						currentBuild._target = "neko"
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:179
					break
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:183
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:183
			_g3 = 0
			_g12 = hxsublime_Config.targets
			while (_g3 < len(_g12)):
				flag2 = (_g12[_g3] if _g3 >= 0 and _g3 < len(_g12) else None)
				_g3 = (_g3 + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:185
				if StringTools.startsWith(l,(("-" + ("null" if flag2 is None else flag2)) + " ")):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:187
					spl5 = l.split(" ")
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:188
					if (len(spl5) == 0):
						None
					else:
						spl5.pop(0)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:189
					outp1 = " ".join([python_Boot.toString1(x1,'') for x1 in spl5])
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:191
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:191
					arg5 = (("-" + ("null" if flag2 is None else flag2)), outp1)
					_this10 = currentBuild._args
					_this10.append(arg5)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:193
					currentBuild._target = flag2
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:194
					currentBuild.output = outp1
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:195
					break
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:199
			if StringTools.startsWith(l,"-cp "):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:201
				cp = l.split(" ")
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:202
				if (len(cp) == 0):
					None
				else:
					cp.pop(0)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:203
				classpath = " ".join([python_Boot.toString1(x1,'') for x1 in cp])
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:205
				abs_classpath = hxsublime_tools_PathTools.joinNorm(build_path,classpath)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:206
				currentBuild.addClasspath(abs_classpath)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:211
		if (len(currentBuild.getClassPaths()) == 0):
			currentBuild.addClasspath(build_path)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:219
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:219
		builds.append(currentBuild)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:221
		return builds

	@staticmethod
	def findBuildFiles(folder,extension):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:227
		loop = None
		loop1 = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:228
		def _hx_local_3(folder1,maxDepth,startTime):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:229
			if ((maxDepth == 0) or (not python_lib_os_Path.isdir(folder1))):
				return []
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:234
			files = None
			_this = python_lib_Glob.glob(python_lib_os_Path.join(folder1,("*." + ("null" if extension is None else extension))))
			def _hx_local_0(x):
				return (x, folder1)
			files = list(map(_hx_local_0,_this))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:237
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:237
			_g = 0
			_g1 = python_lib_Os.listdir(folder1)
			while (_g < len(_g1)):
				dir = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
				_g = (_g + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:239
				f = python_lib_os_Path.join(folder1,dir)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:242
				recurse = None
				x1 = dir
				_hx_local_2 = len(dir)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:243
				if (_hx_local_2 == 4):
					if (dir == ".git"):
						recurse = False
					elif (dir == ".svn"):
						recurse = False
					elif ((len(x1) > 0) and (((("" if ((0 >= len(x1))) else x1[0])) == "."))):
						recurse = False
					else:
						recurse = python_lib_os_Path.isdir(f)
				elif (_hx_local_2 == 12):
					if (dir == "node_modules"):
						recurse = False
					elif ((len(x1) > 0) and (((("" if ((0 >= len(x1))) else x1[0])) == "."))):
						recurse = False
					else:
						recurse = python_lib_os_Path.isdir(f)
				elif (_hx_local_2 == 16):
					if (dir == "bower_components"):
						recurse = False
					elif ((len(x1) > 0) and (((("" if ((0 >= len(x1))) else x1[0])) == "."))):
						recurse = False
					else:
						recurse = python_lib_os_Path.isdir(f)
				elif (_hx_local_2 == 8):
					if (dir == ".vagrant"):
						recurse = False
					elif ((len(x1) > 0) and (((("" if ((0 >= len(x1))) else x1[0])) == "."))):
						recurse = False
					else:
						recurse = python_lib_os_Path.isdir(f)
				elif ((len(x1) > 0) and (((("" if ((0 >= len(x1))) else x1[0])) == "."))):
					recurse = False
				else:
					recurse = python_lib_os_Path.isdir(f)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:248
				if recurse:
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:248
					x2 = loop1(f,(maxDepth - 1),startTime)
					files.extend(x2)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:251
			return files
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:227
		loop1 = _hx_local_3
		loop = loop1
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:253
		return loop(folder,2,haxe_Timer.stamp())

	@staticmethod
	def hxmlToBuilds(project,hxml,folder):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:258
		build_path = python_lib_os_Path.dirname(hxml)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:259
		hxml_buffer = python_lib_Codecs.open(hxml,"r+","utf-8","ignore")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:260
		def _hx_local_1():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:260
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:260
				return hxml_buffer.readline()
			return hxsublime_build_Tools.hxmlBufferToBuilds(project,_hx_AnonObject({'readline': _hx_local_0}),folder,build_path,hxml,hxml)
		return _hx_local_1()

	@staticmethod
	def _find_nme_project_title(nmml_file):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:267
		f = python_lib_Codecs.open(nmml_file,"r+","utf-8","ignore")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:268
		title = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:269
		while True:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:271
			l = f.readline()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:272
			if (l is None):
				break
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:276
			m = hxsublime_build_Tools._extract_tag.search(l)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:277
			if (m is not None):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:279
				tag = m.group(1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:281
				if ((tag == "meta") or ((tag == "app"))):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:283
					mFile = python_lib_Re.search("\\b(file|title)=\"([ a-z0-9_-]+)\"",l,python_lib_Re.I)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:284
					if (mFile is not None):
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:286
						title = mFile.group(2)
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:287
						break
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:292
		Reflect.field(f,"close")()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:293
		return title

	@staticmethod
	def createHaxeBuildFromNmml(project,target,nmml,display_cmd):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:298
		cmd = list(display_cmd)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:299
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:299
		cmd.append(nmml)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:300
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:300
		cmd.append(target.plattform)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:301
		cmd.extend(target.args)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:303
		nmml_dir = python_lib_os_Path.dirname(nmml)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:305
		r = hxsublime_Execute.runCmd(cmd,None,nmml_dir)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:306
		out = r[0]
		err = r[1]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:307
		io = python_lib_io_StringIO(out)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:308
		def _hx_local_1():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:308
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:308
				return io.readline()
			return python_internal_ArrayImpl._get(hxsublime_build_Tools.hxmlBufferToBuilds(project,_hx_AnonObject({'readline': _hx_local_0}),nmml_dir,nmml_dir,nmml,None), 0)
		return _hx_local_1()

	@staticmethod
	def findHxmlProjects(project,folder):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:314
		builds = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:315
		found = hxsublime_build_Tools.findBuildFiles(folder,"hxml")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:316
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:316
		_g = 0
		while (_g < len(found)):
			build = (found[_g] if _g >= 0 and _g < len(found) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:318
			hxml_file = build[0]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:319
			hxml_folder = build[1]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:321
			b = hxsublime_build_Tools.hxmlToBuilds(project,hxml_file,hxml_folder)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:323
			builds.extend(b)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:326
		return builds

	@staticmethod
	def findNmeProjects(project,folder):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:331
		found = hxsublime_build_Tools.findBuildFiles(folder,"nmml")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:332
		builds = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:333
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:333
		_g = 0
		while (_g < len(found)):
			build = (found[_g] if _g >= 0 and _g < len(found) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:335
			nmml_file = build[0]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:336
			title = hxsublime_build_Tools._find_nme_project_title(nmml_file)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:337
			if (title is not None):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:339
				_g1 = 0
				_g2 = hxsublime_Config.nme_targets
				while (_g1 < len(_g2)):
					t = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
					_g1 = (_g1 + 1)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:341
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:341
					x = hxsublime_build_NmeBuild(project, title, nmml_file, t)
					builds.append(x)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:345
		return builds

	@staticmethod
	def findOpenflProjects(project,folder):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:350
		found = hxsublime_build_Tools.findBuildFiles(folder,"xml")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:351
		builds = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:352
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:352
		_g = 0
		while (_g < len(found)):
			build = (found[_g] if _g >= 0 and _g < len(found) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:354
			openfl_xml = build[0]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:355
			title = hxsublime_build_Tools._find_nme_project_title(openfl_xml)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:356
			if (title is not None):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:358
				_g1 = 0
				_g2 = hxsublime_Config.openfl_targets
				while (_g1 < len(_g2)):
					t = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
					_g1 = (_g1 + 1)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:360
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:360
					x = hxsublime_build_OpenFlBuild(project, title, openfl_xml, t)
					builds.append(x)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/build/Tools.hx:365
		return builds
hxsublime_build_Tools._hx_class = hxsublime_build_Tools
_hx_classes["hxsublime.build.Tools"] = hxsublime_build_Tools


class hxsublime_commands_HaxeSaveAllAndRunCommand(sublime_TextCommand):
	_hx_class_name = "hxsublime.commands.HaxeSaveAllAndRunCommand"
	_hx_fields = []
	_hx_methods = ["run"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = sublime_TextCommand


	def __init__(self,v):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:15
		super().__init__(v)

	def run(self,edit,**args):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:19
		haxe_Log.trace("run HaxeSaveAllAndRunCommand",_hx_AnonObject({'fileName': "Build.hx", 'lineNumber': 19, 'className': "hxsublime.commands.HaxeSaveAllAndRunCommand", 'methodName': "run"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:20
		view = self.view
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:21
		view.window().run_command("save_all")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:22
		hxsublime_project_Projects.currentProject(self.view).runBuild(view)

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_commands_HaxeSaveAllAndRunCommand._hx_class = hxsublime_commands_HaxeSaveAllAndRunCommand
_hx_classes["hxsublime.commands.HaxeSaveAllAndRunCommand"] = hxsublime_commands_HaxeSaveAllAndRunCommand


class hxsublime_commands_HaxeSaveAllAndCheckCommand(sublime_TextCommand):
	_hx_class_name = "hxsublime.commands.HaxeSaveAllAndCheckCommand"
	_hx_fields = []
	_hx_methods = ["run"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = sublime_TextCommand


	def __init__(self,v):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:26
		super().__init__(v)

	def run(self,edit,**args):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:30
		haxe_Log.trace("run HaxeSaveAllAndCheckCommand",_hx_AnonObject({'fileName': "Build.hx", 'lineNumber': 30, 'className': "hxsublime.commands.HaxeSaveAllAndCheckCommand", 'methodName': "run"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:31
		view = self.view
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:32
		view.window().run_command("save_all")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:33
		hxsublime_project_Projects.currentProject(self.view).checkBuild(view)

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_commands_HaxeSaveAllAndCheckCommand._hx_class = hxsublime_commands_HaxeSaveAllAndCheckCommand
_hx_classes["hxsublime.commands.HaxeSaveAllAndCheckCommand"] = hxsublime_commands_HaxeSaveAllAndCheckCommand


class hxsublime_commands_HaxeSaveAllAndBuildCommand(sublime_TextCommand):
	_hx_class_name = "hxsublime.commands.HaxeSaveAllAndBuildCommand"
	_hx_fields = []
	_hx_methods = ["run"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = sublime_TextCommand


	def __init__(self,v):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:37
		super().__init__(v)

	def run(self,edit,**args):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:41
		haxe_Log.trace("run HaxeSaveAllAndBuildCommand",_hx_AnonObject({'fileName': "Build.hx", 'lineNumber': 41, 'className': "hxsublime.commands.HaxeSaveAllAndBuildCommand", 'methodName': "run"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:42
		view = self.view
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:43
		view.window().run_command("save_all")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:44
		hxsublime_project_Projects.currentProject(self.view).justBuild(view)

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_commands_HaxeSaveAllAndBuildCommand._hx_class = hxsublime_commands_HaxeSaveAllAndBuildCommand
_hx_classes["hxsublime.commands.HaxeSaveAllAndBuildCommand"] = hxsublime_commands_HaxeSaveAllAndBuildCommand


class hxsublime_commands_HaxeRunBuildCommand(sublime_TextCommand):
	_hx_class_name = "hxsublime.commands.HaxeRunBuildCommand"
	_hx_fields = []
	_hx_methods = ["run"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = sublime_TextCommand


	def __init__(self,v):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:48
		super().__init__(v)

	def run(self,edit,**args):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:52
		view = self.view
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:53
		haxe_Log.trace("run HaxeRunBuildCommand",_hx_AnonObject({'fileName': "Build.hx", 'lineNumber': 53, 'className': "hxsublime.commands.HaxeRunBuildCommand", 'methodName': "run"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:54
		project = hxsublime_project_Projects.currentProject(self.view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:56
		if project.hasBuild():
			project.runBuild(view)
		else:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:62
			haxe_Log.trace("no builds selected",_hx_AnonObject({'fileName': "Build.hx", 'lineNumber': 62, 'className': "hxsublime.commands.HaxeRunBuildCommand", 'methodName': "run"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:63
			project.extractBuildArgs(view,True)

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_commands_HaxeRunBuildCommand._hx_class = hxsublime_commands_HaxeRunBuildCommand
_hx_classes["hxsublime.commands.HaxeRunBuildCommand"] = hxsublime_commands_HaxeRunBuildCommand


class hxsublime_commands_HaxeSelectBuildCommand(sublime_TextCommand):
	_hx_class_name = "hxsublime.commands.HaxeSelectBuildCommand"
	_hx_fields = []
	_hx_methods = ["run"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = sublime_TextCommand


	def __init__(self,v):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:68
		super().__init__(v)

	def run(self,edit,**args):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:72
		hxsublime_project_Projects.currentProject(self.view).selectBuild(self.view)

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_commands_HaxeSelectBuildCommand._hx_class = hxsublime_commands_HaxeSelectBuildCommand
_hx_classes["hxsublime.commands.HaxeSelectBuildCommand"] = hxsublime_commands_HaxeSelectBuildCommand


class hxsublime_commands_HaxeBuildOnSaveListener(sublime_EventListener):
	_hx_class_name = "hxsublime.commands.HaxeBuildOnSaveListener"
	_hx_fields = []
	_hx_methods = ["on_post_save"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = sublime_EventListener


	def on_post_save(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:80
		validView = ((view is not None) and ((view.file_name() is not None)))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:81
		if validView:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:83
			supportedView = (hxsublime_tools_ViewTools.isSupported(view) or StringTools.endsWith(view.file_name(),".erazor.html"))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:85
			if (supportedView and hxsublime_Settings.checkOnSave()):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:87
				project = hxsublime_project_Projects.currentProject(view)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Build.hx:89
				if project.hasBuild():
					project.checkBuild(view)

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_commands_HaxeBuildOnSaveListener._hx_class = hxsublime_commands_HaxeBuildOnSaveListener
_hx_classes["hxsublime.commands.HaxeBuildOnSaveListener"] = hxsublime_commands_HaxeBuildOnSaveListener


class hxsublime_commands_HaxeDisplayCompletionCommand(sublime_TextCommand):
	_hx_class_name = "hxsublime.commands.HaxeDisplayCompletionCommand"
	_hx_fields = []
	_hx_methods = ["run"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = sublime_TextCommand


	def __init__(self,v):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:19
		super().__init__(v)

	def run(self,edit,**kwArgs):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:23
		input_char = None
		if (kwArgs is None):
			input_char = None
		else:
			input_char = kwArgs.get("input_char",None)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:25
		if (input_char is not None):
			self.view.run_command("insert",python_Lib.anonToDict(_hx_AnonObject({'characters': input_char})))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:32
		if ((input_char != ":") and hxsublime_commands__Completion_Helper.isValidCompletion(self.view,edit,input_char)):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:34
			userActivated = (input_char is None)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:35
			options = hxsublime_completion_hx_CompletionOptions(userActivated)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:37
			if (((input_char is None) or ((input_char == "."))) or (not hxsublime_Settings.topLevelCompletionsOnDemand())):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:39
				haxe_Log.trace("RUN - HaxeDisplayCompletionCommand",_hx_AnonObject({'fileName': "Completion.hx", 'lineNumber': 39, 'className': "hxsublime.commands.HaxeDisplayCompletionCommand", 'methodName': "run"}))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:40
				haxe_Log.trace(("options.userActivated:" + Std.string(options.userActivated)),_hx_AnonObject({'fileName': "Completion.hx", 'lineNumber': 40, 'className': "hxsublime.commands.HaxeDisplayCompletionCommand", 'methodName': "run"}))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:43
				def _hx_local_0(ctx):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:43
					return hxsublime_completion_hx_HxCompletion.commandTriggeredAutoComplete(ctx.project,ctx.view,ctx.offset,options,ctx.prefix)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:42
				f = _hx_local_0
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:46
				hxsublime_completion_CompletionListener.trigger(self.view,False,f)

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_commands_HaxeDisplayCompletionCommand._hx_class = hxsublime_commands_HaxeDisplayCompletionCommand
_hx_classes["hxsublime.commands.HaxeDisplayCompletionCommand"] = hxsublime_commands_HaxeDisplayCompletionCommand


class hxsublime_commands__Completion_Helper:
	_hx_class_name = "hxsublime.commands._Completion.Helper"
	_hx_statics = ["isValidCompletion", "anonFunc", "isOpenParensAfterFunctionDefinition", "isCommaAfterOpenParensInFunctionDefinition"]

	@staticmethod
	def isValidCompletion(view,edit,inputChar):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:56
		valid = True
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:57
		if (inputChar == "("):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:59
			src = hxsublime_tools_ViewTools.getContentUntilFirstCursor(view)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:61
			if hxsublime_commands__Completion_Helper.isOpenParensAfterFunctionDefinition(src):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:63
				haxe_Log.trace("Invalid Completion is open par after function",_hx_AnonObject({'fileName': "Completion.hx", 'lineNumber': 63, 'className': "hxsublime.commands._Completion.Helper", 'methodName': "isValidCompletion"}))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:64
				valid = False
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:68
		if (inputChar == ","):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:70
			src1 = hxsublime_tools_ViewTools.getContentUntilFirstCursor(view)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:71
			if hxsublime_commands__Completion_Helper.isCommaAfterOpenParensInFunctionDefinition(src1):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:73
				haxe_Log.trace("Invalid Completion is open par after function",_hx_AnonObject({'fileName': "Completion.hx", 'lineNumber': 73, 'className': "hxsublime.commands._Completion.Helper", 'methodName': "isValidCompletion"}))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:74
				valid = False
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:77
		return valid

	@staticmethod
	def isOpenParensAfterFunctionDefinition(src):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:84
		lastFunction = src.rfind("function", 0, len(src))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:85
		srcPart = HxString.substr(src,lastFunction,None)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:86
		match = python_lib_Re.match(hxsublime_commands__Completion_Helper.anonFunc,srcPart)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:87
		return (match is not None)

	@staticmethod
	def isCommaAfterOpenParensInFunctionDefinition(src):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:93
		found = hxsublime_tools_HxSrcTools.reverse_search_next_char_on_same_nesting_level(src,["("],(len(src) - 1))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:96
		if (found is not None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:98
			srcUntilComma = HxString.substring(src,0,(found[0] + 1))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Completion.hx:95
			return hxsublime_commands__Completion_Helper.isOpenParensAfterFunctionDefinition(srcUntilComma)
		else:
			return False
hxsublime_commands__Completion_Helper._hx_class = hxsublime_commands__Completion_Helper
_hx_classes["hxsublime.commands._Completion.Helper"] = hxsublime_commands__Completion_Helper


class hxsublime_commands_HaxeRestartServerCommand(sublime_WindowCommand):
	_hx_class_name = "hxsublime.commands.HaxeRestartServerCommand"
	_hx_fields = []
	_hx_methods = ["run"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = sublime_WindowCommand


	def __init__(self,w):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CompletionServer.hx:9
		super().__init__(w)

	def run(self,**kwArgs):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CompletionServer.hx:14
		haxe_Log.trace("run HaxeRestartServerCommand",_hx_AnonObject({'fileName': "CompletionServer.hx", 'lineNumber': 14, 'className': "hxsublime.commands.HaxeRestartServerCommand", 'methodName': "run"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CompletionServer.hx:16
		view = sublime_Sublime.active_window().active_view()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CompletionServer.hx:18
		project = hxsublime_project_Projects.currentProject(view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CompletionServer.hx:20
		project.restartServer(view)

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_commands_HaxeRestartServerCommand._hx_class = hxsublime_commands_HaxeRestartServerCommand
_hx_classes["hxsublime.commands.HaxeRestartServerCommand"] = hxsublime_commands_HaxeRestartServerCommand


class hxsublime_commands__CreateType_State:
	_hx_class_name = "hxsublime.commands._CreateType.State"
	_hx_statics = ["current_create_type_info"]
hxsublime_commands__CreateType_State._hx_class = hxsublime_commands__CreateType_State
_hx_classes["hxsublime.commands._CreateType.State"] = hxsublime_commands__CreateType_State


class hxsublime_commands_HaxeCreateTypeCommand(sublime_WindowCommand):
	_hx_class_name = "hxsublime.commands.HaxeCreateTypeCommand"
	_hx_fields = ["classpath", "win"]
	_hx_methods = ["run", "onDone", "onChange", "onCancel"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = sublime_WindowCommand


	def __init__(self,win):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:29
		self.classpath = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:30
		self.win = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:34
		super().__init__(win)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:35
		self.classpath = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:36
		self.win = win

	def run(self,**kwArgs):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:40
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:43
		paths = kwArgs.get("paths",[])
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:44
		t = kwArgs.get("t","class")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:47
		haxe_Log.trace("createtype",_hx_AnonObject({'fileName': "CreateType.hx", 'lineNumber': 47, 'className': "hxsublime.commands.HaxeCreateTypeCommand", 'methodName': "run"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:50
		view = self.win.active_view()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:52
		project = hxsublime_project_Projects.currentProject(view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:54
		builds = list(project.builds)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:56
		if project.hasBuild():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:58
			x = project.getBuild(view)
			builds.insert(0, x)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:61
		pack = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:63
		if (((len(builds) == 0) and ((view is not None))) and ((view.file_name() is not None))):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:65
			haxe_Log.trace(view.file_name(),_hx_AnonObject({'fileName': "CreateType.hx", 'lineNumber': 65, 'className': "hxsublime.commands.HaxeCreateTypeCommand", 'methodName': "run"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:66
			project.extractBuildArgs(view)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:67
			builds = project.builds
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:70
		if ((len(paths) == 0) and ((view is not None))):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:72
			fn = view.file_name()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:73
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:73
			paths.append(fn)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:76
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:76
		_g1 = 0
		while (_g1 < len(paths)):
			path = (paths[_g1] if _g1 >= 0 and _g1 < len(paths) else None)
			_g1 = (_g1 + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:79
			if python_lib_os_Path.isfile(path):
				path = python_lib_os_Path.dirname(path)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:84
			if (self.classpath is None):
				self.classpath = path
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:89
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:89
			_g11 = 0
			while (_g11 < len(builds)):
				b = (builds[_g11] if _g11 >= 0 and _g11 < len(builds) else None)
				_g11 = (_g11 + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:91
				haxe_Log.trace(("build file: " + HxOverrides.stringOrNull(b.buildFile())),_hx_AnonObject({'fileName': "CreateType.hx", 'lineNumber': 91, 'className': "hxsublime.commands.HaxeCreateTypeCommand", 'methodName': "run"}))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:92
				found = False
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:93
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:93
				_g2 = 0
				_g3 = b.classpaths()
				while (_g2 < len(_g3)):
					cp = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
					_g2 = (_g2 + 1)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:95
					haxe_Log.trace(("class path: " + ("null" if cp is None else cp)),_hx_AnonObject({'fileName': "CreateType.hx", 'lineNumber': 95, 'className': "hxsublime.commands.HaxeCreateTypeCommand", 'methodName': "run"}))
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:96
					haxe_Log.trace(("path: " + ("null" if path is None else path)),_hx_AnonObject({'fileName': "CreateType.hx", 'lineNumber': 96, 'className': "hxsublime.commands.HaxeCreateTypeCommand", 'methodName': "run"}))
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:97
					if StringTools.startsWith(path,cp):
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:100
						self.classpath = HxString.substring(path,0,len(cp))
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:101
						haxe_Log.trace(("this.classpath: " + HxOverrides.stringOrNull(self.classpath)),_hx_AnonObject({'fileName': "CreateType.hx", 'lineNumber': 101, 'className': "hxsublime.commands.HaxeCreateTypeCommand", 'methodName': "run"}))
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:103
						rel_path = HxString.substr(path,(len(cp) + 1),None)
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:105
						haxe_Log.trace(rel_path,_hx_AnonObject({'fileName': "CreateType.hx", 'lineNumber': 105, 'className': "hxsublime.commands.HaxeCreateTypeCommand", 'methodName': "run"}))
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:106
						if (len(rel_path) == 0):
							found = True
						else:
							# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:112
							sub_packs = None
							delimiter = python_lib_Os.sep
							if (delimiter == ""):
								sub_packs = list(rel_path)
							else:
								sub_packs = rel_path.split(delimiter)
							# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:113
							haxe_Log.trace(("subpacks:" + Std.string(sub_packs)),_hx_AnonObject({'fileName': "CreateType.hx", 'lineNumber': 113, 'className': "hxsublime.commands.HaxeCreateTypeCommand", 'methodName': "run"}))
							# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:114
							# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:114
							_g4 = 0
							while (_g4 < len(sub_packs)):
								p = (sub_packs[_g4] if _g4 >= 0 and _g4 < len(sub_packs) else None)
								_g4 = (_g4 + 1)
								# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:117
								if (p.find(".") > -1):
									break
								elif (p is not None):
									# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:122
									# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:122
									pack.append(p)
									# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:124
									found = True
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:130
					if found:
						break
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:135
				if found:
					break
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:139
				haxe_Log.trace(("found: " + Std.string(found)),_hx_AnonObject({'fileName': "CreateType.hx", 'lineNumber': 139, 'className': "hxsublime.commands.HaxeCreateTypeCommand", 'methodName': "run"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:142
		if (self.classpath is None):
			if (len(builds) > 0):
				self.classpath = python_internal_ArrayImpl._get((builds[0] if 0 < len(builds) else None).classpaths(), 0)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:150
		haxe_Log.trace(pack,_hx_AnonObject({'fileName': "CreateType.hx", 'lineNumber': 150, 'className': "hxsublime.commands.HaxeCreateTypeCommand", 'methodName': "run"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:153
		packSuggestion = ".".join([python_Boot.toString1(x1,'') for x1 in pack])
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:154
		if (len(packSuggestion) > 0):
			packSuggestion = (("null" if packSuggestion is None else packSuggestion) + ".")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:158
		sublime_Sublime.status_message(("Current classpath : " + HxOverrides.stringOrNull(self.classpath)))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:159
		def _hx_local_5(inp):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:159
			_g.onDone(inp,t)
		self.win.show_input_panel((("Enter " + ("null" if t is None else t)) + " name : "),packSuggestion,_hx_local_5,self.onChange,self.onCancel)

	def onDone(self,inp,cur_type):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:165
		fn = self.classpath
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:166
		parts = inp.split(".")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:167
		pack = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:169
		cl = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:171
		while (len(parts) > 0):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:173
			p = None
			p = (None if ((len(parts) == 0)) else parts.pop(0))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:175
			fn = python_lib_os_Path.join(fn,p)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:177
			if (hxsublime_tools_Regex.isType.match(p) is not None):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:179
				cl = p
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:180
				break
			else:
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:184
				pack.append(p)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:188
		if (len(parts) > 0):
			cl = (parts[0] if 0 < len(parts) else None)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:193
		fn = (("null" if fn is None else fn) + ".hx")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:195
		src = (((((("package " + HxOverrides.stringOrNull(".".join([python_Boot.toString1(x1,'') for x1 in pack]))) + ";\n\n") + ("null" if cur_type is None else cur_type)) + " ") + ("null" if cl is None else cl)) + " ")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:196
		if (cur_type == "typedef"):
			src = (("null" if src is None else src) + "= ")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:200
		src = (("null" if src is None else src) + "{\n\n\t\n\n}")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:202
		hxsublime_commands__CreateType_State.current_create_type_info.h[fn] = src
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:204
		sublime_Sublime.active_window().open_file(fn)

	def onChange(self,inp):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:211
		haxe_Log.trace(inp,_hx_AnonObject({'fileName': "CreateType.hx", 'lineNumber': 211, 'className': "hxsublime.commands.HaxeCreateTypeCommand", 'methodName': "onChange"}))

	def onCancel(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:216
		haxe_Log.trace("cancel",_hx_AnonObject({'fileName': "CreateType.hx", 'lineNumber': 216, 'className': "hxsublime.commands.HaxeCreateTypeCommand", 'methodName': "onCancel"}))

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.classpath = None
		_hx_o.win = None
hxsublime_commands_HaxeCreateTypeCommand._hx_class = hxsublime_commands_HaxeCreateTypeCommand
_hx_classes["hxsublime.commands.HaxeCreateTypeCommand"] = hxsublime_commands_HaxeCreateTypeCommand


class hxsublime_commands_HaxeCreateTypeListener(sublime_EventListener):
	_hx_class_name = "hxsublime.commands.HaxeCreateTypeListener"
	_hx_fields = []
	_hx_methods = ["on_load", "create_file"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = sublime_EventListener


	def on_load(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:225
		can_create_file = None
		def _hx_local_0():
			key = view.file_name()
			return key in hxsublime_commands__CreateType_State.current_create_type_info.h
		can_create_file = ((((view is not None) and ((view.file_name() is not None))) and _hx_local_0()) and ((view.size() == 0)))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:227
		if can_create_file:
			self.create_file(view)

	def create_file(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:235
		data = None
		key = view.file_name()
		data = hxsublime_commands__CreateType_State.current_create_type_info.h.get(key,None)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:238
		def _hx_local_0(v,edit):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:239
			haxe_Log.trace(data,_hx_AnonObject({'fileName': "CreateType.hx", 'lineNumber': 239, 'className': "hxsublime.commands.HaxeCreateTypeListener", 'methodName': "create_file"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:240
			v.insert(edit,0,data)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:241
			sel = v.sel()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:242
			sel.clear()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:243
			pt = v.text_point(5,1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:244
			sel.add(sublime_Region(pt, pt))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:237
		run_edit = _hx_local_0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/CreateType.hx:247
		hxsublime_tools_ViewTools.asyncEdit(view,run_edit)

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_commands_HaxeCreateTypeListener._hx_class = hxsublime_commands_HaxeCreateTypeListener
_hx_classes["hxsublime.commands.HaxeCreateTypeListener"] = hxsublime_commands_HaxeCreateTypeListener


class hxsublime_commands__Execute_Helper:
	_hx_class_name = "hxsublime.commands._Execute.Helper"
	_hx_statics = ["escape_cmd"]

	@staticmethod
	def escape_cmd(cmd):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:31
		print_cmd = list(cmd)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:32
		l = len(print_cmd)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:33
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:33
		_g = 0
		while (_g < l):
			i = _g
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:35
			e = (print_cmd[i] if i >= 0 and i < len(print_cmd) else None)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:36
			if ((e == "--macro") and ((i < ((l - 1))))):
				python_internal_ArrayImpl._set(print_cmd, (i + 1), (("'" + HxOverrides.stringOrNull(python_internal_ArrayImpl._get(print_cmd, (i + 1)))) + "'"))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:41
		return print_cmd
hxsublime_commands__Execute_Helper._hx_class = hxsublime_commands__Execute_Helper
_hx_classes["hxsublime.commands._Execute.Helper"] = hxsublime_commands__Execute_Helper


class hxsublime_commands_HaxeExecCommand(sublime_WindowCommand):
	_hx_class_name = "hxsublime.commands.HaxeExecCommand"
	_hx_fields = ["is_check_run", "output_view", "proc", "encoding", "quiet"]
	_hx_methods = ["run", "is_enabled", "append_data_str", "append_data", "finish", "on_data", "on_finished"]
	_hx_statics = []
	_hx_interfaces = [sublime_def_exec_ProcessListener]
	_hx_super = sublime_WindowCommand


	def __init__(self,window):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:50
		self.is_check_run = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:51
		self.output_view = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:52
		self.proc = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:53
		self.encoding = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:54
		self.quiet = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:52
		self.proc = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:51
		self.output_view = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:57
		super().__init__(window)

	def run(self,**kwArgs):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:61
		cmd = kwArgs.get("cmd",[])
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:63
		def _hx_local_0(x):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:63
			return (x != "")
		cmd = list(filter(_hx_local_0,cmd))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:65
		file_regex = kwArgs.get("file_regex","")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:66
		line_regex = kwArgs.get("line_regex","")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:67
		working_dir = kwArgs.get("working_dir","")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:68
		self.encoding = kwArgs.get("encoding","utf-8")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:70
		env = None
		_hx_def = dict()
		env = kwArgs.get("env",_hx_def)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:71
		self.quiet = kwArgs.get("quiet",False)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:72
		kill = kwArgs.get("kill",False)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:73
		is_check_run = kwArgs.get("is_check_run",False)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:76
		self.is_check_run = is_check_run
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:78
		if (self.encoding is None):
			self.encoding = python_lib_Sys.getfilesystemencoding()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:83
		if (self.output_view is None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:86
			self.output_view = self.window.create_output_panel("exec")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:87
			self.output_view.settings().set("word_wrap",True)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:89
		if kill:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:91
			if (self.proc is not None):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:93
				self.proc.kill()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:94
				self.proc = None
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:95
				self.append_data(None,hxsublime_support_StringTools.encode("[Cancelled]","utf-8"))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:97
			return
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:103
		if (((working_dir == "") and ((self.window.active_view() is not None))) and ((self.window.active_view().file_name() is not None))):
			working_dir = python_lib_os_Path.dirname(self.window.active_view().file_name())
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:109
		self.output_view.settings().set("result_file_regex",file_regex)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:110
		self.output_view.settings().set("result_line_regex",line_regex)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:111
		self.output_view.settings().set("result_base_dir",working_dir)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:115
		self.window.create_output_panel("exec")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:120
		self.proc = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:121
		if (not self.quiet):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:124
			def _hx_local_1(a):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:125
				a1 = None
				_this = a.split("\"")
				a1 = "\\\"".join([python_Boot.toString1(x1,'') for x1 in _this])
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:126
				if (len(a1) >= 2):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:127
					if StringTools.startsWith(a1,"\\\""):
						a1 = ("\"" + HxOverrides.stringOrNull(HxString.substr(a1,2,None)))
					else:
						a1 = a1
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:128
					if StringTools.endsWith(a1,"\\\""):
						a1 = (HxOverrides.stringOrNull(HxString.substring(a1,0,(len(a1) - 2))) + "\"")
					else:
						a1 = a1
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:130
				return a1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:123
			escape_arg = _hx_local_1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:133
			def _hx_local_2():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:133
				_this1 = list(map(escape_arg,cmd))
				return " ".join([python_Boot.toString1(x1,'') for x1 in _this1])
			haxe_Log.trace(("Running Command: " + HxOverrides.stringOrNull(_hx_local_2())),_hx_AnonObject({'fileName': "Execute.hx", 'lineNumber': 133, 'className': "hxsublime.commands.HaxeExecCommand", 'methodName': "run"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:135
			sublime_Sublime.status_message("Building")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:139
		show_panel_on_build = sublime_Sublime.load_settings("Preferences.sublime-settings").get("show_panel_on_build",True)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:140
		if show_panel_on_build:
			self.window.run_command("show_panel",python_Lib.anonToDict(_hx_AnonObject({'panel': "output.exec"})))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:146
		merged_env = env.copy()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:147
		if (self.window.active_view() is not None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:149
			user_env = self.window.active_view().settings().get("build_env")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:150
			if (user_env is not None):
				merged_env.update(user_env)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:158
		if (working_dir != ""):
			python_lib_Os.chdir(working_dir)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:168
		try:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:174
			d = python__KwArgs_KwArgs_Impl_.toDictHelper(kwArgs,None)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:175
			if "working_dir" in d:
				del d["working_dir"]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:176
			if "file_regex" in d:
				del d["file_regex"]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:177
			if "line_regex" in d:
				del d["line_regex"]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:178
			if "encoding" in d:
				del d["encoding"]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:179
			if "is_check_run" in d:
				del d["is_check_run"]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:180
			if "env" in d:
				del d["env"]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:181
			if "cmd" in d:
				del d["cmd"]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:184
			self.proc = sublime_def_exec_AsyncProcess(cmd, None, merged_env, self, "", False)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:186
			def _hx_local_3():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:186
				_this2 = hxsublime_commands__Execute_Helper.escape_cmd(cmd)
				return " ".join([python_Boot.toString1(x1,'') for x1 in _this2])
			self.append_data(self.proc,hxsublime_support_StringTools.encode((("Running Command: " + HxOverrides.stringOrNull(_hx_local_3())) + "\n"),"utf-8"))
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			e = _hx_e1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:191
			self.append_data_str(None,(Std.string(e) + "\n"))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:192
			self.append_data_str(None,(("[cmd:  " + Std.string(cmd)) + "]\n"))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:193
			self.append_data_str(None,(("[dir:  " + HxOverrides.stringOrNull(python_lib_Os.getcwdb().decode("utf-8"))) + "]\n"))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:194
			if "PATH" in merged_env:
				self.append_data_str(None,(("[path: " + HxOverrides.stringOrNull(merged_env.get("PATH",""))) + "]\n"))
			else:
				self.append_data_str(None,(("[path: " + Std.string(python_lib_Os.environ.get("PATH",""))) + "]\n"))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:202
			if (not self.quiet):
				self.append_data_str(None,"[Finished]")

	def is_enabled(self,**kwArgs):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:210
		kill = kwArgs.get("kill",False)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:211
		if kill:
			return ((self.proc is not None) and self.proc.poll())
		else:
			return True

	def append_data_str(self,proc,data):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:223
		self.append_data(proc,hxsublime_support_StringTools.encode(data,"utf-8"))

	def append_data(self,proc,data):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:226
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:229
		if (proc != self.proc):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:233
			if (proc is not None):
				try:
					proc.kill()
				except Exception as _hx_e:
					_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
					pass
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:244
			return
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:247
		st = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:248
		try:
			st = data.decode(self.encoding)
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			e1 = _hx_e1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:254
			st = (("[Decode error - output not " + HxOverrides.stringOrNull(self.encoding)) + "]\n")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:255
			proc = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:260
		if (self.is_check_run and ((st.find("Embedding assets failed! We encountered an error accessing") > -1))):
			return
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:267
		st = StringTools.replace(StringTools.replace(st,"\r\n","\n"),"\r","\n")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:269
		sel = self.output_view.sel()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:270
		selection_was_at_end = ((python_lib_Builtins.len(sel) == 1) and ((sel[0] == sublime_Region(self.output_view.size()))))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:273
		def _hx_local_0(v,edit):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:275
			v.set_read_only(False)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:277
			v.insert(edit,_g.output_view.size(),st)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:278
			if selection_was_at_end:
				v.show(_g.output_view.size())
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:283
			v.set_read_only(True)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:272
		do_edit = _hx_local_0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:285
		hxsublime_tools_ViewTools.asyncEdit(self.output_view,do_edit)

	def finish(self,proc):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:291
		v = self.output_view
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:293
		if (not self.quiet):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:295
			elapsed = (python_lib_Time.time() - proc.start_time)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:296
			exit_code = proc.exit_code()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:299
			if ((exit_code == 0) or ((exit_code is None))):
				self.append_data_str(proc,(("[Finished in " + Std.string(elapsed)) + "]"))
			else:
				self.append_data_str(proc,(((("[Finished in " + Std.string(elapsed)) + " with exit code ") + Std.string(exit_code)) + "]"))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:308
		if (proc != self.proc):
			return
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:315
		v.sel().clear()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:316
		v.sel().add(sublime_Region(0))

	def on_data(self,proc,data):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:322
		def _hx_local_0():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:322
			haxe_Log.trace(data,_hx_AnonObject({'fileName': "Execute.hx", 'lineNumber': 322, 'className': "hxsublime.commands.HaxeExecCommand", 'methodName': "on_data"}))
		sublime_Sublime.set_timeout(_hx_local_0,0)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:323
		def _hx_local_1():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:323
			f = self.append_data
			a1 = proc
			a2 = data
			def _hx_local_2():
				f(a1,a2)
			return _hx_local_2
		sublime_Sublime.set_timeout(_hx_local_1(),0)

	def on_finished(self,proc):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:328
		def _hx_local_0():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Execute.hx:328
			f = self.finish
			a1 = proc
			def _hx_local_1():
				f(a1)
			return _hx_local_1
		sublime_Sublime.set_timeout(_hx_local_0(),0)

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.is_check_run = None
		_hx_o.output_view = None
		_hx_o.proc = None
		_hx_o.encoding = None
		_hx_o.quiet = None
hxsublime_commands_HaxeExecCommand._hx_class = hxsublime_commands_HaxeExecCommand
_hx_classes["hxsublime.commands.HaxeExecCommand"] = hxsublime_commands_HaxeExecCommand


class hxsublime_commands_HaxeFindDeclarationCommand(sublime_TextCommand):
	_hx_class_name = "hxsublime.commands.HaxeFindDeclarationCommand"
	_hx_fields = []
	_hx_methods = ["run", "helperMethod", "run1", "handleSuccessfulResult"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = sublime_TextCommand


	def __init__(self,v):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:31
		super().__init__(v)

	def run(self,edit,**_):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:35
		self.run1(True)

	def helperMethod(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:40
		return "hxsublime.FindDeclaration.__sublimeFindDecl"

	def run1(self,useDisplay,order = 1):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:45
		if (order is None):
			order = 1
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:44
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:46
		haxe_Log.trace("run HaxeFindDeclarationCommand",_hx_AnonObject({'fileName': "FindDeclaration.hx", 'lineNumber': 46, 'className': "hxsublime.commands.HaxeFindDeclarationCommand", 'methodName': "run1"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:47
		view = self.view
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:49
		if (view.file_name() is None):
			return
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:54
		project = hxsublime_project_Projects.currentProject(view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:57
		if (not project.hasBuild()):
			project.extractBuildArgs(view,False)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:62
		if (not project.hasBuild()):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:64
			project.extractBuildArgs(view,True)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:65
			return
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:70
		helperMethod = self.helperMethod()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:72
		src = hxsublime_tools_ViewTools.getContent(view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:75
		packageMatch = python_lib_Re.match(hxsublime_tools_Regex.package_line,src)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:77
		usingPos = None
		if (packageMatch is None):
			usingPos = 0
		else:
			usingPos = packageMatch.end(0)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:79
		usingInsert = "using hxsublime.FindDeclaration;"
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:81
		srcBeforeUsing = HxString.substring(src,0,usingPos)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:85
		sel = view.sel()[0]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:86
		pos = sel.begin()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:88
		exprEnd = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:89
		exprStart = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:91
		if (sel.end() == pos):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:94
			r = hxsublime_commands__FindDeclaration_Helper.getWordAt(view,src,pos)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:95
			word_str = r[0]
			word_start = r[1]
			word_end = r[2]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:97
			chars = ["{", "+", "-", "(", "[", "*", "/", "=", ";", ":"]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:98
			res = hxsublime_tools_HxSrcTools.reverse_search_next_char_on_same_nesting_level(src,chars,(word_end - 1))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:100
			res = hxsublime_tools_HxSrcTools.skipWhitespaceOrComments(src,(res[0] + 1))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:104
			exprEnd = word_end
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:105
			exprStart = res[0]
		else:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:109
			exprStart = pos
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:110
			exprEnd = sel.end()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:113
		srcBeforeExpr = HxString.substring(src,usingPos,exprStart)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:115
		srcAfterExpr = HxString.substr(src,exprEnd,None)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:117
		exprString = HxString.substring(src,exprStart,exprEnd)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:120
		displayStr = None
		if useDisplay:
			displayStr = ".|"
		else:
			displayStr = ""
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:122
		insertBefore = (("null" if helperMethod is None else helperMethod) + "(")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:125
		orderStr = Std.string(order)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:126
		insertAfter = (((", " + ("null" if orderStr is None else orderStr)) + ")") + ("null" if displayStr is None else displayStr))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:129
		newSrc = ((((((("null" if srcBeforeUsing is None else srcBeforeUsing) + ("null" if usingInsert is None else usingInsert)) + ("null" if srcBeforeExpr is None else srcBeforeExpr)) + ("null" if insertBefore is None else insertBefore)) + ("null" if exprString is None else exprString)) + ("null" if insertAfter is None else insertAfter)) + ("null" if srcAfterExpr is None else srcAfterExpr))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:133
		r1 = hxsublime_commands__FindDeclaration_Helper.prepareBuild(view,project,useDisplay,newSrc)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:134
		build = r1[0]
		temp_path = r1[1]
		tempFile = r1[2]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:137
		def _hx_local_0(out,err):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:138
			hxsublime_Temp.removePath(temp_path)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:140
			filePos = python_lib_Re.compile("\\|\\|\\|\\|\\|([^|]+)\\|\\|\\|\\|\\|",python_lib_Re.I)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:142
			res1 = python_lib_Re.search(filePos,out)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:143
			if (res1 is not None):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:146
				json_str = res1.group(1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:147
				jsonResult = python_lib_Json.loads(json_str)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:149
				if "error" in jsonResult:
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:151
					error = jsonResult.get("error",None)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:152
					haxe_Log.trace("nothing found (1), cannot find declaration",_hx_AnonObject({'fileName': "FindDeclaration.hx", 'lineNumber': 152, 'className': "hxsublime.commands.HaxeFindDeclarationCommand", 'methodName': "run1"}))
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:153
					if ((order == 1) and useDisplay):
						_g.run1(True,2)
					elif ((order == 2) and useDisplay):
						_g.run1(True,3)
				else:
					_g.handleSuccessfulResult(view,jsonResult,usingInsert,insertBefore,insertAfter,exprEnd,build,temp_path,tempFile)
			elif ((order == 1) and useDisplay):
				_g.run1(True,2)
			elif ((order == 2) and useDisplay):
				_g.run1(True,3)
			elif useDisplay:
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:179
				haxe_Log.trace("nothing found yet (2), try again without display (workaround)",_hx_AnonObject({'fileName': "FindDeclaration.hx", 'lineNumber': 179, 'className': "hxsublime.commands.HaxeFindDeclarationCommand", 'methodName': "run1"}))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:180
				_g.run1(False)
			else:
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:184
				hxsublime_panel_Panels.defaultPanel().writeln(("Cannot find declaration for expression " + HxOverrides.stringOrNull(exprString.strip(None))))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:185
				haxe_Log.trace("nothing found (3), cannot find declaration",_hx_AnonObject({'fileName': "FindDeclaration.hx", 'lineNumber': 185, 'className': "hxsublime.commands.HaxeFindDeclarationCommand", 'methodName': "run1"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:136
		cb = _hx_local_0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:190
		build.run(project,view,False,cb)

	def handleSuccessfulResult(self,view,jsonResult,usingInsert,insertBefore,insertAfter,exprEnd,build,temp_path,tempFile):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:195
		file = jsonResult.get("file",None)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:196
		_hx_min = jsonResult.get("min",0)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:197
		_hx_max = jsonResult.get("max",0)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:199
		absPath = hxsublime_tools_PathTools.joinNorm(build.getBuildFolder(),file)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:201
		if (absPath == tempFile):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:203
			if (_hx_min > exprEnd):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:205
				_hx_min = (_hx_min - len(insertAfter))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:206
				_hx_min = (_hx_min - len(insertBefore))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:208
			_hx_min = (_hx_min - len(usingInsert))
		else:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:215
			f = python_lib_Codecs.open(absPath,"r","utf-8")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:216
			realSrc = f.read()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:217
			Reflect.field(f,"close")()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:222
			offset = 0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:223
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:223
			_g = 0
			while (_g < _hx_min):
				i = _g
				_g = (_g + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:225
				if ((("" if (((i < 0) or ((i >= len(realSrc))))) else realSrc[i])) == "\r"):
					offset = (offset + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:230
			haxe_Log.trace(("offset: " + Std.string(offset)),_hx_AnonObject({'fileName': "FindDeclaration.hx", 'lineNumber': 230, 'className': "hxsublime.commands.HaxeFindDeclarationCommand", 'methodName': "handleSuccessfulResult"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:232
			_hx_min = (_hx_min - offset)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:235
		if (absPath == tempFile):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:239
			targetView = view
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:242
			haxe_Log.trace(("line ending: " + Std.string(view.settings().get("line_ending"))),_hx_AnonObject({'fileName': "FindDeclaration.hx", 'lineNumber': 242, 'className': "hxsublime.commands.HaxeFindDeclarationCommand", 'methodName': "handleSuccessfulResult"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:244
			targetView.sel().clear()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:245
			targetView.sel().add(sublime_Region(_hx_min))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:247
			targetView.show(sublime_Region(_hx_min))
		else:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:252
			hxsublime_commands__FindDeclaration_State.findDeclFile = absPath
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:253
			hxsublime_commands__FindDeclaration_State.findDeclPos = _hx_min
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:255
			view.window().open_file(absPath)

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_commands_HaxeFindDeclarationCommand._hx_class = hxsublime_commands_HaxeFindDeclarationCommand
_hx_classes["hxsublime.commands.HaxeFindDeclarationCommand"] = hxsublime_commands_HaxeFindDeclarationCommand


class hxsublime_commands__FindDeclaration_State:
	_hx_class_name = "hxsublime.commands._FindDeclaration.State"
	_hx_statics = ["findDeclFile", "findDeclPos"]
hxsublime_commands__FindDeclaration_State._hx_class = hxsublime_commands__FindDeclaration_State
_hx_classes["hxsublime.commands._FindDeclaration.State"] = hxsublime_commands__FindDeclaration_State


class hxsublime_commands__FindDeclaration_Helper:
	_hx_class_name = "hxsublime.commands._FindDeclaration.Helper"
	_hx_statics = ["plugin_path", "getWordAt", "prepareBuild"]

	@staticmethod
	def getWordAt(view,src,pos):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:272
		word = view.word(pos)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:274
		wordStart = word.a
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:275
		wordEnd = word.b
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:277
		wordStr = HxString.substring(src,wordStart,wordEnd)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:279
		return (wordStr, wordStart, wordEnd)

	@staticmethod
	def prepareBuild(view,project,useDisplay,newSrc):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:284
		build = project.getBuild(view).copy()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:285
		build.addArg(("-D", "no-inline"))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:287
		r = hxsublime_Temp.createTempPathAndFile(build,view.file_name(),newSrc)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:288
		tempPath = r[0]
		tempFile = r[1]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:290
		build.addClasspath(tempPath)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:292
		build.addClasspath(python_lib_os_Path.join(hxsublime_commands__FindDeclaration_Helper.plugin_path,"haxetools"))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:295
		haxe_Log.trace(build.classpaths,_hx_AnonObject({'fileName': "FindDeclaration.hx", 'lineNumber': 295, 'className': "hxsublime.commands._FindDeclaration.Helper", 'methodName': "prepareBuild"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:297
		build.addArg(("-dce", "no"))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:299
		if useDisplay:
			build.setAutoCompletion((("null" if tempFile is None else tempFile) + "@0"),False)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:303
		return (build, tempPath, tempFile)
hxsublime_commands__FindDeclaration_Helper._hx_class = hxsublime_commands__FindDeclaration_Helper
_hx_classes["hxsublime.commands._FindDeclaration.Helper"] = hxsublime_commands__FindDeclaration_Helper


class hxsublime_commands_HaxeFindDeclarationListener(sublime_EventListener):
	_hx_class_name = "hxsublime.commands.HaxeFindDeclarationListener"
	_hx_fields = []
	_hx_methods = ["on_activated"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = sublime_EventListener


	def on_activated(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:312
		if ((view is not None) and ((view.file_name() is not None))):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:314
			if (view.file_name() == hxsublime_commands__FindDeclaration_State.findDeclFile):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:316
				view.sel().clear()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:318
				_hx_min = hxsublime_commands__FindDeclaration_State.findDeclPos
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:320
				view.sel().add(sublime_Region(_hx_min))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:325
				def _hx_local_0():
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:325
					view.show_at_center(sublime_Region(_hx_min))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:323
				show = _hx_local_0
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:327
				sublime_Sublime.set_timeout(show,70)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:329
			hxsublime_commands__FindDeclaration_State.findDeclFile = None
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/FindDeclaration.hx:330
			hxsublime_commands__FindDeclaration_State.findDeclPos = None

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_commands_HaxeFindDeclarationListener._hx_class = hxsublime_commands_HaxeFindDeclarationListener
_hx_classes["hxsublime.commands.HaxeFindDeclarationListener"] = hxsublime_commands_HaxeFindDeclarationListener


class hxsublime_commands_HaxeGenerateUsingCommand(sublime_TextCommand):
	_hx_class_name = "hxsublime.commands.HaxeGenerateUsingCommand"
	_hx_fields = []
	_hx_methods = ["run"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = sublime_TextCommand


	def __init__(self,v):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GenerateImport.hx:10
		super().__init__(v)

	def run(self,edit,**_):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GenerateImport.hx:15
		haxe_Log.trace("run HaxeGenerateUsingCommand",_hx_AnonObject({'fileName': "GenerateImport.hx", 'lineNumber': 15, 'className': "hxsublime.commands.HaxeGenerateUsingCommand", 'methodName': "run"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GenerateImport.hx:16
		hxsublime_HaxeImportGenerator.generateUsing(self.view,edit)

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_commands_HaxeGenerateUsingCommand._hx_class = hxsublime_commands_HaxeGenerateUsingCommand
_hx_classes["hxsublime.commands.HaxeGenerateUsingCommand"] = hxsublime_commands_HaxeGenerateUsingCommand


class hxsublime_commands_HaxeGenerateImportCommand(sublime_TextCommand):
	_hx_class_name = "hxsublime.commands.HaxeGenerateImportCommand"
	_hx_fields = []
	_hx_methods = ["run"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = sublime_TextCommand


	def __init__(self,v):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GenerateImport.hx:20
		super().__init__(v)

	def run(self,edit,**_):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GenerateImport.hx:24
		haxe_Log.trace("run HaxeGenerateImportCommand",_hx_AnonObject({'fileName': "GenerateImport.hx", 'lineNumber': 24, 'className': "hxsublime.commands.HaxeGenerateImportCommand", 'methodName': "run"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GenerateImport.hx:25
		hxsublime_HaxeImportGenerator.generateImport(self.view,edit)

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_commands_HaxeGenerateImportCommand._hx_class = hxsublime_commands_HaxeGenerateImportCommand
_hx_classes["hxsublime.commands.HaxeGenerateImportCommand"] = hxsublime_commands_HaxeGenerateImportCommand


class hxsublime_commands_HaxeGetTypeOfExprCommand(hxsublime_commands_HaxeFindDeclarationCommand):
	_hx_class_name = "hxsublime.commands.HaxeGetTypeOfExprCommand"
	_hx_fields = []
	_hx_methods = ["helperMethod", "handleSuccessfulResult"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = hxsublime_commands_HaxeFindDeclarationCommand


	def __init__(self,v):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GetExprType.hx:9
		super().__init__(v)

	def helperMethod(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GetExprType.hx:13
		return "hxsublime.FindDeclaration.__getType"

	def handleSuccessfulResult(self,view,json_res,using_insert,insert_before,insert_after,expr_end,build,temp_path,temp_file):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GetExprType.hx:19
		t = json_res.get("type",None)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GetExprType.hx:20
		e = json_res.get("expr",None)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GetExprType.hx:22
		msg = (((("Expr: " + ("null" if e is None else e)) + "\n") + "Type: ") + ("null" if t is None else t))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GetExprType.hx:24
		hxsublime_panel_Panels.slidePanel().writeln(msg,None,False)

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_commands_HaxeGetTypeOfExprCommand._hx_class = hxsublime_commands_HaxeGetTypeOfExprCommand
_hx_classes["hxsublime.commands.HaxeGetTypeOfExprCommand"] = hxsublime_commands_HaxeGetTypeOfExprCommand


class hxsublime_commands_HaxeGotoBaseCommand(sublime_TextCommand):
	_hx_class_name = "hxsublime.commands.HaxeGotoBaseCommand"
	_hx_fields = ["selecting_build"]
	_hx_methods = ["getEntries", "getData", "getFile", "getSrcPos", "run"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = sublime_TextCommand


	def __init__(self,v):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:26
		self.selecting_build = None
		self.selecting_build = False
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:24
		super().__init__(v)

	def getEntries(self,types):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:30
		raise _HxException("abstract method")

	def getData(self,types):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:34
		raise _HxException("abstract method")

	def getFile(self,data_entry):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:39
		raise _HxException("abstract method")

	def getSrcPos(self,data_entry):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:44
		raise _HxException("abstract method")

	def run(self,edit,**kwArgs):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:47
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:51
		haxe_Log.trace("run HaxeListBuildFieldsCommand",_hx_AnonObject({'fileName': "GotoBase.hx", 'lineNumber': 51, 'className': "hxsublime.commands.HaxeGotoBaseCommand", 'methodName': "run"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:53
		view = self.view
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:55
		project = hxsublime_project_Projects.currentProject(view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:58
		if (not project.hasBuild()):
			project.extractBuildArgs(view,False)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:63
		if (not project.hasBuild()):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:65
			project.extractBuildArgs(view,True)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:66
			return
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:69
		build = project.getBuild(view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:71
		bundle = build.getTypes().merge(build.stdBundle())
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:75
		bundle_types = bundle.allTypesAndEnumConstructorsWithInfo()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:77
		filtered_types = haxe_ds_StringMap()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:79
		_hx_local_0 = bundle_types.keys()
		while _hx_local_0.hasNext():
			k = _hx_local_0.next()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:81
			t = bundle_types.h.get(k,None)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:82
			if build.isTypeAvailable(t):
				filtered_types.h[k] = t
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:89
		function_list = self.getEntries(filtered_types)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:90
		function_list_data = self.getData(filtered_types)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:93
		haxe_Log.trace(Std.string(function_list),_hx_AnonObject({'fileName': "GotoBase.hx", 'lineNumber': 93, 'className': "hxsublime.commands.HaxeGotoBaseCommand", 'methodName': "run"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:95
		haxe_Log.trace(Std.string(len(function_list)),_hx_AnonObject({'fileName': "GotoBase.hx", 'lineNumber': 95, 'className': "hxsublime.commands.HaxeGotoBaseCommand", 'methodName': "run"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:98
		self.selecting_build = True
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:99
		sublime_Sublime.status_message("Please select a type")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:101
		win = view.window()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:103
		sel = view.sel()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:106
		if ((python_lib_Builtins.len(sel) == 1) and ((sel[0].begin() != sel[0].end()))):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:108
			init = None
			_this = hxsublime_tools_ViewTools.getContent(view)
			startIndex = sel[0].begin()
			endIndex = sel[0].end()
			init = HxString.substring(_this,startIndex,endIndex)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:109
			init1 = None
			def _hx_local_1():
				_this1 = EReg("^[A-Za-z_0-9]*$", "")
				_this1.matchObj = python_lib_Re.search(_this1.pattern,init)
				return (_this1.matchObj is not None)
			if _hx_local_1():
				init1 = init
			else:
				init1 = ""
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:110
			hxsublime_commands__GotoBase_State._init_text = init1
		elif (python_lib_Builtins.len(sel) == 1):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:114
			reg = view.word(sel[0].begin())
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:115
			init2 = None
			_this2 = hxsublime_tools_ViewTools.getContent(view)
			startIndex1 = reg.begin()
			endIndex1 = reg.end()
			init2 = HxString.substring(_this2,startIndex1,endIndex1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:116
			init3 = None
			def _hx_local_2():
				_this3 = EReg("^[A-Za-z_0-9]*$", "")
				_this3.matchObj = python_lib_Re.search(_this3.pattern,init2)
				return (_this3.matchObj is not None)
			if _hx_local_2():
				init3 = init2
			else:
				init3 = ""
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:117
			hxsublime_commands__GotoBase_State._init_text = init3
		else:
			hxsublime_commands__GotoBase_State._init_text = ""
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:124
		def _hx_local_4(i):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:126
			hxsublime_commands__GotoBase_State._is_open = False
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:127
			hxsublime_commands__GotoBase_State._init_text = ""
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:128
			if (i >= 0):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:130
				selected_type = (function_list_data[i] if i >= 0 and i < len(function_list_data) else None)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:131
				haxe_Log.trace(("selected field: " + Std.string(selected_type[0])),_hx_AnonObject({'fileName': "GotoBase.hx", 'lineNumber': 131, 'className': "hxsublime.commands.HaxeGotoBaseCommand", 'methodName': "run"}))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:133
				src_pos = _g.getSrcPos(selected_type[1])
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:135
				goto_file = _g.getFile(selected_type[1])
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:137
				hxsublime_commands__GotoBase_State._find_decl_file = goto_file
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:139
				haxe_Log.trace(("find_decl_file: " + Std.string(hxsublime_commands__GotoBase_State._find_decl_file)),_hx_AnonObject({'fileName': "GotoBase.hx", 'lineNumber': 139, 'className': "hxsublime.commands.HaxeGotoBaseCommand", 'methodName': "run"}))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:140
				if (src_pos is not None):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:142
					hxsublime_commands__GotoBase_State._find_decl_pos = src_pos
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:143
					haxe_Log.trace(("src_pos" + Std.string(src_pos)),_hx_AnonObject({'fileName': "GotoBase.hx", 'lineNumber': 143, 'className': "hxsublime.commands.HaxeGotoBaseCommand", 'methodName': "run"}))
				else:
					hxsublime_commands__GotoBase_State._find_decl_pos = 0
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:153
				def _hx_local_3():
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:153
					win.open_file(goto_file)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:151
				show = _hx_local_3
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:156
				sublime_Sublime.set_timeout(show,130)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:123
		onSelected = _hx_local_4
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:159
		hxsublime_commands__GotoBase_State._is_open = True
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:160
		win.show_quick_panel(function_list,onSelected,sublime_Sublime.MONOSPACE_FONT)

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.selecting_build = None
hxsublime_commands_HaxeGotoBaseCommand._hx_class = hxsublime_commands_HaxeGotoBaseCommand
_hx_classes["hxsublime.commands.HaxeGotoBaseCommand"] = hxsublime_commands_HaxeGotoBaseCommand


class hxsublime_commands_HaxeGotoAnythingCommand(hxsublime_commands_HaxeGotoBaseCommand):
	_hx_class_name = "hxsublime.commands.HaxeGotoAnythingCommand"
	_hx_fields = []
	_hx_methods = ["getEntries", "toEntry", "getData", "getFile", "getSrcPos"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = hxsublime_commands_HaxeGotoBaseCommand


	def __init__(self,v):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoAnything.hx:18
		super().__init__(v)

	def getEntries(self,types):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoAnything.hx:23
		fields = None
		_g = []
		_hx_local_1 = types.keys()
		while _hx_local_1.hasNext():
			k = _hx_local_1.next()
			_g1 = 0
			_g2 = types.h.get(k,None).allFieldsList()
			while (_g1 < len(_g2)):
				p = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
				_g1 = (_g1 + 1)
				x = [((HxOverrides.stringOrNull(p.toString()) + " - ") + HxOverrides.stringOrNull(p.kind)), p.type._file]
				_g.append(x)
		fields = _g
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoAnything.hx:24
		types1 = None
		_g11 = []
		_hx_local_3 = types.keys()
		while _hx_local_3.hasNext():
			k1 = _hx_local_3.next()
			def _hx_local_2():
				_this = types.h.get(k1,None)
				return _this._file
			x1 = [k1, _hx_local_2()]
			_g11.append(x1)
		types1 = _g11
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoAnything.hx:25
		fields.extend(types1)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoAnything.hx:26
		return fields

	def toEntry(self,e):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoAnything.hx:29
		return e

	def getData(self,types):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoAnything.hx:33
		fields = None
		_g = []
		_hx_local_1 = types.keys()
		while _hx_local_1.hasNext():
			k = _hx_local_1.next()
			_g1 = 0
			_g2 = types.h.get(k,None).allFieldsList()
			while (_g1 < len(_g2)):
				p = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
				_g1 = (_g1 + 1)
				x = None
				b = self.toEntry(p)
				x = (((("null" if k is None else k) + ".") + HxOverrides.stringOrNull(p.name)), b)
				_g.append(x)
		fields = _g
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoAnything.hx:34
		types1 = None
		_g11 = []
		_hx_local_2 = types.keys()
		while _hx_local_2.hasNext():
			k1 = _hx_local_2.next()
			x1 = None
			b1 = self.toEntry(types.h.get(k1,None))
			x1 = (k1, b1)
			_g11.append(x1)
		types1 = _g11
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoAnything.hx:35
		fields.extend(types1)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoAnything.hx:36
		return fields

	def getFile(self,dataEntry):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoAnything.hx:41
		return dataEntry.file()

	def getSrcPos(self,dataEntry):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoAnything.hx:46
		return dataEntry.srcPos()

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_commands_HaxeGotoAnythingCommand._hx_class = hxsublime_commands_HaxeGotoAnythingCommand
_hx_classes["hxsublime.commands.HaxeGotoAnythingCommand"] = hxsublime_commands_HaxeGotoAnythingCommand


class hxsublime_commands__GotoBase_State:
	_hx_class_name = "hxsublime.commands._GotoBase.State"
	_hx_statics = ["_find_decl_file", "_find_decl_pos", "_init_text", "_is_open"]
hxsublime_commands__GotoBase_State._hx_class = hxsublime_commands__GotoBase_State
_hx_classes["hxsublime.commands._GotoBase.State"] = hxsublime_commands__GotoBase_State


class hxsublime_commands_HaxeGotoBaseListener(sublime_EventListener):
	_hx_class_name = "hxsublime.commands.HaxeGotoBaseListener"
	_hx_fields = []
	_hx_methods = ["on_activated"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = sublime_EventListener


	def on_activated(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:172
		find_pos = hxsublime_commands__GotoBase_State._find_decl_pos
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:173
		find_file = hxsublime_commands__GotoBase_State._find_decl_file
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:175
		if ((view is not None) and hxsublime_commands__GotoBase_State._is_open):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:177
			hxsublime_commands__GotoBase_State._is_open = False
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:179
			hxsublime_tools_ViewTools.insertAtCursor(view,hxsublime_commands__GotoBase_State._init_text)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:180
			hxsublime_commands__GotoBase_State._init_text = ""
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:184
		if ((view is not None) and ((view.file_name() is not None))):
			if (view.file_name() == find_file):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:190
				view.sel().clear()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:192
				_hx_min = find_pos
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:194
				view.sel().add(sublime_Region(_hx_min))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:196
				haxe_Log.trace(("show at:" + Std.string(_hx_min)),_hx_AnonObject({'fileName': "GotoBase.hx", 'lineNumber': 196, 'className': "hxsublime.commands.HaxeGotoBaseListener", 'methodName': "on_activated"}))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:200
				def _hx_local_0():
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:201
					haxe_Log.trace(("show at:" + Std.string(_hx_min)),_hx_AnonObject({'fileName': "GotoBase.hx", 'lineNumber': 201, 'className': "hxsublime.commands.HaxeGotoBaseListener", 'methodName': "on_activated"}))
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:202
					view.show_at_center(sublime_Region(_hx_min))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:199
				show = _hx_local_0
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:204
				sublime_Sublime.set_timeout(show,100)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:205
				hxsublime_commands__GotoBase_State._find_decl_file = None
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBase.hx:206
				hxsublime_commands__GotoBase_State._find_decl_pos = None

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_commands_HaxeGotoBaseListener._hx_class = hxsublime_commands_HaxeGotoBaseListener
_hx_classes["hxsublime.commands.HaxeGotoBaseListener"] = hxsublime_commands_HaxeGotoBaseListener


class hxsublime_commands_HaxeGotoBuildFieldsCommand(hxsublime_commands_HaxeGotoBaseCommand):
	_hx_class_name = "hxsublime.commands.HaxeGotoBuildFieldsCommand"
	_hx_fields = []
	_hx_methods = ["getEntries", "getData", "getFile", "getSrcPos"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = hxsublime_commands_HaxeGotoBaseCommand


	def __init__(self,v):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBuildFields.hx:8
		super().__init__(v)

	def getEntries(self,types):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBuildFields.hx:12
		_g = []
		_hx_local_1 = types.keys()
		while _hx_local_1.hasNext():
			k = _hx_local_1.next()
			_g1 = 0
			_g2 = types.h.get(k,None).allFieldsList()
			while (_g1 < len(_g2)):
				p = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
				_g1 = (_g1 + 1)
				x = [((HxOverrides.stringOrNull(p.toString()) + " - ") + HxOverrides.stringOrNull(p.kind)), p.type._file]
				_g.append(x)
		return _g

	def getData(self,types):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBuildFields.hx:17
		_g = []
		_hx_local_1 = types.keys()
		while _hx_local_1.hasNext():
			k = _hx_local_1.next()
			_g1 = 0
			_g2 = types.h.get(k,None).allFieldsList()
			while (_g1 < len(_g2)):
				p = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
				_g1 = (_g1 + 1)
				x = (((("null" if k is None else k) + ".") + HxOverrides.stringOrNull(p.name)), p)
				_g.append(x)
		return _g

	def getFile(self,data_entry):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBuildFields.hx:22
		return data_entry.type._file

	def getSrcPos(self,data_entry):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBuildFields.hx:27
		return data_entry.srcPos()

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_commands_HaxeGotoBuildFieldsCommand._hx_class = hxsublime_commands_HaxeGotoBuildFieldsCommand
_hx_classes["hxsublime.commands.HaxeGotoBuildFieldsCommand"] = hxsublime_commands_HaxeGotoBuildFieldsCommand


class hxsublime_commands_HaxeGotoBuildTypesCommand(hxsublime_commands_HaxeGotoBaseCommand):
	_hx_class_name = "hxsublime.commands.HaxeGotoBuildTypesCommand"
	_hx_fields = []
	_hx_methods = ["getEntries", "getData", "getFile", "getSrcPos"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = hxsublime_commands_HaxeGotoBaseCommand


	def __init__(self,v):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBuildTypes.hx:8
		super().__init__(v)

	def getEntries(self,types):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBuildTypes.hx:12
		_g = []
		_hx_local_1 = types.keys()
		while _hx_local_1.hasNext():
			k = _hx_local_1.next()
			def _hx_local_0():
				_this = types.h.get(k,None)
				return _this._file
			x = [k, _hx_local_0()]
			_g.append(x)
		return _g

	def getData(self,types):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBuildTypes.hx:17
		_g = []
		_hx_local_0 = types.keys()
		while _hx_local_0.hasNext():
			k = _hx_local_0.next()
			x = None
			b = types.h.get(k,None)
			x = (k, b)
			_g.append(x)
		return _g

	def getFile(self,dataEntry):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBuildTypes.hx:22
		return dataEntry._file

	def getSrcPos(self,dataEntry):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/GotoBuildTypes.hx:27
		return dataEntry.srcPos()

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_commands_HaxeGotoBuildTypesCommand._hx_class = hxsublime_commands_HaxeGotoBuildTypesCommand
_hx_classes["hxsublime.commands.HaxeGotoBuildTypesCommand"] = hxsublime_commands_HaxeGotoBuildTypesCommand


class hxsublime_commands_HaxeInstallLibCommand(sublime_WindowCommand):
	_hx_class_name = "hxsublime.commands.HaxeInstallLibCommand"
	_hx_fields = []
	_hx_methods = ["run", "createMenuItems", "onEntrySelected"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = sublime_WindowCommand


	def __init__(self,w):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:14
		super().__init__(w)

	def run(self,**_):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:18
		view = sublime_Sublime.active_window().active_view()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:20
		project = hxsublime_project_Projects.currentProject(view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:22
		if (project is not None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:24
			manager = project.haxelibManager()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:25
			libs = manager.searchLibs()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:26
			menu = self.createMenuItems(libs,manager)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:28
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:28
				f = self.onEntrySelected
				a1 = libs
				a2 = manager
				def _hx_local_1(i):
					f(a1,a2,i)
				return _hx_local_1
			self.window.show_quick_panel(menu,_hx_local_0())

	def createMenuItems(self,libs,manager):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:34
		menu = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:35
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:35
		_g = 0
		while (_g < len(libs)):
			l = (libs[_g] if _g >= 0 and _g < len(libs) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:37
			if manager.isLibInstalled(l):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:39
				x = [(((("null" if l is None else l) + " [") + HxOverrides.stringOrNull(manager.getLib(l).version)) + "]"), "Remove"]
				menu.append(x)
			else:
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:43
				menu.append([l, "Install"])
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:47
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:47
		menu.append(["Upgrade libraries", "Upgrade installed libraries"])
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:48
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:48
		menu.append(["Haxelib Selfupdate", "Updates Haxelib itself"])
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:50
		return menu

	def onEntrySelected(self,libs,manager,i):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:55
		haxe_Log.trace(("install lib command selected " + Std.string(i)),_hx_AnonObject({'fileName': "Haxelib.hx", 'lineNumber': 55, 'className': "hxsublime.commands.HaxeInstallLibCommand", 'methodName': "onEntrySelected"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:56
		if (i < 0):
			return
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:59
		if (i == len(libs)):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:61
			haxe_Log.trace("upgrade all",_hx_AnonObject({'fileName': "Haxelib.hx", 'lineNumber': 61, 'className': "hxsublime.commands.HaxeInstallLibCommand", 'methodName': "onEntrySelected"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:62
			manager.upgradeAll()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:65
		if (i == ((len(libs) + 1))):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:67
			haxe_Log.trace("self update",_hx_AnonObject({'fileName': "Haxelib.hx", 'lineNumber': 67, 'className': "hxsublime.commands.HaxeInstallLibCommand", 'methodName': "onEntrySelected"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:68
			manager.selfUpdate()
		else:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:72
			lib = (libs[i] if i >= 0 and i < len(libs) else None)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:73
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:73
				_this = manager.available()
				return lib in _this.h
			if _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:75
				haxe_Log.trace(("remove " + ("null" if lib is None else lib)),_hx_AnonObject({'fileName': "Haxelib.hx", 'lineNumber': 75, 'className': "hxsublime.commands.HaxeInstallLibCommand", 'methodName': "onEntrySelected"}))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:76
				manager.removeLib(lib)
			else:
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:80
				haxe_Log.trace(("install " + ("null" if lib is None else lib)),_hx_AnonObject({'fileName': "Haxelib.hx", 'lineNumber': 80, 'className': "hxsublime.commands.HaxeInstallLibCommand", 'methodName': "onEntrySelected"}))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/Haxelib.hx:81
				manager.installLib(lib)

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_commands_HaxeInstallLibCommand._hx_class = hxsublime_commands_HaxeInstallLibCommand
_hx_classes["hxsublime.commands.HaxeInstallLibCommand"] = hxsublime_commands_HaxeInstallLibCommand


class hxsublime_commands_HaxeShowDocCommand(hxsublime_commands_HaxeFindDeclarationCommand):
	_hx_class_name = "hxsublime.commands.HaxeShowDocCommand"
	_hx_fields = []
	_hx_methods = ["helperMethod", "handleSuccessfulResult"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = hxsublime_commands_HaxeFindDeclarationCommand


	def __init__(self,v):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/ShowDoc.hx:8
		super().__init__(v)

	def helperMethod(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/ShowDoc.hx:13
		return "hxsublime.FindDeclaration.__sublimeShowDoc"

	def handleSuccessfulResult(self,view,json_res,using_insert,insert_before,insert_after,expr_end,build,temp_path,temp_file):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/ShowDoc.hx:18
		doc = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/ShowDoc.hx:19
		if "doc" in json_res:
			doc = json_res.get("doc",None)
		else:
			doc = "No documentation found"
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/ShowDoc.hx:27
		haxe_Log.trace(("json: " + Std.string(json_res)),_hx_AnonObject({'fileName': "ShowDoc.hx", 'lineNumber': 27, 'className': "hxsublime.commands.HaxeShowDocCommand", 'methodName': "handleSuccessfulResult"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/ShowDoc.hx:28
		haxe_Log.trace(("doc: " + Std.string(doc)),_hx_AnonObject({'fileName': "ShowDoc.hx", 'lineNumber': 28, 'className': "hxsublime.commands.HaxeShowDocCommand", 'methodName': "handleSuccessfulResult"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/commands/ShowDoc.hx:29
		hxsublime_panel_Panels.slidePanel().writeln(doc,None,False)

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_commands_HaxeShowDocCommand._hx_class = hxsublime_commands_HaxeShowDocCommand
_hx_classes["hxsublime.commands.HaxeShowDocCommand"] = hxsublime_commands_HaxeShowDocCommand


class hxsublime_compiler_CompletionEntry:
	_hx_class_name = "hxsublime.compiler.CompletionEntry"
	_hx_fields = ["hint", "insert", "doc"]

	def __init__(self,hint,insert,doc):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:29
		self.hint = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:30
		self.insert = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:31
		self.doc = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:35
		self.hint = hint
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:36
		self.insert = insert
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:37
		self.doc = doc

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.hint = None
		_hx_o.insert = None
		_hx_o.doc = None
hxsublime_compiler_CompletionEntry._hx_class = hxsublime_compiler_CompletionEntry
_hx_classes["hxsublime.compiler.CompletionEntry"] = hxsublime_compiler_CompletionEntry


class hxsublime_compiler_Output:
	_hx_class_name = "hxsublime.compiler.Output"
	_hx_statics = ["compiler_output", "no_classes_found", "no_classes_found_in_trace", "haxe_compiler_line", "type_parameter_name", "get_type_hint", "get_function_type_params", "completion_field_to_entry", "collect_completion_fields", "extract_errors", "getCompletionOutput", "parse_completion_output", "get_completion_status_and_errors", "parse_completion_errors"]

	@staticmethod
	def get_type_hint(types):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:60
		hints = []
		# /opt/haxe-git/std/python/Syntax.hx:112
		# /opt/haxe-git/std/python/Syntax.hx:113
		i = None
		# /opt/haxe-git/std/python/Syntax.hx:114
		for i in types.__iter__():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:62
			i = i
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:63
			hint = i.text.strip(None)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:64
			hint_types = hxsublime_tools_HxSrcTools.splitFunctionSignature(hint)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:65
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:65
			hints.append(hint_types)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:69
		return hints

	@staticmethod
	def get_function_type_params(name,signature_types):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:77
		new_args = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:78
		type_params = haxe_ds_StringMap()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:79
		name_len = len(name)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:80
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:80
		_g = 0
		while (_g < len(signature_types)):
			t = (signature_types[_g] if _g >= 0 and _g < len(signature_types) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:83
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:83
			x = None
			_this = None
			delimiter = (("null" if name is None else name) + ".")
			if (delimiter == ""):
				_this = list(t)
			else:
				_this = t.split(delimiter)
			x = "".join([python_Boot.toString1(x1,'') for x1 in _this])
			new_args.append(x)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:84
			while True:
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:87
				index = t.find(name)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:88
				if (index == -1):
					break
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:89
				type_start_index = ((index + name_len) + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:90
				t = HxString.substr(t,type_start_index,None)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:92
				m = hxsublime_compiler_Output.type_parameter_name.match(t)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:93
				if (m is not None):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:95
					param_name = m.group(1)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:96
					type_params.h[param_name] = True
				else:
					break
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:105
		keys = None
		_g1 = []
		_hx_local_1 = type_params.keys()
		while _hx_local_1.hasNext():
			k = _hx_local_1.next()
			_g1.append(k)
		keys = _g1
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:106
		keys.reverse()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:107
		type_param_list = keys
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:108
		return (new_args, type_param_list)

	@staticmethod
	def completion_field_to_entry(name,sig,doc):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:114
		insert = name
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:115
		label = name
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:117
		smart_snippets = hxsublime_Settings.smartSnippetsOnCompletion()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:118
		not_smart = (not smart_snippets)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:120
		if (sig is not None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:121
			types = hxsublime_tools_HxSrcTools.splitFunctionSignature(sig)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:123
			r = hxsublime_compiler_Output.get_function_type_params(name,types)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:125
			types1 = r[0]
			type_params = r[1]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:127
			params_sig = ""
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:129
			if (len(type_params) > 0):
				params_sig = (("<" + HxOverrides.stringOrNull(", ".join([python_Boot.toString1(x1,'') for x1 in type_params]))) + ">")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:133
			ret = None
			ret = (None if ((len(types1) == 0)) else types1.pop())
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:135
			signature_separator = " : "
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:137
			if (len(types1) > 0):
				if ((len(types1) == 1) and (((types1[0] if 0 < len(types1) else None) == "Void"))):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:141
					if not_smart:
						label = ((((("null" if name is None else name) + ("null" if params_sig is None else params_sig)) + "()") + ("null" if signature_separator is None else signature_separator)) + ("null" if ret is None else ret))
					else:
						label = (((("null" if name is None else name) + "()") + ("null" if signature_separator is None else signature_separator)) + ("null" if ret is None else ret))
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:142
					if not_smart:
						insert = name
					else:
						insert = (("" + ("null" if name is None else name)) + "${1:()}")
				else:
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:146
					def _hx_local_0(x):
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:146
						return StringTools.replace(StringTools.replace(x,"}","\\}"),"{","\\{")
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:145
					escape_type = _hx_local_0
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:149
					params = (("( " + HxOverrides.stringOrNull(", ".join([python_Boot.toString1(x1,'') for x1 in types1]))) + " )")
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:150
					label = ((((("null" if name is None else name) + ("null" if params_sig is None else params_sig)) + ("null" if params is None else params)) + ("null" if signature_separator is None else signature_separator)) + ("null" if ret is None else ret))
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:152
					new_types = list(types1)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:153
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:153
					_g1 = 0
					_g = len(new_types)
					while (_g1 < _g):
						i = _g1
						_g1 = (_g1 + 1)
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:155
						python_internal_ArrayImpl._set(new_types, i, (((("${" + Std.string((i + 2))) + ":") + HxOverrides.stringOrNull(escape_type((new_types[i] if i >= 0 and i < len(new_types) else None)))) + "}"))
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:158
					if not_smart:
						insert = name
					else:
						insert = (((("null" if name is None else name) + "${1:( ") + HxOverrides.stringOrNull(", ".join([python_Boot.toString1(x1,'') for x1 in new_types]))) + " )}")
			else:
				label = (((("null" if name is None else name) + ("null" if params_sig is None else params_sig)) + ("null" if signature_separator is None else signature_separator)) + ("null" if ret is None else ret))
		elif (python_lib_Re.match("^[A-Z]",name) is not None):
			label = (("null" if name is None else name) + "\tclass")
		else:
			label = (("null" if name is None else name) + "\tpackage")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:169
		res = hxsublime_compiler_CompletionEntry(label, insert, doc)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:171
		return res

	@staticmethod
	def collect_completion_fields(li):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:177
		comps = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:178
		if (li is not None):
			# /opt/haxe-git/std/python/Syntax.hx:113
			i = None
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:180
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:180
				i1 = li.iter("i")
				return i1.__iter__()
			# /opt/haxe-git/std/python/Syntax.hx:114
			for i in _hx_local_0():
				i = i
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:181
				name = i.get("n")
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:182
				sig = i.find("t").text
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:183
				doc = i.find("d").text
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:184
				entry = hxsublime_compiler_Output.completion_field_to_entry(name,sig,doc)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:186
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:186
				comps.append(entry)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:189
		return comps

	@staticmethod
	def extract_errors(_hx_str):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:194
		errors = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:196
		if (len(python_lib__Re_RegexHelper.findallDynamic(hxsublime_compiler_Output.no_classes_found,_hx_str,None,None)) > 0):
			errors = []
		else:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:200
			entries = None
			_this = python_lib__Re_RegexHelper.findallDynamic(hxsublime_compiler_Output.compiler_output,_hx_str,None,None)
			def _hx_local_0(t):
				return list(t)
			entries = list(map(_hx_local_0,_this))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:203
			def _hx_local_1(x):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:203
				return ((x[4] if 4 < len(x) else None) == "Unexpected |")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:202
			invalidCompletionRequest = Lambda.exists(entries,_hx_local_1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:206
			if (not invalidCompletionRequest):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:207
				_g = 0
				_g1 = None
				_this1 = python_lib__Re_RegexHelper.findallDynamic(hxsublime_compiler_Output.compiler_output,_hx_str,None,None)
				def _hx_local_2(t1):
					return list(t1)
				_g1 = list(map(_hx_local_2,_this1))
				while (_g < len(_g1)):
					infos = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
					_g = (_g + 1)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:210
					f = (infos[0] if 0 < len(infos) else None)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:211
					l = (Std.parseInt((infos[1] if 1 < len(infos) else None)) - 1)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:212
					left = Std.parseInt((infos[2] if 2 < len(infos) else None))
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:213
					right = (infos[3] if 3 < len(infos) else None)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:215
					rightInt = 0
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:216
					if (right != ""):
						rightInt = Std.parseInt(right)
					else:
						rightInt = (left + 1)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:222
					m = (infos[4] if 4 < len(infos) else None)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:224
					if (m != "Unexpected |"):
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:226
						errors.append(_hx_AnonObject({'file': f, 'line': l, '_hx_from': left, 'to': rightInt, 'message': m}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:240
		return errors

	@staticmethod
	def getCompletionOutput(temp_file,orig_file,output,commas):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:246
		r = hxsublime_compiler_Output.parse_completion_output(temp_file,orig_file,output)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:247
		hints = r[0]
		comps = r[1]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:248
		new_hints = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:249
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:249
		_g = 0
		while (_g < len(hints)):
			h = (hints[_g] if _g >= 0 and _g < len(hints) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:251
			if (len(h) > commas):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:253
				x = h[commas:None]
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:254
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:254
				new_hints.append(x)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:257
		hints = new_hints
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:259
		r1 = hxsublime_compiler_Output.get_completion_status_and_errors(hints,comps,output,temp_file,orig_file)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:260
		status = None
		errors = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:261
		if (r1 is not None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:262
			status = r1[0]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:263
			errors = r1[1]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:266
		return (hints, comps, status, errors)

	@staticmethod
	def parse_completion_output(temp_file,orig_file,output):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:272
		tree = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:273
		try:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:274
			x = (("<root>" + ("null" if output is None else output)) + "</root>")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:276
			tree = python_lib_xml_etree_ElementTree.XML(x)
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			if isinstance(_hx_e1, Exception):
				e = _hx_e1
				haxe_Log.trace(("invalid xml - error: " + Std.string(e)),_hx_AnonObject({'fileName': "Output.hx", 'lineNumber': 279, 'className': "hxsublime.compiler.Output", 'methodName': "parse_completion_output"}))
			else:
				raise _hx_e
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:282
		hints = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:283
		comps = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:286
		if (tree is not None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:287
			hints = hxsublime_compiler_Output.get_type_hint(tree.iter("type"))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:288
			comps = hxsublime_compiler_Output.collect_completion_fields(tree.find("list"))
		else:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:291
			hints = []
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:292
			comps = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:295
		if (len(hxsublime_compiler_Output.no_classes_found_in_trace.findall(output,0)) > 0):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:297
			smart_snippets = hxsublime_Settings.smartSnippetsOnCompletion()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:298
			insert = None
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:299
			if smart_snippets:
				insert = "${1:value:Dynamic}"
			else:
				insert = "${0}"
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:305
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:305
			x1 = hxsublime_compiler_CompletionEntry("value:Dynamic", insert, "")
			comps.append(x1)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:308
		return (hints, comps)

	@staticmethod
	def get_completion_status_and_errors(hints,comps,output,temp_file,orig_file):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:313
		status = ""
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:315
		errors = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:317
		res = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:320
		if ((len(hints) == 0) and ((len(comps) == 0))):
			return hxsublime_compiler_Output.parse_completion_errors(output,temp_file,orig_file,status)
		else:
			return ("", [])

	@staticmethod
	def parse_completion_errors(output,temp_file,orig_file,status):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:328
		haxe_Log.trace(("output:" + ("null" if output is None else output)),_hx_AnonObject({'fileName': "Output.hx", 'lineNumber': 328, 'className': "hxsublime.compiler.Output", 'methodName': "parse_completion_errors"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:329
		haxe_Log.trace(("status:" + ("null" if status is None else status)),_hx_AnonObject({'fileName': "Output.hx", 'lineNumber': 329, 'className': "hxsublime.compiler.Output", 'methodName': "parse_completion_errors"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:330
		haxe_Log.trace(("orig_file:" + ("null" if orig_file is None else orig_file)),_hx_AnonObject({'fileName': "Output.hx", 'lineNumber': 330, 'className': "hxsublime.compiler.Output", 'methodName': "parse_completion_errors"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:331
		haxe_Log.trace(("temp_file:" + ("null" if temp_file is None else temp_file)),_hx_AnonObject({'fileName': "Output.hx", 'lineNumber': 331, 'className': "hxsublime.compiler.Output", 'methodName': "parse_completion_errors"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:335
		sep = python_lib_Os.sep
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:336
		haxe_Log.trace(("sep: " + ("null" if sep is None else sep)),_hx_AnonObject({'fileName': "Output.hx", 'lineNumber': 336, 'className': "hxsublime.compiler.Output", 'methodName': "parse_completion_errors"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:337
		if (sep == "\\"):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:338
			def _hx_local_0(match_obj):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:339
				haxe_Log.trace("matched",_hx_AnonObject({'fileName': "Output.hx", 'lineNumber': 339, 'className': "hxsublime.compiler.Output", 'methodName': "parse_completion_errors"}))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:340
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:340
				_this = None
				_this1 = match_obj.group(0)
				_this = _this1.split("/")
				return sep.join([python_Boot.toString1(x1,'') for x1 in _this])
			slash_replace = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:343
			output = python_lib_Re.sub("[A-Za-z]:(.*)[.]hx",slash_replace,output)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:346
		output = StringTools.replace(output,temp_file,orig_file)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:348
		haxe_Log.trace(("output after replace: " + ("null" if output is None else output)),_hx_AnonObject({'fileName': "Output.hx", 'lineNumber': 348, 'className': "hxsublime.compiler.Output", 'methodName': "parse_completion_errors"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:349
		output = python_lib_Re.sub("\\(display(.*)\\)","",output)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:351
		lines = output.split("\n")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:352
		l = (lines[0] if 0 < len(lines) else None).strip(None)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:354
		status1 = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:356
		if (len(l) > 0):
			if (l == "<list>"):
				status1 = "No autocompletion available"
			elif (python_lib_Re.match(hxsublime_compiler_Output.haxe_compiler_line,l) is None):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:362
				status1 = l
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:363
				haxe_Log.trace(l,_hx_AnonObject({'fileName': "Output.hx", 'lineNumber': 363, 'className': "hxsublime.compiler.Output", 'methodName': "parse_completion_errors"}))
			else:
				status1 = ""
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:370
		errors = hxsublime_compiler_Output.extract_errors(output)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Output.hx:372
		return (status1, errors)
hxsublime_compiler_Output._hx_class = hxsublime_compiler_Output
_hx_classes["hxsublime.compiler.Output"] = hxsublime_compiler_Output


class hxsublime_compiler_Server:
	_hx_class_name = "hxsublime.compiler.Server"
	_hx_fields = ["_use_wrapper", "_server_proc", "_server_port", "_orig_server_port"]
	_hx_methods = ["get_server_port", "start", "stop", "__del__"]

	def __init__(self,port):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:20
		self._use_wrapper = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:21
		self._server_proc = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:22
		self._server_port = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:23
		self._orig_server_port = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:27
		self._use_wrapper = hxsublime_Settings.useHaxeServermodeWrapper()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:28
		self._server_proc = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:29
		self._server_port = port
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:30
		self._orig_server_port = port

	def get_server_port(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:35
		return self._server_port

	def start(self,haxe_path,cwd = None,env = None,retries = 10):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:39
		if (retries is None):
			retries = 10
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:38
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:41
		if (self._server_proc is None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:42
			cmd = None
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:43
			if self._use_wrapper:
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:45
				wrapper = (HxOverrides.stringOrNull(hxsublime_Plugin.plugin_base_dir()) + "/wrapper")
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:46
				cmd = ["neko", wrapper]
			else:
				cmd = []
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:53
			cmd.extend([haxe_path, "--wait", Std.string(self._server_port)])
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:54
			haxe_Log.trace("start server:",_hx_AnonObject({'fileName': "Server.hx", 'lineNumber': 54, 'className': "hxsublime.compiler.Server", 'methodName': "start"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:56
			haxe_Log.trace(" ".join([python_Boot.toString1(x1,'') for x1 in cmd]),_hx_AnonObject({'fileName': "Server.hx", 'lineNumber': 56, 'className': "hxsublime.compiler.Server", 'methodName': "start"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:59
			def _hx_local_1(e):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:60
				err = ((("Error starting server " + HxOverrides.stringOrNull(" ".join([python_Boot.toString1(x1,'') for x1 in cmd]))) + ": ") + Std.string(e))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:61
				sublime_Sublime.error_message(err)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:62
				if (retries > 0):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:64
					_g.stop()
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:65
					_g._server_port = (_g._server_port + 1)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:66
					haxe_Log.trace(("retry starting server at port: " + Std.string(_g._server_port)),_hx_AnonObject({'fileName': "Server.hx", 'lineNumber': 66, 'className': "hxsublime.compiler.Server", 'methodName': "start"}))
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:67
					_g.start(haxe_path,cwd,env,(retries - 1))
				else:
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:71
					msg = "Cannot start haxe compilation server on ports {0}-{1}"
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:72
					msg = hxsublime_support_StringTools.format(msg,[_g._orig_server_port, _g._server_port])
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:73
					haxe_Log.trace("Server starting error",_hx_AnonObject({'fileName': "Server.hx", 'lineNumber': 73, 'className': "hxsublime.compiler.Server", 'methodName': "start"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:58
			onError = _hx_local_1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:76
			try:
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:79
				full_env = python_lib_Os.environ.copy()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:80
				if (env is not None):
					full_env.update(env)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:85
				if (env is not None):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:87
					def _hx_local_2():
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:87
						this1 = None
						_this = env.keys()
						this1 = iter(_this)
						return python_HaxeIterator(this1)
					_hx_local_3 = _hx_local_2()
					while _hx_local_3.hasNext():
						k = _hx_local_3.next()
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:89
						val = env.get(k,None)
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:90
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:90
						val1 = python_lib_os_Path.expandvars(val)
						full_env[k] = val1
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:95
				haxe_Log.trace(("server env:" + Std.string(full_env)),_hx_AnonObject({'fileName': "Server.hx", 'lineNumber': 95, 'className': "hxsublime.compiler.Server", 'methodName': "start"}))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:96
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:96
				o = _hx_AnonObject({'cwd': cwd, 'env': full_env, 'stdin': python_lib_Subprocess.PIPE, 'stdout': python_lib_Subprocess.PIPE, 'startupinfo': hxsublime_Plugin.startupInfo()})
				if hasattr(o,(("_hx_" + "bufsize") if ("bufsize" in python_Boot.keywords) else (("_hx_" + "bufsize") if (((((len("bufsize") > 2) and ((ord("bufsize"[0]) == 95))) and ((ord("bufsize"[1]) == 95))) and ((ord("bufsize"[(len("bufsize") - 1)]) != 95)))) else "bufsize"))):
					Reflect.setField(o,"bufsize",Reflect.field(o,"bufsize"))
				else:
					Reflect.setField(o,"bufsize",0)
				if hasattr(o,(("_hx_" + "executable") if ("executable" in python_Boot.keywords) else (("_hx_" + "executable") if (((((len("executable") > 2) and ((ord("executable"[0]) == 95))) and ((ord("executable"[1]) == 95))) and ((ord("executable"[(len("executable") - 1)]) != 95)))) else "executable"))):
					Reflect.setField(o,"executable",Reflect.field(o,"executable"))
				else:
					Reflect.setField(o,"executable",None)
				if hasattr(o,(("_hx_" + "stdin") if ("stdin" in python_Boot.keywords) else (("_hx_" + "stdin") if (((((len("stdin") > 2) and ((ord("stdin"[0]) == 95))) and ((ord("stdin"[1]) == 95))) and ((ord("stdin"[(len("stdin") - 1)]) != 95)))) else "stdin"))):
					Reflect.setField(o,"stdin",Reflect.field(o,"stdin"))
				else:
					Reflect.setField(o,"stdin",None)
				if hasattr(o,(("_hx_" + "stdout") if ("stdout" in python_Boot.keywords) else (("_hx_" + "stdout") if (((((len("stdout") > 2) and ((ord("stdout"[0]) == 95))) and ((ord("stdout"[1]) == 95))) and ((ord("stdout"[(len("stdout") - 1)]) != 95)))) else "stdout"))):
					Reflect.setField(o,"stdout",Reflect.field(o,"stdout"))
				else:
					Reflect.setField(o,"stdout",None)
				if hasattr(o,(("_hx_" + "stderr") if ("stderr" in python_Boot.keywords) else (("_hx_" + "stderr") if (((((len("stderr") > 2) and ((ord("stderr"[0]) == 95))) and ((ord("stderr"[1]) == 95))) and ((ord("stderr"[(len("stderr") - 1)]) != 95)))) else "stderr"))):
					Reflect.setField(o,"stderr",Reflect.field(o,"stderr"))
				else:
					Reflect.setField(o,"stderr",None)
				if hasattr(o,(("_hx_" + "preexec_fn") if ("preexec_fn" in python_Boot.keywords) else (("_hx_" + "preexec_fn") if (((((len("preexec_fn") > 2) and ((ord("preexec_fn"[0]) == 95))) and ((ord("preexec_fn"[1]) == 95))) and ((ord("preexec_fn"[(len("preexec_fn") - 1)]) != 95)))) else "preexec_fn"))):
					Reflect.setField(o,"preexec_fn",Reflect.field(o,"preexec_fn"))
				else:
					Reflect.setField(o,"preexec_fn",None)
				if hasattr(o,(("_hx_" + "close_fds") if ("close_fds" in python_Boot.keywords) else (("_hx_" + "close_fds") if (((((len("close_fds") > 2) and ((ord("close_fds"[0]) == 95))) and ((ord("close_fds"[1]) == 95))) and ((ord("close_fds"[(len("close_fds") - 1)]) != 95)))) else "close_fds"))):
					Reflect.setField(o,"close_fds",Reflect.field(o,"close_fds"))
				else:
					Reflect.setField(o,"close_fds",None)
				if hasattr(o,(("_hx_" + "shell") if ("shell" in python_Boot.keywords) else (("_hx_" + "shell") if (((((len("shell") > 2) and ((ord("shell"[0]) == 95))) and ((ord("shell"[1]) == 95))) and ((ord("shell"[(len("shell") - 1)]) != 95)))) else "shell"))):
					Reflect.setField(o,"shell",Reflect.field(o,"shell"))
				else:
					Reflect.setField(o,"shell",None)
				if hasattr(o,(("_hx_" + "cwd") if ("cwd" in python_Boot.keywords) else (("_hx_" + "cwd") if (((((len("cwd") > 2) and ((ord("cwd"[0]) == 95))) and ((ord("cwd"[1]) == 95))) and ((ord("cwd"[(len("cwd") - 1)]) != 95)))) else "cwd"))):
					Reflect.setField(o,"cwd",Reflect.field(o,"cwd"))
				else:
					Reflect.setField(o,"cwd",None)
				if hasattr(o,(("_hx_" + "env") if ("env" in python_Boot.keywords) else (("_hx_" + "env") if (((((len("env") > 2) and ((ord("env"[0]) == 95))) and ((ord("env"[1]) == 95))) and ((ord("env"[(len("env") - 1)]) != 95)))) else "env"))):
					Reflect.setField(o,"env",Reflect.field(o,"env"))
				else:
					Reflect.setField(o,"env",None)
				if hasattr(o,(("_hx_" + "universal_newlines") if ("universal_newlines" in python_Boot.keywords) else (("_hx_" + "universal_newlines") if (((((len("universal_newlines") > 2) and ((ord("universal_newlines"[0]) == 95))) and ((ord("universal_newlines"[1]) == 95))) and ((ord("universal_newlines"[(len("universal_newlines") - 1)]) != 95)))) else "universal_newlines"))):
					Reflect.setField(o,"universal_newlines",Reflect.field(o,"universal_newlines"))
				else:
					Reflect.setField(o,"universal_newlines",None)
				if hasattr(o,(("_hx_" + "startupinfo") if ("startupinfo" in python_Boot.keywords) else (("_hx_" + "startupinfo") if (((((len("startupinfo") > 2) and ((ord("startupinfo"[0]) == 95))) and ((ord("startupinfo"[1]) == 95))) and ((ord("startupinfo"[(len("startupinfo") - 1)]) != 95)))) else "startupinfo"))):
					Reflect.setField(o,"startupinfo",Reflect.field(o,"startupinfo"))
				else:
					Reflect.setField(o,"startupinfo",None)
				if hasattr(o,(("_hx_" + "creationflags") if ("creationflags" in python_Boot.keywords) else (("_hx_" + "creationflags") if (((((len("creationflags") > 2) and ((ord("creationflags"[0]) == 95))) and ((ord("creationflags"[1]) == 95))) and ((ord("creationflags"[(len("creationflags") - 1)]) != 95)))) else "creationflags"))):
					Reflect.setField(o,"creationflags",Reflect.field(o,"creationflags"))
				else:
					Reflect.setField(o,"creationflags",0)
				if (Sys.systemName() == "Windows"):
					self._server_proc = python_lib_subprocess_Popen(cmd, Reflect.field(o,"bufsize"), Reflect.field(o,"executable"), Reflect.field(o,"stdin"), Reflect.field(o,"stdout"), Reflect.field(o,"stderr"), Reflect.field(o,"preexec_fn"), Reflect.field(o,"close_fds"), Reflect.field(o,"shell"), Reflect.field(o,"cwd"), Reflect.field(o,"env"), Reflect.field(o,"universal_newlines"), Reflect.field(o,"startupinfo"), Reflect.field(o,"creationflags"))
				else:
					self._server_proc = python_lib_subprocess_Popen(cmd, Reflect.field(o,"bufsize"), Reflect.field(o,"executable"), Reflect.field(o,"stdin"), Reflect.field(o,"stdout"), Reflect.field(o,"stderr"), Reflect.field(o,"preexec_fn"), Reflect.field(o,"close_fds"), Reflect.field(o,"shell"), Reflect.field(o,"cwd"), Reflect.field(o,"env"), Reflect.field(o,"universal_newlines"), Reflect.field(o,"startupinfo"))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:98
				self._server_proc.poll()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:100
				python_lib_Time.sleep(0.05)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:102
				haxe_Log.trace(("server started at port: " + Std.string(self._server_port)),_hx_AnonObject({'fileName': "Server.hx", 'lineNumber': 102, 'className': "hxsublime.compiler.Server", 'methodName': "start"}))
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				if isinstance(_hx_e1, OSError):
					e1 = _hx_e1
					onError(e1)
				elif isinstance(_hx_e1, ValueError):
					e2 = _hx_e1
					onError(e2)
				else:
					e3 = _hx_e1
					haxe_Log.trace(("ERROR : " + Std.string(e3)),_hx_AnonObject({'fileName': "Server.hx", 'lineNumber': 115, 'className': "hxsublime.compiler.Server", 'methodName': "start"}))

	def stop(self,completeCallback = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:123
		old_port = self._server_port
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:124
		try:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:125
			proc = self._server_proc
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:127
			if (proc is not None):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:128
				self._server_proc = None
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:130
				if self._use_wrapper:
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:132
					proc.stdin.write(hxsublime_support_StringTools.encode("x"))
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:133
					python_lib_Time.sleep(0.2)
				else:
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:136
					proc.terminate()
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:137
					python_lib_Time.sleep(0.2)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:139
				proc.kill()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:140
				proc.wait()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:141
				proc = None
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:146
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:146
				_hx_local_0 = self
				_hx_local_1 = _hx_local_0._server_port
				_hx_local_0._server_port = (_hx_local_1 + 1)
				_hx_local_0._server_port
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			e = _hx_e1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:151
			self._server_proc = None
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:152
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:152
			_hx_local_2 = self
			_hx_local_3 = _hx_local_2._server_port
			_hx_local_2._server_port = (_hx_local_3 + 1)
			_hx_local_2._server_port
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:155
		if (completeCallback is not None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:157
			hxsublime_panel_Panels.defaultPanel().writeln(("stopping server on port: " + Std.string(old_port)))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:158
			completeCallback()

	def __del__(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/compiler/Server.hx:163
		self.stop()

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o._use_wrapper = None
		_hx_o._server_proc = None
		_hx_o._server_port = None
		_hx_o._orig_server_port = None
hxsublime_compiler_Server._hx_class = hxsublime_compiler_Server
_hx_classes["hxsublime.compiler.Server"] = hxsublime_compiler_Server


class hxsublime_completion_CompletionListener(sublime_EventListener):
	_hx_class_name = "hxsublime.completion.CompletionListener"
	_hx_fields = []
	_hx_methods = ["clear", "on_query_completions"]
	_hx_statics = ["triggerCb", "triggerId", "id", "trigger"]
	_hx_interfaces = []
	_hx_super = sublime_EventListener


	def clear(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:55
		hxsublime_completion_CompletionListener.triggerCb = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:56
		hxsublime_completion_CompletionListener.triggerId = -1

	def on_query_completions(self,view,prefix,locations):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:61
		f = hxsublime_completion_CompletionListener.triggerCb
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:62
		if ((f is not None) and ((hxsublime_completion_CompletionListener.triggerId == hxsublime_completion_CompletionListener.id))):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:63
			offset = hxsublime_completion_Completion.getCompletionOffset((locations[0] if 0 < len(locations) else None),prefix)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:64
			project = hxsublime_project_Projects.currentProject(view)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:65
			self.clear()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:62
			return f(_hx_AnonObject({'offset': offset, 'prefix': prefix, 'view': view, 'project': project}))
		else:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:68
			self.clear()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:69
			haxe_Log.trace("------------ ON QUERY COMPLETION ---------------",_hx_AnonObject({'fileName': "Completion.hx", 'lineNumber': 69, 'className': "hxsublime.completion.CompletionListener", 'methodName': "on_query_completions"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:70
			project1 = hxsublime_project_Projects.currentProject(view)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:62
			return hxsublime_completion_Completion.dispatchAutoComplete(project1,view,prefix,(locations[0] if 0 < len(locations) else None))
	triggerCb = None

	@staticmethod
	def trigger(view,showTopLevelSnippets,cb):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:35
		def _hx_local_2():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:35
			_hx_local_0 = hxsublime_completion_CompletionListener
			_hx_local_1 = _hx_local_0.id
			_hx_local_0.id = (_hx_local_1 + 1)
			return _hx_local_0.id
		hxsublime_completion_CompletionListener.triggerId = _hx_local_2()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:36
		hxsublime_completion_CompletionListener.triggerCb = cb
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:40
		def _hx_local_3():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:40
			view.run_command("auto_complete",python_Lib.anonToDict(_hx_AnonObject({'api_completions_only': (not showTopLevelSnippets), 'disable_auto_insert': True, 'next_completion_if_showing': True, 'auto_complete_commit_on_tab': True})))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:38
		run = _hx_local_3
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:48
		view.run_command("hide_auto_complete")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:50
		sublime_Sublime.set_timeout(run,0)

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_completion_CompletionListener._hx_class = hxsublime_completion_CompletionListener
_hx_classes["hxsublime.completion.CompletionListener"] = hxsublime_completion_CompletionListener


class hxsublime_completion_Completion:
	_hx_class_name = "hxsublime.completion.Completion"
	_hx_statics = ["getCompletionScopes", "getCompletionOffset", "canRunCompletion", "isSupportedScope", "emptyHandler", "getAutoCompleteHandler", "dispatchAutoComplete", "logCompletionInfo"]

	@staticmethod
	def getCompletionScopes(view,location):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:83
		return hxsublime_tools_ViewTools.getScopesAt(view,location)

	@staticmethod
	def getCompletionOffset(location,prefix):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:88
		return (location - len(prefix))

	@staticmethod
	def canRunCompletion(offset,scopes):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:93
		if (offset == 0):
			return False
		else:
			return hxsublime_completion_Completion.isSupportedScope(scopes)

	@staticmethod
	def isSupportedScope(scopes):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:98
		return (not hxsublime_tools_ScopeTools.containsStringOrComment(scopes))

	@staticmethod
	def emptyHandler(project,view,offset,prefix):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:103
		return []

	@staticmethod
	def getAutoCompleteHandler(view,scopes):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:109
		handler = None
		if Lambda.has(scopes,hxsublime_Config.SOURCE_HXML):
			handler = hxsublime_completion_hxml_HxmlCompletion.autoComplete
		elif Lambda.has(scopes,hxsublime_Config.SOURCE_HAXE):
			if hxsublime_tools_ViewTools.isHxsl(view):
				handler = hxsublime_completion_hxsl_HxslCompletion.autoComplete
			else:
				handler = hxsublime_completion_hx_HxCompletion.eventTriggeredAutoComplete
		else:
			handler = hxsublime_completion_Completion.emptyHandler
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:118
		return handler

	@staticmethod
	def dispatchAutoComplete(project,view,prefix,location):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:123
		startTime = python_lib_Time.time()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:125
		offset = hxsublime_completion_Completion.getCompletionOffset(location,prefix)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:127
		scopes = hxsublime_completion_Completion.getCompletionScopes(view,location)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:130
		comps = None
		if hxsublime_completion_Completion.canRunCompletion(offset,scopes):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:132
			handler = hxsublime_completion_Completion.getAutoCompleteHandler(view,scopes)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:133
			comps = handler(project,view,offset,prefix)
		else:
			comps = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:137
		hxsublime_completion_Completion.logCompletionInfo(startTime,python_lib_Time.time(),comps)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:139
		return comps

	@staticmethod
	def logCompletionInfo(startTime,endTime,comps):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:144
		runTime = (endTime - startTime)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:145
		haxe_Log.trace(("on_query_completion time: " + Std.string(runTime)),_hx_AnonObject({'fileName': "Completion.hx", 'lineNumber': 145, 'className': "hxsublime.completion.Completion", 'methodName': "logCompletionInfo"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/Completion.hx:146
		haxe_Log.trace(("number of completions: " + Std.string(len(comps))),_hx_AnonObject({'fileName': "Completion.hx", 'lineNumber': 146, 'className': "hxsublime.completion.Completion", 'methodName': "logCompletionInfo"}))
hxsublime_completion_Completion._hx_class = hxsublime_completion_Completion
_hx_classes["hxsublime.completion.Completion"] = hxsublime_completion_Completion


class hxsublime_completion_hx_CompletionBuild:
	_hx_class_name = "hxsublime.completion.hx.CompletionBuild"
	_hx_fields = ["build", "ctx", "tempPath", "tempFile", "cache", "display_cache", "display_cache_set"]
	_hx_methods = ["display"]
	_hx_interfaces = [hxsublime_macros_LazyFunctionSupport]

	def __init__(self,ctx,temp_path,temp_file):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionBuild.hx:25
		self.build = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionBuild.hx:26
		self.ctx = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionBuild.hx:27
		self.tempPath = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionBuild.hx:28
		self.tempFile = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionBuild.hx:29
		self.cache = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionBuild.hx:47
		self.display_cache = None
		self.display_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:34
		self.display_cache_set = False
		self.display_cache = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionBuild.hx:33
		self.build = ctx.build().copy()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionBuild.hx:35
		self.build.addClasspath(temp_path)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionBuild.hx:37
		self.ctx = ctx
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionBuild.hx:39
		self.tempPath = temp_path
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionBuild.hx:41
		self.tempFile = temp_file
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionBuild.hx:43
		self.cache = ctx.project.completionContext.current

	def display(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionBuild.hx:47
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.display_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.display_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionBuild.hx:48
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionBuild.hx:49
				pos = Std.string(_g.ctx.complete_offset_in_bytes())
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionBuild.hx:50
				return ((HxOverrides.stringOrNull(_g.tempFile) + "@") + ("null" if pos is None else pos))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.display_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.display_cache

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.build = None
		_hx_o.ctx = None
		_hx_o.tempPath = None
		_hx_o.tempFile = None
		_hx_o.cache = None
		_hx_o.display_cache = None
		_hx_o.display_cache_set = None
hxsublime_completion_hx_CompletionBuild._hx_class = hxsublime_completion_hx_CompletionBuild
_hx_classes["hxsublime.completion.hx.CompletionBuild"] = hxsublime_completion_hx_CompletionBuild


class hxsublime_completion_hx_CompletionContext:
	_hx_class_name = "hxsublime.completion.hx.CompletionContext"
	_hx_fields = ["prefix", "view", "view_id", "id", "options", "settings", "offset", "project", "view_pos", "isHint_cache", "isHint_cache_set", "complete_offset_in_bytes_cache", "complete_offset_in_bytes_cache_set", "orig_file_cache", "orig_file_cache_set", "build_cache", "build_cache_set", "completeCharIsAfterControlStruct_cache", "completeCharIsAfterControlStruct_cache_set", "inControlStruct_cache", "inControlStruct_cache_set", "srcUntilCompleteOffset_cache", "srcUntilCompleteOffset_cache_set", "lineAfterOffset_cache", "lineAfterOffset_cache_set", "src_cache", "src_cache_set", "completeChar_cache", "completeChar_cache_set", "completionInfo_cache", "completionInfo_cache_set", "commas_cache", "commas_cache_set", "complete_offset_cache", "complete_offset_cache_set", "is_new_cache", "is_new_cache_set", "srcUntilOffset_cache", "srcUntilOffset_cache_set", "tempCompletionSrc_cache", "tempCompletionSrc_cache_set", "prefixIsWhitespace_cache", "prefixIsWhitespace_cache_set"]
	_hx_methods = ["isHint", "complete_offset_in_bytes", "orig_file", "build", "completeCharIsAfterControlStruct", "inControlStruct", "srcUntilCompleteOffset", "lineAfterOffset", "src", "completeChar", "completionInfo", "commas", "complete_offset", "is_new", "srcUntilOffset", "tempCompletionSrc", "prefixIsWhitespace", "eq"]
	_hx_statics = ["controlStructRegex", "getCompletionId", "count_commas_and_complete_offset", "get_completion_info"]
	_hx_interfaces = [hxsublime_macros_LazyFunctionSupport]

	def __init__(self,view,project,offset,options,settings,prefix):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:31
		self.prefix = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:32
		self.view = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:33
		self.view_id = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:34
		self.id = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:35
		self.options = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:36
		self.settings = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:37
		self.offset = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:38
		self.project = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:39
		self.view_pos = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:69
		self.isHint_cache = None
		self.isHint_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:77
		self.complete_offset_in_bytes_cache = None
		self.complete_offset_in_bytes_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:86
		self.orig_file_cache = None
		self.orig_file_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:94
		self.build_cache = None
		self.build_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:104
		self.completeCharIsAfterControlStruct_cache = None
		self.completeCharIsAfterControlStruct_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:110
		self.inControlStruct_cache = None
		self.inControlStruct_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:116
		self.srcUntilCompleteOffset_cache = None
		self.srcUntilCompleteOffset_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:122
		self.lineAfterOffset_cache = None
		self.lineAfterOffset_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:130
		self.src_cache = None
		self.src_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:135
		self.completeChar_cache = None
		self.completeChar_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:141
		self.completionInfo_cache = None
		self.completionInfo_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:147
		self.commas_cache = None
		self.commas_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:153
		self.complete_offset_cache = None
		self.complete_offset_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:158
		self.is_new_cache = None
		self.is_new_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:163
		self.srcUntilOffset_cache = None
		self.srcUntilOffset_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:169
		self.tempCompletionSrc_cache = None
		self.tempCompletionSrc_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:178
		self.prefixIsWhitespace_cache = None
		self.prefixIsWhitespace_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:34
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
		self.isHint_cache_set = False
		self.isHint_cache = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:44
		self.view = view
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:46
		self.prefix = prefix
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:49
		self.offset = offset
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:52
		self.project = project
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:55
		self.options = options
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:58
		self.settings = settings
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:60
		self.view_id = view.id()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:62
		self.id = hxsublime_completion_hx_CompletionContext.getCompletionId()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:64
		self.view_pos = hxsublime_tools_ViewTools.getFirstCursorPos(view)

	def isHint(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:69
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.isHint_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.isHint_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:70
			def _hx_local_2():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:72
				whitespace_re = python_lib_Re.compile("^\\s*$")
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:73
				def _hx_local_1():
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:73
					def _hx_local_0():
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:73
						_hx_str = _g.completeChar()
						return "(,".find(_hx_str)
					return ((_hx_local_0() > -1) and ((python_lib_Re.match(whitespace_re,_g.prefix) is not None)))
				return _hx_local_1()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_2
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.isHint_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.isHint_cache

	def complete_offset_in_bytes(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:77
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.complete_offset_in_bytes_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.complete_offset_in_bytes_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:78
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:79
				s = _g.srcUntilCompleteOffset()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:80
				b = hxsublime_support_StringTools.encode(s)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:82
				return len(b)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.complete_offset_in_bytes_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.complete_offset_in_bytes_cache

	def orig_file(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:86
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.orig_file_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.orig_file_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:88
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:88
				return _g.view.file_name()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.orig_file_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.orig_file_cache

	def build(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:94
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.build_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.build_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:95
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:96
				if (not _g.project.hasBuild()):
					_g.project.extractBuildArgs()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:99
				return _g.project.getBuild(_g.view).copy()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.build_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.build_cache

	def completeCharIsAfterControlStruct(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:104
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.completeCharIsAfterControlStruct_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.completeCharIsAfterControlStruct_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:106
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:106
				return (_g.inControlStruct() and ((_g.completeChar() == "(")))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.completeCharIsAfterControlStruct_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.completeCharIsAfterControlStruct_cache

	def inControlStruct(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:110
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.inControlStruct_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.inControlStruct_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:112
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:112
				return (hxsublime_completion_hx_CompletionContext.controlStructRegex.search(_g.srcUntilCompleteOffset()) is not None)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.inControlStruct_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.inControlStruct_cache

	def srcUntilCompleteOffset(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:116
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.srcUntilCompleteOffset_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.srcUntilCompleteOffset_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:118
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:118
				_this = _g.src()
				endIndex = _g.complete_offset()
				return HxString.substring(_this,0,endIndex)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.srcUntilCompleteOffset_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.srcUntilCompleteOffset_cache

	def lineAfterOffset(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:122
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.lineAfterOffset_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.lineAfterOffset_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:123
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:124
				line_end = None
				_this = _g.src()
				startIndex = _g.offset
				line_end = (_this.find("\n") if ((startIndex is None)) else _this.find("\n", startIndex))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:125
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:125
				_this1 = _g.src()
				return HxString.substring(_this1,_g.offset,line_end)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.lineAfterOffset_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.lineAfterOffset_cache

	def src(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:130
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.src_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.src_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:131
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:131
				return hxsublime_tools_ViewTools.getContent(_g.view)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.src_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.src_cache

	def completeChar(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:135
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.completeChar_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.completeChar_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:137
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:137
				_this = _g.src()
				index = (_g.complete_offset() - 1)
				if ((index < 0) or ((index >= len(_this)))):
					return ""
				else:
					return _this[index]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.completeChar_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.completeChar_cache

	def completionInfo(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:141
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.completionInfo_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.completionInfo_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:143
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:143
				return hxsublime_completion_hx_CompletionContext.get_completion_info(_g.view,_g.offset,_g.src())
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.completionInfo_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.completionInfo_cache

	def commas(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:147
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.commas_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.commas_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:148
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:148
				_this = _g.completionInfo()
				return _this[0]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.commas_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.commas_cache

	def complete_offset(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:153
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.complete_offset_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.complete_offset_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:154
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:154
				_this = _g.completionInfo()
				return _this[1]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.complete_offset_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.complete_offset_cache

	def is_new(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:158
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.is_new_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.is_new_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:159
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:159
				_this = _g.completionInfo()
				return _this[3]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.is_new_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.is_new_cache

	def srcUntilOffset(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:163
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.srcUntilOffset_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.srcUntilOffset_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:165
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:165
				_this = _g.src()
				return HxString.substring(_this,0,(_g.offset - 1))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.srcUntilOffset_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.srcUntilOffset_cache

	def tempCompletionSrc(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:169
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.tempCompletionSrc_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.tempCompletionSrc_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:172
			def _hx_local_3():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:172
				def _hx_local_2():
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:172
					def _hx_local_0():
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:172
						_this = _g.src()
						_hx_len = _g.complete_offset()
						return HxString.substr(_this,0,_hx_len)
					def _hx_local_1():
						_this1 = _g.src()
						pos = _g.complete_offset()
						return HxString.substr(_this1,pos,None)
					return ((HxOverrides.stringOrNull(_hx_local_0()) + "") + HxOverrides.stringOrNull(_hx_local_1()))
				return _hx_local_2()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_3
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.tempCompletionSrc_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.tempCompletionSrc_cache

	def prefixIsWhitespace(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:178
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.prefixIsWhitespace_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.prefixIsWhitespace_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:180
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:180
				return hxsublime_tools_StringTools.isWhitespaceOrEmpty(_g.prefix)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.prefixIsWhitespace_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.prefixIsWhitespace_cache

	def eq(self,other):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:183
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:187
		def _hx_local_0():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:188
			if _g.isHint():
				return ((_g.prefix == other.prefix) or ((_g.prefixIsWhitespace() and other.prefixIsWhitespace())))
			else:
				return True
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:185
		prefixEq = _hx_local_0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:195
		return ((((((((((other is not None) and ((self.orig_file() == other.orig_file()))) and ((self.offset == other.offset))) and ((self.commas() == other.commas()))) and ((self.srcUntilOffset() == other.srcUntilOffset()))) and self.options.eq(other.options)) and ((self.completeChar() == other.completeChar()))) and ((self.lineAfterOffset() == other.lineAfterOffset()))) and ((self.isHint() == other.isHint()))) and prefixEq())

	@staticmethod
	def getCompletionId():
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:28
		x = python_lib_Time.time()
		try:
			return int(x)
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			e = _hx_e1
			return None

	@staticmethod
	def count_commas_and_complete_offset(src,prev_comma,complete_offset):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:212
		commas = 0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:213
		closed_pars = 0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:214
		closed_braces = 0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:215
		closed_brackets = 0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:217
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:217
		_g = 0
		while (_g < prev_comma):
			j = _g
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:219
			i = (prev_comma - j)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:221
			c = None
			if ((i < 0) or ((i >= len(src)))):
				c = ""
			else:
				c = src[i]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:223
			if (c == ")"):
				closed_pars = (closed_pars + 1)
			elif (c == "("):
				if (closed_pars < 1):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:231
					complete_offset = (i + 1)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:232
					break
				else:
					closed_pars = (closed_pars - 1)
			elif (c == ","):
				if (((closed_pars == 0) and ((closed_braces == 0))) and ((closed_brackets == 0))):
					commas = (commas + 1)
			elif (c == "{"):
				closed_braces = (closed_braces - 1)
			elif (c == "}"):
				closed_braces = (closed_braces + 1)
			elif (c == "["):
				closed_brackets = (closed_brackets - 1)
			elif (c == "]"):
				closed_brackets = (closed_brackets + 1)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:265
		return (commas, complete_offset)

	@staticmethod
	def get_completion_info(view,offset,src):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:271
		prev = None
		index = (offset - 1)
		if ((index < 0) or ((index >= len(src)))):
			prev = ""
		else:
			prev = src[index]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:272
		commas = 0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:274
		complete_offset = offset
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:275
		is_new = False
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:276
		prevSymbolIsComma = False
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:277
		if (((prev == " ") and (((offset - 4) >= 0))) and ((HxString.substring(src,(offset - 4),(offset - 1)) == "new"))):
			is_new = True
		elif (not prev in "(.;"):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:283
			fragment = view.substr(sublime_Region(0, offset))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:284
			prev_dot = fragment.rfind(".", 0, len(fragment))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:285
			prev_par = fragment.rfind("(", 0, len(fragment))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:286
			prev_comma = fragment.rfind(",", 0, len(fragment))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:287
			prev_colon = fragment.rfind(":", 0, len(fragment))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:288
			prev_brace = fragment.rfind("{", 0, len(fragment))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:289
			prev_semi = fragment.rfind(";", 0, len(fragment))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:291
			prev_symbol = python_lib_Builtins.max(prev_dot,prev_par,prev_comma,prev_brace,prev_colon,prev_semi)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:293
			if (prev_symbol == prev_comma):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:295
				r = hxsublime_completion_hx_CompletionContext.count_commas_and_complete_offset(src,prev_comma,complete_offset)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:296
				commas = r[0]
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:297
				complete_offset = r[1]
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:298
				prevSymbolIsComma = True
			else:
				complete_offset = python_lib_Builtins.max((prev_dot + 1),(prev_par + 1),(prev_colon + 1),(prev_brace + 1),(prev_semi + 1))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionContext.hx:306
		return (commas, complete_offset, prevSymbolIsComma, is_new)

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.prefix = None
		_hx_o.view = None
		_hx_o.view_id = None
		_hx_o.id = None
		_hx_o.options = None
		_hx_o.settings = None
		_hx_o.offset = None
		_hx_o.project = None
		_hx_o.view_pos = None
		_hx_o.isHint_cache = None
		_hx_o.isHint_cache_set = None
		_hx_o.complete_offset_in_bytes_cache = None
		_hx_o.complete_offset_in_bytes_cache_set = None
		_hx_o.orig_file_cache = None
		_hx_o.orig_file_cache_set = None
		_hx_o.build_cache = None
		_hx_o.build_cache_set = None
		_hx_o.completeCharIsAfterControlStruct_cache = None
		_hx_o.completeCharIsAfterControlStruct_cache_set = None
		_hx_o.inControlStruct_cache = None
		_hx_o.inControlStruct_cache_set = None
		_hx_o.srcUntilCompleteOffset_cache = None
		_hx_o.srcUntilCompleteOffset_cache_set = None
		_hx_o.lineAfterOffset_cache = None
		_hx_o.lineAfterOffset_cache_set = None
		_hx_o.src_cache = None
		_hx_o.src_cache_set = None
		_hx_o.completeChar_cache = None
		_hx_o.completeChar_cache_set = None
		_hx_o.completionInfo_cache = None
		_hx_o.completionInfo_cache_set = None
		_hx_o.commas_cache = None
		_hx_o.commas_cache_set = None
		_hx_o.complete_offset_cache = None
		_hx_o.complete_offset_cache_set = None
		_hx_o.is_new_cache = None
		_hx_o.is_new_cache_set = None
		_hx_o.srcUntilOffset_cache = None
		_hx_o.srcUntilOffset_cache_set = None
		_hx_o.tempCompletionSrc_cache = None
		_hx_o.tempCompletionSrc_cache_set = None
		_hx_o.prefixIsWhitespace_cache = None
		_hx_o.prefixIsWhitespace_cache_set = None
hxsublime_completion_hx_CompletionContext._hx_class = hxsublime_completion_hx_CompletionContext
_hx_classes["hxsublime.completion.hx.CompletionContext"] = hxsublime_completion_hx_CompletionContext


class hxsublime_completion_hx_CompletionOptions:
	_hx_class_name = "hxsublime.completion.hx.CompletionOptions"
	_hx_fields = ["userActivated"]
	_hx_methods = ["copy", "eq"]
	_hx_interfaces = [hxsublime_macros_LazyFunctionSupport]

	def __init__(self,userActivated = False):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionOptions.hx:27
		if (userActivated is None):
			userActivated = False
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionOptions.hx:25
		self.userActivated = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionOptions.hx:29
		self.userActivated = userActivated

	def copy(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionOptions.hx:34
		return hxsublime_completion_hx_CompletionOptions(self.userActivated)

	def eq(self,other):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionOptions.hx:39
		return (self.userActivated == other.userActivated)

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.userActivated = None
hxsublime_completion_hx_CompletionOptions._hx_class = hxsublime_completion_hx_CompletionOptions
_hx_classes["hxsublime.completion.hx.CompletionOptions"] = hxsublime_completion_hx_CompletionOptions


class hxsublime_completion_hx_CompletionResult:
	_hx_class_name = "hxsublime.completion.hx.CompletionResult"
	_hx_fields = ["hints", "ctx", "ret", "comps", "status", "retrieve_toplevel_comps", "_toplevel_comps_cache", "_toplevel_comps_cache_set", "hasHints_cache", "hasHints_cache_set", "hasCompilerResults_cache", "hasCompilerResults_cache_set", "hasResults_cache", "hasResults_cache_set", "showTopLevelSnippets_cache", "showTopLevelSnippets_cache_set", "requiresToplevelComps_cache", "requiresToplevelComps_cache_set", "allComps_cache", "allComps_cache_set"]
	_hx_methods = ["_toplevel_comps", "hasHints", "hasCompilerResults", "hasResults", "showTopLevelSnippets", "requiresToplevelComps", "allComps"]
	_hx_statics = ["emptyResult"]
	_hx_interfaces = [hxsublime_macros_LazyFunctionSupport]

	def __init__(self,ret,comps,status,hints,ctx,retrieve_toplevel_comps):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:28
		self.hints = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:29
		self.ctx = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:31
		self.ret = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:32
		self.comps = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:33
		self.status = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:36
		self.retrieve_toplevel_comps = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:58
		self._toplevel_comps_cache = None
		self._toplevel_comps_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:64
		self.hasHints_cache = None
		self.hasHints_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:69
		self.hasCompilerResults_cache = None
		self.hasCompilerResults_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:74
		self.hasResults_cache = None
		self.hasResults_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:79
		self.showTopLevelSnippets_cache = None
		self.showTopLevelSnippets_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:90
		self.requiresToplevelComps_cache = None
		self.requiresToplevelComps_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:99
		self.allComps_cache = None
		self.allComps_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:34
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
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:43
		self.ret = ret
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:44
		self.comps = comps
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:45
		self.status = status
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:46
		self.hints = hints
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:47
		self.ctx = ctx
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:48
		if (retrieve_toplevel_comps is None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:50
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:50
				return []
			retrieve_toplevel_comps = _hx_local_0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:53
		self.retrieve_toplevel_comps = retrieve_toplevel_comps

	def _toplevel_comps(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:58
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self._toplevel_comps_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self._toplevel_comps_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:60
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:60
				return _g.retrieve_toplevel_comps()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self._toplevel_comps_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self._toplevel_comps_cache

	def hasHints(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:64
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.hasHints_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.hasHints_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:65
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:65
				return (len(_g.hints) > 0)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.hasHints_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.hasHints_cache

	def hasCompilerResults(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:69
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.hasCompilerResults_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.hasCompilerResults_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:70
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:70
				return (len(_g.comps) > 0)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.hasCompilerResults_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.hasCompilerResults_cache

	def hasResults(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:74
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.hasResults_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.hasResults_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:75
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:75
				return (((len(_g.comps) > 0) or ((len(_g.hints) > 0))) or ((_g.requiresToplevelComps() and ((len(_g._toplevel_comps()) > 0)))))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.hasResults_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.hasResults_cache

	def showTopLevelSnippets(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:79
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.showTopLevelSnippets_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.showTopLevelSnippets_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:80
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:81
				req = _g.requiresToplevelComps()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:83
				r = (req and (not _g.ctx.is_new()))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:85
				return r
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.showTopLevelSnippets_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.showTopLevelSnippets_cache

	def requiresToplevelComps(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:90
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.requiresToplevelComps_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.requiresToplevelComps_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:91
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:92
				prefix_is_whitespace = hxsublime_tools_StringTools.isWhitespaceOrEmpty(_g.ctx.prefix)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:94
				r = (not ((((prefix_is_whitespace and _g.hasHints()) and _g.ctx.isHint()) or _g.hasCompilerResults())))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:95
				return r
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.requiresToplevelComps_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.requiresToplevelComps_cache

	def allComps(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:99
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.allComps_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.allComps_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:100
			def _hx_local_1():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:101
				res = []
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:103
				if _g.requiresToplevelComps():
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:104
					x = _g._toplevel_comps()
					res.extend(x)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:106
				res.extend(_g.comps)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:107
				def _hx_local_0(s1,s2):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:107
					if (s1[0] < s2[0]):
						return -1
					elif (s1[0] > s2[0]):
						return 1
					else:
						return 0
				res.sort(key= python_lib_Functools.cmp_to_key(_hx_local_0))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:108
				return res
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.allComps_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.allComps_cache

	@staticmethod
	def emptyResult(ctx,retrieve_toplevel_comps = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionResult.hx:25
		return hxsublime_completion_hx_CompletionResult("", [], "", [], ctx, retrieve_toplevel_comps)

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.hints = None
		_hx_o.ctx = None
		_hx_o.ret = None
		_hx_o.comps = None
		_hx_o.status = None
		_hx_o.retrieve_toplevel_comps = None
		_hx_o._toplevel_comps_cache = None
		_hx_o._toplevel_comps_cache_set = None
		_hx_o.hasHints_cache = None
		_hx_o.hasHints_cache_set = None
		_hx_o.hasCompilerResults_cache = None
		_hx_o.hasCompilerResults_cache_set = None
		_hx_o.hasResults_cache = None
		_hx_o.hasResults_cache_set = None
		_hx_o.showTopLevelSnippets_cache = None
		_hx_o.showTopLevelSnippets_cache_set = None
		_hx_o.requiresToplevelComps_cache = None
		_hx_o.requiresToplevelComps_cache_set = None
		_hx_o.allComps_cache = None
		_hx_o.allComps_cache_set = None
hxsublime_completion_hx_CompletionResult._hx_class = hxsublime_completion_hx_CompletionResult
_hx_classes["hxsublime.completion.hx.CompletionResult"] = hxsublime_completion_hx_CompletionResult


class hxsublime_completion_hx_CompletionSettings:
	_hx_class_name = "hxsublime.completion.hx.CompletionSettings"
	_hx_fields = ["settings"]
	_hx_methods = ["showCompletionTimes"]
	_hx_interfaces = [hxsublime_macros_LazyFunctionSupport]

	def __init__(self,settings):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionSettings.hx:26
		self.settings = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionSettings.hx:29
		self.settings = settings

	def showCompletionTimes(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/CompletionSettings.hx:34
		return self.settings.showCompletionTimes(view)

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.settings = None
hxsublime_completion_hx_CompletionSettings._hx_class = hxsublime_completion_hx_CompletionSettings
_hx_classes["hxsublime.completion.hx.CompletionSettings"] = hxsublime_completion_hx_CompletionSettings


class hxsublime_completion_hx_HxCompletion:
	_hx_class_name = "hxsublime.completion.hx.HxCompletion"
	_hx_statics = ["eventTriggeredAutoComplete", "commandTriggeredAutoComplete", "createCompletionContext", "autoComplete", "createCompletionBuild", "runCompilerCompletion", "completionFinished", "hintsToSublimeCompletions", "combineHintsAndComps", "isEquivalentCompletionAlreadyRunning", "shouldIncludeTopLevelCompletion", "getToplevelCompletions", "updateCompletionCache", "outputToResult", "useCompletionCache", "supportedCompilerCompletionChar", "highlightErrors", "cancelCompletion", "shouldOnlyInsertHint", "autoCompleteAsync", "triggerAsyncCompletion"]

	@staticmethod
	def eventTriggeredAutoComplete(project,view,offset,prefix):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:37
		haxe_Log.trace("------- EVENT TRIGGERED COMPLETION -----------",_hx_AnonObject({'fileName': "HxCompletion.hx", 'lineNumber': 37, 'className': "hxsublime.completion.hx.HxCompletion", 'methodName': "eventTriggeredAutoComplete"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:38
		options = hxsublime_completion_hx_CompletionOptions(False)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:39
		ctx = hxsublime_completion_hx_HxCompletion.createCompletionContext(project,view,offset,options,prefix)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:40
		return hxsublime_completion_hx_HxCompletion.autoComplete(ctx)

	@staticmethod
	def commandTriggeredAutoComplete(project,view,offset,options,prefix):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:45
		haxe_Log.trace("------- COMMAND TRIGGERED COMPLETION -----------",_hx_AnonObject({'fileName': "HxCompletion.hx", 'lineNumber': 45, 'className': "hxsublime.completion.hx.HxCompletion", 'methodName': "commandTriggeredAutoComplete"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:46
		ctx = hxsublime_completion_hx_HxCompletion.createCompletionContext(project,view,offset,options,prefix)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:47
		return hxsublime_completion_hx_HxCompletion.autoComplete(ctx)

	@staticmethod
	def createCompletionContext(project,view,offset,options,prefix):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:53
		settings = hxsublime_completion_hx_CompletionSettings(hxsublime_Settings)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:54
		return hxsublime_completion_hx_CompletionContext(view, project, offset, options, settings, prefix)

	@staticmethod
	def autoComplete(ctx):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:59
		project = ctx.project
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:60
		view = ctx.view
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:62
		cache = project.completionContext.current
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:65
		hxsublime_completion_hx_HxCompletion.cancelCompletion(view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:67
		if hxsublime_completion_hx_HxCompletion.isEquivalentCompletionAlreadyRunning(ctx):
			haxe_Log.trace("cancel completion, same is running",_hx_AnonObject({'fileName': "HxCompletion.hx", 'lineNumber': 69, 'className': "hxsublime.completion.hx.HxCompletion", 'methodName': "autoComplete"}))
		elif hxsublime_completion_hx_HxCompletion.useCompletionCache(ctx,cache.input):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:73
			haxe_Log.trace("use completion cache",_hx_AnonObject({'fileName': "HxCompletion.hx", 'lineNumber': 73, 'className': "hxsublime.completion.hx.HxCompletion", 'methodName': "autoComplete"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:74
			out = cache.output
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:76
			hxsublime_completion_hx_HxCompletion.updateCompletionCache(cache,out)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:77
			hxsublime_completion_hx_HxCompletion.triggerAsyncCompletion(ctx,out,out.showTopLevelSnippets())
		elif hxsublime_completion_hx_HxCompletion.supportedCompilerCompletionChar(ctx.completeChar()):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:81
			haxe_Log.trace("call compiler for completion",_hx_AnonObject({'fileName': "HxCompletion.hx", 'lineNumber': 81, 'className': "hxsublime.completion.hx.HxCompletion", 'methodName': "autoComplete"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:82
			compBuild = hxsublime_completion_hx_HxCompletion.createCompletionBuild(ctx)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:83
			if (compBuild is not None):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:84
				def _hx_local_0(out1,err):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:84
					hxsublime_completion_hx_HxCompletion.completionFinished(ctx,compBuild,out1,err)
				cb = _hx_local_0
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:85
				hxsublime_completion_hx_HxCompletion.runCompilerCompletion(compBuild,cb)
		else:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:90
			haxe_Log.trace("only toplevel + snippets",_hx_AnonObject({'fileName': "HxCompletion.hx", 'lineNumber': 90, 'className': "hxsublime.completion.hx.HxCompletion", 'methodName': "autoComplete"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:91
			def _hx_local_1():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:91
				return hxsublime_completion_hx_HxCompletion.getToplevelCompletions(ctx)
			compResult = hxsublime_completion_hx_CompletionResult.emptyResult(ctx,_hx_local_1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:92
			hxsublime_completion_hx_HxCompletion.updateCompletionCache(cache,compResult)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:93
			hxsublime_completion_hx_HxCompletion.triggerAsyncCompletion(ctx,compResult,compResult.showTopLevelSnippets())
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:95
		return []

	@staticmethod
	def createCompletionBuild(ctx):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:100
		tmp_src = ctx.tempCompletionSrc()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:102
		r = hxsublime_Temp.createTempPathAndFile(ctx.build(),ctx.orig_file(),tmp_src)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:103
		tempPath = r[0]
		tempFile = r[1]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:105
		temp_creation_success = ((tempPath is not None) and ((tempFile is not None)))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:108
		def _hx_local_0():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:109
			compBuild = hxsublime_completion_hx_CompletionBuild(ctx, tempPath, tempFile)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:110
			build = compBuild.build
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:111
			display = compBuild.display()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:114
			build.setAutoCompletion(display,False)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:115
			if ctx.settings.showCompletionTimes(compBuild.ctx.view):
				build.setTimes()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:119
			return compBuild
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:107
		mkBuild = _hx_local_0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:121
		if temp_creation_success:
			return mkBuild()
		else:
			return None

	@staticmethod
	def runCompilerCompletion(compBuild,callback):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:128
		startTime = python_lib_Time.time()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:129
		ctx = compBuild.ctx
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:130
		project = ctx.project
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:131
		build = compBuild.build
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:132
		view = ctx.view
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:133
		haxe_Log.trace("__________COMPLETION INFO________________",_hx_AnonObject({'fileName': "HxCompletion.hx", 'lineNumber': 133, 'className': "hxsublime.completion.hx.HxCompletion", 'methodName': "runCompilerCompletion"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:134
		haxe_Log.trace(compBuild.display(),_hx_AnonObject({'fileName': "HxCompletion.hx", 'lineNumber': 134, 'className': "hxsublime.completion.hx.HxCompletion", 'methodName': "runCompilerCompletion"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:135
		haxe_Log.trace(compBuild.tempFile,_hx_AnonObject({'fileName': "HxCompletion.hx", 'lineNumber': 135, 'className': "hxsublime.completion.hx.HxCompletion", 'methodName': "runCompilerCompletion"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:136
		haxe_Log.trace(sys_io_File.getContent(compBuild.tempFile),_hx_AnonObject({'fileName': "HxCompletion.hx", 'lineNumber': 136, 'className': "hxsublime.completion.hx.HxCompletion", 'methodName': "runCompilerCompletion"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:137
		haxe_Log.trace("_________________________________________",_hx_AnonObject({'fileName': "HxCompletion.hx", 'lineNumber': 137, 'className': "hxsublime.completion.hx.HxCompletion", 'methodName': "runCompilerCompletion"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:139
		def _hx_local_1(out,err):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:141
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:142
				runTime = (python_lib_Time.time() - startTime)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:143
				haxe_Log.trace(("completion time: " + Std.string(runTime)),_hx_AnonObject({'fileName': "HxCompletion.hx", 'lineNumber': 143, 'className': "hxsublime.completion.hx.HxCompletion", 'methodName': "runCompilerCompletion"}))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:144
				hxsublime_Temp.removePath(compBuild.tempPath)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:145
				callback(out,err)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:140
			run = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:151
			project.completionContext.runIfStillUpToDate(ctx.id,run)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:138
		inMainThread = _hx_local_1
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:155
		def _hx_local_4(out1,err1):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:155
			def _hx_local_2():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:155
				f = inMainThread
				a1 = out1
				a2 = err1
				def _hx_local_3():
					f(a1,a2)
				return _hx_local_3
			sublime_Sublime.set_timeout(_hx_local_2(),2)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:153
		onResult = _hx_local_4
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:159
		project.completionContext.setNewCompletion(ctx)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:161
		build.run(project,view,True,onResult)

	@staticmethod
	def completionFinished(ctx,compBuild,out,err):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:166
		ctx1 = compBuild.ctx
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:167
		tempFile = compBuild.tempFile
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:169
		cache = compBuild.cache
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:171
		project = ctx1.project
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:172
		view = ctx1.view
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:175
		def _hx_local_0():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:175
			return hxsublime_completion_hx_HxCompletion.getToplevelCompletions(ctx1)
		compResult = hxsublime_completion_hx_HxCompletion.outputToResult(ctx1,tempFile,err,out,_hx_local_0)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:177
		hasResults = compResult.hasResults()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:179
		if hasResults:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:181
			hxsublime_completion_hx_HxCompletion.updateCompletionCache(cache,compResult)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:182
			showTopLevelSnippets = compResult.showTopLevelSnippets()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:183
			hxsublime_completion_hx_HxCompletion.triggerAsyncCompletion(ctx1,compResult,showTopLevelSnippets)
		else:
			haxe_Log.trace("ignore background completion on finished",_hx_AnonObject({'fileName': "HxCompletion.hx", 'lineNumber': 187, 'className': "hxsublime.completion.hx.HxCompletion", 'methodName': "completionFinished"}))

	@staticmethod
	def hintsToSublimeCompletions(hints):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:195
		def _hx_local_3(h):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:196
			hintIsJustAType = (len(h) == 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:198
			res = None
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:200
			if hintIsJustAType:
				res = ((HxOverrides.stringOrNull((h[0] if 0 < len(h) else None)) + " - No Completion"), "${}")
			else:
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:204
				isFunctionWithoutParams = ((len(h) == 2) and (((h[0] if 0 < len(h) else None) == "Void")))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:206
				insert = None
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:207
				show = None
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:209
				if isFunctionWithoutParams:
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:211
					insert = ")"
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:212
					show = "Void"
				else:
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:217
					def _hx_local_0(p):
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:217
						_this = p.split("}")
						return "\\}".join([python_Boot.toString1(x1,'') for x1 in _this])
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:216
					escapeParam = _hx_local_0
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:219
					last_index = (len(h) - 1)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:220
					params = h[0:last_index]
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:222
					show = ", ".join([python_Boot.toString1(x1,'') for x1 in params])
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:224
					if hxsublime_Settings.smartSnippetsJustCurrent():
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:227
						first = escapeParam((params[0] if 0 < len(params) else None))
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:230
						if (len(params) == 1):
							insert = (("${1:" + ("null" if first is None else first)) + "})${0}")
						else:
							insert = (("${0:" + ("null" if first is None else first)) + "}")
					else:
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:239
						def _hx_local_1(listIndex):
							# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:239
							return Std.string((listIndex + 1))
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:237
						getSnippetIndex = _hx_local_1
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:244
						def _hx_local_2(param,index):
							# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:244
							return (((("${" + HxOverrides.stringOrNull(getSnippetIndex(index))) + ":") + HxOverrides.stringOrNull(escapeParam(param))) + "}")
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:242
						paramSnippet = _hx_local_2
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:247
						snippetList = None
						_g = []
						_g2 = 0
						_g1 = len(params)
						while (_g2 < _g1):
							index1 = _g2
							_g2 = (_g2 + 1)
							x = paramSnippet((params[index1] if index1 >= 0 and index1 < len(params) else None),index1)
							_g.append(x)
						snippetList = _g
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:249
						insert = (HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in snippetList])) + ")${0}")
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:253
				res = (show, insert)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:255
			return res
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:194
		makeHintComp = _hx_local_3
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:257
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:257
		_g3 = []
		_g11 = 0
		while (_g11 < len(hints)):
			h1 = (hints[_g11] if _g11 >= 0 and _g11 < len(hints) else None)
			_g11 = (_g11 + 1)
			x1 = makeHintComp(h1)
			_g3.append(x1)
		return _g3

	@staticmethod
	def combineHintsAndComps(compResult):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:262
		hints = compResult.hints
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:264
		all_comps = hxsublime_completion_hx_HxCompletion.hintsToSublimeCompletions(hints)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:266
		if ((not compResult.ctx.isHint()) or ((len(hints) == 0))):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:268
			haxe_Log.trace("TAKE TOP LEVEL COMPS",_hx_AnonObject({'fileName': "HxCompletion.hx", 'lineNumber': 268, 'className': "hxsublime.completion.hx.HxCompletion", 'methodName': "combineHintsAndComps"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:269
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:269
			x = compResult.allComps()
			all_comps.extend(x)
		elif (len(hints) == 1):
			sublime_Sublime.status_message(("signature: " + HxOverrides.stringOrNull("->".join([python_Boot.toString1(x1,'') for x1 in (hints[0] if 0 < len(hints) else None)]))))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:276
		return all_comps

	@staticmethod
	def isEquivalentCompletionAlreadyRunning(ctx):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:281
		return ctx.project.completionContext.isEquivalentCompletionAlreadyRunning(ctx)

	@staticmethod
	def shouldIncludeTopLevelCompletion(ctx):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:286
		haxe_Log.trace((("complete Char: '" + HxOverrides.stringOrNull(ctx.completeChar())) + "'"),_hx_AnonObject({'fileName': "HxCompletion.hx", 'lineNumber': 286, 'className': "hxsublime.completion.hx.HxCompletion", 'methodName': "shouldIncludeTopLevelCompletion"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:288
		validChar = None
		def _hx_local_0():
			_hx_str = ctx.completeChar()
			return ":(,{;})".find(_hx_str)
		validChar = (_hx_local_0() > -1)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:290
		toplevel_complete = ((validChar or ctx.inControlStruct()) or ctx.is_new())
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:292
		return toplevel_complete

	@staticmethod
	def getToplevelCompletions(ctx):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:297
		user = ctx.options.userActivated
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:299
		settingsValid = (not hxsublime_Settings.topLevelCompletionsOnDemand())
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:300
		prefixValid = (ctx.prefix != "")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:302
		userOrValid = (user or ((prefixValid and settingsValid)))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:304
		toplevelInclude = (userOrValid and hxsublime_completion_hx_HxCompletion.shouldIncludeTopLevelCompletion(ctx))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:307
		comps = None
		if toplevelInclude:
			comps = hxsublime_completion_hx_TopLevel.getToplevelCompletionFiltered(ctx)
		else:
			comps = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:311
		return comps

	@staticmethod
	def updateCompletionCache(cache,compResult):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:316
		cache.output = compResult
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:317
		cache.input = compResult.ctx

	@staticmethod
	def outputToResult(ctx,temp_file,err,ret,retrieve_tl_comps):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:322
		r = hxsublime_compiler_Output.getCompletionOutput(temp_file,ctx.orig_file(),err,ctx.commas())
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:323
		hints = r[0]
		comps1 = r[1]
		status = r[2]
		errors = r[3]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:326
		comps2 = None
		_g = []
		_g1 = 0
		while (_g1 < len(comps1)):
			t = (comps1[_g1] if _g1 >= 0 and _g1 < len(comps1) else None)
			_g1 = (_g1 + 1)
			x = (t.hint, t.insert)
			_g.append(x)
		comps2 = _g
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:327
		ctx.project.completionContext.setErrors(errors)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:328
		if ctx.options.userActivated:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:329
			haxe_Log.trace("do highlight",_hx_AnonObject({'fileName': "HxCompletion.hx", 'lineNumber': 329, 'className': "hxsublime.completion.hx.HxCompletion", 'methodName': "outputToResult"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:330
			hxsublime_completion_hx_HxCompletion.highlightErrors(errors,ctx.view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:333
		return hxsublime_completion_hx_CompletionResult(ret, comps2, status, hints, ctx, retrieve_tl_comps)

	@staticmethod
	def useCompletionCache(lastInput,current_input):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:338
		return lastInput.eq(current_input)

	@staticmethod
	def supportedCompilerCompletionChar(char):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:343
		return ("(.,".find(char) > -1)

	@staticmethod
	def highlightErrors(errors,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:348
		regions = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:350
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:350
		_g = 0
		while (_g < len(errors)):
			e = (errors[_g] if _g >= 0 and _g < len(errors) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:352
			l = e.line
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:353
			left = e._hx_from
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:354
			right = e.to
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:355
			a = view.text_point(l,left)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:356
			b = view.text_point(l,right)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:357
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:357
			x = sublime_Region(a, b)
			regions.append(x)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:359
			hxsublime_panel_Panels.defaultPanel().status("Error",((((((((HxOverrides.stringOrNull(e.file) + ":") + Std.string(l)) + ": characters ") + Std.string(left)) + "-") + Std.string(right)) + ": ") + HxOverrides.stringOrNull(e.message)))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:362
		view.add_regions("haxe-error",regions,"invalid","dot")

	@staticmethod
	def cancelCompletion(view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:367
		view.run_command("hide_auto_complete")

	@staticmethod
	def shouldOnlyInsertHint(ctx,result):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:372
		view = ctx.view
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:373
		use_snippets = hxsublime_Settings.smartSnippets(view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:374
		prefix_is_whitespace = hxsublime_tools_StringTools.isWhitespaceOrEmpty(result.ctx.prefix)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:375
		has_one_hint = (ctx.isHint() and ((len(result.hints) == 1)))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:376
		same_cursor_pos = (hxsublime_tools_ViewTools.getFirstCursorPos(view) == result.ctx.view_pos)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:380
		lineAfterOffset = None
		s = result.ctx.lineAfterOffset()
		lineAfterOffset = s.strip(None)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:381
		really_insert = None
		def _hx_local_0():
			_hx_str = None
			if (0 >= len(lineAfterOffset)):
				_hx_str = ""
			else:
				_hx_str = lineAfterOffset[0]
			return "),".find(_hx_str)
		really_insert = ((len(lineAfterOffset) == 0) or ((_hx_local_0() > -1)))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:383
		return ((((really_insert and prefix_is_whitespace) and use_snippets) and has_one_hint) and same_cursor_pos)

	@staticmethod
	def autoCompleteAsync(ctx,res):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:389
		view = ctx.view
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:390
		ctx1 = res.ctx
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:391
		use_async_results = ((res is not None) and res.hasResults())
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:392
		if use_async_results:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:394
			comps = hxsublime_completion_hx_HxCompletion.combineHintsAndComps(res)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:395
			if hxsublime_completion_hx_HxCompletion.shouldOnlyInsertHint(ctx1,res):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:396
				onlyHint = (comps[0] if 0 < len(comps) else None)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:397
				hxsublime_tools_ViewTools.insertSnippet(view,onlyHint[1])
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:392
				return haxe_ds_Option._hx_None
			else:
				return haxe_ds_Option.Some(comps)
		else:
			return haxe_ds_Option._hx_None

	@staticmethod
	def triggerAsyncCompletion(ctx,res,showTopLevelSnippets = False):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:407
		if (showTopLevelSnippets is None):
			showTopLevelSnippets = False
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:408
		def _hx_local_0(_):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:408
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:408
			_g = hxsublime_completion_hx_HxCompletion.autoCompleteAsync(ctx,res)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:409
			if ((_g.index) == 0):
				x = _g.params[0]
				return x
			elif ((_g.index) == 1):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:410
				hxsublime_completion_hx_HxCompletion.cancelCompletion(ctx.view)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:408
				return []
			else:
				pass
		cb = _hx_local_0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:412
		haxe_Log.trace(("trigger with " + Std.string(showTopLevelSnippets)),_hx_AnonObject({'fileName': "HxCompletion.hx", 'lineNumber': 412, 'className': "hxsublime.completion.hx.HxCompletion", 'methodName': "triggerAsyncCompletion"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/HxCompletion.hx:413
		hxsublime_completion_CompletionListener.trigger(ctx.view,showTopLevelSnippets,cb)
hxsublime_completion_hx_HxCompletion._hx_class = hxsublime_completion_hx_HxCompletion
_hx_classes["hxsublime.completion.hx.HxCompletion"] = hxsublime_completion_hx_HxCompletion


class hxsublime_completion_hx_TopLevel:
	_hx_class_name = "hxsublime.completion.hx.TopLevel"
	_hx_statics = ["TOP_LEVEL_KEYWORDS", "getToplevelKeywords", "getBuildTarget", "getLocalVars", "getLocalFunctions", "getLocalFunctionParams", "getLocalVarsAndFunctions", "getImports", "getUsings", "getImportsAndUsings", "haxeTypeAsCompletion", "getTypeComps", "getToplevelCompletion", "getToplevelCompletionFiltered", "filterTopLevelCompletions"]

	@staticmethod
	def getToplevelKeywords(ctx):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:19
		if ctx.is_new():
			return []
		else:
			return hxsublime_completion_hx_TopLevel.TOP_LEVEL_KEYWORDS

	@staticmethod
	def getBuildTarget(ctx):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:24
		return ctx.build().target().plattform

	@staticmethod
	def getLocalVars(ctx):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:30
		comps = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:31
		def _hx_local_0():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:31
			this1 = hxsublime_tools_Regex.variables.finditer(ctx.src())
			return python_HaxeIterator(this1)
		_hx_local_1 = _hx_local_0()
		while _hx_local_1.hasNext():
			v = _hx_local_1.next()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:32
			x = None
			a = (HxOverrides.stringOrNull(v.group(1)) + "\tvar")
			b = v.group(1)
			x = (a, b)
			comps.append(x)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:34
		return comps

	@staticmethod
	def getLocalFunctions(ctx):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:39
		comps = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:40
		def _hx_local_0():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:40
			this1 = hxsublime_tools_Regex.named_functions.finditer(ctx.src())
			return python_HaxeIterator(this1)
		_hx_local_1 = _hx_local_0()
		while _hx_local_1.hasNext():
			i = _hx_local_1.next()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:42
			f = i.group(1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:43
			if (f != "new"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:45
				x = ((("null" if f is None else f) + "\tfunction"), f)
				comps.append(x)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:48
		return comps

	@staticmethod
	def getLocalFunctionParams(ctx):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:53
		comps = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:55
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:55
		_g = 0
		_g1 = None
		string = ctx.src()
		_g1 = python_lib__Re_RegexHelper.findallDynamic(hxsublime_tools_Regex.function_params,string,None,None)
		while (_g < len(_g1)):
			params_text = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:57
			cleaned_params_text = python_lib_Re.sub(hxsublime_tools_Regex.param_default,"",params_text)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:58
			params_list = cleaned_params_text.split(",")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:59
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:59
			_g2 = 0
			while (_g2 < len(params_list)):
				param = (params_list[_g2] if _g2 >= 0 and _g2 < len(params_list) else None)
				_g2 = (_g2 + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:61
				a = param.strip(None)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:62
				if StringTools.startsWith(a,"?"):
					a = HxString.substr(a,1,None)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:65
				idx = a.find(":")
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:66
				if (idx > -1):
					a = HxString.substring(a,0,idx)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:69
				idx1 = a.find("=")
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:70
				if (idx1 > -1):
					a = HxString.substring(a,0,idx1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:73
				a = a.strip(None)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:74
				cm = ((("null" if a is None else a) + "\tvar"), a)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:75
				if (not Lambda.has(comps,cm)):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:76
					comps.append(cm)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:79
		return comps

	@staticmethod
	def getLocalVarsAndFunctions(ctx):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:83
		comps = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:84
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:84
		x = hxsublime_completion_hx_TopLevel.getLocalVars(ctx)
		comps.extend(x)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:85
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:85
		x1 = hxsublime_completion_hx_TopLevel.getLocalFunctions(ctx)
		comps.extend(x1)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:86
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:86
		x2 = hxsublime_completion_hx_TopLevel.getLocalFunctionParams(ctx)
		comps.extend(x2)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:88
		return comps

	@staticmethod
	def getImports(ctx):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:93
		imports = None
		string = ctx.src()
		imports = python_lib__Re_RegexHelper.findallDynamic(hxsublime_tools_Regex.import_line,string,None,None)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:94
		imported = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:95
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:95
		_g = 0
		while (_g < len(imports)):
			i = (imports[_g] if _g >= 0 and _g < len(imports) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:97
			imp = i[1]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:98
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:98
			imported.append(imp)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:101
		return imported

	@staticmethod
	def getUsings(ctx):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:106
		usings = None
		string = ctx.src()
		usings = python_lib__Re_RegexHelper.findallDynamic(hxsublime_tools_Regex.using_line,string,None,None)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:107
		used = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:108
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:108
		_g = 0
		while (_g < len(usings)):
			i = (usings[_g] if _g >= 0 and _g < len(usings) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:110
			imp = i[1]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:111
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:111
			used.append(imp)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:114
		return used

	@staticmethod
	def getImportsAndUsings(ctx):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:119
		res = hxsublime_completion_hx_TopLevel.getImports(ctx)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:121
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:121
		a = hxsublime_completion_hx_TopLevel.getUsings(ctx)
		res = (res + a)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:123
		return res

	@staticmethod
	def haxeTypeAsCompletion(_hx_type):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:128
		insert = _hx_type.full_pack_with_optional_module_type_and_enum_value
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:129
		display = _hx_type.type_name_with_optional_enum_value
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:130
		display = (("null" if display is None else display) + HxOverrides.stringOrNull((("\t" + HxOverrides.stringOrNull(_hx_type.get_type_hint)))))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:131
		return (display, insert)

	@staticmethod
	def getTypeComps(ctx,bundle,imported):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:136
		build_target = hxsublime_completion_hx_TopLevel.getBuildTarget(ctx)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:137
		comps = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:139
		allTypes = bundle.allTypes()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:141
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:141
		_g = 0
		while (_g < len(allTypes)):
			t = (allTypes[_g] if _g >= 0 and _g < len(allTypes) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:142
			if ctx.build().isTypeAvailable(t):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:143
				snippets = t.toSnippets(imported,ctx.orig_file())
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:144
				comps.extend(snippets)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:148
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:148
		_g1 = 0
		_g11 = bundle.packs()
		while (_g1 < len(_g11)):
			p = (_g11[_g1] if _g1 >= 0 and _g1 < len(_g11) else None)
			_g1 = (_g1 + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:149
			if ctx.build().isPackAvailable(p):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:150
				cm = ((("null" if p is None else p) + "\tpackage"), p)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:151
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:151
				comps.append(cm)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:155
		return comps

	@staticmethod
	def getToplevelCompletion(ctx):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:161
		comps = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:163
		if (not ctx.is_new()):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:164
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:164
			x = hxsublime_completion_hx_TopLevel.getToplevelKeywords(ctx)
			comps.extend(x)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:165
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:165
			x1 = hxsublime_completion_hx_TopLevel.getLocalVarsAndFunctions(ctx)
			comps.extend(x1)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:168
		imported = hxsublime_completion_hx_TopLevel.getImportsAndUsings(ctx)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:170
		buildBundle = ctx.build().getTypes()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:172
		stdBundle = ctx.build().stdBundle()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:176
		def _hx_local_0(t):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:176
			return ((not t.is_private) or ((t._file == ctx.orig_file())))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:174
		filterPrivates = _hx_local_0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:179
		merged_bundle = stdBundle.merge(buildBundle).filter(filterPrivates)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:181
		comps1 = hxsublime_completion_hx_TopLevel.getTypeComps(ctx,merged_bundle,imported)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:183
		comps.extend(comps1)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:185
		return comps

	@staticmethod
	def getToplevelCompletionFiltered(ctx):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:190
		comps = hxsublime_completion_hx_TopLevel.getToplevelCompletion(ctx)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:192
		return hxsublime_completion_hx_TopLevel.filterTopLevelCompletions(ctx.prefix,comps)

	@staticmethod
	def filterTopLevelCompletions(prefix,all_comps):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:197
		comps = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:199
		if (len(prefix) == 0):
			comps = list(all_comps)
		else:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:205
			test = []
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:206
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:206
			_g1 = 0
			_g = len(prefix)
			while (_g1 < _g):
				i = _g1
				_g1 = (_g1 + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:208
				c = None
				if ((i < 0) or ((i >= len(prefix)))):
					c = ""
				else:
					c = prefix[i]
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:210
				isLower = ("abcdefghijklmnopqrstuvwxyz".find(c) > -1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:211
				isUpper = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(c) > -1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:212
				is_digit = ("0123456789".find(c) > -1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:213
				is_special = ("$_#".find(c) > -1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:214
				if (((isLower or isUpper) or is_digit) or is_special):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:216
					offsetUpper = c.upper()
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:217
					offsetLower = c.lower()
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:219
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:219
					test.append(offsetLower)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:222
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:222
			_g2 = 0
			while (_g2 < len(all_comps)):
				c1 = (all_comps[_g2] if _g2 >= 0 and _g2 < len(all_comps) else None)
				_g2 = (_g2 + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:224
				found = True
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:225
				id = c1[1].lower()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:227
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:227
				_g11 = 0
				while (_g11 < len(test)):
					cur = (test[_g11] if _g11 >= 0 and _g11 < len(test) else None)
					_g11 = (_g11 + 1)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:229
					if found:
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:231
						index = id.find(cur)
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:233
						if (index > -1):
							id = HxString.substr(id,(index + 1),None)
						else:
							# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:239
							found = False
							# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:240
							break
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:244
				if found:
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:246
					comps.append(c1)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:250
		haxe_Log.trace((((("number of top level completions (all: " + Std.string(len(all_comps))) + ", filtered: ") + Std.string(len(comps))) + ")"),_hx_AnonObject({'fileName': "Toplevel.hx", 'lineNumber': 250, 'className': "hxsublime.completion.hx.TopLevel", 'methodName': "filterTopLevelCompletions"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hx/Toplevel.hx:251
		return comps
hxsublime_completion_hx_TopLevel._hx_class = hxsublime_completion_hx_TopLevel
_hx_classes["hxsublime.completion.hx.TopLevel"] = hxsublime_completion_hx_TopLevel


class hxsublime_completion_hxml_HxmlCompletion:
	_hx_class_name = "hxsublime.completion.hxml.HxmlCompletion"
	_hx_statics = ["libFlag", "autoComplete"]

	@staticmethod
	def autoComplete(project,view,offset,prefix):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hxml/HxmlCompletion.hx:14
		src = view.substr(sublime_Region(0, offset))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hxml/HxmlCompletion.hx:15
		currentLine = None
		startIndex = (src.find("\n") + 1)
		currentLine = HxString.substring(src,startIndex,offset)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hxml/HxmlCompletion.hx:16
		m = hxsublime_completion_hxml_HxmlCompletion.libFlag.match(currentLine)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hxml/HxmlCompletion.hx:17
		if (m is not None):
			return project.haxelibManager().getCompletions()
		else:
			return []
hxsublime_completion_hxml_HxmlCompletion._hx_class = hxsublime_completion_hxml_HxmlCompletion
_hx_classes["hxsublime.completion.hxml.HxmlCompletion"] = hxsublime_completion_hxml_HxmlCompletion


class hxsublime_completion_hxsl_HxslCompletion:
	_hx_class_name = "hxsublime.completion.hxsl.HxslCompletion"
	_hx_statics = ["autoComplete"]

	@staticmethod
	def autoComplete(project,view,offset,prefix):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hxsl/HxslCompletion.hx:11
		comps = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hxsl/HxslCompletion.hx:12
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hxsl/HxslCompletion.hx:12
		_g = 0
		_g1 = ["Float", "Float2", "Float3", "Float4", "Matrix", "M44", "M33", "M34", "M43", "Texture", "CubeTexture", "Int", "Color", "include"]
		while (_g < len(_g1)):
			t = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hxsl/HxslCompletion.hx:14
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hxsl/HxslCompletion.hx:14
			x = (t, "hxsl Type")
			comps.append(x)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/completion/hxsl/HxslCompletion.hx:16
		return comps
hxsublime_completion_hxsl_HxslCompletion._hx_class = hxsublime_completion_hxsl_HxslCompletion
_hx_classes["hxsublime.completion.hxsl.HxslCompletion"] = hxsublime_completion_hxsl_HxslCompletion


class hxsublime_panel_PanelCloseListener(sublime_EventListener):
	_hx_class_name = "hxsublime.panel.PanelCloseListener"
	_hx_fields = []
	_hx_methods = ["on_close"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = sublime_EventListener


	def on_close(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/Panels.hx:18
		win = view.window()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/Panels.hx:19
		if (win is None):
			win = sublime_Sublime.active_window()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/Panels.hx:23
		win_id = win.id()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/Panels.hx:24
		view_id = view.id()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/Panels.hx:26
		if win_id in hxsublime_panel_Panels._slidePanels.h:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/Panels.hx:28
			panel = hxsublime_panel_Panels.slidePanel(win)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/Panels.hx:29
			if ((panel.outputView is not None) and ((view_id == panel.outputView.id()))):
				panel.outputView = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/Panels.hx:35
		panel_win_id = view.settings().get("haxe_panel_win_id")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/Panels.hx:36
		if (panel_win_id is not None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/Panels.hx:38
			_g = 0
			_g1 = [hxsublime_panel_Panels._debugPanels]
			while (_g < len(_g1)):
				p = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
				_g = (_g + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/Panels.hx:40
				panel1 = p.getOrDefault(panel_win_id,None)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/Panels.hx:41
				if (((panel1 is not None) and ((panel1.outputView is not None))) and ((view_id == panel1.outputViewId))):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/Panels.hx:43
					haxe_Log.trace("panel safely removed",_hx_AnonObject({'fileName': "Panels.hx", 'lineNumber': 43, 'className': "hxsublime.panel.PanelCloseListener", 'methodName': "on_close"}))
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/Panels.hx:44
					panel1.outputView = None
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/Panels.hx:45
					panel1.outputViewId = None

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_panel_PanelCloseListener._hx_class = hxsublime_panel_PanelCloseListener
_hx_classes["hxsublime.panel.PanelCloseListener"] = hxsublime_panel_PanelCloseListener


class hxsublime_tools_Cache:
	_hx_class_name = "hxsublime.tools.Cache"
	_hx_fields = ["time_driven", "cache_time", "data"]
	_hx_methods = ["insert", "exists", "getOrInsert", "unsafeGetVal", "isCacheInvalid", "isCacheValid", "getOrDefault", "getAndDelete", "delete"]

	def __init__(self,data,cache_time = -1):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:20
		if (cache_time is None):
			cache_time = -1
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:15
		self.time_driven = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:16
		self.cache_time = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:18
		self.data = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:22
		self.data = data
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:23
		self.cache_time = cache_time
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:24
		self.time_driven = (cache_time != -1)

	def insert(self,id,value):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:29
		self.data.set(id,_hx_AnonObject({'time': python_lib_Time.time(), 'val': value}))

	def exists(self,id):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:34
		return (self.getOrDefault(id,None) is not None)

	def getOrInsert(self,id,creator):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:39
		res = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:40
		if self.data.exists(id):
			res = self.unsafeGetVal(id)
		else:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:44
			res = creator()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:45
			self.insert(id,res)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:47
		return res

	def unsafeGetVal(self,id):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:52
		return self.data.get(id).val

	def isCacheInvalid(self,id):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:57
		return (not self.isCacheValid(id))

	def isCacheValid(self,id):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:62
		now = python_lib_Time.time()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:64
		return ((now - self.data.get(id).time) <= self.cache_time)

	def getOrDefault(self,id,defaultVal = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:69
		res = defaultVal
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:70
		if self.data.exists(id):
			if (self.time_driven and self.isCacheInvalid(id)):
				self.data.remove(id)
			else:
				res = self.unsafeGetVal(id)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:78
		return res

	def getAndDelete(self,id,defaultVal = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:83
		val = defaultVal
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:84
		if self.data.exists(id):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:86
			if ((not self.time_driven) or self.isCacheValid(id)):
				val = self.unsafeGetVal(id)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:90
			self.data.remove(id)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:92
		return val

	def delete(self,id):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/Cache.hx:97
		if self.data.exists(id):
			self.data.remove(id)

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.time_driven = None
		_hx_o.cache_time = None
		_hx_o.data = None
hxsublime_tools_Cache._hx_class = hxsublime_tools_Cache
_hx_classes["hxsublime.tools.Cache"] = hxsublime_tools_Cache


class hxsublime_panel_Panels:
	_hx_class_name = "hxsublime.panel.Panels"
	_hx_statics = ["_debugPanels", "_slidePanels", "defaultPanel", "slidePanel"]

	@staticmethod
	def defaultPanel(win = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/Panels.hx:64
		return hxsublime_panel_Panels.slidePanel(win)

	@staticmethod
	def slidePanel(win = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/Panels.hx:69
		if (win is None):
			win = sublime_Sublime.active_window()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/Panels.hx:74
		win_id = win.id()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/Panels.hx:76
		if (not win_id in hxsublime_panel_Panels._slidePanels.h):
			hxsublime_panel_Panels._slidePanels.set(win_id,hxsublime_panel_SlidePanel(win))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/Panels.hx:80
		return hxsublime_panel_Panels._slidePanels.h.get(win_id,None)
hxsublime_panel_Panels._hx_class = hxsublime_panel_Panels
_hx_classes["hxsublime.panel.Panels"] = hxsublime_panel_Panels


class hxsublime_panel_SlidePanel:
	_hx_class_name = "hxsublime.panel.SlidePanel"
	_hx_fields = ["win", "outputView", "outputViewId"]
	_hx_methods = ["clear", "write", "writeln", "status"]

	def __init__(self,win):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:15
		self.win = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:16
		self.outputView = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:17
		self.outputViewId = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:21
		self.win = win
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:22
		self.outputView = None

	def clear(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:27
		self.outputView = self.win.create_output_panel("haxe")

	def write(self,text,scope = None,show_timestamp = True):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:31
		if (show_timestamp is None):
			show_timestamp = True
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:33
		win = self.win
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:35
		if (self.outputView is None):
			self.outputView = win.create_output_panel("haxe")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:40
		self.outputView.settings().set("result_file_regex",hxsublime_panel_Tools.haxeFileRegex())
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:42
		win.create_output_panel("haxe")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:44
		panel = self.outputView
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:46
		if show_timestamp:
			text = hxsublime_panel_Tools.timestampMsg(text)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:51
		win.run_command("show_panel",python_Lib.anonToDict(_hx_AnonObject({'panel': "output.haxe"})))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:54
		def _hx_local_0(v,edit):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:55
			region = sublime_Region(v.size(), (v.size() + len(text)))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:56
			v.insert(edit,v.size(),text)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:59
			if (scope is not None):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:61
				icon = "dot"
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:62
				key = ("haxe-" + ("null" if scope is None else scope))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:63
				regions = v.get_regions(key)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:64
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:64
				regions.append(region)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:65
				v.add_regions(key,regions,scope,icon)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:70
			v.sel().clear()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:71
			v.sel().add(sublime_Region(0, 0))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:53
		do_edit = _hx_local_0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:77
		hxsublime_tools_ViewTools.asyncEdit(panel,do_edit)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:79
		return panel

	def writeln(self,msg,scope = None,show_timestamp = True):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:84
		if (show_timestamp is None):
			show_timestamp = True
		if hxsublime_panel_Tools.isValidMessage(msg):
			self.write((("null" if msg is None else msg) + "\n"),scope,show_timestamp)

	def status(self,title,msg):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/SlidePanel.hx:92
		if hxsublime_panel_Tools.isValidMessage(msg):
			self.writeln(((("null" if title is None else title) + ": ") + ("null" if msg is None else msg)))

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.win = None
		_hx_o.outputView = None
		_hx_o.outputViewId = None
hxsublime_panel_SlidePanel._hx_class = hxsublime_panel_SlidePanel
_hx_classes["hxsublime.panel.SlidePanel"] = hxsublime_panel_SlidePanel


class hxsublime_panel_Tools:
	_hx_class_name = "hxsublime.panel.Tools"
	_hx_statics = ["haxeFileRegex", "timestampMsg", "isValidMessage"]

	@staticmethod
	def haxeFileRegex():
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/Tools.hx:8
		return ("^[0-9]{2}:[0-9]{2}:[0-9]{2}[ ]Error:[ ]" + HxOverrides.stringOrNull(HxString.substr(hxsublime_project_Tools.haxeFileRegex,1,None)))

	@staticmethod
	def timestampMsg(msg):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/Tools.hx:13
		return ((HxOverrides.stringOrNull(python_lib_datetime_Datetime.now().strftime("%H:%M:%S")) + " ") + ("null" if msg is None else msg))

	@staticmethod
	def isValidMessage(msg):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/panel/Tools.hx:18
		return (((msg is not None) and ((msg != ""))) and ((msg != "\n")))
hxsublime_panel_Tools._hx_class = hxsublime_panel_Tools
_hx_classes["hxsublime.panel.Tools"] = hxsublime_panel_Tools


class hxsublime_project_ProjectCompletionState:
	_hx_class_name = "hxsublime.project.ProjectCompletionState"
	_hx_fields = ["running", "trigger", "currentId", "errors", "async", "current"]
	_hx_methods = ["addCompletionResult", "isEquivalentCompletionAlreadyRunning", "runIfStillUpToDate", "setNewCompletion", "setTrigger", "clearCompletion", "setErrors", "getAndDeleteTrigger", "getAndDeleteAsync", "getAsync", "deleteAsync"]

	def __init__(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:23
		self.running = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:24
		self.trigger = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:25
		self.currentId = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:26
		self.errors = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:27
		self.async = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:28
		self.current = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:32
		self.running = hxsublime_tools_Cache(haxe_ds_IntMap())
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:33
		self.trigger = hxsublime_tools_Cache(haxe_ds_IntMap(), 1000)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:34
		self.currentId = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:35
		self.errors = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:36
		self.async = hxsublime_tools_Cache(haxe_ds_IntMap(), 1000)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:37
		self.current = _hx_AnonObject({'input': None, 'output': None})

	def addCompletionResult(self,compResult):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:45
		self.async.insert(compResult.ctx.view_id,compResult)

	def isEquivalentCompletionAlreadyRunning(self,ctx):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:52
		complete_offset = ctx.complete_offset
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:53
		view_id = ctx.view_id
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:55
		last_completion_id = self.currentId
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:56
		running_completion = self.running.getOrDefault(last_completion_id,None)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:57
		return (((running_completion is not None) and ((running_completion[0] == complete_offset()))) and ((running_completion[1] == view_id)))

	def runIfStillUpToDate(self,comp_id,run):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:62
		self.running.delete(comp_id)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:63
		if (self.currentId == comp_id):
			run()

	def setNewCompletion(self,ctx):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:71
		def _hx_local_0():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:71
			a = ctx.complete_offset()
			return (a, ctx.view_id)
		self.running.insert(ctx.id,_hx_local_0())
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:72
		self.currentId = ctx.id
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:74
		self.setErrors([])

	def setTrigger(self,view,options):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:79
		haxe_Log.trace("SET TRIGGER",_hx_AnonObject({'fileName': "CompletionState.hx", 'lineNumber': 79, 'className': "hxsublime.project.ProjectCompletionState", 'methodName': "setTrigger"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:80
		self.trigger.insert(view.id(),options)

	def clearCompletion(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:85
		self.current = _hx_AnonObject({'input': None, 'output': None})

	def setErrors(self,errors):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:93
		self.errors = errors

	def getAndDeleteTrigger(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:98
		return self.trigger.getAndDelete(view.id(),None)

	def getAndDeleteAsync(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:103
		return self.async.getAndDelete(view.id(),None)

	def getAsync(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:108
		return self.async.getOrDefault(view.id(),None)

	def deleteAsync(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/CompletionState.hx:113
		self.async.delete(view.id())
		return

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.running = None
		_hx_o.trigger = None
		_hx_o.currentId = None
		_hx_o.errors = None
		_hx_o.async = None
		_hx_o.current = None
hxsublime_project_ProjectCompletionState._hx_class = hxsublime_project_ProjectCompletionState
_hx_classes["hxsublime.project.ProjectCompletionState"] = hxsublime_project_ProjectCompletionState

class hxsublime_project_BuildType(Enum):
	_hx_class_name = "hxsublime.project.BuildType"
	_hx_constructs = ["Run", "Build", "Check"]
hxsublime_project_BuildType.Run = hxsublime_project_BuildType("Run", 0, list())
hxsublime_project_BuildType.Build = hxsublime_project_BuildType("Build", 1, list())
hxsublime_project_BuildType.Check = hxsublime_project_BuildType("Check", 2, list())
hxsublime_project_BuildType._hx_class = hxsublime_project_BuildType
_hx_classes["hxsublime.project.BuildType"] = hxsublime_project_BuildType


class hxsublime_project_Project:
	_hx_class_name = "hxsublime.project.Project"
	_hx_fields = ["_haxelibManager", "_currentBuild", "_selectingBuild", "_projectFile", "_projectId", "_projectPath", "_stdBundle", "_stdPaths", "_serverMode", "completionContext", "builds", "winId", "server"]
	_hx_methods = ["haxelibManager", "projectDir", "nmeExec", "openflExec", "haxelibExec", "haxeExec", "haxeEnv", "startServer", "restartServer", "isServerMode", "isServerModeForBuilds", "generateBuild", "selectBuild", "extractBuildArgs", "hasBuild", "checkBuild", "justBuild", "runBuild", "updateCompilerInfo", "findBuildsInFolders", "getViewFileName", "getCurrentWindow", "getFolders", "createNewHxml", "showBuildSelectionPanel", "setCurrentBuild", "build", "clearBuild", "destroy", "createDefaultBuild", "getOriginalBuild", "getBuild"]
	_hx_statics = ["haxeBuildEnv", "getCompilerInfoEnv", "collectCompilerInfo", "extractHaxeVersion", "removeTrailingPathSep", "isValidClasspath", "parseStdClasspaths", "collectStdClassesAndPacks", "classpathLineRegex", "haxeVersionRegex"]

	def __init__(self,id,file,win_id,server_port):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:39
		self._haxelibManager = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:40
		self._currentBuild = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:41
		self._selectingBuild = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:42
		self._projectFile = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:43
		self._projectId = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:44
		self._projectPath = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:45
		self._stdBundle = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:46
		self._stdPaths = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:47
		self._serverMode = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:49
		self.completionContext = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:50
		self.builds = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:51
		self.winId = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:52
		self.server = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:56
		self.completionContext = hxsublime_project_ProjectCompletionState()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:57
		self._haxelibManager = hxsublime_HaxeLibManager(self)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:58
		self._currentBuild = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:59
		self._selectingBuild = False
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:60
		self.builds = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:61
		self.winId = win_id
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:62
		self.server = hxsublime_compiler_Server(server_port)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:63
		self._projectFile = file
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:64
		self._projectId = id
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:65
		if (self._projectFile is not None):
			self._projectPath = python_lib_os_Path.normpath(python_lib_os_Path.dirname(self._projectFile))
		else:
			self._projectPath = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:71
		self.updateCompilerInfo()

	def haxelibManager(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:77
		return self._haxelibManager

	def projectDir(self,defaultVal):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:82
		if (self._projectPath is not None):
			return self._projectPath
		else:
			return defaultVal

	def nmeExec(self,view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:88
		return [hxsublime_Settings.haxelibExec(), "run", "nme"]

	def openflExec(self,view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:93
		return [hxsublime_Settings.haxelibExec(), "run", "openfl"]

	def haxelibExec(self,view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:98
		return [hxsublime_Settings.haxelibExec()]

	def haxeExec(self,view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:103
		_hx_exec = hxsublime_Settings.haxeExec(view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:104
		if ((not python_lib_os_Path.isabs(_hx_exec)) and ((_hx_exec != "haxe"))):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:105
			cwd = self.projectDir(".")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:106
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:106
				_this = None
				_this1 = python_lib_os_Path.join(cwd,hxsublime_Settings.haxeExec(view))
				_this = _this1.split("/")
				return python_lib_Os.sep.join([python_Boot.toString1(x1,'') for x1 in _this])
			_hx_exec = python_lib_os_Path.normpath(_hx_local_0())
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:108
		return [_hx_exec]

	def haxeEnv(self,view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:114
		return hxsublime_project_Project.haxeBuildEnv(self.projectDir("."))

	def startServer(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:120
		cwd = self.projectDir(".")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:121
		haxe_exec = python_internal_ArrayImpl._get(self.haxeExec(view), 0)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:123
		env = self.haxeEnv()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:125
		self.server.start(haxe_exec,cwd,env)

	def restartServer(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:131
		def _hx_local_0():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:131
			f = self.startServer
			a1 = view
			def _hx_local_1():
				f(a1)
			return _hx_local_1
		self.server.stop(_hx_local_0())

	def isServerMode(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:136
		return (self._serverMode and hxsublime_Settings.useHaxeServermode())

	def isServerModeForBuilds(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:141
		return (self.isServerMode() and hxsublime_Settings.useHaxeServermodeForBuilds())

	def generateBuild(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:144
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:146
		fn = view.file_name()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:148
		def _hx_local_0():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:148
			return Std._hx_is(_g._currentBuild,hxsublime_build_HxmlBuild)
		is_hxml_build = _hx_local_0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:150
		if ((((self._currentBuild is not None) and is_hxml_build()) and ((fn == self._currentBuild.buildFile()))) and ((view.size() == 0))):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:151
			def _hx_local_1(v,e):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:152
				hxml_src = _g._currentBuild.makeHxml()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:153
				v.insert(e,0,hxml_src)
			run_edit = _hx_local_1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:156
			hxsublime_tools_ViewTools.asyncEdit(view,run_edit)

	def selectBuild(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:162
		scopes = None
		_this = view.scope_name(view.sel()[0].end())
		scopes = _this.split(" ")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:164
		if Lambda.has(scopes,"source.hxml"):
			view.run_command("save")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:168
		self.extractBuildArgs(view,True)

	def extractBuildArgs(self,view = None,force_panel = False):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:172
		if (force_panel is None):
			force_panel = False
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:173
		if (view is None):
			view = sublime_Sublime.active_window().active_view()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:177
		folders = self.getFolders(view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:179
		self.builds = self.findBuildsInFolders(folders)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:182
		num_builds = len(self.builds)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:184
		view_build_id = view.settings().get("haxe-current-build-id")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:187
		if (((view_build_id is not None) and ((view_build_id < num_builds))) and (not force_panel)):
			self.setCurrentBuild(view,view_build_id)
		elif (num_builds == 1):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:193
			if force_panel:
				sublime_Sublime.status_message("There is only one build")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:197
			self.setCurrentBuild(view,0)
		elif ((num_builds == 0) and force_panel):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:201
			sublime_Sublime.status_message("No build files found (e.g. hxml, nmml, xml)")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:202
			self.createNewHxml(view,(folders[0] if 0 < len(folders) else None))
		elif ((num_builds > 1) and force_panel):
			self.showBuildSelectionPanel(view)
		else:
			self.setCurrentBuild(view,0)

	def hasBuild(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:216
		return (self._currentBuild is not None)

	def checkBuild(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:221
		self.build(view,hxsublime_project_BuildType.Check)

	def justBuild(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:226
		self.build(view,hxsublime_project_BuildType.Build)

	def runBuild(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:231
		self.build(view,hxsublime_project_BuildType.Run)

	def updateCompilerInfo(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:236
		info = hxsublime_project_Project.collectCompilerInfo(self.haxeExec(),self._projectPath)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:238
		bundle = info[0]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:239
		ver = info[1]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:240
		std_paths = info[2]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:243
		self._serverMode = ((ver is None) or ((ver >= 209)))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:245
		self._stdBundle = bundle
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:246
		self._stdPaths = std_paths

	def findBuildsInFolders(self,folders):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:254
		builds = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:255
		haxe_Log.trace("find builds start",_hx_AnonObject({'fileName': "Project.hx", 'lineNumber': 255, 'className': "hxsublime.project.Project", 'methodName': "findBuildsInFolders"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:256
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:256
		_g = 0
		while (_g < len(folders)):
			f = (folders[_g] if _g >= 0 and _g < len(folders) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:258
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:258
			x = None
			_this = hxsublime_build_Tools.findHxmlProjects(self,f)
			def _hx_local_1(x1):
				return x1
			x = list(map(_hx_local_1,_this))
			builds.extend(x)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:259
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:259
			x2 = None
			_this1 = hxsublime_build_Tools.findNmeProjects(self,f)
			def _hx_local_2(x3):
				return x3
			x2 = list(map(_hx_local_2,_this1))
			builds.extend(x2)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:260
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:260
			x4 = None
			_this2 = hxsublime_build_Tools.findOpenflProjects(self,f)
			def _hx_local_3(x5):
				return x5
			x4 = list(map(_hx_local_3,_this2))
			builds.extend(x4)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:263
		haxe_Log.trace("find builds end",_hx_AnonObject({'fileName': "Project.hx", 'lineNumber': 263, 'className': "hxsublime.project.Project", 'methodName': "findBuildsInFolders"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:264
		return builds

	def getViewFileName(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:269
		if (view is None):
			view = sublime_Sublime.active_window().active_view()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:273
		return view.file_name()

	def getCurrentWindow(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:278
		return hxsublime_project_Tools.getWindow(view)

	def getFolders(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:283
		win = self.getCurrentWindow(view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:284
		folders = win.folders()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:285
		return folders

	def createNewHxml(self,view,folder):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:290
		win = sublime_Sublime.active_window()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:291
		f = python_lib_os_Path.join(folder,"build.hxml")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:293
		self._currentBuild = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:294
		self.getBuild(view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:295
		self._currentBuild.setHxml(f)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:298
		win.open_file(f,sublime_Sublime.TRANSIENT)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:300
		self.setCurrentBuild(view,0)

	def showBuildSelectionPanel(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:303
		_g1 = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:306
		buildsView = None
		_g = []
		_g11 = 0
		_g2 = self.builds
		while (_g11 < len(_g2)):
			b = (_g2[_g11] if _g11 >= 0 and _g11 < len(_g2) else None)
			_g11 = (_g11 + 1)
			x = [b.toString(), python_lib_os_Path.basename(b.buildFile())]
			_g.append(x)
		buildsView = _g
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:309
		self._selectingBuild = True
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:310
		sublime_Sublime.status_message("Please select your build")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:312
		def _hx_local_1(i):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:313
			_g1._selectingBuild = False
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:314
			_g1.setCurrentBuild(view,i)
		onSelected = _hx_local_1
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:317
		win = sublime_Sublime.active_window()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:319
		win.show_quick_panel(buildsView,onSelected,sublime_Sublime.MONOSPACE_FONT)

	def setCurrentBuild(self,view,id):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:325
		haxe_Log.trace("setCurrentBuild",_hx_AnonObject({'fileName': "Project.hx", 'lineNumber': 325, 'className': "hxsublime.project.Project", 'methodName': "setCurrentBuild"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:327
		if ((id < 0) or ((id >= len(self.builds)))):
			id = 0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:331
		if (len(self.builds) > 0):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:332
			view.settings().set("haxe-current-build-id",id)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:333
			self._currentBuild = (self.builds[id] if id >= 0 and id < len(self.builds) else None)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:334
			self._currentBuild.setStdBundle(self._stdBundle)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:336
			view.set_status("haxe-build",self._currentBuild.toString())
		else:
			view.set_status("haxe-build","No build found/selected")

	def build(self,view,_hx_type):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:349
		if (view is None):
			view = sublime_Sublime.active_window().active_view()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:353
		win = view.window()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:355
		env = hxsublime_project_Project.haxeBuildEnv(self.projectDir("."))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:357
		build = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:358
		if self.hasBuild():
			build = self.getOriginalBuild(view)
		else:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:362
			self.extractBuildArgs(view)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:363
			build = self.getOriginalBuild(view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:366
		r = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:370
		if ((_hx_type.index) == 0):
			r = build.prepareRunCmd(self,self.isServerModeForBuilds(),view)
		elif ((_hx_type.index) == 1):
			r = build.prepareBuildCmd(self,self.isServerModeForBuilds(),view)
		elif ((_hx_type.index) == 2):
			r = build.prepareCheckCmd(self,self.isServerMode(),view)
		else:
			pass
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:378
		cmd = r.cmd
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:379
		build_folder = r.folder
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:382
		escaped_cmd = build.escapeCmd(cmd)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:385
		hxsublime_panel_Panels.defaultPanel().writeln(("running: " + HxOverrides.stringOrNull(" ".join([python_Boot.toString1(x1,'') for x1 in escaped_cmd]))))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:389
		win.run_command("hxsublime_commands__haxe_exec",python_Lib.anonToDict(_hx_AnonObject({'cmd': cmd, 'is_check_run': (_hx_type == hxsublime_project_BuildType.Check), 'working_dir': build_folder, 'file_regex': hxsublime_project_Tools.haxeFileRegex, 'env': env})))

	def clearBuild(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:401
		self._currentBuild = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:402
		self.completionContext.clearCompletion()

	def destroy(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:407
		self.server.stop()

	def createDefaultBuild(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:414
		fn = view.file_name()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:416
		src_dir = python_lib_os_Path.dirname(fn)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:418
		src = view.substr(sublime_Region(0, view.size()))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:420
		build = hxsublime_build_HxmlBuild(None, None)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:421
		build._target = "js"
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:423
		folder = python_lib_os_Path.dirname(fn)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:424
		folders = view.window().folders()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:425
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:425
		_g = 0
		while (_g < len(folders)):
			f = (folders[_g] if _g >= 0 and _g < len(folders) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:426
			if (fn.find(f) > -1):
				folder = f
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:431
		pack = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:432
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:432
		_g1 = 0
		_g11 = python_lib__Re_RegexHelper.findallDynamic(hxsublime_tools_Regex.package_line,src,None,None)
		while (_g1 < len(_g11)):
			ps = (_g11[_g1] if _g1 >= 0 and _g1 < len(_g11) else None)
			_g1 = (_g1 + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:434
			if (ps == ""):
				continue
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:436
			pack = ps.split(".")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:437
			packrev = list(pack)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:438
			packrev.reverse()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:439
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:439
			_g2 = 0
			while (_g2 < len(packrev)):
				p = (packrev[_g2] if _g2 >= 0 and _g2 < len(packrev) else None)
				_g2 = (_g2 + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:440
				spl = python_lib_os_Path.split(src_dir)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:441
				if (spl[1] == p):
					src_dir = spl[0]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:447
		cl = python_lib_os_Path.basename(fn)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:449
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:449
		endIndex = cl.rfind(".", 0, len(cl))
		cl = HxString.substring(cl,0,endIndex)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:451
		main = list(pack)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:452
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:452
		main.append(cl)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:453
		build.main = ".".join([python_Boot.toString1(x1,'') for x1 in main])
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:455
		build.output = python_lib_os_Path.join(folder,(HxOverrides.stringOrNull(build.main.lower()) + ".js"))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:457
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:457
		arg = ("-cp", src_dir)
		_this = build._args
		_this.append(arg)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:459
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:459
		arg1 = ("-js", build.output)
		_this1 = build._args
		_this1.append(arg1)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:461
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:461
		hxml = python_lib_os_Path.join(src_dir,"build.hxml")
		build._hxml = hxml
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:462
		return build

	def getOriginalBuild(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:467
		if ((self._currentBuild is None) and ((view.score_selector(0,"source.haxe.2") > 0))):
			self._currentBuild = self.createDefaultBuild(view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:472
		return self._currentBuild

	def getBuild(self,view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:478
		return self.getOriginalBuild(view).copy()

	@staticmethod
	def haxeBuildEnv(project_dir):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:487
		lib_path = hxsublime_Settings.haxeLibraryPath()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:488
		haxe_inst_path = hxsublime_Settings.haxeInstPath()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:489
		neko_inst_path = hxsublime_Settings.nekoInstPath()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:492
		env = python_lib_Os.environ.copy()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:494
		env_path = python_lib_Os.environ.copy().get("PATH","")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:496
		paths = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:499
		path = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:501
		if (lib_path is not None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:504
			if hxsublime_tools_PathTools.isAbsPath(lib_path):
				path = lib_path
			else:
				path = python_lib_os_Path.normpath(python_lib_os_Path.join(project_dir,lib_path))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:510
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:510
			val = None
			_this = path.split("/")
			val = python_lib_Os.sep.join([python_Boot.toString1(x1,'') for x1 in _this])
			env["HAXE_LIBRARY_PATH"] = val
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:511
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:511
			val1 = None
			_this1 = path.split("/")
			val1 = python_lib_Os.sep.join([python_Boot.toString1(x1,'') for x1 in _this1])
			env["HAXE_STD_PATH"] = val1
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:515
		if (haxe_inst_path is not None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:516
			if hxsublime_tools_PathTools.isAbsPath(haxe_inst_path):
				path = haxe_inst_path
			else:
				path = python_lib_os_Path.normpath(python_lib_os_Path.join(project_dir,haxe_inst_path))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:522
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:522
			val2 = None
			_this2 = path.split("/")
			val2 = python_lib_Os.sep.join([python_Boot.toString1(x1,'') for x1 in _this2])
			env["HAXEPATH"] = val2
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:523
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:523
			x = None
			_this3 = path.split("/")
			x = python_lib_Os.sep.join([python_Boot.toString1(x1,'') for x1 in _this3])
			paths.append(x)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:526
		if (neko_inst_path is not None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:528
			path = python_lib_os_Path.normpath(python_lib_os_Path.join(project_dir,neko_inst_path))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:529
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:529
			val3 = None
			_this4 = path.split("/")
			val3 = python_lib_Os.sep.join([python_Boot.toString1(x1,'') for x1 in _this4])
			env["NEKO_INSTPATH"] = val3
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:530
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:530
			x1 = None
			_this5 = path.split("/")
			x1 = python_lib_Os.sep.join([python_Boot.toString1(x1,'') for x1 in _this5])
			paths.append(x1)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:534
		if (len(paths) > 0):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:536
			val4 = ((HxOverrides.stringOrNull(python_lib_Os.pathsep.join([python_Boot.toString1(x1,'') for x1 in paths])) + HxOverrides.stringOrNull(python_lib_Os.pathsep)) + ("null" if env_path is None else env_path))
			env["PATH"] = val4
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:539
		return env

	@staticmethod
	def getCompilerInfoEnv(project_path):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:545
		return hxsublime_project_Project.haxeBuildEnv(project_path)

	@staticmethod
	def collectCompilerInfo(haxeExec,project_path):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:551
		env = hxsublime_project_Project.getCompilerInfoEnv(project_path)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:552
		cmd = list(haxeExec)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:554
		cmd.extend(["-main", "Nothing", "-v", "--no-output"])
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:557
		r = hxsublime_Execute.runCmd(cmd,None,None,env)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:559
		out = r[0]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:560
		err = r[1]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:563
		stdClasspaths = hxsublime_project_Project.parseStdClasspaths(out)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:565
		bundle = hxsublime_project_Project.collectStdClassesAndPacks(stdClasspaths)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:567
		ver = hxsublime_project_Project.extractHaxeVersion(out)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:569
		return (bundle, ver, stdClasspaths)

	@staticmethod
	def extractHaxeVersion(out):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:574
		ver = python_lib_Re.search(hxsublime_project_Project.haxeVersionRegex,out)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:575
		if (ver is not None):
			return Std.parseInt(ver.group(1))
		else:
			return None

	@staticmethod
	def removeTrailingPathSep(path):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:581
		if (len(path) > 1):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:583
			last_pos = (len(path) - 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:584
			last_char = None
			if ((last_pos < 0) or ((last_pos >= len(path)))):
				last_char = ""
			else:
				last_char = path[last_pos]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:585
			if (((last_char == "/") or ((last_char == "\\"))) or ((last_char == python_lib_os_Path.sep))):
				path = HxString.substring(path,0,last_pos)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:590
		return path

	@staticmethod
	def isValidClasspath(path):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:595
		return (((len(path) > 1) and python_lib_os_Path.exists(path)) and python_lib_os_Path.isdir(path))

	@staticmethod
	def parseStdClasspaths(out):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:600
		m = hxsublime_project_Project.classpathLineRegex.match(out)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:602
		stdClasspaths = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:604
		all_paths = None
		_this = m.group(1)
		all_paths = _this.split(";")
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:605
		ignored_paths = [".", "./"]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:607
		std_paths = None
		if (m is not None):
			std_paths = set(all_paths).difference(set(ignored_paths))
		else:
			std_paths = set()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:609
		def _hx_local_0():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:609
			this1 = iter(std_paths)
			return python_HaxeIterator(this1)
		_hx_local_1 = _hx_local_0()
		while _hx_local_1.hasNext():
			p = _hx_local_1.next()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:611
			p1 = python_lib_os_Path.normpath(p)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:613
			p1 = hxsublime_project_Project.removeTrailingPathSep(p1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:615
			if hxsublime_project_Project.isValidClasspath(p1):
				stdClasspaths.append(p1)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:620
		return stdClasspaths

	@staticmethod
	def collectStdClassesAndPacks(stdCps):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:625
		bundle = hxsublime_tools_HxSrcTools.emptyTypeBundle()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:626
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:626
		_g = 0
		while (_g < len(stdCps)):
			p = (stdCps[_g] if _g >= 0 and _g < len(stdCps) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:628
			bundle1 = hxsublime_Types.extractTypes(p,[],[],0,[],False)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:629
			bundle = bundle.merge(bundle1)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Project.hx:631
		return bundle

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o._haxelibManager = None
		_hx_o._currentBuild = None
		_hx_o._selectingBuild = None
		_hx_o._projectFile = None
		_hx_o._projectId = None
		_hx_o._projectPath = None
		_hx_o._stdBundle = None
		_hx_o._stdPaths = None
		_hx_o._serverMode = None
		_hx_o.completionContext = None
		_hx_o.builds = None
		_hx_o.winId = None
		_hx_o.server = None
hxsublime_project_Project._hx_class = hxsublime_project_Project
_hx_classes["hxsublime.project.Project"] = hxsublime_project_Project


class hxsublime_project_Projects:
	_hx_class_name = "hxsublime.project.Projects"
	_hx_methods = ["fileLog"]
	_hx_statics = ["projects", "userHome", "logFile", "nextServerPort", "cleanupProjects", "getProjectId", "getWindow", "currentProject", "createProject"]

	def fileLog(self,msg):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:28
		f = None
		def _hx_local_0():
			_hx_local_0 = python_lib_Builtins.open(hxsublime_project_Projects.logFile,"a+")
			if Std._hx_is(_hx_local_0,python_lib_io_TextIOBase):
				_hx_local_0
			else:
				raise _HxException("Class cast error")
			return _hx_local_0
		f = _hx_local_0()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:29
		f.write((Std.string(msg) + "\n"))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:30
		f.close()

	@staticmethod
	def cleanupProjects():
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:37
		win_ids = None
		_g = []
		_g1 = 0
		_g2 = sublime_Sublime.windows()
		while (_g1 < len(_g2)):
			w = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
			_g1 = (_g1 + 1)
			x = w.id()
			_g.append(x)
		win_ids = _g
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:38
		remove = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:39
		_hx_local_1 = hxsublime_project_Projects.projects.data.keys()
		while _hx_local_1.hasNext():
			p = _hx_local_1.next()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:40
			proj = hxsublime_project_Projects.projects.getOrDefault(p,None)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:41
			if ((proj is not None) and (not Lambda.has(win_ids,proj.winId))):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:42
				remove.append(p)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:46
		haxe_Log.trace(remove,_hx_AnonObject({'fileName': "Projects.hx", 'lineNumber': 46, 'className': "hxsublime.project.Projects", 'methodName': "cleanupProjects"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:47
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:47
		_g11 = 0
		while (_g11 < len(remove)):
			pid = (remove[_g11] if _g11 >= 0 and _g11 < len(remove) else None)
			_g11 = (_g11 + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:48
			haxe_Log.trace(pid,_hx_AnonObject({'fileName': "Projects.hx", 'lineNumber': 48, 'className': "hxsublime.project.Projects", 'methodName': "cleanupProjects"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:49
			project = hxsublime_project_Projects.projects.data.get(pid).val
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:50
			project.destroy()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:51
			haxe_Log.trace("delete project from memory",_hx_AnonObject({'fileName': "Projects.hx", 'lineNumber': 51, 'className': "hxsublime.project.Projects", 'methodName': "cleanupProjects"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:52
			hxsublime_project_Projects.projects.data.remove(pid)

	@staticmethod
	def getProjectId(file,win):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:59
		id = None
		if (file is None):
			id = ("global" + Std.string(win.id()))
		else:
			id = file
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:60
		return id

	@staticmethod
	def getWindow(view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:65
		win = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:66
		if (view is not None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:67
			win = view.window()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:68
			if (win is not None):
				win = sublime_Sublime.active_window()
		else:
			win = sublime_Sublime.active_window()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:74
		return win

	@staticmethod
	def currentProject(view = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:79
		hxsublime_project_Projects.cleanupProjects()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:81
		file = hxsublime_tools_SublimeTools.getProjectFile()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:83
		win = hxsublime_project_Projects.getWindow(view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:85
		id = hxsublime_project_Projects.getProjectId(file,win)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:87
		haxe_Log.trace(("project id:" + ("null" if id is None else id)),_hx_AnonObject({'fileName': "Projects.hx", 'lineNumber': 87, 'className': "hxsublime.project.Projects", 'methodName': "currentProject"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:88
		haxe_Log.trace(("win.id:" + Std.string(win.id())),_hx_AnonObject({'fileName': "Projects.hx", 'lineNumber': 88, 'className': "hxsublime.project.Projects", 'methodName': "currentProject"}))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:90
		def _hx_local_0():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:90
			id1 = id
			a1 = file
			a2 = win
			def _hx_local_1():
				return hxsublime_project_Projects.createProject(id1,a1,a2)
			return _hx_local_1
		res = hxsublime_project_Projects.projects.getOrInsert(id,_hx_local_0())
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:92
		return res

	@staticmethod
	def createProject(id,file,win):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:97
		p = hxsublime_project_Project(id, file, win.id(), hxsublime_project_Projects.nextServerPort)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:98
		hxsublime_project_Projects.nextServerPort = (hxsublime_project_Projects.nextServerPort + 20)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Projects.hx:99
		return p

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_project_Projects._hx_class = hxsublime_project_Projects
_hx_classes["hxsublime.project.Projects"] = hxsublime_project_Projects


class hxsublime_project_Tools:
	_hx_class_name = "hxsublime.project.Tools"
	_hx_statics = ["getWindow", "winStart", "unixStart", "haxeFileRegex"]

	@staticmethod
	def getWindow(view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Tools.hx:9
		win = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Tools.hx:10
		if (view is not None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Tools.hx:12
			win = view.window()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Tools.hx:13
			if (win is None):
				win = sublime_Sublime.active_window()
		else:
			win = sublime_Sublime.active_window()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/project/Tools.hx:21
		return win
hxsublime_project_Tools._hx_class = hxsublime_project_Tools
_hx_classes["hxsublime.project.Tools"] = hxsublime_project_Tools


class hxsublime_support_ArrayTools:
	_hx_class_name = "hxsublime.support.ArrayTools"
	_hx_statics = ["extend", "append", "contains"]

	@staticmethod
	def extend(a,x):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/support/ArrayTools.hx:6
		a.extend(x)

	@staticmethod
	def append(a,x):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/support/ArrayTools.hx:10
		a.append(x)

	@staticmethod
	def contains(a,x):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/support/ArrayTools.hx:15
		return x in a
hxsublime_support_ArrayTools._hx_class = hxsublime_support_ArrayTools
_hx_classes["hxsublime.support.ArrayTools"] = hxsublime_support_ArrayTools


class hxsublime_support_Macros:
	_hx_class_name = "hxsublime.support.Macros"
hxsublime_support_Macros._hx_class = hxsublime_support_Macros
_hx_classes["hxsublime.support.Macros"] = hxsublime_support_Macros


class hxsublime_support_NativeIterableTools:
	_hx_class_name = "hxsublime.support.NativeIterableTools"
	_hx_statics = ["getRaw", "getNativeIterator"]

	@staticmethod
	def getRaw(i):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/support/NativeIterableTools.hx:9
		return i

	@staticmethod
	def getNativeIterator(i):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/support/NativeIterableTools.hx:13
		return i.__iter__()
hxsublime_support_NativeIterableTools._hx_class = hxsublime_support_NativeIterableTools
_hx_classes["hxsublime.support.NativeIterableTools"] = hxsublime_support_NativeIterableTools


class hxsublime_support_NativeIteratorTools:
	_hx_class_name = "hxsublime.support.NativeIteratorTools"
	_hx_statics = ["getRaw"]

	@staticmethod
	def getRaw(i):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/support/NativeIteratorTools.hx:8
		return i
hxsublime_support_NativeIteratorTools._hx_class = hxsublime_support_NativeIteratorTools
_hx_classes["hxsublime.support.NativeIteratorTools"] = hxsublime_support_NativeIteratorTools


class hxsublime_support_StringTools:
	_hx_class_name = "hxsublime.support.StringTools"
	_hx_statics = ["format", "encode", "contains", "strip", "rpartition"]

	@staticmethod
	def format(s,args):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/support/StringTools.hx:10
		return s.format(*args)

	@staticmethod
	def encode(s,encoding = "utf-8",errors = "strict"):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/support/StringTools.hx:14
		if (encoding is None):
			encoding = "utf-8"
		if (errors is None):
			errors = "strict"
		return s.encode(encoding, errors)

	@staticmethod
	def contains(s,e):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/support/StringTools.hx:18
		return e in s

	@staticmethod
	def strip(s,chars = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/support/StringTools.hx:23
		return s.strip(chars)

	@staticmethod
	def rpartition(s,sep):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/support/StringTools.hx:28
		return s.rpartition(sep)
hxsublime_support_StringTools._hx_class = hxsublime_support_StringTools
_hx_classes["hxsublime.support.StringTools"] = hxsublime_support_StringTools


class hxsublime_tools_Regex:
	_hx_class_name = "hxsublime.tools.Regex"
	_hx_statics = ["space_chars", "word_chars", "import_line", "using_line", "package_line", "variables", "named_functions", "function_params", "param_default", "isType", "typeDeclWithScope", "comments", "fieldRegex", "typeDeclWithScopeRegex", "enumConstructorStartDecl"]
hxsublime_tools_Regex._hx_class = hxsublime_tools_Regex
_hx_classes["hxsublime.tools.Regex"] = hxsublime_tools_Regex


class hxsublime_tools_HxSrcTools:
	_hx_class_name = "hxsublime.tools.HxSrcTools"
	_hx_statics = ["getTypesFromSrc", "extractEnumConstructorsFromSrc", "extractEnumConstructorsFromEnum", "skipWhitespaceOrComments", "isSameNestingLevelAtPos", "searchNextCharOnSameNestingLevel", "reverse_search_next_char_on_same_nesting_level", "stripComments", "getPackage", "splitFunctionSignature", "emptyTypeBundle"]

	@staticmethod
	def getTypesFromSrc(src,moduleName,file,src_with_comments):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:44
		if (moduleName is None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:46
			_this = python_lib_os_Path.splitext(python_lib_os_Path.basename(file))
			moduleName = _this[0]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:49
		pack = hxsublime_tools_HxSrcTools.getPackage(src)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:51
		res = haxe_ds_StringMap()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:52
		def _hx_local_0():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:52
			this1 = hxsublime_tools_Regex.typeDeclWithScopeRegex.finditer(src)
			return python_HaxeIterator(this1)
		_hx_local_2 = _hx_local_0()
		while _hx_local_2.hasNext():
			decl = _hx_local_2.next()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:55
			isPrivate = (decl.group(1) is not None)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:57
			type_name = decl.group(4)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:59
			if (type_name == "NME_"):
				haxe_Log.trace(Std.string(decl.group(0)),_hx_AnonObject({'fileName': "HxSrcTools.hx", 'lineNumber': 60, 'className': "hxsublime.tools.HxSrcTools", 'methodName': "getTypesFromSrc"}))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:63
			kind = decl.group(3)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:65
			isExtern = (decl.group(2) is not None)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:67
			isModuleType = (type_name == moduleName)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:68
			isStdType = (moduleName == "StdTypes")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:71
			fullType = hxsublime_tools_HaxeType(pack, moduleName, type_name, kind, isPrivate, isModuleType, isStdType, isExtern, file, src, src_with_comments, decl)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:74
			if (fullType.kind == "enum"):
				fullType._enumConstructors = hxsublime_tools_HxSrcTools.extractEnumConstructorsFromSrc(src,decl.end(4))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:78
			def _hx_local_1():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:78
				key = fullType.fullQualifiedName()
				return key in res.h
			if (not _hx_local_1()):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:80
				key1 = fullType.fullQualifiedName()
				res.h[key1] = fullType
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:83
		return hxsublime_tools_HaxeTypeBundle(res)

	@staticmethod
	def extractEnumConstructorsFromSrc(src,start_pos):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:88
		constructors = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:90
		start = hxsublime_tools_HxSrcTools.searchNextCharOnSameNestingLevel(src,["{"],start_pos)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:91
		if (start is not None):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:92
			end = hxsublime_tools_HxSrcTools.searchNextCharOnSameNestingLevel(src,["}"],(start[0] + 1))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:93
			if (end is not None):
				constructors = hxsublime_tools_HxSrcTools.extractEnumConstructorsFromEnum(HxString.substring(src,(start[0] + 1),(end[0] - 1)))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:97
		return constructors

	@staticmethod
	def extractEnumConstructorsFromEnum(enumStr):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:103
		constructors = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:104
		start = 0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:105
		while True:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:106
			m = hxsublime_tools_Regex.enumConstructorStartDecl.match(enumStr,start)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:107
			if (m is not None):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:108
				constructor = m.group(1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:109
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:109
				constructors.append(constructor)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:110
				end = hxsublime_tools_HxSrcTools.searchNextCharOnSameNestingLevel(enumStr,[";"],m.end(1))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:111
				if (end is not None):
					start = (end[0] + 1)
				else:
					break
			else:
				break
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:122
		return constructors

	@staticmethod
	def skipWhitespaceOrComments(hxSrcSection,start_pos):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:127
		in_single_comment = False
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:128
		in_multi_comment = False
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:130
		count = len(hxSrcSection)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:131
		pos = start_pos
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:133
		while True:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:135
			if (pos > ((count - 1))):
				break
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:137
			c = None
			if ((pos < 0) or ((pos >= len(hxSrcSection)))):
				c = ""
			else:
				c = hxSrcSection[pos]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:138
			next = None
			if (pos < ((count - 1))):
				index = (pos + 1)
				if ((index < 0) or ((index >= len(hxSrcSection)))):
					next = ""
				else:
					next = hxSrcSection[index]
			else:
				next = None
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:140
			if (in_single_comment and ((c == "\n"))):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:142
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:143
				in_single_comment = False
			elif ((in_multi_comment and ((c == "*"))) and ((next == "/"))):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:147
				in_multi_comment = False
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:148
				pos = (pos + 2)
			elif (in_single_comment or in_multi_comment):
				pos = (pos + 1)
			elif ((c == "/") and ((next == "/"))):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:156
				pos = (pos + 2)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:157
				in_single_comment = True
			elif ((c == "/") and ((next == "*"))):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:161
				pos = (pos + 2)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:162
				in_multi_comment = True
			elif (((c == " ") or ((c == "\t"))) or ((c == "\n"))):
				pos = (pos + 1)
			else:
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:170
				b = HxString.substring(hxSrcSection,start_pos,pos)
				return (pos, b)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:173
		return None

	@staticmethod
	def isSameNestingLevelAtPos(hxSrcSection,end_pos,start_pos):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:179
		if (end_pos < start_pos):
			return False
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:183
		open_pars = 0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:184
		open_braces = 0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:185
		open_brackets = 0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:186
		open_angle_brackets = 0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:187
		in_string = False
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:188
		string_char = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:189
		in_regexp = False
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:191
		count = len(hxSrcSection)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:192
		cur = ""
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:193
		pos = start_pos
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:195
		lastPos = (count - 1)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:196
		while True:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:199
			if ((pos == end_pos) or ((pos > lastPos))):
				return ((((((open_pars == 0) and ((open_braces == 0))) and ((open_brackets == 0))) and ((open_angle_brackets == 0))) and (not in_string)) and (not in_regexp))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:204
			c = None
			if ((pos < 0) or ((pos >= len(hxSrcSection)))):
				c = ""
			else:
				c = hxSrcSection[pos]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:205
			ccode = None
			if (0 >= len(c)):
				ccode = -1
			else:
				ccode = ord(c[0])
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:207
			hasNext = (pos < lastPos)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:209
			next = None
			if hasNext:
				index = (pos + 1)
				if ((index < 0) or ((index >= len(hxSrcSection)))):
					next = ""
				else:
					next = hxSrcSection[index]
			else:
				next = None
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:211
			nextCode = None
			if hasNext:
				if (0 >= len(next)):
					nextCode = -1
				else:
					nextCode = ord(next[0])
			else:
				nextCode = None
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:214
			if in_regexp:
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:216
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:217
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:218
				if ((ccode != 92) and ((nextCode == 47))):
					in_regexp = False
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:221
				continue
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:224
			if in_string:
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:227
				if (c == string_char):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:229
					pos = (pos + 1)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:230
					cur = (("null" if cur is None else cur) + ("null" if c is None else c))
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:231
					in_string = False
				elif ((ccode == 92) and ((next == string_char))):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:235
					pos = (pos + 2)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:236
					cur = (("null" if cur is None else cur) + HxOverrides.stringOrNull(((("null" if c is None else c) + ("null" if next is None else next)))))
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:237
					in_string = False
				else:
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:241
					cur = (("null" if cur is None else cur) + ("null" if c is None else c))
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:242
					pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:244
				continue
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:248
			if ((ccode == 126) and ((nextCode == 47))):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:250
				pos = (pos + 2)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:251
				in_regexp = True
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:252
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
			elif ((ccode == 39) or ((ccode == 34))):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:256
				in_string = True
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:257
				string_char = c
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:258
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:259
				pos = (pos + 1)
			elif ((ccode == 45) and ((nextCode == 62))):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:263
				cur = (("null" if cur is None else cur) + "->")
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:264
				pos = (pos + 2)
			elif (ccode == 123):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:268
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:269
				open_braces = (open_braces + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:270
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
			elif (ccode == 125):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:274
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:275
				open_braces = (open_braces - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:276
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
			elif (ccode == 40):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:280
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:281
				open_pars = (open_pars + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:282
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
			elif (ccode == 41):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:286
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:287
				open_pars = (open_pars - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:288
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
			elif (ccode == 91):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:292
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:293
				open_brackets = (open_brackets + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:294
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
			elif (ccode == 93):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:298
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:299
				open_brackets = (open_brackets - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:300
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
			elif (ccode == 60):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:304
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:305
				open_angle_brackets = (open_angle_brackets + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:306
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
			elif (ccode == 62):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:310
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:311
				open_angle_brackets = (open_angle_brackets - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:312
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
			else:
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:316
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:317
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:320
		return False

	@staticmethod
	def searchNextCharOnSameNestingLevel(hxSrcSection,chars,start_pos):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:329
		open_pars = 0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:330
		open_braces = 0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:331
		open_brackets = 0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:332
		open_angle_brackets = 0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:333
		in_string = False
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:334
		string_char = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:335
		in_regexp = False
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:337
		count = len(hxSrcSection)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:338
		cur = ""
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:339
		pos = start_pos
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:340
		while True:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:341
			if (pos > ((count - 1))):
				break
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:344
			c = None
			if ((pos < 0) or ((pos >= len(hxSrcSection)))):
				c = ""
			else:
				c = hxSrcSection[pos]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:347
			next = None
			if (pos < ((count - 1))):
				index = (pos + 1)
				if ((index < 0) or ((index >= len(hxSrcSection)))):
					next = ""
				else:
					next = hxSrcSection[index]
			else:
				next = None
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:349
			if in_regexp:
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:351
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:352
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:353
				if ((c != "\\") and ((next == "/"))):
					in_regexp = False
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:355
				continue
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:358
			if in_string:
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:361
				if (c == string_char):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:363
					pos = (pos + 1)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:364
					cur = (("null" if cur is None else cur) + ("null" if c is None else c))
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:365
					in_string = False
				elif ((c == "\\") and ((next == string_char))):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:369
					pos = (pos + 2)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:370
					cur = (("null" if cur is None else cur) + HxOverrides.stringOrNull(((("null" if c is None else c) + ("null" if next is None else next)))))
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:371
					in_string = False
				else:
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:375
					cur = (("null" if cur is None else cur) + ("null" if c is None else c))
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:376
					pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:378
				continue
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:381
			if (((((open_pars == 0) and ((open_braces == 0))) and ((open_brackets == 0))) and ((open_angle_brackets == 0))) and c in chars):
				return (pos, cur)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:386
			if ((c == "~") and ((next == "/"))):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:388
				pos = (pos + 2)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:389
				in_regexp = True
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:390
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
			elif ((c == "'") or ((c == "\""))):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:394
				in_string = True
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:395
				string_char = c
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:396
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:397
				pos = (pos + 1)
			elif ((c == "-") and ((next == ">"))):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:401
				cur = (("null" if cur is None else cur) + "->")
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:402
				pos = (pos + 2)
			elif (c == "{"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:406
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:407
				open_braces = (open_braces + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:408
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
			elif (c == "}"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:412
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:413
				open_braces = (open_braces - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:414
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
			elif (c == "("):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:418
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:419
				open_pars = (open_pars + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:420
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
			elif (c == ")"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:424
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:425
				open_pars = (open_pars - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:426
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
			elif (c == "["):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:430
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:431
				open_brackets = (open_brackets + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:432
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
			elif (c == "]"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:436
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:437
				open_brackets = (open_brackets - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:438
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
			elif (c == "<"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:442
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:443
				open_angle_brackets = (open_angle_brackets + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:444
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
			elif (c == ">"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:448
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:449
				open_angle_brackets = (open_angle_brackets - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:450
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
			else:
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:454
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:455
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:458
		return None

	@staticmethod
	def reverse_search_next_char_on_same_nesting_level(hxSrcSection,chars,start_pos):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:466
		open_pars = 0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:467
		open_braces = 0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:468
		open_brackets = 0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:469
		open_angle_brackets = 0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:470
		in_string = False
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:471
		string_char = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:474
		cur = ""
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:475
		pos = start_pos
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:476
		while True:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:478
			if (pos <= -1):
				break
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:483
			c = None
			if ((pos < 0) or ((pos >= len(hxSrcSection)))):
				c = ""
			else:
				c = hxSrcSection[pos]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:485
			next = None
			if (pos > 0):
				index = (pos - 1)
				if ((index < 0) or ((index >= len(hxSrcSection)))):
					next = ""
				else:
					next = hxSrcSection[index]
			else:
				next = None
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:487
			if in_string:
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:489
				pos = (pos - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:490
				cur = (("null" if c is None else c) + ("null" if cur is None else cur))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:491
				if ((c == string_char) and ((next != "\\"))):
					in_string = False
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:495
				continue
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:502
			if ((c == "/") and ((next == "/"))):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:504
				pos = (pos - 2)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:505
				cur = ("//" + ("null" if c is None else c))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:506
				continue
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:511
			if (((((open_pars == 0) and ((open_braces == 0))) and ((open_brackets == 0))) and ((open_angle_brackets == 0))) and c in chars):
				return (pos, cur)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:517
			if ((c == "'") or ((c == "\""))):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:519
				in_string = True
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:520
				string_char = c
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:521
				cur = (("null" if c is None else c) + ("null" if cur is None else cur))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:522
				pos = (pos - 1)
			elif ((c == ">") and ((next == "-"))):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:526
				cur = ("->" + ("null" if cur is None else cur))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:527
				pos = (pos - 2)
			elif (c == "}"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:531
				pos = (pos - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:532
				open_braces = (open_braces + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:533
				cur = (("null" if c is None else c) + ("null" if cur is None else cur))
			elif (c == "{"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:537
				pos = (pos - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:538
				open_braces = (open_braces - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:539
				cur = (("null" if c is None else c) + ("null" if cur is None else cur))
			elif (c == ")"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:543
				pos = (pos - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:544
				open_pars = (open_pars + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:545
				cur = (("null" if c is None else c) + ("null" if cur is None else cur))
			elif (c == "("):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:549
				pos = (pos - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:550
				open_pars = (open_pars - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:551
				cur = (("null" if c is None else c) + ("null" if cur is None else cur))
			elif (c == "]"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:555
				pos = (pos - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:556
				open_brackets = (open_brackets + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:557
				cur = (("null" if c is None else c) + ("null" if cur is None else cur))
			elif (c == "["):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:561
				pos = (pos - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:562
				open_brackets = (open_brackets - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:563
				cur = (("null" if c is None else c) + ("null" if cur is None else cur))
			elif (c == ">"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:567
				pos = (pos - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:568
				open_angle_brackets = (open_angle_brackets + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:569
				cur = (("null" if c is None else c) + ("null" if cur is None else cur))
			elif (c == "<"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:573
				pos = (pos - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:574
				open_angle_brackets = (open_angle_brackets - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:575
				cur = (("null" if c is None else c) + ("null" if cur is None else cur))
			else:
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:579
				pos = (pos - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:580
				cur = (("null" if c is None else c) + ("null" if cur is None else cur))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:583
		return None

	@staticmethod
	def stripComments(src):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:589
		return hxsublime_tools_Regex.comments.sub("",src)

	@staticmethod
	def getPackage(src):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:595
		pack = ""
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:596
		all = python_lib__Re_RegexHelper.findallDynamic(hxsublime_tools_Regex.package_line,src,None,None)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:598
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:598
		_g = 0
		while (_g < len(all)):
			ps = (all[_g] if _g >= 0 and _g < len(all) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:599
			pack = ps
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:601
		return pack

	@staticmethod
	def splitFunctionSignature(signature):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:614
		open_pars = 0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:615
		open_braces = 0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:616
		open_brackets = 0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:618
		types = []
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:619
		count = len(signature)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:620
		cur = ""
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:621
		pos = 0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:622
		while True:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:624
			if (pos > ((count - 1))):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:626
				types.append(cur)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:627
				break
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:630
			c = None
			if ((pos < 0) or ((pos >= len(signature)))):
				c = ""
			else:
				c = signature[pos]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:631
			next = None
			if (pos < ((count - 1))):
				index = (pos + 1)
				if ((index < 0) or ((index >= len(signature)))):
					next = ""
				else:
					next = signature[index]
			else:
				next = None
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:633
			if ((c == "-") and ((next == ">"))):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:635
				if (((open_pars == 0) and ((open_braces == 0))) and ((open_brackets == 0))):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:637
					types.append(cur)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:638
					cur = ""
				else:
					cur = (("null" if cur is None else cur) + "->")
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:645
				pos = (pos + 2)
			elif ((((c == " ") and ((open_pars == 0))) and ((open_braces == 0))) and ((open_brackets == 0))):
				pos = (pos + 1)
			elif (c == "{"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:653
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:654
				open_braces = (open_braces + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:655
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
			elif (c == "}"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:659
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:660
				open_braces = (open_braces - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:661
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
			elif (c == "("):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:665
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:666
				open_pars = (open_pars + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:667
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
			elif (c == ")"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:671
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:672
				open_pars = (open_pars - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:673
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
			elif (c == "<"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:677
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:678
				open_brackets = (open_brackets + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:679
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
			elif (c == ">"):
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:683
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:684
				open_brackets = (open_brackets - 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:685
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
			else:
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:689
				pos = (pos + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:690
				cur = (("null" if cur is None else cur) + ("null" if c is None else c))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:693
		return types

	@staticmethod
	def emptyTypeBundle():
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:699
		return hxsublime_tools_HaxeTypeBundle(haxe_ds_StringMap())
hxsublime_tools_HxSrcTools._hx_class = hxsublime_tools_HxSrcTools
_hx_classes["hxsublime.tools.HxSrcTools"] = hxsublime_tools_HxSrcTools


class hxsublime_tools_HaxeModule:
	_hx_class_name = "hxsublime.tools.HaxeModule"
	_hx_fields = ["pack", "name", "file"]

	def __init__(self,pack,name,file):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:706
		self.pack = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:707
		self.name = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:708
		self.file = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:712
		self.pack = pack
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:713
		self.name = name
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:714
		self.file = file

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.pack = None
		_hx_o.name = None
		_hx_o.file = None
hxsublime_tools_HaxeModule._hx_class = hxsublime_tools_HaxeModule
_hx_classes["hxsublime.tools.HaxeModule"] = hxsublime_tools_HaxeModule


class hxsublime_tools_HaxeTypeBundle:
	_hx_class_name = "hxsublime.tools.HaxeTypeBundle"
	_hx_fields = ["_types", "toString_cache", "toString_cache_set", "packs_cache", "packs_cache_set", "allModules_cache", "allModules_cache_set", "allModulesList_cache", "allModulesList_cache_set", "allTypesAndEnumConstructorsWithInfo_cache", "allTypesAndEnumConstructorsWithInfo_cache_set", "allTypesAndEnumConstructors_cache", "allTypesAndEnumConstructors_cache_set", "allTypes_cache", "allTypes_cache_set"]
	_hx_methods = ["toString", "merge", "mergeAll", "packs", "allModules", "allModulesList", "allTypesAndEnumConstructorsWithInfo", "allTypesAndEnumConstructors", "allTypes", "filter"]
	_hx_interfaces = [hxsublime_macros_LazyFunctionSupport]

	def __init__(self,types):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:721
		self._types = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:729
		self.toString_cache = None
		self.toString_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:758
		self.packs_cache = None
		self.packs_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:775
		self.allModules_cache = None
		self.allModules_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:787
		self.allModulesList_cache = None
		self.allModulesList_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:797
		self.allTypesAndEnumConstructorsWithInfo_cache = None
		self.allTypesAndEnumConstructorsWithInfo_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:812
		self.allTypesAndEnumConstructors_cache = None
		self.allTypesAndEnumConstructors_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:820
		self.allTypes_cache = None
		self.allTypes_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:34
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
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:725
		self._types = types

	def toString(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:729
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.toString_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.toString_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:731
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:731
				return (("HaxeTypeBundle(\n" + HxOverrides.stringOrNull(_g._types.toString())) + "\n)")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.toString_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.toString_cache

	def merge(self,other):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:739
		return self.mergeAll([other])

	def mergeAll(self,others):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:744
		res = None
		def _hx_local_0():
			_g = haxe_ds_StringMap()
			_hx_local_1 = self._types.keys()
			while _hx_local_1.hasNext():
				k = _hx_local_1.next()
				value = self._types.h.get(k,None)
				_g.h[k] = value
			return _g
		res = _hx_local_0()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:746
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:746
		_g1 = 0
		while (_g1 < len(others)):
			o = (others[_g1] if _g1 >= 0 and _g1 < len(others) else None)
			_g1 = (_g1 + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:747
			_hx_local_3 = o._types.keys()
			while _hx_local_3.hasNext():
				k1 = _hx_local_3.next()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:748
				value1 = o._types.h.get(k1,None)
				res.h[k1] = value1
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:752
		return hxsublime_tools_HaxeTypeBundle(res)

	def packs(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:758
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.packs_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.packs_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:759
			def _hx_local_3():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:760
				res = haxe_ds_StringMap()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:762
				_hx_local_0 = _g._types.keys()
				while _hx_local_0.hasNext():
					k = _hx_local_0.next()
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:763
					p = _g._types.h.get(k,None).pack
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:764
					if (p != ""):
						res.h[p] = None
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:769
				def _hx_local_2():
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:769
					def _hx_local_1():
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:769
						return res.keys()
					return Lambda.array(_hx_AnonObject({'iterator': _hx_local_1}))
				return _hx_local_2()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_3
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.packs_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.packs_cache

	def allModules(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:775
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.allModules_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.allModules_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:776
			def _hx_local_1():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:777
				res = haxe_ds_StringMap()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:778
				_hx_local_0 = _g._types.keys()
				while _hx_local_0.hasNext():
					k = _hx_local_0.next()
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:779
					t = _g._types.h.get(k,None)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:780
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:780
					key = t.fullPackWithModule()
					value = hxsublime_tools_HaxeModule(t.pack, t.module, t._file)
					res.h[key] = value
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:782
				return res
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.allModules_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.allModules_cache

	def allModulesList(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:787
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.allModulesList_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.allModulesList_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:788
			def _hx_local_1():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:790
				mods = _g.allModules()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:791
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:791
				_g1 = []
				_hx_local_0 = mods.iterator()
				while _hx_local_0.hasNext():
					m = _hx_local_0.next()
					_g1.append(m)
				return _g1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.allModulesList_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.allModulesList_cache

	def allTypesAndEnumConstructorsWithInfo(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:797
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.allTypesAndEnumConstructorsWithInfo_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.allTypesAndEnumConstructorsWithInfo_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:798
			def _hx_local_2():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:799
				res = haxe_ds_StringMap()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:800
				_hx_local_1 = _g._types.keys()
				while _hx_local_1.hasNext():
					k = _hx_local_1.next()
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:801
					t = _g._types.h.get(k,None)
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:802
					if (t.kind == "enum"):
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:803
						_g1 = 0
						_g2 = t.fullQualifiedEnumConstructorsWithOptionalModule()
						while (_g1 < len(_g2)):
							ec = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
							_g1 = (_g1 + 1)
							# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:804
							res.h[ec] = t
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:805
					fq_name = t.fullQualifiedNameWithOptionalModule()
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:806
					res.h[fq_name] = t
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:808
				return res
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_2
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.allTypesAndEnumConstructorsWithInfo_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.allTypesAndEnumConstructorsWithInfo_cache

	def allTypesAndEnumConstructors(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:812
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.allTypesAndEnumConstructors_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.allTypesAndEnumConstructors_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:813
			def _hx_local_1():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:814
				res = _g.allTypesAndEnumConstructorsWithInfo()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:815
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:815
				_g1 = []
				_hx_local_0 = res.keys()
				while _hx_local_0.hasNext():
					k = _hx_local_0.next()
					_g1.append(k)
				return _g1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.allTypesAndEnumConstructors_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.allTypesAndEnumConstructors_cache

	def allTypes(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:820
		_g1 = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.allTypes_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.allTypes_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:822
			def _hx_local_1():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:822
				_g = []
				_hx_local_0 = _g1._types.iterator()
				while _hx_local_0.hasNext():
					v = _hx_local_0.next()
					_g.append(v)
				return _g
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.allTypes_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.allTypes_cache

	def filter(self,fn):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:828
		res = haxe_ds_StringMap()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:829
		_hx_local_0 = self._types.keys()
		while _hx_local_0.hasNext():
			k = _hx_local_0.next()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:830
			t = self._types.h.get(k,None)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:831
			if fn(t):
				res.h[k] = t
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:836
		return hxsublime_tools_HaxeTypeBundle(res)

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o._types = None
		_hx_o.toString_cache = None
		_hx_o.toString_cache_set = None
		_hx_o.packs_cache = None
		_hx_o.packs_cache_set = None
		_hx_o.allModules_cache = None
		_hx_o.allModules_cache_set = None
		_hx_o.allModulesList_cache = None
		_hx_o.allModulesList_cache_set = None
		_hx_o.allTypesAndEnumConstructorsWithInfo_cache = None
		_hx_o.allTypesAndEnumConstructorsWithInfo_cache_set = None
		_hx_o.allTypesAndEnumConstructors_cache = None
		_hx_o.allTypesAndEnumConstructors_cache_set = None
		_hx_o.allTypes_cache = None
		_hx_o.allTypes_cache_set = None
hxsublime_tools_HaxeTypeBundle._hx_class = hxsublime_tools_HaxeTypeBundle
_hx_classes["hxsublime.tools.HaxeTypeBundle"] = hxsublime_tools_HaxeTypeBundle


class hxsublime_tools_EnumConstructor:
	_hx_class_name = "hxsublime.tools.EnumConstructor"
	_hx_fields = ["name", "enumType"]
	_hx_methods = ["toSnippetInsert", "typeHint", "toSnippet", "toString"]

	def __init__(self,name,enum_type):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:854
		self.name = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:855
		self.enumType = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:859
		self.name = name
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:860
		self.enumType = enum_type

	def toSnippetInsert(self,import_list,insert_file):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:865
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:865
		_g = 0
		while (_g < len(import_list)):
			i = (import_list[_g] if _g >= 0 and _g < len(import_list) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:867
			if ((((self.enumType._file == insert_file) or ((i == self.enumType.fullQualifiedNameWithOptionalModule()))) or ((i == self.enumType.fullPackWithModule()))) or ((i == (((HxOverrides.stringOrNull(self.enumType.fullQualifiedNameWithOptionalModule()) + ".") + HxOverrides.stringOrNull(self.name)))))):
				return self.name
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:876
		return ((HxOverrides.stringOrNull(self.enumType.fullQualifiedNameWithOptionalModule()) + ".") + HxOverrides.stringOrNull(self.name))

	def typeHint(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:882
		return "enum value"

	def toSnippet(self,insert_file,import_list):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:888
		location = None
		if (len(self.enumType.fullPackWithOptionalModule()) > 0):
			location = ((" (" + HxOverrides.stringOrNull(self.enumType.fullPackWithOptionalModule())) + ")")
		else:
			location = ""
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:889
		display = (((((HxOverrides.stringOrNull(self.enumType.name) + ".") + HxOverrides.stringOrNull(self.name)) + ("null" if location is None else location)) + "\t") + HxOverrides.stringOrNull(self.typeHint()))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:890
		insert = self.toSnippetInsert(import_list,insert_file)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:892
		return (display, insert)

	def toString(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:897
		return self.name

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.name = None
		_hx_o.enumType = None
hxsublime_tools_EnumConstructor._hx_class = hxsublime_tools_EnumConstructor
_hx_classes["hxsublime.tools.EnumConstructor"] = hxsublime_tools_EnumConstructor


class hxsublime_tools_HaxeField:
	_hx_class_name = "hxsublime.tools.HaxeField"
	_hx_fields = ["type", "name", "kind", "isStatic", "isPublic", "isInline", "isPrivate", "match_decl", "srcPos_cache", "srcPos_cache_set", "isVar_cache", "isVar_cache_set", "file_cache", "file_cache_set", "isFunction_cache", "isFunction_cache_set", "toString_cache", "toString_cache_set", "toExpression_cache", "toExpression_cache_set"]
	_hx_methods = ["srcPos", "isVar", "file", "isFunction", "toString", "toExpression"]
	_hx_interfaces = [hxsublime_macros_LazyFunctionSupport]

	def __init__(self,_hx_type,name,kind,is_static,is_public,is_inline,is_private,match_decl):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:903
		self.type = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:904
		self.name = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:905
		self.kind = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:906
		self.isStatic = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:907
		self.isPublic = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:908
		self.isInline = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:909
		self.isPrivate = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:911
		self.match_decl = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:927
		self.srcPos_cache = None
		self.srcPos_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:942
		self.isVar_cache = None
		self.isVar_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:948
		self.file_cache = None
		self.file_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:955
		self.isFunction_cache = None
		self.isFunction_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:961
		self.toString_cache = None
		self.toString_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:967
		self.toExpression_cache = None
		self.toExpression_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:34
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
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:915
		self.type = _hx_type
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:916
		self.name = name
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:917
		self.kind = kind
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:918
		self.isStatic = is_static
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:919
		self.isPublic = is_public
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:920
		self.isInline = is_inline
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:921
		self.isPrivate = is_private
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:922
		self.match_decl = match_decl

	def srcPos(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:927
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.srcPos_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.srcPos_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:928
			def _hx_local_2():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:930
				def _hx_local_0():
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:930
					this1 = hxsublime_tools_Regex.fieldRegex.finditer(_g.type.src_with_comments)
					return python_HaxeIterator(this1)
				_hx_local_1 = _hx_local_0()
				while _hx_local_1.hasNext():
					decl = _hx_local_1.next()
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:932
					if (decl.group(0) == _g.match_decl.group(0)):
						return decl.start(0)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:937
				return None
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_2
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.srcPos_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.srcPos_cache

	def isVar(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:942
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.isVar_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.isVar_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:944
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:944
				return (_g.kind == "var")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.isVar_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.isVar_cache

	def file(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:948
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.file_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.file_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:951
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:951
				return _g.type._file
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.file_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.file_cache

	def isFunction(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:955
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.isFunction_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.isFunction_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:957
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:957
				return (_g.kind == "function")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.isFunction_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.isFunction_cache

	def toString(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:961
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.toString_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.toString_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:963
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:963
				return ((HxOverrides.stringOrNull(_g.type.fullQualifiedNameWithOptionalModule()) + HxOverrides.stringOrNull((("::" if ((_g.isStatic or ((_g.name == "new")))) else ".")))) + HxOverrides.stringOrNull(_g.name))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.toString_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.toString_cache

	def toExpression(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:967
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.toExpression_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.toExpression_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:969
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:969
				return ((HxOverrides.stringOrNull(_g.type.fullQualifiedNameWithOptionalModule()) + ".") + HxOverrides.stringOrNull(_g.name))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.toExpression_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.toExpression_cache

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.type = None
		_hx_o.name = None
		_hx_o.kind = None
		_hx_o.isStatic = None
		_hx_o.isPublic = None
		_hx_o.isInline = None
		_hx_o.isPrivate = None
		_hx_o.match_decl = None
		_hx_o.srcPos_cache = None
		_hx_o.srcPos_cache_set = None
		_hx_o.isVar_cache = None
		_hx_o.isVar_cache_set = None
		_hx_o.file_cache = None
		_hx_o.file_cache_set = None
		_hx_o.isFunction_cache = None
		_hx_o.isFunction_cache_set = None
		_hx_o.toString_cache = None
		_hx_o.toString_cache_set = None
		_hx_o.toExpression_cache = None
		_hx_o.toExpression_cache_set = None
hxsublime_tools_HaxeField._hx_class = hxsublime_tools_HaxeField
_hx_classes["hxsublime.tools.HaxeField"] = hxsublime_tools_HaxeField


class hxsublime_tools_HaxeType:
	_hx_class_name = "hxsublime.tools.HaxeType"
	_hx_fields = ["_src", "src_with_comments", "match_decl", "is_private", "pack", "module", "kind", "name", "is_module_type", "isStdType", "isExtern", "_file", "_enumConstructors", "strippedStartDeclPos_cache", "strippedStartDeclPos_cache_set", "classBody_cache", "classBody_cache_set", "publicStaticFields_cache", "publicStaticFields_cache_set", "allFields_cache", "allFields_cache_set", "allFieldsList_cache", "allFieldsList_cache_set", "publicStaticVars_cache", "publicStaticVars_cache_set", "publicStaticFunctions_cache", "publicStaticFunctions_cache_set", "classBodyStart_cache", "classBodyStart_cache_set", "strippedEndDeclPos_cache", "strippedEndDeclPos_cache_set", "srcPos_cache", "srcPos_cache_set", "toplevelPack_cache", "toplevelPack_cache_set", "fullPackWithOptionalModule_cache", "fullPackWithOptionalModule_cache_set", "fullPackWithModule_cache", "fullPackWithModule_cache_set", "packList_cache", "packList_cache_set", "packSuffix_cache", "packSuffix_cache_set", "fullQualifiedNameWithOptionalModule_cache", "fullQualifiedNameWithOptionalModule_cache_set", "enumConstructors_cache", "enumConstructors_cache_set", "fullQualifiedEnumConstructorsWithOptionalModule_cache", "fullQualifiedEnumConstructorsWithOptionalModule_cache_set", "classpath_cache", "classpath_cache_set", "fullQualifiedName_cache", "fullQualifiedName_cache_set", "toString_cache", "toString_cache_set"]
	_hx_methods = ["src", "file", "strippedStartDeclPos", "classBody", "publicStaticFields", "allFields", "allFieldsList", "publicStaticVars", "publicStaticFunctions", "classBodyStart", "strippedEndDeclPos", "srcPos", "toSnippet", "toSnippets", "toSnippetInsert", "toplevelPack", "typeHint", "fullPackWithOptionalModule", "fullPackWithModule", "isEnum", "isClass", "isAbstract", "packList", "packSuffix", "fullQualifiedNameWithOptionalModule", "enumConstructors", "fullQualifiedEnumConstructorsWithOptionalModule", "classpath", "fullQualifiedName", "toString"]
	_hx_interfaces = [hxsublime_macros_LazyFunctionSupport]

	def __init__(self,pack,module,name,kind,is_private,is_module_type,is_std_type,is_extern,file,src,src_with_comments,match_decl):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:977
		self._src = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:978
		self.src_with_comments = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:979
		self.match_decl = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:980
		self.is_private = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:981
		self.pack = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:982
		self.module = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:983
		self.kind = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:984
		self.name = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:985
		self.is_module_type = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:986
		self.isStdType = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:987
		self.isExtern = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:988
		self._file = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:989
		self._enumConstructors = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1012
		self.strippedStartDeclPos_cache = None
		self.strippedStartDeclPos_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1019
		self.classBody_cache = None
		self.classBody_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1035
		self.publicStaticFields_cache = None
		self.publicStaticFields_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1048
		self.allFields_cache = None
		self.allFields_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1088
		self.allFieldsList_cache = None
		self.allFieldsList_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1096
		self.publicStaticVars_cache = None
		self.publicStaticVars_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1104
		self.publicStaticFunctions_cache = None
		self.publicStaticFunctions_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1112
		self.classBodyStart_cache = None
		self.classBodyStart_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1124
		self.strippedEndDeclPos_cache = None
		self.strippedEndDeclPos_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1149
		self.srcPos_cache = None
		self.srcPos_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1202
		self.toplevelPack_cache = None
		self.toplevelPack_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1218
		self.fullPackWithOptionalModule_cache = None
		self.fullPackWithOptionalModule_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1225
		self.fullPackWithModule_cache = None
		self.fullPackWithModule_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1248
		self.packList_cache = None
		self.packList_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1255
		self.packSuffix_cache = None
		self.packSuffix_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1262
		self.fullQualifiedNameWithOptionalModule_cache = None
		self.fullQualifiedNameWithOptionalModule_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1270
		self.enumConstructors_cache = None
		self.enumConstructors_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1283
		self.fullQualifiedEnumConstructorsWithOptionalModule_cache = None
		self.fullQualifiedEnumConstructorsWithOptionalModule_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1301
		self.classpath_cache = None
		self.classpath_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1317
		self.fullQualifiedName_cache = None
		self.fullQualifiedName_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1323
		self.toString_cache = None
		self.toString_cache_set = None
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:34
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
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:996
		self._src = src
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:997
		self.src_with_comments = src_with_comments
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:998
		self.match_decl = match_decl
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:999
		self.is_private = is_private
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1000
		self.pack = pack
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1001
		self.module = module
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1002
		self.kind = kind
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1003
		self.name = name
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1004
		self.is_module_type = is_module_type
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1005
		self.isStdType = is_std_type
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1006
		self.isExtern = is_extern
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1007
		self._file = file
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1008
		self._enumConstructors = None

	def src(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:991
		return self._src

	def file(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:992
		return self._file

	def strippedStartDeclPos(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1012
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.strippedStartDeclPos_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.strippedStartDeclPos_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1014
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1014
				return _g.match_decl.start(0)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.strippedStartDeclPos_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.strippedStartDeclPos_cache

	def classBody(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1019
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.classBody_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.classBody_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1020
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1021
				res = None
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1022
				if (_g.strippedEndDeclPos is None):
					res = ""
				else:
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1028
					startIndex = _g.strippedStartDeclPos()
					endIndex = _g.strippedEndDeclPos()
					res = HxString.substring(_g._src,startIndex,endIndex)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1030
				return res
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.classBody_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.classBody_cache

	def publicStaticFields(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1035
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.publicStaticFields_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.publicStaticFields_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1036
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1037
				res = []
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1038
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1038
				x = _g.publicStaticVars()
				res.extend(x)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1039
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1039
				x1 = _g.publicStaticFunctions()
				res.extend(x1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1040
				return res
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.publicStaticFields_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.publicStaticFields_cache

	def allFields(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1048
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.allFields_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.allFields_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1049
			def _hx_local_1():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1050
				startTime = python_lib_Time.time()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1051
				res = haxe_ds_StringMap()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1052
				if (_g.classBody() is not None):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1053
					startPos = None
					_this = _g.classBodyStart()
					startPos = _this[0]
					# /opt/haxe-git/std/python/Syntax.hx:112
					# /opt/haxe-git/std/python/Syntax.hx:113
					decl = None
					# /opt/haxe-git/std/python/Syntax.hx:114
					for decl in hxsublime_tools_Regex.fieldRegex.finditer(_g.classBody()):
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1054
						decl = decl
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1055
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1057
						modifiers = decl.group(1)
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1058
						isStatic = ((modifiers is not None) and ((modifiers.find("static") > -1)))
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1059
						isInline = ((modifiers is not None) and ((modifiers.find("inline") > -1)))
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1060
						isPrivate = ((modifiers is not None) and ((modifiers.find("private") > -1)))
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1061
						isPublic = ((modifiers is not None) and ((modifiers.find("public") > -1)))
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1066
						def _hx_local_0():
							# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1066
							return hxsublime_tools_HxSrcTools.isSameNestingLevelAtPos(_g.classBody(),decl.start(0),startPos)
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1065
						sameNestingLevel = _hx_local_0
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1069
						if ((((isPrivate or isPublic) or isStatic) or _g.isExtern) or sameNestingLevel()):
							# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1071
							kind = decl.group(2)
							# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1072
							name = decl.group(3)
							# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1073
							# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1073
							value = hxsublime_tools_HaxeField(_g, name, kind, isStatic, isPublic, isInline, isPrivate, decl)
							res.h[name] = value
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1075
						startPos = decl.start(0)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1078
				runTime = (python_lib_Time.time() - startTime)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1079
				if (runTime > 0.02):
					haxe_Log.trace(((("allFields Time " + HxOverrides.stringOrNull(_g._file)) + " : ") + Std.string(runTime)),_hx_AnonObject({'fileName': "HxSrcTools.hx", 'lineNumber': 1080, 'className': "hxsublime.tools.HaxeType", 'methodName': "allFields"}))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1082
				return res
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.allFields_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.allFields_cache

	def allFieldsList(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1088
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.allFieldsList_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.allFieldsList_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1089
			def _hx_local_1():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1090
				all = _g.allFields()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1091
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1091
				_g1 = []
				_hx_local_0 = all.iterator()
				while _hx_local_0.hasNext():
					e = _hx_local_0.next()
					_g1.append(e)
				return _g1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.allFieldsList_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.allFieldsList_cache

	def publicStaticVars(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1096
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.publicStaticVars_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.publicStaticVars_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1097
			def _hx_local_1():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1098
				all = _g.allFields()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1099
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1099
				_g1 = []
				_hx_local_0 = all.iterator()
				while _hx_local_0.hasNext():
					e = _hx_local_0.next()
					if (e.isStatic and e.isVar()):
						_g1.append(e)
				return _g1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.publicStaticVars_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.publicStaticVars_cache

	def publicStaticFunctions(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1104
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.publicStaticFunctions_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.publicStaticFunctions_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1105
			def _hx_local_1():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1106
				all = _g.allFields()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1107
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1107
				_g1 = []
				_hx_local_0 = all.iterator()
				while _hx_local_0.hasNext():
					e = _hx_local_0.next()
					if (e.isStatic and e.isFunction()):
						_g1.append(e)
				return _g1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.publicStaticFunctions_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.publicStaticFunctions_cache

	def classBodyStart(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1112
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.classBodyStart_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.classBodyStart_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1113
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1114
				start = _g.match_decl.start(0)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1115
				if ((_g.kind == "abstract") or ((_g.kind == "class"))):
					return hxsublime_tools_HxSrcTools.searchNextCharOnSameNestingLevel(_g._src,["{"],start)
				else:
					return (0, "")
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.classBodyStart_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.classBodyStart_cache

	def strippedEndDeclPos(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1124
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.strippedEndDeclPos_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.strippedEndDeclPos_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1125
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1127
				classBodyStart = _g.classBodyStart()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1128
				res = None
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1129
				if (classBodyStart is not None):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1131
					classBodyEnd = hxsublime_tools_HxSrcTools.searchNextCharOnSameNestingLevel(_g._src,["}"],(classBodyStart[0] + 1))
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1132
					if (classBodyEnd is not None):
						res = classBodyEnd[0]
					else:
						res = None
				else:
					res = None
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1144
				return res
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.strippedEndDeclPos_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.strippedEndDeclPos_cache

	def srcPos(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1149
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.srcPos_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.srcPos_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1150
			def _hx_local_0():
				# /opt/haxe-git/std/python/Syntax.hx:112
				# /opt/haxe-git/std/python/Syntax.hx:113
				decl = None
				# /opt/haxe-git/std/python/Syntax.hx:114
				for decl in hxsublime_tools_Regex.typeDeclWithScope.finditer(_g.src_with_comments):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1152
					decl = decl
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1153
					if (decl.group(0) == _g.match_decl.group(0)):
						return decl.start(0)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1158
				return None
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.srcPos_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.srcPos_cache

	def toSnippet(self,insert_file,import_list):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1164
		location = None
		if (len(self.fullPackWithOptionalModule()) > 0):
			location = ((" (" + HxOverrides.stringOrNull(self.fullPackWithOptionalModule())) + ")")
		else:
			location = ""
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1165
		display = (((HxOverrides.stringOrNull(self.name) + ("null" if location is None else location)) + "\t") + HxOverrides.stringOrNull(self.kind))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1166
		insert = self.toSnippetInsert(import_list,insert_file)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1168
		return (display, insert)

	def toSnippets(self,import_list,insert_file):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1174
		res = [self.toSnippet(insert_file,import_list)]
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1176
		if ((self.kind == "enum") and ((self._enumConstructors is not None))):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1178
			_g = 0
			_g1 = self.enumConstructors()
			while (_g < len(_g1)):
				ev = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
				_g = (_g + 1)
				x = ev.toSnippet(insert_file,import_list)
				res.append(x)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1181
		return res

	def toSnippetInsert(self,import_list,insert_file):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1187
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1187
		_g = 0
		while (_g < len(import_list)):
			i = (import_list[_g] if _g >= 0 and _g < len(import_list) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1189
			if ((((self._file == insert_file) or ((i == self.fullPackWithModule()))) or ((i == self.fullQualifiedNameWithOptionalModule()))) or ((i == self.fullQualifiedName()))):
				return self.name
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1198
		return self.fullQualifiedNameWithOptionalModule()

	def toplevelPack(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1202
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.toplevelPack_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.toplevelPack_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1203
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1204
				pl = _g.packList()
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1205
				if (len(pl) > 0):
					return (pl[0] if 0 < len(pl) else None)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1207
				return None
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.toplevelPack_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.toplevelPack_cache

	def typeHint(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1214
		return self.kind

	def fullPackWithOptionalModule(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1218
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.fullPackWithOptionalModule_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.fullPackWithOptionalModule_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1219
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1220
				mod = None
				if (_g.is_module_type or _g.isStdType):
					mod = ""
				else:
					mod = (HxOverrides.stringOrNull(_g.packSuffix()) + HxOverrides.stringOrNull(_g.module))
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1221
				return (HxOverrides.stringOrNull(_g.pack) + ("null" if mod is None else mod))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.fullPackWithOptionalModule_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.fullPackWithOptionalModule_cache

	def fullPackWithModule(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1225
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.fullPackWithModule_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.fullPackWithModule_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1227
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1227
				return ((HxOverrides.stringOrNull(_g.pack) + HxOverrides.stringOrNull(_g.packSuffix())) + HxOverrides.stringOrNull(_g.module))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.fullPackWithModule_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.fullPackWithModule_cache

	def isEnum(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1233
		return (self.kind == "enum")

	def isClass(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1238
		return (self.kind == "class")

	def isAbstract(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1243
		return (self.kind == "abstract")

	def packList(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1248
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.packList_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.packList_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1250
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1250
				if (len(_g.pack) > 0):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1250
					_this = _g.pack
					return _this.split(".")
				else:
					return []
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.packList_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.packList_cache

	def packSuffix(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1255
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.packSuffix_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.packSuffix_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1257
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1257
				if (len(_g.pack) == 0):
					return ""
				else:
					return "."
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.packSuffix_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.packSuffix_cache

	def fullQualifiedNameWithOptionalModule(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1262
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.fullQualifiedNameWithOptionalModule_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.fullQualifiedNameWithOptionalModule_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1263
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1264
				mod = None
				if (_g.is_module_type or _g.isStdType):
					mod = ""
				else:
					mod = (HxOverrides.stringOrNull(_g.module) + ".")
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1265
				return (((HxOverrides.stringOrNull(_g.pack) + HxOverrides.stringOrNull(_g.packSuffix())) + ("null" if mod is None else mod)) + HxOverrides.stringOrNull(_g.name))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.fullQualifiedNameWithOptionalModule_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.fullQualifiedNameWithOptionalModule_cache

	def enumConstructors(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1270
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.enumConstructors_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.enumConstructors_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1271
			def _hx_local_1():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1272
				res = None
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1273
				if ((_g.kind == "enum") and ((_g._enumConstructors is not None))):
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1274
					_g1 = []
					_g2 = 0
					_g3 = _g._enumConstructors
					while (_g2 < len(_g3)):
						e = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
						_g2 = (_g2 + 1)
						x = hxsublime_tools_EnumConstructor(e, _g)
						_g1.append(x)
					res = _g1
				else:
					res = []
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1279
				return res
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.enumConstructors_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.enumConstructors_cache

	def fullQualifiedEnumConstructorsWithOptionalModule(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1283
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.fullQualifiedEnumConstructorsWithOptionalModule_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.fullQualifiedEnumConstructorsWithOptionalModule_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1284
			def _hx_local_1():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1285
				res = None
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1286
				if ((not ((_g.kind == "enum"))) or ((_g._enumConstructors is None))):
					res = []
				else:
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1292
					fqName = _g.fullQualifiedNameWithOptionalModule()
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1293
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1293
					_g1 = []
					_g2 = 0
					_g3 = _g._enumConstructors
					while (_g2 < len(_g3)):
						e = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
						_g2 = (_g2 + 1)
						_g1.append(((("null" if fqName is None else fqName) + ".") + ("null" if e is None else e)))
					res = _g1
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1295
				return res
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.fullQualifiedEnumConstructorsWithOptionalModule_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.fullQualifiedEnumConstructorsWithOptionalModule_cache

	def classpath(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1301
		_g1 = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.classpath_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.classpath_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1302
			def _hx_local_1():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1303
				path_append = None
				_g = []
				_g2 = 0
				_g3 = _g1.packList()
				while (_g2 < len(_g3)):
					_ = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
					_g2 = (_g2 + 1)
					_g.append("..")
				path_append = _g
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1306
				mod_dir = python_lib_os_Path.dirname(_g1._file)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1307
				fp = [mod_dir]
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1308
				fp.extend(path_append)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1310
				full_dir = python_lib_Os.sep.join([python_Boot.toString1(x1,'') for x1 in fp])
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1312
				return python_lib_os_Path.normpath(full_dir)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_1
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.classpath_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.classpath_cache

	def fullQualifiedName(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1317
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.fullQualifiedName_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.fullQualifiedName_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1319
			def _hx_local_0():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1319
				return ((((HxOverrides.stringOrNull(_g.pack) + HxOverrides.stringOrNull(_g.packSuffix())) + HxOverrides.stringOrNull(_g.module)) + ".") + HxOverrides.stringOrNull(_g.name))
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_0
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.fullQualifiedName_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.fullQualifiedName_cache

	def toString(self):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1323
		_g = self
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:47
		if (not self.toString_cache_set):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:48
			self.toString_cache_set = True
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1325
			def _hx_local_4():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1325
				def _hx_local_3():
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1330
					def _hx_local_0():
						# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1330
						_this = _g.enumConstructors()
						def _hx_local_2():
							def _hx_local_1(ec):
								return ec.toString()
							return list(map(_hx_local_1,_this))
						return _hx_local_2()
					# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/HxSrcTools.hx:1325
					return (((((((((((((((((((((((((((((((((("{" + " pack:") + Std.string(_g.pack)) + ", ") + " module:") + Std.string(_g.module)) + ", ") + " name:") + Std.string(_g.name)) + ", ") + " kind:") + Std.string(_g.kind)) + ", ") + " enum_constructors:") + Std.string(_hx_local_0())) + ", ") + " is_private:") + Std.string(_g.is_private)) + ", ") + " is_module_type:") + Std.string(_g.is_module_type)) + ", ") + " isStdType:") + Std.string(_g.isStdType)) + ", ") + " is_extern:") + Std.string(_g.isExtern)) + ", ") + " file:'") + Std.string(_g._file)) + "'") + " classpath:'") + Std.string(_g.classpath())) + "'") + " }")
				return _hx_local_3()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:49
			eval = _hx_local_4
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:50
			self.toString_cache = eval()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/macros/LazyFunctionMacro.hx:52
		return self.toString_cache

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o._src = None
		_hx_o.src_with_comments = None
		_hx_o.match_decl = None
		_hx_o.is_private = None
		_hx_o.pack = None
		_hx_o.module = None
		_hx_o.kind = None
		_hx_o.name = None
		_hx_o.is_module_type = None
		_hx_o.isStdType = None
		_hx_o.isExtern = None
		_hx_o._file = None
		_hx_o._enumConstructors = None
		_hx_o.strippedStartDeclPos_cache = None
		_hx_o.strippedStartDeclPos_cache_set = None
		_hx_o.classBody_cache = None
		_hx_o.classBody_cache_set = None
		_hx_o.publicStaticFields_cache = None
		_hx_o.publicStaticFields_cache_set = None
		_hx_o.allFields_cache = None
		_hx_o.allFields_cache_set = None
		_hx_o.allFieldsList_cache = None
		_hx_o.allFieldsList_cache_set = None
		_hx_o.publicStaticVars_cache = None
		_hx_o.publicStaticVars_cache_set = None
		_hx_o.publicStaticFunctions_cache = None
		_hx_o.publicStaticFunctions_cache_set = None
		_hx_o.classBodyStart_cache = None
		_hx_o.classBodyStart_cache_set = None
		_hx_o.strippedEndDeclPos_cache = None
		_hx_o.strippedEndDeclPos_cache_set = None
		_hx_o.srcPos_cache = None
		_hx_o.srcPos_cache_set = None
		_hx_o.toplevelPack_cache = None
		_hx_o.toplevelPack_cache_set = None
		_hx_o.fullPackWithOptionalModule_cache = None
		_hx_o.fullPackWithOptionalModule_cache_set = None
		_hx_o.fullPackWithModule_cache = None
		_hx_o.fullPackWithModule_cache_set = None
		_hx_o.packList_cache = None
		_hx_o.packList_cache_set = None
		_hx_o.packSuffix_cache = None
		_hx_o.packSuffix_cache_set = None
		_hx_o.fullQualifiedNameWithOptionalModule_cache = None
		_hx_o.fullQualifiedNameWithOptionalModule_cache_set = None
		_hx_o.enumConstructors_cache = None
		_hx_o.enumConstructors_cache_set = None
		_hx_o.fullQualifiedEnumConstructorsWithOptionalModule_cache = None
		_hx_o.fullQualifiedEnumConstructorsWithOptionalModule_cache_set = None
		_hx_o.classpath_cache = None
		_hx_o.classpath_cache_set = None
		_hx_o.fullQualifiedName_cache = None
		_hx_o.fullQualifiedName_cache_set = None
		_hx_o.toString_cache = None
		_hx_o.toString_cache_set = None
hxsublime_tools_HaxeType._hx_class = hxsublime_tools_HaxeType
_hx_classes["hxsublime.tools.HaxeType"] = hxsublime_tools_HaxeType


class hxsublime_tools_PathTools:
	_hx_class_name = "hxsublime.tools.PathTools"
	_hx_statics = ["removeDir", "joinNorm", "isAbsPath"]

	@staticmethod
	def removeDir(path):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/PathTools.hx:9
		if python_lib_os_Path.isdir(path):
			python_lib_Shutil.rmtree(path)

	@staticmethod
	def joinNorm(path1,path2):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/PathTools.hx:17
		return python_lib_os_Path.normpath(python_lib_os_Path.join(path1,path2))

	@staticmethod
	def isAbsPath(path):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/PathTools.hx:22
		return (python_lib_os_Path.normpath(path) == python_lib_os_Path.abspath(path))
hxsublime_tools_PathTools._hx_class = hxsublime_tools_PathTools
_hx_classes["hxsublime.tools.PathTools"] = hxsublime_tools_PathTools


class hxsublime_tools_ScopeTools:
	_hx_class_name = "hxsublime.tools.ScopeTools"
	_hx_statics = ["containsAny", "containsStringOrComment"]

	@staticmethod
	def containsAny(scopes,scopes_test):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ScopeTools.hx:6
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ScopeTools.hx:6
		_g = 0
		while (_g < len(scopes)):
			s = (scopes[_g] if _g >= 0 and _g < len(scopes) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ScopeTools.hx:8
			def _hx_local_1():
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ScopeTools.hx:8
				x = HxOverrides.arrayGet(s.split("."), 0)
				return x in scopes_test
			if _hx_local_1():
				return True
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ScopeTools.hx:13
		return False

	@staticmethod
	def containsStringOrComment(scopes):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ScopeTools.hx:17
		return hxsublime_tools_ScopeTools.containsAny(scopes,["string", "comments"])
hxsublime_tools_ScopeTools._hx_class = hxsublime_tools_ScopeTools
_hx_classes["hxsublime.tools.ScopeTools"] = hxsublime_tools_ScopeTools


class hxsublime_tools_StringTools:
	_hx_class_name = "hxsublime.tools.StringTools"
	_hx_statics = ["_whitespace", "startsWithAny", "isWhitespaceOrEmpty"]

	@staticmethod
	def startsWithAny(s,l):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/StringTools.hx:15
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/StringTools.hx:15
		_g = 0
		while (_g < len(l)):
			s1 = (l[_g] if _g >= 0 and _g < len(l) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/StringTools.hx:17
			if StringTools.startsWith(s,s1):
				return True
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/StringTools.hx:22
		return False

	@staticmethod
	def isWhitespaceOrEmpty(s):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/StringTools.hx:27
		return (python_lib_Re.match(hxsublime_tools_StringTools._whitespace,s) is not None)
hxsublime_tools_StringTools._hx_class = hxsublime_tools_StringTools
_hx_classes["hxsublime.tools.StringTools"] = hxsublime_tools_StringTools


class hxsublime_tools_SublimeTools:
	_hx_class_name = "hxsublime.tools.SublimeTools"
	_hx_statics = ["getProjectFile"]

	@staticmethod
	def getProjectFile(winId = None):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/SublimeTools.hx:9
		if (winId is None):
			winId = sublime_Sublime.active_window().id()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/SublimeTools.hx:13
		return sublime_Sublime.active_window().project_file_name()
hxsublime_tools_SublimeTools._hx_class = hxsublime_tools_SublimeTools
_hx_classes["hxsublime.tools.SublimeTools"] = hxsublime_tools_SublimeTools


class hxsublime_tools_AsyncEdit:
	_hx_class_name = "hxsublime.tools.AsyncEdit"
	_hx_statics = ["dict", "id", "asyncEdit", "run"]

	@staticmethod
	def asyncEdit(view,doEdit):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:28
		def _hx_local_2():
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:29
			id = hxsublime_tools_AsyncEdit.id
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:30
			if (hxsublime_tools_AsyncEdit.id > 1000000):
				hxsublime_tools_AsyncEdit.id = 0
			else:
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:33
				_hx_local_0 = hxsublime_tools_AsyncEdit
				_hx_local_1 = _hx_local_0.id
				_hx_local_0.id = (_hx_local_1 + 1)
				_hx_local_0.id
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:35
			hxsublime_tools_AsyncEdit.dict[id] = doEdit
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:36
			view.run_command(hxsublime_tools_HaxeTextEditCommand.COMMAND_ID,python_Lib.anonToDict(_hx_AnonObject({'id': id})))
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:27
		start = _hx_local_2
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:39
		sublime_Sublime.set_timeout(start,10)

	@staticmethod
	def run(view,edit,d):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:44
		id = d.get("id",None)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:46
		if id in hxsublime_tools_AsyncEdit.dict:
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:48
			fun = hxsublime_tools_AsyncEdit.dict.get(id,None)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:49
			del hxsublime_tools_AsyncEdit.dict[id]
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:50
			fun(view,edit)
hxsublime_tools_AsyncEdit._hx_class = hxsublime_tools_AsyncEdit
_hx_classes["hxsublime.tools.AsyncEdit"] = hxsublime_tools_AsyncEdit


class hxsublime_tools_HaxeTextEditCommand(sublime_TextCommand):
	_hx_class_name = "hxsublime.tools.HaxeTextEditCommand"
	_hx_fields = []
	_hx_methods = ["run"]
	_hx_statics = ["COMMAND_ID"]
	_hx_interfaces = []
	_hx_super = sublime_TextCommand


	def __init__(self,v):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:55
		super().__init__(v)

	def run(self,edit,**args):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:61
		hxsublime_tools_AsyncEdit.run(self.view,edit,python__KwArgs_KwArgs_Impl_.toDictHelper(args,None))

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
hxsublime_tools_HaxeTextEditCommand._hx_class = hxsublime_tools_HaxeTextEditCommand
_hx_classes["hxsublime.tools.HaxeTextEditCommand"] = hxsublime_tools_HaxeTextEditCommand


class hxsublime_tools_ViewTools:
	_hx_class_name = "hxsublime.tools.ViewTools"
	_hx_statics = ["insertSnippet", "insertAtCursor", "getFirstCursorPos", "asyncEdit", "findViewByName", "createMissingFolders", "getContentUntilFirstCursor", "getContentUntil", "getContent", "isHxsl", "isSupported", "isUnsupported", "getScopesAt", "isHaxe", "isHxml", "isErazor", "isNmml", "replaceContent", "inHaxeCode", "inHaxeString", "inHaxeComments"]

	@staticmethod
	def insertSnippet(view,snippet):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:70
		view.run_command("insert_snippet",python_Lib.anonToDict(_hx_AnonObject({'contents': snippet})))

	@staticmethod
	def insertAtCursor(view,txt):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:77
		def _hx_local_0(v,e):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:77
			v.insert(e,hxsublime_tools_ViewTools.getFirstCursorPos(v),txt)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:75
		doEdit = _hx_local_0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:79
		hxsublime_tools_ViewTools.asyncEdit(view,doEdit)

	@staticmethod
	def getFirstCursorPos(view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:85
		return view.sel()[0].begin()

	@staticmethod
	def asyncEdit(view,doEdit):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:91
		hxsublime_tools_AsyncEdit.asyncEdit(view,doEdit)

	@staticmethod
	def findViewByName(name):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:97
		windows = sublime_Sublime.windows()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:98
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:98
		_g = 0
		while (_g < len(windows)):
			w = (windows[_g] if _g >= 0 and _g < len(windows) else None)
			_g = (_g + 1)
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:100
			views = w.views()
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:102
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:102
			_g1 = 0
			while (_g1 < len(views)):
				v = (views[_g1] if _g1 >= 0 and _g1 < len(views) else None)
				_g1 = (_g1 + 1)
				# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:104
				if (v.name() == name):
					return v
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:107
		return None

	@staticmethod
	def createMissingFolders(view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:113
		fn = view.file_name()
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:114
		path = python_lib_os_Path.dirname(fn)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:115
		if (not python_lib_os_Path.isdir(path)):
			python_lib_Os.makedirs(path)

	@staticmethod
	def getContentUntilFirstCursor(view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:123
		end = hxsublime_tools_ViewTools.getFirstCursorPos(view)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:124
		return hxsublime_tools_ViewTools.getContentUntil(view,end)

	@staticmethod
	def getContentUntil(view,endPos):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:129
		return view.substr(sublime_Region(0, endPos))

	@staticmethod
	def getContent(view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:134
		return view.substr(sublime_Region(0, view.size()))

	@staticmethod
	def isHxsl(view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:139
		return StringTools.endsWith(view.file_name(),hxsublime_Config.HXSL_SUFFIX)

	@staticmethod
	def isSupported(view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:144
		return (view.score_selector(0,((((((HxOverrides.stringOrNull(hxsublime_Config.SOURCE_HAXE) + ",") + HxOverrides.stringOrNull(hxsublime_Config.SOURCE_HXML)) + ",") + HxOverrides.stringOrNull(hxsublime_Config.SOURCE_ERAZOR)) + ",") + HxOverrides.stringOrNull(hxsublime_Config.SOURCE_NMML))) > 0)

	@staticmethod
	def isUnsupported(view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:149
		return (not hxsublime_tools_ViewTools.isSupported(view))

	@staticmethod
	def getScopesAt(view,pos):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:154
		_this = view.scope_name(pos)
		return _this.split(" ")

	@staticmethod
	def isHaxe(view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:160
		return (view.score_selector(0,hxsublime_Config.SOURCE_HAXE) > 0)

	@staticmethod
	def isHxml(view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:164
		return (view.score_selector(0,hxsublime_Config.SOURCE_HXML) > 0)

	@staticmethod
	def isErazor(view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:169
		return (view.score_selector(0,hxsublime_Config.SOURCE_ERAZOR) > 0)

	@staticmethod
	def isNmml(view):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:174
		return (view.score_selector(0,hxsublime_Config.SOURCE_NMML) > 0)

	@staticmethod
	def replaceContent(view,newContent):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:182
		def _hx_local_0(view1,edit):
			# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:182
			view1.replace(edit,sublime_Region(0, view1.size()),newContent)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:180
		doEdit = _hx_local_0
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:186
		view.set_read_only(False)
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:187
		hxsublime_tools_ViewTools.asyncEdit(view,doEdit)

	@staticmethod
	def inHaxeCode(view,caret):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:192
		return (((view.score_selector(caret,"source.haxe") > 0) and ((view.score_selector(caret,"string") == 0))) and ((view.score_selector(caret,"comment") == 0)))

	@staticmethod
	def inHaxeString(view,caret):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:197
		return ((view.score_selector(caret,"source.haxe") > 0) and ((view.score_selector(caret,"string") > 0)))

	@staticmethod
	def inHaxeComments(view,caret):
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/tools/ViewTools.hx:202
		return ((view.score_selector(caret,"source.haxe") > 0) and ((view.score_selector(caret,"comment") > 0)))
hxsublime_tools_ViewTools._hx_class = hxsublime_tools_ViewTools
_hx_classes["hxsublime.tools.ViewTools"] = hxsublime_tools_ViewTools


class python_HaxeIterable:
	_hx_class_name = "python.HaxeIterable"
	_hx_fields = ["x"]
	_hx_methods = ["iterator"]

	def __init__(self,x):
		# /opt/haxe-git/std/python/HaxeIterable.hx:28
		self.x = None
		# /opt/haxe-git/std/python/HaxeIterable.hx:31
		self.x = x

	def iterator(self):
		# /opt/haxe-git/std/python/HaxeIterable.hx:35
		return python_HaxeIterator(self.x.__iter__())

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.x = None
python_HaxeIterable._hx_class = python_HaxeIterable
_hx_classes["python.HaxeIterable"] = python_HaxeIterable


class python__KwArgs_KwArgs_Impl_:
	_hx_class_name = "python._KwArgs.KwArgs_Impl_"
	_hx_statics = ["_new", "toDict", "toDictHelper", "fromDict", "fromT", "typed", "get"]

	@staticmethod
	def _new(d):
		# /opt/haxe-git/std/python/KwArgs.hx:37
		return d

	@staticmethod
	def toDict(this1):
		# /opt/haxe-git/std/python/KwArgs.hx:42
		return python__KwArgs_KwArgs_Impl_.toDictHelper(this1,None)

	@staticmethod
	def toDictHelper(this1,x):
		# /opt/haxe-git/std/python/KwArgs.hx:47
		return this1

	@staticmethod
	def fromDict(d):
		# /opt/haxe-git/std/python/KwArgs.hx:51
		return d

	@staticmethod
	def fromT(d):
		# /opt/haxe-git/std/python/KwArgs.hx:55
		d1 = python_Lib.anonAsDict(d)
		return d1

	@staticmethod
	def typed(this1):
		# /opt/haxe-git/std/python/KwArgs.hx:59
		return python_Lib.dictAsAnon(python__KwArgs_KwArgs_Impl_.toDictHelper(this1,None))

	@staticmethod
	def get(this1,key,_hx_def):
		# /opt/haxe-git/std/python/KwArgs.hx:63
		return this1.get(key,_hx_def)
python__KwArgs_KwArgs_Impl_._hx_class = python__KwArgs_KwArgs_Impl_
_hx_classes["python._KwArgs.KwArgs_Impl_"] = python__KwArgs_KwArgs_Impl_


class python_Lib:
	_hx_class_name = "python.Lib"
	_hx_statics = ["print", "println", "dictToAnon", "anonToDict", "anonAsDict", "dictAsAnon", "toPythonIterable", "toHaxeIterable", "toHaxeIterator"]

	@staticmethod
	def print(v):
		# /opt/haxe-git/std/python/Lib.hx:33
		_hx_str = Std.string(v)
		# /opt/haxe-git/std/python/Lib.hx:35
		python_lib_Sys.stdout.buffer.write(_hx_str.encode("utf-8", "strict"))
		# /opt/haxe-git/std/python/Lib.hx:36
		python_lib_Sys.stdout.flush()

	@staticmethod
	def println(v):
		# /opt/haxe-git/std/python/Lib.hx:40
		_hx_str = Std.string(v)
		# /opt/haxe-git/std/python/Lib.hx:42
		python_lib_Sys.stdout.buffer.write((("" + ("null" if _hx_str is None else _hx_str)) + "\n").encode("utf-8", "strict"))
		# /opt/haxe-git/std/python/Lib.hx:43
		python_lib_Sys.stdout.flush()

	@staticmethod
	def dictToAnon(v):
		# /opt/haxe-git/std/python/Lib.hx:50
		return _hx_AnonObject(v.copy())

	@staticmethod
	def anonToDict(o):
		# /opt/haxe-git/std/python/Lib.hx:59
		if isinstance(o,_hx_AnonObject):
			return o.__dict__.copy()
		else:
			return None

	@staticmethod
	def anonAsDict(o):
		# /opt/haxe-git/std/python/Lib.hx:73
		if isinstance(o,_hx_AnonObject):
			return o.__dict__
		else:
			return None

	@staticmethod
	def dictAsAnon(d):
		# /opt/haxe-git/std/python/Lib.hx:85
		return _hx_AnonObject(d)

	@staticmethod
	def toPythonIterable(it):
		# /opt/haxe-git/std/python/Lib.hx:89
		def _hx_local_3():
			# /opt/haxe-git/std/python/Lib.hx:90
			def _hx_local_2():
				# /opt/haxe-git/std/python/Lib.hx:91
				it1 = HxOverrides.iterator(it)
				# /opt/haxe-git/std/python/Lib.hx:92
				self = None
				# /opt/haxe-git/std/python/Lib.hx:95
				def _hx_local_0():
					# /opt/haxe-git/std/python/Lib.hx:95
					if it1.hasNext():
						return it1.next()
					else:
						raise StopIteration()
				# /opt/haxe-git/std/python/Lib.hx:101
				def _hx_local_1():
					# /opt/haxe-git/std/python/Lib.hx:101
					return self
				# /opt/haxe-git/std/python/Lib.hx:93
				self = _hx_AnonObject({'__next__': _hx_local_0, '__iter__': _hx_local_1})
				# /opt/haxe-git/std/python/Lib.hx:103
				return self
			# /opt/haxe-git/std/python/Lib.hx:89
			return _hx_AnonObject({'__iter__': _hx_local_2})
		return _hx_local_3()

	@staticmethod
	def toHaxeIterable(it):
		# /opt/haxe-git/std/python/Lib.hx:109
		return python_HaxeIterable(it)

	@staticmethod
	def toHaxeIterator(it):
		# /opt/haxe-git/std/python/Lib.hx:113
		return python_HaxeIterator(it)
python_Lib._hx_class = python_Lib
_hx_classes["python.Lib"] = python_Lib


class python__NativeIterable_NativeIterable_Impl_:
	_hx_class_name = "python._NativeIterable.NativeIterable_Impl_"
	_hx_statics = ["toHaxeIterable", "iterator"]

	@staticmethod
	def toHaxeIterable(this1):
		# /opt/haxe-git/std/python/NativeIterable.hx:36
		return python_HaxeIterable(this1)

	@staticmethod
	def iterator(this1):
		# /opt/haxe-git/std/python/NativeIterable.hx:41
		return python_HaxeIterator(this1.__iter__())
python__NativeIterable_NativeIterable_Impl_._hx_class = python__NativeIterable_NativeIterable_Impl_
_hx_classes["python._NativeIterable.NativeIterable_Impl_"] = python__NativeIterable_NativeIterable_Impl_


class python__NativeIterator_NativeIterator_Impl_:
	_hx_class_name = "python._NativeIterator.NativeIterator_Impl_"
	_hx_statics = ["_new", "toHaxeIterator"]

	@staticmethod
	def _new(p):
		# /opt/haxe-git/std/python/NativeIterator.hx:31
		return p

	@staticmethod
	def toHaxeIterator(this1):
		# /opt/haxe-git/std/python/NativeIterator.hx:36
		return python_HaxeIterator(this1)
python__NativeIterator_NativeIterator_Impl_._hx_class = python__NativeIterator_NativeIterator_Impl_
_hx_classes["python._NativeIterator.NativeIterator_Impl_"] = python__NativeIterator_NativeIterator_Impl_


class python_NativeStringTools:
	_hx_class_name = "python.NativeStringTools"
	_hx_statics = ["format", "encode", "contains", "strip", "rpartition"]

	@staticmethod
	def format(s,args):
		# /opt/haxe-git/std/python/NativeStringTools.hx:31
		return s.format(*args)

	@staticmethod
	def encode(s,encoding = "utf-8",errors = "strict"):
		# /opt/haxe-git/std/python/NativeStringTools.hx:35
		if (encoding is None):
			encoding = "utf-8"
		if (errors is None):
			errors = "strict"
		return s.encode(encoding, errors)

	@staticmethod
	def contains(s,e):
		# /opt/haxe-git/std/python/NativeStringTools.hx:39
		return e in s

	@staticmethod
	def strip(s,chars = None):
		# /opt/haxe-git/std/python/NativeStringTools.hx:44
		return s.strip(chars)

	@staticmethod
	def rpartition(s,sep):
		# /opt/haxe-git/std/python/NativeStringTools.hx:49
		return s.rpartition(sep)
python_NativeStringTools._hx_class = python_NativeStringTools
_hx_classes["python.NativeStringTools"] = python_NativeStringTools


class python__VarArgs_VarArgs_Impl_:
	_hx_class_name = "python._VarArgs.VarArgs_Impl_"
	_hx_statics = ["_new", "raw", "toArray", "fromArray"]

	@staticmethod
	def _new(d):
		# /opt/haxe-git/std/python/VarArgs.hx:38
		return d

	@staticmethod
	def raw(this1):
		# /opt/haxe-git/std/python/VarArgs.hx:42
		return this1

	@staticmethod
	def toArray(this1):
		# /opt/haxe-git/std/python/VarArgs.hx:46
		if (not Std._hx_is(this1,list)):
			return list(this1)
		else:
			return this1

	@staticmethod
	def fromArray(d):
		# /opt/haxe-git/std/python/VarArgs.hx:50
		return d
python__VarArgs_VarArgs_Impl_._hx_class = python__VarArgs_VarArgs_Impl_
_hx_classes["python._VarArgs.VarArgs_Impl_"] = python__VarArgs_VarArgs_Impl_


class python_internal_ArrayImpl:
	_hx_class_name = "python.internal.ArrayImpl"
	_hx_statics = ["get_length", "concat", "copy", "iterator", "indexOf", "lastIndexOf", "join", "toString", "pop", "push", "unshift", "remove", "shift", "slice", "sort", "splice", "map", "filter", "insert", "reverse", "_get", "_set", "unsafeGet", "unsafeSet"]

	@staticmethod
	def get_length(x):
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:31
		return len(x)

	@staticmethod
	def concat(a1,a2):
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:35
		return (a1 + a2)

	@staticmethod
	def copy(x):
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:40
		return list(x)

	@staticmethod
	def iterator(x):
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:45
		return python_HaxeIterator(x.__iter__())

	@staticmethod
	def indexOf(a,x,fromIndex = None):
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:50
		_hx_len = len(a)
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:52
		l = None
		if (fromIndex is None):
			l = 0
		elif (fromIndex < 0):
			l = (_hx_len + fromIndex)
		else:
			l = fromIndex
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:55
		if (l < 0):
			l = 0
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:56
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:56
		_g = l
		while (_g < _hx_len):
			i = _g
			_g = (_g + 1)
			# /opt/haxe-git/std/python/internal/ArrayImpl.hx:57
			if (a[i] == x):
				return i
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:59
		return -1

	@staticmethod
	def lastIndexOf(a,x,fromIndex = None):
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:64
		_hx_len = len(a)
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:66
		l = None
		if (fromIndex is None):
			l = _hx_len
		elif (fromIndex < 0):
			l = ((_hx_len + fromIndex) + 1)
		else:
			l = (fromIndex + 1)
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:69
		if (l > _hx_len):
			l = _hx_len
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:70
		def _hx_local_1():
			# /opt/haxe-git/std/python/internal/ArrayImpl.hx:70
			nonlocal l
			l = (l - 1)
			return l
		while (_hx_local_1() > -1):
			if (a[l] == x):
				return l
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:73
		return -1

	@staticmethod
	def join(x,sep):
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:79
		return sep.join([python_Boot.toString1(x1,'') for x1 in x])

	@staticmethod
	def toString(x):
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:84
		return (("[" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in x]))) + "]")

	@staticmethod
	def pop(x):
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:89
		if (len(x) == 0):
			return None
		else:
			return x.pop()

	@staticmethod
	def push(x,e):
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:94
		x.append(e)
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:95
		return len(x)

	@staticmethod
	def unshift(x,e):
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:100
		x.insert(0, e)

	@staticmethod
	def remove(x,e):
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:105
		try:
			# /opt/haxe-git/std/python/internal/ArrayImpl.hx:106
			x.remove(e)
			# /opt/haxe-git/std/python/internal/ArrayImpl.hx:107
			return True
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			e1 = _hx_e1
			return False

	@staticmethod
	def shift(x):
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:115
		if (len(x) == 0):
			return None
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:116
		return x.pop(0)

	@staticmethod
	def slice(x,pos,end = None):
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:121
		return x[pos:end]

	@staticmethod
	def sort(x,f):
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:125
		x.sort(key= python_lib_Functools.cmp_to_key(f))

	@staticmethod
	def splice(x,pos,_hx_len):
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:130
		if (pos < 0):
			pos = (len(x) + pos)
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:131
		if (pos < 0):
			pos = 0
		# /opt/haxe-git/std/python/Syntax.hx:80
		res = x[pos:(pos + _hx_len)]
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:133
		del x[pos:(pos + _hx_len)]
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:134
		return res

	@staticmethod
	def map(x,f):
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:139
		return list(map(f,x))

	@staticmethod
	def filter(x,f):
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:144
		return list(filter(f,x))

	@staticmethod
	def insert(a,pos,x):
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:149
		a.insert(pos, x)

	@staticmethod
	def reverse(a):
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:153
		a.reverse()

	@staticmethod
	def _get(x,idx):
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:158
		if ((idx > -1) and ((idx < len(x)))):
			return x[idx]
		else:
			return None

	@staticmethod
	def _set(x,idx,v):
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:163
		l = len(x)
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:164
		while (l < idx):
			# /opt/haxe-git/std/python/internal/ArrayImpl.hx:165
			# /opt/haxe-git/std/python/internal/ArrayImpl.hx:165
			x.append(None)
			# /opt/haxe-git/std/python/internal/ArrayImpl.hx:166
			l = (l + 1)
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:168
		if (l == idx):
			# /opt/haxe-git/std/python/internal/ArrayImpl.hx:169
			x.append(v)
		else:
			x[idx] = v
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:173
		return v

	@staticmethod
	def unsafeGet(x,idx):
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:177
		return x[idx]

	@staticmethod
	def unsafeSet(x,idx,val):
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:181
		x[idx] = val
		# /opt/haxe-git/std/python/internal/ArrayImpl.hx:182
		return val
python_internal_ArrayImpl._hx_class = python_internal_ArrayImpl
_hx_classes["python.internal.ArrayImpl"] = python_internal_ArrayImpl


class _HxException(Exception):
	_hx_class_name = "_HxException"
	_hx_fields = ["val"]
	_hx_methods = []
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = Exception


	def __init__(self,val):
		# /opt/haxe-git/std/python/internal/HxException.hx:28
		self.val = None
		# /opt/haxe-git/std/python/internal/HxException.hx:31
		message = str(val)
		# /opt/haxe-git/std/python/internal/HxException.hx:32
		super().__init__(message)
		# /opt/haxe-git/std/python/internal/HxException.hx:33
		self.val = val

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.val = None
_HxException._hx_class = _HxException
_hx_classes["_HxException"] = _HxException


class python_internal_Internal:
	_hx_class_name = "python.internal.Internal"
python_internal_Internal._hx_class = python_internal_Internal
_hx_classes["python.internal.Internal"] = python_internal_Internal


class HxString:
	_hx_class_name = "HxString"
	_hx_statics = ["split", "charCodeAt", "charAt", "lastIndexOf", "toUpperCase", "toLowerCase", "indexOf", "toString", "get_length", "fromCharCode", "substring", "substr"]

	@staticmethod
	def split(s,d):
		# /opt/haxe-git/std/python/internal/StringImpl.hx:31
		if (d == ""):
			return list(s)
		else:
			return s.split(d)

	@staticmethod
	def charCodeAt(s,index):
		# /opt/haxe-git/std/python/internal/StringImpl.hx:37
		if ((((s is None) or ((len(s) == 0))) or ((index < 0))) or ((index >= len(s)))):
			return None
		else:
			return ord(s[index])

	@staticmethod
	def charAt(s,index):
		# /opt/haxe-git/std/python/internal/StringImpl.hx:43
		if ((index < 0) or ((index >= len(s)))):
			return ""
		else:
			return s[index]

	@staticmethod
	def lastIndexOf(s,_hx_str,startIndex = None):
		# /opt/haxe-git/std/python/internal/StringImpl.hx:48
		if (startIndex is None):
			return s.rfind(_hx_str, 0, len(s))
		else:
			# /opt/haxe-git/std/python/internal/StringImpl.hx:52
			i = s.rfind(_hx_str, 0, (startIndex + 1))
			# /opt/haxe-git/std/python/internal/StringImpl.hx:53
			startLeft = None
			if (i == -1):
				startLeft = max(0,((startIndex + 1) - len(_hx_str)))
			else:
				startLeft = (i + 1)
			# /opt/haxe-git/std/python/internal/StringImpl.hx:54
			check = s.find(_hx_str, startLeft, len(s))
			# /opt/haxe-git/std/python/internal/StringImpl.hx:55
			if ((check > i) and ((check <= startIndex))):
				return check
			else:
				return i

	@staticmethod
	def toUpperCase(s):
		# /opt/haxe-git/std/python/internal/StringImpl.hx:65
		return s.upper()

	@staticmethod
	def toLowerCase(s):
		# /opt/haxe-git/std/python/internal/StringImpl.hx:69
		return s.lower()

	@staticmethod
	def indexOf(s,_hx_str,startIndex = None):
		# /opt/haxe-git/std/python/internal/StringImpl.hx:73
		if (startIndex is None):
			return s.find(_hx_str)
		else:
			return s.find(_hx_str, startIndex)

	@staticmethod
	def toString(s):
		# /opt/haxe-git/std/python/internal/StringImpl.hx:80
		return s

	@staticmethod
	def get_length(s):
		# /opt/haxe-git/std/python/internal/StringImpl.hx:84
		return len(s)

	@staticmethod
	def fromCharCode(code):
		# /opt/haxe-git/std/python/internal/StringImpl.hx:91
		return "".join(map(chr,[code]))

	@staticmethod
	def substring(s,startIndex,endIndex = None):
		# /opt/haxe-git/std/python/internal/StringImpl.hx:96
		if (startIndex < 0):
			startIndex = 0
		# /opt/haxe-git/std/python/internal/StringImpl.hx:97
		if (endIndex is None):
			return s[startIndex:]
		else:
			# /opt/haxe-git/std/python/internal/StringImpl.hx:100
			if (endIndex < 0):
				endIndex = 0
			# /opt/haxe-git/std/python/internal/StringImpl.hx:101
			if (endIndex < startIndex):
				return s[endIndex:startIndex]
			else:
				return s[startIndex:endIndex]

	@staticmethod
	def substr(s,startIndex,_hx_len = None):
		# /opt/haxe-git/std/python/internal/StringImpl.hx:112
		if (_hx_len is None):
			return s[startIndex:]
		else:
			# /opt/haxe-git/std/python/internal/StringImpl.hx:115
			if (_hx_len == 0):
				return ""
			# /opt/haxe-git/std/python/internal/StringImpl.hx:116
			return s[startIndex:(startIndex + _hx_len)]
HxString._hx_class = HxString
_hx_classes["HxString"] = HxString


class python_io_NativeInput(haxe_io_Input):
	_hx_class_name = "python.io.NativeInput"
	_hx_fields = ["stream", "wasEof"]
	_hx_methods = ["get_canSeek", "close", "tell", "throwEof", "eof", "readinto", "seek", "readBytes"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = haxe_io_Input


	def __init__(self,s):
		# /opt/haxe-git/std/python/io/NativeInput.hx:32
		self.stream = None
		# /opt/haxe-git/std/python/io/NativeInput.hx:33
		self.wasEof = None
		# /opt/haxe-git/std/python/io/NativeInput.hx:41
		self.canSeek = None
		# /opt/haxe-git/std/python/io/NativeInput.hx:36
		self.stream = s
		# /opt/haxe-git/std/python/io/NativeInput.hx:37
		self.wasEof = False
		# /opt/haxe-git/std/python/io/NativeInput.hx:38
		if (not self.stream.readable()):
			raise _HxException("Write-only stream")

	def get_canSeek(self):
		# /opt/haxe-git/std/python/io/NativeInput.hx:45
		return self.stream.seekable()

	def close(self):
		# /opt/haxe-git/std/python/io/NativeInput.hx:50
		self.stream.close()

	def tell(self):
		# /opt/haxe-git/std/python/io/NativeInput.hx:55
		return self.stream.tell()

	def throwEof(self):
		# /opt/haxe-git/std/python/io/NativeInput.hx:59
		self.wasEof = True
		# /opt/haxe-git/std/python/io/NativeInput.hx:60
		raise _HxException(haxe_io_Eof())

	def eof(self):
		# /opt/haxe-git/std/python/io/NativeInput.hx:64
		return self.wasEof

	def readinto(self,b):
		# /opt/haxe-git/std/python/io/NativeInput.hx:68
		raise _HxException("abstract method, should be overriden")

	def seek(self,p,mode):
		# /opt/haxe-git/std/python/io/NativeInput.hx:72
		raise _HxException("abstract method, should be overriden")

	def readBytes(self,s,pos,_hx_len):
		# /opt/haxe-git/std/python/io/NativeInput.hx:77
		if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > s.length))):
			raise _HxException(haxe_io_Error.OutsideBounds)
		# /opt/haxe-git/std/python/io/NativeInput.hx:81
		if self.get_canSeek():
			self.seek(pos,sys_io_FileSeek.SeekBegin)
		elif (pos > 0):
			raise _HxException((("Cannot call readBytes for pos > 0 (" + Std.string(pos)) + ") on not seekable stream"))
		# /opt/haxe-git/std/python/io/NativeInput.hx:86
		ba = bytearray(_hx_len)
		# /opt/haxe-git/std/python/io/NativeInput.hx:87
		ret = self.readinto(ba)
		# /opt/haxe-git/std/python/io/NativeInput.hx:88
		s.blit(pos,haxe_io_Bytes.ofData(ba),0,_hx_len)
		# /opt/haxe-git/std/python/io/NativeInput.hx:89
		if (ret == 0):
			self.throwEof()
		# /opt/haxe-git/std/python/io/NativeInput.hx:91
		return ret

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.stream = None
		_hx_o.wasEof = None
python_io_NativeInput._hx_class = python_io_NativeInput
_hx_classes["python.io.NativeInput"] = python_io_NativeInput


class python_io_IInput:
	_hx_class_name = "python.io.IInput"
	_hx_fields = ["bigEndian"]
	_hx_methods = ["set_bigEndian", "readByte", "readBytes", "close", "readAll", "readFullBytes", "read", "readUntil", "readLine", "readFloat", "readDouble", "readInt8", "readInt16", "readUInt16", "readInt24", "readUInt24", "readInt32", "readString"]
python_io_IInput._hx_class = python_io_IInput
_hx_classes["python.io.IInput"] = python_io_IInput


class python_io_NativeBytesInput(python_io_NativeInput):
	_hx_class_name = "python.io.NativeBytesInput"
	_hx_fields = []
	_hx_methods = ["readByte", "seek", "readinto"]
	_hx_statics = []
	_hx_interfaces = [python_io_IInput]
	_hx_super = python_io_NativeInput


	def __init__(self,stream):
		# /opt/haxe-git/std/python/io/NativeBytesInput.hx:38
		super().__init__(stream)

	def readByte(self):
		# /opt/haxe-git/std/python/io/NativeBytesInput.hx:45
		ret = self.stream.read(1)
		# /opt/haxe-git/std/python/io/NativeBytesInput.hx:47
		if (len(ret) == 0):
			self.throwEof()
		# /opt/haxe-git/std/python/io/NativeBytesInput.hx:49
		return ret[0]

	def seek(self,p,pos):
		# /opt/haxe-git/std/python/io/NativeBytesInput.hx:54
		self.wasEof = False
		# /opt/haxe-git/std/python/io/NativeBytesInput.hx:55
		python_io_IoTools.seekInBinaryMode(self.stream,p,pos)
		return

	def readinto(self,b):
		# /opt/haxe-git/std/python/io/NativeBytesInput.hx:59
		return self.stream.readinto(b)

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
python_io_NativeBytesInput._hx_class = python_io_NativeBytesInput
_hx_classes["python.io.NativeBytesInput"] = python_io_NativeBytesInput


class python_io_IFileInput:
	_hx_class_name = "python.io.IFileInput"
	_hx_methods = ["seek", "tell", "eof"]
	_hx_interfaces = [python_io_IInput]
python_io_IFileInput._hx_class = python_io_IFileInput
_hx_classes["python.io.IFileInput"] = python_io_IFileInput


class python_io_FileBytesInput(python_io_NativeBytesInput):
	_hx_class_name = "python.io.FileBytesInput"
	_hx_fields = []
	_hx_methods = []
	_hx_statics = []
	_hx_interfaces = [python_io_IFileInput]
	_hx_super = python_io_NativeBytesInput


	def __init__(self,stream):
		# /opt/haxe-git/std/python/io/FileBytesInput.hx:32
		super().__init__(stream)
python_io_FileBytesInput._hx_class = python_io_FileBytesInput
_hx_classes["python.io.FileBytesInput"] = python_io_FileBytesInput


class python_io_NativeOutput(haxe_io_Output):
	_hx_class_name = "python.io.NativeOutput"
	_hx_fields = ["stream"]
	_hx_methods = ["close", "get_canSeek", "prepare", "flush", "tell"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = haxe_io_Output


	def __init__(self,stream):
		# /opt/haxe-git/std/python/io/NativeOutput.hx:31
		self.stream = None
		# /opt/haxe-git/std/python/io/NativeOutput.hx:33
		self.canSeek = None
		# /opt/haxe-git/std/python/io/NativeOutput.hx:36
		self.stream = stream
		# /opt/haxe-git/std/python/io/NativeOutput.hx:37
		if (not stream.writable()):
			raise _HxException("Read only stream")

	def close(self):
		# /opt/haxe-git/std/python/io/NativeOutput.hx:42
		self.stream.close()

	def get_canSeek(self):
		# /opt/haxe-git/std/python/io/NativeOutput.hx:47
		return self.stream.seekable()

	def prepare(self,nbytes):
		# /opt/haxe-git/std/python/io/NativeOutput.hx:52
		self.stream.truncate(nbytes)

	def flush(self):
		# /opt/haxe-git/std/python/io/NativeOutput.hx:57
		self.stream.flush()

	def tell(self):
		# /opt/haxe-git/std/python/io/NativeOutput.hx:63
		return self.stream.tell()

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.stream = None
python_io_NativeOutput._hx_class = python_io_NativeOutput
_hx_classes["python.io.NativeOutput"] = python_io_NativeOutput


class python_io_NativeBytesOutput(python_io_NativeOutput):
	_hx_class_name = "python.io.NativeBytesOutput"
	_hx_fields = []
	_hx_methods = ["seek", "prepare", "writeByte"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = python_io_NativeOutput


	def __init__(self,stream):
		# /opt/haxe-git/std/python/io/NativeBytesOutput.hx:33
		super().__init__(stream)

	def seek(self,p,pos):
		# /opt/haxe-git/std/python/io/NativeBytesOutput.hx:38
		python_io_IoTools.seekInBinaryMode(self.stream,p,pos)
		return

	def prepare(self,nbytes):
		# /opt/haxe-git/std/python/io/NativeBytesOutput.hx:43
		self.stream.truncate(nbytes)

	def writeByte(self,c):
		# /opt/haxe-git/std/python/io/NativeBytesOutput.hx:48
		self.stream.write(bytearray([c]))

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
python_io_NativeBytesOutput._hx_class = python_io_NativeBytesOutput
_hx_classes["python.io.NativeBytesOutput"] = python_io_NativeBytesOutput


class python_io_IOutput:
	_hx_class_name = "python.io.IOutput"
	_hx_fields = ["bigEndian"]
	_hx_methods = ["set_bigEndian", "writeByte", "writeBytes", "flush", "close", "write", "writeFullBytes", "writeFloat", "writeDouble", "writeInt8", "writeInt16", "writeUInt16", "writeInt24", "writeUInt24", "writeInt32", "prepare", "writeInput", "writeString"]
python_io_IOutput._hx_class = python_io_IOutput
_hx_classes["python.io.IOutput"] = python_io_IOutput


class python_io_IFileOutput:
	_hx_class_name = "python.io.IFileOutput"
	_hx_methods = ["seek", "tell"]
	_hx_interfaces = [python_io_IOutput]
python_io_IFileOutput._hx_class = python_io_IFileOutput
_hx_classes["python.io.IFileOutput"] = python_io_IFileOutput


class python_io_FileBytesOutput(python_io_NativeBytesOutput):
	_hx_class_name = "python.io.FileBytesOutput"
	_hx_fields = []
	_hx_methods = []
	_hx_statics = []
	_hx_interfaces = [python_io_IFileOutput]
	_hx_super = python_io_NativeBytesOutput


	def __init__(self,stream):
		# /opt/haxe-git/std/python/io/FileBytesOutput.hx:30
		super().__init__(stream)
python_io_FileBytesOutput._hx_class = python_io_FileBytesOutput
_hx_classes["python.io.FileBytesOutput"] = python_io_FileBytesOutput


class python_io_NativeTextInput(python_io_NativeInput):
	_hx_class_name = "python.io.NativeTextInput"
	_hx_fields = []
	_hx_methods = ["readByte", "seek", "readinto"]
	_hx_statics = []
	_hx_interfaces = [python_io_IInput]
	_hx_super = python_io_NativeInput


	def __init__(self,stream):
		# /opt/haxe-git/std/python/io/NativeTextInput.hx:39
		super().__init__(stream)

	def readByte(self):
		# /opt/haxe-git/std/python/io/NativeTextInput.hx:44
		ret = self.stream.read(1)
		# /opt/haxe-git/std/python/io/NativeTextInput.hx:46
		if (len(ret) == 0):
			self.throwEof()
		# /opt/haxe-git/std/python/io/NativeTextInput.hx:48
		return HxString.charCodeAt(ret,0)

	def seek(self,p,pos):
		# /opt/haxe-git/std/python/io/NativeTextInput.hx:53
		self.wasEof = False
		# /opt/haxe-git/std/python/io/NativeTextInput.hx:54
		python_io_IoTools.seekInTextMode(self.stream,self.tell,p,pos)

	def readinto(self,b):
		# /opt/haxe-git/std/python/io/NativeTextInput.hx:58
		return self.stream.buffer.readinto(b)

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
python_io_NativeTextInput._hx_class = python_io_NativeTextInput
_hx_classes["python.io.NativeTextInput"] = python_io_NativeTextInput


class python_io_FileTextInput(python_io_NativeTextInput):
	_hx_class_name = "python.io.FileTextInput"
	_hx_fields = []
	_hx_methods = []
	_hx_statics = []
	_hx_interfaces = [python_io_IFileInput]
	_hx_super = python_io_NativeTextInput


	def __init__(self,stream):
		# /opt/haxe-git/std/python/io/FileTextInput.hx:32
		super().__init__(stream)
python_io_FileTextInput._hx_class = python_io_FileTextInput
_hx_classes["python.io.FileTextInput"] = python_io_FileTextInput


class python_io_NativeTextOutput(python_io_NativeOutput):
	_hx_class_name = "python.io.NativeTextOutput"
	_hx_fields = []
	_hx_methods = ["seek", "writeByte"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = python_io_NativeOutput


	def __init__(self,stream):
		# /opt/haxe-git/std/python/io/NativeTextOutput.hx:34
		super().__init__(stream)
		# /opt/haxe-git/std/python/io/NativeTextOutput.hx:35
		if (not stream.writable()):
			raise _HxException("Read only stream")

	def seek(self,p,pos):
		# /opt/haxe-git/std/python/io/NativeTextOutput.hx:40
		python_io_IoTools.seekInTextMode(self.stream,self.tell,p,pos)

	def writeByte(self,c):
		# /opt/haxe-git/std/python/io/NativeTextOutput.hx:45
		self.stream.write("".join(map(chr,[c])))

	@staticmethod
	def _hx_empty_init(_hx_o):		pass
python_io_NativeTextOutput._hx_class = python_io_NativeTextOutput
_hx_classes["python.io.NativeTextOutput"] = python_io_NativeTextOutput


class python_io_FileTextOutput(python_io_NativeTextOutput):
	_hx_class_name = "python.io.FileTextOutput"
	_hx_fields = []
	_hx_methods = []
	_hx_statics = []
	_hx_interfaces = [python_io_IFileOutput]
	_hx_super = python_io_NativeTextOutput


	def __init__(self,stream):
		# /opt/haxe-git/std/python/io/FileTextOutput.hx:30
		super().__init__(stream)
python_io_FileTextOutput._hx_class = python_io_FileTextOutput
_hx_classes["python.io.FileTextOutput"] = python_io_FileTextOutput


class python_io_IoTools:
	_hx_class_name = "python.io.IoTools"
	_hx_statics = ["createFileInputFromText", "createFileInputFromBytes", "createFileOutputFromText", "createFileOutputFromBytes", "seekInTextMode", "seekInBinaryMode"]

	@staticmethod
	def createFileInputFromText(t):
		# /opt/haxe-git/std/python/io/IoTools.hx:39
		return sys_io_FileInput(python_io_FileTextInput(t))

	@staticmethod
	def createFileInputFromBytes(t):
		# /opt/haxe-git/std/python/io/IoTools.hx:43
		return sys_io_FileInput(python_io_FileBytesInput(t))

	@staticmethod
	def createFileOutputFromText(t):
		# /opt/haxe-git/std/python/io/IoTools.hx:47
		return sys_io_FileOutput(python_io_FileTextOutput(t))

	@staticmethod
	def createFileOutputFromBytes(t):
		# /opt/haxe-git/std/python/io/IoTools.hx:51
		return sys_io_FileOutput(python_io_FileBytesOutput(t))

	@staticmethod
	def seekInTextMode(stream,tell,p,pos):
		# /opt/haxe-git/std/python/io/IoTools.hx:56
		pos1 = None
		# /opt/haxe-git/std/python/io/IoTools.hx:58
		if ((pos.index) == 0):
			pos1 = 0
		elif ((pos.index) == 1):
			# /opt/haxe-git/std/python/io/IoTools.hx:60
			p = (tell() + p)
			# /opt/haxe-git/std/python/io/IoTools.hx:61
			pos1 = 0
		elif ((pos.index) == 2):
			# /opt/haxe-git/std/python/io/IoTools.hx:63
			stream.seek(0,2)
			# /opt/haxe-git/std/python/io/IoTools.hx:64
			p = (tell() + p)
			# /opt/haxe-git/std/python/io/IoTools.hx:65
			pos1 = 0
		else:
			pass
		# /opt/haxe-git/std/python/io/IoTools.hx:68
		stream.seek(p,pos1)

	@staticmethod
	def seekInBinaryMode(stream,p,pos):
		# /opt/haxe-git/std/python/io/IoTools.hx:73
		pos1 = None
		# /opt/haxe-git/std/python/io/IoTools.hx:75
		if ((pos.index) == 0):
			pos1 = 0
		elif ((pos.index) == 1):
			pos1 = 1
		elif ((pos.index) == 2):
			pos1 = 2
		else:
			pass
		# /opt/haxe-git/std/python/io/IoTools.hx:79
		stream.seek(p,pos1)
python_io_IoTools._hx_class = python_io_IoTools
_hx_classes["python.io.IoTools"] = python_io_IoTools


class python_lib__Re_Choice_Impl_:
	_hx_class_name = "python.lib._Re.Choice_Impl_"
	_hx_statics = ["fromA", "fromB"]

	@staticmethod
	def fromA(x):
		# /opt/haxe-git/std/python/lib/Re.hx:28
		return x

	@staticmethod
	def fromB(x):
		# /opt/haxe-git/std/python/lib/Re.hx:29
		return x
python_lib__Re_Choice_Impl_._hx_class = python_lib__Re_Choice_Impl_
_hx_classes["python.lib._Re.Choice_Impl_"] = python_lib__Re_Choice_Impl_


class python_lib__Re_RegexHelper:
	_hx_class_name = "python.lib._Re.RegexHelper"
	_hx_statics = ["findallDynamic"]

	@staticmethod
	def findallDynamic(r,string,pos = None,endpos = None):
		# /opt/haxe-git/std/python/lib/Re.hx:85
		if (endpos is None):
			if (pos is None):
				return r.findall(string)
			else:
				return r.findall(string,pos)
		else:
			return r.findall(string,pos,endpos)
python_lib__Re_RegexHelper._hx_class = python_lib__Re_RegexHelper
_hx_classes["python.lib._Re.RegexHelper"] = python_lib__Re_RegexHelper


class sys_io_File:
	_hx_class_name = "sys.io.File"
	_hx_statics = ["getContent", "saveContent", "getBytes", "saveBytes", "read", "write", "append", "copy"]

	@staticmethod
	def getContent(path):
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:37
		f = python_lib_Builtins.open(path,"r",-1,"utf-8",None,"")
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:38
		content = f.read(-1)
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:39
		f.close()
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:40
		return content

	@staticmethod
	def saveContent(path,content):
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:44
		f = python_lib_Builtins.open(path,"w",-1,"utf-8",None,"")
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:45
		f.write(content)
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:46
		f.close()

	@staticmethod
	def getBytes(path):
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:50
		f = python_lib_Builtins.open(path,"rb",-1)
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:51
		size = f.read(-1)
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:52
		b = haxe_io_Bytes.ofData(size)
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:53
		f.close()
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:54
		return b

	@staticmethod
	def saveBytes(path,_hx_bytes):
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:58
		f = python_lib_Builtins.open(path,"wb",-1)
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:59
		f.write(_hx_bytes.b)
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:60
		f.close()

	@staticmethod
	def read(path,binary = True):
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:63
		if (binary is None):
			binary = True
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:64
		mode = None
		if binary:
			mode = "rb"
		else:
			mode = "r"
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:66
		f = python_lib_Builtins.open(path,mode,-1,None,None,(None if binary else ""))
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:68
		if binary:
			return python_io_IoTools.createFileInputFromBytes(f)
		else:
			return python_io_IoTools.createFileInputFromText(f)

	@staticmethod
	def write(path,binary = True):
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:71
		if (binary is None):
			binary = True
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:72
		mode = None
		if binary:
			mode = "wb"
		else:
			mode = "w"
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:73
		f = python_lib_Builtins.open(path,mode,-1,None,None,(None if binary else ""))
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:75
		if binary:
			return python_io_IoTools.createFileOutputFromBytes(f)
		else:
			return python_io_IoTools.createFileOutputFromText(f)

	@staticmethod
	def append(path,binary = True):
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:78
		if (binary is None):
			binary = True
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:79
		mode = None
		if binary:
			mode = "ab"
		else:
			mode = "a"
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:80
		f = python_lib_Builtins.open(path,mode,-1,None,None,(None if binary else ""))
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:82
		if binary:
			return python_io_IoTools.createFileOutputFromBytes(f)
		else:
			return python_io_IoTools.createFileOutputFromText(f)

	@staticmethod
	def copy(srcPath,dstPath):
		# /opt/haxe-git/std/python/_std/sys/io/File.hx:87
		python_lib_Shutil.copy(srcPath,dstPath)
		return
sys_io_File._hx_class = sys_io_File
_hx_classes["sys.io.File"] = sys_io_File


class sys_io_FileInput(haxe_io_Input):
	_hx_class_name = "sys.io.FileInput"
	_hx_fields = ["impl"]
	_hx_methods = ["set_bigEndian", "seek", "tell", "eof", "readByte", "readBytes", "close", "readAll", "readFullBytes", "read", "readUntil", "readLine", "readFloat", "readDouble", "readInt8", "readInt16", "readUInt16", "readInt24", "readUInt24", "readInt32", "readString"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = haxe_io_Input


	def __init__(self,impl):
		# /opt/haxe-git/std/python/_std/sys/io/FileInput.hx:32
		self.impl = None
		# /opt/haxe-git/std/python/_std/sys/io/FileInput.hx:37
		self.impl = impl

	def set_bigEndian(self,b):
		# /opt/haxe-git/std/python/_std/sys/io/FileInput.hx:41
		return self.impl.set_bigEndian(b)

	def seek(self,p,pos):
		# /opt/haxe-git/std/python/_std/sys/io/FileInput.hx:45
		self.impl.seek(p,pos)
		return

	def tell(self):
		# /opt/haxe-git/std/python/_std/sys/io/FileInput.hx:48
		return self.impl.tell()

	def eof(self):
		# /opt/haxe-git/std/python/_std/sys/io/FileInput.hx:51
		return self.impl.eof()

	def readByte(self):
		# /opt/haxe-git/std/python/_std/sys/io/FileInput.hx:55
		return self.impl.readByte()

	def readBytes(self,s,pos,_hx_len):
		# /opt/haxe-git/std/python/_std/sys/io/FileInput.hx:59
		return self.impl.readBytes(s,pos,_hx_len)

	def close(self):
		# /opt/haxe-git/std/python/_std/sys/io/FileInput.hx:63
		self.impl.close()

	def readAll(self,bufsize = None):
		# /opt/haxe-git/std/python/_std/sys/io/FileInput.hx:67
		return self.impl.readAll(bufsize)

	def readFullBytes(self,s,pos,_hx_len):
		# /opt/haxe-git/std/python/_std/sys/io/FileInput.hx:71
		self.impl.readFullBytes(s,pos,_hx_len)

	def read(self,nbytes):
		# /opt/haxe-git/std/python/_std/sys/io/FileInput.hx:75
		return self.impl.read(nbytes)

	def readUntil(self,end):
		# /opt/haxe-git/std/python/_std/sys/io/FileInput.hx:79
		return self.impl.readUntil(end)

	def readLine(self):
		# /opt/haxe-git/std/python/_std/sys/io/FileInput.hx:83
		return self.impl.readLine()

	def readFloat(self):
		# /opt/haxe-git/std/python/_std/sys/io/FileInput.hx:87
		return self.impl.readFloat()

	def readDouble(self):
		# /opt/haxe-git/std/python/_std/sys/io/FileInput.hx:91
		return self.impl.readDouble()

	def readInt8(self):
		# /opt/haxe-git/std/python/_std/sys/io/FileInput.hx:95
		return self.impl.readInt8()

	def readInt16(self):
		# /opt/haxe-git/std/python/_std/sys/io/FileInput.hx:99
		return self.impl.readInt16()

	def readUInt16(self):
		# /opt/haxe-git/std/python/_std/sys/io/FileInput.hx:103
		return self.impl.readUInt16()

	def readInt24(self):
		# /opt/haxe-git/std/python/_std/sys/io/FileInput.hx:107
		return self.impl.readInt24()

	def readUInt24(self):
		# /opt/haxe-git/std/python/_std/sys/io/FileInput.hx:111
		return self.impl.readUInt24()

	def readInt32(self):
		# /opt/haxe-git/std/python/_std/sys/io/FileInput.hx:115
		return self.impl.readInt32()

	def readString(self,_hx_len):
		# /opt/haxe-git/std/python/_std/sys/io/FileInput.hx:119
		return self.impl.readString(_hx_len)

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.impl = None
sys_io_FileInput._hx_class = sys_io_FileInput
_hx_classes["sys.io.FileInput"] = sys_io_FileInput


class sys_io_FileOutput(haxe_io_Output):
	_hx_class_name = "sys.io.FileOutput"
	_hx_fields = ["impl"]
	_hx_methods = ["seek", "tell", "set_bigEndian", "writeByte", "writeBytes", "flush", "close", "write", "writeFullBytes", "writeFloat", "writeDouble", "writeInt8", "writeInt16", "writeUInt16", "writeInt24", "writeUInt24", "writeInt32", "prepare", "writeInput", "writeString"]
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = haxe_io_Output


	def __init__(self,impl):
		# /opt/haxe-git/std/python/_std/sys/io/FileOutput.hx:31
		self.impl = None
		# /opt/haxe-git/std/python/_std/sys/io/FileOutput.hx:34
		self.impl = impl

	def seek(self,p,pos):
		# /opt/haxe-git/std/python/_std/sys/io/FileOutput.hx:38
		self.impl.seek(p,pos)
		return

	def tell(self):
		# /opt/haxe-git/std/python/_std/sys/io/FileOutput.hx:42
		return self.impl.tell()

	def set_bigEndian(self,b):
		# /opt/haxe-git/std/python/_std/sys/io/FileOutput.hx:46
		return self.impl.set_bigEndian(b)

	def writeByte(self,c):
		# /opt/haxe-git/std/python/_std/sys/io/FileOutput.hx:50
		self.impl.writeByte(c)

	def writeBytes(self,s,pos,_hx_len):
		# /opt/haxe-git/std/python/_std/sys/io/FileOutput.hx:54
		return self.impl.writeBytes(s,pos,_hx_len)

	def flush(self):
		# /opt/haxe-git/std/python/_std/sys/io/FileOutput.hx:58
		self.impl.flush()

	def close(self):
		# /opt/haxe-git/std/python/_std/sys/io/FileOutput.hx:62
		self.impl.close()

	def write(self,s):
		# /opt/haxe-git/std/python/_std/sys/io/FileOutput.hx:66
		self.impl.write(s)

	def writeFullBytes(self,s,pos,_hx_len):
		# /opt/haxe-git/std/python/_std/sys/io/FileOutput.hx:70
		self.impl.writeFullBytes(s,pos,_hx_len)

	def writeFloat(self,x):
		# /opt/haxe-git/std/python/_std/sys/io/FileOutput.hx:74
		self.impl.writeFloat(x)

	def writeDouble(self,x):
		# /opt/haxe-git/std/python/_std/sys/io/FileOutput.hx:78
		self.impl.writeDouble(x)

	def writeInt8(self,x):
		# /opt/haxe-git/std/python/_std/sys/io/FileOutput.hx:82
		self.impl.writeInt8(x)

	def writeInt16(self,x):
		# /opt/haxe-git/std/python/_std/sys/io/FileOutput.hx:86
		self.impl.writeInt16(x)

	def writeUInt16(self,x):
		# /opt/haxe-git/std/python/_std/sys/io/FileOutput.hx:90
		self.impl.writeUInt16(x)

	def writeInt24(self,x):
		# /opt/haxe-git/std/python/_std/sys/io/FileOutput.hx:94
		self.impl.writeInt24(x)

	def writeUInt24(self,x):
		# /opt/haxe-git/std/python/_std/sys/io/FileOutput.hx:98
		self.impl.writeUInt24(x)

	def writeInt32(self,x):
		# /opt/haxe-git/std/python/_std/sys/io/FileOutput.hx:102
		self.impl.writeInt32(x)

	def prepare(self,nbytes):
		# /opt/haxe-git/std/python/_std/sys/io/FileOutput.hx:106
		self.impl.prepare(nbytes)

	def writeInput(self,i,bufsize = None):
		# /opt/haxe-git/std/python/_std/sys/io/FileOutput.hx:110
		self.impl.writeInput(i,bufsize)

	def writeString(self,s):
		# /opt/haxe-git/std/python/_std/sys/io/FileOutput.hx:114
		self.impl.writeString(s)

	@staticmethod
	def _hx_empty_init(_hx_o):
		_hx_o.impl = None
sys_io_FileOutput._hx_class = sys_io_FileOutput
_hx_classes["sys.io.FileOutput"] = sys_io_FileOutput

class sys_io_FileSeek(Enum):
	_hx_class_name = "sys.io.FileSeek"
	_hx_constructs = ["SeekBegin", "SeekCur", "SeekEnd"]
sys_io_FileSeek.SeekBegin = sys_io_FileSeek("SeekBegin", 0, list())
sys_io_FileSeek.SeekCur = sys_io_FileSeek("SeekCur", 1, list())
sys_io_FileSeek.SeekEnd = sys_io_FileSeek("SeekEnd", 2, list())
sys_io_FileSeek._hx_class = sys_io_FileSeek
_hx_classes["sys.io.FileSeek"] = sys_io_FileSeek

# /opt/haxe-git/std/python/_std/Math.hx:135
Math.NEGATIVE_INFINITY = float("-inf")
# /opt/haxe-git/std/python/_std/Math.hx:136
Math.POSITIVE_INFINITY = float("inf")
# /opt/haxe-git/std/python/_std/Math.hx:137
Math.NaN = float("nan")
# /opt/haxe-git/std/python/_std/Math.hx:138
Math.PI = python_lib_Math.pi

python_Boot.keywords = set(["and", "del", "from", "not", "with", "as", "elif", "global", "or", "yield", "assert", "else", "if", "pass", "None", "break", "except", "import", "raise", "True", "class", "exec", "in", "return", "False", "continue", "finally", "is", "try", "def", "for", "lambda", "while"])
python_Boot.prefixLength = len("_hx_")
Date.EPOCH_UTC = python_lib_datetime_Datetime.fromtimestamp(0,python_lib_datetime_Timezone.utc)
Date.EPOCH_LOCAL = python_lib_datetime_Datetime.fromtimestamp(0)
def _hx_init_Sys_environ():
	# /opt/haxe-git/std/python/_std/Sys.hx:30
	def _hx_local_0():
		# /opt/haxe-git/std/python/_std/Sys.hx:31
		Sys.environ = haxe_ds_StringMap()
		# /opt/haxe-git/std/python/_std/Sys.hx:33
		env = python_lib_Os.environ
		# /opt/haxe-git/std/python/_std/Sys.hx:35
		def _hx_local_1():
			# /opt/haxe-git/std/python/_std/Sys.hx:35
			_this = env.keys()
			def _hx_local_3():
				def _hx_local_2():
					this1 = iter(_this)
					return python_HaxeIterator(this1)
				return _hx_local_2()
			return _hx_local_3()
		_hx_local_4 = _hx_local_1()
		while _hx_local_4.hasNext():
			key = _hx_local_4.next()
			# /opt/haxe-git/std/python/_std/Sys.hx:36
			value = env.get(key,None)
			Sys.environ.h[key] = value
		# /opt/haxe-git/std/python/_std/Sys.hx:38
		return Sys.environ
	return _hx_local_0()
Sys.environ = _hx_init_Sys_environ()
haxe_Unserializer.DEFAULT_RESOLVER = Type
haxe_Unserializer.BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789%:"
haxe_Unserializer.CODES = None
def _hx_init_haxe_io_FPHelper_i64tmp():
	# /opt/haxe-git/std/haxe/io/FPHelper.hx:35
	def _hx_local_0():
		# /opt/haxe-git/std/haxe/io/FPHelper.hx:35
		x = haxe__Int64____Int64(0, 0)
		return x
	return _hx_local_0()
haxe_io_FPHelper.i64tmp = _hx_init_haxe_io_FPHelper_i64tmp()
haxe_io_FPHelper.LN2 = 0.6931471805599453
hxsublime_Config.target_packages = ["python", "flash", "neko", "js", "php", "cpp", "cs", "java", "sys"]
hxsublime_Config.targets = ["js", "cpp", "swf", "neko", "php", "java", "cs", "as3", "python"]
def _hx_init_hxsublime_Config_target_std_packages():
	# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Config.hx:10
	def _hx_local_0():
		# /home/frabbit/github/haxe-sublime-plugin-hx/src/hxsublime/Config.hx:10
		_g = haxe_ds_StringMap()
		_g.h["js"] = ["js"]
		_g.h["cpp"] = ["cpp", "sys"]
		_g.h["neko"] = ["neko", "sys"]
		_g.h["php"] = ["php", "sys"]
		_g.h["python"] = ["python", "sys"]
		_g.h["java"] = ["java", "sys"]
		_g.h["cs"] = ["cs", "sys"]
		_g.h["swf"] = ["flash"]
		_g.h["as3"] = ["flash"]
		return _g
	return _hx_local_0()
hxsublime_Config.target_std_packages = _hx_init_hxsublime_Config_target_std_packages()
hxsublime_Config.ignored_folders_list = [".git", ".svn"]
hxsublime_Config.ignored_folders = hxsublime_Config.mk_ignored_folders()
hxsublime_Config.ignored_packages_list = ["neko._std", "cpp._std", "php._std", "js._std", "flash._std", "python._std", "java._std", "cs._std"]
hxsublime_Config.ignored_packages = hxsublime_Config.mk_ignored_packages()
hxsublime_Config.ignored_types = ["haxe.io.BytesData.Unsigned_char__"]
hxsublime_Config.nme_targets = [hxsublime_NmeTarget("Flash", "flash", ["-debug"]), hxsublime_NmeTarget("HTML5", "html5", ["-debug"]), hxsublime_NmeTarget("C++", "cpp", ["-debug"]), hxsublime_NmeTarget("Windows", "windows", ["-debug"]), hxsublime_NmeTarget("Mac", "mac", ["-debug"]), hxsublime_NmeTarget("Linux", "linux", ["-debug"]), hxsublime_NmeTarget("Linux 64", "linux", ["-64 -debug"]), hxsublime_NmeTarget("iOs - iPhone simulator", "ios", ["-simulator -debug"]), hxsublime_NmeTarget("iOs - iPad simulator", "ios", ["-simulator -ipad -debug"]), hxsublime_NmeTarget("iOs - update XCode project", "ios", ["-ipad -debug"]), hxsublime_NmeTarget("Neko", "neko", ["-debug"]), hxsublime_NmeTarget("Neko 64", "neko", ["-64 -debug"]), hxsublime_NmeTarget("WebOs", "webos", ["-debug"]), hxsublime_NmeTarget("BlackBerry", "blackberry", ["-debug"]), hxsublime_NmeTarget("Android", "android", ["-debug"])]
hxsublime_Config.openfl_targets = [hxsublime_OpenFlTarget("Flash", "flash", ["-debug"]), hxsublime_OpenFlTarget("HTML5", "html5", ["-debug"]), hxsublime_OpenFlTarget("C++", "cpp", ["-debug"]), hxsublime_OpenFlTarget("Windows", "windows", ["-debug"]), hxsublime_OpenFlTarget("Mac", "mac", ["-debug"]), hxsublime_OpenFlTarget("Linux", "linux", ["-debug"]), hxsublime_OpenFlTarget("Linux 64", "linux", ["-64 -debug"]), hxsublime_OpenFlTarget("iOs - iPhone simulator", "ios", ["-simulator -debug"]), hxsublime_OpenFlTarget("iOs - iPad simulator", "ios", ["-simulator -ipad -debug"]), hxsublime_OpenFlTarget("iOs - update XCode project", "ios", ["-ipad -debug"]), hxsublime_OpenFlTarget("Neko", "neko", ["-debug"]), hxsublime_OpenFlTarget("Neko 64", "neko", ["-64 -debug"]), hxsublime_OpenFlTarget("Emscripten", "emscripten", ["-debug"]), hxsublime_OpenFlTarget("WebOs", "webos", ["-debug"]), hxsublime_OpenFlTarget("BlackBerry", "blackberry", ["-debug"]), hxsublime_OpenFlTarget("Android", "android", ["-debug"])]
hxsublime_Config.SOURCE_HAXE = "source.haxe.2"
hxsublime_Config.SOURCE_HXML = "source.hxml"
hxsublime_Config.SOURCE_NMML = "source.nmml"
hxsublime_Config.SOURCE_ERAZOR = "source.erazor"
hxsublime_Config.HXSL_SUFFIX = ".hxsl"
hxsublime_HaxeLibManager.__meta__ = _hx_AnonObject({'fields': _hx_AnonObject({'available': _hx_AnonObject({'property': None})})})
hxsublime_HaxeLibManager.libLine = python_lib_Re.compile("([^:]*):[^\\[]*\\[(dev\\:)?(.*)\\]")
hxsublime_Plugin._startupInfo = None
hxsublime_Types.validPackageRegex = python_lib_Re.compile("^[_a-z][a-zA-Z0-9_]*$")
hxsublime_Types.fileTypeCache = haxe_ds_StringMap()
hxsublime_build_NmeBuild.__meta__ = _hx_AnonObject({'fields': _hx_AnonObject({'title': _hx_AnonObject({'property': None}), 'buildFile': _hx_AnonObject({'property': None}), 'target': _hx_AnonObject({'property': None}), 'plattform': _hx_AnonObject({'property': None}), 'stdBundle': _hx_AnonObject({'property': None})})})
hxsublime_build_Tools._extract_tag = python_lib_Re.compile("<([a-z0-9_-]+).*?\\s(name|main|title|file)=\"([ a-z0-9_./-]+)\"",python_lib_Re.I)
hxsublime_commands__Completion_Helper.anonFunc = python_lib_Re.compile("^function(\\s+[a-zA-Z0-9$_]*\\s+)?\\s*\\($")
hxsublime_commands__CreateType_State.current_create_type_info = haxe_ds_StringMap()
hxsublime_commands__FindDeclaration_State.findDeclFile = None
hxsublime_commands__FindDeclaration_State.findDeclPos = None
hxsublime_commands__FindDeclaration_Helper.plugin_path = hxsublime_Plugin.plugin_base_dir()
hxsublime_commands__GotoBase_State._find_decl_file = None
hxsublime_commands__GotoBase_State._find_decl_pos = None
hxsublime_commands__GotoBase_State._init_text = ""
hxsublime_commands__GotoBase_State._is_open = False
hxsublime_compiler_Output.compiler_output = python_lib_Re.compile("^([^:]+):([0-9]+): (?:character(?:s?)|line(?:s?))? ([0-9]+)-?([0-9]+)? : (.*)",python_lib_Re.M)
hxsublime_compiler_Output.no_classes_found = python_lib_Re.compile("^No classes found in .*",python_lib_Re.M)
hxsublime_compiler_Output.no_classes_found_in_trace = python_lib_Re.compile("^No classes found in trace$",python_lib_Re.M)
hxsublime_compiler_Output.haxe_compiler_line = "^([^:]*):([0-9]+): characters? ([0-9]+)-?[0-9]* :(.*)$"
hxsublime_compiler_Output.type_parameter_name = python_lib_Re.compile("^([A-Z][_a-zA-Z0-9]*)")
hxsublime_completion_CompletionListener.triggerId = -1
hxsublime_completion_CompletionListener.id = 0
hxsublime_completion_hx_CompletionContext.controlStructRegex = python_lib_Re.compile("\\s+(if|switch|for|while)\\s*\\($")
hxsublime_completion_hx_TopLevel.TOP_LEVEL_KEYWORDS = [("trace\ttoplevel", "trace"), ("this\ttoplevel", "this"), ("super\ttoplevel", "super")]
hxsublime_completion_hxml_HxmlCompletion.libFlag = python_lib_Re.compile("-lib\\s+(.*?)")
hxsublime_panel_Panels._debugPanels = hxsublime_tools_Cache(haxe_ds_IntMap())
hxsublime_panel_Panels._slidePanels = haxe_ds_IntMap()
hxsublime_project_Project.classpathLineRegex = python_lib_Re.compile("Classpath : (.*)")
hxsublime_project_Project.haxeVersionRegex = python_lib_Re.compile("haxe_([0-9]{3})",python_lib_Re.M)
hxsublime_project_Projects.projects = hxsublime_tools_Cache(haxe_ds_StringMap())
hxsublime_project_Projects.userHome = python_lib_os_Path.expanduser("~")
hxsublime_project_Projects.logFile = python_lib_os_Path.join(hxsublime_project_Projects.userHome,"st3_haxe_log.txt")
hxsublime_project_Projects.nextServerPort = 6000
hxsublime_project_Tools.winStart = "(?:(?:[A-Za-z][:])"
hxsublime_project_Tools.unixStart = "(?:[/]?)"
hxsublime_project_Tools.haxeFileRegex = (((("^(" + HxOverrides.stringOrNull(hxsublime_project_Tools.winStart)) + "|") + HxOverrides.stringOrNull(hxsublime_project_Tools.unixStart)) + ")?(?:[^:]*)):([0-9]+): (?:character(?:s?)|line(?:s?))? ([0-9]+)-?[0-9]*\\s?:(.*)$")
hxsublime_tools_Regex.space_chars = python_lib_Re.compile("\\s")
hxsublime_tools_Regex.word_chars = python_lib_Re.compile("[a-z0-9._]",python_lib_Re.I)
hxsublime_tools_Regex.import_line = python_lib_Re.compile("^([ \t]*)import\\s+([a-z0-9._]+);",(python_lib_Re.I | python_lib_Re.M))
hxsublime_tools_Regex.using_line = python_lib_Re.compile("^([ \t]*)using\\s+([a-z0-9._]+);",(python_lib_Re.I | python_lib_Re.M))
hxsublime_tools_Regex.package_line = python_lib_Re.compile("\\s*package\\s*([a-z0-9.]*)\\s*;",python_lib_Re.I)
hxsublime_tools_Regex.variables = python_lib_Re.compile("var\\s+([^:;\\s]*)",python_lib_Re.I)
hxsublime_tools_Regex.named_functions = python_lib_Re.compile("function\\s+([a-zA-Z0-9_]+)\\s*",python_lib_Re.I)
hxsublime_tools_Regex.function_params = python_lib_Re.compile("function\\s+[a-zA-Z0-9_]+\\s*\\(([^\\)]*)",python_lib_Re.M)
hxsublime_tools_Regex.param_default = python_lib_Re.compile("(=\\s*\"*[^\"]*\")",python_lib_Re.M)
hxsublime_tools_Regex.isType = python_lib_Re.compile("^[A-Z][a-zA-Z0-9_]*$")
hxsublime_tools_Regex.typeDeclWithScope = python_lib_Re.compile("(private\\s+)?(?:extern\\s+)?(class|typedef|enum|interface|abstract)\\s+([A-Z][a-zA-Z0-9_]*)\\s*",python_lib_Re.M)
hxsublime_tools_Regex.comments = python_lib_Re.compile("(//[^\n\r]*?[\n\r]|/\\*(.*?)\\*/)",(python_lib_Re.MULTILINE | python_lib_Re.DOTALL))
hxsublime_tools_Regex.fieldRegex = python_lib_Re.compile("((?:(?:public|static|inline|private)\\s+)*)(var|function)\\s+([a-zA-Z_][a-zA-Z0-9_]*)",python_lib_Re.MULTILINE)
hxsublime_tools_Regex.typeDeclWithScopeRegex = python_lib_Re.compile("(private\\s+)?(extern\\s+)?(class|typedef|enum|interface|abstract)\\s+(:?[A-Z][a-zA-Z0-9_]*)\\s*",python_lib_Re.M)
hxsublime_tools_Regex.enumConstructorStartDecl = python_lib_Re.compile("\\s+([a-zA-Z_]+)",python_lib_Re.M)
hxsublime_tools_StringTools._whitespace = python_lib_Re.compile("^\\s*$")
hxsublime_tools_AsyncEdit.dict = dict()
hxsublime_tools_AsyncEdit.id = 0
hxsublime_tools_HaxeTextEditCommand.COMMAND_ID = "hxsublime_tools__haxe_text_edit"

hxsublime_Main.main()