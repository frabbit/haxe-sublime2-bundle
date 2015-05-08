package hxsublime.build;

import hxsublime.build.HxmlBuild;
import hxsublime.Config;
import hxsublime.panel.Panels;
import hxsublime.project.Project;
import hxsublime.tools.PathTools;
import python.lib.Codecs;
import python.lib.Glob;
import python.lib.Inspect;
import python.lib.io.StringIO;
import python.lib.Os;
import python.lib.os.Path;
import python.lib.Re;
import python.Tuple;
import sublime.Sublime;

using StringTools;
using hxsublime.support.ArrayTools;

using hxsublime.support.StringTools;

private typedef Buffer = {
	public function readline ():String;

}

class Tools {


	static var _extract_tag = Re.compile("<([a-z0-9_-]+).*?\\s(name|main|title|file)=\"([ a-z0-9_./-]+)\"", Re.I);

	// TODO refactor this method into smaller managable chunks
	static function hxmlBufferToBuilds(project:Project, hxml_buffer:Buffer, folder:String, build_path:String, buildFile:String = null, hxml:String = null)
	{
		var builds = [];

		var currentBuild = new HxmlBuild(hxml, buildFile);

		var f = hxml_buffer;
		while (true)
		{
			var l = f.readline();


			if (l == "") {
				break;
			}

			if (l == "\n") {
				continue;
			}

			l = l.strip();

			if (l.startsWith("#build-name="))
			{
				currentBuild.name = l.substr(12);
				continue;
			}
			if (l.startsWith("#"))
			{
				continue;
			}

			if (l.startsWith("--next"))
			{
				if (currentBuild.getClassPaths().length == 0)
				{
					trace("no classpaths");
					currentBuild.addClasspath( build_path );
				}

				builds.push( currentBuild );
				currentBuild = new HxmlBuild(hxml, buildFile);
				continue;
			}

			if (l.endsWith(".hxml"))
			{

				trace("found ref of hxml file:" + l);
				var path = Path.dirname(hxml);
				var subBuilds = hxmlToBuilds(project, path + Os.sep + l, folder);
				if (subBuilds.length == 1)
				{
					var b = subBuilds[0];
					currentBuild.merge(b);
				}
			}

			if (l.startsWith("-main") )
			{
				var spl = l.split(" ");
				if (spl.length == 2 )
				{
					currentBuild.main = spl[1];
				}
				else {
					Sublime.status_message( "Invalid build.hxml : no Main class" );
				}
			}

			if (l.startsWith("-lib") )
			{
				var spl = l.split(" ");
				if (spl.length == 2 )
				{
					var lib = project.haxelibManager().get( spl[1] );
					if (lib != null)
					{
						//trace("lib to build:" + Std.string(lib));
						currentBuild.addLib( lib );
					}
					else {

						currentBuild.addArg( Tuple2.make("-lib", spl[1] ) );
						//from haxe import panel
						Panels.defaultPanel().writeln("Error: haxelib library " + Std.string(spl[1]) + " is not installed" );
					}
				}
				else {
					Sublime.status_message( "Invalid build.hxml : lib not found" );
				}
			}

			if (l.startsWith("-cmd") )
			{
				var spl = l.split(" ");
				currentBuild.addArg( Tuple2.make( "-cmd" , spl.slice(1).join(" ") ) );
			}

			if (l.startsWith("--macro"))
			{
				var spl = l.split(" ");
				currentBuild.addArg( Tuple2.make( "--macro" , spl.slice(1).join(" ")  ) );
			}

			if (l.startsWith("-D"))
			{
				var x = l.split(" ");

				var tup = Tuple2.make(x[0], x[1]);
				currentBuild.addArg( tup );
				currentBuild.addDefine(tup._2);
				continue;
			}

			for (flag in [ "swf-version" , "swf-header",
						"debug" , "-no-traces" , "-flash-use-stage" , "-gen-hx-classes" ,
						"-remap" , "-no-inline" , "-no-opt" , "-php-prefix" ,
						"-js-namespace" , "-interp" , "-dead-code-elimination" ,
						"-php-front" , "-php-lib", "dce" , "-js-modern", "-times" ])
			{
				if (l.startsWith( "-"+flag ) )
				{
					var x = l.split(" ");

					var p2 = if (x.length == 1) "" else x[1];
					currentBuild.addArg( Tuple2.make(x[0], p2) );

					break;
				}
			}

			for (flag in [ "resource" , "xml" , "x" , "swf-lib" , "java-lib" ])
			{
				if (l.startsWith( "-"+flag ) )
				{
					var spl = l.split(" ");
					var outp = Path.join( folder , spl.slice(1).join(" ") );
					currentBuild.addArg( Tuple2.make("-"+flag, outp) );
					if (flag == "x")
					{
						currentBuild._target = "neko";
					}
					break;
				}
			}

			for (flag in Config.targets)
			{
				if (l.startsWith( "-" + flag + " " ) )
				{
					var spl = l.split(" ");
					spl.shift();
					var outp = spl.join(" ");

					currentBuild.addArg( Tuple2.make("-"+flag, outp) );

					currentBuild._target = flag;
					currentBuild.output = outp;
					break;
				}
			}

			if (l.startsWith("-cp "))
			{
				var cp = l.split(" ");
				cp.shift();
				var classpath = cp.join( " " );

				var abs_classpath = PathTools.joinNorm( build_path , classpath );
				currentBuild.addClasspath( abs_classpath );
				//currentBuild.addArg( ("-cp" , abs_classpath ) )
			}
		}

		if (currentBuild.getClassPaths().length == 0)
		{

			currentBuild.addClasspath( build_path );
			//currentBuild.args.push( ("-cp" , build_path ) )
		}

		//currentBuild.get_types()
		builds.push( currentBuild );

		return builds;
	}


	static function findBuildFiles(folder:String, extension:String)
	{

		if (!Path.isdir(folder) )
		{
			return [];
		}

		var files = Glob.glob( Path.join( folder , "*."+extension ) ).map(function (x) return Tuple2.make(x, folder));


		for (dir in Os.listdir(folder))
		{
			var f = Path.join(folder, dir);
			var x = Glob.glob( Path.join( f , "*."+extension ) ).map(function (x) return Tuple2.make(x, f));
			files.extend( x );
		}

		return files;
	}

	static function hxmlToBuilds (project, hxml, folder):Array<HxmlBuild>
	{
		var build_path = Path.dirname(hxml);
		var hxml_buffer = Codecs.open( hxml , "r+" , "utf-8" , "ignore" );
		return hxmlBufferToBuilds(project, { readline : function () return hxml_buffer.readline() }, folder, build_path, hxml, hxml);
	}



	static function _find_nme_project_title(nmml_file)
	{
		var f = Codecs.open( nmml_file , "r+", "utf-8" , "ignore" );
		var title = null;
		while (true)
		{
			var l = f.readline();
			if (l == null)
			{
				break;
			}
			var m = _extract_tag.search(l);
			if (m != null)
			{
				var tag = m.group(1);

				if (tag == "meta" || tag == "app")
				{
					var mFile = Re.search("\\b(file|title)=\"([ a-z0-9_-]+)\"", l, Re.I);
					if (mFile != null)
					{
						title = mFile.group(2);
						break;
					}
				}
			}
		}
		(f:Dynamic).close();
		return title;
	}

	public static function createHaxeBuildFromNmml (project:Project, target, nmml, display_cmd:Array<String>)
	{
		var cmd = display_cmd.copy();
		cmd.push(nmml);
		cmd.push(target.plattform);
		cmd.extend(target.args);

		var nmml_dir = Path.dirname(nmml);

		var r = Execute.runCmd( cmd, null, nmml_dir );
		var out = r._1, err = r._2;
		var io = new StringIO(out);
		return hxmlBufferToBuilds(project, { readline : function () return io.readline() }, nmml_dir, nmml_dir, nmml, null)[0];
	}

	public static function findHxmlProjects( project, folder )
	{

		var builds = [];
		var found = findBuildFiles(folder, "hxml");
		for (build in found) {

			var hxml_file = build._1;
			var hxml_folder = build._2;

			var b = hxmlToBuilds(project, hxml_file, hxml_folder);

			builds.extend(b);
		}

		return builds;
	}

	public static function findNmeProjects( project:Project, folder:String )
	{
		var found = findBuildFiles(folder, "nmml");
		var builds = [];
		for (build in found)
		{
			var nmml_file = build._1;
			var title = _find_nme_project_title(nmml_file);
			if (title != null)
			{
				for (t in Config.nme_targets)
				{
					builds.push(new NmeBuild(project, title, nmml_file, t));
				}
			}
		}
		return builds;
	}

	public static function findOpenflProjects( project:Project, folder:String )
	{
		var found = findBuildFiles(folder, "xml");
		var builds = [];
		for (build in found)
		{
			var openfl_xml = build._1;
			var title = _find_nme_project_title(openfl_xml);
			if (title != null)
			{
				for (t in Config.openfl_targets)
				{
					builds.push(new OpenFlBuild(project, title, openfl_xml, t));
				}
			}
		}

		return builds;
	}
}
