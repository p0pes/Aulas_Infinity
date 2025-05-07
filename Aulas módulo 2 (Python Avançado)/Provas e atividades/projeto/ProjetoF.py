def adicionar_tarefas(lista_tarefas, tarefa, prioridade) :
        
    tarefa = {"Nome" : tarefa, "Conclusão" : "Não concluido.", "Prioridade" : prioridade}
    lista_tarefas.append(tarefa)

def concluir_tarefa(lista_tarefas, alt_conc) :
        
    for tarefa in lista_tarefas:
        if tarefa["Nome"] == alt_conc:
            tarefa["Conclusão"] = "Concluido"
            return True
    return False

def alterar_prioridade(lista_tarefas, nome_tarefa, alt_prio):
    for tarefa in lista_tarefas:
        if tarefa["Nome"] == nome_tarefa:
            tarefa["Prioridade"] = alt_prio
            return True
    return False
        
def organizar_prioridade(lista_tarefas, prioridade) :
    
      return sorted(lista_tarefas, key=lambda x: x[prioridade])

def remover_tarefa (Lista_tarefas, remov) :
    for tarefa in Lista_tarefas :
        if tarefa["Nome"] == remov :
            Lista_tarefas.remove(tarefa)