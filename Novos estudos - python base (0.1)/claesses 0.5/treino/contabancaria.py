class ContaBancaria:
    taxa_juros_anual = 0.10
    def __init__(self, numero: str, titular: str, saldo: float = 0.0):
        pass
    
    def depositar(self, valor: float):
        pass
    def sacar(self, valor: float):
        pass
    def extrato(self):
        pass

    @classmethod
    def alterar_taxa(cls, nova_taxa: float):
        pass
    @classmethod
    def criar_com_prefixo(cls, prefixo: str, sequencial: int, titular: str, saldo_inicial: float = 0.0):
        pass

    @staticmethod
    def validar_numero_conta(numero: str) -> bool:
        pass
    def calcular_juros_simples(principal: float, taxa_anual: float, anos: int) -> float:
        pass