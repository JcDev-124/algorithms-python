valores = []

valor = int(input("Digite um valor (ou -1 para encerrar): "))
while valor != -1:
    valores.append(valor)
    valor = int(input("Digite um valor (ou -1 para encerrar): "))

print("Quantidade de valores lidos:", len(valores))
print("Valores informados:", end=" ")
for valor in valores:
    print(valor, end=" ")
print()
print("Valores na ordem inversa:")
for valor in reversed(valores):
    print(valor)
soma = sum(valores)
media = soma / len(valores)
print("Soma dos valores:", soma)
print("Média dos valores:", media)
print("Quantidade de valores acima da média:", sum(1 for valor in valores if valor > media))
print("Quantidade de valores abaixo de sete:", sum(1 for valor in valores if valor < 7))
print("Programa encerrado.")
