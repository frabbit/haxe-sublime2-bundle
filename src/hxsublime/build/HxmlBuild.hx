package hxsublime.build;

import hxsublime.Haxelib.HaxeLibLibrary;
import hxsublime.project.Project;
import hxsublime.tools.HxSrcTools.HaxeTypeBundle;
import python.lib.os.Path;
import python.lib.Time;
import sublime.View;



class HxmlBuild {

	public var show_times:Bool;
	public var std_bundle:HaxeTypeBundle;
	public var args:Array<Tup2<String,String>>;
	public var main:String;
	public var target:String;
	public var output:String;
	public var hxml:String;
	public var _build_file:String;
	public var classpaths:Array<String>;
	public var libs:Array<HaxeLibLibrary>;
	public var type_bundle:HaxeTypeBundle;
	public var _update_time;
	public var mode_completion:Bool;
	public var defines:Array<String>;
	public var name:String;

	public function __init__(hxml, build_file)  
	{
		
		this.show_times = false;
		this.std_bundle = hxsrctools.empty_type_bundle();
		this.args = [];
		this.main = null;
		this.target = null;
		this.output = "dummy.js";
		this.hxml = hxml;
		this._build_file = build_file;
		this.classpaths = [];
		this.libs = [];
		this.type_bundle = null;
		this._update_time = null;
		this.mode_completion = false;
		this.defines = [];
		this.name = null;
	}
		

	@property
	public function title() 
	{
		return this.output;
	}

	

	@property
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
			n = this.name
		}
		else {
			n = if (this.main == null) "[No Main]" else this.main;
		}
		return n
	}

	public function set_std_bundle(std_bundle) 
	{
		this.std_bundle = std_bundle
	}

	
	public function equals (other) 
	{
		
		return (this.args == other.args 
			&& this.main == other.main
			&& this.name == other.name
			&& this.target == other.target
			&& this.output == other.output
			&& this.hxml == other.hxml
			&& this.classpaths == other.classpaths
			&& this.libs == other.libs
			&& this.show_times == other.show_times
			&& this.mode_completion == other.mode_completion
			&& this.defines == other.defines
			&& this._build_file == other._build_file)
	}
		   
	public function merge (other_build) 
	{
		ob = other_build
		this.args.extend(ob.args)

		//for c in ob.classpaths:
		//	if c !in this.classpaths:
		//		this.classpaths.push(c)
		this.classpaths.extend(ob.classpaths)
		
		this.libs.extend(ob.libs);
		this.defines = defines.extend(ob.defines);
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

		var hb = new HxmlBuild(this.hxml, this.build_file);
		hb.args = this.args.copy();
		hb.main = this.main;
		hb.name = this.name;
		hb.target = this.target;
		hb.output = this.output;
		hb.defines = this.defines.copy();
		hb.std_bundle = this.std_bundle;
		hb.classpaths = this.classpaths.copy();
		hb.libs = this.libs.copy();
		hb.type_bundle = this.type_bundle;
		hb._update_time = this._update_time;
		hb.show_times = this.show_times;
		hb.mode_completion = this.mode_completion;
		return hb;
	}
	public function add_arg(arg:String) 
	{
		this.args.push(arg);
	}

	public function get_build_folder () 
	{
		return if (this.build_file != null) Path.dirname(this.build_file) else null;
	}

	public function set_build_cwd () 
	{
		this.set_cwd(this.get_build_folder());
	}
	
	public function align_drive_letter(path) 
	{
		var is_win =  sublime.platform() == "windows"
		
		if (is_win) {
			var reg = re.compile("^([a-z]):(.*)$");
			var match = re.match(reg, path);
			if (match != null) {
				path = match.group(1).upper() + ":" + match.group(2);
			}
		}
		return path
	}

	public function add_classpath (cp) 
	{
		var cp = this.align_drive_letter(cp);
		if (!cp in this.classpaths) {
			this.classpaths.push(cp)
			this.args.push(Tup2.create("-cp", cp))
		}
	}
	

	public function add_lib(lib:HaxeLibLibrary) 
	{
		this.libs.push(lib)
		this.add_arg( Tup2.create("-lib", lib.name))
	}

	public function get_classpath_of_file (file) 
	{
		var file = st2_to_unicode(file);
		
		var file = this.align_drive_letter(file);
		
		var cps = this.classpaths.copy();

		build_folder = this.get_build_folder()
		if (build_folder != null && !Lambda.has(cps, build_folder)) 
		{
			trace("add build folder to classpaths: " + build_folder + ", classpaths: " + Std.string(cps))
			cps.push(build_folder);
		}
		for (cp in cps) 
		{
			var prefix = Path.commonprefix([cp, file]);
			if (prefix == cp) {
				return cp;
			}
		}

		return null
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

		return if (cp != null) file.replace(cp, "")[1:] else null
	}

	public function target_to_string () 
	{
		if (this.target == null) {
			target = "js";
		}
		else 
		{
			var target = this.target;
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
		var outp = "# Autogenerated "+this.hxml+"\n\n"
		outp += "# "+this.to_string() + "\n"
		outp += "-main "+ this.main + "\n"
		for (a in this.args) {
			outp += " ".join( list(a) ) + "\n";
		}
		
		var d = Path.dirname( this.hxml ) + "/"
		
		// relative paths
		outp = outp.replace( d , "")
		outp = outp.replace( "-cp "+Path.dirname( this.hxml )+"\n", "")

		outp = outp.replace("--no-output " , "")
		outp = outp.replace("-v" , "")

		outp = outp.replace("dummy" , this.main.lower() )

		return outp.strip()
	}

	public function set_cwd (cwd:String) 
	{
		this.args.push(Tup2.create("--cwd" , cwd ));
	}

	public function set_times () 
	{
		this.show_times = true
		this.args.push(Tup2.create("--times", ""))
		this.args.push(Tup2.create("-D", "macro-times"))
		this.args.push(Tup2.create("-D", "macro_times"))
	}

	public function set_server_mode (server_port = 6000) 
	{
		this.args.push(Tup2.create("--connect" , str(server_port)))
	}

	public function get_command_args (haxe_path) 
	{
		cmd = list(haxe_path)

		for a in this.args :
			cmd.extend( list(a) )

		for l in this.libs :
			cmd.push( "-lib" )
			cmd.push( l.as_cmd_arg() )

		if this.main != null:
			cmd.push("-main")
			cmd.push(this.main)
		return cmd
	}

	public function set_auto_completion (display, macro_completion = false, no_output = true) 
	{
		
		this.mode_completion = true;

		var args = this.args;

		this.main = null;

		public function filterTargets (x) 
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

		function filter_commands_and_dce (x) 
		{
			return x._1 != "-cmd" && x._1 != "-dce"
		}


		args = list(filter(filter_commands_and_dce, args ))

		if (!this.show_times) 
		{
			function filter_times (x) 
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

		this.args = args;
	}


	public function _update_types() 
	{

		// haxe.output_panel.HaxePanel.status("haxe-debug", "updating types")
		trace("update types for classpaths:" + Std.string(this.classpaths))
		trace("update types for libs:" + Std.string(this.libs))
		this.type_bundle = hxtypes.find_types(this.classpaths, this.libs, this.get_build_folder(), [], [], include_private_types = false )
	}

		


	public function _should_refresh_types(now) 
	{
		
		// if this._update_time != null:
		// 	trace("update_diff:" + str(now - this._update_time))
		// 	trace("update_diff:" + str((now - this._update_time > 100)))
		return this.type_bundle == null || this._update_time == null || (now - this._update_time) > 10
	}

	public function get_types()  
	{
		var now = Time.time()
		
		if (this._should_refresh_types(now)) {
			trace("UPDATE THE TYPES NOW")
			this._update_time = now
			this._update_types()
		}

		return this.type_bundle
	}

	public function prepare_check_cmd(project, server_mode, view) 
	{
		cmd, build_folder = this.prepare_build_cmd(project, server_mode, view)
		cmd.push("--no-output")
		return cmd, build_folder
	}
	

	@property
	public function absolute_output() 
	{
		if (Path.isabs(this.output)) {
			return this.output;
		}
		else {
			return this.get_build_folder() + "/" + this.output;
		}
	}
		

	public function prepare_run_cmd (project, server_mode, view) 
	{
		cmd, build_folder, nekox_file = this._prepare_run(project, view, server_mode)

		
		default_open_ext = hxsettings.open_with_default_app()

		if (nekox_file != null) 
		{
			cmd.extend(["-cmd", "neko " + nekox_file])
		}
		else if (this.target == "swf" && default_open_ext != null)
		{
			cmd.extend(["-cmd", default_open_ext + " " + this.absolute_output])
		}
		else if (this.target == "neko")
		{
			cmd.extend(["-cmd", "neko " + this.absolute_output])
		}
		else if (this.target == "cpp")
		{
			sep_index = this.main.rfind(".")
			exe = this.main[sep_index+1:] if sep_index > -1 else this.main
			cmd.extend(["-cmd", Path.join(this.absolute_output,exe) + "-debug"])
		}
		else if (this.target == "js" && "nodejs" in this.defines)
		{
			cmd.extend(["-cmd", "nodejs " + this.absolute_output])
		}
		else if (this.target == "java")
		{
			var sep_index = this.absolute_output.rfind(Path.sep)
			var jar = if (sep_index == -1) this.absolute_output + ".jar" else this.absolute_output.substr(sep_index+1) + ".jar";
			cmd.extend(["-cmd", "java -jar " + Path.join(this.absolute_output, jar)]);
		}
		else if (this.target == "cs") 
		{
			cmd.extend(["-cmd", "cd " + this.absolute_output])
			cmd.extend(["-cmd", "gmcs -recurse:*.cs -main:" + this.main + " -out:" + this.main + ".exe-debug"])
			cmd.extend(["-cmd", Path.join(".", this.main + ".exe-debug")])
		}

		return Tup2.create(cmd, build_folder);
	}

	public function prepare_build_cmd (project:Project, server_mode:Bool, view:View) 
	{
		cmd, build_folder,_ = this._prepare_run(project, view, server_mode);
		return Tup2.create(cmd, build_folder);
	}

	public function _prepare_run (project, view, server_mode:Null<Bool> = null) 
	{

		server_mode = if (server_mode == null) project.is_server_mode() else server_mode;
		
		run_exec = this._get_run_exec(project, view);
		b = this.copy()
		
		nekox_file_name = null
		
		for (i in 0...b.args.length) 
		{
			var a = b.args[i]
			if (a[0] == "-x") {
				nekox_file_name = a[1] + ".n"
				b.args[i] = Tup2.create("-neko", nekox_file_name);
			}
		}

		if (server_mode) {
			project.start_server( view )
			b.set_server_mode(project.server.get_server_port())
		}

		
		b.set_build_cwd()
		var cmd = b.get_command_args(run_exec)

		return Tup3.create(cmd, this.get_build_folder(), nekox_file_name)
	}

	public function _get_run_exec(project:Project, view:View) 
	{
		return project.haxe_exec(view)
	}

	public function escape_cmd(cmd:Array<String>) 
	{
		print_cmd = cmd.copy();
		l = print_cmd.length;
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
		cmd, build_folder, nekox_file_name = this._prepare_run(project, view, server_mode)
		var print_cmd = cmd.copy();
		for (i in 0...print_cmd.length) 
		{
			var e = print_cmd[i]
			if (e == "--macro" && i < len(print_cmd)-1)
			{
				print_cmd[i+1] = "'" + print_cmd[i+1] + "'";
			}
		}
		
		function cb (out, err) 
		{
			this._on_run_complete(out, err, build_folder, nekox_file_name)
			callback(out, err)
		}

		run_cmd_async( args=cmd, input="", cwd=build_folder, env=env, callback=cb )
	}
	
	

	public function _run_sync (project:Project, view:View, server_mode:Null<Bool> = null) 
	{
		var env = project.haxe_env(view)
		var r = this._prepare_run(project, view, server_mode)
		var cmd = r._1; 
		var build_folder = r._2; 
		var nekox_file_name = r._3;

		trace(" ".join(cmd))
		out, err = run_cmd( args=cmd, input="", cwd=build_folder, env=env )
		
		this._on_run_complete(out, err, build_folder, nekox_file_name)
		
		return out,err
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
		neko_file = Path.join(build_folder, neko_file_name);
		trace("run nekox: " + neko_file) ;
		out, err = run_cmd(["neko", neko_file]);
		hxpanel.default_panel().writeln(out);
		hxpanel.default_panel().writeln(err);
	}

	public function run(project:Project, view:View, async:Bool, callback:String->String->Void, server_mode = null) 
	{
		if (async) {
			trace("RUN ASYNC COMPLETION")
			this._run_async( project, view, callback, server_mode )
		}
		else {
			trace("RUN SYNC COMPLETION")
			var r = this._run_sync( project, view, server_mode );
			var out = r._1;
			var err = r._2;
			callback(out, err)
		}
	}

	public function is_type_available (type) 
	{
		var pack = type.toplevel_pack;
		return pack == null || this.is_pack_available(pack);
	}


	public function is_pack_available (pack) 
	{
		if (pack == "") 
		{
			return true;
		}

		pack = pack.split(".")[0];
		var target = this.target;

		var available = true;

		if (pack != null && target != null && pack in config.target_packages) 
		{
			if (target in config.target_std_packages) 
			{
				if (pack !in config.target_std_packages[target]) 
				{
					available = false;
				}
			}
		}
		return available;
	}
}

/*
import os
import re
import time
import sublime

from haxe import config
from haxe import types as hxtypes
from haxe import panel as hxpanel
from haxe.tools import hxsrctools
from haxe.tools.stringtools import to_unicode, encode_utf8, st2_to_unicode
from haxe import settings as hxsettings

from haxe.execute import run_cmd, run_cmd_async
from haxe.log import log



*/