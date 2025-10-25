def main():

    mapa = carrega_mapa()
    fim = False
    pontos = 0
    total = total_pontos(mapa)
    print("Batalha Naval")
    print("Você pode fazer até %d pontos\n"%total)

    print("Digite as coordenadas separadas por virgula")
    while not fim:
        x, y = input("Digite x y (-1,-1 para terminar): ").split(',')
        x, y = int(x), int(y)
        print("Voce jogou em: %d,%d"%(x,y))
        if (x,y) == (-1,-1):
            fim = True
        elif (x,y) in mapa and mapa[x,y] > 0:
            valor = mapa[x,y]
            print("Voce acertou uma embarcacao e fez %d pontos"%valor)
            pontos += valor
            mapa[x,y] = 0
            if total_pontos( mapa ) == 0:
                fim = True
        else:
            print("Agua!!")

    print("Voce fez %d pontos"%pontos)

#----------------------------------------------------
def total_pontos(dic):
    ''' (dict) -> int '''
    soma = 0
    for i in dic:
        soma += dic[i]
    return soma

#----------------------------------------------------
def carrega_mapa():
    return {(2,5):100, (20,60):30, (21,60):30, (42,71):20, (43,71):20, (44,71):20, (45,71):20, (20,12):20, (21,12):20, (50,21):70}

#----------------------------------------------------
main()