package hxsublime;

import hxsublime.Plugin;
import python.lib.Os;
import python.lib.os.Path;
import python.lib.Subprocess;
import python.lib.subprocess.Popen;

import python.lib.ThreadLowLevel;
import python.lib.Types;
import sublime.Sublime;

using python.lib.StringTools;

class Execute {
	public static function run_cmd_async(args:Array<String>, callback:String->String->Void, input:String=null, cwd:String=null, env=null)
	{

		function in_thread ()
		{
			var r = run_cmd(args, input, cwd, env);
			var out = r._1, err = r._2;
			Sublime.set_timeout(callback.bind(out, err), 1);
		}

		ThreadLowLevel.start_new_thread(in_thread, Tuple.empty());
	}


	public static function run_cmd( args:Array<String>, input:String=null, cwd:String=null, env:Dict<String,String>=null ):Tup2<String, String>
	{
		if (cwd == null) 
		{
			cwd = ".";
		}

		try 
		{
			var base_env = Os.environ.copy();
			
			if (env != null) 
			{
				base_env.update(env);
			}
			
			var env = base_env;

			//trace(env);

			for (k in env.keys().iter().toHaxeIterator()) 
			{
				var val = env.get(k, null);
				env.set(k, Path.expandvars(val));
			}


			// safely remove empty strings from args
			var encoded_args = args.filter(function (s) return s != "");
			
			
			
			var p = Popen.create(encoded_args, { cwd : cwd, stdout : Subprocess.PIPE, stderr : Subprocess.PIPE, stdin :Subprocess.PIPE, startupinfo : Plugin.startupInfo(), env : env});
			
			var inputBytes = input != null ? input.encode("utf-8") : null;
			//print("INPUT:" + str(input))
			var r = p.communicate(inputBytes);
			var out = r._1, err = r._2;

			
			return Tup2.create(out.decode("utf-8"), err.decode("utf-8"));
		}
		catch (e:Dynamic) 
		{
			trace(e);
			var p = args[0];
			var err = 'Error while running $p: in $cwd ($e)'; 
			return Tup2.create("", err);
		}
	}
}

/*


import sys
import os
import sublime

from subprocess import Popen, PIPE

from haxe.plugin import STARTUP_INFO

from haxe.plugin import is_st3

from haxe.tools.stringtools import encode_utf8

from haxe.log import log

if is_st3:
	import _thread as thread
else:
	import thread




*/