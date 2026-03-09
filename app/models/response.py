from pydantic import BaseModel
from typing import List, Dict

class RewardResponse(BaseModel):
    decision_id: str
    policy_version: str
    reward_type: str
    reward_value: int
    xp: int
    reason_codes: List[str]
    meta: Dict