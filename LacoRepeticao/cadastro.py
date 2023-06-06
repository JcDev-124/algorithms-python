nome = input("Digite o nome: ")

while len(nome) <= 3:
    print("Nome inválido. Digite novamente.")
    nome = input("Digite o nome: ")

idade = -1

while idade < 0 or idade > 150:
    idade = int(input("Digite a idade: "))

    if idade < 0 or idade > 150:
        print("Idade inválida. Digite novamente.")

salario = -1

while salario <= 0:
    salario = float(input("Digite o salário: "))

    if salario <= 0:
        print("Salário inválido. Digite novamente.")

sexo = input("Digite o sexo (f - feminino / m - masculino): ")

while sexo.lower() != 'f' and sexo.lower() != 'm':
    print("Sexo inválido. Digite novamente.")
    sexo = input("Digite o sexo (f - feminino / m - masculino): ")

estado_civil = input("Digite o estado civil (s - solteiro / c - casado / v - viúvo / d - divorciado): ")

while estado_civil.lower() not in ['s', 'c', 'v', 'd']:
    print("Estado civil inválido. Digite novamente.")
    estado_civil = input("Digite o estado civil (s - solteiro / c - casado / v - viúvo / d - divorciado): ")

print("Informações validadas com sucesso!")
