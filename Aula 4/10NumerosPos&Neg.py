pos = 0
neg =0

for list in range(0, 10) :
    num = int(input("Insira o numero: "))
    if num > 0 :
        print(f"{num} é positivo")
        pos += 1
    elif num < 0 :
        print(f"{num} é negativo")
        neg += 1
    elif num == 0 :
        print(f"{num} é zero")
print(f"Sua sequencia tem {pos} números positivos e {neg} números negativos!")