class Precios:
    def __init__(self, lista=None):
        self.lista = list(lista) if lista is not None else []

    def agregar(self, valor):
        self.lista.append(valor)

    def total(self):
        return sum(self.lista)


if __name__ == "__main__":
    precios = Precios([10, 25, 5, 40, 15])
    print(precios.total())
