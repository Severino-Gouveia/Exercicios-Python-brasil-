# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população 
# de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários 
# para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e
count =0
while count < 2:
  count += 1
  A = float(input("DIGITE A POPULAÇÃO : "))
  taxa_A = float(input("DIGITE A PORCENTAGEM NO FORMATO 0,00 : "))
  B = 200000
  taxa_B = 0.015
  anos = 0


  while A <= B:
    A = A + (A * taxa_A)
    B = B + (B * taxa_B)
    anos = anos + 1

  print("Serão necessários", anos, "anos para que a população do país A ultrapasse ou iguale a população do país B")

 