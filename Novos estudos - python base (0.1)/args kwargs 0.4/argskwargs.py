def montar_pc(*componentes, **configs):
    print('Componentes: ')
    for componente in componentes:
        print(f' - {componente}')
    print("Configuração: ")
    for chave, valor in configs.items():
        print(f'{chave} - {valor}')


montar_pc("Placa-mãe", "SSD", "RAM", processador="Ryzen 5", ram="16GB")
