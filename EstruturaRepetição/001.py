#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. 
user = str(input("Digite seu nome de usuário: "))
senha = str(input("Digite sua senha: "))
while user == senha:
	print("Usuário e senha não podem ser iguais, por favor, digite novamente!")
	user = str(input("Digite seu nome de usuário: "))
	senha = str(input("Digite sua senha: "))
else:
	print("Login...")
