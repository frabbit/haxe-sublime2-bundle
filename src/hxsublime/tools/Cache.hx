
package hxsublime.tools;

import haxe.ds.StringMap;
import Map.IMap;
import python.lib.Time;

typedef CacheEntry<T> = {
	time : Float,
	val : T,
}

class Cache<K, T>
{

	var time_driven : Bool;
	var cache_time : Int;

	public var data : IMap<K, CacheEntry<T>>;

	public function new (data:IMap<K, CacheEntry<T>>,cache_time = -1 )
	{
		this.data = data;
		this.cache_time = cache_time;
		this.time_driven = cache_time != -1;
	}

	public function insert (id:K, value:T)
	{
		data.set(id, { time : Time.time(), val : value});
	}

	public function exists (id:K)
	{
		return getOrDefault(id, null) != null;
	}

	public function getOrInsert (id:K, creator:Void->T)
	{
		var res = null;
		if (data.exists(id)) {

			res = unsafeGetVal(id);
		} else {
			res = creator();
			insert(id, res);
		}
		return res;
	}

	function unsafeGetVal (id:K)
	{
		return data.get(id).val;
	}

	function isCacheInvalid (id:K)
	{
		return !isCacheValid(id);
	}

	function isCacheValid (id:K)
	{
		var now = Time.time();

		return now - data.get(id).time <= cache_time;
	}

	public function getOrDefault (id:K, defaultVal:T = null)
	{
		var res = defaultVal;
		if (data.exists(id))
		{
			if (time_driven && isCacheInvalid(id)) {
				data.remove(id);
			} else {
				res = unsafeGetVal(id);
			}
		}
		return res;
	}

	public function getAndDelete (id:K, defaultVal = null)
	{
		var val = defaultVal;
		if (data.exists(id))
		{
			if (!time_driven || isCacheValid(id))
			{
				val = unsafeGetVal(id);
			}
			data.remove(id);
		}
		return val;
	}

	public function delete (id:K)
	{
		if (data.exists(id)) {
			data.remove(id);
		}
	}


}
