#Implemente um sistema simples de cadastro de usuários usando um dicionário.
#Cada usuário deve ter um nome, idade e e-mail. Permita que o usuário adicione
#novos cadastros e visualize todos os cadastros.

usuarios = {}

while True:
    print("-------------------------------------------------")
    print("Insira uma opção dentre as seguintes:\n1- Cadastras um novo usuario.\n2- Verificar todos os cadastros.\n3- Encerrar o programa.")
    menu = str(input("\nInsira o número: "))
    if menu == "3" :
        break
    elif menu == "2" :
        print("-------------------------------------------------")
        print(usuarios)
    elif menu == "1" :
        print("-------------------------------------------------")
        usuario = str(input("Insira o nome do usuario que quer cadastras: "))
        idade = int(input(f"Insira a idade do usuario {usuario}: "))
        email = str(input(f"Insira o e-mail do usuario {usuario}: "))
        usuarios[usuario] = {'idade': idade, 'email': email}
    else:
        print("Opção inválida. Tente novamente.")
        continue