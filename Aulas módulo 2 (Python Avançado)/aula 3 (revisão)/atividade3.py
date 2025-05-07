#Faça um programa que peça 10 números inteiros,
#calcule e mostre a quantidade de números pares e a
#quantidade de números impares.

numPar = 0
numImpar = 0

for x in range(10) :
    num = 0
    num = int(input("Insira o núme que vai ser adicionado ao conjunto: "))
    res = num % 2
    if res == 0 :
        numPar += 1
    if res != 0 :
        numImpar += 1

print(f"Você inseriu\n{numPar} números pares.\n{numImpar} números impares.")