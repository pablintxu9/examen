alumnos = [ 
    {"nombre": "Ana", "notas": {"Mates": 8, "Lengua": 9}}, 
    {"nombre": "Luis", "notas": {"Mates": 4, "Lengua": 5}}, 
    {"nombre": "Eva", "notas": {"Mates": 9, "Lengua": 8}} 
]

def mejor_estudiante(alumnos):
    mayor=0
    mejor=""
    for alumno in alumnos:
        if alumno["notas"]["Mates"]>mayor:
            mayor=alumno["notas"]["Mates"]
            mejor=alumno["nombre"]
    return mejor
print(mejor_estudiante(alumnos))