package hxsublime;

import hxsublime.build.Build;
import hxsublime.Exceptions.ExtractBuildPathException;
import hxsublime.Exceptions.GetRelativePathException;
import hxsublime.tools.PathTools;
import python.lib.Codecs;
import python.lib.Os;
import python.lib.os.Path;
import python.lib.Tempfile;
import python.Tuple;


class Temp {

	public static function getTempPathId(build:Build)
	{
		var path = build.getBuildFolder();

		if (path == null)
		{
			throw new ExtractBuildPathException(build);
		}

		var path1 = path.split(Os.sep).join("_").split(":").join("_");

		var temp_path = Path.join(Tempfile.gettempdir(), "haxe_sublime_hx" + path1 + "_");

		return temp_path;
	}

	public static function createTempPath(build:Build)
	{
		var temp_path = getTempPathId(build);


		PathTools.removeDir(temp_path);
		Os.makedirs(temp_path);

		return temp_path;
	}

	public static function createFile(temp_path:String, build:Build, orig_file:String, content:String)
	{

		var relative = build.getRelativePath(orig_file);
		trace(relative);
		trace(orig_file);
		trace("relative:" + Std.string(relative));
		if (relative == null)
		{
			throw new GetRelativePathException(build, orig_file);
		}

		var new_file = Path.join(temp_path, relative);
		var new_file_dir = Path.dirname(new_file);
		if (!Path.exists(new_file_dir))
		{
			Os.makedirs(new_file_dir);
		}

		var f = Codecs.open( new_file , "wb" , "utf-8" , "ignore" );
		f.write( content );

		(f:Dynamic).close();
		trace(new_file);
		return new_file;
	}

	public static function createTempPathAndFile(build:Build, orig_file:String, content:String)
	{
		var temp_path = createTempPath(build);

		var temp_file = createFile(temp_path, build, orig_file, content);
		return Tuple2.make(temp_path, temp_file);
	}

	public static function removePath (temp_path:String)
	{
		if (temp_path != null)
		{
			PathTools.removeDir(temp_path);
		}

	}

}
