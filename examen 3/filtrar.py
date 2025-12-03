def filtrar_palabras(lista, letra):
    filtro = []
    for palabras in lista:
        if palabras.startswith(letra):
            filtro.append(palabras)
            return 

print(filtrar_palabras(["mango", "pera", "manzana"], "m"))
