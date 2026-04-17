from graph.agent_graph import graph

def main():
    state = {
        "financial_data": {},
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
    main()