class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # atributo privado

    # Getter → obtém o valor
    def get_saldo(self):
        return self.__saldo

    # Setter → altera o valor com validação
    def set_saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
        else:
            print("❌ Saldo não pode ser negativo!")

c1 = Conta("Daniel", 1000)

print(c1.get_saldo())  # 1000
c1.set_saldo(1500)
print(c1.get_saldo())  # 1500
c1.set_saldo(-50)      # ❌ Saldo não pode ser negativo!