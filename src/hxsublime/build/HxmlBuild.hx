package hxsublime.build;

import hxsublime.Config.Target;
import hxsublime.Haxelib.HaxeLibLibrary;
import hxsublime.panel.Panels;
import hxsublime.project.Project;

import hxsublime.Settings;
import hxsublime.tools.HxSrcTools;
import python.lib.os.Path;
import python.lib.Re;
import python.lib.Time;
import python.lib.Types.Tup2;
import python.lib.Types.Tup3;
import sublime.Sublime;
import sublime.View;

using python.lib.ArrayTools;

using StringTools;

using python.lib.StringTools;

class HxmlBuild implements hxsublime.build.Build 
{

	var _showTimes:Bool;
	var _stdBundle:HaxeTypeBundle;
	var _args:Array<Tup2<String,String>>;
	
	var _hxml:String;
	var _buildFile:String;
	var libs:Array<HaxeLibLibrary>;
	var _updateTime:Int;
	var defines:Array<String>;
	
	var _classpaths:Array<String>;
	var typeBundle:HaxeTypeBundle;
	var modeCompletion:Bool;

	public var name:String;
	public var main:String;
	public var _target:String;
	public var output:String;

	public function getClassPaths ():Array<String>
	{
		return _classpaths;
	}

	public function new(hxml:String, build_file:String)  
	{
		
		this._showTimes = false;
		this._stdBundle = HxSrcTools.emptyTypeBundle();
		this._args = [];
		this.main = null;
		this._target = null;

		this.output = "dummy.js";
		this._hxml = hxml;
		this._buildFile = build_file;
		this._classpaths = [];
		this.libs = [];
		this.typeBundle = null;
		this._updateTime = null;
		this.modeCompletion = false;
		this.defines = [];
		this.name = null;
	}



	public function stdBundle () return _stdBundle;

	public function target () return { name : _target, plattform : _target, args : []};

	public function classpaths ():Array<String> return _classpaths;
	
	public function hxml () return _hxml;

	
	public function title() 
	{
		return this.output;
	}

	public function setHxml (hxml:String) {
		this._hxml = hxml;
	}
	

	
	public function buildFile() 
	{
		return this._buildFile;
	}

	public function addDefine (define:String) 
	{
		this.defines.push(define);
	}
		
	
	function setMain(main:String) 
	{
		this.main = main;
	}
	


	function getName () 
	{
		var n = null;
		if (this.name != null) {
			n = this.name;
		}
		else {
			n = if (this.main == null) "[No Main]" else this.main;
		}
		return n;
	}

	public function setStdBundle(stdBundle) 
	{
		this._stdBundle = stdBundle;
	}

	public function args () return _args;

	public function equals (other) 
	{
		
		return (this.args() == other._args()
			&& this.main == other.main
			&& this.name == other.name
			&& this._target == other._target
			&& this.output == other.output
			&& this.hxml() == other.hxml()
			&& this.classpaths() == other.classpaths()
			&& this.libs == other.libs
			&& this._showTimes == other._showTimes
			&& this.modeCompletion == other.modeCompletion
			&& this.defines == other.defines
			&& this._buildFile == other._buildFile);
	}
		   
	public function merge (other_build:HxmlBuild) 
	{
		var ob = other_build;
		this._args.extend(ob.args());

		this._classpaths.extend(ob.classpaths());
		
		this.libs.extend(ob.libs);
		defines.extend(ob.defines);
		
		if (this.main == null) 
		{
			this.main = ob.main;
		}
		if (this.name == null) 
		{
			this.name = ob.name;
		}
	}
	
	public function copy () 
	{

		this.getTypes();

		var hb = new HxmlBuild(this._hxml, this.buildFile());
		hb._args = this.args().copy();
		hb.main = this.main;
		hb.name = this.name;
		hb._target = this._target;
		hb.output = this.output;
		hb.defines = this.defines.copy();
		hb._stdBundle = this._stdBundle;
		hb._classpaths = this._classpaths.copy();
		hb.libs = this.libs.copy();
		hb.typeBundle = this.typeBundle;
		hb._updateTime = this._updateTime;
		hb._showTimes = this._showTimes;
		hb.modeCompletion = this.modeCompletion;
		return hb;
	}
	public function addArg(arg:Tup2<String,String>) 
	{
		this._args.push(arg);
	}

	public function getBuildFolder () 
	{
		return if (this.buildFile() != null) Path.dirname(this.buildFile()) else null;
	}

	public function setBuildCwd () 
	{
		this.setCwd(this.getBuildFolder());
	}
	
	function alignDriveLetter(path:String) 
	{
		var is_win =  Sublime.platform() == "windows";
		
		if (is_win) {
			var reg = Re.compile("^([a-z]):(.*)$");
			var match = Re.match(reg, path);
			if (match != null) {
				path = match.group(1).toUpperCase() + ":" + match.group(2);
			}
		}
		return path;
	}

	public function addClasspath (cp) 
	{
		var cp = this.alignDriveLetter(cp);
		if (!Lambda.has(this._classpaths, cp)) {
			this._classpaths.push(cp);
			this._args.push(Tup2.create("-cp", cp));
		}
	}
	

	public function addLib(lib:HaxeLibLibrary) 
	{
		this.libs.push(lib);
		this.addArg( Tup2.create("-lib", lib.name));
	}

	function getClasspathOfFile (file) 
	{
			
		var file = this.alignDriveLetter(file);
		
		var cps = this._classpaths.copy();

		var build_folder = this.getBuildFolder();
		if (build_folder != null && !Lambda.has(cps, build_folder)) 
		{
			trace("add build folder to classpaths: " + build_folder + ", classpaths: " + Std.string(cps));
			cps.push(build_folder);
		}
		for (cp in cps) 
		{
			var prefix = Path.commonprefix([cp, file]);
			if (prefix == cp) {
				return cp;
			}
		}

		return null;
	}

	//function isFileInClasspath (file:String) 
	//{
	//	file = this.alignDriveLetter(file);
	//	return this.getClasspathOfFile(file) != null;
	//}

	public function getRelativePath (file:String) 
	{
		file = this.alignDriveLetter(file);

		var cp = this.getClasspathOfFile(file);

		trace(file);
		trace(file.replace(cp, ""));
		trace(file.replace(cp, "").substr(1));

		return if (cp != null) file.replace(cp, "").substr(1) else null;
	}

	function targetToString () 
	{
		var target = null;
		if (this._target == null) {
			target = "js";
		}
		else 
		{
			target = this._target;
			if (target == "js" && Lambda.has(this.defines, "nodejs")) 
			{
				target = "node.js";
			}
		}
		return target;
	}

	public function toString()  
	{
		var out = Path.basename(this.output);
		var main = this.getName();
		var target = this.targetToString();
		return '$main ($target - $out)';
	}
	
	public function makeHxml()  
	{
		var outp = "# Autogenerated "+this.hxml+"\n\n";
		outp += "# "+this.toString() + "\n";
		outp += "-main "+ this.main + "\n";
		for (a in this._args) {
			outp += a._1 + " " + a._2 + "\n";
		}
		
		var d = Path.dirname( this._hxml ) + "/";
		
		// relative paths
		outp = outp.replace( d , "");
		outp = outp.replace( "-cp "+Path.dirname( this._hxml )+"\n", "");

		outp = outp.replace("--no-output " , "");
		outp = outp.replace("-v" , "");

		outp = outp.replace("dummy" , this.main.toLowerCase() );

		return outp.strip();
	}

	function setCwd (cwd:String) 
	{
		this._args.push(Tup2.create("--cwd" , cwd ));
	}

	public function setTimes () 
	{
		this._showTimes = true;
		this._args.push(Tup2.create("--times", ""));
		this._args.push(Tup2.create("-D", "macro-times"));
		this._args.push(Tup2.create("-D", "macro_times"));
	}

	function setServerMode (server_port = 6000) 
	{
		this._args.push(Tup2.create("--connect" , Std.string(server_port)));
	}

	function getCommandArgs (haxe_path:Array<String>) 
	{
		var cmd = haxe_path.copy();

		for (a in this._args)
		{
			cmd.extend( [a._1, a._2] );
		}

		for (l in this.libs)
		{
			cmd.push( "-lib" );
			cmd.push( l.as_cmd_arg() );
		}

		if (this.main != null) 
		{
			cmd.push("-main");
			cmd.push(this.main);
		}
		return cmd;
	}

	public function setAutoCompletion (display, macroCompletion = false, noOutput = true) 
	{
		
		this.modeCompletion = true;

		var args = this._args;

		this.main = null;

		function filterTargets (x:Tup2<String,String>) 
		{
			return x._1 != "-cs" && x._1 != "-x" && x._1 != "-js" && x._1 != "-php" && x._1 != "-cpp" && x._1 != "-swf" && x._1 != "-java";
		}

		if (macroCompletion) 
		{
			args = args.filter(filterTargets ).copy();
		}
		else 
		{
			args = args.map(function (x) return if (x._1 == "-x") Tup2.create("-neko", x._2) else x).copy();
		}

		function filterCommandsAndDce (x:Tup2<String,String>) 
		{
			return x._1 != "-cmd" && x._1 != "-dce";
		}


		args = args.filter(filterCommandsAndDce );

		if (!this._showTimes) 
		{
			function filterTimes (x:Tup2<String,String>) 
			{
				return x._1 != "--times";
			}
			args = args.filter(filterTimes).copy();
		}

		if (macroCompletion) 
		{
			args.push(Tup2.create("-neko", "__temp.n"));
		}

		
		args.push( Tup2.create("--display", display ) );
		if (noOutput) 
		{
			args.push( Tup2.create("--no-output" , "") );
		}

		this._args = args;
	}


	function updateTypes() 
	{
		// haxe.output_panel.HaxePanel.status("haxe-debug", "updating types")
		trace("update types for classpaths:" + Std.string(this._classpaths));
		trace("update types for libs:" + Std.string(this.libs));
		this.typeBundle = Types.findTypes(this._classpaths, this.libs, this.getBuildFolder(), [], [], false );
	}

		


	function shouldRefreshTypes(now) 
	{
		return this.typeBundle == null || this._updateTime == null || (now - this._updateTime) > 10;
	}

	public function getTypes()  
	{
		var now = Time.time();
		
		if (this.shouldRefreshTypes(now)) 
		{
			trace("UPDATE THE TYPES NOW");
			this._updateTime = now;
			this.updateTypes();
			var runTime = Time.time() - now;
			trace("update types time: " + runTime);
		}

		return this.typeBundle;
	}

	public function prepareCheckCmd(project, server_mode, view) 
	{
		var r = this.prepareBuildCmd(project, server_mode, view);
		var cmd = r._1, build_folder = r._2;
		cmd.push("--no-output");
		return Tup2.create(cmd, build_folder);
	}
	
	function absoluteOutput() 
	{
		if (Path.isabs(this.output)) {
			return this.output;
		}
		else {
			return Path.join(this.getBuildFolder(),this.output);
		}
	}
		
	public function prepareRunCmd (project:Project, server_mode:Bool, view:View):Tup2<Array<String>, String>
	{
		var r = this.prepareRun(project, view, server_mode);
		var cmd = r._1, build_folder = r._2, nekox_file = r._3;

		trace(this.args);
		trace(cmd);
		trace(build_folder);
		trace(nekox_file);
		
		var default_open_ext = Settings.openWithDefaultApp();

		if (nekox_file != null) 
		{
			cmd.extend(["-cmd", "neko " + nekox_file]);
		}
		else if (this._target == "swf" && default_open_ext != null)
		{
			cmd.extend(["-cmd", default_open_ext + " " + this.absoluteOutput()]);
		}
		else if (this._target == "neko")
		{
			cmd.extend(["-cmd", "neko " + this.absoluteOutput()]);
		}
		else if (this._target == "cpp")
		{
			var sep_index = this.main.lastIndexOf(".");
			var exe = if (sep_index > -1) this.main.substr(sep_index+1) else this.main;
			cmd.extend(["-cmd", Path.join(this.absoluteOutput(),exe) + "-debug"]);
		}
		else if (this._target == "js" && Lambda.has(this.defines, "nodejs"))
		{
			cmd.extend(["-cmd", "nodejs " + this.absoluteOutput()]);
		}
		else if (this._target == "java")
		{
			var sep_index = this.absoluteOutput().lastIndexOf(Path.sep);
			var jar = if (sep_index == -1) this.absoluteOutput() + ".jar" else this.absoluteOutput().substr(sep_index+1) + ".jar";
			cmd.extend(["-cmd", "java -jar " + Path.join(this.absoluteOutput(), jar)]);
		}
		else if (this._target == "cs") 
		{
			cmd.extend(["-cmd", "cd " + this.absoluteOutput()]);
			cmd.extend(["-cmd", "gmcs -recurse:*.cs -main:" + this.main + " -out:" + this.main + ".exe-debug"]);
			cmd.extend(["-cmd", Path.join(".", this.main + ".exe-debug")]);
		}

		return Tup2.create(cmd, build_folder);
	}

	public function prepareBuildCmd (project:Project, server_mode:Bool, view:View) 
	{
		var r = this.prepareRun(project, view, server_mode);
		var cmd = r._1, build_folder = r._2;
		return Tup2.create(cmd, build_folder);
	}

	public function prepareRun (project:Project, view:View, server_mode:Null<Bool> = null):Tup3<Array<String>, String, String>
	{

		server_mode = if (server_mode == null) project.isServerMode() else server_mode;
		
		var run_exec = this.getExecutable(project, view);
		var b = this.copy();
		
		var nekoxFileName = null;
		
		for (i in 0...b._args.length) 
		{
			var a = b._args[i];
			if (a._1 == "-x") {
				nekoxFileName = a._2 + ".n";
				b._args[i] = Tup2.create("-neko", nekoxFileName);
			}
		}

		if (server_mode) {
			project.startServer( view );
			b.setServerMode(project.server.get_server_port());
		}

		
		b.setBuildCwd();
		var cmd = b.getCommandArgs(run_exec);

		return Tup3.create(cmd, this.getBuildFolder(), nekoxFileName);
	}

	function getExecutable(project:Project, view:View) 
	{
		return project.haxeExec(view);
	}

	public function escapeCmd(cmd:Array<String>) 
	{
		var print_cmd = cmd.copy();
		var l = print_cmd.length;
		for (i in 0...l) 
		{
			var e = print_cmd[i];
			if (e == "--macro" && i < l-1) 
			{
				print_cmd[i+1] = "'" + print_cmd[i+1] + "'";
			}
		}
		return print_cmd;
	}

	function runAsync (project:Project, view:View, callback:String->String->Void, server_mode:Null<Bool> = null) 
	{
		var env = project.haxeEnv(view);
		var r = this.prepareRun(project, view, server_mode);
		var cmd = r._1, build_folder = r._2, nekox_file_name = r._3;
		var print_cmd = cmd.copy();
		for (i in 0...print_cmd.length) 
		{
			var e = print_cmd[i];
			if (e == "--macro" && i < print_cmd.length-1)
			{
				print_cmd[i+1] = "'" + print_cmd[i+1] + "'";
			}
		}
		
		function cb (out, err) 
		{
			this.onRunComplete(out, err, build_folder, nekox_file_name);
			callback(out, err);
		}

		Execute.runCmdAsync( cmd, cb, "", build_folder, env );
	}
	
	

	function runSync (project:Project, view:View, server_mode:Null<Bool> = null) 
	{
		var env = project.haxeEnv(view);
		var r = this.prepareRun(project, view, server_mode);
		var cmd = r._1; 
		var build_folder = r._2; 
		var nekox_file_name = r._3;

		trace(cmd.join(" "));
		var r = Execute.runCmd( cmd, "", build_folder, env );
		var out = r._1, err = r._2;
		
		this.onRunComplete(out, err, build_folder, nekox_file_name);
		
		return Tup2.create(out,err);
	}


	function onRunComplete(out, err, build_folder, nekox_file_name) 
	{
		trace("---------------cmd-------------------");
		trace("out:" + out);
		trace("err:" + err);
		trace("---------compiler-output-------------");
		if (nekox_file_name != null) 
		{
			this.runNekoX(build_folder, nekox_file_name);
		}
	}
		

	function runNekoX(build_folder:String, neko_file_name:String) 
	{
		var neko_file = Path.join(build_folder, neko_file_name);
		trace("run nekox: " + neko_file) ;
		var r = Execute.runCmd(["neko", neko_file]);
		var out = r._1, err = r._2;
		Panels.defaultPanel().writeln(out);
		Panels.defaultPanel().writeln(err);
	}

	public function run(project:Project, view:View, async:Bool, callback:String->String->Void, server_mode = null) 
	{
		if (async) 
		{
			trace("RUN ASYNC COMPLETION");
			this.runAsync( project, view, callback, server_mode );
		}
		else 
		{
			trace("RUN SYNC COMPLETION");
			var r = this.runSync( project, view, server_mode );
			var out = r._1;
			var err = r._2;
			callback(out, err);
		}
	}

	
	public function isTypeAvailable (type:HaxeType) 
	{
		var pack = type.toplevelPack();
		return pack == null || this.isPackAvailable(pack);
	}

	public function isPackAvailable (pack:String) 
	{
		if (pack == "") 
		{
			return true;
		}

		pack = pack.split(".")[0];
		var target = this._target;

		var available = true;

		if (pack != null && target != null && Lambda.has(Config.target_packages, pack)) 
		{
			if (Config.target_std_packages.exists(target))
			{
				if (!Lambda.has(Config.target_std_packages.get(target), pack)) 
				{
					available = false;
				}
			}
		}
		return available;
	}
}
