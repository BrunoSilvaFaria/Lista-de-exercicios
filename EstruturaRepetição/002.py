'''
Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd'; 
'''
nome = str(input("Digite seu nome: "))
while len(nome) < 3:
	nome = str(input("Digite seu nome: "))

idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
	idade = int(input("Digite sua idade: "))

sal = float(input("Digite seu salário: "))
while sal <= 0:
	sal = float(input("Digite seu salário: "))

sexo = str(input("Digite seu sexo(F - M): ")).capitalize()
while sexo != "F" and sexo != "M":
	sexo = str(input("Digite seu sexo(F - M): ")).capitalize()

estadoCivil = str(input("Digite seu estado civil: ")).capitalize()
while estadoCivil[0] != "S" and estadoCivil[0] != "C" and estadoCivil[0] != "V" and estadoCivil[0] != "D":
	estadoCivil = str(input("Digite seu estado civil: ")).capitalize() 
