"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento. 
"""
salarioAtual = float(input("Digite seu salário atual: "))
percentualAplicado = 0
valorAumento = 0
novoSalario = 0

if salarioAtual <= 280:
	percentualAplicado = 20
elif salarioAtual > 280 and salarioAtual <=700:
	percentualAplicado = 15
elif salarioAtual > 700 and salarioAtual <= 1500:
	percentualAplicado = 10
else:
	percentualAplicado = 5

valorAumento = salarioAtual * percentualAplicado / 100
novoSalario = salarioAtual + valorAumento
def imprimir():
	print("Salário antes do ajuste: R${:.2f}".format(salarioAtual))
	print("Percentual aplicado: {}%".format(percentualAplicado))
	print("Valor do aumento: R${:.2f}".format(valorAumento))
	print("Novo Salário: R${:.2f}".format(novoSalario))

imprimir()
