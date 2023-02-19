valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - imposto_renda - inss - sindicato

print("Salário Bruto: R$ %.2f" % salario_bruto)
print("Imposto de Renda (11%%): R$ %.2f" % imposto_renda)
print("INSS (8%%): R$ %.2f" % inss)
print("Sindicato (5%%): R$ %.2f" % sindicato)
print("Salário Líquido: R$ %.2f" % salario_liquido)

# primeiro pedimos ao usuário para digitar o valor da hora trabalhada e o número de horas trabalhadas.
# Em seguida, calculamos o salário bruto multiplicando o valor da hora pelo número de horas trabalhadas.
# Depois, calculamos os descontos de imposto de renda, INSS e sindicato, multiplicando o salário bruto 
# por suas respectivas taxas. Finalmente, calculamos o salário líquido subtraindo os descontos do salário bruto.
# Note que estamos usando formatação de string (usando o operador %) para imprimir os valores com apenas
# duas casas decimais (R$ X,XX).