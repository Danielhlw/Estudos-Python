from pathlib import Path

# criar arquivos dentro de uma pasta

arquivo = Path("meus_dados/arquivo.txt")
arquivo.write_text("Linha de teste do arquivo\n")

texto = arquivo.read_text()
print(texto)

