notas = []

for i in range(4):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("Notas:", notas)
print("Média:", media)
