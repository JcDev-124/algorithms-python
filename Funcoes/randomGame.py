import random

def jogo_craps():
    primeiro_lancamento = random.randint(2, 12)
    print("Resultado do primeiro lançamento:", primeiro_lancamento)
    
    if primeiro_lancamento == 7 or primeiro_lancamento == 11:
        print("Natural! Você ganhou!")
        return
    elif primeiro_lancamento == 2 or primeiro_lancamento == 3 or primeiro_lancamento == 12:
        print("Craps! Você perdeu!")
        return
    
    print("Ponto:", primeiro_lancamento)
    
    while True:
        proximo_lancamento = random.randint(2, 12)
        print("Próximo lançamento:", proximo_lancamento)
        
        if proximo_lancamento == primeiro_lancamento:
            print("Você acertou o ponto! Você ganhou!")
            return
        elif proximo_lancamento == 7:
            print("Você tirou 7. Você perdeu!")
            return

jogo_craps()
