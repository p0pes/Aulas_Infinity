num = 0
for x in range(1, 51) :
    if x % 2 == 0 :
        num += x
    elif x % 2 != 0 :
        num += 0
print(num)