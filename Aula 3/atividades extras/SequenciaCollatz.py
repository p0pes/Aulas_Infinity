num = int(input("Insira um numero: "))

while num > 1 :
    print(num)
    if (num%2) == 0 :
        num /= 2
    else :
        num = (num * 3) + 1
print(num)