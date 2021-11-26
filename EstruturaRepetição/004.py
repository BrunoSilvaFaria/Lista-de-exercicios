#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação. 
paisAhab = int(input("Digite a população do pais A: "))
taxaA = float(input("Digite a taxa de descimento da população do pais A: "))
paisBhab = int(input("Digite a população do pais B: "))
taxaB = float(input("Digite a taxa de descimento da população do pais B: "))
ano = 0
while paisAhab < paisBhab:
	paisAhab = paisAhab + (paisAhab * (taxaA / 100))
	paisBhab = paisBhab + (paisBhab * (taxaB / 100))
	ano +=1
else:
	print("É necessário",ano,"anos para que tenha o pais A tenha uma população maior!")
