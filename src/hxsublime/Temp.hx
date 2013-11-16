package hxsublime;

import hxsublime.build.Build;
import hxsublime.Exceptions.ExtractBuildPathException;
import hxsublime.Exceptions.GetRelativePathException;
import hxsublime.tools.PathTools;
import python.lib.Codecs;
import python.lib.Os;
import python.lib.os.Path;
import python.lib.Tempfile;
import python.lib.Types.Tup2;


class Temp {

	public static function get_temp_path_id(build:Build) {

		
		var path = build.get_build_folder();

		if (path == null) {
			throw new ExtractBuildPathException(build);
		}

		var path1 = path.split(Os.sep).join("_").split(":").join("_");

		var temp_path = Path.join(Tempfile.gettempdir(), "haxe_sublime_hx" + path1 + "_");

		return temp_path;
	}

	public static function create_temp_path(build:Build) {

		var temp_path = get_temp_path_id(build);
		
		
		PathTools.removeDir(temp_path);
		Os.makedirs(temp_path);

		return temp_path;
	}

	public static function create_file(temp_path:String, build:Build, orig_file:String, content:String) 
	{
		
		var relative = build.get_relative_path(orig_file);
		trace(relative);
		trace(orig_file);
		trace("relative:" + Std.string(relative));
		if (relative == null) {
			throw new GetRelativePathException(build, orig_file);
		}

		var new_file = Path.join(temp_path, relative);
		var new_file_dir = Path.dirname(new_file);
		if (!Path.exists(new_file_dir)) {
			Os.makedirs(new_file_dir);
		}
		
		var f = Codecs.open( new_file , "wb" , "utf-8" , "ignore" );
		f.write( content );
		f.close();
		trace(new_file);
		return new_file;
	}

	public static function create_temp_path_and_file(build:Build, orig_file:String, content:String) {
		var temp_path = create_temp_path(build);
			
		var temp_file = create_file(temp_path, build, orig_file, content);
		return Tup2.create(temp_path, temp_file);
	}

	public static function remove_path (temp_path:String) {
		if (temp_path != null) {
			PathTools.removeDir(temp_path);
		}

	}

}

/*
import os

import codecs
import tempfile

from haxe.log import log
from haxe.tools import pathtools

from haxe import exceptions

from haxe.tools.stringtools import encode_utf8, st2_to_unicode

*/