package hxsublime;

import python.Dict;

import hxsublime.macros.LazyFunctionSupport;

import python.lib.Builtins;
import python.lib.Inspect;

import python.lib.xml.etree.ElementTree;
import hxsublime.Temp;
import hxsublime.Codegen;
import sublime.View;
import sublime.Sublime;
import sublime.Window;
import sublime.Region;
import hxsublime.tools.Cache;
import hxsublime.completion.Completion;
import hxsublime.tools.StringTools;
import hxsublime.tools.PathTools;
import hxsublime.tools.SublimeTools;
import hxsublime.tools.ViewTools;
import hxsublime.tools.ScopeTools;
import hxsublime.project.Projects;
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
import hxsublime.completion.hxsl.HxslCompletion;
import hxsublime.completion.hxml.HxmlCompletion;
import hxsublime.compiler.Server;
import hxsublime.compiler.Output;

using Lambda;

using StringTools;

class Main {

	
	public static function main ()
	{
		// sublime doesn't like the regular stdout print method
		haxe.Log.trace = function (msg, ?pos) {
			var prefix = pos.fileName + ":" + pos.lineNumber;
			Builtins.print(prefix + ":" + Std.string(msg));
		}
	}

}

