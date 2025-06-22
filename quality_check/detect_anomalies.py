import os
import pandas as pd
from datetime import datetime

# Set base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

INPUT_FILE = os.path.join(ROOT_DIR, "metadata_logs", "cleaned_sales.csv")
ANOMALIES_FILE = os.path.join(ROOT_DIR, "metadata_logs", "anomalies.csv")
CLEANED_OUTPUT = os.path.join(ROOT_DIR, "metadata_logs", "qa_cleaned_sales.csv")
LOG_FILE = os.path.join(ROOT_DIR, "metadata_logs", "quality_log.csv")

def log_quality(status, message=""):
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "job_name": "detect_anomalies",
        "status": status,
        "message": message
    }

    df_log = pd.DataFrame([log_entry])
    if not os.path.exists(LOG_FILE):
        df_log.to_csv(LOG_FILE, index=False)
    else:
        df_log.to_csv(LOG_FILE, mode='a', index=False, header=False)

# Main process
try:
    df = pd.read_csv(INPUT_FILE)

    # Conditions for anomalies
    is_invalid_amount = (df['amount'] < 1) | (df['amount'] > 100000)
    is_null = df.isnull().any(axis=1)
    is_duplicate = df.duplicated()

    anomalies = df[is_invalid_amount | is_null | is_duplicate]
    df_cleaned = df.drop(anomalies.index)

    # Save files
    anomalies.to_csv(ANOMALIES_FILE, index=False)
    df_cleaned.to_csv(CLEANED_OUTPUT, index=False)

    print("✅ Quality check completed.")
    print(f"❗ Anomalies detected: {len(anomalies)} rows")
    print(f"✅ Clean data saved as: qa_cleaned_sales.csv")
    log_quality("success", f"{len(anomalies)} anomalies removed")

except Exception as e:
    print("❌ Quality check failed:", str(e))
    log_quality("failure", str(e))
