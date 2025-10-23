import json

alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 7.0},
    {"nome": "Carlos", "nota": 9.2}
]

# salvando arquivo
with open ("alunos.json", "w", encoding="utf-8") as arquivo:
    json.dump(alunos, arquivo, indent=4, ensure_ascii=False)

# lendo arquivo
with open ("alunos.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

for aluno in dados:
    print(f"O aluno {aluno['nome']} tirou nota {aluno['nota']}.")