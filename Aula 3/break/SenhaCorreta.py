senha = str("1234")
tenta = str("")

while True :
    tent = input("Insira a senha correta: ")
    if tent != senha :
        print("Senha incorreta.")
    elif tent == senha :
        print("Senha correta, bem vindo!")
        break