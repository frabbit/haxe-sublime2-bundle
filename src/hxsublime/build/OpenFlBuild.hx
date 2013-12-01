package hxsublime.build;

import hxsublime.build.HxmlBuild;
import hxsublime.macros.LazyFunctionSupport;
import hxsublime.project.Project;
import hxsublime.tools.HxSrcTools.HaxeType;
import sublime.View;

using python.lib.ArrayTools;

class OpenFlBuild extends NmeBuild implements LazyFunctionSupport 
{
	
	public function new (project:Project, title:String, openfl_xml:String, target, cb:HxmlBuild = null)
	{
		super(project, title, openfl_xml, target, cb);
	}
	
	override public function copy ()
	{
		var hxml_copy = if (this._hxmlBuild != null) this.hxmlBuild().copy() else null;
		var r = new OpenFlBuild(this.project, this.title(), this.nmml, this.target(), hxml_copy);
		
		return r;
	}
	
	override public function getExecutable(project:Project, view:View)
	{
		return project.openflExec(view);
	}
	
	//public function filterPlatformSpecific(packs_or_classes:Array<String>)
	//{
	//	var res = [];
	//	for (c in packs_or_classes) {
	//		// allow only flash package
	//		if (!hxsublime.tools.StringTools.startsWithAny(c,["native", "browser", "nme"]))
	//		{
	//			res.push(c);
	//		}
	//	}
	//	return res;
	//}
	
	override public function toString() 
	{
		// out = os.path.basename(this.hxml_build.output)
		var out = this.title();
		var target = this.target().name;
		return '${out} (OpenFL - ${target})';
	}
	
	//@lazyFunction
	override public function isTypeAvailable (type:HaxeType)
	{
		var pack = type.toplevelPack();
		return pack == null || this.isPackAvailable(pack);
	}
	//@lazyFunction
	override public function isPackAvailable (pack:String)
	{
		if (pack == "")
		{
			return true;
		}

		var pack = pack.split(".")[0];
		var target = this.hxmlBuild().target;

		var tp = Config.target_packages.copy();
		tp.extend(["native", "browser", "nme"]);

		var no_target_pack = !Lambda.has(tp, pack);
		var is_flash_pack = pack == "flash";

		var available = target == null || no_target_pack || is_flash_pack;

		return available;
	}
}
