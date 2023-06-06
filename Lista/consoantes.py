vetor = []

for i in range(10):
    caracter = input("Digite um caractere: ")
    vetor.append(caracter)

consoantes = 0

for caractere in vetor:
    if caractere.lower() not in ['a', 'e', 'i', 'o', 'u']:
        consoantes += 1

print("Quantidade de consoantes:", consoantes)
print("Consoantes:", [caractere for caractere in vetor if caractere.lower() not in ['a', 'e', 'i', 'o', 'u']])
