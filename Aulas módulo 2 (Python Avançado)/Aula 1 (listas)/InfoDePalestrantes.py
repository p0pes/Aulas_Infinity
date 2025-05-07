#Crie uma tupla para representar as informações de três
#palestrantes, cada uma contendo o nome, o tema da
#palestra e a instituição à qual estão vinculados.
#Exiba na tela as informações do terceiro palestrante,
#incluindo nome, tema da palestra e instituição.

palestrantes = (

("Roberto", "Ensino a distãncia", "Colegio slaoq"),
("Robson", "Fisiculturismo", "Unifacs"),
("Renato", "Segurançca de dados", "Unijorge",)

)

print("------------------------------------------")
print(f"Nome do terceiro palestrante:", palestrantes[2][0])
print(f"Tema do terceiro palestrante:", palestrantes[2][1])
print(f"Instituição do terceiro palestrante:", palestrantes[2][2])
print("------------------------------------------")