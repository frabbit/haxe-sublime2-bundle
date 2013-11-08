


class Temp {

	public static function get_temp_path_id(build) {

		
		var path = build.get_build_folder();

		if (path == null) {
			throw ExtractBuildPathException(build);
		}

		var path1 = "_".join("_".join(path.split(os.sep)).split(":"));

		var temp_path = os.path.join(tempfile.gettempdir(), "haxe_sublime_hx" + path1 + "_");

		return temp_path;
	}

	public static function create_temp_path(build) {

		var temp_path = get_temp_path_id(build);
		
		
		pathtools.remove_dir(temp_path);
		Os.makedirs(temp_path);

		return temp_path
	}

	public static function create_file(temp_path:String, build:Build, orig_file:String, content:String) 
	{
		var orig_file = st2_to_unicode(orig_file);
		var relative = build.get_relative_path(orig_file);
		trace("relative:" + str(encode_utf8(relative)));
		if (relative == null) {
			throw exceptions.GetRelativePathException(build, orig_file);
		}

		var new_file = os.path.join(temp_path, relative);
		var new_file_dir = os.path.dirname(new_file);
		if (!os.path.exists(new_file_dir)) {
			os.makedirs(new_file_dir);
		}
		
		var f = codecs.open( new_file , "wb" , "utf-8" , "ignore" );
		f.write( content );
		f.close();
		return new_file;
	}

	public static function create_temp_path_and_file(build, orig_file:String, content:String) {
		var temp_path = create_temp_path(build);
			
		var temp_file = create_file(temp_path, build, orig_file, content);
		return Tup2.create(temp_path, temp_file);
	}

	public static function remove_path (temp_path:String) {
		if (temp_path != null) {
			pathtools.remove_dir(temp_path);
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