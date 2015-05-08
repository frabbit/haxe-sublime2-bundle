package hxsublime.macros;

import haxe.macro.Context;
import haxe.macro.Expr.Access.AStatic;
import haxe.macro.Expr.Field;
import haxe.macro.Expr.FieldType.FFun;

using Lambda;

class LazyFunctionMacro {

	static var id = "lazyFunction";

	macro public static function build ():Array<Field> 
	{
		var fields = Context.getBuildFields();
		var cl = Context.getLocalClass().get();

		var metaName = ":" + id + "__Applied";
		if (!cl.meta.has(metaName)) {

			cl.meta.add(metaName,[], Context.currentPos());
			var newFields = [];
			for (f in fields) {
				if (f.meta.exists(function (e) return e.name == id)) {
					f.meta = f.meta.filter(function (e) return e.name != id);
					switch (f.kind) {
						case FFun(fn) if (fn.args.length == 0):

							var name = f.name + "_cache";
							var name1 = f.name + "_cache_set";
							var isStatic = f.access.exists(function (a) return a.match(AStatic));

							var temp = macro class X { private var $name = null; private var $name1 = false; };
							var cacheField = temp.fields[0];
							cacheField.pos = f.pos;
							var cacheSetField = temp.fields[1];
							cacheSetField.pos = f.pos;
							if (isStatic) {
								cacheField.access.push(AStatic);
								cacheSetField.access.push(AStatic);
							}
							newFields.push(cacheField);
							newFields.push(cacheSetField);
							fn.expr = macro {
								
								if (!$i{name1}) {
									$i{name1} = true;
									function eval () ${fn.expr};
									$i{name} = eval();
								}
								return $i{name};
							};
						case _:
					}
				}
				newFields.push(f);
			}
			return newFields;
		} else {
			return fields;
		}
	}
}