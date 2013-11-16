
package sublime.def.exec;

import python.lib.io.FileIO;
import python.lib.Types.Bytes;
import sublime.def.exec.AsyncProcess;




@:keep extern interface ProcessListener 
{
    public function on_data(proc:AsyncProcess, data:Bytes):Void;

    public function on_finished(proc:AsyncProcess):Void;

    @:keep public static function __init__ ():Void 
	{
		untyped __python__("import Default");
		//untyped __python__("_hx_stexec = getattr(Default, 'exec')");
		
		untyped __python__("sublime_def_exec_ProcessListener = getattr(Default, 'exec').ProcessListener");
		
	}
}