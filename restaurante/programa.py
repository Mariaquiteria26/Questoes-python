from funcoes import *

cardapio = [
{"id": 1, "nome": "Gelato", "preco": 12.5},
{"id": 2, "nome": "Cannoli", "preco": 40},
{"id": 3, "nome": "Tiramisù", "preco": 159},
{"id": 4, "nome": "Bombolone", "preco": 70},
{"id": 5, "nome": "Bolo Caprese", "preco": 200},
{"id": 6, "nome": "Panna Cotta", "preco": 55}
]

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
            adicionar_pedido(cardapio, lista)
        case '3':
           exibir_pedido(lista)
        case '4':
            remover_item(lista)
        case '0':
            break
        case _:
            print('Opção inválida.')