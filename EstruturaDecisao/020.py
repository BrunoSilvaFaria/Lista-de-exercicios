'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1. 
'''
valor = int(input("Digite o valor que deseja sacar (10-600): "))
cem =  valor // 100
cinq = valor % 100 // 50
dez = valor % 100 % 50 // 10
cinc = valor % 100 % 50 % 10 // 5
um = valor % 100 % 50 % 10 % 5 // 1

def imprimeValor(num, valorNome):
	if num == 1:
		print("{} nota de {}".format(num, valorNome))
	elif num > 1:
		print("{} notas de {}".format(num, valorNome))
	else: 
		print(end="")

if valor >= 10 and valor <= 600:
	imprimeValor(cem, "100")
	imprimeValor(cinq, "50")
	imprimeValor(dez, "10")
	imprimeValor(cinc, "5")
	imprimeValor(um, "1")
else:
	print("Valor invalido")
