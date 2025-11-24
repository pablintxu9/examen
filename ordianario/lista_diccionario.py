
ventas = [ 
    {"id": 1, "region": "Europa", "importe": 100}, 
    {"id": 2, "region": "USA", "importe": 50}, 
    {"id": 3, "region": "Europa", "importe": 200}, 
    {"id": 4, "region": "Asia", "importe": 150} 
]
def total_ventas_por_region(ventas, region):
    total = 0
    for venta in ventas:
        if venta["region"] == region:
            total += venta["importe"]
    return total
print (total_ventas_por_region(ventas, "Europa"))  # Output: 300