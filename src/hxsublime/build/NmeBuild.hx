package hxsublime.build;

import hxsublime.build.Build;
import hxsublime.build.HxmlBuild;
import hxsublime.Config;
import hxsublime.Config.Target;
import hxsublime.macros.LazyFunctionSupport;
import hxsublime.project.Project;
import hxsublime.tools.HxSrcTools.HaxeType;
import python.lib.os.Path;
import python.Tuple;
import sublime.Sublime;
import sublime.View;


using StringTools;

using hxsublime.support.ArrayTools;

class NmeBuild implements Build implements LazyFunctionSupport {


	var _title : String;
	var _target:Target;
	var _hxmlBuild : HxmlBuild;

	public var nmml : String;
	public var project : Project;

	public function new (project:Project, title:String, nmml:String, target, cb:HxmlBuild = null)
	{
		this._title = title;
		this._target = target;
		this.nmml = nmml;
		this._hxmlBuild = cb;
		this.project = project;
	}

	public function setHxml (hxml:String) {
		this.hxmlBuild().setHxml(hxml);
	}

	public function makeHxml()  {
		return this.hxmlBuild().makeHxml();
	}

	@property
	public function title()
	{
		return this._title;
	}

	@property
	public function buildFile()
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

	function getHxmlBuildWithNmeDisplay()
	{
		var view = Sublime.active_window().active_view();
		var display_cmd = this.getBuildCommand(this.project, view).copy();
		display_cmd.push("display");

		return Tools.createHaxeBuildFromNmml(this.project, this._target, this.nmml, display_cmd);
	}


	public function hxmlBuild ()
	{

		if (this._hxmlBuild == null)
		{
			this._hxmlBuild = this.getHxmlBuildWithNmeDisplay();
		}

		return this._hxmlBuild;
	}

	public function toString()
	{
		var title = this.title();
		var target = this.target().name;
		return '${title} (NME - ${target})';

	}

	public function setStdBundle(std_bundle)
	{
		this.hxmlBuild().setStdBundle(std_bundle);
	}

	function _filter_platform_specific(packs_or_classes:Array<String>)
	{
	 	var res = [];
	 	for (c in packs_or_classes) {
	 		if (!c.startsWith("native") && !c.startsWith("browser") && !c.startsWith("flash") && !c.startsWith("flash9") && !c.startsWith("flash8")) {
	 			res.push(c);
	 		}
	 	}
	 	return res;
	}
	public function getTypes()
	{
		var bundle = this.hxmlBuild().getTypes();
		return bundle;
	}

	@property
	public function stdBundle()
	{
		return this.hxmlBuild().stdBundle();
	}

	public function addArg(arg)
	{
		this.hxmlBuild().addArg(arg);
	}

	public function copy ()
	{
		var hxmlCopy = if (this._hxmlBuild != null) this.hxmlBuild().copy() else null;

		return new NmeBuild(this.project, this.title(), this.nmml, this._target, hxmlCopy);
	}

	public function getRelativePath(file:String)
	{
		return this.hxmlBuild().getRelativePath(file);
	}

	public function getBuildFolder()
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

	public function setAutoCompletion(display:String, ?macro_completion = false, ?no_output = true)
	{
		this.hxmlBuild().setAutoCompletion(display, macro_completion, no_output);
	}

	public function setTimes()
	{
		this.hxmlBuild().setTimes();
	}

	public function addDefine (define:String)
	{
		this.hxmlBuild().addDefine(define);
	}

	public function addClasspath(cp:String)
	{
		this.hxmlBuild().addClasspath(cp);
	}

	public function run(project:Project, view:View, async:Bool, on_result:String->String->Void, server_mode:Null<Bool> = null)
	{
		this.hxmlBuild().run(project, view, async, on_result, server_mode);
	}

	function getExecutable(project:Project, view:View)
	{
		return project.nmeExec(view);
	}

	function getBuildCommand(project:Project, view:View)
	{
		return this.getExecutable(project, view).copy();
	}

	public function escapeCmd(cmd:Array<String>)
	{
		return this.hxmlBuild().escapeCmd(cmd);
	}

	public function prepareCheckCmd(project:Project, server_mode:Bool, view:View)
	{
		var r = this.prepareBuildCmd(project, server_mode, view);
		var cmd = r._1, folder = r._2;
		cmd.push("--no-output");
		return Tuple2.make(cmd, folder);
	}

	public function prepareBuildCmd(project:Project, server_mode:Bool, view:View)
	{
		return prepareCmd(project, server_mode, view, "build");
	}

	public function prepareRunCmd (project:Project, server_mode:Bool, view:View)
	{
		return prepareCmd(project, server_mode, view, "test");
	}

	function prepareCmd(project:Project, server_mode:Bool, view:View, command:String)
	{
		var cmd = getBuildCommand(project, view);

		cmd.push(command);
		cmd.push(this.buildFile());
		cmd.push(this.target().plattform);
		cmd.extend(this.target().args);

		if (server_mode)
		{
			cmd.extend(["--connect", Std.string(project.server.get_server_port())]);
		}

		return Tuple2.make(cmd, this.getBuildFolder());
	}


	public function classpaths ()
	{
		return this.hxmlBuild().classpaths();
	}


	public function args ()
	{
		return this.hxmlBuild().args();
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

		var pack = pack.split(".")[0];
		var target = this.hxmlBuild().target;

		var tp = Config.target_packages.concat(["native", "browser", "nme"]);

		var noTargetPack = !Lambda.has(tp, pack);
		var isNmePack = pack == "nme";

		var available = target == null || noTargetPack || isNmePack;

		return available;
	}
}
