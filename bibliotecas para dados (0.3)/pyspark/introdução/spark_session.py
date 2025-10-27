from pyspark.sql import SparkSession

# Criação da sessão principal do Spark
spark = SparkSession.builder \
    .appName("Exemplo") \
    .getOrCreate()

# Exibe a versão do Spark
print(spark.version)