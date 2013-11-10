
package hxsublime.build;

import hxsublime.Config.Target;
import hxsublime.project.Project;
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
	public function hxml():String;
	public function make_hxml():String;
	public function prepare_check_cmd(project:Project, server_mode:Bool, view:View):Tup2<Array<String>, String>; 
	public function prepare_build_cmd(project:Project, server_mode:Bool, view:View):Tup2<Array<String>, String>;
	public function prepare_run_cmd(project:Project, server_mode:Bool, view:View):Tup2<Array<String>, String>; 
	public function escape_cmd (cmd:Array<String>):Array<String>;
	public var target:String;
}