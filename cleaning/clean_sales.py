import os
import pandas as pd
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

STAGING_PATH = os.path.join(ROOT_DIR, "metadata_logs", "staging_sales.csv")
CLEANED_PATH = os.path.join(ROOT_DIR, "metadata_logs", "cleaned_sales.csv")
LOG_PATH = os.path.join(ROOT_DIR, "metadata_logs", "cleaning_log.csv")

def log_cleaning(status, message=""):
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "job_name": "clean_sales",
        "status": status,
        "message": message
    }

    df_log = pd.DataFrame([log_entry])
    if not os.path.exists(LOG_PATH):
        df_log.to_csv(LOG_PATH, index=False)
    else:
        df_log.to_csv(LOG_PATH, mode='a', index=False, header=False)

try:
    df = pd.read_csv(STAGING_PATH)
    df_cleaned = df[(df['amount'] > 0) & (~df['amount'].isnull())]
    df_cleaned.to_csv(CLEANED_PATH, index=False)
    print("✅ Cleaning successful.")
    log_cleaning("success")
except Exception as e:
    print("❌ Cleaning failed:", str(e))
    log_cleaning("failure", str(e))
