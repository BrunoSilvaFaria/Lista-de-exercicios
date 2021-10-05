#Faça um Programa que peça dois números e imprima o maior deles. 
num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
if num1 > num2:
	print(num1,"é maior")
elif num2 > num1:
	print(num2,"é maior")
else:
	print("Ambos os números são iguais")
