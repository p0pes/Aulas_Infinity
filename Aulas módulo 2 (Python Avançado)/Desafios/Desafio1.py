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

menu = str(input("Insira o nome do aluno que quer adicionar as notas: "))

if menu == "pedro" :
    materiaP = str(input("Insira qual materia você quer alterar: "))
    if materiaP == "historia" :
        NotasP["historia"] = str(input("Insira a nota na materia historia: "))
    elif materiaP == "matematica" :
        NotasP["matematica"] = str(input("Insira a nota na materia matematica: "))
    elif materiaP == "ciencias" :
        NotasP["ciencias"] = str(input("Insira a nota na materia ciencias: "))
if menu == "matheus" :
    materiaM = str(input("Insira qual materia você quer alterar: "))
    if materiaM == "historia" :
        NotasM["historia"] = str(input("Insira a nota na materia historia: "))
    elif materiaM == "matematica" :
        NotasM["matematica"] = str(input("Insira a nota na materia matematica: "))
    elif materiaM == "ciencias" :
        NotasM["ciencias"] = str(input("Insira a nota na materia ciencias: "))
if menu == "andre" :
    materiaA = str(input("Insira qual materia você quer alterar: "))
    if materiaA == "historia" :
        NotasA["historia"] = str(input("Insira a nota na materia historia: "))
    elif materiaA == "matematica" :
        NotasA["matematica"] = str(input("Insira a nota na materia matematica: "))
    elif materiaA == "ciencias" :
        NotasA["ciencias"] = str(input("Insira a nota na materia ciencias: "))

print(matheus)
print(pedro)
print(andre)