class Pessoa:
    @staticmethod
    def maior_de_idade(idade):
        return idade >= 18

print(Pessoa.maior_de_idade(20))  # True
print(Pessoa.maior_de_idade(15))  # False
