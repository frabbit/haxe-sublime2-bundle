package hxsublime;
import hxsublime.build.Build;
import python.Exceptions;

class ExtractBuildPathException extends Exception
{
	public function  new(build:Build)
	{
		super("Cannot ExtractBuildPath from build " + Std.string(build));
	}
}

class GetRelativePathException extends Exception
{
	public function  new(build:Build, file:String)
	{
		super("Cannot get the relative path of " + Std.string(file) + " for build " + Std.string(build));
	}
}


class CreateTempFileOrFolderException extends Exception
{
	public function  new(build:Build, file_or_folder:String)
	{
		super("Cannot create temp file or folder (" + Std.string(file_or_folder) + ") from build (" + Std.string(build) + ")");
	}
}
