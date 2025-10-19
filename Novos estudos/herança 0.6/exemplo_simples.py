# Classe pai
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Classe filha
class Aluno(Pessoa):
    def estudar(self):
        print(f"{self.nome} está estudando!")
