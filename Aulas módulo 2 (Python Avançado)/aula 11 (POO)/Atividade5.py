#Crie uma classe chamada Fatura , a classe Fatura deve incluir
#s seguintes atributos o nome do item; o preço unitário do item;
#quantidade de item a ser faturado; valor total da fatura; Sua
#classe deve ter um construtor que inicialize todos os atributos
#menos o valor total da fatura. Forneça um método chamado
#gerar_fatura que calcula o valor da fatura (isto é, multiplicar a
#quantidade pelo preço por item).

class Fatura :
    def __init__ (self, nome, preco, quantidade) :
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def gerar_fatura(self) :
        self.total = self.preco * self.quantidade
        return self.total

fatura = Fatura("Tenis", 399.99, 4)
valor_total = fatura.gerar_fatura()
print(valor_total)