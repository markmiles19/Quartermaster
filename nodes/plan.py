from utils.logger import log_step
from agents.financial_crew import run_financial_analysis

def plan(state):
    forecast = state["forecast"]

    result = run_financial_analysis(
    state["financial_data"],
    forecast
    )

    output = str(result).lower()
    if "high" in output:
        risk = "high"
    elif "medium" in output:
        risk = "medium"
    else:
        risk = "low"

    decision = str(result)

    state["risk"] = risk
    state["decision"] = decision
    log_step("PLAN", {
        "risk": risk,
        "decision": decision
    })
    
    return state
