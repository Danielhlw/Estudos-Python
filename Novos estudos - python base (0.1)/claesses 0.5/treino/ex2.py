# Atribuo de classe

class Aluno:
    escola = "Escola municipal"

    def __init__(self, nome, serie):
        self.nome = nome
        self.serie = serie

    def info(self):
        print(f"O nome do aluno é {self.nome}. A sua série é: {self.serie}")

print(Aluno.escola)

p1 = Aluno("Daniel", 3)

p1.info()