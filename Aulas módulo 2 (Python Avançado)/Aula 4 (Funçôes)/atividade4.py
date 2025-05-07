#Crie uma função que receba dois números e retorne a
#subtração do primeiro pelo segundo.

def subtracao (n1, n2) :
    return n1 - n2
   
n1 = int(input("Insira o primeiro numero: "))
n2 = int(input("Insira o segundo numero: "))

print(f"A subtração dos números é {subtracao(n1,n2)}")