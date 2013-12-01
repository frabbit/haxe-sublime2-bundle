package hxsublime.commands;

import hxsublime.build.Build;
import hxsublime.panel.Panels;
import hxsublime.Plugin;
import hxsublime.project.Projects;
import hxsublime.project.Project;
import hxsublime.Temp;
import hxsublime.tools.HxSrcTools;
import hxsublime.tools.PathTools;
import hxsublime.tools.ViewTools;
import python.lib.Codecs;
import python.lib.Json;
import python.lib.os.Path;
import python.lib.Re;
import sublime.Edit;
import sublime.EventListener;
import sublime.Region;
import sublime.Sublime;
import sublime.TextCommand;
import sublime.View;
import python.lib.Types;

import hxsublime.tools.HxSrcTools.Regex in HxRegex;

using python.lib.StringTools;

@:keep class HaxeFindDeclarationCommand extends TextCommand 
{
    override public function run( edit:Edit, ?_:KwArgs ) 
    {
        this.run1(true);
    }

    public function helperMethod()
    {
        return "hxsublime.FindDeclaration.__sublimeFindDecl";
    }


    public function run1 (useDisplay:Bool, order:Int = 1)
    {
        trace("run HaxeFindDeclarationCommand");
        var view = this.view;

        if (view.file_name() == null)
        {
            return;
        }

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



        var helperMethod = this.helperMethod();
        
        var src = ViewTools.getContent(view);


        var packageMatch = Re.match(HxRegex.package_line, src);

        var usingPos = if (packageMatch == null) 0 else packageMatch.end(0);

        var usingInsert = "using hxsublime.FindDeclaration;";

        var srcBeforeUsing = src.substring(0, usingPos);
        //var src_after_using = src.substr(using_pos);

        
        var sel = view.sel()[0];
        var pos = sel.begin();

        var exprEnd = null;
        var exprStart = null;

        if (sel.end() == pos) 
        {

            var r = Helper.getWordAt(view, src, pos);
            var word_str = r._1, word_start = r._2, word_end = r._3;

            var chars = ["{", "+", "-", "(", "[", "*", "/", "=", ";", ":"];
            var res = HxSrcTools.reverse_search_next_char_on_same_nesting_level(src, chars, word_end-1);
            
            res = HxSrcTools.skipWhitespaceOrComments(src, res._1+1);



            exprEnd = word_end;
            exprStart = res._1;
        }
        else 
        {
            exprStart = pos;
            exprEnd = sel.end();
        }
        
        var srcBeforeExpr = src.substring(usingPos,exprStart);

        var srcAfterExpr = src.substr(exprEnd);

        var exprString = src.substring(exprStart,exprEnd);


        var displayStr = if (useDisplay) ".|" else "";

        var insertBefore = helperMethod + "(";


        var orderStr = Std.string(order);
        var insertAfter = ", " + orderStr + ")" + displayStr;

        
        var newSrc = srcBeforeUsing + usingInsert + srcBeforeExpr + insertBefore +  exprString + insertAfter + srcAfterExpr;
        
        //trace(newSrc);

        var r = Helper.prepareBuild(view, project, useDisplay, newSrc);
        var build = r._1, temp_path = r._2, tempFile = r._3;

        function cb (out:String, err:String)
        {
            Temp.removePath(temp_path);

            var filePos = Re.compile("\\|\\|\\|\\|\\|([^|]+)\\|\\|\\|\\|\\|", Re.I);

            var res = Re.search(filePos, out);
            if (res != null) 
            {
                //we've got a proper response
                var json_str = res.group(1);
                var jsonResult = Json.loads(json_str);

                if (jsonResult.hasKey("error")) 
                {
                    var error = jsonResult.get("error", null);
                    trace("nothing found (1), cannot find declaration");
                    if (order == 1 && useDisplay)
                    {
                        this.run1(true, 2);   
                    }
                    else if (order == 2 && useDisplay)
                    {
                        this.run1(true, 3);
                    }
                }    
                else
                {
                    this.handleSuccessfulResult(view, jsonResult, usingInsert, insertBefore, insertAfter, exprEnd, build, temp_path, tempFile);
                }
            }
            else
            {
                if (order == 1 && useDisplay)
                {
                    this.run1(true, 2);
                }
                else if (order == 2 && useDisplay) 
                {
                    this.run1(true, 3);
                }
                else if (useDisplay)
                {
                    trace("nothing found yet (2), try again without display (workaround)");
                    this.run1(false);
                }
                else 
                {
                    Panels.defaultPanel().writeln("Cannot find declaration for expression " + exprString.strip());
                    trace("nothing found (3), cannot find declaration");
                }
            }
        }

        build.run(project, view, false, cb);
    }

    public function handleSuccessfulResult(view:View, jsonResult:Dict<String, Dynamic>, usingInsert:String, insertBefore:String, insertAfter:String, exprEnd:Int, build:Build, temp_path:String, tempFile:String)
    {
        var file = jsonResult.get("file", null);
        var min = jsonResult.get("min", 0);
        var max = jsonResult.get("max", 0);

        var absPath = PathTools.joinNorm(build.getBuildFolder(), file);

        if (absPath == tempFile)
        {
            if (min > exprEnd)
            {
                min -= insertAfter.length;
                min -= insertBefore.length;
            }
            min -= usingInsert.length;
            // we have manually stored a temp file with only \n line endings
            // so we don't have to adjust the real file position and the sublime
            // text position
        }
        else 
        {
            var f = Codecs.open(absPath, "r", "utf-8");
            var realSrc = f.read();
            f.close();
            // line endings could be \r\n, but sublime text has only \n after
            // opening a file, so we have to calculate the offset betweet the
            // returned position and the real position by counting all \r before min
            // should be moved to a utility function
            var offset = 0;
            for (i in 0...min) 
            {
                if (realSrc.charAt(i) == "\r") 
                {
                    offset += 1;
                }
            }
            trace("offset: " + Std.string(offset));

            min -= offset;
        }

        if (absPath == tempFile)
        {
            // file is active view
            //absPath = view.file_name();
            var targetView = view;


            trace("line ending: " + Std.string(view.settings().get("line_ending")));

            targetView.sel().clear();
            targetView.sel().add(new Region(min));

            targetView.show(new Region(min));
        }
        else 
        {
            //global find_decl_pos, find_decl_file
            State.findDeclFile = absPath;
            State.findDeclPos = min;
            // open file and listen => HaxeFindDeclarationListener
            view.window().open_file(absPath);
        }
    }
}
//shared between FindDelaration Command and Listener
private class State 
{
    public static var findDeclFile:Null<String> = null;
    public static var findDeclPos:Null<Int> = null;
}

private class Helper 
{
    static var plugin_path = Plugin.plugin_base_dir();

    public static function getWordAt(view:View, src:String, pos:Int)
    {
        var word = view.word(pos);

        var wordStart = word.a;
        var wordEnd = word.b;

        var wordStr = src.substring(wordStart,wordEnd);

        return Tup3.create(wordStr, wordStart, wordEnd);
    }

    public static function prepareBuild(view:View, project:Project, useDisplay:Bool, newSrc:String)
    {
        var build = project.getBuild(view).copy();
        build.addArg(Tup2.create("-D", "no-inline"));

        var r = Temp.createTempPathAndFile(build, view.file_name(), newSrc);
        var tempPath = r._1, tempFile = r._2;

        build.addClasspath(tempPath);

        build.addClasspath(Path.join(plugin_path, "haxetools"));
        

        trace(build.classpaths);

        build.addArg(Tup2.create("-dce", "no"));

        if (useDisplay)
        {
            build.setAutoCompletion(tempFile + "@0", false);
        }
        return Tup3.create(build, tempPath, tempFile);
    }
}

@:keep class HaxeFindDeclarationListener extends EventListener
{
    override public function on_activated(view:View) 
    {
        //global find_decl_pos, find_decl_file
        if (view != null && view.file_name() != null) 
        {
            if (view.file_name() == State.findDeclFile)
            {
                view.sel().clear();

                var min = State.findDeclPos;

                view.sel().add(new Region(min));
                // move to line is delayed, seems to work better
                // without delay the animation to the region does not work properly sometimes
                function show () 
                {
                    view.show_at_center(new Region(min));
                }
                Sublime.set_timeout(show, 70);
            }
            State.findDeclFile = null;
            State.findDeclPos = null;
        }
    }
}

