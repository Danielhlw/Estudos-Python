import csv

with open("dados.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(f"{linha['nome']} tem {linha['idade']} anos e mora em {linha['cidade']}.")
