package hxsublime.support;


import haxe.macro.Expr;

import haxe.macro.Context;
#if macro
import haxe.macro.ExprTools;
#end
#if !macro


import python.NativeIterator;
#end


class Macros {


    @:noUsing macro public static function pyFor <T>(v:Expr, it:Expr, b:Expr):haxe.macro.Expr
    {

        var id = switch (v.expr) {
            case EConst(CIdent(x)):x;
            case _ : Context.error("unexpected " + ExprTools.toString(v) + ": const ident expected", v.pos);
        }

        return macro
            //var $id = hxsublime.support.NativeIteratorTools.getRaw($it).__next__();
            python.Syntax.foreach($v, $it, {
                var $id = $v;
                var $id = if (false) hxsublime.support.NativeIteratorTools.getRaw($it).__next__() else $v;
                $b;
            });
    }



}