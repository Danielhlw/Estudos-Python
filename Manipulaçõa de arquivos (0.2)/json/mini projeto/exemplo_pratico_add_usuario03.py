import json

with open ("usuarios.json", "r") as arquivo:
    dados = json.load(arquivo)

novo_usuario = {"id": 4, "nome": "Ana", "idade": 28, "cidade": "Recife"}

# append nos dados virtualmente
dados.append(novo_usuario)

# escrita dos dados no json

with open ("usuarios.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)

# visualização do dado...
for dado in dados:
    print(f"{dado}")
