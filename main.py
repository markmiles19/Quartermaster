from graph.agent_graph import graph

def main(balance, daily_net):
    state = {
        "financial_data": {
            "Balance": balance,
            "daily_net": daily_net
        },
        "forecast": {},
        "risk": "",
        "decision": "",
        "action_result": ""
    }

    print("\nNow Running Quartermaster Agent\n")

    result = graph.invoke(state)

    print("\nFinal Output\n")
    print(f"Financial Data: {result['financial_data']}")
    print(f"Forecast Final Balance: {result['forecast']['final_balance']}")
    print(f"Risk Level: {result['risk']}")
    print(f"Decision: {result['decision']}")
    print(f"Action Result: {result['action_result']}")
    print("\nFinished!\n")


if __name__ == "__main__":
    # These are only test values for right now.
    # Later we will pass in the actual balance and daily net once we get this figured out.
    main(5000, -150)