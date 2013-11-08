package hxsublime.completion.hx;

import hxsublime.tools.StringTools;




class CompletionResult {
    
    public static function empty_result (ctx, retrieve_toplevel_comps = null):
        return new CompletionResult("", [], "", [], ctx, retrieve_toplevel_comps)


    public var ret:String;
    public var comps:Array<String>;
    public var status:String;
    public var hints:Array<String>;
    public var ctx:CompletionContext;

    public var retrieve_toplevel_comps:Void->Array<String>;



    public function new (ret:String, comps:Array<String>, status:String, hints:Array<String>, ctx:CompletionContext, retrieve_toplevel_comps:Void->Array<String>) 
    {
        this.ret = ret
        this.comps = comps
        this.status = status
        this.hints = hints
        this.ctx = ctx
        if (retrieve_toplevel_comps == null) {
            retrieve_toplevel_comps = function () return [];
        }

        this.retrieve_toplevel_comps = retrieve_toplevel_comps
    }

        

    @lazyprop
    public function _toplevel_comps():Array<String> {
        return retrieve_toplevel_comps();
    }


    public function has_hints () {
        return hints.length > 0;
    }

    public function has_compiler_results () {
        return comps.length > 0;
    }

    public function has_results () {
        return comps.length > 0 || hints.length > 0 || (requires_toplevel_comps() && self._toplevel_comps.length > 0);
    }

    public function show_top_level_snippets () {
        return requires_toplevel_comps() && !ctx.is_new;
    }

    

    public function requires_toplevel_comps() 
    {
        prefix_is_whitespace = StringTools.is_whitespace_or_empty(ctx.prefix);
        trace("prefix_is_whitespace:" + Std.string(prefix_is_whitespace));
        trace("has_hints:" + Std.string(self.has_hints()));
        trace("has_hint:" + Std.string(self.ctx.options.types.has_hint()));
        trace("has_compiler_results:" + Std.string(self.has_compiler_results()));
        return !((prefix_is_whitespace && has_hints() && ctx.options.types.has_hint()) || has_compiler_results());
    }

    public function all_comps () {
        var res = [];
        if (requires_toplevel_comps()) {
            trace("yes required toplevel comps");
            res = res.concat(_toplevel_comps);
        }
        res = res.concat(comps);
        res.sort();
        return res;
    }

}


typedef TODO = #if debug #error "type is not yet defined" #else Dynamic #end

class CompletionBuild {

    public var build:Build;
    public var ctx:CompletionContext;
    public var temp_path:String;
    public var temp_file:String
    public var cache:TODO

    public function new (ctx:CompletionContext, temp_path:String, temp_file:String)
    {
        this.build = ctx.build.copy();
        // add the temp_path to the classpath of the build
        this.build.add_classpath(temp_path);
        // the completion context
        this.ctx = ctx;
        // stores the temporary classpath which contains the temp_file
        this.temp_path = temp_path;
        // stores the temporary file path which is used for completion
        this.temp_file = temp_file;

        this.cache = ctx.project.completion_context.current;
    }

    @lazyprop
    public function display() 
    {
        var pos = if (!Settings.use_offset_completion()) "0" else Std.string(ctx.complete_offset_in_bytes);
        return temp_file + "@" + pos;
    }
}


class CompletionOptions {
    public function new(trigger, context = hcc.COMPILER_CONTEXT_REGULAR, types = hcc.COMPLETION_TYPE_REGULAR, toplevel = hcc.COMPLETION_TYPE_TOPLEVEL):
        this._types = new CompletionTypes(types);
        this._toplevel = TopLevelOptions(toplevel);
        this._context = context;
        this._trigger = trigger;

    public function copy_as_manual() 
    {
        return CompletionOptions(hcc.COMPLETION_TRIGGER_MANUAL, this._context, this.types.val, this._toplevel.val);
    }

    public function copy_as_async() 
    {
        return CompletionOptions(hcc.COMPLETION_TRIGGER_ASYNC, this._context, this.types.val, this._toplevel.val);
    }

    @property
    public function types() 
    {
        return this._types;
    }


    @lazyprop
    public function async_trigger() 
    {
        return this._trigger == hcc.COMPLETION_TRIGGER_ASYNC;
    }

    @lazyprop
    public function manual_completion() 
    {
        return this._trigger == hcc.COMPLETION_TRIGGER_MANUAL;
    }

    @lazyprop
    public function macro_completion() 
    {
        return this._context == hcc.COMPILER_CONTEXT_MACRO;
    }

    @lazyprop
    public function regular_completion() 
    {
        return this._context == hcc.COMPILER_CONTEXT_REGULAR;
    }

    public function eq (other:CompletionOptions) 
    {
        return this._trigger == other._trigger and this._types.eq(other._types) and this._toplevel.eq(other._toplevel) and this._context == other._context;
    }
}


class CompletionTypes {


    var _opt:Int;

    public function new( val = Constants.COMPLETION_TYPE_REGULAR) {
        _opt = val;
    }

    public function val () {
        return _opt;
    }

    public function add (val:Int) 
    {
        _opt |= val;
    }

    public function add_hint () 
    {
        _opt = _opt | Constants.COMPLETION_TYPE_HINT;
    }

    public function has_regular () {
        return (_opt & Constants.COMPLETION_TYPE_REGULAR) > 0;
    }

    public function has_hint () {
        return (_opt & Constants.COMPLETION_TYPE_HINT) > 0;
    }
    
    public function has_toplevel () {
        return (_opt & Constants.COMPLETION_TYPE_TOPLEVEL) > 0;
    }

    public function has_toplevel_forced () {
        return (_opt & Constants.COMPLETION_TYPE_TOPLEVEL_FORCED) > 0;
    }

    public function eq (other:CompletionTypes) {
        return _opt == other._opt;
    }

}

class TopLevelOptions {

    var _opt:Int;

    public function new(val = 0) {
        this._opt = val;
    }

    
    public function val () {
        return this._opt;
    }

    public function set (val) {
        this._opt |= val;
    }

    public function has_types () {
        return (this._opt & Constants.TOPLEVEL_OPTION_TYPES) > 0;
    }

    public function has_locals () {
        return (this._opt & Constants.TOPLEVEL_OPTION_LOCALS) > 0;
    }
    
    public function has_keywords () {
        return (this._opt & Constants.TOPLEVEL_OPTION_KEYWORDS) > 0;
    }

    public function eq (other:TopLevelOptions) {
        return this._opt == other._opt;
    }
}


class CompletionSettings {
    public function new(settings):
        this.settings = settings

    @lazyprop
    public function smarts_hints_only_next() {
        return settings.smarts_hints_only_next();
    }

    @lazyprop
    public function no_fuzzy_completion() {
        return settings.no_fuzzy_completion();
    }

    @lazyprop
    public function top_level_completions_only_on_demand() {
        return settings.top_level_completions_on_demand();
    }

    @lazyprop
    public function is_async_completion() {
        return settings.is_async_completion();
    }

    @lazyprop
    public function show_only_async_completions() {
        return settings.show_only_async_completions();
    }

    @lazyprop
    public function get_completion_delays() {
        return settings.get_completion_delays();
    }

    public function show_completion_times(view:View) {
        return settings.show_completion_times(view);
    }
}

class Types {
    public static var control_struct = Re.compile( "\\s+(if|switch|for|while)\\s*\\($" );    
}


class CompletionContext {
    public function new(view:View, project:Project, offset:Int, options:CompletionOptions, settings:CompletionSettings, prefix:String) 
    {
        this.view = view;

        this.prefix = prefix;

        // position in src where auto completion was triggered
        this.offset = offset;
    
        // current project
        this.project = project;
        
        // context independent completion options
        this.options = options;

        // user settings
        this.settings = settings;

        this.view_id = view.id();

        this.id = get_completion_id();

        this.view_pos = Viewtools.get_first_cursor_pos(view);

    }
   

    @lazyprop
    public function complete_offset_in_bytes() {
        var s = src_until_complete_offset()
        
        var s_bytes = s.encode();
        
        
        return s_bytes.length;
    }

    @lazyprop
    public function orig_file() {
        return view.file_name();
    }

    // build which is used for current compiler completion
    @lazyprop
    public function build() {
        if (!project.has_build()) {
            project.extract_build_args();
        }
        return project.get_build( view ).copy();
    }

    // indicates if completion starts after the first ( after a control struct like while, if, for etc.
    @lazyprop
    public function complete_char_is_after_control_struct() {
        return in_control_struct() && complete_char() == "(";
    }

    @lazyprop
    public function in_control_struct() {
        return control_struct.search( self.src_until_complete_offset ) is not None
    }

    @lazyprop
    public function src_until_complete_offset() {
        return self.src[0:self.complete_offset]
    }

    @lazyprop 
    public function line_after_offset() {
        line_end = self.src.find("\n", self.offset)
        return self.src[self.offset:line_end]
    }

    // src of current file
    @lazyprop
    public function src () {
        return Viewtools.get_content(view);
    }

    @lazyprop
    public function complete_char () {
        return src().charAt(complete_offset()-1);
    }

    @lazyprop
    public function src_from_complete_to_offset() {
        return src.substring(complete_offset(), offset);
    }

    @lazyprop
    public function src_from_complete_to_prefix_end() {
        rest = src().substring(complete_offset()+1, offset+1 + prefix.length);
        trace("REEEEEEEEEEST:'" + rest + "'");
        return rest;
    }
                
    @lazyprop
    public function offset_char () {
        return src().charAt(offset);
    }

    @lazyprop
    public function _completion_info() {
        trace("CALLED ONCE")
        return get_completion_info(view, offset, src)
    }

    @lazyprop
    public function commas(self) {
        return _completion_info()[0];
    }

    @lazyprop
    public function prev_symbol_is_comma() {
        return _completion_info()[2];
    }

    // position in source where compiler completion gets triggered
    @lazyprop
    public function complete_offset() {
        return self._completion_info[1];
    }

    @lazyprop
    public function is_new() {
        return self._completion_info[3];
    }

    @lazyprop
    public function src_until_offset () {
        return self.src().substring(0,offset-1);
    }

    @lazyprop
    public function temp_completion_src() 
    {
        return src().substr(0,complete_offset) + "|" + src().substr(complete_offset);
    }


    @lazyprop
    public function prefix_is_whitespace() {
        return StringTools.is_whitespace_or_empty(prefix);
    }

    public function eq (other:CompletionContext) {

        function prefix_check() 
        {
            var prefix_same = true;
            if (options.types.has_hint()) 
            {
                prefix_same = this.prefix == other.prefix || (this.prefix_is_whitespace() && other.prefix_is_whitespace());
            }

            trace("same PREFIX:" + Std.string(prefix_same))
            trace("PREFIXES:" + this.prefix + " - " + other.prefix)
            return prefix_same
        }

        return 
               this != None 
            && other != None
            && this.orig_file == other.orig_file
            && this.offset == other.offset
            && this.commas == other.commas
            && this.src_until_offset == other.src_until_offset
            && this.options.eq(other.options)
            && this.complete_char == other.complete_char
            && this.line_after_offset == other.line_after_offset
            && prefix_check();
    }


    public static function count_commas_and_complete_offset (src, prev_comma, complete_offset) 
    {
        var commas = 0;
        var closed_pars = 0;
        var closed_braces = 0;
        var closed_brackets = 0;

        for i in range( prev_comma , 0 , -1 ) :
            c = src[i]
            if c == ")" :
                closed_pars += 1
            elif c == "(" :
                if closed_pars < 1 :
                    complete_offset = i+1
                    break
                else :
                    closed_pars -= 1
            elif c == "," :
                if closed_pars == 0 and closed_braces == 0 and closed_brackets == 0 :
                    commas += 1
            elif c == "{" :
                #commas = 0
                closed_braces -= 1

            elif c == "}" :
                closed_braces += 1
            elif c == "[" :
                #commas = 0
                closed_brackets -= 1
            elif c == "]" :
                closed_brackets += 1

        return (commas, complete_offset)
    }


    public static function get_completion_info (view, offset, src) 
    {
        prev = src[offset-1]
        commas = 0
        
        complete_offset = offset
        is_new = False
        prev_symbol_is_comma = False
        if (prev == " " and (offset-4 >= 0) and src[offset-4:offset-1] == "new"):
            is_new = True
        elif prev not in "(.;" :
            fragment = view.substr(sublime.Region(0,offset))
            prev_dot = fragment.rfind(".")
            prev_par = fragment.rfind("(")
            prev_comma = fragment.rfind(",")
            prev_colon = fragment.rfind(":")
            prev_brace = fragment.rfind("{")
            prev_semi = fragment.rfind(";")
            
            
            prev_symbol = max(prev_dot,prev_par,prev_comma,prev_brace,prev_colon, prev_semi)
            
            if prev_symbol == prev_comma:
                commas, complete_offset = count_commas_and_complete_offset(src, prev_comma, complete_offset)
                #print("closedBrackets : " + str(closedBrackets))
                prev_symbol_is_comma = True
            else :
                complete_offset = max( prev_dot + 1, prev_par + 1 , prev_colon + 1, prev_brace + 1, prev_semi + 1 )
                
        log("COMPLETE_CHAR:" + src[complete_offset-1])
        return (commas, complete_offset, prev_symbol_is_comma, is_new)
    }




}

class CompletionInfo 
{
    public function new(commas:Int, complete_offset:Int, toplevel_complete, is_new:Bool) 
    {
        this.commas = commas;
        this.complete_offset = complete_offset;
        this.toplevel_complete = toplevel_complete;
        this.is_new = is_new;
    }
}



/*
import sublime
import re

import time

from haxe.plugin import is_st3


from haxe.tools.decorator import lazyprop
from haxe.tools import viewtools, stringtools
from haxe.log import log
from haxe.completion.hx import constants as hcc
from haxe import settings





def get_completion_id ():
    # make the current time the id for this completion
    return time.time()





*/