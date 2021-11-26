#Altere o programa anterior para mostrar no final a soma dos números. 
num1 = int(input("Digite o inicio: "))
num2 = int(input("Digite o fim: "))
soma = 0
for x in range(num1, num2 + 1):
	soma += x
print("Soma: ",soma)
