# Método de classe

class Carro:
    fabrica = "Volkswagen"

    def __init__ (self, porta, rodas):
        self.porta = porta
        self.rodas = rodas

    def chamar_carro(self):
        print(f"Nome da fábrica:{Carro.fabrica}, quantidade de portas: {self.porta}, quantidade de  rodas: {self.rodas}")
        print()

    @classmethod
    def alterar_fabrica(cls, nova):
        cls.fabrica = nova


c1 = Carro(4, 6)
print(c1.fabrica)
Carro.alterar_fabrica("Nissan")
print(c1.fabrica)

c1.chamar_carro()