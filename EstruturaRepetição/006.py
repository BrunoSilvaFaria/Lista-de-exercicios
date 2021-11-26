#Faça um programa que leia 5 números e informe o maior número. 
maior = 0
for x in range(1, 6):
	num = float(input("Digite um número: "))
	if num > maior:
		maior = num
print(maior)
