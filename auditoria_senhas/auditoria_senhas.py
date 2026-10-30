senha_correta = str("python2026")
senha_digitada = ""

while senha_digitada != senha_correta:
    senha_digitada = str(input("Digite a senha: "))
    if senha_digitada != senha_correta:
        print("Senha incorreta. Tente novamente.")
        print("")
    else:
        print("Acesso concedido. Bem-vindo ao sistema!")
