#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida. 
data = str(input("Digite uma data(dd/mm/aaaa): "))
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6])

diaBool = False
mesBool = False
anoBool = False

if dia >= 1 and dia <= 31:
	diaBool = True
if mes >= 1 and mes <= 12:
	mesBool = True
if ano >=1:
	anoBool = True

if diaBool == True and mesBool == True and anoBool == True:
	print("Data Valida")
else:
	print("Data invalida")

