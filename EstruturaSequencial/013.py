"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas
"""
#Peso dos peixes
peso = float(input("Digite quanto(s) kg de peixe pescou: "))

# Excesso de peixe
excessoPeso = peso - 50

# Valor Multa
multa = 4
multaPagar = excessoPeso * multa

# Verificando se há excesso e informando o valor a ser pago da multa
if excessoPeso >= 1:
	print("Peso excedeu: {:.2f}kg".format(excessoPeso))
	print("Multa a ser paga: R${:.2f}".format(multaPagar))
else:
	print("Parabéns. Não excedeu o limite de peso, não é necessário pagar multa")
