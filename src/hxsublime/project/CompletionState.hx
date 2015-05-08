package hxsublime.project;

import haxe.ds.IntMap;
import hxsublime.compiler.Output.CompilerError;
import hxsublime.completion.hx.CompletionContext;
import hxsublime.completion.hx.CompletionOptions;
import hxsublime.completion.hx.CompletionResult;
import hxsublime.tools.Cache;
import python.Tuple;
import sublime.View;

//from haxe.log import log
//from haxe.tools.cache import Cache

typedef CompletionCache = {
    input : CompletionContext,
    output : CompletionResult,
}


class ProjectCompletionState
{
    public var running:Cache<Int, Tuple2<Int,Int>>;
    public var trigger:Cache<Int, CompletionOptions>;
    public var currentId:Int;
    public var errors:Array<CompilerError>;
    public var async:Cache<Int, CompletionResult>;
    public var current:CompletionCache;

    public function new()
    {
        this.running = new Cache(new IntMap());
        this.trigger = new Cache(new IntMap(), 1000);
        this.currentId = null;
        this.errors = [];
        this.async = new Cache(new IntMap(), 1000);
        this.current = {
            input : null,
            output : null
        }
    }

    public function addCompletionResult (compResult:CompletionResult)
    {
        async.insert(compResult.ctx.view_id, compResult);
    }

    public function isEquivalentCompletionAlreadyRunning(ctx:CompletionContext)
    {
        // check if another completion with the same properties is already running
        // in this case we don't need to start a new completion
        var complete_offset = ctx.complete_offset;
        var view_id = ctx.view_id;

        var last_completion_id = currentId;
        var running_completion = running.getOrDefault(last_completion_id, null);
        return running_completion != null && running_completion._1 == complete_offset() && running_completion._2 == view_id;
    }

    public function runIfStillUpToDate (comp_id:Int, run:Void->Void)
    {
        running.delete(comp_id);
        if (currentId == comp_id) {
            run();
        }
    }

    public function setNewCompletion (ctx:CompletionContext)
    {
        // store current completion id and properties
        running.insert(ctx.id, Tuple2.make(ctx.complete_offset(), ctx.view_id));
        currentId = ctx.id;

        setErrors([]);
    }

    public function setTrigger(view:View, options)
    {
        trace("SET TRIGGER");
        trigger.insert(view.id(), options);
    }

    public function clearCompletion ()
    {
        current = {
            input : null,
            output : null
        }
    }

    public function setErrors (errors)
    {
        this.errors = errors;
    }

    public function getAndDeleteTrigger( view:View)
    {
        return trigger.getAndDelete(view.id(), null);
    }

    public function getAndDeleteAsync(view:View)
    {
        return this.async.getAndDelete(view.id(), null);
    }

    public function getAsync( view:View)
    {
        return async.getOrDefault(view.id(), null);
    }

    public function deleteAsync( view:View)
    {
        return async.delete(view.id());
    }
}