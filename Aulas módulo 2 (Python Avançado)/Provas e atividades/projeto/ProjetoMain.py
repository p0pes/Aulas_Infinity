from ProjetoF import*

lista_tarefas = []
menu = ""

print("Insira um dos seguintes números para continuar com a aplicação:\n"
      "1- Adicionar tarefa.\n"
      "2- Concluir tarefa.\n"
      "3- Alterar a prioridade de uma tarefa.\n"
      "4- Listar tarefas organizadas por prioridade.\n"
      "5- Remover uma tarefa.\n"
      "0- Encerrar programa.")

while True :
    menu = str(input("Insira um número ou use 9 para acessar o menu novamente: : "))
    if menu == "0" :
        print("Sistema encerrado!")
        break
    elif menu == "1" :
        tarefa = input("Insira o nome da tarefa: ")
        prioridade = int(input("Insira o número de prioridade dessa tarefa: "))
        adicionar_tarefas(lista_tarefas, tarefa, prioridade)
        print(f"Tarefa {tarefa} adicionada!")
        print("--------------------------")
    elif menu == "2" :
        alt_conc = input("Insira qual tarefa quer concluir: ")
        if concluir_tarefa(lista_tarefas, alt_conc) :
            print(f"Tarefa {alt_conc} concluida!")
            print("--------------------------")
        else :
            print("----Esta tarefa não existe!----")
    elif menu == "3":
        nome_tarefa = input("Insira a tarefa para alterar sua prioridade: ")
        alt_prio = int(input("Insira a nova prioridade dessa tarefa: "))
        if alterar_prioridade(lista_tarefas, nome_tarefa, alt_prio):
            print(f"Prioridade da tarefa '{nome_tarefa}' alterada!")
            print("--------------------------")
        else:
            print("----Esta tarefa não existe!----")
    elif menu == "4" :
        lista_prioridade = organizar_prioridade(lista_tarefas, 'Prioridade')
        for x in lista_prioridade :
            print(x)
        print("--------------------------")
    elif menu == "5" :
        remov = str(input("Insira a tarefa que vai ser removida da lista: "))
        print(f"Trefa {remov} removida!")
        remover_tarefa(lista_tarefas, remov)
    elif menu == "9" :
        print("--------------------------------------------------------------------")
        print("Intruções do menu:\n"
      "1- Adicionar tarefa.\n"
      "2- Concluir tarefa.\n"
      "3- Alterar a prioridade de uma tarefa.\n"
      "4- Listar tarefas organizadas por prioridade.\n"
      "5- Remover uma tarefa.\n"
      "0- Encerrar programa.")
        print("--------------------------------------------------------------------")
    else :
        print("----Insira uma opção válida!----")