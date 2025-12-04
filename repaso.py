def arbol(n):
    for i in range(1, n+1):
        for j in range(i):
            print("*", end="")
        print()


def factorial(n):
    if n == 0 :
        return 1
    else:
        return n*factorial(n-1)
print(factorial(3))
