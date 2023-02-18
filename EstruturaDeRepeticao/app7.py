#Faça um programa que leia 5 números e informe o maior número.

numbers = []

for i in range(5):
    number = int(input("Digite um número: "))
    numbers.append(number)

print("O maior número é", max(numbers))