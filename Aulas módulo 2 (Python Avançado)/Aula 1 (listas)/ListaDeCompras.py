#defifnir o elemento em uma lista e inserir um item "[]" em todos eles

lista = [
    "2 pacotes de arroz",
    "3 pacotes de feijão",
    "4 kg de carne",
    "2kg de carne de porco",
    "1kg de bacon",3
]

ins = str(input("Insira o item que quer colocar na lista: "))

lista.append(ins)

print("Lista de compras:\n")

for x in lista :
    print(f"[ ] {x}")