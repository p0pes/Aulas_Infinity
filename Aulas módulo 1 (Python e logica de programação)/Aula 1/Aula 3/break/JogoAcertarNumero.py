menu = ""
tent = ""
resposta = "7"

while True :
    menu = str(input("Insira S para iniciar o jogo e N para fechar o jogo: "))
    if menu == "N" :
        break
    elif menu == "S" :
        tent = str(input("Insira sua tentativa de numero: "))
        if tent == resposta :
            print("Parabens, voce venceu! :D")
            break
        elif tent != resposta :
            print("Numero errado, tente mais uma vez!")
    else :
        print("Insira uma opcao valida")