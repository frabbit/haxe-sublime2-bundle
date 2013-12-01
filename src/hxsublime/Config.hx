package hxsublime;

import haxe.ds.StringMap;
import python.lib.Types;

class Config 
{
    
    public static var target_packages = ["flash","flash8","neko","js","php","cpp","cs","java", "sys"];
    public static var targets = ["js","cpp","swf8","swf","neko","php","java","cs", "as3"];
    
    public static var target_std_packages:StringMap<Array<String>> = [
        "js"   => ["js"],
        "cpp"  => ["cpp", "sys"],
        "neko" => ["neko", "sys"],
        "php"  => ["php", "sys"],
        "java" => ["java", "sys"],
        "cs"   => ["cs", "sys"],
        "swf"  => ["flash"],
        "as3"  => ["flash"],
        "swf8" => ["flash8"]
    ];
    public static var ignored_folders_list =  [".git", ".svn"];

    

    public static function mk_ignored_folders () return {
        var x = new StringMap();
        for (p in ignored_folders_list) {
            x.set(p, true);
        }
        x;
    }
    public static var ignored_folders = mk_ignored_folders();

    public static var ignored_packages_list = ["neko._std", "cpp._std", "php._std", "js._std", "flash._std"];

    
    
    public static function mk_ignored_packages () return {
        var x = new StringMap();
        for (p in ignored_folders_list) {
            x.set(p,true);
        }
        x;
    }    
    public static var ignored_packages = mk_ignored_packages();

    public static var ignored_types = ["haxe.io.BytesData.Unsigned_char__"];

    public static var nme_targets = [
        new NmeTarget("Flash",                "flash",      ["-debug"]),
        new NmeTarget("HTML5",                "html5",      ["-debug"]),
        new NmeTarget("C++",                  "cpp",        ["-debug"]),
        new NmeTarget("Windows",              "windows",    ["-debug"]),
        new NmeTarget("Mac",                  "mac",        ["-debug"]),
        new NmeTarget("Linux",                "linux",      ["-debug"]),
        new NmeTarget("Linux 64",             "linux",      ["-64 -debug"]),
        new NmeTarget("iOs - iPhone simulator",    "ios",        ["-simulator -debug"]),
        new NmeTarget("iOs - iPad simulator",      "ios",        ["-simulator -ipad -debug"]),
        new NmeTarget("iOs - update XCode project",        "ios",        ["-ipad -debug"]),
        new NmeTarget("Neko",                "neko",   ["-debug"]),
        new NmeTarget("Neko 64",             "neko",    ["-64 -debug"]),
        new NmeTarget("WebOs",             "webos",     ["-debug"]),
        new NmeTarget("BlackBerry",             "blackberry",   ["-debug"]),
        new NmeTarget("Android",             "android",   ["-debug"])
    ];

    public static var openfl_targets = [
        new OpenFlTarget("Flash",                "flash",          ["-debug"]),
        new OpenFlTarget("HTML5",                "html5",          ["-debug"]),
        new OpenFlTarget("C++",                  "cpp",           ["-debug"]),
        new OpenFlTarget("Windows",              "windows",       ["-debug"]),
        new OpenFlTarget("Mac",                  "mac",       ["-debug"]),
        new OpenFlTarget("Linux",                "linux",       ["-debug"]),
        new OpenFlTarget("Linux 64",             "linux",        ["-64 -debug"]),
        new OpenFlTarget("iOs - iPhone simulator",    "ios",         ["-simulator -debug"]),
        new OpenFlTarget("iOs - iPad simulator",      "ios",         ["-simulator -ipad -debug"]),
        new OpenFlTarget("iOs - update XCode project",        "ios",        ["-ipad -debug"]),
        new OpenFlTarget("Neko",                "neko",        ["-debug"]),
        new OpenFlTarget("Neko 64",             "neko",         ["-64 -debug"]),
        new OpenFlTarget("Emscripten",             "emscripten",   ["-debug"]),    
        new OpenFlTarget("WebOs",             "webos",     ["-debug"]),
        new OpenFlTarget("BlackBerry",             "blackberry",    ["-debug"]),
        new OpenFlTarget("Android",             "android",     ["-debug"])
    ];


    public static var SOURCE_HAXE = 'source.haxe.2';
    public static var SOURCE_HXML = 'source.hxml';
    public static var SOURCE_NMML = 'source.nmml';
    public static var SOURCE_ERAZOR = 'source.erazor';
    public static var HXSL_SUFFIX = '.hxsl';

}


typedef Target = {
    public var name:String;
    public var plattform:String;
    public var args:Array<String>;   
}

class NmeTarget 
{
    public var name:String;
    public var plattform:String;
    public var args:Array<String>;

    public function new (name:String, plattform:String, args:Array<String>)
    {
        this.name = name;
        this.plattform = plattform;
        this.args = args;
    }
}
 
class OpenFlTarget 
{
    public var name:String;
    public var plattform:String;
    public var args:Array<String>;

    public function new (name:String, plattform:String, args:Array<String>)
    {
        this.name = name;
        this.plattform = plattform;
        this.args = args;
    }
}       

        
 



