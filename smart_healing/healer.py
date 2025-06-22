import os
import pandas as pd
from datetime import datetime

# Base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

INPUT_FILE = os.path.join(ROOT_DIR, "metadata_logs", "qa_cleaned_sales.csv")
HEALED_FILE = os.path.join(ROOT_DIR, "metadata_logs", "healed_sales.csv")
LOG_FILE = os.path.join(ROOT_DIR, "metadata_logs", "healing_log.csv")

def log_healing(status, message=""):
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "job_name": "healer",
        "status": status,
        "message": message
    }

    df_log = pd.DataFrame([log_entry])
    if not os.path.exists(LOG_FILE):
        df_log.to_csv(LOG_FILE, index=False)
    else:
        df_log.to_csv(LOG_FILE, mode='a', index=False, header=False)

try:
    df = pd.read_csv(INPUT_FILE)

    # Healing Rule 1: Fill missing amounts with mean
    if df['amount'].isnull().any():
        mean_amount = df['amount'].mean()
        df['amount'] = df['amount'].fillna(mean_amount)

    # Healing Rule 2: Cap very high amounts to 100000
    df['amount'] = df['amount'].apply(lambda x: 100000 if x > 100000 else x)

    # Healing Rule 3 (Optional): Round all amounts
    df['amount'] = df['amount'].round(2)

    df.to_csv(HEALED_FILE, index=False)
    print("✅ Healing successful.")
    log_healing("success", "Data healed and saved.")

except Exception as e:
    print("❌ Healing failed:", str(e))
    log_healing("failure", str(e))
