def calcular_idade(ano_nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade_atual = ano_atual - ano_nascimento
    print (f"Você tem {idade_atual} anos")

calcular_idade(2003)