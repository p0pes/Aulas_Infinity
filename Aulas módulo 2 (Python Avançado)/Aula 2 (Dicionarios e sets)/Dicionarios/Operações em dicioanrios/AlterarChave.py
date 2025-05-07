#Se a chave já existir no dicionário, terá seu valor
#sobrescrito. Se a chave não existir, ela será criada e o valor
#será atribuída a ela

dicionario = {
              "Pedro" : "22 anos",
              "Matheus" : "19 anos"
              }

print(dicionario)

dicionario["Pedro"] = "23 anos"

print(dicionario)