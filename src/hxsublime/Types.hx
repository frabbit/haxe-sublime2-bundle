package hxsublime;

import haxe.ds.StringMap;
import hxsublime.Config;
import hxsublime.Haxelib.HaxeLibLibrary;
import hxsublime.panel.Base.Panels;
import hxsublime.tools.HxSrcTools;
import python.lib.Codecs;
import python.lib.Glob;
import python.lib.Os;
import python.lib.Re;

import python.lib.os.Path;
import python.lib.Types.Tup2;


class Types 
{
	public static function find_types (classpaths, libs:Array<HaxeLibLibrary>, base_path, filtered_classes = null, filtered_packages = null, include_private_types = true) 
	{

		var bundle = HxSrcTools.empty_type_bundle();

		var cp = [];
		cp = cp.concat( classpaths );

		for (lib in libs) {
			if (lib != null) {
				cp.push( lib.path );
			}
		}

		for (path in cp) 
		{
			var p = Path.join( base_path, path );

			if (Path.exists(p)) {
				var b = extract_types( p, filtered_classes, filtered_packages, 0, [], include_private_types );
				bundle = bundle.merge(b);
			}
			else {
				Panels.default_panel().writeln("Error: The classpath " + p + " does not exist, in case of nme or openfl you need have to build (CTRL + ENTER) the project first (the build creates these paths)");
			}
		}

		return bundle;
	}

	public static var valid_package = Re.compile("^[_a-z][a-zA-Z0-9_]*$");

	public static function is_valid_package (pack:String) 
	{
		return valid_package.match(pack) != null && pack != "_std";
	}

	public static function extract_types( path:String , filtered_classes = null, filtered_packages = null, depth = 0, pack:Array<String> = null, include_private_types = true)  
	{
		
		if (pack == null) pack = [];
		if (filtered_classes == null) 
		{
			filtered_classes = [];
		}
		if (filtered_packages == null) 
		{
			filtered_packages = [];
		}
		
		var bundle = HxSrcTools.empty_type_bundle();
		
		
		for (fullpath in Glob.glob( Path.join(path,"*.hx") )) 
		{ 
			
			var f = Path.basename(fullpath);

			var r = Path.splitext( f );
			var cl = r._1;
			var ext = r._2;
								
			if (!Lambda.has(filtered_classes, cl)) 
			{

				var file = Path.join( path , f );
				if (Path.exists(file)) 
				{
					
					var module_bundle = extract_types_from_file(file, cl, include_private_types);
					
					bundle = bundle.merge(module_bundle);


					
				}
			}
		}
				
					
		
		for (f in Os.listdir( path )) 
		{
		
			if (is_valid_package(f)) 
			{
				var r = Path.splitext( f );
				var cl = r._1;
				var ext = r._2;
				
				var cur_pack_base = if (pack.length > 0) pack.join(".") + "." else "";

				var cur_pack = cur_pack_base + f;

				if (Path.isdir( Path.join( path , f ) ) && !Lambda.has(filtered_packages, cur_pack) && !Config.ignored_packages.exists(cur_pack)) 
				{
					
					var next_pack = pack.copy();
					next_pack.push(f);
					
					var sub_bundle = extract_types( Path.join( path , f ) , filtered_classes, filtered_packages, depth + 1, next_pack, include_private_types );
					bundle = bundle.merge(sub_bundle);
				}
			}
		}
		
		return bundle;
	}

	public static var file_type_cache = new StringMap<Tup2<Float, HaxeTypeBundle>>();



	public static function extract_types_from_file (file:String, module_name:String = null, include_private_types = true) 
	{
		//trace("extract types from file");
		var mtime = Path.getmtime(file);
		if (file_type_cache.exists(file) && file_type_cache.get(file)._1 == mtime) 
		{
			return file_type_cache.get(file)._2;
		}

		// use cache based on last file modification

		if (module_name == null) 
		{
			module_name = Path.splitext( Path.basename(file) )._1;
		}

		var s = Codecs.open( file , "r" , "utf-8" , "ignore" );
		var src_with_comments = s.read();

		var src = HxSrcTools.strip_comments(src_with_comments);
		


		var bundle = HxSrcTools.get_types_from_src(src, module_name, file, src_with_comments);

		file_type_cache.set(file, Tup2.create(mtime, bundle));

		

		return bundle;
	}
}

/*

import os, codecs, glob, re

from haxe import config as hxconfig
from haxe import panel
from haxe.tools import hxsrctools
from haxe.log import log




*/