# fatiar e filtrar arrays

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(arr)

print(arr[0:3])  # primeiros 3 elementos (0, 1, 2)
print(arr[3:])   # do 4º até o final
print(arr[:5])  # do início até o 5º elemento
print(arr[-3:])  # últimos 3 elementos

print("----------- Filtrando com condicionais ------------ ")

print(arr[arr > 40]) # elementos maiores que 40
print(arr[(arr > 30) & (arr < 70)]) # elementos entre 30 e 70
arr[arr < 50] = 0 # substitui elementos menores que 50 por 0
print(arr) 

