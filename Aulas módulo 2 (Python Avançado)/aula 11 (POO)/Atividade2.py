#Crie um classe chamada pessoa com os atributos: nome, idade, peso, gênero

class Pessoa:
    def __init__(self, nome, idade, peso, genero) :
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = genero

Pedro = Pessoa("Pedro", 22, 100, "masculino")

