# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

num1 = int(input("Digite o primeiro numero inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = float( input("Digite um número Real: "))

resultado1 = (2 * num1 * (num2 / 2))
resultado2 = (3 * num1) + num3
resultado3 = num3 ** 3

print("O produto do dobro do primeiro com metade do segundo é: ", resultado1)
print("A soma do triplo do primeiro com o terceiro é: ", resultado2)
print("O terceiro elevado ao cubo é: ", resultado3)

# Neste exemplo, a função input() é utilizada para solicitar ao usuário que digite 2 números inteiros e 1 
# número real. Em seguida, cada um dos cálculos descritos é realizado e o resultado é armazenado em uma 
# variável correspondente. Por fim, a função print() é utilizada para exibir os resultados na tela.
