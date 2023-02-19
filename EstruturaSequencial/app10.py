#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input("Digite a temperatura em graus Celsius: "))

fahrenheit = (celsius*1.8) + 32

print("A temperatura em graus Fahrenheit é: {:.1f}".format(fahrenheit))

# Neste exemplo, a função input() é utilizada para solicitar ao usuário que digite a temperatura em graus Celsius. 
# Em seguida, a fórmula para converter a temperatura de Celsius para Fahrenheit é utilizada 
# (F = C * 1.8 + 32) e o resultado é armazenado na variável fahrenheit. Por fim, a função print()
#  é utilizada para exibir o resultado na tela.