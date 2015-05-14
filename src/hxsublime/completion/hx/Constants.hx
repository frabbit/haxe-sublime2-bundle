package hxsublime.completion.hx;
class Constants 
{
	public static inline var COMPLETION_TYPE_REGULAR = 1; // regular compiler completion without hints
	public static inline var COMPLETION_TYPE_HINT = 2; // compiler hints
	public static inline var COMPLETION_TYPE_TOPLEVEL = 4; // include top level if useful
	public static inline var COMPLETION_TYPE_TOPLEVEL_FORCED = COMPLETION_TYPE_TOPLEVEL | 8; // force inclusion of top level completion
	public static inline var TOPLEVEL_OPTION_TYPES = 1;
	public static inline var TOPLEVEL_OPTION_LOCALS = 2;
	public static inline var TOPLEVEL_OPTION_KEYWORDS = 4;
	public static inline var TOPLEVEL_OPTION_ALL = TOPLEVEL_OPTION_KEYWORDS | TOPLEVEL_OPTION_LOCALS | TOPLEVEL_OPTION_TYPES;
}

