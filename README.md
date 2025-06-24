
# Batch Data Pipeline on AWS using PySpark

## About the Project

This is a hands-on data engineering project where I built a complete batch data processing pipeline using AWS services. The goal was to simulate a real-world scenario of ingesting, transforming, and analyzing sales data using scalable and cloud-native tools.

The pipeline reads raw CSV data stored in Amazon S3, processes it using a PySpark job running on Amazon EMR, and saves the cleaned data back to S3 in Parquet format. The transformed data is then cataloged with AWS Glue and made available for querying with Amazon Athena.

I developed this project to strengthen my practical skills with AWS and distributed data processing.

## Main Steps

- Load raw CSV data from S3
- Process and transform the data using PySpark on EMR
- Filter transactions with total amount greater than or equal to 300
- Add a new column to classify transaction amount as "high" or "low"
- Save the output as Parquet files in a separate S3 location
- Catalog the final dataset using Glue
- Query the results using Athena

## Tools and Services Used

- Amazon S3
- Amazon EMR (Spark)
- PySpark
- AWS Glue
- Amazon Athena

## Sample Output

The output is a Parquet dataset stored in S3, enriched with a new column `amount_category` and filtered to include only transactions above a certain threshold. This makes the data ready for analytics through SQL queries in Athena.

## Why I Did This

This project is part of my learning path in cloud-based data engineering. My focus was on practicing batch processing in a realistic setup, using the kind of tools that are commonly found in production environments.

