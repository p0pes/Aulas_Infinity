opc = ""

while opc != "sair" :
    print("---------------------")
    print("OPÇÕES")
    print("Digite 1 para a pimeira opcão.")
    print("Digite 2 para a segunda opcão.")
    print("Digite 3 para a terceira opção.")
    print("Digite sair para encerrar o programa.")
    print("---------------------")
    opc = str(input("Escolha uma das opções: "))

    if opc == "1" :
        print("Você escolheu a opção 1!")
    elif opc == "2" :
        print("Você escolheu a opção 2!")
    elif opc == "3" :
        print("Você escolheu a opção 3!")
    elif opc == "sair" :
        print("Programa encerrado!")
    else :
        print("Opção inválida. Tente novamente.")