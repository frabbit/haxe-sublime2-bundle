package hxsublime.build;

import hxsublime.project.Project;
import python.lib.Glob;
import python.lib.io.StringIO;
import python.lib.os.Path;
import sublime.Sublime;

using StringTools;
using python.lib.ArrayTools;

class Tools {

	static var _extract_tag = Re.compile("<([a-z0-9_-]+).*?\\s(name|main|title|file)=\"([ a-z0-9_./-]+)\"", re.I);

	// TODO refactor this method into smaller managable chunks
	public static function _hxml_buffer_to_builds(project:Project, hxml_buffer:StringIO, folder:String, build_path:String, build_file:String = null, hxml:String = null)
	{
		var builds = [];

		var current_build = new HxmlBuild(hxml, build_file);
		
		// print("build file exists")
		var f = hxml_buffer;
		while (true)
		{ 
			var l = f.readline() 
			if (l == null) {
				break;
			}

			if (l == "") {
				continue;
			}

			l = l.strip();

			if (l.startsWith("#build-name=")) 
			{
				current_build.name = l.substr(12);
				continue;
			}
			if (l.startsWith("#"))
			{
				continue;
			}



			if (l.startsWith("--next")) 
			{
				if (current_build.classpaths.length == 0) 
				{
					trace("no classpaths");
					current_build.add_classpath( build_path );
				}
					//current_build.args.push( ("-cp" , build_path ) )
				//current_build.get_types()
				builds.push( current_build );
				current_build = new HxmlBuild(hxml, build_file);
				continue;
			}
				
			
			
			if (l.endswith(".hxml"))
			{
				
				trace("found ref of hxml file:" + l);
				path = Path.dirname(hxml);
				sub_builds = _hxml_to_builds(project, path + os.sep + l, folder);
				if (len(sub_builds) == 1)
				{
					b = sub_builds[0];
					current_build.merge(b);
				}
			}

			if (l.startsWith("-main") )
			{
				spl = l.split(" ");
				if (len( spl ) == 2 )
				{
					current_build.main = spl[1];
				}
				else {
					Sublime.status_message( "Invalid build.hxml : no Main class" );
				}
			}
			
			if (l.startsWith("-lib") )
			{
				var spl = l.split(" ")
				if (len( spl ) == 2 )
				{
					var lib = project.haxelib_manager.get( spl[1] );
					if (lib != null)
					{
						trace("lib to build:" + str(lib));
						current_build.add_lib( lib );
					}
					else {

						current_build.add_arg( Tup2.create("-lib", spl[1] ) )
						//from haxe import panel
						panel.default_panel().writeln("Error: haxelib library " + str(spl[1]) + " is not installed" )
					}
				}
				else {
					sublime.status_message( "Invalid build.hxml : lib not found" )
				}
			}

			if (l.startsWith("-cmd") )
			{
				var spl = l.split(" ");
				current_build.add_arg( Tup2.create( "-cmd" , spl.substr(1).join(" ") ) );
			}
			
			if (l.startsWith("--macro"))
			{
				var spl = l.split(" ");
				current_build.add_arg( Tup2.create( "--macro" , spl.substr(1).join(" ")  ) );
			}

			if (l.startsWith("-D"))
			{
				var x = l.split(" ");
				var tup = Tup2.create(x[0], x[1]);
				current_build.add_arg( tup );
				current_build.add_define(tup._2);
				continue
			}

			for (flag in [ "swf-version" , "swf-header", 
						"debug" , "-no-traces" , "-flash-use-stage" , "-gen-hx-classes" , 
						"-remap" , "-no-inline" , "-no-opt" , "-php-prefix" , 
						"-js-namespace" , "-interp" , "-dead-code-elimination" , 
						"-php-front" , "-php-lib", "dce" , "-js-modern", "-times" ])
			{
				if (l.startsWith( "-"+flag ) )
				{	
					var x = l.split(" ");
					current_build.add_arg( Tup2.create(x[0], x[1]) );
					
					break;
				}
			}
			
			for (flag in [ "resource" , "xml" , "x" , "swf-lib" , "java-lib" ])
			{
				if (l.startsWith( "-"+flag ) )
				{
					var spl = l.split(" ")
					var outp = Path.join( folder , spl.substr(1).join(" ") )
					current_build.add_arg( Tup2.create("-"+flag, outp) )
					if (flag == "x")
					{
						current_build.target = "neko";
					}
					break
				}
			}

			for (flag in config.targets)
			{
				if (l.startsWith( "-" + flag + " " ) )
				{
					var spl = l.split(" ");
					spl.shift();
					var outp = spl.join(" ");
					current_build.add_arg( Tup2.create("-"+flag, outp) );
					
					current_build.target = flag;
					current_build.output = outp;
					break;
				}
			}

			if (l.startsWith("-cp "))
			{
				var cp = l.split(" ")
				cp.shift();
				var classpath = cp.join( " " );
				
				abs_classpath = pathtools.join_norm( build_path , classpath );
				current_build.add_classpath( abs_classpath );
				//current_build.add_arg( ("-cp" , abs_classpath ) )
			}
		}

		if (current_build.classpaths.length == 0)
		{
			trace("no classpaths");
			current_build.add_classpath( build_path );
			//current_build.args.push( ("-cp" , build_path ) )
		}

		//current_build.get_types()
		builds.push( current_build );

		return builds;
	}
	
	
	public static function _find_build_files_in_folder(folder:String, extension:String)
	{
		if (!Path.isdir(folder) )
		{
			return [];
		}
			
		var files = Glob.glob( Path.join( folder , "*."+extension ) ).map(function (x) return Tup2.create(x, folder));
		
		for (dir in Os.listdir(folder)) 
		{
			var f = Path.join(folder, dir);
			var x = Glob.glob( Path.join( f , "*."+extension ) ).map(function (x) return Tup2.create(x, f));
			files.extend( x );
		}
		return files;
	}
	
	public static function _hxml_to_builds (project, hxml, folder)
	{
		var build_path = Path.dirname(hxml);
		var hxml_buffer = codecs.open( hxml , "r+" , "utf-8" , "ignore" )
		return _hxml_buffer_to_builds(project, hxml_buffer, folder, build_path, hxml, hxml);
	}
	
	

	public static function _find_nme_project_title(nmml_file)
	{
		var f = codecs.open( nmml_file , "r+", "utf-8" , "ignore" );
		var title = null;
		while (true) 
		{
			var l = f.readline()
			if (l == null) 
			{
				break;
			}
			var m = _extract_tag.search(l);
			if (m != null) 
			{
				var tag = m.group(1);
				
				if (tag == "meta" || tag == "app") 
				{
					var mFile = re.search("\\b(file|title)=\"([ a-z0-9_-]+)\"", l, re.I);
					if (mFile != null) 
					{
						title = mFile.group(2);
						break;
					}
				}
			}
		}

		f.close();
		return title;
	}
	
	public static function create_haxe_build_from_nmml (project:Project, target, nmml, display_cmd:Array<String>)
	{

		var cmd = display_cmd.copy();
		cmd.push(nmml);
		cmd.push(target.plattform);
		cmd.extend(target.args);

		nmml_dir = Path.dirname(nmml);

		out, err = run_cmd( cmd, cwd=nmml_dir )

		return _hxml_buffer_to_builds(project, new StringIO(out), nmml_dir, nmml_dir, nmml, null)[0]
	}
	
	public static function find_hxml_projects( project, folder ) 
	{
		
		var builds = [];
		var found = _find_build_files_in_folder(folder, "hxml");
		for (build in found) {
			
			var hxml_file = build._1;
			var hxml_folder = build._2;
			
			var b = _hxml_to_builds(project, hxml_file, hxml_folder);
			trace("builds in hxml " + Std.string(hxml_file) + ":" + Std.string(b.length));
			builds.extend(b);
		}

		return builds;
	}
	
	public static function find_nme_projects( project:Project, folder:String ) 
	{
		var found = _find_build_files_in_folder(folder, "nmml");
		var builds = [];
		for (build in found) 
		{
			nmml_file = build._1;
			title = _find_nme_project_title(nmml_file)
			if (title != null) 
			{
				for (t in config.nme_targets) 
				{
					builds.push(new NmeBuild(project, title, nmml_file, t));
				}
			}
		}
		return builds
	}
	
	public static function find_openfl_projects( project:Project, folder:String ) 
	{

		var found = _find_build_files_in_folder(folder, "xml");
		var builds = [];
		for (build in found) 
		{
			var openfl_xml = build._1;
			title = _find_nme_project_title(openfl_xml);
			if (title != null) 
			{
				for (t in config.openfl_targets)
				{
					builds.push(new OpenFlBuild(project, title, openfl_xml, t))
				}
			}
		}


		return builds
}

/*
// -*- coding: utf-8 -*-
import os
import sys
import re
import glob
import codecs
import sublime

from haxe import config

from haxe.tools import pathtools

from haxe.execute import run_cmd
from haxe.trace import trace

from haxe.tools.stringtools import encode_utf8, to_unicode



from haxe.build.hxmlbuild import HxmlBuild
from haxe.build.nmebuild import NmeBuild
from haxe.build.openflbuild import OpenFlBuild

try:
	from io import StringIO
except:
	from StringIO import StringIO


*/