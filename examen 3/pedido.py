stock = { 
    "CPU": 10, 
    "RAM": 50, 
    "SSD": 20, 
    "Mouse": 0 
}
def procesar_pedido(stock, pedido):
    for componentes in stock:
        if componentes in pedido:
            if stock[componentes] >= pedido[componentes]:
                stock[componentes] -= pedido[componentes]
            else:
                return f"Stock insuficiente para {componentes}"
    return stock
pedido_cliente = {
    "CPU": 2, 
    "RAM": 4, 
    "Mouse": 1 
}
print(procesar_pedido(stock, pedido_cliente))