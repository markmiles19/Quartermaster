from utils.logger import log_step

def act(state):
    risk = state["risk"]
    decision = state["decision"]

    if risk == "low":
        action_result = "No action taken"
    elif risk == "medium":
        action_result = f"Recommended action: {decision}"
    elif risk == "high":
        action_result = f"URGENT: {decision} (requires user approval)"

    state["action_result"] = action_result
    log_step("ACT", action_result)

    return state