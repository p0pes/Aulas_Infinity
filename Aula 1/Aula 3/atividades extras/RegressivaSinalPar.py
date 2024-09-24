num = int(input("Insira o número: "))

while num != 0 :
    res = num % 2
    if res == 0 :
        print(f"{num} é um número par.")
    else :
        print(f"{num}")
    num -= 1