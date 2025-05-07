import math

def area_perimetro_quadrado(n1):
    
    area = n1 * n1
    per = 4 * n1

    return f"A area desse quadrado é : {area}. E o perimetro é : {per}."

def area_perimetro_retangulo(n1, n2):
    area = n1 * n2
    per = 2 * n1 + n2
    
    return f"A area desse retangulo é : {area}. E o perimetro é : {per}."

def area_perimetro_circulo(n1):
    
    area = math.pi * n1 ** 2
    circu = 2 * math.pi * n1

    return f"A area desse circulo é : {area}. E a circunferencia é : {circu}."