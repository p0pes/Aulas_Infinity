#Crie uma calculadora com opções de soma, multiplicação,
#subtração, divisão e sair.
#(Ela deverá funcionar infinitamente, até que o usuário decida #sair da calculadora.)
#Utilize funções de rotina para cada operação e funções de #unidade lógica para
#realizar os cálculos.

def receber_numeros () :
    n1 = float(input("Insira aqui o número 1: "))
    n2 = float(input("Insira aqui o número 2: "))
    return n1, n2

def soma (n1, n2) :    
    return n1 + n2
    
def subtrair (n1, n2) :
    return n1 - n2

def multiplicar (n1, n2) :    
    return n1 * n2

def dividir (n1, n2) :
    return n1 / n2

while True :
    
    print("Insira um dos seguintes itens para seguir com o programa\n 1- Somar\n 2- subtrair\n 3- multiplicar\n 4- dividir\n 5-Encerrar")
    menu = int(input("\n-> "))
    
    print("---------------------------------")
    if menu == 1 :
        n1, n2 = receber_numeros()
        print(f"O resultado da soma foi {soma(n1, n2)}")
    elif menu == 2 :
        n1, n2 = receber_numeros()
        print(f"O resultado da subtração foi {subtrair(n1, n2)}")
    elif menu == 3 :
        n1, n2 = receber_numeros()
        print(f"O resultado da multiplicação foi {multiplicar(n1, n2)}")
    elif menu == 4 :
        n1, n2 = receber_numeros()
        print(f"O resultado da divisão foi {dividir(n1, n2)}")
    elif menu == 5 :
        print("Calculadora encerrada!")
        break
    else :
        print("Insira uma opção valida!")
        continue
    print("---------------------------------")