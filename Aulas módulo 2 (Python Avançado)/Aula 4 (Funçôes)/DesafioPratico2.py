#Cadastro de matricula e nome de aluno usando função

dicionario = {}

def cadastro () :
    nome = str(input("Insira aqui o nome do aluno que quer cadastrar: "))
    matricula = str(input("Insira aqui a matricula desse aluno: "))
    return nome, matricula

def incluir_dicionario (nome, matricula):
    dicionario[matricula] = nome
    


while True :
    print("Insira um dos seguintes números para continuar:\n 1- cadastrar um aluno.\n 2- Checar os cadastros.\n 3- Encerrar o programa.")       
    menu = str(input("\n-->"))
    print("-----------------------------------------------")
    if menu == "1" :
        nome, matricula = cadastro()
        incluir_dicionario(nome, matricula)
    elif menu == "3" :
        print("Programa encerrado!")
        break
    elif menu == "2" :
        print(dicionario)
    print("-----------------------------------------------")