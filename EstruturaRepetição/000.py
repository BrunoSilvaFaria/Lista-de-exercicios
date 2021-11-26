#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 
num = int(input("Digite um valor(0-10): "))
while num < 0 or num > 10:
	num = int(input("Valor inválido! Digite um valor(0-10): "))
else:
	print("Número informado foi: ",num)
