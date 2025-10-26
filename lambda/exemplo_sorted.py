produtos = [
    {'nome': 'Laptop', 'preco': 3500},
    {'nome': 'Mouse', 'preco': 50},
    {'nome': 'Teclado', 'preco': 150}
]

produtos_ordenados = sorted(produtos, key=lambda item: item['preco'])
print(produtos_ordenados)