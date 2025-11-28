def exponente(base, exp):
    if exp == 0:
        return 1
    else:
        return base * exponente(base, exp - 1)

print(exponente(2, 4))

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3))

lista_a=[1,2,3,4,5,6,7,8,9]
lista_b=[2,6]   
for i in lista_a:
    if i in lista_b:
        print(i,"esta en las dos listas")

def exponente(base,exp):
    if exp==0:
        print(1)
    else:
        print(base*exponente(base,exp-1))
    
