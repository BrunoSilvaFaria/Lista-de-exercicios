"""
	Faça um programa para uma loja de tintas. 
	O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
	Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
	Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 
"""
areaPintar = float(input("Digite a área que deseja pintar: "))

# 1 lata pinta 54m
metroLata = 54

quantidadeLatas = areaPintar / metroLata
preçoLatas = 80

# Verifica a quantidade de latas e adiciona uma lata a mais, se necessário.
if areaPintar % 54 >= 1:
	# Transforma em número inteiro e adiciona mais uma lata
	quantidadeLatas = quantidadeLatas // 1 + 1

valorPagar = quantidadeLatas * preçoLatas

# Função necessária para imprimir a quantidade de latas e o valor a ser pago
def imprimir():
	print("Quantidade de lata(s): {:.0f}".format(quantidadeLatas))
	print("Valor a ser pago: R${:.2f}".format(valorPagar))

imprimir()
