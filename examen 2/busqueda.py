lista=[1,3,2,,6,8,7]
def busqueda(lista,o):
    for i in range(len(lista)):
        if lista[i]==o:
            return i
    return -1