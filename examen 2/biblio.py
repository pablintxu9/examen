class libro:
    def __init__(self,titulo,autor,disponible:bool=True):
        self.titulo=titulo
        self.autor=autor
        self.disponible=disponible

    def __str__(self):
        return f"titulo {self.titulo} - autor: {self.autor} - disponible: {self.disponible}"

class biblioteca:
    def __init__(self,libros):
        self.libros=libros

    def agregar_libro(self,libro):
        self.libros.append(libro)

    def prestar_libro(self,titulo):
        if titulo.disponible==True:
            titulo.disponible=False
            return f"el libro {titulo} ha sido prestado"
        else:
            return f"el libro {titulo} no esta disponible"
        


libro1=libro("quijote","cervantes",False)
libro2=libro("principe","machiavelo",True)
biblioteca1=biblioteca([])
biblioteca1.agregar_libro(libro1)
biblioteca1.agregar_libro(libro2)
print(libro2)


