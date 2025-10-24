import os
import shutil # para deletar pasta com conteúdo (shutil.rmtree("pasta"))

os.remove("dados_usuarios.json")  # remove arquivo
os.rmdir("meus_dados")            # remove pasta (vazia)

