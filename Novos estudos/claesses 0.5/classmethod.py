class Pessoa:
    especie = "Humano"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod # decorator que afeta a classe inteira
    def mudar_especie(cls, nova_especie):
        cls.especie = nova_especie

Pessoa.mudar_especie("Andróide")

p1 = Pessoa("Daniel", 26)
p2 = Pessoa("Ana", 22)

print(p1.especie)  # andróide
print(p2.especie)  # andróide
