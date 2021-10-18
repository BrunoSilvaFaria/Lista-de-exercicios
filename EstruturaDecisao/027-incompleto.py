'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                          Até 5 Kg           Acima de 5 Kg
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. 

Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar. 
'''
print("=====Tipos de carne Disponivel=====")
print("1------ File Duplo\n2------ Alcatra\n3------ Picanha")
tipoCarne = ["Filé Duplo", "Alcatra", "Picanha"]
escolha = int(input("Escolha o tipo de carne que deseja: "))
quant = float(input("Digite quantos kg deseja comprar: "))
def calculaValor(quant, valorMin, valorMax):
	global valorTotal
	if quant >= 1 and quant <= 5:
		valorTotal = quant * valorMin
	else:
		valorTotal = quant * valorMax

if escolha == 1:
	calculaValor(quant, 4.9, 5.8)
elif escolha == 2:
	calculaValor(quant, 5.9, 6.8)
elif escolha == 3:
	calculaValor(quant, 6.9, 7.8)
else:
	print("Valor invalido")

print("=====Formas de Pagamento====")
print("1-----Dinheiro\n2----- Cartão de crédito\n3-----Cartão de Débito\n4-----Cartão Tabajará")
formaPag = ["Dinheiro", "Cartão de Cŕedito", "Cartão de Débito", "Cartão Tabajará"]
print(formaPag[1])
formaPagamento = int(input("Escolha a forma de pagamento: "))
print(formaPag[formaPagamento])
if formaPagamento == 4:
	valorTotal *= 0.95

print("=====Cupom Fiscal=====")
print("Tipo de Carne: ",tipoCarne[escolha+1])
#print("Quantidade de Carne: {}kg".format(quant))
#print("Forma de Pagamento: ",formaPag[formaPagamento])
print("Valor a ser pago: R${:.2f}".format(valorTotal))
