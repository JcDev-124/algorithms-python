def quantidade_digitos(numero):
    quantidade = len(str(numero))
    return quantidade

numero = int(input("Digite um número: "))
quantidade = quantidade_digitos(numero)
print("Quantidade de dígitos:", quantidade)
