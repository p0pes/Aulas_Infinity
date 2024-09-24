num = 0
while num <= 99 :
    som = int(input(f"Insia o numero da soma: "))
    num += som
    if num == 100 :
        print(f"Suas somas terminaram em 100!")
    elif num > 100 :
        print("Suas somas passaram de 100!")
    elif num < 100 :
        print(f"O numero {num} é menor do que 100!")
