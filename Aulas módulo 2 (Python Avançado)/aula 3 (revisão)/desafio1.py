#Você foi contratado para desenvolver um programa simples para
#auxiliar em um processo de compra de produtos. O programa deve
#permitir ao usuário inserir o nome e o preço de vários produtos,
#perguntando se deseja continuar inserindo mais produtos após cada
#entrada. Ao final, o programa deve fornecer um resumo da compra, incluindo:
#A) O total gasto na compra.
#B) A quantidade de produtos que custam mais de R$1000.
#C) O nome do produto mais barato.
#Desenvolva o programa em Python utilizando conceitos de
#entrada/saída de dados, condicionais e laços de repetição.

lista_de_produtos = {}
valor_total = 0
produtos_caros = 0

print("Insira um número dentre as seguintes opções :\n1 - Adicionar um novo procuto.\n2 - Verificar os produtos inseridos.\n3 - Encerrar o programa.")

while True :
    menu = str(input("Número do menu : "))
    if menu == "3" :
        break
    elif menu == "2" :
        print(lista_de_produtos)
    elif menu == "1" :
        prod = str(input("Insira o nome do produto a ser colocado: "))
        prec = float(input("Insira o valor deste produto em reais: "))
        lista_de_produtos[prod] = prec
        valor_total += prec
        if prec > 1000 :
            produtos_caros += 1

print(f"O valor total da sua compra foi {valor_total:.2f}R$.")
print(f"Você comprou {produtos_caros} itens que valem mais do que 1000 reais.")