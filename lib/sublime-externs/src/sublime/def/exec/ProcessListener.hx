
package sublime.def.exec;

import python.lib.io.FileIO;
import sublime.def.exec.AsyncProcess;




@:keep extern interface ProcessListener 
{
    public function on_data(proc:AsyncProcess, data:String):Void;

    public function on_finished(proc:AsyncProcess):Void;

    @:keep public static function __init__ ():Void 
	{
		untyped __python__("import Default");
		untyped __python__("_hx_stexec = getattr(Default, 'exec')");
		python.Macros.importFromAs("_hx_stexec","ProcessListener", "sublime.def.exec.ProcessListener");
	}
}