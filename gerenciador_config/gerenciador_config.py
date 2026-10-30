try:
    with open("config.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            print("")
            print(linha)
except FileNotFoundError:
    print("Arquivo de configuração não encontrado. Criando configuração padrão...")
    with open("config.txt", "w", encoding="utf-8") as config:
        config.write("usuario=admin\nservidor=127.0.0.1")
