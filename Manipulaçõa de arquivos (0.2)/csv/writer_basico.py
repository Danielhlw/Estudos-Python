import csv

with open ("dados.csv", "w") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Carlos", 29, "Recifer"])