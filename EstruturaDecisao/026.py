'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                          Até 5 Kg           Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 

	Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. 
'''
quantMorango = float(input("Digite a quantidade de morango (kg): "))
quantMaca= float(input("Digite a quantidade de maca (kg): "))
quantTotal = quantMorango + quantMaca

if quantMorango >=1 and quantMorango <= 5:
	precoMorangoKg = 2.5
else:
	precoMorangoKg = 2.2

if quantMaca >=1 and quantMaca <= 5:
	precoMacaKg = 1.8
else:
	precoMacaKg = 1.5

valorMorango = quantMorango * precoMorangoKg
valorMaca = quantMaca * precoMacaKg
valorTotal = valorMorango + valorMaca

if quantTotal > 8 or valorTotal > 25:
	valorTotal *= 0.9

print("Valor a ser pago: R${:.2f} ".format(valorTotal))

