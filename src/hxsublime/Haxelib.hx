package hxsublime;

import haxe.ds.StringMap;
import hxsublime.project.Project;
import hxsublime.tools.HxSrcTools.HaxeType;



class HaxeLibLibrary {

	public var name: String;
	public var dev: Bool;
	public var version: String;
	public var classes: Array<HaxeType>;
	public var packages: Array<String>;
	public var path:String;

	public function new(manager:HaxeLibManager, name:String , dev:Bool , version:String ) 
	{
		this.name = name;
		this.dev = dev;
		this.version = version;
		this.classes = null;
		this.packages = null;
 
		if (dev) {
			this.path = version;
			this.version = "dev";
		} else {
			path = Path.join( manager.basePath , name , self.version.split(".").join(","));
		}
	}
 

	public function as_cmd_arg () 
	{
		return name + ":" + version;
	}

	public function extract_types( ) 
	{
		if (dev || classes == null && packages == null) {
			var t = hxtypes.extract_types( self.path );
			classes = t._1;
			packages = t._2;
		}
		
		return Tup2.create(self.classes, self.packages);
	}
}



class HaxeLibManager {
	
	var _available:StringMap<HaxeLibLibrary>;

	var project:Project;

	var basePath : String;

	var scanned : Bool;

	public function new(project:Project){
		_available = new StringMap();
		basePath = null;
		scanned = false;
		this.project = project;
	}


	@property
	public function available (){
		if (!self.scanned) {
			scan();
		}
		return _available;
	}

	public function get( name:String ) {
		if( available.exists(name))
			return available.get(name);
		else {
			Sublime.status_message( "Haxelib : "+ name +" project not installed" );
			return null;
		}
	}

	public function get_completions() {
		var comps = [];
		for (k in available.keys())
		{
			lib = available[k];
			comps.push( Tup2.create( lib.name + " [" + lib.version + "]" , lib.name ) );
		}

		return comps;
	}

	static var libLine = Re.compile("([^:]*):[^\\[]*\\[(dev\\:)?(.*)\\]");

	public function scan() 
	{
		scanned = true;
		var env = project.haxe_env();
		trace("do scan");
		var cmd = project.haxelib_exec();
		cmd.push("config");
		var r = run_cmd( cmd, env=env );
		var hlout = r._1;
		var hlerr = r._2;
		var basePath = hlout.strip();

		_available = new StringMap();

		var cmd = project.haxelib_exec();
		cmd.push("list");
		
		var r = run_cmd( cmd, env=env );
		var hlout = r._1;
		var hlerr = r._2;
		trace("haxelib output: " + hlout);
		trace("haxelib error: " + hlerr);
		for (l in hlout.split("\n")) {
			found = libLine.match( l );
			if (found != null) 
			{
				var g = found.groups();
				var name = g._1, dev = g._2, version = g._3;
				var lib = new HaxeLibLibrary( self, name , dev != null , version );

				_available.set( name , lib);
			}
		}
	}

	public function install_lib(lib){
		var cmd = project.haxelib_exec();
		var env = project.haxe_env();
		cmd.push("install");
		cmd.push(lib);
		trace(Std.string(cmd));
		run_cmd(cmd, env=env);
		scan();
	}

	public function remove_lib(lib){
		var cmd = project.haxelib_exec();
		var env = project.haxe_env();
		cmd.push("remove");
		cmd.push(lib);
		trace(Std.string(cmd));
		run_cmd(cmd,env=env);
		scan();
	}

	public function upgrade_all(){
		var cmd = project.haxelib_exec();
		var env = project.haxe_env();
		cmd.push("upgrade");
		trace(Std.string(cmd));
		run_cmd(cmd, env=env);
		scan();
	}

	public function self_update(){
		var cmd = project.haxelib_exec();
		var env = project.haxe_env();
		cmd.push("selfupdate");
		trace(Std.string(cmd));
		run_cmd(cmd, env=env);
		scan();
	}

	public function search_libs(){
		var cmd = project.haxelib_exec();
		var env = project.haxe_env();
		cmd.push("search");
		cmd.push("_");
		trace(Std.string(cmd));
		var res = run_cmd(cmd, env=env);
		var out = res._1;
		var err = res._2;
		return _collect_libraries(out);
	}

	public function _collect_libraries(out:String){
		var x = out.split("\n");
		x.reverse();
		return x;
	}

	public function is_lib_installed(lib:String){
		return Lambda.has(available.keys(), lib);
	}
	
	public function get_lib(lib:String) {
		return available.get(lib);
	}

}

/*
import re
import os
import sublime

from haxe import types as hxtypes

from haxe.log import log

from haxe.execute import run_cmd



*/