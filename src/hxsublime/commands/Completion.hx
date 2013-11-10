package hxsublime.commands;

import sublime.Edit;
import sublime.TextCommand;
import sublime.View;
import python.lib.Types;

class HaxeAsyncTriggeredCompletionCommand extends TextCommand
{
    override public function run( kwArgs:KwArgs) 
    {
        var edit:Edit = kwArgs.get("edit");
        var options = new CompletionOptions(
            hxcc.COMPLETION_TRIGGER_ASYNC, 
            hxcc.COMPILER_CONTEXT_REGULAR, 
            hxcc.COMPLETION_TYPE_REGULAR);
        trigger_completion(self.view, options);
    }


}
class HaxeDisplayCompletionCommand extends TextCommand
{
    override public function run( kwArgs:KwArgs) 
    {
        var edit:Edit = kwArgs.get("edit");
        var input_char:String = kwArgs.get("input_char");
        
        
        if (input_char != null) 
        {
            self.view.run_command("insert" , {
                "characters" : input_char
            });
        }
        trace("RUN - HaxeDisplayCompletionCommand");
        if (is_valid_completion(self.view, edit, input_char)) 
        {
            var options = new CompletionOptions(
                hxcc.COMPLETION_TRIGGER_MANUAL, 
                hxcc.COMPILER_CONTEXT_REGULAR, 
                hxcc.COMPLETION_TYPE_REGULAR);
            trigger_completion(self.view, options);
        }
    }
}

class HaxeDisplayMacroCompletionCommand extends TextCommand
{
    override public function run( kwArgs:KwArgs) 
    {
        var edit:Edit = kwArgs.get("edit");
        trace("RUN - HaxeDisplayMacroCompletionCommand");
        
        var options = new CompletionOptions(
            hxcc.COMPLETION_TRIGGER_MANUAL, 
            hxcc.COMPILER_CONTEXT_REGULAR, 
            hxcc.COMPLETION_TYPE_REGULAR);
        trigger_completion(self.view, options);
    }
}

class HaxeHintDisplayCompletionCommand extends TextCommand
{
    override public function run( kwArgs:KwArgs) 
    {
        var edit:Edit = kwArgs.get("edit");
        trace("RUN - HaxeHintDisplayCompletionCommand");
        
        var options = new CompletionOptions(
            hxcc.COMPLETION_TRIGGER_MANUAL, 
            hxcc.COMPILER_CONTEXT_REGULAR, 
            hxcc.COMPLETION_TYPE_HINT);
        trigger_completion(self.view, options);
    }

}
class HaxeMacroHintDisplayCompletionCommand extends TextCommand
{
    override public function run( kwArgs:KwArgs) 
    {
        var edit:Edit = kwArgs.get("edit");
        trace("RUN - HaxeMacroHintDisplayCompletionCommand");
        
        var options = new CompletionOptions(
            hxcc.COMPLETION_TRIGGER_MANUAL, 
            hxcc.COMPILER_CONTEXT_MACRO, 
            hxcc.COMPLETION_TYPE_HINT);

        trigger_completion(self.view, options);
    }
}

class Helper {

    
    public static function is_valid_completion (view:View, edit:Edit, input_char:String) 
    {
        var valid = true;
        if (input_char == "(") 
        {
            var src = viewtools.get_content_until_first_cursor(view);
            
            if (is_open_parenthesis_after_function_definition(src))
            {
                trace("Invalid Completion is open par after function");
                valid = false;
            }
        }
        
        if (input_char == ",") 
        {
            var src = viewtools.get_content_until_first_cursor(view);
            if (is_comma_after_open_parenthesis_of_function_definition(src)) 
            {
                trace("Invalid Completion is open par after function");
                valid = false;
            }
        }

        return valid;
    }

    public static var anon_func = re.compile("^function(\\s+[a-zA-Z0-9$_]*\\s+)?\\s*\\($");

    
    public static function is_open_parenthesis_after_function_definition (src:String) 
    {
        var last_function = src.rfind("function");
        var src_part = src.substr(last_function);
        var match = re.match(anon_func, src_part);
        trace(Std.string(match));
        trace(src_part);
        return match != null;

    }

    public static function is_comma_after_open_parenthesis_of_function_definition (src:String) 
    {
        trace("src_full:" + src);

        var found = hxsrctools.reverse_search_next_char_on_same_nesting_level(src, "(", src.length-1);

        trace("match:" + Std.string(found));

        var res = false;
        if (found != null) 
        {
            var src_until_comma = src.substring(0,found[0]+1);
            trace("src_until_comma: " + src_until_comma);
            res = is_open_parenthesis_after_function_definition(src_until_comma);
        }

        return res;
    }
}
/*

import haxe.completion.hx.constants as hxcc

import sublime_plugin
import re 
from haxe.trace import trace

from haxe.tools import viewtools
from haxe.tools import stringtools
from haxe.tools import hxsrctools

from haxe.completion.hx.types import CompletionOptions
from haxe.completion.hx.base import trigger_completion



*/