#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 
letra = str(input("Digite F ou M: ")).capitalize()
if letra == "F":
	print("Sexo feminino")
elif letra == "M":
	print("Sexo masculino")
else:
	print("Sexo inválido")
