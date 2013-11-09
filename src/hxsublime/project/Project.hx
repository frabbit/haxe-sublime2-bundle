package hxsublime.project;

import hxsublime.build.Build;
import hxsublime.compiler.Server;
import hxsublime.Haxelib.HaxeLibManager;
import hxsublime.project.CompletionState.ProjectCompletionState;
import python.lib.os.Path;
import python.lib.Re;
import sublime.Edit;
import sublime.View;




class Project {

    public var completion_context:ProjectCompletionState;
    public var _haxelib_manager:HaxeLibManager;
    public var current_build:Build;
    public var selecting_build:Bool;
    public var builds:Array<Build>;
    public var win_id:Int;
    public var server:Server;
    public var project_file:String;
    public var project_id:String;
    public var project_path:String;


    public function new (id, file:String, win_id, server_port:Int) {
        
        this.completion_context = new ProjectCompletionState();
        this._haxelib_manager = new HaxeLibManager(self);
        this.current_build = null;
        this.selecting_build = false;
        this.builds = [];
        this.win_id = win_id;
        this.server = new Server(server_port);
        this.project_file = file;
        this.project_id = id;
        if (this.project_file != null) {
            this.project_path = Path.normpath(os.path.dirname(self.project_file));
        }
        else {
            self.project_path = null;
        }
        _update_compiler_info();
    }

    
    public function haxelib_manager () 
    {
        return _haxelib_manager;
    } 

    public function project_dir (defaultVal:String) 
    {
        return if (project_path != null) project_path else defaultVal;
    }
            

    public function nme_exec (view:View = null) {
        return [Settings.haxelib_exec(), "run", "nme"];
    }

    public function openfl_exec (view:View = null) {
        return [Settings.haxelib_exec(), "run", "openfl"];
    }

    public function haxelib_exec (view:View = None) {
        return [Settings.haxelib_exec()];
    }

    public function haxe_exec (view:View = null) {
        var haxe_exec = Settings.haxe_exec(view);
        if (!Path.isabs(haxe_exec) && haxe_exec != "haxe") {
            var cwd = project_dir(".");
            haxe_exec = Path.normpath(Path.join(cwd, Settings.haxe_exec(view)).split("/").join(Os.sep));
        }
        return [haxe_exec];
    }

    
    public function haxe_env (view:View = None) {
        return _haxe_build_env(project_dir("."));
    }
    
    
    public function start_server(view:View) {
        var cwd = project_dir(".");
        var haxe_exec = haxe_exec(view)[0];
        
        var env = haxe_env();
        
        server.start(haxe_exec, cwd, env=env);
    }
    

    public function restart_server ( view:View) {
        server.stop(start_server.bind( view ) );
    }

    public function is_server_mode () {
        return server_mode && Settings.use_haxe_servermode();
    }

    public function is_server_mode_for_builds () {
        return is_server_mode() && Settings.use_haxe_servermode_for_builds();
    }

    public function generate_build( view:View) {
        var fn = view.file_name();
        
        var is_hxml_build = function () return Std.is(self.current_build, hxbuild.HxmlBuild);

        if (current_build != None && is_hxml_build() && fn == current_build.hxml && view.size() == 0) {
            function run_edit(v:View, e:Edit) {
                var hxml_src = current_build.make_hxml();
                v.insert(e,0,hxml_src);
                v.end_edit(e);
            }

            viewtools.async_edit(view, run_edit);
        }
    }

    public function select_build( view:View ) 
    {
        var scopes = view.scope_name(view.sel()[0].end()).split();
        
        if (Lambda.has(scopes, 'source.hxml')) {
            view.run_command("save");
        }

        extract_build_args( view , true );
    }

    public function extract_build_args( view:View = None , force_panel = false ) {

        if (view == null) {
            view = Sublime.active_window().active_view();
        }



        var folders = _get_folders(view);
        trace(folders);
        
        this.builds = _find_builds_in_folders(folders);
        
        var num_builds = builds.length;

        var view_build_id:Int = view.settings().get("haxe-current-build-id");
        trace("view_build_id:" + Std.string(view_build_id));

        if (view_build_id != None && view_build_id < num_builds && !force_panel) 
        {
            _set_current_build( view , view_build_id );
        }
        else if (num_builds == 1) 
        {
            if (force_panel) 
            {
                Sublime.status_message("There is only one build");
            }
            _set_current_build( view , int(0) );
        }
        else if (num_builds == 0 && force_panel) 
        {
            Sublime.status_message("No build files found (e.g. hxml, nmml, xml)");
            _create_new_hxml(view, folders[0]);
        }
        else if (num_builds > 1 && force_panel) 
        {
            _show_build_selection_panel(view);
        }
        else 
        {
            _set_current_build( view , 0 );
        }
    }

    public function has_build () {
        return current_build != null;
    }

    public function check_build(view:View) {
        _build(view, "check");
    }

    public function just_build(view:View) {
        _build(view, "build");
    }
        
    public function run_build( view:View ) {
        _build(view, "run");
    }

    public function _update_compiler_info () {
        var info = _collect_compiler_info(haxe_exec(), project_path);

        var bundle = info._1, 
            ver = info._2, 
            std_paths = info._3;
        //assume it's supported if no version available
        server_mode = ver == null || ver >= 209;

        std_bundle = bundle;
        std_paths = std_paths;
        //self.std_packages = packs
        //self.std_classes = ["Void","String", "Float", "Int", "UInt", "Bool", "Dynamic", "Iterator", "Iterable", "ArrayAccess"]
        //self.std_classes.extend(classes)
    }

    


    // TODO rewrite this function and make it understandable
    
    public function _find_builds_in_folders(folders:Array<String>):Array<Build> {
        var builds = [];
        for (f in folders) {
            builds = builds.concat(Builds.find_hxml_projects(this, f));
            builds = builds.concat(Builds.find_nme_projects(this, f));
            builds = builds.concat(Builds.find_openfl_projects(this, f));
        }
        return builds;
    }

    public function _get_view_file_name (view:View) {
        if (view == null) 
        {
            view = sublime.active_window().active_view();
        }
        return view.file_name();
    }

    public function _get_current_window (view:View) {
        return get_window(view);
    }

    public function _get_folders (view:View) {
        var win = _get_current_window(view);
        var folders = win.folders();
        return folders;
    }

    


    public function _create_new_hxml (self, view, folder) {
        win = sublime.active_window();
        f = os.path.join(folder,"build.hxml");

        self.current_build = null;
        self.get_build(view);
        self.current_build.hxml = f;

        //for whatever reason generate_build doesn't work without transient
        win.open_file(f,sublime.TRANSIENT);

        self._set_current_build( view , int(0) );
    }

    public function _show_build_selection_panel(self, view) {
        
        buildsView = [for (b in builds) Tup2.create(b.to_string(), os.path.basename(b.build_file))];

        
        self.selecting_build = true;
        sublime.status_message("Please select your build");
        
        function on_selected (i) {
            self.selecting_build = false;
            self._set_current_build(view, i);
        }

        win = sublime.active_window();
        win.show_quick_panel( buildsView , on_selected  , sublime.MONOSPACE_FONT );
    }

    public function _set_current_build( self, view , id ) {
        
        log( "_set_current_build");
        
        if (id < 0 || id >= self.builds.length) {
            id = 0;
        }
        
        if (self.builds.length > 0) {
            view.settings().set("haxe-current-build-id", id);
            self.current_build = self.builds[id];
            self.current_build.set_std_bundle(self.std_bundle);

            view.set_status("haxe-build",self.current_build.to_string());
            //hxpanel.default_panel().writeln( "build selected: " + self.current_build.to_string() )
        }
        else {
            view.set_status("haxe-build","No build found/selected");
            //hxpanel.default_panel().writeln( "No build found/selected" )
        }
            
    }
    
    public function _build(self, view, type = "run") {

        if (view == null) {
            view = sublime.active_window().active_view();
        }

        var win = view.window();

        var env = _haxe_build_env(project_dir("."));
        
        if (has_build()) {
            build = get_original_build(view);
        }
        else {
            extract_build_args(view);
            build = get_original_build(view);
        }

        if (type == "run") { // build and run
            r = build.prepare_run_cmd(self, self.is_server_mode_for_builds(), view);
        }
        else if (type == "build") { // just build
            r  = build.prepare_build_cmd(self, self.is_server_mode_for_builds(), view);
        }
        else { // only check for errors
            r = build.prepare_check_cmd(self, self.is_server_mode(), view);
        }
        var cmd = r._1;
        var build_folder = r._2;
        
        
        escaped_cmd = build.escape_cmd(cmd);


        hxpanel.default_panel().writeln("running: " + " ".join(escaped_cmd));


        
        win.run_command("haxe_exec", {
            cmd: cmd,
            is_check_run : type == "check",
            working_dir: build_folder,
            file_regex : haxe_file_regex,
            env : env
        });

    }

    public function clear_build() {
        current_build = null;
        completion_context.clear_completion();
    }

    public function destroy () {
        server.stop();
    }


    // TODO rewrite this function and make it understandable
    public function _create_default_build (view) {
        var fn = view.file_name();

        var src_dir = os.path.dirname( fn );

        var src = view.substr(sublime.Region(0, view.size()));
    
        var build = hxbuild.HxmlBuild(null, null);
        build.target = "js";

        var folder = Path.dirname(fn);
        var folders = view.window().folders();
        for (f in folders) {
            if (Lambda.has(fn, f)) {
                folder = f;
            }
        }

        var pack = [];
        for (ps in hxsrctools.package_line.findall( src )) {
            if (ps == "") continue;
                
            pack = ps.split(".");
            var packrev = pack.copy();
            packrev.reverse();
            for (p in packrev) {
                var spl = os.path.split( src_dir );
                if( spl[1] == p ) {
                    src_dir = spl[0];
                }
            }
        }

        var cl = os.path.basename(fn);
        
        cl = cl.substring(0, cl.rfind("."));

        var main = pack.substr(0);
        main.push( cl );
        build.main = ".".join( main );

        build.output = os.path.join(folder,build.main.lower() + ".js");

        build.args.push( Tup2.create("-cp" , src_dir) );

        build.args.push( Tup2.create("-js" , build.output ) );

        build.hxml = Path.join( src_dir , "build.hxml");
        return build;
    }

    public function get_original_build( view:View ) {
        
        if (current_build == null && view.score_selector(0,"source.haxe.2") > 0) {
            this.current_build = this._create_default_build(view);
        }
           
        return this.current_build;
    }


    public function get_build( view:View ) {
        return get_original_build(view).copy();
    }


    // STATIC SECTION

    static function _haxe_build_env (project_dir:String) {
        
        lib_path = hxsettings.haxe_library_path();
        haxe_inst_path = hxsettings.haxe_inst_path();
        neko_inst_path = hxsettings.neko_inst_path();


        var env = os.environ.copy();

        var env_path = os.environ.copy()["PATH"];
        
        

        paths = [];

        function do_encode(s) {
            return s;
        }
        var path = null;
        if (lib_path != null) 
        {

            if (pathtools.is_abs_path(lib_path)) {
                path = lib_path;
            } else {
                path = os.path.normpath(os.path.join(project_dir, lib_path));
            }

            env.set("HAXE_LIBRARY_PATH", do_encode(os.sep.join(path.split("/"))));
            env.set("HAXE_STD_PATH", do_encode(os.sep.join(path.split("/"))));
        }
        

        if (haxe_inst_path != null) {
            if (pathtools.is_abs_path(haxe_inst_path)) {
                path = haxe_inst_path;
            } else {
                path = os.path.normpath(os.path.join(project_dir, haxe_inst_path));
            }
            
            env.set("HAXEPATH", do_encode(os.sep.join(path.split("/"))));
            paths.push(do_encode(os.sep.join(path.split("/"))));
        }

        if (neko_inst_path != null) {
            path = os.path.normpath(os.path.join(project_dir, neko_inst_path));
            env.set("NEKO_INSTPATH", do_encode(os.sep.join(path.split("/"))));
            paths.append(do_encode(os.sep.join(path.split("/"))));
        }

        
        if (paths.length > 0) {
            env.set("PATH", paths.join(Os.pathsep) + os.pathsep + env_path);
        }

        
        trace(Std.string(env));
        return env;
    }


    static function _get_compiler_info_env (project_path:String) {

        return _haxe_build_env(project_path);
    }


    static function _collect_compiler_info (haxe_exec:String, project_path:String) {
        env = _get_compiler_info_env(project_path);
        cmd = haxe_exec;

        cmd = cmd.concat(["-main", "Nothing", "-v", "--no-output"]);

        
        var r = hxexecute.run_cmd( cmd, env=env );
        var out = r._1;
        var err = r._2;


        var std_classpaths = _extract_std_classpaths(out);
        
        var bundle = _collect_std_classes_and_packs(std_classpaths);
                
        var ver = _extract_haxe_version(out);
        
        return Tup3.create(bundle, ver, std_classpaths);
    }

    static function _extract_haxe_version (out:String) {
        var ver = Re.search( _haxe_version , out );
        return if (ver != null) Std.int(ver.group(1)) else null;
    }


    static function _remove_trailing_path_sep(path:String) {
        if (path.length > 1) {
            var last_pos = path.length-1;
            var last_char = path[last_pos];
            if (last_char == "/" ||  last_char == "\\" || last_char == os.path.sep) {
                path = path.substring(0,last_pos);
            }
        }
        return path;
    }

    static function _is_valid_classpath(path:String) {
        return path.length > 1 && os.path.exists(path) && os.path.isdir(path);
    }

    static function _extract_std_classpaths (out:String) {
        m = _classpath_line.match(out);
            
        var std_classpaths = [];

        var all_paths = m.group(1).split(";");
        var ignored_paths = [".","./"];

        var std_paths = if (m != null) set(all_paths) - set(ignored_paths) else [];
        
        for (p in std_paths) {
            var p = os.path.normpath(p);
            
            p = _remove_trailing_path_sep(p);

            if (_is_valid_classpath(p)) {
                std_classpaths.append(p);
            }
        }

        return std_classpaths;
    }


    static function _collect_std_classes_and_packs(std_cps:String) {
        var bundle = hxsrctools.empty_type_bundle();
        for (p in std_cps) {
            bundle1 = hxtypes.extract_types( p, [], [], 0, [], false );
            bundle = bundle.merge(bundle1);
        }
        return bundle;
    }

    private static var _classpath_line = Re.compile("Classpath : (.*)");
    private static var _haxe_version = Re.compile("haxe_([0-9]{3})", Re.M);
}

/*
# -*- coding: utf-8 -*-
import sublime
import os
import re
import sys

from haxe.plugin import is_st3, is_st2

from haxe import build as hxbuild
from haxe import panel as hxpanel
from haxe import types as hxtypes
from haxe import settings as hxsettings
from haxe import execute as hxexecute
from haxe import haxelib

from haxe.tools import viewtools
from haxe.tools import pathtools
from haxe.tools import hxsrctools

from haxe.compiler import server as hxserver

from haxe.log import log

from haxe.project.tools import get_window, haxe_file_regex

from haxe.project.completion_state import ProjectCompletionState










*/