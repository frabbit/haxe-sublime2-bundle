package hxsublime.build;

import hxsublime.build.HxmlBuild;
import hxsublime.project.Project;
import sublime.View;

using python.lib.ArrayTools;

class OpenFlBuild extends NmeBuild 
{
	
	public function new (project:Project, title:String, openfl_xml:String, target, cb:HxmlBuild = null)
	{
		super(project, title, openfl_xml, target, cb);
	}
	
	override public function copy ()
	{
		var hxml_copy = if (this._hxml_build != null) this.hxml_build().copy() else null;
		var r = new OpenFlBuild(this.project, this.title(), this.nmml, this.target(), hxml_copy);
		
		return r;
	}
	
	override public function _get_run_exec(project:Project, view:View)
	{
		return project.openfl_exec(view);
	}
	
	public function filter_platform_specific(packs_or_classes:Array<String>)
	{
		var res = [];
		for (c in packs_or_classes) {
			// allow only flash package
			if (!hxsublime.tools.StringTools.startsWithAny(c,["native", "browser", "nme"]))
			{
				res.push(c);
			}
		}
		return res;
	}
	
	override public function to_string() 
	{
		// out = os.path.basename(this.hxml_build.output)
		var out = this.title;
		var target = this.target().name;
		return '${out} (OpenFL - ${target})';
	}
	
	override public function is_type_available (type)
	{
		var pack = type.toplevel_pack;
		return pack == null || this.is_pack_available(pack);
	}
	
	override public function is_pack_available (pack:String)
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
		var is_flash_pack = pack == "flash";

		var available = target == null || no_target_pack || is_flash_pack;

		return available;
	}
}

/*

from haxe import config

from haxe.tools import stringtools

from haxe.log import log

from haxe.build.nmebuild import NmeBuild


*/