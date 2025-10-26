import pandas as pd

# Construção do DataFrame inicial
dados = {
    "nome": ["Ana", "Bruno", "Carla", "Daniel"],
    "idade": [25, 32, 28, 22],
    "salario": [4500, 5200, 4800, 3900]
}

df = pd.DataFrame(dados)
print(df)

# Adicionando nova coluna fixa
df["setor"] = ["RH", "TI", "Design", "TI"]
print("\nDataFrame com nova coluna 'setor':")
print(df)

# Adicionando nova coluna derivada (a partir de outra)
df["bonus"] = df["salario"] * 0.1
print("\nDataFrame com coluna 'bonus' calculada:")
print(df)

# Atualizando valores de uma coluna específica
df.loc[df["setor"] == "TI", "bonus"] = df["salario"] * 0.15
print("\nBonus atualizado para o setor de TI:")
print(df)

# Removendo colunas
df = df.drop("idade", axis=1)
print("\nDataFrame após remover a coluna 'idade':")
print(df)

# Renomeando colunas
df = df.rename(columns={"nome": "colaborador", "salario": "renda"})
print("\nDataFrame com colunas renomeadas:")
print(df)