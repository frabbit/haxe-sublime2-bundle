package hxsublime;
import python.lib.Types.Exception;
class ExtractBuildPathException extends Exception {
	public function  new(build) {
		super("Cannot ExtractBuildPath from build " + Std.string(build))
	}
}

class GetRelativePathException extends Exception {
	public function  new(build, file) {
		super("Cannot get the relative path of " + Std.string(file) + " for build " + Std.string(build))
	}
}


class CreateTempFileOrFolderException extends Exception {
	public function  new(build, file_or_folder) {
		super("Cannot create temp file or folder (" + Std.string(file_or_folder) + ") from build (" + Std.string(build) + ")")
	}
}
