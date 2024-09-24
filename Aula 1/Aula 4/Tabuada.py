num = int(input("Insira o numero : "))
resp = 1
for mult in range(1, 11) :
    print(f"{resp} x {num} = {mult * num}")
    resp += 1