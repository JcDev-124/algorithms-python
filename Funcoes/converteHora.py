def converte_hora(hora, minuto):
    if hora > 12:
        hora -= 12
        periodo = 'P.M.'
    else:
        periodo = 'A.M.'
    return hora, minuto, periodo

continuar = True
while continuar:
    hora = int(input("Digite a hora (entre 0 e 23): "))
    minuto = int(input("Digite os minutos (entre 0 e 59): "))
    
    hora_convertida, minuto_convertido, periodo = converte_hora(hora, minuto)
    print("Hora convertida:", hora_convertida, ":", minuto_convertido, periodo)
    
    opcao = input("Deseja converter outra hora? (S/N): ")
    if opcao.upper() != 'S':
        continuar = False
