# Código base para o jogo da forca

# O caminho para o arquivo 'lista_palavras.txt' deve ser indicado corretamente

# As palavras serão armazenadas em uma lista


"""
*** Funcionamento básico do jogo ***

O usuário digita o número de letras da palavra que será sorteada da lista.
Caso não haja palavras com este número de letras, o programa deve escolher
uma palavra qualquer e informar ao usuário.
O número de erros permitidos deve ser calculado a partir do número de letras
da palavra por meio de uma fórmula de sua escolha.
A cada acerto de letra, deve imprimir na tela as posições corretas e underscore
para indicar as posições faltantes.
"""

# início do programa

import random #biblioteca aleatoria
from os import system # comandos do sistema

system("cls") # limpa o terminal

arquivo = "lista_palavras.txt" # altere o caminho se necessário
                               # o ideal é que esteja no mesmo diretório do programa

def le_arquivo(arq):
    """ Lê arquivo especificado e retorna uma lista com todas as linhas """    
    with open(arq, encoding="UTF-8") as f:
        return [linha.strip() for linha in f] # método strip remove o '\n' do final da linha

lista = le_arquivo(arquivo)
#print(lista) # descomente para verificar se a lista está correta

quanti_len = int(input("Qual da quantiade de letras?"))

lista_criada = []

for i in range(0,1000):
    if quanti_len == len(lista[i]):
        lista_criada.append(lista[i])

#print(lista_criada)# Verificação da lista

palavra=random.choice(lista_criada) # Define a palavra escolhida
erros_quant = quanti_len * 2 # quanditade de erros que opde ser 

system("cls") # Limpa o terminal, mas precisa importar a blib. "from os import system"

print(palavra)# Reposta

print(f"Você tem um total de um total de {erros_quant}") # mostra a quantidade de erros 

chute_list= []
chute_prova=[]

palavra_list = []
for x in range(quanti_len):
    palavra_list.append(list(palavra)[x])
print(palavra_list)


for x in range(erros_quant):
    chute = input("Digite uma letra")
    chute_list.append(chute)
    if chute in palavra_list:
        chute_prova.insert(x,chute)
        print(chute_prova)
        print("Acertou 1")
    else:
        print(f"Errou Agora você tem um total de {erros_quant-x+1}")
    #.index verificar

print(chute_list)