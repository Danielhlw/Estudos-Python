import numpy as np

dados = np.array([10, 20, 30, 40, 50])

media = np.mean(dados)
mediana = np.median(dados)
desvio_padrao = np.std(dados)
print("Média:", media)
print("Mediana:", mediana)
print("Desvio Padrão:", desvio_padrao)