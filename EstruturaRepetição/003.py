'''
	Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
	Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. 
'''
paisAhab = 80000
taxaA = 3 / 100
paisBhab = 200000
taxaB = 1.5 / 100
ano = 0
while paisAhab < paisBhab:
	paisAhab = paisAhab + (paisAhab * taxaA)
	paisBhab = paisBhab + (paisBhab * taxaB)
	ano +=1
else:
	print("É necessário",ano,"anos para que tenha o pais A tenha uma população maior!")
	
