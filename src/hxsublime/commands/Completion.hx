package hxsublime.commands;

import hxsublime.completion.hx.HxCompletion;
import hxsublime.completion.hx.Constants;
import hxsublime.completion.hx.CompletionOptions;
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
        HxCompletion.triggerCompletion(this.view, options);
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
        if (input_char == ":") 
        {
            return;
        }
        if (Helper.isValidCompletion(this.view, edit, input_char)) 
        {
            var options = new CompletionOptions(
                Constants.COMPLETION_TRIGGER_MANUAL, 
                Constants.COMPILER_CONTEXT_REGULAR, 
                Constants.COMPLETION_TYPE_REGULAR);
            HxCompletion.triggerCompletion(this.view, options);
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
        HxCompletion.triggerCompletion(this.view, options);
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
        HxCompletion.triggerCompletion(this.view, options);
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

        HxCompletion.triggerCompletion(this.view, options);
    }
}

class Helper {

    
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

        var res = false;
        if (found != null) 
        {
            var srcUntilComma = src.substring(0,found._1+1);
            res = isOpenParensAfterFunctionDefinition(srcUntilComma);
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