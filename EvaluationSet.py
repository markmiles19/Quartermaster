from graph.agent_graph import graph
from tools.sql_tool import run_sql

print("\nRunning Quartermaster Evaluation\n")

def run_test_case(name, state, expected_behavior):
    print(f"--- {name} ---")
    try:
        result = graph.invoke(state)
    except Exception as e:
        print("FAIL: Agent crashed")
        print(e)
        return False

    required_keys = ["financial_data", "forecast", "risk", "decision", "action_result"]
    for key in required_keys:
        if key not in result:
            print(f"FAIL: Missing {key}")
            return False

    if not expected_behavior(result):
        print("FAIL: Behavior check failed")
        print("Result:", result)
        return False

    print("PASS\n")
    return True

# TEST 1: This ensures that the system flags a high risk whenever there is a negative cash flow.
test1 = {
    "financial_data": {"balance": 12000, "daily_net": -500},
    "forecast": {},
    "risk": "",
    "decision": "",
    "action_result": ""
}

def expect_high_risk(result):
    return result["risk"].lower() == "high"

# TEST 2: Opposite to the previous test, this ensures the system recognizes a low risk scenerio.
test2 = {
    "financial_data": {"balance": 15000, "daily_net": 300},
    "forecast": {},
    "risk": "",
    "decision": "",
    "action_result": ""
}

def expect_low_risk(result):
    return result["risk"].lower() in ["low", "medium"]

# TEST 3: The system recognizes risk when there is gain and loss, but this tests the edge case in which there is no change.
test3 = {
    "financial_data": {"balance": 10000, "daily_net": 0},
    "forecast": {},
    "risk": "",
    "decision": "",
    "action_result": ""
}

def expect_valid_risk(result):
    return result["risk"].lower() in ["low", "medium", "high"]

# TEST 4: This ensures that the same decision is made in two different instances of the same input.
def consistency_test():
    print("--- Consistency Test ---")
    state = {
        "financial_data": {"balance": 12000, "daily_net": -500},
        "forecast": {},
        "risk": "",
        "decision": "",
        "action_result": ""
    }

    result1 = graph.invoke(state)
    result2 = graph.invoke(state)

    if result1["risk"] == result2["risk"] and result1["decision"] == result2["decision"]:
        print("PASS\n")
        return True
    else:
        print("FAIL: Inconsistent results\n")
        return False

# TEST 5: Verifies that the database can be queried.
def database_test():
    print("--- Database Test ---")
    rows = run_sql("SELECT * FROM finances;")

    if rows is not None and len(rows) > 0:
        print(f"PASS: {len(rows)} rows returned\n")
        return True
    else:
        print("FAIL: No data returned\n")
        return False

results = []

results.append(run_test_case("High Risk Scenario", test1, expect_high_risk))
results.append(run_test_case("Low Risk Scenario", test2, expect_low_risk))
results.append(run_test_case("Edge Case Scenario", test3, expect_valid_risk))
results.append(consistency_test())
results.append(database_test())

if all(results):
    print("Evaluation complete: ALL TESTS PASSED\n")
else:
    print("Evaluation complete: SOME TESTS FAILED\n")