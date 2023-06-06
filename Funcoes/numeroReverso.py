def reverso_numero(numero):
    numero_str = str(numero)
    reverso_str = numero_str[::-1]
    reverso = int(reverso_str)
    return reverso

numero = int(input("Digite um número: "))
reverso = reverso_numero(numero)
print("Reverso do número:", reverso)
