from cardapio import*

def adicionar_pedido(cardapio, pedidos):
    id = int(input("Digite o id do item: "))
    for i in cardapio:
        if i["id"] == id:
            item = i["nome"]
            id = i["id"]
            qtd = int(input("Quantas unidades você deseja: "))
            total = i['preco'] * qtd
    pedido = {
        "id": id,
        "item": item,
        "qtd": qtd,
        "total": total
    }
    pedidos.append(pedido)
    return pedidos