# 🛠️ Self-Healing Data Pipeline

A robust, modular pipeline designed to **ingest, clean, detect anomalies, and self-heal** corrupted sales data using Python and Pandas. Built to simulate real-world data engineering workflows with logging, quality checks, and automated healing mechanisms.

---

## 📌 Project Overview

This project demonstrates a **self-healing ETL pipeline** that:
- Ingests raw sales data from source
- Cleans and preprocesses it
- Detects anomalies (e.g., nulls, invalid formats)
- Attempts to automatically **heal the data**
- Maintains logs for **ingestion**, **cleaning**, **quality checks**, and **healing**

Perfect for showcasing **data engineering + automation skills**!

---

## ⚙️ Tech Stack

| Tool / Library     | Purpose                          |
|--------------------|----------------------------------|
| **Python**         | Core language                    |
| **Pandas**         | Data cleaning, transformation    |
| **VS Code**        | IDE                              |
| **Git & GitHub**   | Version control                  |
| **Jupyter Notebook** | Testing + development (optional) |
| **CSV Files**      | Simulated data source & output   |

---

## 🧠 Key Features

- ✅ Modular pipeline (Ingestion → Cleaning → QA → Healing)
- ✅ Logging for every stage in `metadata_logs/`
- ✅ Detection of missing values and invalid entries
- ✅ Auto-fix strategies for healing bad data
- ✅ Ready for deployment or extension with Snowflake/DBT integration

---

## 📂 Folder Structure

```bash
self-healing-data-pipeline/
│
├── ingestion/
│   └── ingest_sales.py
│
├── cleaning/
│   └── clean_sales.py
│
├── quality_check/
│   └── detect_anomalies.py
│
├── smart_healing/
│   └── healer.py
│
├── metadata_logs/
│   ├── ingestion_log.csv
│   ├── cleaning_log.csv
│   ├── quality_log.csv
│   ├── healing_log.csv
│   ├── staging_sales.csv
│   ├── qa_cleaned_sales.csv
│   └── healed_sales.csv
