from funcoes import *

lista_produtos = []

print("Insira um dos seguintes numeros para seguir com as funções:\n"
      "1 - Adicionar produto.\n"
      "2 - Apagar produto.\n"
      "3 - Atualizar produto\n"
      "4 - Verificar lista.\n")

while True :
    
    menu = input("-> : ")
    if menu == "1" :
        produto = str(input("Insira o nome do produto: "))
        qnt = int(input("Insira a quantidade do produto: "))
        val = float(input("Insira o valor do produto: "))
        adicionar_produto(lista_produtos, produto, qnt, val)
    elif menu == "2" :
        exprod = str(input("Insira o produtor que quer apagar: "))
        remover_produto(exprod, lista_produtos)
    elif menu == "4" :
        for x in lista_produtos :
            print(x)
    else :
        print("Insira uma opção válida!")