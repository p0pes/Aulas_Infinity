#receber 3 numeros em uma lista e tirar a media deles

lista = []

x = float(input("insira a primeira nota:"))
y = float(input("insira a segunda nota:"))
z = float(input("insira a terceira nota:"))

lista.insert(0,x)
lista.insert(1,y)
lista.insert(2,z)

med = (lista[0]+lista[1]+lista[2])/3
print(med)