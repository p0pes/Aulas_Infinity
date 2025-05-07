# Criação da classe carro :

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo_carro = modelo
        self.cor_carro = cor
        self.ano_carro = ano
        self.velocidade = 0

# Definição de im objeot dentro dessa classe:

carro_pedro = Carro("Palio", "Preto", 2015)

carro_fodase = Carro("Ferrari", "Vermelho", 2023)

# Trabalhar com dados especificos desse objeto usando esse método

print(carro_fodase.cor_carro)
print(carro_pedro.cor_carro)

# Alterando um dado especifico, não altera nada da classe

carro_pedro.cor_carro = "azul"

print(carro_pedro.cor_carro)