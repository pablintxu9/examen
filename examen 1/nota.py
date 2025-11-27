notas_clase = [ 
    {"nombre": "Ana", "nota": 8.5}, 
    {"nombre": "Luis", "nota": 4.0}, 
    {"nombre": "Marta", "nota": 9.2}, 
    {"nombre": "Pedro", "nota": 6.5} 
]

def calcular_promedio_notas(notas):
    total = 0
    for estudiante in notas:
        total += estudiante["nota"]
    promedio = total / len(notas)
    return promedio 

print(calcular_promedio_notas(notas_clase))

    
