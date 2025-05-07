#Crie um módulo chamado manipulacao_strings que
#contenha funções para realizar operações com strings,
#como inverter uma string, contar o número de palavras
#em uma string e verificar se uma string é um
#palíndromo (lê-se igual de trás para frente). Crie
#um programa principal que importe o módulo e use
#essas funções com strings fornecidas pelo usuário.

from funcoes import *

string = str(input("Insira qual a frase/palavra quer manipular: "))
print("---------------------------------------------------------------")


print("Insira um dos seguintes números para iniciar as manipulações na sua string: ")
print("1- Inverter.")
print("2- Dizer quantas letras possui.")
print("3- Checar palndromo.")
print("4- Exibir letra por letra.")
print("0- Encerrar programa.")

while True :
    menu = input("Insira a função: ")
    if menu == "0" :
        print("Programa encerrado! :)")
        break
    elif menu == "1" :
        print(f"A sua string invertida se torna '{inverter(string)}'!")
        print("-------------------------------------------------------")
    elif menu == "2" :
        print(f"A quantidade de letras é igual a {contar_letras(string)}!")
        print("-------------------------------------------------------")
    elif menu == "3" : 
        print(palindro(string))
        print("-------------------------------------------------------")
    elif menu == "4" :
        for y in exibir_vertical(string) :
            print(y)
        print("-------------------------------------------------------")
    else :
        print("-------== INSIRA UMA OPÇÃO VÁLIDA ==-------")