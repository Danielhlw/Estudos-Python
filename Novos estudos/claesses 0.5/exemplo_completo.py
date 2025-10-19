class Pessoa:
    especie = "Humano"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, sou {self.nome} e tenho {self.idade} anos. Sou um {self.especie}.")

    @classmethod
    def mudar_especie(cls, nova_especie):
        cls.especie = nova_especie

    @staticmethod
    def e_adulto(idade):
        return idade >= 18


p1 = Pessoa("Daniel", 26)
p1.apresentar()

Pessoa.mudar_especie("Andróide")
p2 = Pessoa("Ana", 22)
p2.apresentar()

print(Pessoa.e_adulto(15))  # False
print(Pessoa.e_adulto(30))  # True
