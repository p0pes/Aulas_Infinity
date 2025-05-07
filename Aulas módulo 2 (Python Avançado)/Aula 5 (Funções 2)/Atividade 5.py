#Crie uma função que aceita uma lista de números e use
#a função filter para retornar uma nova lista contendo
#apenas os números pares da lista de entrada.

lista = []

for x in range(5) :
    lista.append(int(input("Insira os números para serem verificados: ")))

def verificar_numeros (lista) :
    pares = []
    for num in lista :
        if num % 2 == 0 :
            pares.append(num)
    return pares

lista_pares = verificar_numeros(lista)
        
print(f"Os números pares são: {lista_pares}")