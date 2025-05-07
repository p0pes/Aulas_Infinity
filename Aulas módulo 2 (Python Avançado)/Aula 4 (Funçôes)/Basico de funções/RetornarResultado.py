#O return é usado para especificar o que
#a função deve retornar, sempre que usar
#o return e quiser exibir o resultado obtido,
#terá que ser usado o print(), pois o return
#não exibe nada na tela

def saudacao (nome) :
    return (f"olá {nome}")

resultado = saudacao("pedro")
print(resultado)