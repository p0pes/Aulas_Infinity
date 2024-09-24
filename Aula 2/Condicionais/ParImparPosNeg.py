n1 = float(input("Insira um nunero inteiro para ser verificado :"))
res = n1 % 2

if res == 0 and n1 > 0 :
    print(f"Seu número {n1} é par e positivo")
elif res == 0 and n1 < 0 :
    print(f"Seu número {n1} é par e negativo")
elif res != 0 and n1 > 0 :
    print(f"Seu número {n1} é impar e positivo")
elif res != 0 and n1 < 0 :
    print(f"Seu número {n1} é impar e negativo")
elif n1 == 0 :
    print("seu numero é 0")