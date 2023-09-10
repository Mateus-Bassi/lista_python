"""
Crie uma versão do jogo da velha 4x4. As regras são as mesmas da versão 3x3

O jogo e bem simples vou das uma explicação básica sobre as funções presentes:
Funçoes:
“Criar_tabuleiro” - faz apenas a criacao visual do tabuleiro 
"Verificar_vitoria" - a cada jogada faz a verificacao se o Usuario da vez ganhou
"Jogo_da_velha" - faz o jogo acontecendo dentro de um while ate ter um vencedor
"main" - apenas executa a funcao jogo_da_velha

"""
from os import system

def Cria_tabuleiro(tabuleiro): #mostra o tabuleiro  (visual apenas)
    system("cls") # Limpa a tela
    for i in tabuleiro:
        for elem in i:
            print(elem + "  ", end = '')# Faz o print do tabuleiro formatado
        print()
    
def verificar_vitoria(tabuleiro):
    #Verificar linha
    for i in tabuleiro: # i e sua linha 
        if len(set(i)) == 1 and i[0]!='-':
            return True
    #Verificar Coluna
    for j in range(len(tabuleiro[0])): #j e a quantidade de colunas
        coluna = [tabuleiro[i][j] for i in range(len(tabuleiro))]
        if len(set(coluna)) == 1 and coluna[0] != '-':
            return True
    
    #Verificar diagonal1
    for i in range(len(tabuleiro[0])):
        diagonal1 = [tabuleiro[j][j] for j in range(len(tabuleiro[0]))]
        if len(set(diagonal1)) == 1 and diagonal1[0] !='-':
            return True
        
    #Verificar diagonal2
    for i in range(len(tabuleiro[0])):#quantidade de colunas
        diagonal_invertida = [tabuleiro[i][len(tabuleiro) - i - 1] for i in range(len(tabuleiro))]
        if len(set(diagonal_invertida)) == 1 and diagonal_invertida[0] != '-':
            return True
        
    return False   

def jogo_da_velha():# Jogo
    tabuleiro = [["-" for _ in range(4)] for _ in range(4 )] # Cria o tabuleiro
    Cria_tabuleiro(tabuleiro)# Chama o visual do tabuleiro
    jogador_atual = 'X'
    while True:
        # Testa se esta colocando um valor 'INT'
        try: 
            print(f"---Vez do jogador {jogador_atual}---")
            linha = int(input("Digite Qual linha vai marcar: "))
            
            # Testa se esta colocando um valor valido
            if linha >= 4 or linha < 0:
                print("Valor invalido")
                continue

            coluna = int(input("Digite Qual colunha vai marcar: "))
            # Testa se esta colocando uma valor valido
            if coluna>= 4 or coluna <0:
                print("Valor invalido")
                continue

            #Verifica se ja tem valor nesse local
            if tabuleiro[linha][coluna] == 'X' or tabuleiro[linha][coluna] == 'O':
                print("Ja foi jogado nesse local")
                continue
            else:    
                tabuleiro [linha][coluna] = jogador_atual # Registra o jogada
            
            # Mostra o tabuleiro
            Cria_tabuleiro(tabuleiro)

            if verificar_vitoria(tabuleiro) == True:
                #Alguem ganhou
                print(f"O jogador {jogador_atual} Ganhou")
                break
            
            # Define quem e o jogador da vez e faz a troca a cada jogada
            jogador_atual = 'O' if jogador_atual == 'X' else 'X' 
        except ValueError:
            print("Valor invalido tente novamente")

jogo_da_velha()