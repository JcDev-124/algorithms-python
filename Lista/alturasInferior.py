idades = []
alturas = []

for i in range(30):
    idade = int(input("Digite a idade do aluno {}: ".format(i+1)))
    altura = float(input("Digite a altura do aluno {}: ".format(i+1)))
    idades.append(idade)
    alturas.append(altura)

media_altura = sum(alturas) / len(alturas)
alunos_mais_de_13_anos = sum(1 for i in range(30) if idades[i] > 13 and alturas[i] < media_altura)

print("Quantidade de alunos com mais de 13 anos e altura inferior à média:", alunos_mais_de_13_anos)
