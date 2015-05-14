package hxsublime.commands;

import hxsublime.tools.ViewTools;
import python.lib.Os;
import python.lib.os.Path;
import python.lib.Sys;
import python.lib.Time;
import python.Bytes;
import python.Dict;
import python.lib.FileObject;
import python.KwArgs;
import sublime.def.exec.AsyncProcess;
import sublime.def.exec.ProcessListener;
import sublime.Edit;
import sublime.Region;
import sublime.Sublime;
import sublime.View;
import sublime.Window;
import sublime.WindowCommand;


using StringTools;


using hxsublime.support.StringTools;

private class Helper
{
    public static function escape_cmd(cmd:Array<String>)
    {
        var print_cmd = cmd.copy();
        var l = print_cmd.length;
        for (i in 0...l)
        {
            var e = print_cmd[i];
            if (e == "--macro" && i < l-1)
            {
                print_cmd[i+1] = "'" + print_cmd[i+1] + "'";
            }
        }
        return print_cmd;
    }
}



@:keep class HaxeExecCommand extends WindowCommand implements ProcessListener
{

    var is_check_run:Bool;
    var output_view : View = null;
    var proc:AsyncProcess = null;
    var encoding:String;
    var quiet : Bool;

    public function new (window:Window) {
        super(window);
    }
    override public function run(kwArgs:KwArgs<Dynamic>)
    {
        var cmd:Array<String> = kwArgs.get("cmd", []);

        cmd = cmd.filter(function (x) return x != "");

        var file_regex:String = kwArgs.get("file_regex", "");
        var line_regex:String = kwArgs.get("line_regex", "");
        var working_dir:String = kwArgs.get("working_dir", "");
        this.encoding = kwArgs.get("encoding", "utf-8");

        var env:Dict<String,String> = kwArgs.get("env", new Dict());
        this.quiet = kwArgs.get("quiet", false);
        var kill:Bool = kwArgs.get("kill", false);
        var is_check_run:Bool = kwArgs.get("is_check_run", false);


        this.is_check_run = is_check_run;

        if (encoding == null)
        {
            encoding = Sys.getfilesystemencoding();
        }

        if (this.output_view == null)
        {
            // Try not to call get_output_panel until the regexes are assigned
            this.output_view = this.window.create_output_panel("exec");
            this.output_view.settings().set('word_wrap', true);
        }
        if (kill)
        {
            if (this.proc != null)
            {
                this.proc.kill();
                this.proc = null;
                this.append_data(null, "[Cancelled]".encode("utf-8"));
            }
            return;
        }



        // Default the to the current files directory if no working directory was given
        if (working_dir == "" && this.window.active_view() != null && this.window.active_view().file_name() != null)
        {
            working_dir = Path.dirname(this.window.active_view().file_name());
        }


        this.output_view.settings().set("result_file_regex", file_regex);
        this.output_view.settings().set("result_line_regex", line_regex);
        this.output_view.settings().set("result_base_dir", working_dir);

        // Call get_output_panel a second time after assigning the above
        // settings, so that it'll be picked up as a result buffer
        this.window.create_output_panel("exec");




        this.proc = null;
        if (!this.quiet) {

            function escape_arg(a:String)
            {
                var a = a.split('"').join('\\"');
                if (a.length >= 2) {
                    a = if (a.startsWith('\\"')) '"' + a.substr(2) else a;
                    a = if (a.endsWith('\\"')) a.substring(0, a.length-2) + '"' else a;
                }
                return a;
            }

            trace("Running Command: " + cmd.map(escape_arg ).join(" "));

            Sublime.status_message("Building");
        }


        var show_panel_on_build = Sublime.load_settings("Preferences.sublime-settings").get("show_panel_on_build", true);
        if (show_panel_on_build)
        {
            this.window.run_command("show_panel", python.Lib.anonToDict({"panel": "output.exec"}));
        }


        var merged_env = env.copy();
        if (this.window.active_view() != null)
        {
            var user_env = this.window.active_view().settings().get('build_env');
            if (user_env != null)
            {
                merged_env.update(user_env);
            }
        }

        // Change to the working dir, rather than spawning the process with it,
        // so that emitted working dir relative path names make sense
        if (working_dir != "")
        {
            Os.chdir(working_dir);
        }

        //var err_type = OSError;
        //if (os.name == "nt") {
        //    err_type = WindowsError
        //}

        try
        {
            // Forward kwargs to AsyncProcess

            //trace("CMD:" + Std.string(cmd));
            //trace("ENV:" + Std.string(merged_env));
            var d:Dict<String, Dynamic> = kwArgs;
            if (d.hasKey("working_dir")) d.remove("working_dir");
            if (d.hasKey("file_regex")) d.remove("file_regex");
            if (d.hasKey("line_regex")) d.remove("line_regex");
            if (d.hasKey("encoding")) d.remove("encoding");
            if (d.hasKey("is_check_run")) d.remove("is_check_run");
            if (d.hasKey("env")) d.remove("env");
            if (d.hasKey("cmd")) d.remove("cmd");
            //d.remove("line_regex");

            this.proc = new AsyncProcess(cmd, null, merged_env, this, "", false);

            this.append_data(this.proc, ("Running Command: " + Helper.escape_cmd(cmd).join(" ") + "\n").encode("utf-8"));
        }
        // TODO is it a good idea to catch all? see: http://stackoverflow.com/questions/4990718/python-about-catching-any-exception
        catch (e:Dynamic)
        {
            this.append_data_str(null, Std.string(e) + "\n");
            this.append_data_str(null, "[cmd:  " + Std.string(cmd) + "]\n");
            this.append_data_str(null, "[dir:  " + Os.getcwdb().decode("utf-8") + "]\n");
            if (merged_env.hasKey("PATH"))
            {
                this.append_data_str(null, "[path: " + merged_env.get("PATH", "") + "]\n");
            }
            else
            {
                this.append_data_str(null, "[path: " + Std.string(Os.environ.get("PATH", "")) + "]\n");
            }
            if (!this.quiet)
            {
                this.append_data_str(null, "[Finished]");
            }
        }
    }
    override public function is_enabled(kwArgs:KwArgs<Dynamic>):Bool
    {
        var kill = kwArgs.get("kill", false);
        if (kill)
        {
            return this.proc != null && this.proc.poll();
        }
        else
        {
            return true;
        }
    }


    public function append_data_str(proc, data:String) {
        this.append_data(proc, data.encode("utf-8"));
    }

    public function append_data(proc, data:Bytes)
    {

        if (proc != this.proc)
        {
            // a second call to exec has been made before the first one
            // finished, ignore it instead of intermingling the output.
            if (proc != null)
            {
                try
                {
                    proc.kill();
                }
                catch (e:Dynamic)
                {

                }
            }
            return;
        }

        var st = null;
        try
        {
            st = data.decode(this.encoding);
        }
        catch (e:Dynamic)
        {
            st = "[Decode error - output not " + this.encoding + "]\n";
            proc = null;
        }

        // quick and dirty workaround, nme and openfl display errors when --no-output is defined,
        // maybe we should move to normal haxe/hxml run with --no-output, this way we can also use server_mode caching
        if (this.is_check_run && st.indexOf("Embedding assets failed! We encountered an error accessing") > -1)
        {
            return;
        }

        // Normalize newlines, Sublime Text always uses a single \n separator
        // in memory.
        st = st.replace('\r\n', '\n').replace('\r', '\n');

        var sel = this.output_view.sel();
        var selection_was_at_end = (sel.length == 1 && sel[0] == new Region(this.output_view.size()));

        function do_edit(v:View, edit:Edit)
        {

            v.set_read_only(false);

            v.insert(edit, this.output_view.size(), st);
            if (selection_was_at_end)
            {
                v.show(this.output_view.size());
            }

            v.set_read_only(true);
        }
        ViewTools.asyncEdit(this.output_view, do_edit);
    }

    public function finish(proc:AsyncProcess)
    {

        var v = this.output_view;

        if (!this.quiet)
        {
            var elapsed = Time.time() - proc.start_time;
            var exit_code = proc.exit_code();


            if (exit_code == 0 || exit_code == null)
            {
                this.append_data_str(proc, '[Finished in ${Std.string(elapsed)}]');
            }
            else
            {
                this.append_data_str(proc, '[Finished in ${Std.string(elapsed)} with exit code ${exit_code}]');
            }
        }
        if (proc != this.proc)
        {
            return;
        }

        // Set the selection to the start, so that next_result will work as expected

        v.sel().clear();
        v.sel().add(new Region(0));
    }


    public function on_data(proc:AsyncProcess, data:Bytes):Void
    {
        Sublime.set_timeout(function () trace(data), 0);
        Sublime.set_timeout(this.append_data.bind(proc, data), 0);
    }

    public function on_finished(proc:AsyncProcess):Void
    {
        Sublime.set_timeout(this.finish.bind(proc), 0);
    }


}
