#Receba uma lista de números e use funções agregadoras
#para contar quantos valores são ímpares

lista =[28, 71, 52, 16, 99, 3, 55, 71, 82, 37, 12, 45, 8, 67, 23]
pares = []
impares = []


for x in lista :
    if x % 2 == 0 :
        pares.append(x)
    elif x % 2 != 0 :
        impares.append(x)

print(len(pares))
print(len(impares))