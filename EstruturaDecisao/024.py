'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" 

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".
'''
listaPergunta = [ "Telefonou para a vítima?", "Esteve no local do crime?" ,"Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
tamanho = len(listaPergunta)
posi = 0
for x in range(0, tamanho):
	res = str(input(listaPergunta[x])).capitalize()
	if res[0:1] == "S":
		posi += 1

listaResposta = ["Inocente", "Suspeita", "Cúmplice", "Cúmplice", "Assassino"]
print(listaResposta[posi-1])
