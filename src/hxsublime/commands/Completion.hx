package hxsublime.commands;

import hxsublime.completion.hx.Base;
import hxsublime.completion.hx.Constants;
import hxsublime.completion.hx.Types.CompletionOptions;
import hxsublime.tools.HxSrcTools;
import hxsublime.tools.ViewTools;
import python.lib.Re;
import sublime.Edit;
import sublime.TextCommand;
import sublime.View;
import python.lib.Types;

@:keep class HaxeAsyncTriggeredCompletionCommand extends TextCommand
{
    override public function run( edit:Edit, ?kwArgs:KwArgs) 
    {
        var options = new CompletionOptions(
            Constants.COMPLETION_TRIGGER_ASYNC, 
            Constants.COMPILER_CONTEXT_REGULAR, 
            Constants.COMPLETION_TYPE_REGULAR);
        Base.trigger_completion(this.view, options);
    }


}
@:keep class HaxeDisplayCompletionCommand extends TextCommand
{
    override public function run( edit:Edit, ?kwArgs:KwArgs) 
    {

        var input_char:String = kwArgs == null ? null : kwArgs.get("input_char", null);
        
        
        if (input_char != null) 
        {
            this.view.run_command("insert" , Dict.fromObject({
                "characters" : input_char
            }));
        }
        trace("RUN - HaxeDisplayCompletionCommand");
        if (Helper.is_valid_completion(this.view, edit, input_char)) 
        {
            var options = new CompletionOptions(
                Constants.COMPLETION_TRIGGER_MANUAL, 
                Constants.COMPILER_CONTEXT_REGULAR, 
                Constants.COMPLETION_TYPE_REGULAR);
            Base.trigger_completion(this.view, options);
        }
    }
}

@:keep class HaxeDisplayMacroCompletionCommand extends TextCommand
{
    override public function run( edit:Edit, ?kwArgs:KwArgs) 
    {
        trace("RUN - HaxeDisplayMacroCompletionCommand");
        
        var options = new CompletionOptions(
            Constants.COMPLETION_TRIGGER_MANUAL, 
            Constants.COMPILER_CONTEXT_REGULAR, 
            Constants.COMPLETION_TYPE_REGULAR);
        Base.trigger_completion(this.view, options);
    }
}

@:keep class HaxeHintDisplayCompletionCommand extends TextCommand
{
    override public function run( edit:Edit, ?kwArgs:KwArgs) 
    {

        trace("RUN - HaxeHintDisplayCompletionCommand");
        
        var options = new CompletionOptions(
            Constants.COMPLETION_TRIGGER_MANUAL, 
            Constants.COMPILER_CONTEXT_REGULAR, 
            Constants.COMPLETION_TYPE_HINT);
        Base.trigger_completion(this.view, options);
    }

}
@:keep class HaxeMacroHintDisplayCompletionCommand extends TextCommand
{
    override public function run( edit:Edit, ?kwArgs:KwArgs) 
    {
        
        trace("RUN - HaxeMacroHintDisplayCompletionCommand");
        
        var options = new CompletionOptions(
            Constants.COMPLETION_TRIGGER_MANUAL, 
            Constants.COMPILER_CONTEXT_MACRO, 
            Constants.COMPLETION_TYPE_HINT);

        Base.trigger_completion(this.view, options);
    }
}

class Helper {

    
    public static function is_valid_completion (view:View, edit:Edit, input_char:String) 
    {
        var valid = true;
        if (input_char == "(") 
        {
            var src = ViewTools.getContentUntilFirstCursor(view);
            
            if (is_open_parenthesis_after_function_definition(src))
            {
                trace("Invalid Completion is open par after function");
                valid = false;
            }
        }
        
        if (input_char == ",") 
        {
            var src = ViewTools.getContentUntilFirstCursor(view);
            if (is_comma_after_open_parenthesis_of_function_definition(src)) 
            {
                trace("Invalid Completion is open par after function");
                valid = false;
            }
        }

        return valid;
    }

    public static var anon_func = Re.compile("^function(\\s+[a-zA-Z0-9$_]*\\s+)?\\s*\\($");

    
    public static function is_open_parenthesis_after_function_definition (src:String) 
    {
        var last_function = src.lastIndexOf("function");
        var src_part = src.substr(last_function);
        var match = Re.match(anon_func, src_part);
        trace(Std.string(match));
        trace(src_part);
        return match != null;

    }

    public static function is_comma_after_open_parenthesis_of_function_definition (src:String) 
    {
        trace("src_full:" + src);

        var found = HxSrcTools.reverse_search_next_char_on_same_nesting_level(src, ["("], src.length-1);

        trace("match:" + Std.string(found));

        var res = false;
        if (found != null) 
        {
            var src_until_comma = src.substring(0,found._1+1);
            trace("src_until_comma: " + src_until_comma);
            res = is_open_parenthesis_after_function_definition(src_until_comma);
        }

        return res;
    }
}
/*

import haxe.completion.hx.constants as Constants

import sublime_plugin
import re 
from haxe.trace import trace

from haxe.tools import viewtools
from haxe.tools import stringtools
from haxe.tools import hxsrctools

from haxe.completion.hx.types import CompletionOptions
from haxe.completion.hx.base import trigger_completion



*/