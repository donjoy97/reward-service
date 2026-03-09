import redis
import json

class Cache:
    # Cache layer
    # Redis (preferred)
    # Memory fallback (if Redis down)
    def __init__(self):
        try:
            # Connect to Redis server
            # ping() checks if Redis is alive
            self.client = redis.Redis(host="localhost", port=6379)
            self.client.ping()
            self.redis=True
        except:
            self.redis=False
            self.store={}   # dictionary as fallback cache
                            # the service does not crash when Redis is down

    def get(self,key):
        try:
            if self.redis:
                val=self.client.get(key) # Redis returns bytes
                return json.loads(val) if val else None #we convert it back to Python
            return self.store.get(key) # Fetch from the in-memory dictionary, if redis fails
        except:
            return None

    def set(self,key,val,ttl=None):
        try:
            if self.redis:
                self.client.setex(key,ttl,json.dumps(val)) # JSON string in Redis
            else:
                self.store[key]=val
                # TTL is ignored in memory fallback
        except:
            pass

cache=Cache()