"""
Crie um jogo da velha NxN em que o usuário deve definir as dimensões do tabuleiro (sempre quadrado)

"""
from os import system

def Cria_tabuleiro(tabuleiro): #mostra o tabuleiro
    system("cls") # Limpa a tela
    for i in tabuleiro:
        for elem in i:
            print(elem + "  ", end = '')
        print()
    
def tamanho_tabuleiro(): # Cria o tamanho do tabuleiro editavel
    while True:
        try:
            tamanho_temp = int(input("Digite o tamanho do seu jogo: "))
            if tamanho_temp < 2:
                print("Valor invalido, tente numero maiores que 2")
            else:
                return tamanho_temp
        except ValueError:
            print("Digite um valor valido ...")


def jogo_da_velha():# Jogo
    tamanho =tamanho_tabuleiro()
    tabuleiro = [["-" for _ in range(tamanho)] for _ in range(tamanho)] # Cria o tabuleiro
    Cria_tabuleiro(tabuleiro)# Chama o visual do tabuleiro
    jogador_atual = 'X'
    while True:
        # Testa se esta colocando um valor 'INT'
        try: 
            print(f"---Vez do jogador {jogador_atual}---")
            linha = int(input("Digite Qual linha vai marcar: "))
            
            # Testa se esta colocando um valor valido
            if linha >= tamanho or linha < 0:
                print("Valor invalido")
                continue

            coluna = int(input("Digite Qual colunha vai marcar: "))
            # Testa se esta colocando uma valor valido
            if coluna>= tamanho or coluna <0:
                print("Valor invalido")
                continue

            #Verifica se ja tem valor nesse local
            if tabuleiro[linha][coluna] == 'X' or tabuleiro[linha][coluna] == 'O':
                print("Ja foi jogado nesse local")
                continue
            else:    
                tabuleiro [linha][coluna] = jogador_atual # Registra o jogador
            
            # Mostra o tabuleiro
            Cria_tabuleiro(tabuleiro)

            # Mostra 
            jogador_atual = 'O' if jogador_atual == 'X' else 'X' 
        except ValueError:
            print("Valor invalido tente novamente")

jogo_da_velha()