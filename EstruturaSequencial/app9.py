#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print("A temperatura em Celsius é: {:.2f}".format(celsius))

# Na primeira linha, solicitamos ao usuário que insira a temperatura em graus Fahrenheit, e armazenamos o valor digitado na variável fahrenheit.
# Em seguida, usamos a fórmula para converter a temperatura de Fahrenheit para Celsius: (F - 32) * 5/9. Armazenamos o resultado na variável celsius.
# Por fim, imprimimos a temperatura em Celsius formatada com duas casas decimais usando o método format().