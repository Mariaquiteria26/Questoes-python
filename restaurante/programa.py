from funcoes import *


lista = []
while True:
    print('''
Menu:
[1] Ver cardápio
[2] Adicionar item ao pedido
[3] Ver pedido
[4] Remover item
[0] Finalizar
''')
    
    
    op = input('Digite a sua opção: ').strip()
    
    match op:
        case '1':
            exibir_cardapio(cardapio)
        case '2':
            exibir(lista)
        case '3':
            buscar(lista)
        case '4':
            mais_cara(lista)
        case '5':
            med = media(lista)
            print(f'Média de consumo: {med}')
        case '0':
            break
        case _:
            print('Opção inválida.')
    

