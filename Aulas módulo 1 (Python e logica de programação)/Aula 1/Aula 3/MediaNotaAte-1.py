nota = float(0)
soma = float(0)
quantidade = int(0)
resultado = float(0)

while nota != -1 :
    quantidade += 1
    nota = float((input("Insira a nota: ")))
    if nota == -1 :
        soma += 1
        quantidade -= 1
    soma += nota
    resultado = soma/quantidade
print(f"Voce inseriu {quantidade} notas e sua media foi de {resultado:.2f}")