import pandas as pd

# Construção do DataFrame 
dados = {
    "nome": ["Ana", "Bruno", "Carla", "Daniel", "Eduardo"],
    "idade": [25, 32, 28, 22, 40],
    "salario": [4500, 5200, 4800, 3900, 6100]
}
df = pd.DataFrame(dados)
print(df)

# Estatísticas básicas por coluna numérica 
print("\nMédia das idades:", df["idade"].mean())
print("Idade mínima:", df["idade"].min())
print("Idade máxima:", df["idade"].max())
print("Soma dos salários:", df["salario"].sum())
print("Média dos salários:", df["salario"].mean())

# Resumo descritivo das colunas numéricas 
print("\n Resumo estatístico completo:")
print(df.describe())

# Metadados rápidos (tamanho e nomes de colunas)
print("\n Quantidade de linhas:", len(df))
print("Colunas:", list(df.columns))

# Estatística em múltiplas colunas de uma vez ---
print("\n Média de idade e salário:")
print(df["salario"])
