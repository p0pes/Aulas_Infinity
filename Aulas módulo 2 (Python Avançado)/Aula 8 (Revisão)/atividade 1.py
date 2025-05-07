#Dada uma lista de números, crie uma nova lista contendo
#apenas os números pares.

lista = [1, 2, 3, 4, 5, 6, 7, 9,]
listap = []

for x in lista :
    if x % 2 == 0 :
        listap.append(x)

print(listap)