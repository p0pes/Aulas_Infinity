#Documentar suas funções é
#essencial para que outros
#esenvolvedores (ou você
#mesmo no futuro) possam
#ntender o que a função faz,
#quais parâmetros ela recebe
#e o que ela retorna.

def lista_de_numeros_pares(lista:list) :
    '''
    essa função tem como objetivo percorrer a lista usando o for para filtrar os numeros pares de uma lista qualquer
    '''
    for numero in lista :
        if numero % 2 == 0 :
            print(numero)

lista_qualquer = [1, 2, 3, 4, 5]

lista_de_numeros_pares(lista_qualquer)