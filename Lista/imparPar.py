vetor = []
pares = []
impares = []

for i in range(20):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Números digitados:", vetor)
print("Números pares:", pares)
print("Números ímpares:", impares)
