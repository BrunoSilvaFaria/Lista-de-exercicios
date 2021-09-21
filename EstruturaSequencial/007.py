#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. 

horaTrabalhada = float(input("Digite quantas horas trabalha: "))
valorHora = float(input("Digite quanto ganha por hora: "))
salario = horaTrabalhada * valorHora
print("Salário: R${:.2f}".format(salario))
