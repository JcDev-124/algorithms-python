populacao_A = float(input("Digite a população do país A: "))
populacao_B = float(input("Digite a população do país B: "))
taxa_crescimento_A = float(input("Digite a taxa de crescimento do país A (em decimal): "))
taxa_crescimento_B = float(input("Digite a taxa de crescimento do país B (em decimal): "))
anos = 0

while populacao_A < populacao_B:
    populacao_A += populacao_A * taxa_crescimento_A
    populacao_B += populacao_B * taxa_crescimento_B
    anos += 1

print("Após", anos, "anos, a população do país A ultrapassará ou igualará a população do país B.")
