def filtrar_palabras(lista, letra):
    filtro=[]
    for palabra in lista:
        if palabra.startswith(letra):
            filtro.append(palabra)
    return filtro

print(filtrar_palabras(["manzana","banana","mandarina","pera","melon"],"m"))