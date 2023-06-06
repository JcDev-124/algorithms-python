vetor = []

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

soma_quadrados = sum(numero**2 for numero in vetor)

print("Soma dos quadrados dos elementos do vetor:", soma_quadrados)
