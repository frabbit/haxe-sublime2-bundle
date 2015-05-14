package hxsublime.tools;
import python.lib.os.Path;
import StringTools in ST;
import sublime.Region;
import sublime.Sublime;

import hxsublime.Config;

import sublime.TextCommand;

import python.lib.Os;

import python.KwArgs;

import sublime.View;
import sublime.Edit;

import python.Dict;

class AsyncEdit
{
	public static var dict : Dict<Int, View->Edit->Void> = new Dict();
	public static var id:Int = 0;

	public static function asyncEdit(view:View, doEdit:View->Edit->Void)
	{
	    function start()
	    {
	        var id = AsyncEdit.id;
	        if (AsyncEdit.id > 1000000)
	        	AsyncEdit.id = 0
	        else
	        	AsyncEdit.id += 1;

	        AsyncEdit.dict.set(id, doEdit);
	        view.run_command(HaxeTextEditCommand.COMMAND_ID, python.Lib.anonToDict({ "id" : id }));
	    }

	    Sublime.set_timeout(start, 10);
	}

	public static function run (view:View, edit:Edit, d:Dict<String, Dynamic>)
	{
        var id:Int = d.get("id", null);

        if (AsyncEdit.dict.hasKey(id))
        {
        	var fun = AsyncEdit.dict.get(id, null);
            AsyncEdit.dict.remove(id);
            fun(view, edit);
        }
    }
}

@:keep class HaxeTextEditCommand extends TextCommand
{
	public static var COMMAND_ID = "hxsublime_tools__haxe_text_edit";

	override public function run (edit:Edit, ?args:KwArgs<Dynamic>)
	{
		AsyncEdit.run(view, edit, args.toDict());
    }
}

class ViewTools {


	public static function insertSnippet (view:View, snippet:String)
	{
		view.run_command("insert_snippet", python.Lib.anonToDict({ 'contents' : snippet }) );
	}

	public static function insertAtCursor(view:View, txt:String)
	{
		function doEdit(v:View, e:Edit)
		{
			v.insert(e, getFirstCursorPos(v), txt);
		}
		asyncEdit(view, doEdit);
	}


	public static function getFirstCursorPos (view:View)
	{
		return view.sel()[0].begin();
	}


	public static function asyncEdit(view:View, doEdit:View->Edit->Void)
	{
	    AsyncEdit.asyncEdit(view, doEdit);
	}


	public static function findViewByName (name:String):Null<View>
	{
		var windows = Sublime.windows();
		for (w in windows)
		{
			var views = w.views();

			for (v in views)
			{
				if (v.name() == name) return v;
			}
		}
		return null;
	}


	public static function createMissingFolders(view:View)
	{
		var fn = view.file_name();
		var path = Path.dirname( fn );
		if (!Path.isdir( path )) {
			Os.makedirs( path );
		}
	}


	public static function getContentUntilFirstCursor (view:View)
	{
		var end = getFirstCursorPos(view);
		return getContentUntil(view, end);
	}

	public static function getContentUntil (view:View, endPos:Int)
	{
		return view.substr(new Region(0, endPos));
	}

	public static function getContent (view:View)
	{
		return view.substr(new Region(0, view.size()));
	}

	public static function isHxsl (view:View)
	{
		return ST.endsWith(view.file_name(), Config.HXSL_SUFFIX);
	}

	public static function isSupported (view:View)
	{
		return view.score_selector(0,Config.SOURCE_HAXE+','+Config.SOURCE_HXML+','+Config.SOURCE_ERAZOR+','+Config.SOURCE_NMML) > 0;
	}

	public static function isUnsupported (view:View)
	{
		return !isSupported(view);
	}

	public static function getScopesAt (view:View, pos:Int)
	{
		return view.scope_name(pos).split(" ");
	}


	public static function isHaxe(view:View)
	{
		return view.score_selector(0,Config.SOURCE_HAXE) > 0;
	}
	public static function isHxml(view:View)
	{
		return view.score_selector(0,Config.SOURCE_HXML) > 0;
	}

	public static function isErazor(view:View)
	{
		return view.score_selector(0,Config.SOURCE_ERAZOR) > 0;
	}

	public static function isNmml(view:View)
	{
		return view.score_selector(0,Config.SOURCE_NMML) > 0;
	}


	public static function replaceContent (view:View, newContent:String)
	{
		function doEdit(view:View, edit:Edit)
		{
			view.replace(edit, new Region(0, view.size()), newContent);
			//view.end_edit(edit);
		}

		view.set_read_only(false);
		asyncEdit(view, doEdit);
	}

	public static function inHaxeCode (view:View, caret:Int)
	{
		return view.score_selector(caret,"source.haxe") > 0 && view.score_selector(caret,"string") == 0 && view.score_selector(caret,"comment") == 0;
	}

	public static function inHaxeString (view:View, caret:Int)
	{
		return view.score_selector(caret,"source.haxe") > 0 && view.score_selector(caret,"string") > 0;
	}

	public static function inHaxeComments (view:View, caret:Int)
	{
		return view.score_selector(caret,"source.haxe") > 0 && view.score_selector(caret,"comment") > 0;
	}

}
