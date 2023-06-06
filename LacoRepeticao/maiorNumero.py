maior_numero = float('-inf')

for _ in range(5):
    numero = float(input("Digite um número: "))
    if numero > maior_numero:
        maior_numero = numero

print("O maior número é:", maior_numero)
