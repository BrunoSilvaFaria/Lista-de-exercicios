#Faça um Programa que leia três números e mostre o maior e o menor deles. 
num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
num3 = float(input("Digite um número: "))
if num1 > num2 and num1 > num2:
	if num2 > num3:
		print(num3,"é menor")
	else:
		print(num2,"é menor")
	print(num1,"é maior")
elif num2 > num1 and num2 > num3:
	if num1 > num3:
		print(num3,"é menor")
	else:
		print(num1,"é menor")
	print(num2,"é maior")
elif num3 > num1 and num3 > num2:
	if num1 > num2:
		print(num2,"é menor")
	else:
		print(num1,"é menor")
	print(num3,"é maior")
else:
	print("Números iguais")
