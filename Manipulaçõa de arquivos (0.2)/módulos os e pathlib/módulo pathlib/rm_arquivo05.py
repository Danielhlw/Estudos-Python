from pathlib import Path

pasta = Path("meus_dados")
arquivo = Path("meus_dados/arquivo.txt")

arquivo.unlink() # remove o arquivo
pasta.rmdir() # # remove a pasta (se estiver vazia)
 
