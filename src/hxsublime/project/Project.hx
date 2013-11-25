package hxsublime.project;

import hxsublime.build.Build;
import hxsublime.build.HxmlBuild;
import hxsublime.compiler.Server;
import hxsublime.Haxelib.HaxeLibManager;
import hxsublime.panel.Base.Panels;
import hxsublime.project.CompletionState.ProjectCompletionState;
import hxsublime.Settings;
import hxsublime.tools.HxSrcTools;
import hxsublime.tools.HxSrcTools.HaxeTypeBundle;
import hxsublime.tools.PathTools;
import hxsublime.tools.ViewTools;
import python.lib.Os;
import python.lib.os.Path;
import python.lib.Re;
import python.lib.Types.Dict;
import python.lib.Types.Set;
import python.lib.Types.Tup2;
import python.lib.Types.Tup3;
import sublime.Edit;
import sublime.Region;
import sublime.Sublime;
import sublime.View;
import hxsublime.tools.HxSrcTools.Regex in HxRegex;
using python.lib.ArrayTools;
//using Settings;


class Project 
{

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
    public var std_bundle:HaxeTypeBundle;
    public var std_paths:Array<String>;
    public var server_mode:Bool;


    public function new (id, file:String, win_id, server_port:Int) {
        
        this.completion_context = new ProjectCompletionState();
        this._haxelib_manager = new HaxeLibManager(this);
        this.current_build = null;
        this.selecting_build = false;
        this.builds = [];
        this.win_id = win_id;
        this.server = new Server(server_port);
        this.project_file = file;
        this.project_id = id;
        if (this.project_file != null) {
            this.project_path = Path.normpath(Path.dirname(this.project_file));
        }
        else {
            this.project_path = null;
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

    public function haxelib_exec (view:View = null) {
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

    
    public function haxe_env (view:View = null) {
        return _haxe_build_env(project_dir("."));
    }
    
    
    public function start_server(view:View) {
        var cwd = project_dir(".");
        var haxe_exec = haxe_exec(view)[0];
        
        var env = haxe_env();
        
        server.start(haxe_exec, cwd, env);
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
        
        var is_hxml_build = function () return Std.is(this.current_build, HxmlBuild);

        if (current_build != null && is_hxml_build() && fn == current_build.build_file() && view.size() == 0) {
            function run_edit(v:View, e:Edit) {
                var hxml_src = current_build.make_hxml();
                v.insert(e,0,hxml_src);
            }

            ViewTools.asyncEdit(view, run_edit);
        }
    }

    public function select_build( view:View ) 
    {
        var scopes = view.scope_name(view.sel()[0].end()).split(" ");
        
        if (Lambda.has(scopes, 'source.hxml')) {
            view.run_command("save");
        }

        extract_build_args( view , true );
    }

    public function extract_build_args( view:View = null , force_panel = false ) {

        if (view == null) {
            view = Sublime.active_window().active_view();
        }



        var folders = _get_folders(view);
        
        
        this.builds = _find_builds_in_folders(folders);
        
        
        var num_builds = builds.length;

        var view_build_id:Int = view.settings().get("haxe-current-build-id");
        

        if (view_build_id != null && view_build_id < num_builds && !force_panel) 
        {
            _set_current_build( view , view_build_id );
        }
        else if (num_builds == 1) 
        {
            if (force_panel) 
            {
                Sublime.status_message("There is only one build");
            }
            _set_current_build( view , 0 );
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
        this.server_mode = ver == null || ver >= 209;

        this.std_bundle = bundle;
        this.std_paths = std_paths;
        //this.std_packages = packs
        //this.std_classes = ["Void","String", "Float", "Int", "UInt", "Bool", "Dynamic", "Iterator", "Iterable", "ArrayAccess"]
        //this.std_classes.extend(classes)
    }

    


    // TODO rewrite this function and make it understandable
    
    public function _find_builds_in_folders(folders:Array<String>):Array<Build> {
        var builds:Array<Build> = [];
        trace("find builds start");
        for (f in folders) 
        {
            builds.extend(hxsublime.build.Tools.find_hxml_projects(this, f).map(function (x):Build return x));
            builds.extend(hxsublime.build.Tools.find_nme_projects(this, f).map(function (x):Build return x));
            builds.extend(hxsublime.build.Tools.find_openfl_projects(this, f).map(function (x):Build return x));
        }
        
        trace("find builds end");
        return builds;
    }

    public function _get_view_file_name (view:View) {
        if (view == null) 
        {
            view = Sublime.active_window().active_view();
        }
        return view.file_name();
    }

    public function _get_current_window (view:View) {
        return hxsublime.project.Tools.get_window(view);
    }

    public function _get_folders (view:View) {
        var win = _get_current_window(view);
        var folders = win.folders();
        return folders;
    }

    


    public function _create_new_hxml (view:View, folder:String) {
        var win = Sublime.active_window();
        var f = Path.join(folder,"build.hxml");

        this.current_build = null;
        this.get_build(view);
        this.current_build.setHxml(f);

        //for whatever reason generate_build doesn't work without transient
        win.open_file(f,Sublime.TRANSIENT);

        this._set_current_build( view , 0 );
    }

    public function _show_build_selection_panel(view:View) {
        
        var buildsView = [for (b in builds) [b.to_string(), Path.basename(b.build_file())]];

        
        this.selecting_build = true;
        Sublime.status_message("Please select your build");
        
        function on_selected (i:Int) {
            this.selecting_build = false;
            this._set_current_build(view, i);
        }

        var win = Sublime.active_window();
        
        win.show_quick_panel( buildsView , on_selected  , Sublime.MONOSPACE_FONT );
    }

    public function _set_current_build( view:View , id:Int ) {
        
        trace( "_set_current_build");
        
        if (id < 0 || id >= this.builds.length) {
            id = 0;
        }
        
        if (this.builds.length > 0) {
            view.settings().set("haxe-current-build-id", id);
            this.current_build = this.builds[id];
            this.current_build.set_std_bundle(this.std_bundle);

            view.set_status("haxe-build",this.current_build.to_string());
            //hxpanel.default_panel().writeln( "build selected: " + this.current_build.to_string() )
        }
        else {
            view.set_status("haxe-build","No build found/selected");
            //hxpanel.default_panel().writeln( "No build found/selected" )
        }
            
    }
    
    public function _build(view:View, type = "run") {

        if (view == null) {
            view = Sublime.active_window().active_view();
        }

        var win = view.window();

        var env = _haxe_build_env(project_dir("."));
        
        var build:Build = null;
        if (has_build()) {
            build = get_original_build(view);
        }
        else {
            extract_build_args(view);
            build = get_original_build(view);
        }

        var r = null;
        if (type == "run") { // build and run
            r = build.prepare_run_cmd(this, this.is_server_mode_for_builds(), view);
        }
        else if (type == "build") { // just build
            r  = build.prepare_build_cmd(this, this.is_server_mode_for_builds(), view);
        }
        else { // only check for errors
            r = build.prepare_check_cmd(this, this.is_server_mode(), view);
        }
        var cmd = r._1;
        var build_folder = r._2;
        
        
        var escaped_cmd = build.escape_cmd(cmd);


        Panels.default_panel().writeln("running: " + escaped_cmd.join(" "));


        
        win.run_command("hxsublime_commands__haxe_exec", Dict.fromObject({
            cmd: cmd,
            is_check_run : type == "check",
            working_dir: build_folder,
            file_regex : Tools.haxe_file_regex,
            env : env
        }));

    }

    public function clear_build() {
        current_build = null;
        completion_context.clear_completion();
    }

    public function destroy () {
        server.stop();
    }


    // TODO rewrite this function and make it understandable
    public function _create_default_build (view:View):Build {
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
        for (ps in HxRegex.package_line.findallString( src )) {
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

        build.add_arg( Tup2.create("-cp" , src_dir) );

        build.add_arg( Tup2.create("-js" , build.output ) );

        build.setHxml(Path.join( src_dir , "build.hxml"));
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

    static function _haxe_build_env (project_dir:String) 
    {
        
        var lib_path = Settings.haxe_library_path();
        var haxe_inst_path = Settings.haxe_inst_path();
        var neko_inst_path = Settings.neko_inst_path();


        var env = Os.environ.copy();

        var env_path = Os.environ.copy().get("PATH", "");
        
        

        var paths = [];

        function do_encode(s) {
            return s;
        }
        var path = null;
        if (lib_path != null) 
        {

            if (PathTools.is_abs_path(lib_path)) {
                path = lib_path;
            } else {
                path = Path.normpath(Path.join(project_dir, lib_path));
            }

            env.set("HAXE_LIBRARY_PATH", do_encode(path.split("/").join(Os.sep)));
            env.set("HAXE_STD_PATH", do_encode(path.split("/").join(Os.sep)));
        }
        

        if (haxe_inst_path != null) {
            if (PathTools.is_abs_path(haxe_inst_path)) {
                path = haxe_inst_path;
            } else {
                path = Path.normpath(Path.join(project_dir, haxe_inst_path));
            }
            
            env.set("HAXEPATH", do_encode(path.split("/").join(Os.sep)));
            paths.push(do_encode(path.split("/").join(Os.sep)));
        }

        if (neko_inst_path != null) 
        {
            path = Path.normpath(Path.join(project_dir, neko_inst_path));
            env.set("NEKO_INSTPATH", do_encode(path.split("/").join(Os.sep)));
            paths.append(do_encode(path.split("/").join(Os.sep)));
        }

        
        if (paths.length > 0) 
        {
            env.set("PATH", paths.join(Os.pathsep) + Os.pathsep + env_path);
        }

        
        //trace(Std.string(env));
        return env;
    }


    static function _get_compiler_info_env (project_path:String) {

        return _haxe_build_env(project_path);
    }


    static function _collect_compiler_info (haxe_exec:Array<String>, project_path:String) {
        var env = _get_compiler_info_env(project_path);
        var cmd = haxe_exec;

        cmd.extend(["-main", "Nothing", "-v", "--no-output"]);

        
        var r = Execute.run_cmd( cmd, null,null,env );
        //trace(r);
        //trace(r._1);
        //trace(r._2);
        var out = r._1;
        var err = r._2;


        var std_classpaths = _extract_std_classpaths(out);
        
        var bundle = _collect_std_classes_and_packs(std_classpaths);
                
        var ver = _extract_haxe_version(out);
        
        return Tup3.create(bundle, ver, std_classpaths);
    }

    static function _extract_haxe_version (out:String) {
        var ver = Re.search( _haxe_version , out );
        return if (ver != null) Std.parseInt(ver.group(1)) else null;
    }


    static function _remove_trailing_path_sep(path:String) {
        if (path.length > 1) {
            var last_pos = path.length-1;
            var last_char = path.charAt(last_pos);
            if (last_char == "/" ||  last_char == "\\" || last_char == Path.sep) {
                path = path.substring(0,last_pos);
            }
        }
        return path;
    }

    static function _is_valid_classpath(path:String) {
        return path.length > 1 && Path.exists(path) && Path.isdir(path);
    }

    static function _extract_std_classpaths (out:String) {
        var m = _classpath_line.match(out);
            
        var std_classpaths = [];

        //trace(out);

        var all_paths = m.group(1).split(";");
        var ignored_paths = [".","./"];

        var std_paths = if (m != null) new Set(all_paths).minus(new Set(ignored_paths)) else new Set();
        
        for (p in std_paths.iterator()) {
            var p = Path.normpath(p);
            
            p = _remove_trailing_path_sep(p);

            if (_is_valid_classpath(p)) {
                std_classpaths.append(p);
            }
        }

        return std_classpaths;
    }


    static function _collect_std_classes_and_packs(std_cps:Array<String>) {
        var bundle = HxSrcTools.empty_type_bundle();
        for (p in std_cps) {
            var bundle1 = hxsublime.Types.extract_types( p, [], [], 0, [], false );
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