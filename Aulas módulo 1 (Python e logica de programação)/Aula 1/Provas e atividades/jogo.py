import random

menu = ""
tent = 0
resposta = str(random.randint(1,10))
vida = 3

while True :
    menu = str(input("Insira 's' para iniciar o jogo e 'n' para fechar o jogo. Ou 'ajuda' para receber as instruções: "))
    if menu == "n" :
        break
    elif menu == "s" :
        while True :
            tent = str(input("Insira sua tentativa de número: "))
            if tent == resposta :
                print(f"--------------------------")  
                print("Parabéns, você venceu! :D")
                break
            elif tent != resposta :
                vida -= 1
            print(f"-------------------------------------")    
            print(f"Número errado! Você possui {vida} vidas!")
            if vida <= 0 and tent != resposta :
                print(f"----------------------------------------------------")
                print(f"Você perdeu todas as suas vidas, tente mais uma vez.")
                break
        break
    elif menu == "ajuda" :
        print(f"-------------------------------------------------------------------------------------------")
        print("Este é um jogo que consiste em acertar um número aleatorio de 1 até 10, tendo 3  tentativas.")
    else :
        print("Insira uma opção valida.")