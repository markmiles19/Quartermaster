# Quartermaster

Quartermaster is a Python-based agent system designed to analyze financial data, generate forecasts, assess risk, and make automated decisions. It uses an agent graph workflow and a SQLite database to simulate financial reasoning.

---

## Project Structure

```bash
quartermaster/
├── graph/
│ └── agent_graph.py # Defines the agent workflow and logic
├── tools/
│ └── sql_tool.py # Helper functions for running SQL queries
├── logs/
│ └── run_logs.txt # Execution logs
├── main.py # Entry point for running the agent
├── setup_db.py # Initializes and seeds the database
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```


---

## What the Program Does

When you run `main.py`, the Quartermaster Agent:

1. Initializes a shared state object
2. Passes the state through an agent graph
3. Collects:
   - Financial data
   - Forecasted final balance
   - Risk level
   - Decision
   - Action result
4. Prints a clear summary of the final output

This structure makes it easy to later replace test values with real financial data.

---

## Setup Instructions

### 1. Create a Virtual Environment  
**(Only run once per session)**

```bash
python3 -m venv venv
```

Activate it:

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Initialize the Database

This creates and prepares the SQLite database used by the agent.

```bash
python setup_db.py
Running the Program
```

To execute the Quartermaster Agent and view the output:

```bash
python main.py
```

The output includes:

- Financial data loaded from the database
- Forecasted final balance
- Risk assessment
- The agent’s decision
- The result of that decision
- Logs

Execution logs are saved to:

```bash
logs/run_logs.txt
```

These logs are useful for debugging and tracking agent behavior.

**Debugging (Optional)**

To directly view the database contents, uncomment this line in main.py:

```bash
print(run_sql("SELECT * FROM finances;"))
```

**Notes**

- Current financial values are test values only.
- Designed to be modular and easy to extend.
- Additional agents or logic can be added to the graph workflow.

**Requirements**

- Python 3.9+
- SQLite (included with Python)
- See requirements.txt for required packages.

## Evaluation

The project includes an evaluation script that tests whether the Quartermaster system is working correctly.

The evaluation checks:
- If the agent runs without crashing
- If all required outputs are returned
- If results are consistent across runs
- If the database is accessible and returning data

---

## Running the Evaluation

Make sure your virtual environment is activated and the database has been set up first:

```bash
python setup_db.py
```

Then run the evaluation script:

```bash
python evaluate.py
```

**What You Should See**

When the evaluation runs, it will step through each test:

Runs the agent graph
Checks required output fields
Compares results for consistency
Tests database access

At the end, you will see:

```bash
Evaluation complete: ALL TESTS PASSED ✅
```

Or you will see messages showing which step failed.

**Notes**

- The evaluation uses test data from the database.
- It is meant for debugging and verification, not production use
- If a test fails, check terminal output for the exact step that failed