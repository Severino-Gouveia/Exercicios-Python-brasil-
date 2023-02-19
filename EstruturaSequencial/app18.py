# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de
#  Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link
#   (em minutos).

tamanho_arquivo = float(input("Digite o tamanho do arquivo em MB: "))
velocidade_link = float(input("Digite a velocidade do link de Internet em Mbps: "))

velocidade_mb = velocidade_link / 8
tempo = tamanho_arquivo / velocidade_mb / 60

print("O tempo aproximado de download é de {:.2f} minutos".format(tempo))


# Para resolver este problema, podemos usar a fórmula de tempo de download:
# tempo = tamanho_do_arquivo / (velocidade_do_link / 8)
# A velocidade do link é dada em Mbps (megabits por segundo), enquanto o tamanho 
# do arquivo é dado em MB (megabytes). Por isso, precisamos converter a velocidade
#  do link para megabytes por segundo (MB/s) antes de fazer o cálculo.

#  Pedimos ao usuário que digite o tamanho do arquivo em MB e a velocidade do link em Mbps.
# Em seguida, convertemos a velocidade do link para megabytes por segundo, dividindo por 8 
# (já que 1 byte = 8 bits).
# Usamos a fórmula para calcular o tempo de download em minutos.
# Finalmente, imprimimos o tempo aproximado de download em minutos, com duas casas decimais.