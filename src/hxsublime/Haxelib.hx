package hxsublime;

import haxe.ds.StringMap;
import hxsublime.Execute;
import hxsublime.project.Project;
import hxsublime.tools.HxSrcTools.HaxeType;
import python.lib.os.Path;
import python.lib.Re;
import python.lib.Types.Tup2;
import sublime.Sublime;


using python.lib.StringTools;


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
			path = Path.join( manager.basePath , name , this.version.split(".").join(","));
		}
	}
 

	public function as_cmd_arg () 
	{
		return name + ":" + version;
	}

	public function extract_types( ) 
	{
		if (dev || classes == null && packages == null) {
			var t = Types.extract_types( this.path );
			classes = t.all_types();
			packages = t.packs();
		}
		
		return Tup2.create(this.classes, this.packages);
	}
}



class HaxeLibManager {
	
	var _available:StringMap<HaxeLibLibrary>;

	var project:Project;

	public var basePath : String;

	var scanned : Bool;

	public function new(project:Project){
		_available = new StringMap();
		basePath = null;
		scanned = false;
		this.project = project;
	}


	@property
	public function available (){
		if (!this.scanned) {
			scan();
		}
		return _available;
	}

	public function get( name:String ) {
		if( available().exists(name))
			return available().get(name);
		else {
			Sublime.status_message( "Haxelib : "+ name +" project not installed" );
			return null;
		}
	}

	public function get_completions() {
		var comps = [];
		for (k in available().keys())
		{
			var lib = available().get(k);
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
		var r = Execute.run_cmd( cmd, env );
		var hlout = r._1;
		var hlerr = r._2;
		var basePath = hlout.strip();

		_available = new StringMap();

		var cmd = project.haxelib_exec();
		cmd.push("list");
		
		var r = Execute.run_cmd( cmd, env );
		var hlout = r._1;
		var hlerr = r._2;
		trace("haxelib output: " + hlout);
		trace("haxelib error: " + hlerr);
		for (l in hlout.split("\n")) {
			var found = libLine.match( l );
			if (found != null) 
			{
				var g = found.groups();
				var name = g._1, dev = g._2, version = g._3;
				var lib = new HaxeLibLibrary( this, name , dev != null , version );

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
		Execute.run_cmd(cmd, null, null, env);
		scan();
	}

	public function remove_lib(lib){
		var cmd = project.haxelib_exec();
		var env = project.haxe_env();
		cmd.push("remove");
		cmd.push(lib);
		trace(Std.string(cmd));
		Execute.run_cmd(cmd,null, null, env);
		scan();
	}

	public function upgrade_all(){
		var cmd = project.haxelib_exec();
		var env = project.haxe_env();
		cmd.push("upgrade");
		trace(Std.string(cmd));
		Execute.run_cmd(cmd, null, null, env);
		scan();
	}

	public function this_update(){
		var cmd = project.haxelib_exec();
		var env = project.haxe_env();
		cmd.push("thisupdate");
		trace(Std.string(cmd));
		Execute.run_cmd(cmd, null, null, env);
		scan();
	}

	public function search_libs(){
		var cmd = project.haxelib_exec();
		var env = project.haxe_env();
		cmd.push("search");
		cmd.push("_");
		trace(Std.string(cmd));
		var res = Execute.run_cmd(cmd, null, null, env);
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
		return available().exists(lib);
	}
	
	public function get_lib(lib:String) {
		return available().get(lib);
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