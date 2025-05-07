lista = []
animais_grandes = []
animais_pequenos = []

for x in range(5) : 
    ani = input("Insira até 5 nomes de animais para a sua lista: ")
    lista.append(ani)
    
print("Lista completa de animais: ")
for animal in lista :
    print(animal)
    if len(animal) >= 5 :
        animais_grandes.append(animal)
    elif len(animal) < 5 :
        animais_pequenos.append(animal)
    else :
        continue
print('----------------------------------')
print("Animais com mais de 5 letras: ")
for animal in animais_grandes :
    print(animal)

print('----------------------------------')
print("Animais com menos de 5 letras: ")
for animal in animais_pequenos :
    print(animal)