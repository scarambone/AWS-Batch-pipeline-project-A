from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col

spark = SparkSession.builder.appName("SalesDataTransformation").getOrCreate()

# Caminho de entrada e saída
input_path = "s3://alexandre-batch-pipeline/raw/sales_data.csv"
output_path = "s3://alexandre-batch-pipeline/processed/"

# Ler CSV
df = spark.read.option("header", "true").csv(input_path)

# Converter total_amount para float
df = df.withColumn("total_amount", col("total_amount").cast("double"))

# Adicionar classificação de valor
df = df.withColumn(
    "amount_category",
    when(col("total_amount") >= 300, "high").otherwise("low")
)

# Filtrar apenas vendas com total >= 300
df_filtered = df.filter(col("total_amount") >= 300)

# Gravar como Parquet
df_filtered.write.mode("overwrite").parquet(output_path)

spark.stop()
