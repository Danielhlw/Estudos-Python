def media_filtrada (*args):
    soma = 0
    contador = 0
    for i in args:
        if i > 0:
            soma += i
            contador += 1
        else:
            print (f"Valor {i} é negativo, não entrará na média.")
    if contador == 0:
        return 0
    return soma / contador


media = media_filtrada(2,3,4,5, -2, -3, -5)

print(f"A média disso é: {media}")

