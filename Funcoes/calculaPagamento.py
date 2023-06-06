def valorPagamento(valor_prestacao, dias_atraso):
    if dias_atraso == 0:
        return valor_prestacao
    else:
        multa = valor_prestacao * 0.03
        juros = valor_prestacao * (0.001 * dias_atraso)
        valor_total = valor_prestacao + multa + juros
        return valor_total

relatorio = []
continuar = True
while continuar:
    valor = float(input("Digite o valor da prestação (ou 0 para encerrar): "))
    if valor == 0:
        continuar = False
    else:
        dias_atraso = int(input("Digite o número de dias em atraso: "))
        valor_total = valorPagamento(valor, dias_atraso)
        relatorio.append(valor_total)
        print("Valor a ser pago:", valor_total)

quantidade_prestacoes = len(relatorio)
valor_total_prestacoes = sum(relatorio)
print("Relatório do dia:")
print("Quantidade de prestações pagas:", quantidade_prestacoes)
print("Valor total das prestações pagas:", valor_total_prestacoes)
