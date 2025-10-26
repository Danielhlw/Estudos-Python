import pandas as pd

# Construção do DataFrame
dados = {
    "nome": ["Ana", "Bruno", "Carla", "Daniel", "Eduardo"],
    "idade": [25, 32, 28, 22, 40],
    "salario": [4500, 5200, 4800, 3900, 6100],
    "setor": ["RH", "TI", "Design", "TI", "Financeiro"]
}
df = pd.DataFrame(dados)

print(df)

# Filtragem simples
print("\nFuncionários com idade maior que 30:")
print(df[df["idade"] > 30])

# Filtragem composta com 'e' lógico (&)
print("\nFuncionários com idade maior que 25 E salário acima de 4500:")
print(df[(df["idade"] > 25) & (df["salario"] > 4500)])

print("\nFuncionários do setor de TI OU com salário acima de 6000:")
print(df[(df["setor"] == "TI") | (df["salario"] > 6000)])

print("\nFuncionários do setor de TI:")
print(df[(df["setor"] == "TI")])

# Atualização condicional (aumento de 10% para salários abaixo da média)
media_salario = df["salario"].mean()
df.loc[df["salario"] < media_salario, "salario"] *= 1.1

print("\nSalários atualizados para quem ganhava abaixo da média:")
print(df)
