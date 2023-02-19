peso = float(input("Digite o peso do peixe : "))

if peso > 50:
    peso_excedente = peso - 50
    multa = peso_excedente * 4.0
    print("Peso excedente: {:.2f} kg".format (peso_excedente))
    print("Valor da multa: R$ ", multa)
else:
    print("O peso do peixe está dentro do limite permitido.")
