# Faça um programa que receba dois números inteiros e gere os números inteiros
#  que estão no intervalo compreendido por eles.

def main():
    num1 = int(input("Insira o primeiro número inteiro: "))
    num2 = int(input("Insira o segundo número inteiro: "))

    if num1 < num2:
        for i in range(num1, num2 + 1):
            print(i, end=" ")
    else:
        for i in range(num2, num1 + 1):
            print(i, end=" ")

if __name__ == "__main__":
    main()