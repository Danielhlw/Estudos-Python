class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    @property
    def saldo(self):  # getter
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):  # setter
        if valor >= 0:
            self.__saldo = valor
        else:
            print("❌ Saldo inválido!")

c1 = Conta("Daniel", 500)
print(c1.saldo)  # usa o getter
c1.saldo = 1000  # usa o setter
print(c1.saldo)
c1.saldo = -200  # inválido

