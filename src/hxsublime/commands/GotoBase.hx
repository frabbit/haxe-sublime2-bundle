package hxsublime.commands;

import haxe.ds.StringMap;
import hxsublime.project.Projects;
import hxsublime.tools.HxSrcTools.HaxeType;
import hxsublime.tools.ViewTools;
import python.Tuple;
import python.KwArgs;
import sublime.Edit;
import sublime.EventListener;
import sublime.Region;
import sublime.Sublime;
import sublime.TextCommand;
import sublime.View;

private class State
{
    public static var _find_decl_file = null;
    public static var _find_decl_pos = null;
    public static var _init_text = "";
    public static var _is_open = false;
}

@:keep class HaxeGotoBaseCommand<T> extends TextCommand
{
    var selecting_build:Bool = false;

    function getEntries (types:StringMap<HaxeType>):Array<Array<String>>
    {
        return throw "abstract method";
    }
    function getData (types:StringMap<HaxeType>):Array<Tuple2<String, T>>
    {
        return throw "abstract method";
    }

    function getFile(data_entry:T):String
    {
        return throw "abstract method";
    }

    function getSrcPos(data_entry:T):Int
    {
        return throw "abstract method";
    }

    override public function run( edit:Edit, ?kwArgs:KwArgs<Dynamic> )
    {


        trace("run HaxeListBuildFieldsCommand");

        var view = this.view;

        var project = Projects.currentProject(view);


        if (!project.hasBuild())
        {
            project.extractBuildArgs(view, false);
        }

        if (!project.hasBuild())
        {
            project.extractBuildArgs(view, true);
            return;
        }

        var build = project.getBuild(view);

        var bundle = build.getTypes().merge(build.stdBundle());



        var bundle_types = bundle.allTypesAndEnumConstructorsWithInfo();

        var filtered_types = new StringMap();

        for (k in bundle_types.keys())
        {
            var t = bundle_types.get(k);
            if (build.isTypeAvailable(t))
            {
                filtered_types.set(k, t);
            }
        }


        var function_list = this.getEntries(filtered_types);
        var function_list_data = this.getData(filtered_types);

        
        trace(Std.string(function_list));

        trace(Std.string(function_list.length));


        this.selecting_build = true;
        Sublime.status_message("Please select a type");

        var win = view.window();

        var sel = view.sel();


        if (sel.length == 1 && sel[0].begin() != sel[0].end())
        {
            var init = ViewTools.getContent(view).substring(sel[0].begin(), sel[0].end());
            var init = ~/^[A-Za-z_0-9]*$/.match(init) ? init : "";
            State._init_text = init;
        }
        else if (sel.length == 1)
        {
            var reg = view.word(sel[0].begin());
            var init = ViewTools.getContent(view).substring(reg.begin(), reg.end());
            var init = ~/^[A-Za-z_0-9]*$/.match(init) ? init : "";
            State._init_text = init;
        }
        else
        {
            State._init_text = "";
        }
        function onSelected (i:Int)
        {

            State._is_open = false;
            State._init_text = "";
            if (i >= 0)
            {
                var selected_type = function_list_data[i];
                trace("selected field: " + Std.string(selected_type._1));

                var src_pos = this.getSrcPos(selected_type._2);

                var goto_file = this.getFile(selected_type._2);

                State._find_decl_file = goto_file;

                trace("find_decl_file: " + Std.string(State._find_decl_file));
                if (src_pos != null)
                {
                    State._find_decl_pos = src_pos;
                    trace("src_pos" + Std.string(src_pos) );
                }
                else
                {
                    State._find_decl_pos = 0;
                }


                function show()
                {
                    win.open_file(goto_file);
                }

                Sublime.set_timeout(show, 130);
            }
        }
        State._is_open = true;
        win.show_quick_panel( function_list , onSelected  , Sublime.MONOSPACE_FONT );
    }


}


@:keep class HaxeGotoBaseListener extends EventListener
{

    override public function on_activated(view:View)
    {


        // global _find_decl_pos, _find_decl_file, _is_open, _init_text
        var find_pos = State._find_decl_pos;
        var find_file = State._find_decl_file;
        trace("HaxeGotoBaseListener::on_activated");


        trace(Std.string(view));


        if (view != null && State._is_open)
        {
            State._is_open = false;

            ViewTools.insertAtCursor(view, State._init_text);
            State._init_text = "";
        }


        if (view != null && view.file_name() != null)
        {

            if (view.file_name() == find_file)
            {

                view.sel().clear();

                var min = find_pos;

                view.sel().add(new Region(min));

                trace("show at:" + Std.string(min));
                // move to line is delayed, seems to work better
                // without delay the animation to the region does not work properly sometimes
                function show ()
                {
                    trace("show at:" + Std.string(min));
                    view.show_at_center(new Region(min));
                }
                Sublime.set_timeout(show, 100);
                State._find_decl_file = null;
                State._find_decl_pos = null;
            }
        }
    }
}
