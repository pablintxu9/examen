class personaje:
    def __init__(self, vida,aguante,inteligencia):
        self.vida=vida
        self.aguante=aguante
        self.inteligencia=inteligencia
    def __str__(self):
        return f"vida: {self.vida}\naguante: {self.aguante} \ninteligencia: {self.inteligencia}"
    def subir_nivel(self):
        print("Elija qué atributo desea subir de nivel:")
        a = int(input("1. vida\n2. aguante\n3. inteligencia\n> "))
        if a == 1:
            self.vida += 10
        elif a == 2:
            self.aguante += 10
        elif a == 3:
            self.inteligencia += 10
        else:
            print("Opción no válida")
    def morir(self, vida):
        if vida <= 0:
            print("El personaje ha muerto")
    def turno(self):
        if True:
            print("Es tu turno")


class guerrero(personaje):
    def __init__(self, vida, aguante, inteligencia, fuerza):
        super().__init__(vida, aguante, inteligencia)
        self.fuerza = fuerza
    def __str__(self):
        return super().__str__() + f"\nfuerza: {self.fuerza}"
    def subir_nivel(self):
        super().subir_nivel()
        self.fuerza += 5
