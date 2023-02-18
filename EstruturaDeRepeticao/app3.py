
# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

def verificar_nome():
    nome = input("Escreva seu nome: ")
    while len(nome) < 3:
        print("Erro: seu nome precisa ter mais de 3 caracteres.")
        nome = input("Enter a string: ")
    print("Nome aceito:", nome)


def verificar_idade():
    idade = int(input("Escreva sua idade : "))
    while idade <0 or idade >100:
        print("Erro: vc precisa ter no minimo de 100 anos.")
        idade = int(input("Escreva seu nome: "))
    print("idade aceita:", idade)

def verificar_salario():
    salario = int(input("Escreva seu salario: "))
    while salario ==0 :
        print("Erro: salario precisa ser maior que 0.")
        salario = int(input("Escreva seu salario: "))
    print("salario aceito:", salario)
def verificar_genero():
  while True:
      genero = input("Digite seu genero M ou F: ").upper()
      if genero == "M" or genero == "F":
          break
      print("Entrada inválida, por favor tente novamente.")
  
  print("Você escolheu", genero)

def verificar_estado_civil():
  while True:
      e_civil = input("Digite seu estado civil no formato S, C, V ou D: ").upper()
      if e_civil =="S" or e_civil =="C" or e_civil =="V"or e_civil =="D" :
          break
      print("Entrada inválida, por favor tente novamente.")
  
  print("Você escolheu", e_civil)


verificar_nome()
verificar_idade()
verificar_salario()
verificar_genero()
verificar_estado_civil()