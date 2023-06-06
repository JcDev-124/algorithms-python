numero = int(input("Digite um número para ver a tabuada (de 1 a 10): "))

while numero < 1 or numero > 10:
    print("Número inválido. Digite novamente.")
    numero = int(input("Digite um número para ver a tabuada (de 1 a 10): "))

print("Tabuada de", numero, ":")

for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
