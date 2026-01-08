class turno:
    def __init__(self, turno, inicio):
        self.turno = turno
        self.inicio = inicio
class personaje(turno):
    def __init__(self, vida,aguante,inteligencia,turno, experiencia, escudo, inicio):
        super().__init__(self, turno, inicio)
        self.vida=vida
        self.aguante=aguante
        self. experiencia=experiencia
        self.inteligencia=inteligencia
        self.escudo=escudo

    def accion(self):
        if self.turno == True:
            print("¿Que accion le gustariai realizar?\n1-atacar\n2-curarse\n3-subir nivel")
            accion = int("")
            return accion
        else:
            print("¿quieres usar un escudo?")
            defensa = int("si o no")
            if defensa == "si":
               escudo -=1
               print("tequedan ", escudo)


    def elegir_clase():
        print("¿que clase te gustaria ser?\n1-guerrero\n2-mago")

    def subir_nivel(): 
        print("Elija qué atributo desea subir de nivel:")
        a = int(input("1. vida\n2. aguante\n3. inteligencia\n> "))
        if a == 1:
            self.vida += 10
        elif a == 2:
            self.aguante += 4
        elif a == 3:
            self.inteligencia += 2
        else:
            print("Opción no válida")

    def atacar(self):
        if accion == 2:
            pass
    def morir(self, vida):
        if vida <= 0:
            print("El personaje ha muerto")
            