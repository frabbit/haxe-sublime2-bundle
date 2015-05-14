package hxsublime;

import hxsublime.Plugin;
import python.lib.Os;
import python.lib.os.Path;
import python.lib.Subprocess;
import python.lib.subprocess.Popen;

import python.Tuple;
import python.Dict;
import python.lib.ThreadLowLevel;

import sublime.Sublime;

using hxsublime.support.StringTools;

class Execute 
{
	public static function runCmdAsync(args:Array<String>, callback:String->String->Void, input:String=null, cwd:String=null, env=null)
	{
		function inMainThread ()
		{
			var r = runCmd(args, input, cwd, env);
			var out = r._1, err = r._2;
			Sublime.set_timeout(callback.bind(out, err), 1);
		}
		ThreadLowLevel.start_new_thread(inMainThread, new Tuple());
	}

	public static function runCmd( args:Array<String>, input:String=null, cwd:String=null, env:Dict<String,String>=null ):Tuple2<String, String>
	{
		if (cwd == null)
		{
			cwd = ".";
		}
		
		return try
		{
			var base_env = Os.environ.copy();

			if (env != null)
			{
				base_env.update(env);
			}

			var env = base_env;

			for (k in env.keys().iter().toHaxeIterator())
			{
				var val = env.get(k, null);
				env.set(k, Path.expandvars(val));
			}

			// safely remove empty strings from args
			var cmdArgs = args.filter(function (s) return s != "");

			var p = Popen.create(cmdArgs, { cwd : cwd, stdout : Subprocess.PIPE, stderr : Subprocess.PIPE, stdin :Subprocess.PIPE, startupinfo : Plugin.startupInfo(), env : env});

			var inputBytes = input != null ? input.encode("utf-8") : null;

			var r = p.communicate(inputBytes);
			var out = r._1, err = r._2;


			Tuple2.make(out.decode("utf-8"), err.decode("utf-8"));
		}
		catch (e:Dynamic)
		{
			trace(e);
			var p = args[0];
			var err = 'Error while running $p: in $cwd ($e)';
			Tuple2.make("", err);
		}
	}
}
