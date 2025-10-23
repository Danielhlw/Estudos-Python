import json

try:
    with open("usuarios.json", "r", encoding="utf-8") as arquivo:
        usuarios = json.load(arquivo)
except FileNotFoundError:
    usuarios = []

usuarios.append({"id": 5, "nome": "Carlos", "idade": 35, "cidade": "Campinas"})

with open("usuarios.json", "w", encoding="utf-8") as arquivo:
    json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)
