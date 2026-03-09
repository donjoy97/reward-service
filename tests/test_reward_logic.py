from app.services.reward_service import calculate_xp

def test_xp():
    assert calculate_xp(100,"NEW") > 0