package hxsublime;

import python.lib.Re;

import python.lib.os.Path;


class Types 
{
	public static function find_types (classpaths, libs, base_path, filtered_classes = null, filtered_packages = null, include_private_types = true) 
	{

		var bundle = hxsrctools.empty_type_bundle();

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
				panel.default_panel().writeln("Error: The classpath " + p + " does not exist, in case of nme or openfl you need have to build (CTRL + ENTER) the project first (the build creates these paths)");
			}
		}

		return bundle;
	}

	public static var valid_package = Re.compile("^[_a-z][a-zA-Z0-9_]*$");

	public static function is_valid_package (pack:String) 
	{
		return valid_package.match(pack) && pack != "_std";
	}

	public static function extract_types( path:String , filtered_classes = null, filtered_packages = null, depth = 0, pack = [], include_private_types = true)  
	{
		if (filtered_classes == null) 
		{
			filtered_classes = [];
		}
		if (filtered_packages == null) 
		{
			filtered_packages = [];
		}
		
		var bundle = hxsrctools.empty_type_bundle();
		
		for (fullpath in glob.glob( Path.join(path,"*.hx") )) 
		{ 
			f = os.path.basename(fullpath);

			var r = Os.path.splitext( f );
			var cl = r._1;
			var ext = r._2;
								
			if (!Lambda.has(filtered_classes, cl)) 
			{
				var file = os.path.join( path , f );
				if (Path.exists(file)) 
				{
					module_bundle = extract_types_from_file(file, cl, include_private_types);
					bundle = bundle.merge(module_bundle);
				}
			}
		}
				
					
		
		for (f in os.listdir( path )) 
		{
			if (is_valid_package(f)) 
			{
				var r = Os.path.splitext( f );
				var cl = r._1;
				var ext = r._2;
				
				var cur_pack_base = if (pack.length > 0) pack.join(".") + "." else "";

				var cur_pack = cur_pack_base + f;

				if (os.path.isdir( os.path.join( path , f ) ) && !Lambda.has(filtered_packages, cur_pack) && !Lambda.has(hxconfig.ignored_packages, cur_pack)) 
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

	public static var file_type_cache = new StringMap();



	public static function extract_types_from_file (file:String, module_name:String = null, include_private_types = true) 
	{
		var mtime = Path.getmtime(file);
		if (file_type_cache.exists(file) && file_type_cache.get(file)._1 == mtime) 
		{
			return file_type_cache.get(file)._2;
		}

		// use cache based on last file modification

		if (module_name == null) 
		{
			module_name = Path.splitext( os.path.basename(file) )._1;
		}

		s = codecs.open( file , "r" , "utf-8" , "ignore" );
		src_with_comments = s.read();
		src = hxsrctools.strip_comments(src_with_comments);
		

		var bundle = hxsrctools.get_types_from_src(src, module_name, file, src_with_comments);

		file_type_cache.set(file, Tup2.create(mtime, bundle));

		return bundle
	}
}

/*

import os, codecs, glob, re

from haxe import config as hxconfig
from haxe import panel
from haxe.tools import hxsrctools
from haxe.log import log




*/