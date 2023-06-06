notas_alunos = []

for i in range(10):
    notas = []
    for j in range(4):
        nota = float(input("Digite a nota do aluno {}: ".format(i+1)))
        notas.append(nota)
    media = sum(notas) / len(notas)
    notas_alunos.append(media)

num_alunos_aprovados = sum(1 for nota in notas_alunos if nota >= 7.0)

print("Número de alunos com média maior ou igual a 7.0:", num_alunos_aprovados)
