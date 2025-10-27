from pyspark.sql import SparkSession
import pandas as pd

spark = SparkSession.builder.appName("LeituraEscritaArquivos").getOrCreate()

# Lendo um arquivo CSV com cabeçalho
df_csv = spark.read.csv("bibliotecas para dados (0.3)/pyspark/introdução/dados/vendas.csv", header=True, inferSchema=True)
df_csv.show(5)
df_csv.printSchema()

df_json = spark.read.json("bibliotecas para dados (0.3)/pyspark/introdução/dados/clientes.json", multiLine=True)
df_json.show(5)
df_json.printSchema()

# Tratamento de dados faltantes com Pandas (aqui, após conectar com o spark.
# mas dá para fazer o tratamento diretamente no pyspark, usando df_son.na.drop() etc)
df = df_json.toPandas()
print(df.isna().sum())
df.dropna(inplace=True)
print(df.head())
