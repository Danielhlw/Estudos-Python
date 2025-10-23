# Append adiciona, se for "w", ele vai sobrescrever o arquivo todo!

with open ("dados.txt", "a") as arquivo:
    arquivo.write("adicionando linha\n")

with open ("dados.txt", "r") as arquivo:
    print(arquivo.read())