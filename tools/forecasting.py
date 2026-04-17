def forecast_cash_flow(financial_data, days=30):
    balance = financial_data["balance"]
    daily_net = financial_data["daily_net"]

    projection = []

    for day in range(days):
        # This is where we predict the new balance.
        balance += daily_net
        projection.append(balance)

    return {
        "projection": projection,
        "final_balance": projection[-1]
    }