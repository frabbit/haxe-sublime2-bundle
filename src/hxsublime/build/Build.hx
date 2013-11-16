
package hxsublime.build;

import hxsublime.completion.hx.Types.CompletionContext;
import hxsublime.Config.Target;
import hxsublime.project.Project;
import hxsublime.tools.HxSrcTools.HaxeType;
import hxsublime.tools.HxSrcTools.HaxeTypeBundle;
import python.lib.Types.Tup2;
import sublime.View;

typedef Build = {

	public function setHxml (hxml:String):Void;
	public function get_relative_path(path:String):String;
	public function set_std_bundle(bundle:HaxeTypeBundle):Void;
	public function to_string():String;
	public function copy():Build;
	public function build_file():String;
	public function add_classpath(cp:String):Void;
	//public function hxml():String;
	public function make_hxml():String;
	public function prepare_check_cmd(project:Project, server_mode:Bool, view:View):Tup2<Array<String>, String>; 
	public function prepare_build_cmd(project:Project, server_mode:Bool, view:View):Tup2<Array<String>, String>;
	public function prepare_run_cmd(project:Project, server_mode:Bool, view:View):Tup2<Array<String>, String>; 
	public function escape_cmd (cmd:Array<String>):Array<String>;
	public function is_type_available(t:HaxeType):Bool;
	public function is_pack_available(p:String):Bool;
	public function get_types():HaxeTypeBundle;
	public function get_build_folder():String;
	public function set_auto_completion(display:String, ?macro_completion:Bool, ?no_output:Bool):Void;
	public function set_times():Void;
	public function run(project:Project, view:View, async:Bool, onResult:String->String->Void, ?serverMode:Null<Bool>):Void;
	public function std_bundle():HaxeTypeBundle;
	public function target():Target;
	public function classpaths():Array<String>;
	public function args():Array<Tup2<String, String>>;
	public function add_arg(a:Tup2<String, String>):Void;
	//public var ctx:CompletionContext;
}