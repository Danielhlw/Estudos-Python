class Animal:
    def __init__ (self, nome):
        self.nome = nome

    def falar(self):
        print(f"O animal {self.nome} faz um som")

class Cachorro(Animal):
    def falar(self):
        print(f"O cachorro {self.nome} está latindo")

class Gato(Animal):
    def falar(self):
        print(f"O gato {self.nome} está miando")

a = Animal("bicho")
c = Cachorro("Rex")
g = Gato("Mimi")

a.falar()
c.falar()
g.falar()