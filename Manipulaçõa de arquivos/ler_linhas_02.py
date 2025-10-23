with open ("dados.txt", "r") as arquivo:
    for linha in arquivo:
        print(f"Linha: {linha.strip()}")