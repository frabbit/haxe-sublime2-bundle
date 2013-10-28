package hxsublime.tools;

import python.lib.os.Path;
import python.lib.Shutil.ShUtil;

class PathTools {
	public static function removeDir (path:String) 
	{
		if (Path.isdir(path)) {
			ShUtil.rmtree(path);
		}
	}
	
	public static function joinNorm(path1:String, path2:String) 
	{
		return Path.normpath(Path.join(path1, path2));	
	}

}