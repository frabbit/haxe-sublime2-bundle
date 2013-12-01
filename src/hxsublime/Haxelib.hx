package hxsublime;

import haxe.ds.StringMap;
import hxsublime.Execute;
import hxsublime.project.Project;
import hxsublime.tools.HxSrcTools.HaxeType;
import python.lib.os.Path;
import python.lib.Re;
import python.lib.Types.Tup2;
import python.lib.Types.Tup3;
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
			var t = Types.extractTypes( this.path );
			classes = t.allTypes();
			packages = t.packs();
		}
		
		return Tup2.create(this.classes, this.packages);
	}
}



class HaxeLibManager 
{
	
	static var libLine = Re.compile("([^:]*):[^\\[]*\\[(dev\\:)?(.*)\\]");


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

	public function getCompletions():Array<Tup2<String, String>> 
	{
		var comps = [];
		for (k in available().keys())
		{
			var lib = available().get(k);
			trace(lib);
			comps.push( Tup2.create( lib.name + " [" + lib.version + "]" , lib.name ) );
		}

		return comps;
	}

	

	public function scan() 
	{
		scanned = true;
		var env = project.haxeEnv();
		var cmd = project.haxelibExec();
		cmd.push("config");
		var r = Execute.runCmd( cmd, env );
		var hlout = r._1;
		var hlerr = r._2;
		basePath = hlout.strip();

		_available = new StringMap();

		var cmd = project.haxelibExec();
		cmd.push("list");
		
		var r = Execute.runCmd( cmd, env );
		var hlout = r._1;
		var hlerr = r._2;
		//trace("haxelib output: " + hlout);
		//trace("haxelib error: " + hlerr);
		for (l in hlout.split("\n")) 
		{
			var found = libLine.match( l );
			if (found != null) 
			{
				var g:Tup3<String,String,String> = cast found.groups(null);
				if (g != null) 
				{
					var name = g._1, dev = g._2, version = g._3;
					var lib = new HaxeLibLibrary( this, name , dev != null , version );

					_available.set( name , lib);
				}
			}
		}
	}

	public function installLib(lib:String)
	{
		var cmd = project.haxelibExec();
		var env = project.haxeEnv();
		cmd.push("install");
		cmd.push(lib);
		trace(Std.string(cmd));
		Execute.runCmd(cmd, null, null, env);
		scan();
	}

	public function removeLib(lib:String)
	{
		var cmd = project.haxelibExec();
		var env = project.haxeEnv();
		cmd.push("remove");
		cmd.push(lib);
		trace(Std.string(cmd));
		Execute.runCmd(cmd,null, null, env);
		scan();
	}

	public function upgradeAll()
	{
		var cmd = project.haxelibExec();
		var env = project.haxeEnv();
		cmd.push("upgrade");
		trace(Std.string(cmd));
		Execute.runCmd(cmd, null, null, env);
		scan();
	}

	public function selfUpdate()
	{
		var cmd = project.haxelibExec();
		var env = project.haxeEnv();
		cmd.push("thisupdate");
		trace(Std.string(cmd));
		Execute.runCmd(cmd, null, null, env);
		scan();
	}

	public function searchLibs()
	{
		var cmd = project.haxelibExec();
		var env = project.haxeEnv();
		cmd.push("search");
		cmd.push("_");
		//trace(Std.string(cmd));
		var res = Execute.runCmd(cmd, null, null, env);
		var out = res._1;
		var err = res._2;
		return parseLibraries(out);
	}

	function parseLibraries(out:String):Array<String>
	{
		var x = out.split("\n").filter(function (x) return x != "" && x.indexOf("libraries found") == -1);
		x.reverse();
		return x;
	}

	public function isLibInstalled(lib:String)
	{
		return available().exists(lib);
	}
	
	public function getLib(lib:String) 
	{
		return available().get(lib);
	}

}
