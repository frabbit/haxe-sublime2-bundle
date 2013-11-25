
package hxsublime;

import python.lib.Types.Dict;

import hxsublime.macros.LazyFunctionSupport;

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
import hxsublime.commands.ShowDoc;
import hxsublime.panel.TabPanel;
import hxsublime.panel.SlidePanel;
import hxsublime.panel.Tools;
import hxsublime.completion.hxsl.Base;
import hxsublime.completion.hxml.Base;
import hxsublime.compiler.Server;
import hxsublime.compiler.Output;


using Lambda;



using StringTools;

enum Hui {
	Foo1(a:Int);
	Foo2;
}

class Main{

	public static function main () {
		
		// var z = function () return 1;

		// z();

		// trace(z());


		// trace(1);

		// trace(1 + "hey");

		// trace("hey");

		// trace({ foo : "bar"});
		// var z = true;
		//var t = switch (z) {
		//	case true: 5;
		//	case false: 7;
		//}
		var t = Foo1(5);
		var z = switch (t) {
			case Foo1(x) if (x > 2): true;
			case _: false;
		}
		trace(t);
	}


}
