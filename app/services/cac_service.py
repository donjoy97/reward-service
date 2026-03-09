from datetime import date
from app.core.cache import cache

def key(user_id):
    return f"cac:{user_id}:{date.today()}"

def get_spend(user_id):
    return cache.get(key(user_id)) or 0

def add_spend(user_id,amount):
    total=get_spend(user_id)+amount
    cache.set(key(user_id),total,86400)