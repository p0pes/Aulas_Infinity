cpos = 0
cneg = 0

for x in range(10) :
    num = int(input("Insira o número: "))
    
    if num == 0 :
        break
    if num >= 0 :
        cpos += 1
        print(f"O número {num} é positivo")
    elif num <= 0 :
        cneg += 1
        print(f"O número {num} é negativo")
print(f"Você teve {cneg} números negativos e {cpos} números positivos!")