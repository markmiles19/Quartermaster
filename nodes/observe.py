from tools.sql_tool import run_sql

def observe(state):
    result = run_sql("SELECT balance, daily_net FROM finances LIMIT 1;")

    state["financial_data"] = {
        "balance": result[0][0],
        "daily_net": result[0][1]
    }

    print("OBSERVE:", state["financial_data"])
    return state