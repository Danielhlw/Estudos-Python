from pathlib import Path

# filtrar arquivos dentro de uma pasta

pasta = Path("meus_dados")


for item in pasta.glob("*.txt"):
    print(item)
