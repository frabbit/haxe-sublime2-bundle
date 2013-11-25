package hxsublime.build;

import hxsublime.Config.Target;
import hxsublime.Haxelib.HaxeLibLibrary;
import hxsublime.panel.Base.Panels;
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

class HxmlBuild {

	public var show_times:Bool;
	public var _std_bundle:HaxeTypeBundle;
	public var _args:Array<Tup2<String,String>>;
	public var main:String;
	public var _target:String;
	public var output:String;
	public var _hxml:String;
	public var _build_file:String;
	public var _classpaths:Array<String>;
	public var libs:Array<HaxeLibLibrary>;
	public var type_bundle:HaxeTypeBundle;
	public var _update_time:Int;
	public var mode_completion:Bool;
	public var defines:Array<String>;
	public var name:String;

	public function new(hxml:String, build_file:String)  
	{
		
		this.show_times = false;
		this._std_bundle = HxSrcTools.empty_type_bundle();
		this._args = [];
		this.main = null;
		this._target = null;

		this.output = "dummy.js";
		this._hxml = hxml;
		this._build_file = build_file;
		this._classpaths = [];
		this.libs = [];
		this.type_bundle = null;
		this._update_time = null;
		this.mode_completion = false;
		this.defines = [];
		this.name = null;
	}
	public function std_bundle () return _std_bundle;

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
	

	
	public function build_file() 
	{
		return this._build_file;
	}

	public function add_define (define:String) 
	{
		this.defines.push(define);
	}
		
	
	public function set_main(main:String) 
	{
		this.main = main;
	}
	


	public function get_name () 
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

	public function set_std_bundle(std_bundle) 
	{
		this._std_bundle = std_bundle;
	}

	public function args () return _args;

	public function equals (other) 
	{
		
		return (this.args() == other._args()
			&& this.main == other.main
			&& this.name == other.name
			&& this._target == other._target
			&& this.output == other.output
			&& this.hxml == other.hxml
			&& this.classpaths == other.classpaths
			&& this.libs == other.libs
			&& this.show_times == other.show_times
			&& this.mode_completion == other.mode_completion
			&& this.defines == other.defines
			&& this._build_file == other._build_file);
	}
		   
	public function merge (other_build:HxmlBuild) 
	{
		var ob = other_build;
		this._args.extend(ob.args());

		//for c in ob.classpaths:
		//	if c !in this.classpaths:
		//		this.classpaths.push(c)
		this._classpaths.extend(ob.classpaths());
		
		this.libs.extend(ob.libs);
		defines.extend(ob.defines);
		if (this.main == null) {
			this.main = ob.main;
		}
		if (this.name == null) {
			this.name = ob.name;
		}
	}
	
	public function copy () 
	{

		this.get_types();

		var hb = new HxmlBuild(this._hxml, this.build_file());
		hb._args = this.args().copy();
		hb.main = this.main;
		hb.name = this.name;
		hb._target = this._target;
		hb.output = this.output;
		hb.defines = this.defines.copy();
		hb._std_bundle = this._std_bundle;
		hb._classpaths = this._classpaths.copy();
		hb.libs = this.libs.copy();
		hb.type_bundle = this.type_bundle;
		hb._update_time = this._update_time;
		hb.show_times = this.show_times;
		hb.mode_completion = this.mode_completion;
		return hb;
	}
	public function add_arg(arg:Tup2<String,String>) 
	{
		this._args.push(arg);
	}

	public function get_build_folder () 
	{
		return if (this.build_file != null) Path.dirname(this.build_file()) else null;
	}

	public function set_build_cwd () 
	{
		this.set_cwd(this.get_build_folder());
	}
	
	public function align_drive_letter(path:String) 
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

	public function add_classpath (cp) 
	{
		var cp = this.align_drive_letter(cp);
		if (!Lambda.has(this._classpaths, cp)) {
			this._classpaths.push(cp);
			this._args.push(Tup2.create("-cp", cp));
		}
	}
	

	public function add_lib(lib:HaxeLibLibrary) 
	{
		this.libs.push(lib);
		this.add_arg( Tup2.create("-lib", lib.name));
	}

	public function get_classpath_of_file (file) 
	{
			
		var file = this.align_drive_letter(file);
		
		var cps = this._classpaths.copy();

		var build_folder = this.get_build_folder();
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

	public function is_file_in_classpath (file:String) 
	{
		file = this.align_drive_letter(file);
		return this.get_classpath_of_file(file) != null;
	}

	public function get_relative_path (file:String) 
	{
		file = this.align_drive_letter(file);



		var cp = this.get_classpath_of_file(file);

		trace(file);
		trace(file.replace(cp, ""));
		trace(file.replace(cp, "").substr(1));

		return if (cp != null) file.replace(cp, "").substr(1) else null;
	}

	public function target_to_string () 
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

	public function to_string()  
	{

		var out = Path.basename(this.output);
		var main = this.get_name();
		var target = this.target_to_string();
		return '$main ($target - $out)';
	}
	
	public function make_hxml()  
	{
		var outp = "# Autogenerated "+this.hxml+"\n\n";
		outp += "# "+this.to_string() + "\n";
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

	public function set_cwd (cwd:String) 
	{
		this._args.push(Tup2.create("--cwd" , cwd ));
	}

	public function set_times () 
	{
		this.show_times = true;
		this._args.push(Tup2.create("--times", ""));
		this._args.push(Tup2.create("-D", "macro-times"));
		this._args.push(Tup2.create("-D", "macro_times"));
	}

	public function set_server_mode (server_port = 6000) 
	{
		this._args.push(Tup2.create("--connect" , Std.string(server_port)));
	}

	public function get_command_args (haxe_path:Array<String>) 
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

	public function set_auto_completion (display, macro_completion = false, no_output = true) 
	{
		
		this.mode_completion = true;

		var args = this._args;

		this.main = null;

		function filterTargets (x:Tup2<String,String>) 
		{
			return x._1 != "-cs" && x._1 != "-x" && x._1 != "-js" && x._1 != "-php" && x._1 != "-cpp" && x._1 != "-swf" && x._1 != "-java";
		}

		if (macro_completion) 
		{
			args = args.filter(filterTargets ).copy();
		}
		else 
		{
			args = args.map(function (x) return if (x._1 == "-x") Tup2.create("-neko", x._2) else x).copy();
		}

		function filter_commands_and_dce (x:Tup2<String,String>) 
		{
			return x._1 != "-cmd" && x._1 != "-dce";
		}


		args = args.filter(filter_commands_and_dce );

		if (!this.show_times) 
		{
			function filter_times (x:Tup2<String,String>) 
			{
				return x._1 != "--times";
			}
			args = args.filter(filter_times).copy();
		}

		if (macro_completion) 
		{
			args.push(Tup2.create("-neko", "__temp.n"));
		}

		
		args.push( Tup2.create("--display", display ) );
		if (no_output) 
		{
			args.push( Tup2.create("--no-output" , "") );
		}

		this._args = args;
	}


	public function _update_types() 
	{

		// haxe.output_panel.HaxePanel.status("haxe-debug", "updating types")
		trace("update types for classpaths:" + Std.string(this._classpaths));
		trace("update types for libs:" + Std.string(this.libs));
		this.type_bundle = Types.find_types(this._classpaths, this.libs, this.get_build_folder(), [], [], false );
	}

		


	public function _should_refresh_types(now) 
	{
		
		// if this._update_time != null:
		// 	trace("update_diff:" + str(now - this._update_time))
		// 	trace("update_diff:" + str((now - this._update_time > 100)))
		return this.type_bundle == null || this._update_time == null || (now - this._update_time) > 10;
	}

	public function get_types()  
	{
		var now = Time.time();
		
		if (this._should_refresh_types(now)) {
			trace("UPDATE THE TYPES NOW");
			this._update_time = now;
			this._update_types();
		}

		return this.type_bundle;
	}

	public function prepare_check_cmd(project, server_mode, view) 
	{
		var r = this.prepare_build_cmd(project, server_mode, view);
		var cmd = r._1, build_folder = r._2;
		cmd.push("--no-output");
		return Tup2.create(cmd, build_folder);
	}
	
	public function absolute_output() 
	{
		if (Path.isabs(this.output)) {
			return this.output;
		}
		else {
			return this.get_build_folder() + "/" + this.output;
		}
	}
		
	public function prepare_run_cmd (project:Project, server_mode:Bool, view:View):Tup2<Array<String>, String>
	{
		var r = this._prepare_run(project, view, server_mode);
		var cmd = r._1, build_folder = r._2, nekox_file = r._3;

		trace(this.args);
		trace(cmd);
		trace(build_folder);
		trace(nekox_file);
		
		var default_open_ext = Settings.open_with_default_app();

		if (nekox_file != null) 
		{
			cmd.extend(["-cmd", "neko " + nekox_file]);
		}
		else if (this._target == "swf" && default_open_ext != null)
		{
			cmd.extend(["-cmd", default_open_ext + " " + this.absolute_output()]);
		}
		else if (this._target == "neko")
		{
			cmd.extend(["-cmd", "neko " + this.absolute_output()]);
		}
		else if (this._target == "cpp")
		{
			var sep_index = this.main.lastIndexOf(".");
			var exe = if (sep_index > -1) this.main.substr(sep_index+1) else this.main;
			cmd.extend(["-cmd", Path.join(this.absolute_output(),exe) + "-debug"]);
		}
		else if (this._target == "js" && Lambda.has(this.defines, "nodejs"))
		{
			cmd.extend(["-cmd", "nodejs " + this.absolute_output()]);
		}
		else if (this._target == "java")
		{
			var sep_index = this.absolute_output().lastIndexOf(Path.sep);
			var jar = if (sep_index == -1) this.absolute_output() + ".jar" else this.absolute_output().substr(sep_index+1) + ".jar";
			cmd.extend(["-cmd", "java -jar " + Path.join(this.absolute_output(), jar)]);
		}
		else if (this._target == "cs") 
		{
			cmd.extend(["-cmd", "cd " + this.absolute_output()]);
			cmd.extend(["-cmd", "gmcs -recurse:*.cs -main:" + this.main + " -out:" + this.main + ".exe-debug"]);
			cmd.extend(["-cmd", Path.join(".", this.main + ".exe-debug")]);
		}

		return Tup2.create(cmd, build_folder);
	}

	public function prepare_build_cmd (project:Project, server_mode:Bool, view:View) 
	{
		var r = this._prepare_run(project, view, server_mode);
		var cmd = r._1, build_folder = r._2;
		return Tup2.create(cmd, build_folder);
	}

	public function _prepare_run (project:Project, view:View, server_mode:Null<Bool> = null):Tup3<Array<String>, String, String>
	{

		server_mode = if (server_mode == null) project.is_server_mode() else server_mode;
		
		var run_exec = this._get_run_exec(project, view);
		var b = this.copy();
		
		var nekox_file_name = null;
		
		for (i in 0...b._args.length) 
		{
			var a = b._args[i];
			if (a._1 == "-x") {
				nekox_file_name = a._2 + ".n";
				b._args[i] = Tup2.create("-neko", nekox_file_name);
			}
		}

		if (server_mode) {
			project.start_server( view );
			b.set_server_mode(project.server.get_server_port());
		}

		
		b.set_build_cwd();
		var cmd = b.get_command_args(run_exec);

		return Tup3.create(cmd, this.get_build_folder(), nekox_file_name);
	}

	public function _get_run_exec(project:Project, view:View) 
	{
		return project.haxe_exec(view);
	}

	public function escape_cmd(cmd:Array<String>) 
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

	public function _run_async (project:Project, view:View, callback:String->String->Void, server_mode:Null<Bool> = null) 
	{
		var env = project.haxe_env(view);
		var r = this._prepare_run(project, view, server_mode);
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
			this._on_run_complete(out, err, build_folder, nekox_file_name);
			callback(out, err);
		}

		Execute.run_cmd_async( cmd, cb, "", build_folder, env );
	}
	
	

	public function _run_sync (project:Project, view:View, server_mode:Null<Bool> = null) 
	{
		var env = project.haxe_env(view);
		var r = this._prepare_run(project, view, server_mode);
		var cmd = r._1; 
		var build_folder = r._2; 
		var nekox_file_name = r._3;

		trace(cmd.join(" "));
		var r = Execute.run_cmd( cmd, "", build_folder, env );
		var out = r._1, err = r._2;
		
		this._on_run_complete(out, err, build_folder, nekox_file_name);
		
		return Tup2.create(out,err);
	}


	public function _on_run_complete(out, err, build_folder, nekox_file_name) 
	{
		trace("---------------cmd-------------------");
		trace("out:" + out);
		trace("err:" + err);
		trace("---------compiler-output-------------");
		if (nekox_file_name != null) 
		{
			this._run_neko_x(build_folder, nekox_file_name);
		}
	}
		

	public function _run_neko_x(build_folder:String, neko_file_name:String) 
	{
		var neko_file = Path.join(build_folder, neko_file_name);
		trace("run nekox: " + neko_file) ;
		var r = Execute.run_cmd(["neko", neko_file]);
		var out = r._1, err = r._2;
		Panels.default_panel().writeln(out);
		Panels.default_panel().writeln(err);
	}

	public function run(project:Project, view:View, async:Bool, callback:String->String->Void, server_mode = null) 
	{
		if (async) {
			trace("RUN ASYNC COMPLETION");
			this._run_async( project, view, callback, server_mode );
		}
		else {
			trace("RUN SYNC COMPLETION");
			var r = this._run_sync( project, view, server_mode );
			var out = r._1;
			var err = r._2;
			callback(out, err);
		}
	}

	@lazyFunction
	public function is_type_available (type:HaxeType) 
	{
		var pack = type.toplevel_pack();
		return pack == null || this.is_pack_available(pack);
	}

	@lazyFunction
	public function is_pack_available (pack:String) 
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
