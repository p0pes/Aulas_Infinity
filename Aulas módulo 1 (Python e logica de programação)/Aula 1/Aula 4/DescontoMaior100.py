#5 preços diferentes, usar o for para calcular o total e colocar um desconto de 10%
desc = 0
val = 0

for x in range(5) :
    prc = float(input(f"Insira o valor: "))
    val += prc

    
if val > 100 : 
    desc = val *0.1
    val -= desc
    print(f"Você recebu desconto, seu valor é {val}.")
elif val <= 100 :
    print(f"Você não recebeu desconto, {val} é o seu valor.")