from time import sleep
import os as os
from functions import *

produtos = []
limpar()

print('\t  Seja Bem-Vindo!!')

sleep(1.5)
limpar()
sleep(2)

opcao = menu() #---> chamando a funcao menu e guardando o return da funcao numa variavel

while opcao != 4:
        if opcao == 1:
                opcao = cadastro_produtos(produtos, opcao)

        elif opcao == 2:
                limpar()
                sleep(0.5)
                mostrar_produtos(produtos)
                input('Aperte \'enter\' para voltar ao menu... ')
                limpar()
                opcao = menu()

        elif opcao == 3:
                limpar()
                mostrar_produtos(produtos)
                opcao = remover_produto(produtos)
                
        elif opcao == 4:
                limpar()
                sleep(0.5)
                print('Programa finalizado!')

        else:
                print('Opção inválida!')