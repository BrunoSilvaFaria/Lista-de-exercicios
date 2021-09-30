#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

#    o produto do dobro do primeiro com metade do segundo .
#    a soma do triplo do primeiro com o terceiro.
#    o terceiro elevado ao cubo.

num1 = int(input("Digite o numero 1: "))
num2 = int(input("Digite o numero 2: "))
num3 = float(input("Digite o numero 3: "))
print("Produto do dobro do primeiro com metade do segundo:  ",num1*(num2/2))
print("Soma do triplo do primeiro com o terceiro: ",num1*3+num3)
print("Terceiro elevado ao cubo: ",num3**2)

