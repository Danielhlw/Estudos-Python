class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome        # público
        self._cidade = "Assis"  # protegido
        self.__cpf = "123.456.789-00"  # privado

p = Pessoa("Daniel", 22)

print(p.nome)      # ✅ ok
print(p._cidade)   # ⚠️ possível, mas não recomendado
print(p.__cpf)     # 🚫 ERRO: atributo privado

