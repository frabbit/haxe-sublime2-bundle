package hxsublime.panel;

import python.lib.datetime.DateTime;

class Tools {
	public static function haxe_file_regex() {
		// avoid circular dependency
		// from haxe.project.tools import haxe_file_regex
		return "^[0-9]{2}:[0-9]{2}:[0-9]{2}[ ]Error:[ ]" + haxe_file_regex.substr(1);
	}

	public static function timestamp_msg (msg) {
		return DateTime.now().strftime("%H:%M:%S") + " " + msg;
	}

	public static function valid_message (msg) {
		return msg != None && msg != "" && msg != "\n";
	}
}

/*
from datetime import datetime


def haxe_file_regex():
	#avoid circular dependency
	from haxe.project.tools import haxe_file_regex
	return "^[0-9]{2}:[0-9]{2}:[0-9]{2}[ ]Error:[ ]" + haxe_file_regex[1:]

def timestamp_msg (msg):
	return datetime.now().strftime("%H:%M:%S") + " " + msg;

def valid_message (msg):
	return msg != None and msg != "" and msg != "\n"
*/