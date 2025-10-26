# soma de matrizes
import numpy as np 

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

b = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

print(a+b) # soma elemento a elemento
print(a*b) # multiplicação elemento a elemento
print(a.dot(b)) # produto matricial
print(a.sum()) # soma todos os elementos da matriz
print(a.sum(axis=0)) # soma por colunas
print(a.sum(axis=1)) # soma por linhas
