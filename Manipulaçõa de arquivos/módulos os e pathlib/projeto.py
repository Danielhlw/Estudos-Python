from pathlib import Path
import json
from datetime import datetime

# 1 - criação da pasta de trabalho
BASE = Path("data_pipeline")
LOG = BASE / "pipeline.log"
BASE.mkdir(exist_ok=True)

def log(msg):
    # Função simples para registrar eventos no arquivo de log
    hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with LOG.open("a", encoding="utf-8") as f:
        f.write(f"[{hora}] {msg}\n")
    print(f"[LOG] {msg}")  

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

log(f"Novo arquivo salvo: {arquivo_saida.name} ({len(usuarios)} registros)")

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
        log(f"Arquivo carregado com sucesso: {mais_recente.name}")
        print(f"registros: {len(dados)}")
        print("amostra (nome > cidade):")
        for u in dados[:3]:
            print(f" • {u['nome']} → {u['cidade']}")
    except json.JSONDecodeError as e:
        log(f"Erro ao ler JSON ({mais_recente.name}): {e}")
else:
    log("Nenhum arquivo JSON encontrado na pasta.")