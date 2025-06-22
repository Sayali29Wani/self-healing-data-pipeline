import pandas as pd
import os
from datetime import datetime

# File paths
RAW_PATH = "../data/sales_data.csv"
STAGING_PATH = "../metadata_logs/staging_sales.csv"
LOG_PATH = "../metadata_logs/ingestion_log.csv"

# Function to log job status
def log_ingestion(status, message=""):
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "job_name": "ingest_sales",
        "status": status,
        "message": message
    }

    df_log = pd.DataFrame([log_entry])
    if not os.path.exists(LOG_PATH):
        df_log.to_csv(LOG_PATH, index=False)
    else:
        df_log.to_csv(LOG_PATH, mode='a', index=False, header=False)

# Try reading and saving the file
try:
    df = pd.read_csv(RAW_PATH)
    df.to_csv(STAGING_PATH, index=False)
    print("✅ Ingestion successful.")
    log_ingestion("success")
except Exception as e:
    print("❌ Ingestion failed:", str(e))
    log_ingestion("failure", str(e))
