from app.core.cache import cache

TTL=86400

# generates unique cache key
def key(txn_id,user_id,merchant_id):
    return f"idem:{txn_id}:{user_id}:{merchant_id}"

def get_existing(txn_id,user_id,merchant_id):
    # Creates the cache key
    # Looks up the cache
    # Returns stored result if present
    return cache.get(key(txn_id,user_id,merchant_id))

# stores result with TTL.
def save(txn_id,user_id,merchant_id,value):
    cache.set(key(txn_id,user_id,merchant_id),value,TTL)