total = 0

while True:
    n = input("Digite um número (ou n para sair): ")
    if n == "n":
        break
    try:
        total += float(n)
        print(f"Total acumulado: {total}")
    except ValueError:
        print("Por favor, digite um número válido ou 'n' para sair.")