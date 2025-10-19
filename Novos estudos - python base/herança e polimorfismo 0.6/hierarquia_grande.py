class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Funcionario(Pessoa):
    def trabalhar(self):
        print(f"{self.nome} está trabalhando.")

class Gerente(Funcionario):
    def trabalhar(self):
        print(f"{self.nome} está gerenciando a equipe.")


p1 = Funcionario("João")
p2 = Gerente("Maria")