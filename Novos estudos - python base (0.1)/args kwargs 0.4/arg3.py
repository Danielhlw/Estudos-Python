def analisar_numeros (*args):
    if not args:
        return "Nenhum número fornecido"
    
    maior = max(args)
    menor = min(args) 
    soma_positivos = 0
    cont_positivos = 0
    cont_negativos = 0

    for i in args:
        if i > 0:
            soma_positivos += i
            cont_positivos += 1
        elif i < 0:
            cont_negativos += 1
        
    media_positivos = soma_positivos / cont_positivos if cont_positivos > 0 else 0

    return {
        "maior": maior,
        "menor": menor,
        "media_positivos": media_positivos,
        "negativos": cont_negativos
    }


resultado = analisar_numeros(10, -2, 5, 0, 8, -3)
print(resultado)