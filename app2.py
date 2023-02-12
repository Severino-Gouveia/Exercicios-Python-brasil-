# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.
nome=input("Digite seu nome :")
senha=input("digite sua senha :")
while senha==nome:
    senha=input("Senha inválida :")
else:
    print(f"Nome cadastrado :{nome} \nSenha cadastrada : {senha}")