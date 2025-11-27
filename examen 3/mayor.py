def mayor(lista):
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo
print(mayor([3, 5, 2, 8, 1]))