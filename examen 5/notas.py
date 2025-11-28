import numpy as np
class alumno:
    def __init__(self, nota=None):
        sef.nota =list(nota) if nota is not None else []
    def leer_notas(self):
        open "notas.txt","r" as archivo:
        for nota in archivo:
                self.nota.append(float(nota.strip()))
    def calcular_media(self):
        media = np.array(self.nota).mean()
        return media
    
