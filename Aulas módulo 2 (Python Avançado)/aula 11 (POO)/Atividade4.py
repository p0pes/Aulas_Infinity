#Crie uma classe Calculadora que tenha métodospara realizar operações matemáticas básicas (+ , - ,*, / ).

class Calculadora :
    def __init__ (self, num1, num2, operacao) :
        
        self.num1 = num1
        self.num2 = num2
        self.operacao = operacao

    def soma(self) :
            return self.num1 + self.num2
        
    def subtracao(self) :
            return self.num1 - self.num2
        
    def mult(self) :
            return self.num1 * self.num2
        
    def divisao(self) :
            return self.num1 / self.num2
        
operacao = str(input("Insira a operação a ser realizada (+, -, *, /): "))
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

calculo = Calculadora(num1, num2, operacao)

if calculo.operacao == "+" :
    print(calculo.soma())
elif calculo.operacao == "-" :
    print(calculo.subtracao())
elif calculo.operacao == "*" :
    print(calculo.mult())
elif calculo.operacao == "/" :
    print(calculo.divisao())