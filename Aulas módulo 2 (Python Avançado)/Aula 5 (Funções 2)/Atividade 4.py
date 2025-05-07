#Crie uma função que aceita uma lista de números e use
#a função map para retornar uma nova lista contendo o
#dobro de cada número na lista de entrada.

def drobar_numeros(drobar) :
    return drobar * 2

lista = []

print("Insira a quantidade de números que quer pôr nesta lista, depois insira eles. O números serão exibidos no final com o valor dobrado!")
quantidade = int(input("Insira a quantidade de números: "))

for x in range(quantidade) :
    num = int(input("Insira o número: "))
    lista.append(num)

resultado = map(drobar_numeros, lista)

print(list(resultado))