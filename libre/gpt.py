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
        return False
    for i in range(2,n):
        if n%i==0 and n!=i:
            return False
        else:
            return True
print(primos(7))

#invertir lista
def invertir(lista):
    listai=[]
    for i in range(len(lista)):
        listai.append(lista[len(lista)-1-i])
    return listai
print(invertir([1,2,3,4,5]))

#arbol
def arbol(n):
    for i in range(n):
        for j in range(2*i+1):
            print("*", end="")
        print()
arbol(5)
    
#palindromos
def palindromo(p):
    for i in range(len(p)):
        if p[i] != p[len(p)-1-i]:
            return False
    return True
print(palindromo("coser"))

def calculadora(a,b):
    print("1.Suma\n2.Resta\n3.Multiplicacion\n4.Division")
    operacion = input("Elige una operacion: ")
    print(operacion)
    if operacion == "1":
        return a+b
    elif operacion == "2":
        return a-b
    elif operacion == "3":
        return a*b
    elif operacion == "4":
        return a/b
    else:
        return "Operacion no valida"
print(calculadora(10,5))

#maximo minimo
def maximo_minimo(lista):
    maximo = lista[0]
    minimo = lista[0]
    for num in lista:
        if num > maximo:
            maximo = num
        if num < minimo:
            minimo = num
    return maximo, minimo
print(maximo_minimo([3,5,1,8,2]))

#sin duplicados
def sin_duplicados(lista):
    lista_sin=[]
    for elemento in lista:
        if elemento not in lista_sin:
            lista_sin.append(elemento)
    return lista_sin

def lista_sin2(lista):
    return list(set(lista))

#potencia
def potencia(base, exp):
    if exp ==0:
        return 1
    return base *(potencia(base, exp-1))
print(potencia(2,3))

#facotrial
def factorial(n):
    if n ==0:
        return 1
    return n*factorial(n-1)

