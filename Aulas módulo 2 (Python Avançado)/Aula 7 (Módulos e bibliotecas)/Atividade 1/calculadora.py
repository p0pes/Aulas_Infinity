#Crie um programa que será uma calculadora.
#Nesta calculadora você deverá ter um módulo para as
#operações matemáticas, o arquivo principal deverá
#conter apenas um menu de escolha para o usuário
#(soma, subtração, multiplicação e divisão).

from operacoes import *

n1 = 0
n2 = 0
menu = ""

print("Insira um dos seguintes números para iniciar as operações: ")
print("1- Soma.")
print("2- Subtração.")
print("3- Divisão.")
print("4- multiplicação.")
print("0- Encerrar programa.")

while True :
    menu = input("Insira a função: ")
    print("------------------------------------------")
    if menu == "0" :
        print("Programa encerrado! :)")
        break
    elif menu == "1" :
        n1, n2 = receber_numeros(n1, n2)
        print("------------------------------------------")
        print(f"O resultado da sua soma é {soma(n1, n2)}!")
    elif menu == "2" :
        n1, n2 = receber_numeros(n1, n2)
        print("------------------------------------------")
        print(f"O resultado da sua subtração é {subttracao(n1, n2)}!")
    elif menu == "3" :
        n1, n2 = receber_numeros(n1, n2)
        print("------------------------------------------")
        print(f"O resultado da sua divisão é {divisao(n1, n2)}!")
    elif menu == "4" :
        n1, n2 = receber_numeros(n1, n2)
        print("------------------------------------------")
        print(f"O resultado da sua multiplicação é {multiplicacao(n1, n2)}!")
    else :
        print("Insira uma opção válida!")
        continue