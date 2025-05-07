#Escreva uma função que receba uma lista e retorne o maior e o menor elemento.

lista = []
lista_int = []
x= 0

for cont in range(3) :
    x += 1
    cont = input(f"Insira o {x} numero de 1 a 9 pra a lista: ")
    lista.append(cont)

lista.sort()
print("-------------------------------")
print(f"{lista[2]} é o maior número")
print("-------------------------------")
print(f"{lista[0]} é o menor número")
print("-------------------------------")