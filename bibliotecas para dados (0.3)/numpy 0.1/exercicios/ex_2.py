# criar uma matriz 2x3 com os valores de 1 a 6

import numpy as np

matriz = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matriz)

print(matriz.shape)  # exibir o formato da matriz
print(matriz[0, 1])  # acessar o elemento na linha 1, coluna 2
print(matriz[1]) # acessar a segunda linha
print(matriz[1, 2]) # acessar o elemento na linha 2, coluna 3