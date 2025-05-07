num = int(input("Insira o número: "))
mult = 0
res = 0

while mult < 10 :
    mult += 1
    res = num * mult
    if res % 3 == 0:
        print(res)