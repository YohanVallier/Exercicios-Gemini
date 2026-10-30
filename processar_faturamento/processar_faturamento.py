total_faturado = 0.0
itens_validos = 0

try:
    with open("vendas_dia.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha_limpa = linha.strip()
            try:
                valor = float(linha_limpa)
                total_faturado += valor
                itens_validos += 1
            except ValueError:
                print(f"AVISO: Linha ignorada por conter dado inválido -> {linha_limpa}")

    with open("relatorio_final.txt", "w", encoding="utf-8") as relatorio:
        relatorio.write(f"Total Faturado: R$ {total_faturado: .2f}\n")
        relatorio.write(f"Quantidade de lançamentos válidos: {itens_validos}\n")

    print("Processamento concluído com sucesso!")

except FileNotFoundError:
    print("ERRO CRÍTICO: O arquivo 'vendas_dias.txt' não foi encontrado na pasta.")
