class Conta:
    def __init__(self, titular, saldo):
        self._saldo = saldo

class ContaPoupanca(Conta):
    def render_juros(self):
        self._saldo *= 1.05  # permitido (protegido)
        print(f"Novo saldo com juros: {self._saldo}")
