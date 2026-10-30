with open("compras.txt", "w", encoding="utf-8") as arquivo:
    pass

while True:
    lista_desejos = input(
        "Digite o nome de um produto para sua lista de desejos (ou digite 'sair' para encerrar): "
    ).title()
    if lista_desejos.strip().lower() == "sair":
        print("")
        print("Encerrando o programa. Obrigado por usar a lista de desejos!")
        break
    else:
        with open("compras.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(lista_desejos + "\n")

print("\nLista de desejos atualizada com sucesso!")
with open("compras.txt", "r", encoding="utf-8") as arquivo:
    leitura = arquivo.read()

    if leitura == "":
        print("\nNão há itens na lista de desejos.")
    else:
        print("\nItens na lista de desejos:")
        print(f"\n{leitura}")
