# Criação da classe carro :

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo_carro = modelo
        self.cor_carro = cor
        self.ano_carro = ano
        self.velocidade_atual = 0

# Definição dos métodos

    def acelerar(self, velocidade):
        self.velocidade_atual += velocidade
        print(f"O carro acelerou e está a {self.velocidade_atual} km/h")   
    def frear(self, velocidade):
        if self.velocidade_atual >= velocidade:
            self.velocidade_atual -= velocidade
            print(f"O carro freoou e está a {self.velocidade_atual} km/h")
        else :
            self.velocidade_atual = 0
            print(f"O carro freoou e está parado")
    def ligar(self) :
        return f"O {self.modelo_carro} está ligado!"
    
# Definição de um objeto dentro dessa classe:

carro_pedro = Carro("Palio", "Preto", 2015)
carro_fodase = Carro("Ferrari", "Vermelho", 2023)

# Utilização dos métodos da classe

carro_pedro.acelerar(150)
carro_fodase.acelerar(20)

print(carro_pedro.ligar())

carro_pedro.frear(100)
carro_fodase.frear(50)