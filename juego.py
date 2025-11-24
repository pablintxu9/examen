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
    
 
    

guerrero=personaje(100,80,30)
mago=personaje(70,50,100)
print(guerrero)
mago.subir_nivel()
print(mago)
