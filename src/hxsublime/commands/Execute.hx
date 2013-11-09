package hxsublime.commands;

import sublime.Edit;
import sublime.View;



interface ProcessListener 
{
    public function on_data(proc, data):Void;

    public function on_finished(proc):Void;
}

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



class HaxeExecCommand extends WindowCommand implements ProcessListener 
{

    var is_check_run:Bool;
    var output_view : View;

    public function run(kwArgs:KwArgs) 
    {

        var cmd:Array<String> = kwArgs.get("cmd", []);
        var file_regex:String = kwArgs.get("file_regex", "");
        var line_regex:String = kwArgs.get("line_regex", "");
        var working_dir:String = kwArgs.get("working_dir", "");
        var encoding:Null<String> = kwArgs.get("encoding", null);
        var env:Dict<String,String> = kwArgs.get("env", new Dict());
        var quiet:Bool = kwArgs.get("quiet", false);
        var kill:Bool = kwArgs.get("kill", false);
        var is_check_run:Bool = kwArgs.get("is_check_run", false);

        trace("ENV1: " + Std.string(env));


        this.is_check_run = is_check_run;

        if (encoding == null) 
        {
            encoding = sys.getfilesystemencoding()
        }

        trace("run haxe exec");
        if (kill) 
        {
            if (this.proc != null) 
            {
                this.proc.kill();
                this.proc = null;
                this.append_data(null, "[Cancelled]");
            }
            return;
        }

        if (this.output_view == null) 
        {
            // Try not to call get_output_panel until the regexes are assigned
            this.output_view = this.window.get_output_panel("exec");
            this.output_view.settings().set('word_wrap', true);
        }

        // Default the to the current files directory if no working directory was given
        if (working_dir == "" && this.window.active_view() != null && this.window.active_view().file_name() != null) 
        {
            working_dir = os.path.dirname(this.window.active_view().file_name());
        }


        this.output_view.settings().set("result_file_regex", file_regex);
        this.output_view.settings().set("result_line_regex", line_regex);
        this.output_view.settings().set("result_base_dir", working_dir);
        
        trace("WORKING DIR:" + working_dir);
        // Call get_output_panel a second time after assigning the above
        // settings, so that it'll be picked up as a result buffer
        this.window.get_output_panel("exec");

        this.encoding = encoding;
        this.quiet = quiet;

        this.proc = null;
        if (!this.quiet) {
            
            function escape_arg(a:String)
            {
                var a = a.split('"').join('\\"');
                if (a.length >= 2) {
                    a = if (a.startswith('\\"')) '"' + a[2:] else a;
                    a = if (a.endswith('\\"')) a[0:len(a)-2] + '"' else a;
                }
                return a;
            }

            trace("Running Command : " + " ".join(map(escape_arg, cmd)));

            sublime.status_message("Building")
        }


        var show_panel_on_build = sublime.load_settings("Preferences.sublime-settings").get("show_panel_on_build", true);
        if (show_panel_on_build) 
        {
            this.window.run_command("show_panel", {"panel": "output.exec"});
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
            os.chdir(working_dir);
        }

        //var err_type = OSError;
        //if (os.name == "nt") {
        //    err_type = WindowsError
        //}

        try 
        {
            // Forward kwargs to AsyncProcess
            
            trace("CMD:" + Std.string(cmd));
            trace("ENV:" + Std.string(merged_env));
            this.proc = new AsyncProcess(cmd, null, merged_env, this, untyped __python_kwargs__(kwargs));

            this.append_data(this.proc, "Running Command: " + _escape_cmd(cmd).join(" ") + "\n");
        }
        // TODO is it a good idea to catch all? see: http://stackoverflow.com/questions/4990718/python-about-catching-any-exception
        catch (e:Dynamic) 
        {
            this.append_data(null, Std.string(e) + "\n");
            this.append_data(null, "[cmd:  " + Std.string(cmd) + "]\n");
            this.append_data(null, "[dir:  " + Std.string(os.getcwdu()) + "]\n");
            if ("PATH" in merged_env) 
            {
                this.append_data(null, "[path: " + Std.string(merged_env["PATH"]) + "]\n");
            }
            else 
            {
                this.append_data(null, "[path: " + Std.string(os.environ["PATH"]) + "]\n");
            }
            if (!this.quiet) 
            {
                this.append_data(null, "[Finished]");
            }
        }
    }

    public function is_enabled(kill = false)
    {
        if (kill) 
        {
            return this.proc != null && this.proc.poll();
        }
        else
        {
            return true;
        }
    }

    public function append_data(proc, data:String)
    {
        if (proc != this.proc) 
        {
            // a second call to exec has been made before the first one
            // finished, ignore it instead of intermingling the output.
            if (proc) 
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
            st = Helper.encode_utf8(data);
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
        var selection_was_at_end = (sel.length == 1 && sel[0] == sublime.Region(this.output_view.size()));
        
        public function do_edit(v:View, edit:Edit)
        {

            v.set_read_only(false);
            
            v.insert(edit, this.output_view.size(), st);
            if (selection_was_at_end) 
            {
                v.show(this.output_view.size());
            }
            v.end_edit(edit);

            v.set_read_only(true);
            
        viewtools.async_edit(this.output_view, do_edit);
    }

    public function finish(proc)
    {
        
        var v = this.output_view;
        
        if (!this.quiet) 
        {
            var elapsed = Time.time() - proc.start_time;
            var exit_code = proc.exit_code();
            
            
            if (exit_code == 0 || exit_code == null) 
            {
                this.append_data(proc, '[Finished in ${elapsed}]');
            }
            else
            {
                this.append_data(proc, '[Finished in ${elapsed} with exit code ${exit_code}]')
            }
        }
        if (proc != this.proc) 
        {
            return
        }

        // Set the selection to the start, so that next_result will work as expected
        
        v.sel().clear();
        v.sel().add(sublime.Region(0));
    }
        

    public function on_data(proc, data:String):Void
    {
        sublime.set_timeout(function () trace(data), 0);
        sublime.set_timeout(this.append_data.bind(proc, data), 0);
    }

    public function on_finished(proc):Void
    {
        sublime.set_timeout(this.finish.bind(proc), 0);
    }


}

/*
import sublime, sublime_plugin
import os,sys

import functools
import time

from haxe.plugin import is_st3
from haxe.tools import viewtools
from haxe.trace import trace

from haxe.tools.stringtools import encode_utf8, to_unicode

if is_st3:
    import _thread as thread
else:
    import thread

try :
    stexec = __import__("exec")
    ExecCommand = stexec.ExecCommand
    AsyncProcess = stexec.AsyncProcess 
except ImportError as e :
    import Default
    stexec = getattr( Default , "exec" )
    ExecCommand = stexec.ExecCommand
    AsyncProcess = stexec.AsyncProcess



*/