'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

    Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro

    Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro 

	Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90. 
'''
litro = float(input("Digite o valor de litro vendido: "))
tipoCombus = str(input("Tipo de combustível (A-álcool | G-gasolina): ")).capitalize()
pagar = True
if tipoCombus == "G":
	if litro > 1 and litro <= 20:
		valorPago = (litro * 2.5) * 0.96
	elif litro > 20:
		valorPago = (litro * 2.5) * 0.94
	else:
		pagar = False

if tipoCombus == "A":
	if litro > 1 and litro <= 20:
		valorPago = (litro * 1.9) * 0.97
	elif litro > 20:
		valorPago = (litro * 1.9) * 0.95
	else:
		pagar = False

if pagar == True:
	print("Valor total a ser pago: R$ ",valorPago)
else:
	print("Valor invalido")

		

