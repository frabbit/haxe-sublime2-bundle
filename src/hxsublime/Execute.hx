package hxsublime;

import python.lib.subprocess.Popen;
import python.lib.Types.OSError;

class Execute {
	public static function run_cmd_async(args:Array<String>, callback:String->String->Void, input:String=null, cwd:String=null, env=null)
	{

		public static function in_thread ()
		{
			var r = run_cmd(args, input, cwd, env);
			var out = r._1, err = r._2;
			sublime.set_timeout(callback.bind(out, err), 1);
		}

		ThreadLowLevel.start_new_thread(in_thread, ())
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

			for (k in env) 
			{
				var val = env[k];
				env[k] = Path.expandvars(val);
			}


			// safely remove empty strings from args
			var encoded_args = args.filter(function (s) return s != "");
			
			
			
			var p = Popen.create(encoded_args, { cwd : cwd, stdout : PIPE, stderr : PIPE, stdin :PIPE, startupinfo : STARTUP_INFO, env : env});
			
			var inputBytes = input.encode("utf-8");
			//print("INPUT:" + str(input))
			var r = p.communicate(inputBytes);
			var out = r._1, err = r._2;


			return Tup2.create(out.decode("utf-8"), err.decode("utf-8"));
		}
		catch (e:Dynamic) 
		{
			var p = args[0];
			err = 'Error while running $p: in $cwd ($e)'; 
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