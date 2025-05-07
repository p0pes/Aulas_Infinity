#Crie um programa que permite ao usuário calcular a
#área e operímetro de formas geométricas simples,
#como quadrados, retângulos e círculos. Use funções
#matemáticas do módulo math para realizar os cálculos.

from funcoes import *

n1, n2 = 0, 0


print("Insira um dos seguintes comandos para seguir com os calculos de area e perimetro:\n"
      "1 - Area do quadrado.\n"
      "2 - Area do retangulo.\n"
      "3 - Area do circulo.\n")

menu = str(input("Insira o número: "))

if menu == "1" :
    n1 = int(input("Insira o lado do quadrado: "))
    print(area_perimetro_quadrado(n1))
elif menu == "2" :
    n1 = int(input("Insira o primeiro lado do retangulo: "))
    n2 = int(input("Insira o segundo lado do retangulo: "))
    print(area_perimetro_retangulo(n1, n2))
elif menu == "3" :
    n1 = float(input("Insira o raio do circulo: "))
    print(area_perimetro_circulo(n1))