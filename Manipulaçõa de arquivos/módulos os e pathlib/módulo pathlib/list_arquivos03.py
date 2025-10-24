from pathlib import Path

# listar arquivos dentro de uma pasta

pasta = Path("meus_dados")
for item in pasta.iterdir():
    print(item)

