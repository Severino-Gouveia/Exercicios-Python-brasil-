# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em 
# latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

# Definir os valores das latas e galões
preco_lata = 80.00
capacidade_lata = 18
preco_galao = 25.00
capacidade_galao = 3.6

# Pedir ao usuário o tamanho da área em metros quadrados a ser pintada
tamanho_area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Calcular a quantidade de tinta necessária em litros com 10% de folga
tinta_necessaria = tamanho_area / 6 * 1.1

# Calcular o número de latas necessárias arredondando para cima
num_latas = math.ceil(tinta_necessaria / capacidade_lata)

# Calcular o preço total das latas
preco_total_latas = num_latas * preco_lata

# Calcular o número de galões necessários arredondando para cima
num_galoes = math.ceil(tinta_necessaria / capacidade_galao)

# Calcular o preço total dos galões
preco_total_galoes = num_galoes * preco_galao

# Calcular a mistura de latas e galões que resulta no menor desperdício de tinta
# Testar todas as combinações possíveis de latas e galões
melhor_preco = None
melhor_combinacao = None
for num_latas_atual in range(num_latas + 1):
    for num_galoes_atual in range(num_galoes + 1):
        # Calcular a quantidade total de tinta das latas e galões
        tinta_total = num_latas_atual * capacidade_lata + num_galoes_atual * capacidade_galao
        # Calcular o preço total da combinação
        preco_total_combinacao = num_latas_atual * preco_lata + num_galoes_atual * preco_galao
        # Verificar se a combinação atende à área necessária e tem o menor desperdício de tinta
        if tinta_total >= tinta_necessaria and (melhor_preco is None or preco_total_combinacao < melhor_preco):
            melhor_preco = preco_total_combinacao
            melhor_combinacao = (num_latas_atual, num_galoes_atual)

# Imprimir os resultados
print("Quantidade de tinta necessária: {:.2f} litros".format(tinta_necessaria))
print("Comprando apenas latas de 18 litros:")
print(" - Quantidade de latas: {}".format(num_latas))
print(" - Preço total: R$ {:.2f}".format(preco_total_latas))
print("Comprando apenas galões de 3,6 litros:")
print(" - Quantidade de galões: {}".format(num_galoes))
print(" - Preço total: R$ {:.2f}".format(preco_total_galoes))
print("Misturando latas e galões:")
print(" - Quantidade de latas: {}".format(melhor_combinacao[0]))
print(" - Quantidade de galões: {}".format(melhor_combinacao[1]))
print(" - Preço total: R$ {:.2f}".format(melhor_preco))
