id = int(input("Insira sua idade: "))
hab = str(input("Informe com S(sim) ou N(não) se você possui habilitação: "))

if hab == "S" and id >= 18 :
    print("Você possui habilitação e é maior de idade!")
elif hab == "N" and id >= 18 :
    print("Você não possui habilitação e é maior de idade!")
elif hab == "N" and id <= 18 :
    print("Você não possuio habilitação e não é maior de idade!")
else :
    print("você não deveria ter habilitação :(")