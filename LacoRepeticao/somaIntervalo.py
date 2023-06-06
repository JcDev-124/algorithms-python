inicio = int(input("Digite o número inicial do intervalo: "))
fim = int(input("Digite o número final do intervalo: "))

soma = 0

for num in range(inicio, fim + 1):
    soma += num
    print(num)

print("Soma dos números:", soma)
