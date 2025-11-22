empleados = [ 
    {"id": 1, "nombre": "Carlos", "departamento": "Ventas", "salario": 1500}, 
    {"id": 2, "nombre": "Ana", "departamento": "IT", "salario": 2200}, 
    {"id": 3, "nombre": "Luis", "departamento": "Ventas", "salario": 1400} 
] 

def calcular_gasto_departamento(departamentos,depto): 
    total = 0 
    for empleado in departamentos: 
        if empleado["departamento"] == depto: 
            total += empleado["salario"] 
    return total
print(calcular_gasto_departamento(empleados, "IT"))