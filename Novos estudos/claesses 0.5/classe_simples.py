class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def saudacao(self):
        print(f"Saudações, {self.nome}, você tem {self.idade}")

p1 = Pessoa("Daniel", 22)
p1.saudacao()