salario = float(input("Digite o salário atual do colaborador: "))

if salario <= 280:
    percentual_aumento = 20
elif salario <= 700:
    percentual_aumento = 15
elif salario <= 1500:
    percentual_aumento = 10
else:
    percentual_aumento = 5

aumento = salario * percentual_aumento / 100
novo_salario = salario + aumento

print("Salário antes do reajuste:", salario)
print("Percentual de aumento aplicado:", percentual_aumento, "%")
print("Valor do aumento:", aumento)
print("Novo salário:", novo_salario)
