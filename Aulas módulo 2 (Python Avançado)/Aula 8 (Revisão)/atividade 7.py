#Você possui dados de vendas trimestrais de uma
#empresa em uma lista. Cada trimestre é representado
#como uma lista de números, onde cada número
#representa o valor de vendas de um mês (janeiro a
#março, abril a junho, julho a setembro e outubro a
#dezembro).
#Você deve realizar as seguintes tarefas:
#Calcule a média de vendas por trimestre.
#Encontre o trimestre com a maior soma de vendas.
#Encontre o trimestre com a menor soma de vendas.
#Calcule o total de vendas no ano inteiro.
#Construa seus dados fictícios

lista = [88, 27, 59, 72, 13, 64, 36, 91, 45, 20, 51, 33]
t1 = []
t2 = []
t3 = []
t4 = []

for x in lista :
    if len(t1) <= 2 :
        t1.append(x)
    elif len(t2) <= 2 :
        t2.append(x)
    elif len(t3) <= 2 :
        t3.append(x)
    elif len(t4) <= 2 :
        t4.append(x)

t1M = sum(t1) / len(t1)
t2M = sum(t2) / len(t2)
t3M = sum(t3) / len(t3)
t4M = sum(t4) / len(t3)