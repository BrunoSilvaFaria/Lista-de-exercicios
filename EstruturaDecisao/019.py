'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:

    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''
nota1 = float(input("Digite o valor da 1ª nota: "))
nota2 = float(input("Digite o valor da 2ª nota: "))
nota3 = float(input("Digite o valor da 3ª nota: "))
media = (nota1 + nota2 + nota3) / 3

if media <=10:
	print("Sua media foi de",media,". Você foi",end=" ")
	if media == 10:
		print("Aprovado com Distinção")
	elif media < 10 and media >= 7:
		print("Aprovado")
	else:
		print("Reprovado")
else:
	print("Média invalida")

