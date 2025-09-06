from time import sleep
import os

def mostrar_produtos(produtos):
    print('Produtos: ', produtos)

def limpar ():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    limpar()
    print('\tNossas Opções')
    sleep(0.3)
    print('[1] Para cadastrar um novo produto')
    sleep(0.3)
    print('[2] Para consultar os produtos disponíveis')
    sleep(0.3)
    print('[3] Para remover um produto existente')
    sleep(0.3)
    print('[4] Para sair')
    sleep(0.3)

    opc_selecionada = int(input('\nDigite a opção e pressione \'enter\': '))
    opcao = opc_selecionada
    return opcao

def remover_produto(produtos):
    remover = int(input('Insira a localização do número que será removido: ')) - 1
    confirmar = input(f'Você realmente deseja remover \'{produtos[remover]}\': ')
    
    if confirmar.lower() == "sim":
        removido = produtos.pop(remover)
        print(f'Produto "{removido}" removido com sucesso!')
    opcao = menu()
    return opcao

def cadastro_produtos(produtos, opcao):
    qtde_produtos = int(input('Informe quantos produtos serão cadastrados: '))
    for i in range(qtde_produtos):
        item = input(f'Digite o Item {i + 1}: ')
        produtos.append(item)

    limpar()
    sleep(0.5)
    mostrar_produtos(produtos)

    while opcao != 4:
        print('Atuais Opções: \n[1] Menu \n[2] Cadastrar mais produtos\n[3] Remover produtos\n[4] Sair')
        final_produtos = int(input('Digite o escolhido: '))

        if final_produtos == 1:#menu
                limpar()
                opcao = menu()
                return opcao

        elif final_produtos == 2:#cadastrar mais produtos
                limpar()
                opcao = cadastro_produtos(produtos, opcao)

        elif final_produtos == 3:#--> Remover produto
                limpar()
                mostrar_produtos(produtos)
                opcao = remover_produto(produtos)
                return opcao
        
        elif final_produtos == 4:#sair
                limpar()
                opcao = 4
                limpar()
                print('Programa Finalizado!')
                sleep(2)
                limpar()

                opcao = 4
                return opcao

        else:
                print('Opção inválida!')