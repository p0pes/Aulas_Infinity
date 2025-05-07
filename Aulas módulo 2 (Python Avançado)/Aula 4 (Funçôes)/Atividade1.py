#Crie uma função que receba um nome e imprima uma
#saudação personalizada.

def dizer_ola(nome):
    return f"Boa tarde {nome}!"

nome = str(input("Insira aqui o seu nome: "))

print(dizer_ola(nome))