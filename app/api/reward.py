from fastapi import APIRouter, HTTPException
from app.models.request import RewardRequest # defined Request model
from app.services.reward_service import decide_reward # to calculate reward
from app.services.idempotency_service import get_existing, save # Checks if the request was already processed or Stores the result for idempotency.

router = APIRouter()

@router.post("/reward/decide") #creates an API endpoint
def decide(req: RewardRequest):
    # Reads JSON request body
    # Converts it into a RewardRequest object
    # Validates the fields

    # This checks if the same request was already processed earlier
    cached = get_existing(req.txn_id, req.user_id, req.merchant_id)
    # Then return the previous response instead of recalculating.
    if cached:
        return cached

    try:
        result = decide_reward(req) # calculate the reward
        save(req.txn_id, req.user_id, req.merchant_id, result) #stores the result
        return result

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))