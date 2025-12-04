def mayor(lista):
    mayor=lista[0]
    for num in lista:
        if num>=0:
            mayor=num
    return print(mayor)
mayor([1,2,14,3,5,8])