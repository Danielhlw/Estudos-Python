ler_arquivo = input("Digite o arquivo a ser lido: ")

try:
    with open (ler_arquivo, "r") as arquivo:
        print(arquivo.read())
except FileNotFoundError:
    print(f"Erro: O arquivo '{ler_arquivo}' não foi encontrado.")
