from tools.forecasting import forecast_cash_flow

def analyze(state):
    forecast = forecast_cash_flow(state["financial_data"])

    state["forecast"] = forecast

    print("ANALYZE:", forecast["final_balance"])
    return state