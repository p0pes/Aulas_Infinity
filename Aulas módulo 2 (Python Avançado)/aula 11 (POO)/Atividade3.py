#Crie uma classe Empresa que permita gerenciar
#funcionários. Os funcionários devem ter informações
#como nome, cargo e salário. A empresa deve ser capaz
#de adicionar, remover e listar funcionários.

class Empresa:
    def __init__(self, nome, cargo, salario) :
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

funcionarios = []

print("Insira uma das seguintes opções:"
          "\n1 - Adicionar funcionário."
          "\n2 - Remover funcionário."
          "\n3 - Listar funcionário."
          "\n4 - Encerrar.")

while True :
    print("-------------------")
    menu = input("Insira aqui: ")
    if menu == "1" :
        nome = str(input("Insira o nome do funcionário: "))
        cargo = str(input("Insira a função desse funcionário: "))
        salario = float(input("insira o salário desse funcionário:"))
        funcionario = Empresa(nome, cargo, salario)
        funcionarios.append(funcionario)
    
    elif menu == "2" :
        delete = input("Insira o funcionario que quer remover: ")
        for x in funcionarios :
            if delete == x.nome :
                funcionarios.remove(x)
            else :
                continue
            
    elif menu == "3" :
        for x in funcionarios :
            print("--------------------------------")
            print(f"Nome: {x.nome}")
            print(f"Cargo: {x.cargo}")
            print(f"Salário: {x.salario}")

    elif menu == "4" :
        break 