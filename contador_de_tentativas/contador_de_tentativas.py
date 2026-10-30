senha_banco = int(input("Digite a senha do banco: "))
tentativas = 0

while tentativas < 3 and senha_banco != 123456:
    tentativas += 1
    if tentativas >= 1 and tentativas <= 3:
        print("Senha incorreta. Tente novamente.")
        print("")
        print(f"Tentativa {tentativas} de 3.")
        print("")
        if tentativas == 3:
            print("Você só tem mais 1 tentativa restante.")
        print("")
        senha_banco = int(input("Digite a senha do banco: "))
    else:
        print("Número máximo de tentativas excedido.")
        print("")
        break
print("Acesso concedido. Bem-vindo ao banco!")
