def exponente(base, exp):
    if exp == 0:
        return 1
    else:
        return base * exponente(base, exp - 1)

print(exponente(2, 4))