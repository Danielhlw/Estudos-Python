import os

arquivo = "usuarios.json"

if os.path.exists(arquivo):
    print("O arquivo existe!")
else:
    print("Arquivo não encontrado.")


