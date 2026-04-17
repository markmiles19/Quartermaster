from tools.sql_tool import run_sql
from utils.logger import log_step

def observe(state):
    result = run_sql("SELECT balance, daily_net FROM finances LIMIT 1;")

    balance, daily_net = result[0]

    state["financial_data"] = {
        "balance": balance,
        "daily_net": daily_net
    }

    log_step("Observe", state["financial_data"])

    print("OBSERVE:", state["financial_data"])

    return state