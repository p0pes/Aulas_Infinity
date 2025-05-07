#Desenvolva um programa que recebe um dicionário, uma
#chave e um valor como entrada e adiciona a chave e o
#valor ao dicionário, atualizando o valor se a chave já
#existir.

dic = {
    "Marcelo" : "Professor",
    "Andre" : "Empresario",
    "Ana" : "Gerente"
    }

x = str(input("Insira a chave para o dicionario: "))
y = str(input("Insira o valor da chave : "))

dic[x] = y

print(dic)