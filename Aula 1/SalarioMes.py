salario = int (input("Insira seu ganho por mes: "))
horas_na_semana = int (input("Insira quantas horas voce trabalha na semana: "))
horas_no_mes = int (horas_na_semana * 4)
salario_por_hora = int (salario / horas_no_mes)
print(f"Voce recebe {salario_por_hora} por hora!")