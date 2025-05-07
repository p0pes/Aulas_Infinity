pal = str(input("Insira a palavra: "))
vog = 0

for letras in pal :
    if letras.lower() in "aeiou" :
        vog += 1
print(f"Sua palavra possui {vog} vogais")