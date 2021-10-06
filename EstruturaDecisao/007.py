#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. . 
num1 = float(input("Digite o preço do 1º produto: "))
num2 = float(input("Digite o preço do 2º produto: "))
num3 = float(input("Digite o preço do 3º produto: "))
if num1 < num2 and num1 < num2:
	print("1º produto compensa mais")
elif num2 < num1 and num2 < num3:
	print("2º produto compensa mais")
elif num3 < num1 and num3 < num2:
	print("3º produto compensa mais")
else:
	print("Produtos com preços iguais")
