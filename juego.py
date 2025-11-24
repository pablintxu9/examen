class personaje:
    def __init__(self, vida,aguante,inteligencia,turno:bool=True):
        self.vida=vida
        self.aguante=aguante
        self.inteligencia=inteligencia
        self.turno=turno
    def __str__(self):
        return f"vida: {self.vida}\naguante: {self.aguante} \ninteligencia: {self.inteligencia} \nturno: {self.turno}"
    
class guerrero(personaje):
    def __init__(self):
        super().__init__(vida=150,aguante=100,inteligencia=50)

class hechicero(personaje):
    def __init__(self):
        super().__init__(vida=100,aguante=50,inteligencia=150)

print(guerrero())
print(hechicero())