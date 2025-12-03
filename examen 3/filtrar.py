def filtrar_palabras(lista, letra):
    filtro=[]
    for palabra in lista:
        if palabra.startswith(letra):
            filtro.append(palabra)
            return filtro
        else:
            return "palabra no encontrada"
print(filtrar_palabras(["mango", "pera","manzana"], "p"))