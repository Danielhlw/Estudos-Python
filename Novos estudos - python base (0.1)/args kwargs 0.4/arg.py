def produto_total (*numeros):
    resultado = 1
    for i in numeros:
        resultado *= i
    return resultado
   
num = produto_total(5,4)

print(f"O produto total da operação é: {num}")