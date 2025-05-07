#Crie um programa que solicita ao usuário que insira três
#notas e, em seguida, calcule a média dessas notas
#usando uma função. A função deve receber as três
#notas como argumentos e retornar a média. Por fim, o
#programa deve imprimir a média calculada.

def calcular_nota(n1, n2, n3) :
    return (n1 + n2 + n3)/3

n1 = int(input("Insira a primeira nota: "))
n2 = int(input("Insira a segunda nota: "))
n3 = int(input("Insira a terceira nota: "))

print(f"A média dessas notas é {calcular_nota(n1, n2, n3)}")