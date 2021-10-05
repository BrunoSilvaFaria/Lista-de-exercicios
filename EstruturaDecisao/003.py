#Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 
vogais = ["a", "e", "i", "o", "u"]
letra = str(input("Digite um letra: "))
if letra in vogais:
	print("Vogal")
else:
	print("Consoante")
