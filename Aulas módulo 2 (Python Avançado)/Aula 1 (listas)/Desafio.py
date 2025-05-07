#Suponha que você está gerenciando uma competição esportiva e tem
#uma lista de tuplas representando os resultados das equipes em
#diferentes modalidades. Cada tupla contém o nome da equipe, seguido
#por uma lista de pontuações obtidas em cada rodada da competição.

#1.Calcule a média das pontuações de cada equipe e armazene esses
#valores em uma nova lista chamada medias.
#2.Ordene a lista medias em ordem decrescente.
#3.Crie uma nova lista chamada classificacao que contém tuplas, onde
#cada tupla contém o nome da equipe e sua média de pontuações.
#4.Exiba na tela a classificação final das equipes, mostrando o nome da
#equipe e sua média, da equipe com a pontuação mais alta para a
#mais baixa.

res = [
    ["cornos", 10, 2, 9, 6],
    ["abutres", 3, 6, 2, 4],
    ["javalis", 9, 9, 10, 10],
    ["suricatos", 2, 3, 1, 5],
]

media = []
for eqp in res :
    medeqp = (eqp[1] + eqp[2] + eqp[3] + eqp[4])/4
    media.append(eqp[0])
media.sort(reverse=True)


classificacao = []
for eqp in res :
    media_equipes = (eqp[1] + eqp[2] + eqp[3])
    tupla_equipes = (eqp[0], media_equipes)
    classificacao.append(tupla_equipes) 
print(classificacao)

for med in media :
    for clas in classificacao :
        if med == clas[1] :
            print(clas[0], clas[1])