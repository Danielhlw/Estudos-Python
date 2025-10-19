tentativas = 3
senha_correta = 123

while True:
    senha = int(input("Digite uma senha: "))
    if senha == senha_correta:
        print("Acesso permitido!")
        break
    else:
        tentativas -= 1
        print(f"Você só tem {tentativas} tentativas!")
        if tentativas == 0:
            print("Acesso bloqueado!")
            break