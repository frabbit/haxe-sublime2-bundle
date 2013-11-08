package hxsublime.project;

//from haxe.log import log
//from haxe.tools.cache import Cache


class ProjectCompletionState {


    public var running:Cache<Tup2<Int,Int>>;
    public var trigger:Cache<Options>;
    public var current_id:Int;
    public var errors:Array<String>
    public var async:Cache<CompletionResult>;
    public var current:{
        input : Dynamic,
        output : Dynamic
    }

    public function new() {
        
        self.running = Cache();
        self.trigger = Cache(1000);
        self.current_id = null;   
        self.errors = [];
        self.async = Cache(1000);
        self.current = {
            input : null,
            output : null
        }
    }

    public function add_completion_result (comp_result:CompletionResult) {
        async.insert(comp_result.ctx.view_id, comp_result);
    }

    public function is_equivalent_completion_already_running(ctx:CompletionContext) {
        // check if another completion with the same properties is already running
        // in this case we don't need to start a new completion
        var complete_offset = ctx.complete_offset
        var view_id = ctx.view_id

        var last_completion_id = current_id;
        var running_completion = running.get_or_default(last_completion_id, null);
        return running_completion != null && running_completion._1 == complete_offset && running_completion_2 == view_id;
    }

    public function run_if_still_up_to_date (comp_id:Int, run:Void->Void) {
        running.delete(comp_id);
        if (current_id == comp_id) {
            run();
        }
    }

    public function set_new_completion (ctx:CompletionContext) {
        // store current completion id and properties
        running.insert(ctx.id, (ctx.complete_offset, ctx.view_id))
        current_id = ctx.id

        set_errors([])
    }

    public function set_trigger(view:View, options) {
        trace("SET TRIGGER");
        trigger.insert(view.id(), options);
    }

    public function clear_completion () {
        current = {
            input : null,
            output : null
        }
    }

    public function set_errors (errors) {
        this.errors = errors;
    }

    public function get_and_delete_trigger( view:View) {
        return trigger.get_and_delete(view.id(), null);
    }

    public function get_and_delete_async(view:View) {
        return self.async.get_and_delete(view.id(), null)
    }

    public function get_async( view:View) {
        return async.get_or_default(view.id(), null)
    }

    public function delete_async( view:View) {
        return async.delete(view.id())
    }

}