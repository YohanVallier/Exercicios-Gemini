cont = 0

try:
    with open("sistema.log", "r", encoding="utf-8") as arquivo, \
         open("erros_criticos.log", "w", encoding="utf-8") as erro:
        for linha in arquivo:
            if "ERROR" in linha:
                erro.write(linha)
                cont+=1
    print(f"Filtro concluído. {cont} erros críticos foram isolados em erros_criticos.log.")

except FileNotFoundError:
    print("O arquivo não exite! O programa se incerra aqui.")
