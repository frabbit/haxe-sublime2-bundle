
package sublime.def.exec;

import python.lib.io.FileIO;
import python.Bytes;
import sublime.def.exec.AsyncProcess;

@:pythonImport("Default.exec", "ProcessListener")
extern interface ProcessListener
{
    public function on_data(proc:AsyncProcess, data:Bytes):Void;

    public function on_finished(proc:AsyncProcess):Void;
}