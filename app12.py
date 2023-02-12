# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro
#  entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. 
#  A saída deve ser conforme o exemplo abaixo:

print("Bem-vindo ao gerador de tabuada!")

numero = int(input("De qual número você deseja ver a tabuada? "))

if numero < 1 or numero > 10:
    print("Por favor, informe um número entre 1 e 10.")
else:
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
