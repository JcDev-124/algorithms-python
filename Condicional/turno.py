turno = input("Em que turno você estuda? Digite M para matutino, V para vespertino ou N para noturno: ")

if turno == "M" or turno == "m":
    print("Bom Dia!")
elif turno == "V" or turno == "v":
    print("Boa Tarde!")
elif turno == "N" or turno == "n":
    print("Boa Noite!")
else:
    print("Valor Inválido!")
