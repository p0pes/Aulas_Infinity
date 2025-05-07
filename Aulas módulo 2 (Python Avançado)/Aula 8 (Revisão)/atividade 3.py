#Crie um conjunto com nomes de cores. Implemente uma
#função que retorne as cores que têm mais de quatro
#letras.

lista = ["amarelo", "azul", "verde", "vermelho", "rosa", "roxo", "violeta", "preto"]
listac= []

def cores4(lista, listac):
    
    for x in lista :
        if len(x) > 4 :
            listac.append(x)
    return listac

print(cores4(lista, listac))