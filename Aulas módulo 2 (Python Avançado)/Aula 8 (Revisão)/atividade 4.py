#Crie uma função que receba uma lista de strings e
#retorne uma nova lista contendo apenas as strings
#palíndromos.

def palindromo(lista, listap):
    for string in lista:
        check1 = string.lower()
        check2 = string[::-1]
        if check1 == check2:
            listap.append(string)
    return listap

lista = ["pikachu", "piplup", "girafarig", "ovo"]
listap = []
resultados = palindromo(lista, listap)
print(resultados)