package hxsublime.tools;

class ScopeTools {
	public static function containsAny (scopes:Array<String>, scopes_test:Array<String>) 
	{
		for (s in scopes) 
		{
			if (python.lib.ArrayTools.contains( scopes_test, s.split(".")[0])) 
			{
				return true;
			}
		}
		return false;
	}
	public static function containsStringOrComment (scopes:Array<String>) 
	{
		return containsAny(scopes, ["string", "comments"]);
	}
}
