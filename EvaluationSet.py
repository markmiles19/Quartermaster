from graph.agent_graph import graph
from tools.sql_tool import run_sql

print("\nRunning Quartermaster Evaluation\n")

# Step 1: Create test state
state = {
    "financial_data": {},
    "forecast": {},
    "risk": "",
    "decision": "",
    "action_result": ""
}

# Step 2: Run agent
print("Step 1: Running agent...")
try:
    result = graph.invoke(state)
    print("PASS: Agent ran successfully\n")
except Exception as e:
    print("FAIL: Agent crashed")
    print(e)
    exit()

# Step 3: Check outputs
print("Step 2: Checking outputs...")
required_keys = ["financial_data", "forecast", "risk", "decision", "action_result"]

missing = False
for key in required_keys:
    if key not in result:
        print(f"FAIL: Missing {key}")
        missing = True

if not missing:
    print("PASS: All required outputs present\n")
else:
    exit()

# Step 4: Check consistency
print("Step 3: Checking consistency...")
result2 = graph.invoke(state)

if result["risk"] == result2["risk"] and result["decision"] == result2["decision"]:
    print("PASS: Results are consistent\n")
else:
    print("FAIL: Results are inconsistent")
    exit()

# Step 5: Check database
print("Step 4: Checking database...")
rows = run_sql("SELECT * FROM finances;")

if rows is not None:
    print(f"PASS: Database returned {len(rows)} rows\n")
else:
    print("FAIL: Database returned no data")
    exit()

print("Evaluation complete: ALL TESTS PASSED\n")