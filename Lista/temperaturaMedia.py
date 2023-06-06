temperaturas = []

for mes in range(12):
    temperatura = float(input("Digite a temperatura média do mês {}: ".format(mes+1)))
    temperaturas.append(temperatura)

media_anual = sum(temperaturas) / len(temperaturas)

print("Temperaturas acima da média anual:")
for mes in range(12):
    if temperaturas[mes] > media_anual:
        print("Mês", mes+1, ":", temperaturas[mes])
