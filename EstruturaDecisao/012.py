#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. 
listaDias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
dia = int(input("Digite um dia da semana(1-Domingo | 7-Sábado):"))
if dia >= 1 and dia <= 7:
	print(listaDias[dia-1])
else:
	print("Valor inválido")
