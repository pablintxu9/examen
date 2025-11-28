#vocales de cadena
def contar_vocales(cadena):
    vocales=["a","e", "i","o","u","A","E","I","O","U"]
    contador=0
    for vocal in vocales:
        for letra in cadena:
            if letra == vocal:
                contador+=1
    return contador
print(contar_vocales("Hola Mundo"))

#tabla de multiplicar
def tabla(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
tabla(7)

#primos
def primos(n):
    if n<2:
        return True
    resto = n%divisor
    if resto ==0:
        
    
