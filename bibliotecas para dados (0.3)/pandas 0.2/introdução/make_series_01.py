# introducao/make_series_01.py

import pandas as pd

# Criando uma Series a partir de uma lista (é uma series bem básica)
idades = pd.Series([22, 25, 30, 28, 35])

print("Series de idades:")
print(idades)

# Exibindo informações básicas
print("\nTipo de dados:", idades.dtype)
print("Quantidade de elementos:", idades.size)
print("Índices:", idades.index)
print("Média das idades:", idades.mean())

# Criando uma Series com índices personalizados
idades_nomes = pd.Series(
    [22, 25, 30, 28, 35],
    index=["Ana", "Bruno", "Carla", "Daniel", "Eduardo"]
)

print("\nSeries com nomes personalizados:")
print(idades_nomes)

# Acessando os valores
print("\nIdade de Daniel:", idades_nomes["Daniel"])
