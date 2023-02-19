# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#  utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite a sua altura em metros: "))
genero = input("Digite o seu gênero (M para Masculino e F para Feminino): ").upper()

if genero == "M":
    peso_ideal = (72.7 * altura) - 58
    print("O seu peso ideal é: {:.2f} kg".format( peso_ideal))
elif genero == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print("O seu peso ideal é: {:.2f} kg".format( peso_ideal))
else:
    print("Gênero inválido. Por favor, digite M para Masculino ou F para Feminino.")