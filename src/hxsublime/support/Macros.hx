package hxsublime.support;

import haxe.macro.Expr;

class Macros {

    @:noUsing macro public static function pyFor <T>(v:Expr, it:Expr, b:Expr):haxe.macro.Expr
    {
        return macro @:pos(v.pos)
            python.Syntax.foreach($v, $it, {
                // this is a trick to make block expression type safe (checked by the compiler)
                $v = if (false) hxsublime.support.NativeIteratorTools.getRaw($it).__next__() else $v;
                $b;
            });
    }
}