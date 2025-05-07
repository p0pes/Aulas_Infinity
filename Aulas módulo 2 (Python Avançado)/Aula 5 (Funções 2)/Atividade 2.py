#Crie um programa que define uma função
#calcular_area_retangulo que recebe dois argumentos,
#comprimento e largura de um retângulo, e retorna a
#área desse retângulo. Em seguida, o programa deve
#solicitar ao usuário que insira o comprimento e a
#largura e imprimir a área calculada.

def calcular_area(c, l) :
    return c * l

c = float(input("Insira o valor do comprimento do retângulo: "))
l = float(input("Insira o valor da largura do retângulo: "))

print(f"O valor da area do retangulo é {calcular_area(c, l)}")