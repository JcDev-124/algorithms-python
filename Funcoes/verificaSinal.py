def verifica_sinal(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'

numero = int(input("Digite um número: "))
sinal = verifica_sinal(numero)
print("O sinal do número é:", sinal)
