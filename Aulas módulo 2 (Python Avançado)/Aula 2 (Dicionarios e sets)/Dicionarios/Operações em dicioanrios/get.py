#Retorna o valor para a chave especificada se esta existir no
#dicionário, senão, será retornado um valor padrão definido. Caso
#este valor não seja definido, a função retornará None

dicionario = {
              "Pedro" : "22 anos",
              "Matheus" : "19 anos"
              }

print(dicionario.get("Pedro"))