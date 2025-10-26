import pandas as pd

# map() e filter() com listas puras

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

dobrados = list(map(lambda x: x * 2, numeros))
print("Dobro dos números:", dobrados)

pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", pares)

dobrados_pares = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numeros)))
print("Dobro dos números pares:", dobrados_pares)

# map() e filter() no Pandas

df = pd.DataFrame({
    "nome": ["Ana", "Bruno", "Carla", "Daniel"],
    "idade": [25, 32, 28, 22],
    "salario": [4500, 5200, 4800, 3900]
})

print("\nDataFrame original:")
print(df)

df["salario_dobrado"] = df["salario"].map(lambda s: s * 2)
print("\nColuna 'salario_dobrado' criada com map():")
print(df)

df_filtrado = df[df["idade"] > 25]
print("\nDataFrame filtrado (idade > 25):")
print(df_filtrado)


# apply() — múltiplas colunas

df["descricao"] = df.apply(
    lambda x: f"{x['nome']} tem {x['idade']} anos e ganha R${x['salario']}",
    axis=1
)
print("\nNova coluna 'descricao' criada com apply():")
print(df)

df["categoria"] = df.apply(
    lambda x: "Alto" if x["salario"] > 5000 and x["idade"] > 30 else "Médio",
    axis=1
)

print(df)