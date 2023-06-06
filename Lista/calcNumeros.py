vetor = []

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

soma = sum(vetor)
multiplicacao = 1

for numero in vetor:
    multiplicacao *= numero

print("Soma dos números:", soma)
print("Multiplicação dos números:", multiplicacao)
print("Números digitados:", vetor)
