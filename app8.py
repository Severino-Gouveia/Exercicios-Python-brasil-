#Faça um programa que leia 5 números e informe a soma e a média dos números.
numeros = []

for i in range(3):
    numero= int(input("Digite um número: "))
    numeros.append(numero)

soma_dos_mumeros = sum(numeros)
media = soma_dos_mumeros / len(numeros)

print("A soma dos números é", soma_dos_mumeros)
print("A média dos números é", media)
