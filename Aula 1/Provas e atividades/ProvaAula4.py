ini = int(input("Insira o número onde o intervalo se inicia: "))
fim = int(input("Insira o número onde o intervalo se encerra: "))
soma = int(0)

for x in range(ini, (fim+1)) :
    if x % 2 == 0 :
        soma += x

if soma >= 1 :
    print(f"A soma dos números pares dentro deste intervalo é igual a: {soma}!")
else:
    print("Não há números pares no intervalo.")