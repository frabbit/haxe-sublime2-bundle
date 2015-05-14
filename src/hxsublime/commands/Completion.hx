package hxsublime.commands;

import haxe.Unserializer;
import hxsublime.completion.Completion.CompletionInput;
import hxsublime.completion.Completion.CompletionListener;
import hxsublime.completion.hx.HxCompletion;
import hxsublime.completion.hx.CompletionOptions;
import hxsublime.Settings;
import hxsublime.tools.HxSrcTools;
import hxsublime.tools.ViewTools;
import python.lib.Re;
import sublime.Edit;
import sublime.TextCommand;
import sublime.View;

import python.KwArgs;


@:keep class HaxeDisplayCompletionCommand extends TextCommand
{
    override public function run( edit:Edit, ?kwArgs:KwArgs<Dynamic>)
    {
        var input_char:String = kwArgs == null ? null : kwArgs.get("input_char", null);

        if (input_char != null)
        {
            this.view.run_command("insert" , python.Lib.anonToDict({
                "characters" : input_char
            }));
        }

        if (input_char != ":" && Helper.isValidCompletion(this.view, edit, input_char))
        {
            var userActivated = input_char == null;
            var options = new CompletionOptions(userActivated);

            if (input_char == null || input_char == "." || !Settings.topLevelCompletionsOnDemand()) 
            {
                trace("RUN - HaxeDisplayCompletionCommand");
                trace("options.userActivated:" + options.userActivated);

                function f (ctx:CompletionInput) {
                	return HxCompletion.commandTriggeredAutoComplete(ctx.project, ctx.view, ctx.offset, options, ctx.prefix);
                }

                CompletionListener.trigger(view, false, f);
            }
        }
    }
}

private class Helper 
{
    public static function isValidCompletion (view:View, edit:Edit, inputChar:String)
    {
        var valid = true;
        if (inputChar == "(")
        {
            var src = ViewTools.getContentUntilFirstCursor(view);

            if (isOpenParensAfterFunctionDefinition(src))
            {
                trace("Invalid Completion is open par after function");
                valid = false;
            }
        }

        if (inputChar == ",")
        {
            var src = ViewTools.getContentUntilFirstCursor(view);
            if (isCommaAfterOpenParensInFunctionDefinition(src))
            {
                trace("Invalid Completion is open par after function");
                valid = false;
            }
        }
        return valid;
    }

    static var anonFunc = Re.compile("^function(\\s+[a-zA-Z0-9$_]*\\s+)?\\s*\\($");

    static function isOpenParensAfterFunctionDefinition (src:String)
    {
        var lastFunction = src.lastIndexOf("function");
        var srcPart = src.substr(lastFunction);
        var match = Re.match(anonFunc, srcPart);
        return match != null;
    }

    static function isCommaAfterOpenParensInFunctionDefinition (src:String)
    {
        var found = HxSrcTools.reverse_search_next_char_on_same_nesting_level(src, ["("], src.length-1);

        return 
            if (found != null)
            {
                var srcUntilComma = src.substring(0,found._1+1);
                isOpenParensAfterFunctionDefinition(srcUntilComma);
            } 
            else false;
    }
}
