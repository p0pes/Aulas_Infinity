#Crie uma função que receba um horário e imprima
#"Bom dia!", "Boa tarde!" ou "Boa noite!"
#conforme o horário.
#6 ate 12 = bom dia
#12 ate 18 = boa tarde
#18 ate 6 = boa noite

def saudar_horario (horas) :
    if 6 <= horas < 12 :
        print("Bom dia!")
    elif 12<= horas < 18 :
        print("Boa tarde!")
    else :
        print("Boa noite")

horas = int(input("Insira qual é a hora aproximada agora: "))

saudar_horario(horas)