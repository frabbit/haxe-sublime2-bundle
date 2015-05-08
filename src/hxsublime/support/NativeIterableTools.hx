
package hxsublime.support;

import python.NativeIterable;
import python.NativeIterator;

class NativeIterableTools {

	public static inline function getRaw <T>(i:NativeIterable<T>):NativeIterableRaw<T> {
		return cast i;
	}

	public static inline function getNativeIterator <T>(i:NativeIterable<T>):NativeIterator<T> {
		return (cast i:NativeIterableRaw<T>).__iter__();
	}

}