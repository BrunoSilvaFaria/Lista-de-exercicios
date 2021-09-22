# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. 

celsius = float(input("Digite a temperatura: "))
fah = (celsius  * 9) / 5 + 32
print("{}ºC = {}ºF".format(celsius, fah))
