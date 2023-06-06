nota = -1

while nota < 0 or nota > 10:
    nota = float(input("Digite uma nota entre zero e dez: "))

    if nota < 0 or nota > 10:
        print("Valor inválido. Digite novamente.")

print("Nota válida:", nota)
