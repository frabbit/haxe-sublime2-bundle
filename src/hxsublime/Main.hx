
package hxsublime;

import python.lib.Inspect;

 
 import python.lib.xml.etree.ElementTree;
 import hxsublime.Temp;
 import hxsublime.Codegen;
 import sublime.View;
 import sublime.Sublime;
 import sublime.Window;
 import sublime.Region;
 import hxsublime.tools.Cache;
 import hxsublime.completion.Base;
 import hxsublime.tools.StringTools;
 import hxsublime.tools.PathTools;
 import hxsublime.tools.SublimeTools;
 import hxsublime.tools.ViewTools;
 import hxsublime.tools.ScopeTools;
 import hxsublime.project.Base;
 import hxsublime.Settings;
 import hxsublime.Exceptions;
 import hxsublime.Log;
 import hxsublime.tools.HxSrcTools;
 import hxsublime.Types;
 import hxsublime.commands.Build;
 import hxsublime.commands.Completion;
 import hxsublime.commands.CompletionServer;
 import hxsublime.commands.CreateType;
 import hxsublime.commands.Execute;
 import hxsublime.commands.FindDeclaration;
 import hxsublime.commands.GenerateImport;
 import hxsublime.commands.GotoAnything;
 import hxsublime.commands.GotoBase;
 import hxsublime.commands.GotoBuildFields;
 import hxsublime.commands.Haxelib;
 import hxsublime.commands.GetExprType;
 import hxsublime.commands.GotoBuildTypes;

using Lambda;


class Hui {
	public function new () {

	}
	public function foo () {
		return 1;
	}

	public static function doIt () {}
}


class Main {

	public static function main () {


		
		
		
	}
}
