''''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal. 
'''
num1= float(input("Digite o valor do 1º numero: "))
num2= float(input("Digite o valor do 2º numero: "))
opera = int(input("Escolha a operação que deseja (1: + | 2: - | 3: * | 4: / ): "))
if opera == 1:
	res = num1 + num2
elif opera == 2:
	res = num1 - num2
elif opera == 3:
	res = num1 * num2
elif opera == 4:
	res = num1 / num2
else:
	print("Operação inválida")
print("O resultado é",res)
if res % 2 == 0:
	print("Número par")
else:
	print("Número impar")

if res > 1:
	print("Número positivo")
else:
	print("Número negativo")

if res // 1 == res:
	print("Número inteiro")
else:
	print("Número decimal")
