class Pessoa:
    especie = "Humano"  # atributo de classe (compartilhado)

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Daniel", 26)
p2 = Pessoa("Ana", 22)

print(p1.especie)
print(p2.especie)