tab = [['O','O','X'],['O','X','O'],['X','O','O']]
l = [['X','O','X'],['X','-','-'],['X','-','']]

col = 2

print(tab)

print("Venceu = ", all([tab[x][col] == 'X' for x in range(len(tab))]))