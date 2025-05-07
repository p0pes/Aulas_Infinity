Id1 = int (input("Insira a primeira idade: "))
Id2 = int (input("Insira a segunda idade: "))

if Id1 > Id2 :
    print(f"A primeira idade é maior do quer a segunda!")
elif Id1 < Id2 :
    print(f"A segunda idade é maior do que a primeira!")
elif Id1 == Id2 :
    print(f"As duas idades são iguais!")