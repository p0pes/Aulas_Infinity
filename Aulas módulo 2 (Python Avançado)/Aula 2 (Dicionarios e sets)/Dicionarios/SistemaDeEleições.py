#Crie um sistema de eleições que faça um while true onde o usuario possa votar em um
#candidato ate digitar 0, armazene os votos em 0 e mostre os resultados

resultado = {
    "Lila" : 0,
    "Bolso" : 0
}

print("Digite 1 para votar no Bolso ou 2 para votar no Lila, Digite 0 para encerrar a votação")

ValorLila = 0
ValorBolso = 0

while True :
    voto = int(input("Insira o número da votação: "))
    if voto == 1 :
        ValorBolso += 1
    elif voto == 2 :
        ValorLila += 1
    elif voto == 0 :
        print("Votação encerrada!")
        break
    else :
        print("Insira um valor válido")
        continue

resultado["Bolso"] = ValorBolso
resultado["Lila"] = ValorLila

print(resultado)

if resultado["Bolso"] > resultado["Lila"] :
    print("Bolso ganhou!!!")

if resultado["Lila"] > resultado["Bolso"] :
    print("Lila ganhou!!!")