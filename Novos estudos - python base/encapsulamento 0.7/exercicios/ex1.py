class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("Saldo inválido! Não é possível atribuir um valor negativo.")
    
    def sacar(self, valor):
        if valor <=0:
            print("Valor de saque inválido!")
        elif valor > self.__saldo:
            print("Saldo insuficiente para saque!")
        else:
            self.__saldo -= valor
            print(f"Saque de {valor} realizado com sucesso.")
        
    def depositar(self, valor):
        if valor <=0:
            print("Valor de depósito inválido!")
        else:
            self.__saldo += valor
            print(f"Depósito de {valor} realizado com sucesso.")
        


c = ContaBancaria("Daniel", 1000)

print(f"Titular: {c.titular}")
print(f"Saldo atual: R$ {c.saldo:.2f}")

c.depositar(500)
print(c.saldo)
c.sacar(250)
print(c.saldo)
c.sacar(5000)
print(c.saldo)
c.saldo = -100
print(c.saldo)
c.saldo = 2000



print(f"Saldo final: R$ {c.saldo:.2f}")
