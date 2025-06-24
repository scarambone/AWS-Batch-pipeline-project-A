
# 📦 Project: Batch Data Pipeline on AWS with PySpark

## 📌 Overview

This project showcases a complete batch data processing pipeline built entirely on **AWS**, using **Apache Spark on Amazon EMR** for scalable transformations. It simulates a realistic enterprise scenario in which raw sales data is ingested, transformed, stored in optimized formats, cataloged, and queried — all within the AWS ecosystem.

## 🎯 Goals

- Ingest raw CSV data from **Amazon S3**
- Process and transform the data using **PySpark on Amazon EMR**
- Filter high-value transactions (≥ 300)
- Add a classification column (`high` or `low`) based on purchase amount
- Store the output in **Parquet format** back to S3
- Catalog the transformed dataset with **AWS Glue**
- Enable serverless SQL analytics using **Amazon Athena**

## 🧱 Architecture

```
S3 (raw data)
   ↓
Amazon EMR (PySpark job)
   ↓
S3 (processed Parquet files)
   ↓
AWS Glue Crawler → Glue Catalog
   ↓
Amazon Athena (SQL queries)
```

## 🛠️ Technologies Used

- **Amazon S3** – Data lake storage
- **Amazon EMR** – Managed Spark cluster
- **PySpark** – Batch transformation logic
- **AWS Glue** – Schema discovery and data cataloging
- **Amazon Athena** – Serverless querying engine

## 📊 Dataset Example

Sample sales dataset containing:
- `order_id`, `customer_id`, `order_date`, `total_amount`
- Derived column: `amount_category` (`high` if ≥ 300, else `low`)

## ✅ Project Outcome

- Built a functional batch ETL pipeline using AWS services
- Processed raw CSV files and outputted clean Parquet datasets
- Registered processed data in the AWS Glue Catalog
- Verified the pipeline by querying transformed data using Athena
