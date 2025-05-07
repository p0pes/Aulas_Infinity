prc = float(input("Insira o valor do produto: "))
qnt = int(input("Insira a quantidade do produto: "))

prc *= qnt

if qnt >= 10 :
    desc = prc * 0.1
    prc -= desc

print(f"O valor total é {prc}")
