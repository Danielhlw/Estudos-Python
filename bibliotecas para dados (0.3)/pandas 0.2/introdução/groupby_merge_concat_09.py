import pandas as pd

# DataFrame base
vendas = pd.DataFrame({
    "vendedor": ["Ana", "Bruno", "Ana", "Daniel", "Bruno", "Ana"],
    "loja": ["Assis", "Assis", "São Paulo", "Assis", "São Paulo", "Curitiba"],
    "valor": [500, 700, 1200, 400, 950, 800]
})

print("Tabela original de vendas: ")
print(vendas)

# Agrupamento simples por vendedor
# “Pegue a coluna valor e separe-a por vendedor.”
agrupado = vendas.groupby("vendedor")["valor"].sum()
print("\nTotal de vendas por vendedor: ")
print(agrupado)

# Agrupamento múltiplo: vendedor e loja
agrupado_multi = vendas.groupby(["vendedor", "loja"])["valor"].sum().reset_index()
print("\nTotal de vendas por vendedor e loja:")
print(agrupado_multi)

# Múltiplas agregações: soma, média e máximo por loja
print("\nMúltiplas agregações por loja:")
lojita = vendas.groupby("loja")["valor"].agg(["sum", "mean", "max"])
print (lojita)