#Crie uma função que receba dois números e retorne a
#multiplicação deles.

def multiplicar (n1, n2) :
    return n1 * n2
   
n1 = int(input("Insira o primeiro numero: "))
n2 = int(input("Insira o segundo numero: "))

print(f"A multiplicação dos números é {multiplicar(n1,n2)}")