#Faça um programa que, dado um conjunto de N
#números, determine o menor valor, o maior valor e a
#soma dos valores.

lista = []
soma = 0

while True :
    print("insira 1 para adicionar um novo numero e 2 para encerrar o programa.")
    menu = str(input("Insira o valor: "))
    if menu == "2" :
        break
    if menu == "1" :
        num = 0
        num = int(input("Insira o númera para a lista: "))
        lista.append(num)

lista.sort()

menorNumero = lista[0]
maiorNumero = lista[-1]

for x in lista :
    soma += x

print("-------------------------------------")
print(lista)
print("-------------------------------------")
print(f"{menorNumero} é o menor número da sua lista")
print(f"{maiorNumero} é o maior número da sua lista")
print(f"{soma} é a soma dos seus números")