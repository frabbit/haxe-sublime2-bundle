package hxsublime.compiler;

import hxsublime.panel.Base.Panels;
import hxsublime.Plugin;
import python.lib.Os;
import python.lib.os.Path;
import python.lib.subprocess.Popen;
import python.lib.Subprocess;
import python.lib.Time;
import python.lib.Types.OSError;
import python.lib.Types.Tup2;
import python.lib.Types.ValueError;
import sublime.Sublime;

using python.lib.StringTools;
using python.lib.ArrayTools;

class Server 
{
	public var _use_wrapper : Bool;
	public var _server_proc:Popen;
	public var _server_port : Int;
	public var _orig_server_port : Int;

	public function new (port:Int) {

		this._use_wrapper = Settings.use_haxe_servermode_wrapper();
		this._server_proc = null;
		this._server_port = port;
		this._orig_server_port = port;
	}


	public function get_server_port () 
	{
		return this._server_port;
	}

	public function start( haxe_path:String, cwd:String = null, env = null, retries:Int = 10 ) 
	{
				
		if (this._server_proc == null) { 
			var cmd = null;
			if (this._use_wrapper) 
			{
				var wrapper = Plugin.plugin_base_dir() + "/wrapper";
				cmd = ["neko", wrapper];
			}
			else 
			{
				cmd = [];
			}
			
			cmd.extend([haxe_path , "--wait" , Std.string(this._server_port) ]);
			trace("start server:");
			
			trace(cmd.join(" "));

			function onError (e:Dynamic) {
				var err = 'Error starting server ${cmd.join(" ")}: ${Std.string(e)}';
				Sublime.error_message(err);
				if (retries > 0) 
				{
					this.stop();
					this._server_port += 1;
					trace("retry starting server at port: " + Std.string(this._server_port));
					this.start(haxe_path, cwd, env, retries-1);
				}
				else 
				{
					var msg = "Cannot start haxe compilation server on ports {0}-{1}";
					msg = msg.format([this._orig_server_port, this._server_port]);
					trace("Server starting error");
					// hxpanel.default_panel().writeln(msg)
					// sublime.error_message(msg)
				}
			}
			try {
				
				
				var full_env = Os.environ.copy();
				if (env != null) 
				{
					full_env.update(env);
				}
					
				if (env != null) 
				{
					for (k in env.keys()) 
					{
						var val = null;
						try 
						{
							val = env.get(k, null);
						}
						catch (e:Dynamic) 
						{
							val = env.get(k, null);
						}
						
						full_env.set(k, Path.expandvars(val));
					}
				}
				

				trace("server env:" + Std.string(full_env));
				this._server_proc = Popen.create(cmd, {cwd:cwd, env:full_env, stdin:Subprocess.PIPE, stdout:Subprocess.PIPE, startupinfo:Plugin.startupInfo()});
				
				this._server_proc.poll();

				Time.sleep(0.05);
					
				trace("server started at port: " + Std.string(this._server_port));
				// hxpanel.default_panel().writeln("server started at port: " + Std.string(this._server_port))
			}
			catch (e:OSError) 
			{
				onError(e);
			}
			catch (e:ValueError) 
			{
				onError(e);
			}
			catch (e:Dynamic) 
			{
				trace("ERROR : " + Std.string(e));
			}
		}
	}
		

	public function stop( completeCallback:Void->Void = null)  
	{
		var old_port = this._server_port;
		try {
			var proc = this._server_proc;

			if (proc != null) {
				this._server_proc = null;
				
				if (this._use_wrapper) {
					proc.stdin.write("x");
					Time.sleep(0.2);
				}
				else {
					proc.terminate();
					Time.sleep(0.2);
				}
				proc.kill();
				proc.wait();
				proc = null;
				//del proc
				
				// running the process on the same port causes zombie processes
				// increment the server port to avoid this
				this._server_port += 1;
			}
		}
		catch (e:Dynamic) 
		{
			this._server_proc = null;
		}
		
		if (completeCallback != null) 
		{
			Panels.default_panel().writeln("stopping server on port: " + Std.string(old_port));
			completeCallback();
		}
	}

	public function __del__() {
		this.stop();
	}
}


/*
import sublime
import sys
import os

from subprocess import Popen, PIPE
import time 
from haxe.plugin import is_st3

from haxe.plugin import STARTUP_INFO
from haxe.log import log
from haxe import plugin
from haxe import panel as hxpanel
from haxe import settings as hxsettings

class Server ():
	
		
		
*/