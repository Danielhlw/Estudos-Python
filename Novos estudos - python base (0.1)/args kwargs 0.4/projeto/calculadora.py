def calculadora(*numeros, **opcoes):
    if not numeros:
        return "Nenhum número fornecido"
    
    operacao = opcoes.get("operacao", "soma")

    resultado = numeros[0]

    if operacao == 'soma':
        for n in numeros[1:]:
            resultado += n
    elif operacao == 'subtracao':
        for n in numeros[1:]:
            resultado -= n 


    elif operacao == "multiplicacao":
        for n in numeros[1:]:
            resultado *= n

    elif operacao == "divisao":
        for n in numeros[1:]:
            if n == 0:
                return "Erro: divisão por zero!"
            resultado /= n

    else:
        return f"Operação '{operacao}' não reconhecida."

    return resultado