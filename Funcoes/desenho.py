def desenha_moldura(linhas=1, colunas=1):
    linhas = max(1, min(20, linhas))
    colunas = max(1, min(20, colunas))
    
    print("+" + "-" * colunas + "+")
    for _ in range(linhas):
        print("|" + " " * colunas + "|")
    print("+" + "-" * colunas + "+")

num_linhas = int(input("Digite o número de linhas: "))
num_colunas = int(input("Digite o número de colunas: "))

desenha_moldura(num_linhas, num_colunas)
