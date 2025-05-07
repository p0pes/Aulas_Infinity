#Escreva um programa que recebe um dicionário e uma
#lista de chaves como entrada e verifica se todas as
#chaves da lista existem no dicionário. A função deve
#retornar True se todas as chaves existirem e False caso
#contrário.

dic = {
    "nota1" : 9.5,
    "nota2" : 10,
    "nota3" : 2.9,
    "nota4": 4.7
}

chaves = ["nota1", "nota4", "nota12", "nota7", "nota9", "nota2"]

for x in chaves :
    if x in dic :
        print(f"{x} esta no dicionario")
    elif x not in dic :
        print(f"{x} não está no dicionario")