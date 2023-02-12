
def main():
    num1 = int(input("Insira o primeiro número inteiro: "))
    num2 = int(input("Insira o segundo número inteiro: "))

    intervalo = []
    if num1 < num2:
        for i in range(num1, num2+1):
            intervalo.append(i)
    else:
        for i in range(num2, num1+1):
            intervalo.append(i)

    print("Números no intervalo:", intervalo)
    print("Soma dos números:", sum(intervalo))

if __name__ == '__main__':
    main()

# Este programa primeiro pede ao usuário para inserir dois números inteiros. 
# Em seguida, verifica se o primeiro número é menor que o segundo ou vice-versa, e usa o laço "for" para gerar uma lista de 
# números inteiros no intervalo. Por fim, a função sum() é usada para calcular a soma dos números no intervalo.