from tabulate import *

def carregar_cardapio():
    cardapio = [
{"id": 1, "nome": "Gelato", "preco": 12.5},
{"id": 2, "nome": "Cannoli", "preco": 40},
{"id": 3, "nome": "Tiramisù", "preco": 159},
{"id": 4, "nome": "Bombolone", "preco": 70},
{"id": 5, "nome": "Bolo Caprese", "preco": 200},
{"id": 6, "nome": "Panna Cotta", "preco": 55}
]

def exibir_cardapio(cardapio):
    print(tabulate(cardapio, headers='keys', tablefmt='fancy_gate'))
    

def adicionar_pedido(cardapio, pedidos):
    item = int(input("Digite o id do item: ")) .strip() 
    qtd = int(input("Quantas unidades você deseja: ")) .strip()
    total = cardapio[id]['preco'] * qtd
    pedido = {
        "item": item,
        "qtd": qtd,
        "total": total
    }
    pedidos.append(pedido)
    return pedidos


def exibir_pedido(pedidos):
    print(tabulate(pedidos, headers='keys', tablefmt='fancy_gate'))
    st = sum([pedido['total'] for pedido in pedidos])

def remover_item(pedidos):
    remover = int(input("Digite o id do item que você quer remover: "))
    for i in pedidos:
        if remover == i['item']:
          pedidos.remove('remover')