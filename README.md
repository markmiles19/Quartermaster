# Quartermaster

Quartermaster is a Python-based agent system designed to analyze financial data, generate forecasts, assess risk, and make automated decisions. It uses an agent graph workflow and a SQLite database to simulate financial reasoning.

---

## Project Structure


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

Activate it:

macOS / Linux

source venv/bin/activate

Windows

venv\Scripts\activate
2. Install Dependencies
pip install -r requirements.txt
3. Initialize the Database

This creates and prepares the SQLite database used by the agent.

python setup_db.py
Running the Program

To execute the Quartermaster Agent and view the output:

python main.py

The output includes:

Financial data loaded from the database
Forecasted final balance
Risk assessment
The agent’s decision
The result of that decision
Logs

Execution logs are saved to:

logs/run_logs.txt

These logs are useful for debugging and tracking agent behavior.

Debugging (Optional)

To directly view the database contents, uncomment this line in main.py:

print(run_sql("SELECT * FROM finances;"))
Notes
Current financial values are test values only
Designed to be modular and easy to extend
Additional agents or logic can be added to the graph workflow
Requirements
Python 3.9+
SQLite (included with Python)
See requirements.txt for required packages
