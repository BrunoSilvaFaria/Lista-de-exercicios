#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

 #   Para homens: (72.7*h) - 58
 #   Para mulheres: (62.1*h) - 44.7 

sexo = str(input("Digite seu sexo (M | F): ")).capitalize()
altura = float(input("Digite sua altura (ex.: 1.65): "))

if sexo[0:1] == "F":
	pesoIdeal = (62.1*altura) - 44.7 
else:
	pesoIdeal = (72.7*altura) - 58

print("Peso ideal: {:.0f}".format(pesoIdeal))

