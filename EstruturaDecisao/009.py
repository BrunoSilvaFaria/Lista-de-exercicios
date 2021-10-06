"""
Faça um Programa que pergunte em que turno você estuda.
 Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. 
"""
periodo = str(input("Digite o turno que você estuda(M-V-N): ")).capitalize()
if periodo[0] == "M":
	print("Bom dia!")
elif periodo[0] == "V":
	print("Boa tarde!")
elif periodo[0] == "N":
	print("Boa noite!")
else:
	print("Valor inválido")
