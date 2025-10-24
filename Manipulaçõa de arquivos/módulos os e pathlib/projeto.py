from pathlib import Path
import json
from datetime import datetime

# 1 - criação da pasta de trabalho
BASE = Path("data_pipeline")
BASE.mkdir(exist_ok=True)

# 2 - dataset + timestamp 
usuarios = [
    {"id": 1, "nome": "Daniel", "idade": 22, "cidade": "Maceió"},
    {"id": 2, "nome": "Maria", "idade": 25, "cidade": "São Paulo"},
    {"id": 3, "nome": "João",  "idade": 30, "cidade": "Curitiba"},
]

# salvando com a variavel timstamp, (ano, mes, dia, hora, minuto, segundo...
# que fica  gravado no corpo do arquivo) 
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
arquivo_saida = BASE / f"usuarios_{timestamp}.json"

with arquivo_saida.open("w", encoding="utf-8") as f:
    json.dump(usuarios, f, indent=4, ensure_ascii=False)
print(f"salvo: {arquivo_saida}")

# 3 - listar arquivos JSON da pasta (ordenados por nome/tempo)
jsons = sorted(BASE.glob("usuarios_*.json"))
print("\n arquivos na pasta:")
for p in jsons:
    print(" -", p.name)

# 4 - carregar o arquivo mais recente e mostrar um resumo
if jsons:
    mais_recente = jsons[-1]
    try:
        with mais_recente.open("r", encoding="utf-8") as f:
            dados = json.load(f)
        print(f"\n carregado: {mais_recente.name}")
        print(f"registros: {len(dados)}")
        print("amostra (nome > cidade):")
        for u in dados[:3]:
            print(f" • {u['nome']} → {u['cidade']}")
    except json.JSONDecodeError as e:
        print("JSON inválido:", e)
else:
    print("nenhum arquivo JSON encontrado em", BASE)
