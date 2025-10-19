def soma():
    x = input('Digite o primeiro número: ')
    y = input('Digite o segundo número: ')
    soma = int(x) + int(y)
    print(f'A soma de {x} + {y} é {soma}')

def subtracao():
    x = input('Digite o primeiro número: ')
    y = input('Digite o segundo número: ')
    subtracao = int(x) - int(y)
    print(f'A subtracao de {x} - {y} é {subtracao}')

def multiplicacao():
    x = input('Digite o primeiro número: ')
    y = input('Digite o segundo número: ')
    multiplicacao = float(x) * float(y)
    print(f'A multiplicação de {x} * {y} é {multiplicacao}')

def divisao():
    x = input('Digite o primeiro número: ')
    y = input('Digite o segundo número: ')
    divisao = int(x)/int(y)
    print(f'A divisão de {x} / {y} é {divisao}')

escolha=1

while escolha:
    print('0. Sair')
    print('1. Somar')
    print('2. Subtrair')
    print('3. Multiplicação')
    print('4. Divisao ')

    escolha = int(input('Opção: '))

    if(escolha==1):
        soma()
    if(escolha==2):
        subtracao()
    if(escolha==3):
        multiplicacao()
    if(escolha==4):
        divisao()