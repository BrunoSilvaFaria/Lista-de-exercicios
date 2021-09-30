#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). 

tamanhoArquivo = float(input("Digite o tamanho do arquivo: "))
velocidade = float(input("Digite a velocidade: "))
tempo = tamanhoArquivo / velocidade
print ("{:.2f}m".format(tempo / 60))
