import pandas as pd

# Criar um DataFrame com dicionário
dados = {
    "nome": ["Ana", "Bruno", "Carla", "Daniel"],
    "idade": [25, 32, 28, 22],
    "cidade": ["Assis", "São Paulo", "Curitiba", "Recife"]
}

df = pd.DataFrame(dados)

# Exibir a tabela completa
print(df)

# Mostrar informações básicas
print("\nFormato (linhas, colunas):", df.shape)
print("Colunas:", df.columns)
print("Tipos de dados:")
print(df.dtypes)
print("\nResumo estatístico:")
print(df.describe()) # Describe é um dos métodos mais utilizados e úteis

# Acessar colunas
print("\nColuna idade:")
print(df["idade"])

# Acessar mais de uma coluna
print("\nNome e cidade:")
print(df[["nome", "cidade"]])

# Acessar uma linha específica
print("\nLinha 0 (primeira):")
print(df.loc[0])

# Intervalo de linhas
print("\nLinhas 1 e 2:")
print(df.iloc[1:3])