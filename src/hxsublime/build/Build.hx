package hxsublime.build;

import hxsublime.completion.hx.CompletionContext;
import hxsublime.Config.Target;
import hxsublime.project.Project;
import hxsublime.tools.HxSrcTools.HaxeType;
import hxsublime.tools.HxSrcTools.HaxeTypeBundle;
import python.Tuple;
import sublime.View;

interface Build {

	public function setHxml (hxml:String):Void;
	public function getRelativePath(path:String):String;
	public function setStdBundle(bundle:HaxeTypeBundle):Void;
	public function toString():String;
	public function copy():Build;
	public function buildFile():String;
	public function addClasspath(cp:String):Void;
	//public function hxml():String;
	public function makeHxml():String;
	public function prepareCheckCmd(project:Project, server_mode:Bool, view:View):Tuple2<Array<String>, String>;
	public function prepareBuildCmd(project:Project, server_mode:Bool, view:View):Tuple2<Array<String>, String>;
	public function prepareRunCmd(project:Project, server_mode:Bool, view:View):Tuple2<Array<String>, String>;
	public function escapeCmd (cmd:Array<String>):Array<String>;
	public function isTypeAvailable(t:HaxeType):Bool;
	public function isPackAvailable(p:String):Bool;
	public function getTypes():HaxeTypeBundle;
	public function getBuildFolder():String;
	public function setAutoCompletion(display:String, ?macro_completion:Bool, ?no_output:Bool):Void;
	public function setTimes():Void;
	public function run(project:Project, view:View, async:Bool, onResult:String->String->Void, ?serverMode:Null<Bool>):Void;
	public function stdBundle():HaxeTypeBundle;
	public function target():Target;
	public function classpaths():Array<String>;
	public function args():Array<Tuple2<String, String>>;
	public function addArg(a:Tuple2<String, String>):Void;
	//public var ctx:CompletionContext;
}