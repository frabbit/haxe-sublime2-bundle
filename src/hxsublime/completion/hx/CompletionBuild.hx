package hxsublime.completion.hx;

import hxsublime.build.Build;
import hxsublime.macros.LazyFunctionSupport;
import hxsublime.project.CompletionState.CompletionCache;
import hxsublime.project.Project;
import hxsublime.Settings;
import hxsublime.tools.StringTools;
import hxsublime.tools.ViewTools;
import python.lib.Builtins;
import python.lib.Re;
import python.lib.Time;
import python.Tuple;
import sublime.Region;
import sublime.View;

using hxsublime.support.StringTools;


using hxsublime.support.ArrayTools;


class CompletionBuild implements LazyFunctionSupport {

    public var build(default, null):Build;
    public var ctx(default, null):CompletionContext;
    public var tempPath(default, null):String;
    public var tempFile(default, null):String;
    public var cache(default, null):CompletionCache;

    public function new (ctx:CompletionContext, temp_path:String, temp_file:String)
    {
        this.build = ctx.build().copy();
        // add the temp_path to the classpath of the build
        this.build.addClasspath(temp_path);
        // the completion context
        this.ctx = ctx;
        // stores the temporary classpath which contains the temp_file
        this.tempPath = temp_path;
        // stores the temporary file path which is used for completion
        this.tempFile = temp_file;

        this.cache = ctx.project.completionContext.current;
    }

    @lazyFunction
    public function display()
    {
        var pos = if (!Settings.useOffsetCompletion()) "0" else Std.string(ctx.complete_offset_in_bytes);
        return tempFile + "@" + pos;
    }
}

