def estoque_total (**kwargs):
    numeros = 0
    for chave, valor in kwargs.items():
        print(f'item: {chave}')

    for chave, valor in kwargs.items():
        print(f"item: {chave}, {valor}")
        numeros += valor
    return numeros
    
print(estoque_total(camisetas=10, canecas=5, chaveiros=20))
