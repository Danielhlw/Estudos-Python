# Criar arquivo (simulação)
with open ("dados.txt", "w") as arquivo:
    arquivo.write("Olá, mundo!\n")
    arquivo.write("Arquivo base de manipulação de arquivos com python.\n")

# Ler conteúdo do arquivo
with open ("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

print("Arquivo fechado?", arquivo.closed)