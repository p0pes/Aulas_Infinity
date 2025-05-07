#crie duas listas e as una sem que tenham elementos repetidos

lista1 = [1, 4, 6, 7, 10]
lista2 = [1, 2, 7, 10, 22]
set1 = set(lista1)
set2 = set(lista2)

set1.update(set2)

print(set1)