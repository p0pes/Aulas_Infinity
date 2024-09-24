login = str(input("Insira seu login: "))
senha = str(input("Insira sua senha: "))

if login != "admin" and senha != "1234" :
    print("Seu login e senha estão errados!")
elif login == "admin" and senha != "1234" :
    print("Sua senha está incorreta!")
elif login == "admin" and senha == "1234" :
    print("Login concluído!")
else :
    print("Este usuário não existe.")