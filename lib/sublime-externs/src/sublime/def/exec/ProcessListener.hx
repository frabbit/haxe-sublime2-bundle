
package sublime.def.exec;

import python.lib.io.FileIO;
import python.Bytes;
import sublime.def.exec.AsyncProcess;


@:keep extern interface ProcessListener
{
    public function on_data(proc:AsyncProcess, data:Bytes):Void;

    public function on_finished(proc:AsyncProcess):Void;

    public static function __init__ ():Void {
		python.Syntax.pythonCode("import Default");
		python.Syntax.pythonCode("stexec = getattr(Default, 'exec')");
		python.Syntax.pythonCode("sublime_def_exec_ProcessListener = stexec.ProcessListener");
	}
}