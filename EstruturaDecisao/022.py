#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento. 
num = float(input("Digite um numero: "))
if num // 1 == num:
	print("Número inteiro")
else:
	print("Número decimal")
