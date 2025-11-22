def busqueda(lista, o):
    for i in range(len(lista)):
        if lista[i] == o:
            return i    
    return -1

print(busqueda([1,2,3,4,5,6,7,8,9], 5))
