
package hxsublime.support;

import python.NativeIterator;

class NativeIteratorTools {

	public static inline function getRaw <T>(i:NativeIterator<T>):python.NativeIterator.NativeIteratorRaw<T> {
		return cast i;
	}

}