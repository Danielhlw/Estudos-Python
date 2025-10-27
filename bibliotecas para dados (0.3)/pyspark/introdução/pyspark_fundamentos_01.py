from pyspark.sql import SparkSession

# Cria a sessão principal do Spark
spark = SparkSession.builder \
    .appName("ExemploFundamentos") \
    .getOrCreate()

# Criação de um DataFrame
dados = [
    ("Ana", 25, 4500),
    ("Bruno", 32, 5200),
    ("Carla", 28, 4800),
    ("Daniel", 22, 3900),
    ("Eduardo", 40, 6100)
]

colunas = ["nome", "idade", "salario"]

df = spark.createDataFrame(dados, colunas)
df.show()

# Operações básicas
df.printSchema()
df.select("nome").show()
df.filter(df.idade > 30).show()
df.groupBy("idade").count().show()
df.orderBy(df.salario.desc()).show()
