import json

usuarios = [
    {"id": 1, "nome": "Daniel", "idade": 22, "cidade": "Assis"},
    {"id": 2, "nome": "Maria", "idade": 25, "cidade": "São Paulo"},
    {"id": 3, "nome": "João", "idade": 30, "cidade": "Curitiba"}
]

with open ("usuarios.json", "w", encoding="utf-8") as arquivo:
    json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)


# mostrando o dado cru
with open ("usuarios.json", "r") as arquivo: 
    dados = json.load(arquivo)
print(dados)

# mostrando o dado estético
for usuario in dados:
    print(f'{usuario["nome"]} mora em {usuario["cidade"]} e tem {usuario["idade"]} anos') 

