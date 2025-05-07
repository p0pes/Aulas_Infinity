#O programa deve permitir ao usuário
#cadastrar alunos. Cada aluno terá as seguintes
#informações: nome, idade e notas em três disciplinas:
#Matemática, Ciências e História. Os dados de cada aluno
#devem ser armazenados em um dicionário com as
#seguintes chaves:'nome',
#'idade','notas'. As notas devem ser armazenadas em uma tupla.

NotasP = {"matematica": "", "ciencias": "", "historia": ""}
NotasA = {"matematica": "", "ciencias": "", "historia": ""}
NotasM = {"matematica": "", "ciencias": "", "historia": ""}

pedro = {"Nome":"Pedro Lopes", "Idade":"22", "Notas":NotasP}
matheus = {"Nome":"Matheus Lopes", "Idade":"19", "Notas":NotasM}
andre = {"Nome":"Andre Lopes", "Idade":"49", "Notas":NotasA}

while True :
    print("->digite 1 para escolher alterar ou adicionar algum dado.\n->digite 2 para verificar os dados ja colocados\n->digite 3 para encerrar o programa")
    menu1 = str(input("-> : "))
    if menu1 == "2" :
        print("----------------------------------------------------")
        print(matheus)
        print(pedro)
        print(andre)
        print("----------------------------------------------------")
    elif menu1 == "3" :
        break
    elif menu1 == "1" :
        menu2 = str(input("Insira o nome do aluno que quer adicionar as notas: "))
        if menu2 == "pedro" :
            materiaP = str(input("Insira qual materia você quer alterar: "))
            if materiaP == "historia" :
                NotasP["historia"] = str(input("Insira a nota na materia historia: "))
            elif materiaP == "matematica" :
                NotasP["matematica"] = str(input("Insira a nota na materia matematica: "))
            elif materiaP == "ciencias" :
                NotasP["ciencias"] = str(input("Insira a nota na materia ciencias: "))
        if menu2 == "matheus" :
            materiaM = str(input("Insira qual materia você quer alterar: "))
            if materiaM == "historia" :
                NotasM["historia"] = str(input("Insira a nota na materia historia: "))
            elif materiaM == "matematica" :
                NotasM["matematica"] = str(input("Insira a nota na materia matematica: "))
            elif materiaM == "ciencias" :
                NotasM["ciencias"] = str(input("Insira a nota na materia ciencias: "))
        if menu2 == "andre" :
            materiaA = str(input("Insira qual materia você quer alterar: "))
            if materiaA == "historia" :
                NotasA["historia"] = str(input("Insira a nota na materia historia: "))
            elif materiaA == "matematica" :
                NotasA["matematica"] = str(input("Insira a nota na materia matematica: "))
            elif materiaA == "ciencias" :
                NotasA["ciencias"] = str(input("Insira a nota na materia ciencias: "))