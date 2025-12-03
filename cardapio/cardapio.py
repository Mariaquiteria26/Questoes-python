import tabulate

def carregar_cardapio(cardapio):

    cardapio = [
{"id": 1, "nome": "Hambúrguer", "preco": 12.50},
{"id": 2, "nome": "Batata Frita", "preco": 7.00},
{"id": 3, "nome": "Refrigerante", "preco": 5.00}
]
    
def exibir_cardapio(cardapio):
    return print(tabulate(cardapio, headers='keys', tablefmt='fancy_gate'))

def buscar_pedido(cardapio, pedidos):
    id = int(input("Digite o id do item: "))
    for i in cardapio:
        if i["id"] == id:
            item = i["nome"]
            id = i["id"]