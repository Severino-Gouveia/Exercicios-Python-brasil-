# valor_hora = float(input("Digite o valor que voçê ganha por hora: "))
# horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# salario = valor_hora * horas_trabalhadas

# print(f"O seu sálario total no mês é de {salario} reais ")


salario = float(input("Qual é o seu salário mensal? "))
horas_trabalhadas = 160 # supondo uma jornada de trabalho de 40 horas semanais

valor_hora = salario / horas_trabalhadas

print("Seu salário é de R$ {:.2f} por hora.".format(valor_hora))
