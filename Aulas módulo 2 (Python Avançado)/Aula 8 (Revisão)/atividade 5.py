#Dado um dicionário que representa as vendas de
#produtos, encontre o produto mais vendido (ou os
#produtos mais vendidos, se houver um empate).

produto_mais_vendido = []

produtos = {
    "Camiseta": 120,
    "Calça Jeans": 85,
    "Tênis Esportivo": 200,
    "Bolsa de Couro": 55,
    "Relógio de Pulso": 150,
    "Óculos de Sol": 180,
    "Meias Esportivas": 300,
    "Tênis Casual": 130,
    "Cinto de Couro": 70,
    "Boné": 160,
    "Blusa de Frio": 110,
    "Sapatênis": 95,
    "Mochila": 140,
    "Chapéu": 60
}
valoralto = (max(produtos.values()))

for produto, vendas in produtos.items():
    if vendas == valoralto :
        produto_mais_vendido.append(produto)

print(produto_mais_vendido)