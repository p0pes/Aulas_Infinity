#Crie uma função chamada concatenar_strings que
#aceita um número variável de strings como argumentos
#posicionais (usando *args). A função deve concatenar
#todas as strings em uma única string e retorná-la.

def concatenar_string (*bosta) :
    string_inteira = ""

    for x in bosta :
        string_inteira += x
    return string_inteira

print(concatenar_string("coco", "lixo", "bosta"))