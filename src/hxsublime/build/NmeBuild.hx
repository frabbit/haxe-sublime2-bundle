package hxsublime.build;

import hxsublime.build.HxmlBuild;
import hxsublime.Config;
import hxsublime.Config.Target;
import hxsublime.project.Project;
import hxsublime.tools.HxSrcTools.HaxeType;
import python.lib.os.Path;
import python.lib.Types.Tup2;
import sublime.Sublime;
import sublime.View;


using StringTools;

using python.lib.ArrayTools;

class NmeBuild {

	
	var _title : String;
	var _target:Target;
	var _hxml_build : HxmlBuild;

	public var nmml : String;
	public var project : Project;

	public function new (project:Project, title:String, nmml:String, target, cb:HxmlBuild = null)
	{
		this._title = title;
		this._target = target;
		this.nmml = nmml;
		this._hxml_build = cb;
		this.project = project;
	}

	public function setHxml (hxml:String) {
		this.hxml_build().setHxml(hxml);
	}

	public function make_hxml()  {
		return this.hxml_build().make_hxml();
	}

	@property
	public function title()
	{
		return this._title;
	}

	@property
	public function build_file()
	{
		return this.nmml;
	}

	@property
	public function target()
	{
		return this._target;
	}

	@property
	public function plattform()
	{
		return this._target.plattform;
	}

	public function _get_hxml_build_with_nme_display()
	{
		var view = Sublime.active_window().active_view();
		var display_cmd = this.get_build_command(this.project, view).copy();
		display_cmd.push("display");
		//from haxe.build.tools import create_haxe_build_from_nmml
		return Tools.create_haxe_build_from_nmml(this.project, this._target, this.nmml, display_cmd);
	}

	@property
	public function hxml_build ()
	{
		trace("create hxml build");
		if (this._hxml_build == null) 
		{
			this._hxml_build = this._get_hxml_build_with_nme_display();
		}

		return this._hxml_build;
	
	}

	public function to_string() 
	{
		var title = this.title();
		var target = this.target().name;
		return '${title} (NME - ${target})';
		
	}

	public function set_std_bundle(std_bundle)
	{
		this.hxml_build().set_std_bundle(std_bundle);
	}

	public function _filter_platform_specific(packs_or_classes:Array<String>)
	{
	 	var res = [];
	 	for (c in packs_or_classes) {
	 		if (!c.startsWith("native") && !c.startsWith("browser") && !c.startsWith("flash") && !c.startsWith("flash9") && !c.startsWith("flash8")) {
	 			res.push(c);
	 		}
	 	}
	 	return res;
	}
	public function get_types()
	{
		var bundle = this.hxml_build().get_types();
		return bundle;
	}

	@property
	public function std_bundle()
	{
		return this.hxml_build().std_bundle();
	}

	public function add_arg(arg)
	{
		this.hxml_build().add_arg(arg);
	}

	public function copy ()
	{
		var hxml_copy = if (this._hxml_build != null) this.hxml_build().copy() else null;

		return new NmeBuild(this.project, this.title(), this.nmml, this._target, hxml_copy);
	}

	public function get_relative_path(file:String)
	{
		return this.hxml_build().get_relative_path(file);
	}

	public function get_build_folder()
	{
		var r = null;
		if (this.nmml != null) 
		{
			r = Path.dirname(this.nmml);
		}
		trace("build_folder: " + Std.string(r));
		trace("nmml: " + Std.string(this.nmml));
		return r;
	}

	public function set_auto_completion(display:String, macro_completion = false, no_output = true)
	{
		this.hxml_build().set_auto_completion(display, macro_completion, no_output);
	}

	public function set_times()
	{
		this.hxml_build().set_times();
	}

	public function add_define (define:String)
	{
		this.hxml_build().add_define(define);
	}

	public function add_classpath(cp:String)
	{
		this.hxml_build().add_classpath(cp);
	}

	public function run(project:Project, view:View, async:Bool, on_result:String->String->Void, server_mode:Null<Bool> = null)
	{
		this.hxml_build().run(project, view, async, on_result, server_mode);
	}

	public function _get_run_exec(project:Project, view:View)
	{
		return project.nme_exec(view);
	}

	public function get_build_command(project:Project, view:View)
	{
		return this._get_run_exec(project, view).copy();
	}

	public function escape_cmd(cmd:Array<String>) {
		return this.hxml_build().escape_cmd(cmd);
	}

	public function prepare_check_cmd(project:Project, server_mode:Bool, view:View)
	{
		var r = this.prepare_build_cmd(project, server_mode, view);
		var cmd = r._1, folder = r._2;
		cmd.push("--no-output");
		return Tup2.create(cmd, folder);
	}

	public function prepare_build_cmd(project:Project, server_mode:Bool, view:View)
	{
		return this._prepare_cmd(project, server_mode, view, "build");
	}

	public function prepare_run_cmd (project:Project, server_mode:Bool, view:View)
	{
		return this._prepare_cmd(project, server_mode, view, "test");
	}

	public function _prepare_cmd(project:Project, server_mode:Bool, view:View, command:String)
	{
		var cmd = this.get_build_command(project, view);

		cmd.push(command);
		cmd.push(this.build_file());
		cmd.push(this.target().plattform);
		cmd.extend(this.target().args);

		if (server_mode) 
		{
			cmd.extend(["--connect", Std.string(project.server.get_server_port())]);
		}

		return Tup2.create(cmd, this.get_build_folder());
	}

	public function _prepare_run(project:Project, view, server_mode)
	{
		return this.hxml_build()._prepare_run(project, view, server_mode);
	}

	@property
	public function classpaths ()
	{
		return this.hxml_build().classpaths();
	}

	@property
	public function args ()
	{
		return this.hxml_build().args();
	}

	public function is_type_available (type:HaxeType)
	{
		var pack = type.toplevel_pack();
		return pack == null || this.is_pack_available(pack);
	}

	public function is_pack_available (pack:String)
	{

		if (pack == "") 
		{
			return true;
		}

		var pack = pack.split(".")[0];
		var target = this.hxml_build().target;
		
		var tp = Config.target_packages.copy();
		tp.extend(["native", "browser", "nme"]);

		var no_target_pack = !Lambda.has(tp, pack);
		var is_nme_pack = pack == "nme";

		var available = target == null || no_target_pack || is_nme_pack;

		return available;
	}
}

/*

import os
import sublime 
from haxe import config

from haxe.log import log

from haxe.tools.stringtools import encode_utf8


*/