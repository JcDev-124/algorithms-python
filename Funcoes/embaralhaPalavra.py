import random

def embaralha_palavra(palavra):
    lista_caracteres = list(palavra)
    random.shuffle(lista_caracteres)
    palavra_embaralhada = "".join(lista_caracteres)
    return palavra_embaralhada

palavra = input("Digite uma palavra: ")
palavra_embaralhada = embaralha_palavra(palavra)
print("Palavra embaralhada:", palavra_embaralhada)
