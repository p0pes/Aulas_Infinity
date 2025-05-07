def inverter (string) :
    return string[::-1]

def contar_letras (string) :
    return len(string)

def palindro(string) : 
    check1 = string.lower()
    check2= string[::-1]

    if check1 == check2 :
        return f"{string} é um palindromo!"
    else :
        return f"{string} não é um palindromo"

def exibir_vertical(string) :
    lista = []

    for x in string :
         lista.append(x)
    return lista