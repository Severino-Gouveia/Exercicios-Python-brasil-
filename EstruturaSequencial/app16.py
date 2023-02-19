# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
# a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a
# tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas
# de tinta a serem compradas e o preço total.

area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
litros_necessarios = area / 3
latas_necessarias = int(litros_necessarios / 18)
if latas_necessarias * 18 < litros_necessarios:
    latas_necessarias += 1

preco_total = latas_necessarias * 80

print("Quantidade de latas de tinta a serem compradas: %d" % latas_necessarias)
print("Preço total: R$ %.2f" % preco_total)

# Neste exemplo, primeiro pedimos ao usuário que digite o tamanho em metros quadrados da área a ser pintada. Em seguida,
# calculamos a quantidade de litros de tinta necessários dividindo a área por 3. Depois, calculamos o
# número de latas necessárias dividindo a quantidade de litros necessários por 18 e arredondando para 
# cima usando a função int(). Se a quantidade de latas necessárias não for suficiente para cobrir todos
# os litros necessários, adicionamos uma lata extra. Finalmente, calculamos o preço total multiplicando
# o número de latas necessárias pelo preço de cada lata (R$ 80,00).
# Note que estamos usando formatação de string (usando o operador %) para imprimir os valores com apenas 
# duas casas decimais (R$ X,XX).