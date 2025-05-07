#Faça um programa que peça para n pessoas a sua
#idade, ao final o programa devera verificar se a média
#de idade da turma varia entre 0 e 25, 26 e 60 e maior
#que 60; e então, dizer se a turma é jovem, adulta ou
#idosa, conforme a média calculada.

print("Insira a seguir o valor das idades da turma um por um")
contador = -1
idade = 0

alunos = int(input("Insira o número de alunos na sala: "))

for x in range(alunos) :
    contador += 1
    idade += int(input(f"Insira a idade do aluno {contador + 1}: "))

med = idade/alunos

print("-----------------------------------------------------------")

if med < 25 :
    print(f"A média de idades da sala é {med},\nsua turma é jovem!")
elif med < 60:
    print(f"A média de idades da sala é {med},\nsua turma é adulta!")
elif med >= 60:
    print(f"A média de idades da sala é {med},\nsua turma é idosa!")