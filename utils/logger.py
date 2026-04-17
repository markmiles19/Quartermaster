import os
from datetime import datetime

LOG_FILE = "logs/run_logs.txt"

def log_step(step: str, data):
    os.makedirs("logs", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {step}: {data}\n")