"""
O exercicio e bem simples vou das uma explicação básica sobre as funções presentes:
Funçoes:
main - ela e repomsavem por chamar todas as outras, o arquivo e executador nela
cadastrar_usuario - e a funcao que cadastra todos os usuarios e define um ID para eles, faciliando no filtro depois 
imprimir_valores - e reponsavel pela todas as formas de impressao presente no exercicio

"""

from os import system
banco_usuarios = {} # Cria a base de dados 
list_nomes = []
system("cls") # Limpa a tela

def imprimir_valores(opt):
    system("cls") # limpa o terminal 
    while True:
        # Cabacalho da impressao
        print("------Opções de impressão-------\n")
        print("1 - Imprime todos os valores")
        print("2 - Filtrar por nomes")
        print("3 - Filtrar por Campos")
        print("4 - Filtrar por nomes e campos")
        print("5 - Sair")
        try:
            escolha = int(input("Digite uma opcao: "))
            if escolha > 5 or escolha < 0: # Verifica se e uma opcao valida
                print("Valor invalido tente uma das opcoes acima...")
            if escolha == 5: # Sai da opcao de impressao 
                break
            if escolha == 1: # Aqui faz mostra todos os valores 
                print("---- Dados ----")
                print(banco_usuarios)
                print("\n\n")
            if escolha == 2: # Sepera todos o nomes em linhas (opcao de list esta comentado)
                for i in range(1, id + 1):
                    if i in banco_usuarios:
                        print(banco_usuarios[i]['nome'])
            """         
            # se quiser mostrar em lista basta tirar esse comentario("""""") e comentar o "print(banco_usuarios[i]['nome'])" de cima           
                        list_nomes.append(banco_usuarios[i]['nome'])
                print(list_nomes)
            """
            if escolha == 3: # Define o campo de busca e o valor buscado 
                busca = input("Digite o campo de busca: ")
                busca_valor = input("Digite o valor buscado: ")
                for i in range(1, id + 1):
                    if i in banco_usuarios:
                        if banco_usuarios[i][busca] == busca_valor:
                            print(f"{banco_usuarios[i]['nome']} - {banco_usuarios[i][busca]}")
            if escolha == 4: # Define os nomes e campos que podemos buscar 
                nome_de_busca = input("Digite os nomes que vamos buscar (Separados pode ,): ")
                nome_de_busca= nome_de_busca.split(",")
                campos_de_busca = input("Digite o campo que vamos buscar (Separados pode ,):")
                campos_de_busca = campos_de_busca.split(",")
                for i in range(1,id+1):
                    if i in banco_usuarios:
                        usuario = banco_usuarios[id]
                        list_dados4 = []
                        for campo in campos_de_busca:
                            if campo in usuario and usuario[campo] in nome_de_busca:
                                list_dados4.append(f"{campo}: {usuario[campo]}")
                        
                        if list_dados4:
                            print(f"ID: {id}")
                            print(", ".join(list_dados4))
        except ValueError: # Verifica se e uma opcao do tipo INT 
            print("Valor invalido... tente novamente")



def cadastrar_usuario(campos_obrigatorios):
    novo_usuario = {}

    print("Cadastro de novo usuário:")
    
    # mostra os campos obrigatorios para um cadastro
    for campo in campos_obrigatorios:
        valor = input(f"Digite o valor para '{campo}': ")
        novo_usuario[campo] = valor
    
    while True:
        # Pergunta se quiser adicionar um campo a mais
        campo_adicional = input("Digite o nome de um campo adicional (ou 'sair' para finalizar): ")
        
        if campo_adicional.lower() == "sair":
            break
        
        valor_adicional = input(f"Digite o valor para '{campo_adicional}': ")
        novo_usuario[campo_adicional] = valor_adicional
    # Atribui um ID para o usuario 
    banco_usuarios[id] = novo_usuario
    print("Usuário cadastrado com sucesso!")

# Definição dos campos obrigatórios (podem ser personalizados)
campos_obrigatorios = ('nome', 'idade', 'email')
id = 1
# Exemplo de uso 
while True:
    #cabeçalho
    print("---------------------------------")
    print("Digite '0' para sair\nDigite '1' para cadastrar usuario.\nDigite '2' para ver as opcoes de impressao.\n")
    print("---------------------------------")
    try:
        opt = int(input("Digite uma opção: "))
        if opt == 1 : # cadastra novo usuário
            cadastrar_usuario(campos_obrigatorios)
            id += 1
            system("cls")
        if opt == 2 : # imprime usuário
            imprimir_valores(opt)
        if opt == 0: # fecha o programa
            print("Finalizando banco ...")
            break
        if opt >2 or opt<0: # verifica valor inteiro
            print("Valor invalido... Tente outra opcao entre  0-1-2")
    except ValueError: # verifica se e numero 
        print("Valor invalido... Use apenas numeros")
