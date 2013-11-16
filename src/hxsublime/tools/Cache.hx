
package hxsublime.tools;

import haxe.ds.StringMap;
import Map.IMap;
import python.lib.Time;

typedef CacheEntry<T> = {
	time : Int,
	val : T,
}

class Cache<K, T> 
{
	
	var time_driven : Bool;
	var cache_time : Int;
	public var data : IMap<K, CacheEntry<T>>;

	public function new (cache_time = -1, data:IMap<K, CacheEntry<T>> = null ) 
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
		return get_or_default(id, null) != null;
	}
	
	public function get_or_insert (id:K, creator:Void->T) 
	{
		var res = null;
		if (data.exists(id)) {
			
			res = _get_val(id);
		} else {
			res = creator();
			insert(id, res);
		}
		return res;
	}

	function _get_val (id:K) 
	{
		return data.get(id).val;
	}

	function _cache_invalid (id:K) 
	{
		return !_cache_valid(id);
	}

	function _cache_valid (id:K) 
	{
		var now = Time.time();
		
		return now - data.get(id).time <= cache_time;
	}

	public function get_or_default (id:K, defaultVal = null) 
	{
		var res = defaultVal;
		if (data.exists(id))
			if (time_driven && _cache_invalid(id)) {
				data.remove(id);
			} else {
				res = _get_val(id);
			}
		return res;
	}

	public function get_and_delete (id:K, defaultVal = null) 
	{
		var val = defaultVal;
		if (data.exists(id)) {
			if (!time_driven || _cache_valid(id)) {
				val = _get_val(id);
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

/*import time

class Cache:
	def __init__ (self, cache_time = -1 ):
		self.data = {}
		self.cache_time = cache_time
		self.time_driven = cache_time != -1

	def insert (self, id, value):
		self.data[id] = (time.time(), value)

	def exists (self, id):
		return self.get_or_default(id, None) != None
	
	def get_or_insert (self, id, creator):
		res = None
		if id in self.data:
			res = self._get_val(id)
		else:
			res = creator()
			self.insert(id, res)
		return res

	def _get_val (self, id):
		return self.data[id][1]

	def _cache_invalid (self, id):
		return not self._cache_valid(id)

	def _cache_valid (self, id):
		now = time.time()
		return now - self.data[id][0] <= self.cache_time

	def get_or_default (self, id, default = None):
		res = default
		if id in self.data:
			if self.time_driven and self._cache_invalid(id):
				del self.data[id]
			else:
				res = self._get_val(id)
		return res

	def get_and_delete (self, id, default=None):
		val = default
		if id in self.data:
			if not self.time_driven or self._cache_valid(id):
				val = self._get_val(id)
			del self.data[id]
		return val

	def delete (self, id):
		if (id in self.data):
			del self.data[id]
*/