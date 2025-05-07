#Crie uma função que receba dois números e retorne a
#soma deles.

def soma (n1, n2) :
    return f"{n1 + n2}"

n1 = int(input("Insira o valor do primeiro numero: "))
n2 = int(input("Insira o valor do segundo numero: "))

print(f"a soma desses números é : {soma(n1, n2)}")