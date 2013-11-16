package hxsublime.completion.hx;

import hxsublime.build.Build;
import hxsublime.completion.hx.Constants;
import hxsublime.project.Project;
import hxsublime.Settings;
import hxsublime.tools.StringTools;
import hxsublime.tools.ViewTools;
import python.lib.Builtin;
import python.lib.Re;
import python.lib.Time;
import python.lib.Types.Tup2;
import python.lib.Types.Tup4;
import python.lib.Types.Tup5;
import sublime.Region;
import sublime.View;

using python.lib.StringTools;


using python.lib.ArrayTools;

class CompletionResult {
    
    public static function empty_result (ctx:CompletionContext, retrieve_toplevel_comps = null) {
        return new CompletionResult("", [], "", [], ctx, retrieve_toplevel_comps);
    }


    public var ret:String;
    public var comps:Array<Tup2<String, String>>;
    public var status:String;
    public var hints:Array<Array<String>>;
    public var ctx:CompletionContext;

    public var retrieve_toplevel_comps:Void->Array<Tup2<String, String>>;



    public function new (ret:String, comps:Array<Tup2<String, String>>, status:String, hints:Array<Array<String>>, ctx:CompletionContext, retrieve_toplevel_comps:Void->Array<Tup2<String, String>>) 
    {
        
        this.ret = ret;
        this.comps = comps;
        this.status = status;
        this.hints = hints;
        this.ctx = ctx;
        if (retrieve_toplevel_comps == null) {
            
            retrieve_toplevel_comps = function () return [];
        }

        this.retrieve_toplevel_comps = retrieve_toplevel_comps;
    }

        

    var _lazy_toplevel_comps = null;

    @lazyprop
    public function _toplevel_comps():Array<Tup2<String, String>> {
        
        if (_lazy_toplevel_comps == null) {
            _lazy_toplevel_comps = retrieve_toplevel_comps();
            
        }        
        
        return _lazy_toplevel_comps;
    }


    public function has_hints () {
        return hints.length > 0;
    }

    public function has_compiler_results () {
        return comps.length > 0;
    }

    public function has_results () {
        return comps.length > 0 || hints.length > 0 || (requires_toplevel_comps() && this._toplevel_comps().length > 0);
    }

    public function show_top_level_snippets () {

        var req = requires_toplevel_comps();

        
        var r = req && !ctx.is_new();

        

        return r;
    }

    

    public function requires_toplevel_comps() 
    {
        var prefix_is_whitespace = hxsublime.tools.StringTools.isWhitespaceOrEmpty(ctx.prefix);
        trace("prefix_is_whitespace:" + Std.string(prefix_is_whitespace));
        trace("has_hints:" + Std.string(this.has_hints()));
        trace("has_hint:" + Std.string(this.ctx.options.types().has_hint()));
        trace("has_compiler_results:" + Std.string(this.has_compiler_results()));
        var r = !((prefix_is_whitespace && has_hints() && ctx.options.types().has_hint()) || has_compiler_results());
        trace("requires_toplevel_comps:" + r);
        return r;
    }

    public function all_comps () {
        
        var res = [];
        
        if (requires_toplevel_comps()) {
            res.extend(_toplevel_comps());
        }
        res.extend(comps);
        res.sort(function (s1, s2) return (s1._1 < s2._1) ? -1 : (s1._1 > s2._1) ? 1 : 0);
        return res;
    }

}


typedef TODO = #if debug #error "type is not yet defined" #else Dynamic #end

class CompletionBuild {

    public var build:Build;
    public var ctx:CompletionContext;
    public var temp_path:String;
    public var temp_file:String;
    public var cache:TODO;

    public function new (ctx:CompletionContext, temp_path:String, temp_file:String)
    {
        this.build = ctx.build().copy();
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

    var _types:CompletionTypes;
    var _toplevel:TopLevelOptions;
    var _context:Int;
    var _trigger:Int;

    public function new(trigger:Int, context = Constants.COMPILER_CONTEXT_REGULAR, types = Constants.COMPLETION_TYPE_REGULAR, toplevel = Constants.COMPLETION_TYPE_TOPLEVEL)
    {
        this._types = new CompletionTypes(types);
        this._toplevel = new TopLevelOptions(toplevel);
        this._context = context;
        this._trigger = trigger;
    }

    public function copy_as_manual() 
    {
        return new CompletionOptions(Constants.COMPLETION_TRIGGER_MANUAL, this._context, this.types().val(), this._toplevel.val());
    }

    public function copy_as_async() 
    {
        return new CompletionOptions(Constants.COMPLETION_TRIGGER_ASYNC, this._context, this.types().val(), this._toplevel.val());
    }

    @property
    public function types() 
    {
        return this._types;
    }


    @lazyprop
    public function async_trigger() 
    {
        return this._trigger == Constants.COMPLETION_TRIGGER_ASYNC;
    }

    @lazyprop
    public function manual_completion() 
    {
        return this._trigger == Constants.COMPLETION_TRIGGER_MANUAL;
    }

    @lazyprop
    public function macro_completion() 
    {
        return this._context == Constants.COMPILER_CONTEXT_MACRO;
    }

    @lazyprop
    public function regular_completion() 
    {
        return this._context == Constants.COMPILER_CONTEXT_REGULAR;
    }

    public function eq (other:CompletionOptions) 
    {
        return this._trigger == other._trigger && this._types.eq(other._types) && this._toplevel.eq(other._toplevel) && this._context == other._context;
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


typedef SettingsInterface = {
    //public function smarts_hints_only_next(?view:View):Bool;
    public function no_fuzzy_completion(?view:View):Bool;
    public function top_level_completions_on_demand(?view:View):Bool;
    public function is_async_completion(?view:View):Bool;
    public function show_only_async_completions(?view:View):Bool;
    public function get_completion_delays(?view:View):Tup2<Int, Int>;
    public function show_completion_times(?view:View):Bool;
}

class CompletionSettings {
    var settings:SettingsInterface;
    public function new(settings)
    {

        this.settings = settings;
    }

    //@lazyprop
    //public function smarts_hints_only_next() {
    //    return settings.smarts_hints_only_next();
    //}

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

    static function get_completion_id () {
        // make the current time the id for this completion
        return Time.time();
    }

    public var prefix:String;
    public var view : View;
    public var view_id : Int;
    public var id : Int;
    public var options:CompletionOptions;
    public var settings:CompletionSettings;
    public var offset:Int;
    public var project:Project;
    public var view_pos:Int;

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

        this.view_pos = ViewTools.getFirstCursorPos(view);

    }
   

    var lazyCompleteOffsetInBytes:Int;

    @lazyprop
    public function complete_offset_in_bytes() 
    {
        if (lazyCompleteOffsetInBytes == null) {
            var s = src_until_complete_offset();
            
            var s_bytes = s.encode();
            
            
            lazyCompleteOffsetInBytes = s_bytes.length;
        }
        return lazyCompleteOffsetInBytes;
    }

    @lazyprop
    public function orig_file() {
        return view.file_name();
    }

    // build which is used for current compiler completion
    var lazyBuild = null;
    @lazyprop
    public function build() 
    {
        if (lazyBuild == null) {
            if (!project.has_build()) {
                project.extract_build_args();
            }
            lazyBuild = project.get_build( view ).copy();
        }
        return lazyBuild;
    }

    // indicates if completion starts after the first ( after a control struct like while, if, for etc.
    @lazyprop
    public function complete_char_is_after_control_struct() {
        return in_control_struct() && complete_char() == "(";
    }

    @lazyprop
    public function in_control_struct() {
        return Types.control_struct.search( this.src_until_complete_offset() ) != null;
    }

    @lazyprop
    public function src_until_complete_offset() {
        return this.src().substring(0,this.complete_offset());
    }

    @lazyprop 
    public function line_after_offset() {
        var line_end = this.src().indexOf("\n", this.offset);
        return this.src().substring(this.offset,line_end);
    }

    // src of current file


    var _lazy_src = null;
    @lazyprop
    public function src () {
        if (_lazy_src == null) {
            _lazy_src = ViewTools.getContent(view);
        }
        return _lazy_src;
    }


    var lazyCompleteChar = null;

    @lazyprop
    public function complete_char () {
        if (lazyCompleteChar == null) {
            lazyCompleteChar = src().charAt(complete_offset()-1);
        }
        return lazyCompleteChar;
    }

    @lazyprop
    public function src_from_complete_to_offset() {
        return src().substring(complete_offset(), offset);
    }

    @lazyprop
    public function src_from_complete_to_prefix_end() {
        var rest = src().substring(complete_offset()+1, offset+1 + prefix.length);
        
        return rest;
    }
                
    @lazyprop
    public function offset_char () {
        return src().charAt(offset);
    }

    @lazyprop
    public function _completion_info() {
        
        return get_completion_info(view, offset, src());
    }

    @lazyprop
    public function commas() {
        return _completion_info()._1;
    }

    @lazyprop
    public function prev_symbol_is_comma() {
        return _completion_info()._3;
    }

    // position in source where compiler completion gets triggered
    @lazyprop
    public function complete_offset() {
        return this._completion_info()._2;
    }

    @lazyprop
    public function is_new() {
        return this._completion_info()._4;
    }

    @lazyprop
    public function src_until_offset () {
        return this.src().substring(0,offset-1);
    }

    @lazyprop
    public function temp_completion_src() 
    {
        return src().substr(0,complete_offset()) + "|" + src().substr(complete_offset());
    }


    @lazyprop
    public function prefix_is_whitespace() 
    {
        return hxsublime.tools.StringTools.isWhitespaceOrEmpty(prefix);
    }

    public function eq (other:CompletionContext) {

        function prefix_check() 
        {
            var prefix_same = true;
            if (options.types().has_hint()) 
            {
                prefix_same = this.prefix == other.prefix || (this.prefix_is_whitespace() && other.prefix_is_whitespace());
            }

            trace("same PREFIX:" + Std.string(prefix_same));
            trace("PREFIXES:" + this.prefix + " - " + other.prefix);
            return prefix_same;
        }

        return 
               this != null 
            && other != null
            && this.orig_file == other.orig_file
            && this.offset == other.offset
            && this.commas == other.commas
            && this.src_until_offset == other.src_until_offset
            && this.options.eq(other.options)
            && this.complete_char == other.complete_char
            && this.line_after_offset == other.line_after_offset
            && prefix_check();
    }


    public static function count_commas_and_complete_offset (src:String, prev_comma:Int, complete_offset:Int) 
    {
        var commas = 0;
        var closed_pars = 0;
        var closed_braces = 0;
        var closed_brackets = 0;

        for (j in 0...prev_comma) 
        {
            var i = prev_comma - j;
            
            var c = src.charAt(i);
            
            if (c == ")" )
            {
                closed_pars += 1;
            }
            else if (c == "(" )
            {
                if (closed_pars < 1 )
                {
                    complete_offset = i+1;
                    break;
                }
                else 
                {
                    closed_pars -= 1;
                }
            }
            else if (c == "," )
            {
                if (closed_pars == 0 && closed_braces == 0 && closed_brackets == 0 )
                {
                    commas += 1;
                }
            }
            else if (c == "{" )
            {
                //commas = 0
                closed_braces -= 1;
            }
            else if (c == "}" )
            {
                closed_braces += 1;
            }
            else if (c == "[" )
            {
                //commas = 0
                closed_brackets -= 1;
            }
            else if (c == "]" )
            {
                closed_brackets += 1;
            }
        }
        return Tup2.create(commas, complete_offset);
    }


    public static function get_completion_info (view:View, offset:Int, src:String) 
    {
        var prev = src.charAt(offset-1);
        var commas = 0;
        
        var complete_offset = offset;
        var is_new = false;
        var prev_symbol_is_comma = false;
        if (prev == " " && (offset-4 >= 0) && src.substring(offset-4,offset-1) == "new")
        {
            is_new = true;
        }
        else if (!"(.;".contains(prev) ) 
        {
            var fragment = view.substr(new Region(0,offset));
            var prev_dot = fragment.lastIndexOf(".");
            var prev_par = fragment.lastIndexOf("(");
            var prev_comma = fragment.lastIndexOf(",");
            var prev_colon = fragment.lastIndexOf(":");
            var prev_brace = fragment.lastIndexOf("{");
            var prev_semi = fragment.lastIndexOf(";");
            
            

            

            var prev_symbol = Builtin.max(prev_dot,prev_par,prev_comma,prev_brace,prev_colon, prev_semi);
            
            if (prev_symbol == prev_comma)
            {
                var r = count_commas_and_complete_offset(src, prev_comma, complete_offset);
                commas = r._1;
                complete_offset = r._2;
                //print("closedBrackets : " + str(closedBrackets))
                prev_symbol_is_comma = true;
            }
            else 
            {
                complete_offset = Builtin.max( prev_dot + 1, prev_par + 1 , prev_colon + 1, prev_brace + 1, prev_semi + 1 );
            }
        }
                
        //trace("COMPLETE_CHAR:" + src.charAt(complete_offset-1));

        return Tup4.create(commas, complete_offset, prev_symbol_is_comma, is_new);
    }




}

// class CompletionInfo 
// {

//     public var commas:Int;
//     public var complete_offset:Int;
//     public var toplevel_complete:Bool;
//     public var is_new:Bool;
//     public function new(commas:Int, complete_offset:Int, toplevel_complete:Bool, is_new:Bool) 
//     {
//         this.commas = commas;
//         this.complete_offset = complete_offset;
//         this.toplevel_complete = toplevel_complete;
//         this.is_new = is_new;
//     }
// }



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