from app.services.idempotency_service import save,get_existing

def test_cache():
    save("t1","u1","m1",{"a":1})
    assert get_existing("t1","u1","m1")=={"a":1}