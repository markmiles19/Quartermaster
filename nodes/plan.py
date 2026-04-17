from utils.logger import log_step

def plan(state):
    forecast = state["forecast"]
    final_balance = forecast["final_balance"]

    if final_balance < 0:
        risk = "high"
    elif final_balance <= 500:
        risk = "medium"
    else:
        risk = "low"

    if risk == "high":
        decision = "Reduce expenses and delay non-critical payments"
    elif risk == "medium":
        decision = "Monitor closely and reduce discretionary spending"
    else:
        decision = "No immediate action required"

    state["risk"] = risk
    state["decision"] = decision
    log_step("PLAN", {
        "risk": risk,
        "decision": decision
    })
    
    return state