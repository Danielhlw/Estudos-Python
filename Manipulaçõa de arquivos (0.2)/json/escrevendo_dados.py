import json

dados = {
    "nome": "Daniel",
    "idade": 22,
    "cursos": ["Python", "SQL"],
    "endereco": {
        "cidade": "São Paulo",
        "estado": "SP"
    },
    "ativo": True
}

with open("dados_novos.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)