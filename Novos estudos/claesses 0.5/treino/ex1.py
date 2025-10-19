class Pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self):
        print(f"olá, meu nome é {self.nome} e tenho {self.idade}")

p1 = Pessoa("Daniel", 22)

p1.falar()