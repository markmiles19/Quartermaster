from graph.agent_graph import graph
from tools.sql_tool import run_sql

def main():
    state = {
        "financial_data": {},
        "forecast": {},
        "risk": "",
        "decision": "",
        "action_result": ""
    }

    print("\n\nNow Running Quartermaster Agent\n|\nv\n")

    result = graph.invoke(state)

    print("\n\nFinal Output\n|\nv\n")
    print(f"Financial Data: {result['financial_data']}")
    print(f"Forecast Final Balance: {result['forecast']['final_balance']}")
    print(f"Risk Level: {result['risk']}")
    print(f"Decision: {result['decision']}")
    print(f"Action Result: {result['action_result']}")
    print("\n\nFinished!\n")

    # Uncomment the block below to view the database for debugging purposed.
    # print(run_sql("SELECT * FROM finances;"))


if __name__ == "__main__":
    # These are only test values for right now.
    # Later we will pass in the actual balance and daily net once we get this figured out.
    main()