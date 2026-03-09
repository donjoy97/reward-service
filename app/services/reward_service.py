import uuid #generates a unique decision ID for every reward decision
from app.policies.policy_loader import policy # reward rules loaded from your YAML policy file.
from app.services.persona_service import persona_service # determines the user persona
from app.services.cac_service import get_spend, add_spend # 

def calculate_xp(amount,persona):

    multiplier=policy["persona_multipliers"].get(persona,1)

    xp=amount*policy["xp_per_rupee"]*multiplier

    return int(min(xp,policy["max_xp_per_txn"]))


def decide_reward(req):

    persona=persona_service.get_persona(req.user_id)

    xp=calculate_xp(req.amount,persona)

    reward_type="XP"
    reward_value=0

    cap=policy["daily_cac_cap"][persona]

    if get_spend(req.user_id) < cap:

        reward_type="CHECKOUT"
        reward_value=int(req.amount*0.05)

        add_spend(req.user_id,reward_value)

    return {
        "decision_id":str(uuid.uuid4()),
        "policy_version":policy["policy_version"],
        "reward_type":reward_type,
        "reward_value":reward_value,
        "xp":xp,
        "reason_codes":[],
        "meta":{"persona":persona}
    }