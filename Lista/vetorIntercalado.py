vetor1 = []
vetor2 = []
vetor3 = []

for i in range(10):
    numero1 = int(input("Digite um número inteiro para o vetor 1: "))
    vetor1.append(numero1)
    numero2 = int(input("Digite um número inteiro para o vetor 2: "))
    vetor2.append(numero2)

for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print("Vetor intercalado:", vetor3)
