package hxsublime.completion.hxsl;

import hxsublime.project.Project;
import python.lib.Types;
import sublime.View;


class Base 
{
	public static function auto_complete( project:Project, view:View , offset:Int, prefix:String ) 
	{
	    var comps = [];
	    for (t in ["Float","Float2","Float3","Float4","Matrix","M44","M33","M34","M43","Texture","CubeTexture","Int","Color","include"]) 
	    {
	        comps.push( Tup2.create( t , "hxsl Type" ) );
	    }
	    return comps;
	}
}
