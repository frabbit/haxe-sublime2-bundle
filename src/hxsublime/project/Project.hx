package hxsublime.project;

import hxsublime.build.Build;
import hxsublime.build.HxmlBuild;
import hxsublime.compiler.Server;
import hxsublime.Haxelib.HaxeLibManager;
import hxsublime.panel.Panels;
import hxsublime.project.CompletionState.ProjectCompletionState;
import hxsublime.Settings;
import hxsublime.tools.HxSrcTools;
import hxsublime.tools.HxSrcTools.HaxeTypeBundle;
import hxsublime.tools.PathTools;
import hxsublime.tools.ViewTools;
import python.lib.Os;
import python.lib.os.Path;
import python.lib.Re;
import python.Dict;
import python.Set;
import python.Tuple;

import sublime.Edit;
import sublime.Region;
import sublime.Sublime;
import sublime.View;
import hxsublime.tools.HxSrcTools.Regex in HxRegex;
using hxsublime.support.ArrayTools;
//using Settings;


enum BuildType {
    Run;
    Build;
    Check;
}


class Project
{
    var _haxelibManager:HaxeLibManager;
    var _currentBuild:Build;
    var _selectingBuild:Bool;
    var _projectFile:String;
    var _projectId:String;
    var _projectPath:String;
    var _stdBundle:HaxeTypeBundle;
    var _stdPaths:Array<String>;
    var _serverMode:Bool;

    public var completionContext:ProjectCompletionState;
    public var builds:Array<Build>;
    public var winId:Int;
    public var server:Server;

    public function new (id, file:String, win_id, server_port:Int) {

        this.completionContext = new ProjectCompletionState();
        this._haxelibManager = new HaxeLibManager(this);
        this._currentBuild = null;
        this._selectingBuild = false;
        this.builds = [];
        this.winId = win_id;
        this.server = new Server(server_port);
        this._projectFile = file;
        this._projectId = id;
        if (this._projectFile != null) {
            this._projectPath = Path.normpath(Path.dirname(this._projectFile));
        }
        else {
            this._projectPath = null;
        }
        updateCompilerInfo();
    }


    public function haxelibManager ()
    {
        return _haxelibManager;
    }

    function projectDir (defaultVal:String)
    {
        return if (_projectPath != null) _projectPath else defaultVal;
    }


    public function nmeExec (view:View = null)
    {
        return [Settings.haxelibExec(), "run", "nme"];
    }

    public function openflExec (view:View = null)
    {
        return [Settings.haxelibExec(), "run", "openfl"];
    }

    public function haxelibExec (view:View = null)
    {
        return [Settings.haxelibExec()];
    }

    public function haxeExec (view:View = null)
    {
        var exec = Settings.haxeExec(view);
        if (!Path.isabs(exec) && exec != "haxe") {
            var cwd = projectDir(".");
            exec = Path.normpath(Path.join(cwd, Settings.haxeExec(view)).split("/").join(Os.sep));
        }
        return [exec];
    }


    public function haxeEnv (view:View = null)
    {
        return haxeBuildEnv(projectDir("."));
    }


    public function startServer(view:View)
    {
        var cwd = projectDir(".");
        var haxe_exec = haxeExec(view)[0];

        var env = haxeEnv();

        server.start(haxe_exec, cwd, env);
    }


    public function restartServer ( view:View)
    {
        server.stop(startServer.bind( view ) );
    }

    public function isServerMode ()
    {
        return _serverMode && Settings.useHaxeServermode();
    }

    function isServerModeForBuilds ()
    {
        return isServerMode() && Settings.useHaxeServermodeForBuilds();
    }

    public function generateBuild( view:View)
    {
        var fn = view.file_name();

        var is_hxml_build = function () return Std.is(this._currentBuild, HxmlBuild);

        if (_currentBuild != null && is_hxml_build() && fn == _currentBuild.buildFile() && view.size() == 0) {
            function run_edit(v:View, e:Edit) {
                var hxml_src = _currentBuild.makeHxml();
                v.insert(e,0,hxml_src);
            }

            ViewTools.asyncEdit(view, run_edit);
        }
    }

    public function selectBuild( view:View )
    {
        var scopes = view.scope_name(view.sel()[0].end()).split(" ");

        if (Lambda.has(scopes, 'source.hxml')) {
            view.run_command("save");
        }

        extractBuildArgs( view , true );
    }

    public function extractBuildArgs( view:View = null , force_panel = false )
    {
        if (view == null) {
            view = Sublime.active_window().active_view();
        }

        var folders = getFolders(view);

        this.builds = findBuildsInFolders(folders);


        var num_builds = builds.length;

        var view_build_id:Int = view.settings().get("haxe-current-build-id");


        if (view_build_id != null && view_build_id < num_builds && !force_panel)
        {
            setCurrentBuild( view , view_build_id );
        }
        else if (num_builds == 1)
        {
            if (force_panel)
            {
                Sublime.status_message("There is only one build");
            }
            setCurrentBuild( view , 0 );
        }
        else if (num_builds == 0 && force_panel)
        {
            Sublime.status_message("No build files found (e.g. hxml, nmml, xml)");
            createNewHxml(view, folders[0]);
        }
        else if (num_builds > 1 && force_panel)
        {
            showBuildSelectionPanel(view);
        }
        else
        {
            setCurrentBuild( view , 0 );
        }
    }

    public function hasBuild ()
    {
        return _currentBuild != null;
    }

    public function checkBuild(view:View)
    {
        build(view, Check);
    }

    public function justBuild(view:View)
    {
        build(view, Build);
    }

    public function runBuild( view:View )
    {
        build(view, Run);
    }

    function updateCompilerInfo ()
    {
        var info = collectCompilerInfo(haxeExec(), _projectPath);

        var bundle = info._1,
            ver = info._2,
            std_paths = info._3;

        //assume it's supported if no version available
        this._serverMode = ver == null || ver >= 209;

        this._stdBundle = bundle;
        this._stdPaths = std_paths;
    }




    // TODO rewrite this function and make it understandable

    function findBuildsInFolders(folders:Array<String>):Array<Build>
    {
        var builds:Array<Build> = [];
        trace("find builds start");
        for (f in folders)
        {
            builds.extend(hxsublime.build.Tools.findHxmlProjects(this, f).map(function (x):Build return x));
            builds.extend(hxsublime.build.Tools.findNmeProjects(this, f).map(function (x):Build return x));
            builds.extend(hxsublime.build.Tools.findOpenflProjects(this, f).map(function (x):Build return x));
        }

        trace("find builds end");
        return builds;
    }

    function getViewFileName (view:View)
    {
        if (view == null)
        {
            view = Sublime.active_window().active_view();
        }
        return view.file_name();
    }

    function getCurrentWindow (view:View)
    {
        return hxsublime.project.Tools.getWindow(view);
    }

    function getFolders (view:View)
    {
        var win = getCurrentWindow(view);
        var folders = win.folders();
        return folders;
    }

    function createNewHxml (view:View, folder:String)
    {
        var win = Sublime.active_window();
        var f = Path.join(folder,"build.hxml");

        this._currentBuild = null;
        this.getBuild(view);
        this._currentBuild.setHxml(f);

        //for whatever reason generate_build doesn't work without transient
        win.open_file(f,Sublime.TRANSIENT);

        this.setCurrentBuild( view , 0 );
    }

    function showBuildSelectionPanel(view:View)
    {

        var buildsView = [for (b in builds) [b.toString(), Path.basename(b.buildFile())]];


        this._selectingBuild = true;
        Sublime.status_message("Please select your build");

        function onSelected (i:Int) {
            this._selectingBuild = false;
            this.setCurrentBuild(view, i);
        }

        var win = Sublime.active_window();

        win.show_quick_panel( buildsView , onSelected  , Sublime.MONOSPACE_FONT );
    }

    function setCurrentBuild( view:View , id:Int )
    {

        trace( "setCurrentBuild");

        if (id < 0 || id >= this.builds.length) {
            id = 0;
        }

        if (this.builds.length > 0) {
            view.settings().set("haxe-current-build-id", id);
            this._currentBuild = this.builds[id];
            this._currentBuild.setStdBundle(this._stdBundle);

            view.set_status("haxe-build",this._currentBuild.toString());
            //hxpanel.default_panel().writeln( "build selected: " + this._currentBuild.to_string() )
        }
        else {
            view.set_status("haxe-build","No build found/selected");
            //hxpanel.default_panel().writeln( "No build found/selected" )
        }

    }

    function build(view:View, type:BuildType)
    {

        if (view == null) {
            view = Sublime.active_window().active_view();
        }

        var win = view.window();

        var env = haxeBuildEnv(projectDir("."));

        var build:Build = null;
        if (hasBuild()) {
            build = getOriginalBuild(view);
        }
        else {
            extractBuildArgs(view);
            build = getOriginalBuild(view);
        }

        var r = null;

        switch (type) {
            case Run:
                r = build.prepareRunCmd(this, this.isServerModeForBuilds(), view);
            case Build:
                r  = build.prepareBuildCmd(this, this.isServerModeForBuilds(), view);
            case Check:
                r = build.prepareCheckCmd(this, this.isServerMode(), view);
        }


        var cmd = r._1;
        var build_folder = r._2;


        var escaped_cmd = build.escapeCmd(cmd);


        Panels.defaultPanel().writeln("running: " + escaped_cmd.join(" "));



        win.run_command("hxsublime_commands__haxe_exec", python.Lib.anonToDict({
            cmd: cmd,
            is_check_run : type == Check,
            working_dir: build_folder,
            file_regex : Tools.haxeFileRegex,
            env : env
        }));

    }

    public function clearBuild()
    {
        _currentBuild = null;
        completionContext.clearCompletion();
    }

    public function destroy ()
    {
        server.stop();
    }


    // TODO rewrite this function and make it understandable
    function createDefaultBuild (view:View):Build
    {
        var fn = view.file_name();

        var src_dir = Path.dirname( fn );

        var src = view.substr( new Region(0, view.size()));

        var build = new HxmlBuild(null, null);
        build._target = "js";

        var folder = Path.dirname(fn);
        var folders = view.window().folders();
        for (f in folders) {
            if (fn.indexOf(f) > -1) {
                folder = f;
            }
        }

        var pack = [];
        for (ps in HxRegex.package_line.findallString( src ))
        {
            if (ps == "") continue;

            pack = ps.split(".");
            var packrev = pack.copy();
            packrev.reverse();
            for (p in packrev) {
                var spl = Path.split( src_dir );
                if( spl._2 == p ) {
                    src_dir = spl._1;
                }
            }
        }

        var cl = Path.basename(fn);

        cl = cl.substring(0, cl.lastIndexOf("."));

        var main = pack.copy();
        main.push( cl );
        build.main = main.join( "." );

        build.output = Path.join(folder,build.main.toLowerCase() + ".js");

        build.addArg( Tuple2.make("-cp" , src_dir) );

        build.addArg( Tuple2.make("-js" , build.output ) );

        build.setHxml(Path.join( src_dir , "build.hxml"));
        return build;
    }

    public function getOriginalBuild( view:View )
    {
        if (_currentBuild == null && view.score_selector(0,"source.haxe.2") > 0)
        {
            this._currentBuild = createDefaultBuild(view);
        }

        return this._currentBuild;
    }


    public function getBuild( view:View )
    {
        return getOriginalBuild(view).copy();
    }


    // STATIC SECTION

    static function haxeBuildEnv (project_dir:String)
    {

        var lib_path = Settings.haxeLibraryPath();
        var haxe_inst_path = Settings.haxeInstPath();
        var neko_inst_path = Settings.nekoInstPath();


        var env = Os.environ.copy();

        var env_path = Os.environ.copy().get("PATH", "");

        var paths = [];


        var path = null;

        if (lib_path != null)
        {

            if (PathTools.isAbsPath(lib_path)) {
                path = lib_path;
            } else {
                path = Path.normpath(Path.join(project_dir, lib_path));
            }

            env.set("HAXE_LIBRARY_PATH", path.split("/").join(Os.sep));
            env.set("HAXE_STD_PATH", path.split("/").join(Os.sep));
        }


        if (haxe_inst_path != null) {
            if (PathTools.isAbsPath(haxe_inst_path)) {
                path = haxe_inst_path;
            } else {
                path = Path.normpath(Path.join(project_dir, haxe_inst_path));
            }

            env.set("HAXEPATH", path.split("/").join(Os.sep));
            paths.push(path.split("/").join(Os.sep));
        }

        if (neko_inst_path != null)
        {
            path = Path.normpath(Path.join(project_dir, neko_inst_path));
            env.set("NEKO_INSTPATH", path.split("/").join(Os.sep));
            paths.append(path.split("/").join(Os.sep));
        }


        if (paths.length > 0)
        {
            env.set("PATH", paths.join(Os.pathsep) + Os.pathsep + env_path);
        }

        return env;
    }


    static function getCompilerInfoEnv (project_path:String)
    {
        return haxeBuildEnv(project_path);
    }


    static function collectCompilerInfo (haxeExec:Array<String>, project_path:String)
    {
        var env = getCompilerInfoEnv(project_path);
        var cmd = haxeExec.copy();

        cmd.extend(["-main", "Nothing", "-v", "--no-output"]);


        var r = Execute.runCmd( cmd, null,null,env );

        var out = r._1;
        var err = r._2;


        var stdClasspaths = parseStdClasspaths(out);

        var bundle = collectStdClassesAndPacks(stdClasspaths);

        var ver = extractHaxeVersion(out);

        return Tuple3.make(bundle, ver, stdClasspaths);
    }

    static function extractHaxeVersion (out:String)
    {
        var ver = Re.search( haxeVersionRegex , out );
        return if (ver != null) Std.parseInt(ver.group(1)) else null;
    }


    static function removeTrailingPathSep(path:String)
    {
        if (path.length > 1)
        {
            var last_pos = path.length-1;
            var last_char = path.charAt(last_pos);
            if (last_char == "/" ||  last_char == "\\" || last_char == Path.sep)
            {
                path = path.substring(0,last_pos);
            }
        }
        return path;
    }

    static function isValidClasspath(path:String)
    {
        return path.length > 1 && Path.exists(path) && Path.isdir(path);
    }

    static function parseStdClasspaths (out:String)
    {
        var m = classpathLineRegex.match(out);

        var stdClasspaths = [];

        var all_paths = m.group(1).split(";");
        var ignored_paths = [".","./"];

        var std_paths = if (m != null) new Set(all_paths).difference(new Set(ignored_paths)) else new Set();

        for (p in std_paths.iterator())
        {
            var p = Path.normpath(p);

            p = removeTrailingPathSep(p);

            if (isValidClasspath(p))
            {
                stdClasspaths.append(p);
            }
        }
        return stdClasspaths;
    }

    static function collectStdClassesAndPacks(stdCps:Array<String>)
    {
        var bundle = HxSrcTools.emptyTypeBundle();
        for (p in stdCps)
        {
            var bundle1 = hxsublime.Types.extractTypes( p, [], [], 0, [], false );
            bundle = bundle.merge(bundle1);
        }
        return bundle;
    }

    static var classpathLineRegex = Re.compile("Classpath : (.*)");
    static var haxeVersionRegex = Re.compile("haxe_([0-9]{3})", Re.M);
}
