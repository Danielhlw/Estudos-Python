from pathlib import Path

# criar um caminho

caminho = Path("meus_dados")
caminho.mkdir(exist_ok=True)

print(caminho.exists())