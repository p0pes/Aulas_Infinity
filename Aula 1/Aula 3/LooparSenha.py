senha = ""

while senha != "1234" :
    senha = str(input("Insira sua senha: "))
    if senha == "1234" :
        print("Login concluido!")
    elif senha != "1234" :
        print("Senha incorreta!")