"""
	Faça um Programa para uma loja de tintas.
	O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
	Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. 
"""

areaPintar = float(input("Digite a área que deseja pintar: "))

# 1 lata pinta 144m
metroLata = 144

# 1 Galão pinta 21.6m
metroGalao = 21.6


quantidadeLatas = areaPintar / metroLata
precoLatas = 80

quantidadeGalao = areaPintar / metroGalao
precoGalao = 25

# Verifica a quantidade de latas e adiciona uma lata a mais, se necessário.
if areaPintar % 144 >= 1:
	# Transforma em número inteiro e adiciona mais uma lata
	quantidadeLatas = quantidadeLatas // 1 + 1

# Verifica a quantidade de galões adiciona um galão a mais, se necessário.
if areaPintar % 21.6>= 1:
	# Transforma em número inteiro e adiciona mais um galao
	quantidadeGalao = quantidadeGalao // 1 + 1

valorPagarLatas = quantidadeLatas * precoLatas
valorPagarGalao= quantidadeGalao * precoGalao

# Misturar Galões e latas
def mistura():
	quantidadeLatasMes = areaPintar // metroLata
	quantidadeGalaoMes = (areaPintar - (quantidadeLatasMes * 144)) / metroLata

	if areaPintar <= 144:
		print("Felizmente, não é necessário mesclar!")

	# Verifica a quantidade de galões adiciona um galão a mais, se necessário.
	elif (areaPintar - (quantidadeLatasMes * 144)) % 21.6 > 0:
		# Transforma em número inteiro e adiciona mais um galao
		quantidadeGalaoMes = quantidadeGalaoMes // 1 + 1

		print("Quantidade de lata(s): {:.0f}".format(quantidadeLatasMes))
		print("Quantidade de galo(es): {:.0f}".format(quantidadeGalaoMes))
		valorTotal = quantidadeLatasMes * precoLatas + quantidadeGalaoMes * precoGalao
		print("Valor a ser pago: R${:.2f}".format(valorTotal))


def imprimir():
	print("=======Latas========")
	print("Quantidade de lata(s): {:.0f}".format(quantidadeLatas))
	print("Valor a ser pago: R${:.2f}".format(valorPagarLatas))

	print("=======Galões========")
	print("Quantidade de galo(s): {:.0f}".format(quantidadeGalao))
	print("Valor a ser pago: R${:.2f}".format(valorPagarGalao))

	print("=======Latas e Galões========")
	mistura()

imprimir()

