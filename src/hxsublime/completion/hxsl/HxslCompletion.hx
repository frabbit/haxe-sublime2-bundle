package hxsublime.completion.hxsl;

import hxsublime.project.Project;
import sublime.View;
import python.Tuple;

class HxslCompletion
{
	public static function autoComplete( project:Project, view:View , offset:Int, prefix:String )
	{
	    var comps = [];
	    for (t in ["Float","Float2","Float3","Float4","Matrix","M44","M33","M34","M43","Texture","CubeTexture","Int","Color","include"])
	    {
	        comps.push( Tuple2.make( t , "hxsl Type" ) );
	    }
	    return comps;
	}
}
