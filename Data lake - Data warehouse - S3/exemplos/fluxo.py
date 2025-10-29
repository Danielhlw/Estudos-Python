import pyspark as spark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum


# 1. Bronze > leitura
df_bronze = spark.read.csv("s3://empresa/bronze/vendas.csv", header=True, inferSchema=True)

# 2. Silver > limpeza e transformação
df_silver = df_bronze.filter(col("valor_total") > 0).dropDuplicates(["id_venda"])

# 3. Gold > agregação final
df_gold = df_silver.groupBy("loja").agg(_sum("valor_total").alias("faturamento"))

# 4. Escrita final
df_gold.write.mode("overwrite").parquet("s3://empresa/gold/faturamento_por_loja.parquet")
