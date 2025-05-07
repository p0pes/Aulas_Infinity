#Peça a idade ao usuario e diga em que fase da vida eçe está baseado em sua idade

idade = int(input("Insira a sua idade: "))

if idade < 12 :
    print(f"Sua idade é {idade}, você é criança.")
if idade <= 17 :
    print(f"Sua idade é {idade}, você é adolescente.")
if idade <= 59 :
    print(f"Sua idade é {idade}, você é adulto.")
if idade > 59 :
    print(f"Sua idade é {idade}, você é idoso.")