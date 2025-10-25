import json

with open ("dados.json", "r") as arquivo:
    dados = json.load(arquivo)

print(dados)
print(dados["nome"])
print(dados["endereco"]["cidade"])