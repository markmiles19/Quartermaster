from utils.logger import log_step
from agents.financial_crew import run_financial_analysis

def plan(state):
    financial_data = state["financial_data"]

    result = run_financial_analysis(
        financial_data,
        state.get("forecast")
    )

    analysis_output = result.tasks_output[0].raw

    output_lower = analysis_output.lower()

    # VERY IMPORTANT TO INITIALIZE THIS FIRST!!!
    risk = "low"

    tool_call = {
        "tool": "none",
        "query": None
    }

    decision = ""

    # Make sure the formatting is the exact same as the prompt.
    if "risk: high" in output_lower:
        risk = "high"
    elif "risk: medium" in output_lower:
        risk = "medium"
    elif "risk: low" in output_lower:
        risk = "low"

    if "tool: email" in output_lower:
        tool_call = {"tool": "email", "query": None}
    elif "tool: forecast" in output_lower:
        tool_call = {"tool": "forecast", "query": None}

    if "reason:" in output_lower:
        decision = analysis_output.split("REASON:")[-1].strip()
    else:
        decision = analysis_output

    print(f'output: {output_lower}')
    print(f'Testing risk: {risk}')
    state["risk"] = risk
    state["analysis"] = result.tasks_output[0].raw
    state["strategy"] = result.tasks_output[1].raw
    state["decision"] = decision
    state["tool_call"] = tool_call

    log_step("PLAN", {
        "risk": risk,
        "tool_call": tool_call
    })
    
    return state