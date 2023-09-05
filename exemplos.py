"""
Verificacao de vencedor

"""
# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

# Função para verificar se o jogo terminou
def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas, colunas e diagonais
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]) or all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

# Função principal do jogo
def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogo_em_andamento = True

    while jogo_em_andamento:
        imprimir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}")
        linha = int(input("Digite a linha (0, 1 ou 2): "))
        coluna = int(input("Digite a coluna (0, 1 ou 2): "))

        if linha < 0 or linha > 2 or coluna < 0 or coluna > 2 or tabuleiro[linha][coluna] != " ":
            print("Jogada inválida. Tente novamente.")
            continue

        tabuleiro[linha][coluna] = jogador_atual

        if verificar_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"O jogador {jogador_atual} venceu!")
            jogo_em_andamento = False
        elif all([elem != " " for linha in tabuleiro for elem in linha]):
            imprimir_tabuleiro(tabuleiro)
            print("O jogo empatou!")
            jogo_em_andamento = False

        jogador_atual = "O" if jogador_atual == "X" else "X"

if __name__ == "__main__":
    jogo_da_velha()