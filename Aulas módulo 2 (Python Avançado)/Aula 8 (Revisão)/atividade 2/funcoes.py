def adicionar_produto(lista_produtos, produto, qnt, val):

    produto = {"Nome" : produto, "Quantidade" : qnt, "Valor" : val}
    lista_produtos.append(produto)

def remover_produto(exprod, lista_produtos):
    
    for x in lista_produtos:
        if x["Nome"] == exprod:
            lista_produtos.remove(x)
        else:
            print(f"Produto '{exprod}' não encontrado.")
            break

def atualizar_produto():
    pass