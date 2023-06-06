idades = []
alturas = []

for i in range(5):
    idade = int(input("Digite a idade da pessoa {}: ".format(i+1)))
    altura = float(input("Digite a altura da pessoa {}: ".format(i+1)))
    idades.append(idade)
    alturas.append(altura)

idades.reverse()
alturas.reverse()

print("Idades na ordem inversa:", idades)
print("Alturas na ordem inversa:", alturas)
