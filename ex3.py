
"""
O jogo e bem simples vou das uma explicação básica sobre as funções presentes:
Funçoes:
"le_arquivo" - Apenas le um arquivo .txt com varias palavras para fazer a escolha random (Fornecido pelo professor)
"main" - Aqui acontece todo o jogo 

"""

import random
import os

# Limpa o terminal
os.system("cls")

# Caminho do arquivo de palavras
arquivo = "lista_palavras.txt"

def le_arquivo(arq):
    """ Lê o arquivo especificado e retorna uma lista com todas as linhas """
    with open(arq, encoding="UTF-8") as f:
        return [linha.strip() for linha in f]

lista = le_arquivo(arquivo)

quanti_len = int(input("Qual é o tamanho da palavra que deseja adivinhar? "))

# Filtra as palavras do tamanho especificado
lista_criada = [palavra for palavra in lista if len(palavra) == quanti_len]

# Limpa o terminal novamente
os.system("cls")

# Escolhe uma palavra aleatória da lista
palavra = random.choice(lista_criada)
erros_quant = quanti_len * 2  # Número máximo de erros permitidos

list_tentativas = []
letras_nao_utilizadas = list('abcdefghijklmnopqrstuvwxyz')  # Todas as letras do alfabeto inicialmente

while True:
    if erros_quant > 0: # Verifica a quantidade de erros  que ainda tem e se forem maior 
        print(f"Você tem um total de {erros_quant} tentativas restantes.\n")
        print("Palavras tentadas:", ", ".join(list_tentativas))
        print("Letras não utilizadas:", ", ".join(letras_nao_utilizadas))
        
        tentativa = input("Digite uma palavra: ")
        
        if len(tentativa) != quanti_len: # Palavra digitada tem mais caracteres (listas)
            print("Tentativa inválida. A palavra deve ter exatamente", quanti_len, "letras.")
        else:
            list_tentativas.append(tentativa)
            if tentativa == palavra: # Certou e ganhou o jogo
                print("Parabéns! Você acertou a palavra:", palavra)
                break
            else:
                letras_corretas = [] #list com as letras corretas 
                letras_incorretas = [] # List com letras erradas que serao removidas do letras_nao_utilizadas
                for i in range(quanti_len):
                    if tentativa[i] == palavra[i]:
                        letras_corretas.append(tentativa[i])
                    elif tentativa[i] in palavra:
                        letras_incorretas.append(tentativa[i])
                
                if letras_corretas:
                    print("Letras corretas no lugar certo:", " ".join(letras_corretas))
                
                if letras_incorretas:
                    print("Letras corretas no lugar errado:", " ".join(letras_incorretas))
                
                letras_utilizadas = set(tentativa)
                letras_nao_utilizadas = [letra for letra in letras_nao_utilizadas if letra not in letras_utilizadas] # Atualiza as letras 
                
                erros_quant -= 1 # diminui a quantidade de tentativas restantes
    else:
        print("Fim de jogo! Você perdeu. A palavra era:", palavra) # Voce perdeu o jogo
        break