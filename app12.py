
print("Bem-vindo ao gerador de tabuada!")

numero = int(input("De qual número você deseja ver a tabuada? "))

if numero < 1 or numero > 10:
    print("Por favor, informe um número entre 1 e 10.")
else:
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
