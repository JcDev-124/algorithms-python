perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas = []

for pergunta in perguntas:
    resposta = input(pergunta + " (S/N): ")
    while resposta.upper() not in ['S', 'N']:
        print("Resposta inválida. Digite novamente.")
        resposta = input(pergunta + " (S/N): ")
    respostas.append(resposta.upper())

num_sim = respostas.count('S')

if num_sim == 2:
    classificacao = "Suspeita"
elif 3 <= num_sim <= 4:
    classificacao = "Cúmplice"
elif num_sim == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

print("Classificação:", classificacao)
