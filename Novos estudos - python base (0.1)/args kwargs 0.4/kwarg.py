def relatorio_aluno(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

relatorio_aluno(nome="Ana", idade=20, curso="Engenharia", nota_final=9.5)