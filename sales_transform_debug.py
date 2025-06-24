
from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col

spark = SparkSession.builder.appName("SalesDataTransformationDebug").getOrCreate()

input_path = "s3://alexandre-batch-pipeline/raw/sales_data.csv"
output_path = "s3://alexandre-batch-pipeline/processed/"

try:
    print("📥 Lendo arquivo CSV do S3...")
    df = spark.read.option("header", "true").csv(input_path)
    print("✅ Schema do DataFrame:")
    df.printSchema()

    print("🔍 Primeiras linhas do dataset:")
    df.show(5)

    print("🔄 Convertendo coluna 'total_amount' para double...")
    df = df.withColumn("total_amount", col("total_amount").cast("double"))

    print("📊 Adicionando coluna de classificação de valor...")
    df = df.withColumn(
        "amount_category",
        when(col("total_amount") >= 300, "high").otherwise("low")
    )

    print("🔎 Filtrando vendas com total_amount >= 300...")
    df_filtered = df.filter(col("total_amount") >= 300)

    print("💾 Gravando saída como Parquet no S3...")
    df_filtered.write.mode("overwrite").parquet(output_path)

    print("✅ Job finalizado com sucesso!")

except Exception as e:
    print("❌ Erro durante a execução do job:", str(e))

spark.stop()
