n1 = float (input("Insira a primeira nota: "))
n2 = float (input("Insira a segunda nota: "))

if n1 >= 6 and n2 >= 6 :
    print(f"As duas notas são maiores do que 6!")
elif n1 >= 6 and n2 < 6 :
    print(f"Apenas a primeira nota é maior do que 6!")
elif n1 < 6 and n2 >= 6 : 
    print(f"Apenas a segunda nota é maior do que 6!")
elif n1 < 6 and n2 < 6 :
    print(f"As duas notas são menores do que 6!")