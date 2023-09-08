"""
Desenvolver o jogo https://term.ooo/ a partir do arquivo lista_palavras.txt. O jogo deve serjogado por meio do terminal, mantendo a lógica do jogo original. Devem aparecer as letras quejá foram descobertas, as letras já tentadas no teclado e assim por diante. Atente-se àformatação

"""
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

quanti_len = int(input("Qual da quantiade de letras?")) # tamanho da palavra

lista_criada = []

for i in range(0,1000):
    if quanti_len == len(lista[i]):
        lista_criada.append(lista[i])

system("cls") # Limpa o terminal, mas precisa importar a blib. "from os import system"

# --------------------------------------------------------------------------------------------------------


palavra=random.choice(lista_criada) # Define a palavra escolhida
erros_quant = quanti_len * 2 # quanditade de erros que opde ser 

# Reposta print(palavra)

list_tentativas = []
while True:
        
        if erros_quant > 0: # Verifica quantas jogadas ainda tem (Esta funcionando)
            print(f"Você tem um total de um total de {erros_quant}\n")
            print("Palavras tentadas:")
            # imprime lista que dos chutes 
            
            tentativa = list(input("Digite uma palavra: "))
            if (len(tentativa)>quanti_len or len(tentativa)<quanti_len):
                print("Tentativa invalida, tente novamente")
            else:
                if list(tentativa) == palavra:
                    print("parabens voce ganhou")
                else:
                    # mostra a quantidade de erros 
                    list_tentativas.append(tentativa)
                    print("voce errou tente novamente")
                    erros_quant -= 1
        else:
             print("fim de jogo, YOU LOSE")
             break
