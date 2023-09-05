"""
Crie uma versão do jogo da velha 4x4. As regras são as mesmas da versão 3x3
"""

def Cria_tabuleiro():
    for _ in range(3):
        for _ in range(3):
            print('_ ', end="")
        print('\n')


"""
tab = [['O','O','X'],['O','X','O'],['X','O','O']]
l = [['X','O','X'],['X','-','-'],['X','-','']]

col = 2

print(tab)

print("Venceu = ", all([tab[x][col] == 'X' for x in range(len(tab))]))

"""

Cria_tabuleiro()