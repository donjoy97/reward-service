from pydantic import BaseModel

class RewardRequest(BaseModel):
    txn_id: str
    user_id: str
    merchant_id: str
    amount: float
    txn_type: str
    ts: int