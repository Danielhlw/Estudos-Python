import numpy as np

matriz = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matriz)

print("# --------------------------------------------------- #")

print(matriz.shape)  # 2 linhas, 3 colunas

print("# --------------------------------------------------- #")

print(matriz[0, 1])  # elemento linha 0, coluna 1 > 2

print("# --------------------------------------------------- #")

print(matriz[:, 2])  # todos os elementos da coluna 2 > [3 6]

print("# --------------------------------------------------- #")
