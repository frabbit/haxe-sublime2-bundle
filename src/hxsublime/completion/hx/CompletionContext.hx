package hxsublime.completion.hx;

import hxsublime.build.Build;
import hxsublime.completion.hx.CompletionOptions;
import hxsublime.completion.hx.CompletionSettings;
import hxsublime.macros.LazyFunctionSupport;
import hxsublime.project.CompletionState.CompletionCache;
import hxsublime.project.Project;
import hxsublime.Settings;
import hxsublime.tools.StringTools;
import hxsublime.tools.ViewTools;
import python.lib.Builtins;
import python.lib.Re;
import python.lib.Time;
import python.Tuple;
import sublime.Region;
import sublime.View;

using hxsublime.support.StringTools;

using hxsublime.support.ArrayTools;

class CompletionContext implements LazyFunctionSupport
{
    static var controlStructRegex = Re.compile( "\\s+(if|switch|for|while)\\s*\\($" );

    static function getCompletionId () {
        return Std.int(Time.time());
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

        this.id = getCompletionId();

        this.view_pos = ViewTools.getFirstCursorPos(view);
    }

    @lazyFunction
    public function isHint()
    {
        var whitespace_re = Re.compile("^\\s*$");
        return "(,".indexOf(completeChar()) > -1 && Re.match(whitespace_re, prefix) != null;
    }

    @lazyFunction
    public function complete_offset_in_bytes()
    {
        var s = srcUntilCompleteOffset();
        var b = s.encode();

        return b.length;
    }

    @lazyFunction
    public function orig_file()
    {
        return view.file_name();
    }

    // build which is used for current compiler completion

    @lazyFunction
    public function build()
    {
        if (!project.hasBuild()) {
            project.extractBuildArgs();
        }
        return project.getBuild( view ).copy();
    }

    // indicates if completion starts after the first ( after a control struct like while, if, for etc.
    @lazyFunction
    public function completeCharIsAfterControlStruct()
    {
        return inControlStruct() && completeChar() == "(";
    }

    @lazyFunction
    public function inControlStruct()
    {
        return controlStructRegex.search( this.srcUntilCompleteOffset() ) != null;
    }

    @lazyFunction
    function srcUntilCompleteOffset()
    {
        return this.src().substring(0,this.complete_offset());
    }

    @lazyFunction
    public function lineAfterOffset()
    {
        var line_end = this.src().indexOf("\n", this.offset);
        return this.src().substring(this.offset,line_end);
    }

    // src of current file
    @lazyFunction
    public function src () {
        return ViewTools.getContent(view);
    }

    @lazyFunction
    public function completeChar () {

        return src().charAt(complete_offset()-1);
    }

    @lazyFunction
    function completionInfo() {

        return get_completion_info(view, offset, src());
    }

    @lazyFunction
    public function commas() {
        return completionInfo()._1;
    }

    // position in source where compiler completion gets triggered
    @lazyFunction
    public function complete_offset() {
        return this.completionInfo()._2;
    }

    @lazyFunction
    public function is_new() {
        return this.completionInfo()._4;
    }

    @lazyFunction
    function srcUntilOffset () {
        return this.src().substring(0,offset-1);
    }

    @lazyFunction
    public function tempCompletionSrc()
    {
        return src().substr(0,complete_offset()) + "|" + src().substr(complete_offset());
    }


    @lazyFunction
    function prefixIsWhitespace()
    {
        return hxsublime.tools.StringTools.isWhitespaceOrEmpty(prefix);
    }

    public function eq (other:CompletionContext) {

        function prefixEq()
        {
            return 
                if (isHint())
                {
                    this.prefix == other.prefix || (this.prefixIsWhitespace() && other.prefixIsWhitespace());
                }
                else true;
        }

        return
               this != null
            && other != null
            && this.orig_file() == other.orig_file()
            && this.offset == other.offset
            && this.commas() == other.commas()
            && this.srcUntilOffset() == other.srcUntilOffset()
            && this.options.eq(other.options)
            && this.completeChar() == other.completeChar()
            && this.lineAfterOffset() == other.lineAfterOffset()
            && this.isHint() == other.isHint()
            && prefixEq();
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
        return Tuple2.make(commas, complete_offset);
    }


    public static function get_completion_info (view:View, offset:Int, src:String)
    {
        var prev = src.charAt(offset-1);
        var commas = 0;

        var complete_offset = offset;
        var is_new = false;
        var prevSymbolIsComma = false;
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

            var prev_symbol = Builtins.max(prev_dot,prev_par,prev_comma,prev_brace,prev_colon, prev_semi);

            if (prev_symbol == prev_comma)
            {
                var r = count_commas_and_complete_offset(src, prev_comma, complete_offset);
                commas = r._1;
                complete_offset = r._2;
                prevSymbolIsComma = true;
            }
            else
            {
                complete_offset = Builtins.max( prev_dot + 1, prev_par + 1 , prev_colon + 1, prev_brace + 1, prev_semi + 1 );
            }
        }

        return Tuple4.make(commas, complete_offset, prevSymbolIsComma, is_new);
    }




}
