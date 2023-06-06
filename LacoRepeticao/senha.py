nome = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

while senha == nome:
    print("Erro: a senha não pode ser igual ao nome de usuário.")
    senha = input("Digite a senha novamente: ")

print("Nome de usuário e senha registrados com sucesso!")
