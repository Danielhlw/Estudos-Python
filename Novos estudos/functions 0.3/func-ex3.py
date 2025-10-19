def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
number = int(input("Digite o número para saber se é ou não par: "))

if eh_par(number):
    print(f"Número {number} é par!")
else:
    print(f"Número {number} é impar!")