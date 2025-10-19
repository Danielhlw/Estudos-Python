class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)   # chama o construtor da classe Pai
        self.matricula = matricula      # adiciona algo novo

    def apresentar(self):
        super().apresentar()            # chama o método original
        print(f"Sou aluno com matrícula {self.matricula}.")


a1 = Aluno("Daniel", 22, "A123")
a1.apresentar()