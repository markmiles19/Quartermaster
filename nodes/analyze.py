from tools.forecasting import forecast_cash_flow
from utils.logger import log_step

def analyze(state):
    forecast = forecast_cash_flow(state["financial_data"])

    state["forecast"] = forecast

    print("ANALYZE:", forecast["final_balance"])
    return state