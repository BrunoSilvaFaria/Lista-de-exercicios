"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16 
"""
numero = int(input("Digite um número menor que 1000: "))
def calculaNumero():
	global cen, dez, unid
	cen = numero // 100
	dez = numero % 100 // 10
	unid = numero % 100 % 10 // 1

def formataPrint():
	calculaNumero()
	if unid >=1:
		if cen == 1:
			print(cen,"centena",end=" ")
		elif cen > 1:
			print(cen,"centenas",end=" ")
		else:
			print("")
	else:
		if cen == 1:
			print(cen,"centena",end=" ")
		elif cen > 1:
			print(cen,"centenas",end=" ")
		else:
			print("")
		

	if cen >=1 and unid >= 1:
		if dez == 1:
			print(",",dez,"dezena",end=" ")
		elif dez > 1:
			print(",",dez,"dezenas",end=" ")
		else:
			print(end="")
	elif cen < 1:
		if dez == 1:
			print(dez,"dezena",end=" ")
		elif dez > 1:
			print(dez,"dezenas",end=" ")
		else:
			print(end="")
	elif unid < 1:
		if dez == 1:
			print("e",dez,"dezena",end=" ")
		elif dez > 1:
			print("e",dez,"dezenas",end=" ")
		else:
			print(end="")
	
		

	if cen ==0 and cen == 0:
		if unid == 1:
			print(unid,"unidade")
		elif unid > 1:
			print(unid,"unidades")
		else:
			print(end="")
	else:
		if unid == 1:
			print("e",unid,"unidade")
		elif unid > 1:
			print("e",unid,"unidades")
		else:
			print(end="")
		
		

		
if numero <= 1000:
	formataPrint()


