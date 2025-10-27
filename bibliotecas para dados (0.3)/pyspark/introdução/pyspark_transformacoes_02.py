from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Criação da sessão
spark = SparkSession.builder.appName("Transformacoes").getOrCreate()

# DataFrame base
dados = [
    ("Ana", 25, 4500),
    ("Bruno", 32, 5200),
    ("Carla", 28, 4800),
    ("Daniel", 22, 3900),
    ("Eduardo", 40, 6100)
]
colunas = ["nome", "idade", "salario"]
df = spark.createDataFrame(dados, colunas)

# Seleção e renomeação
df.select(col("nome").alias("funcionario"), col("salario").alias("renda")).show()

# Criação de colunas derivadas
df = df.withColumn("bonus", df["salario"] * 0.10)
df = df.withColumn("salario_total", df["salario"] + col("bonus"))

# Condicionais com when
df = df.withColumn(
    "categoria_idade",
    when(df.idade < 25, "Jovem")
    .when(df.idade < 35, "Adulto")
    .otherwise("Sênior")
)

# Visualização final
df.show()

# Agregações
df.groupBy("categoria_idade").agg(
    avg("salario").alias("media_salario"),
    avg("bonus").alias("media_bonus")
).show()
