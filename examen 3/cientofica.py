import numpy as np 
import matplotlib.pyplot as ptl 
 
prof = [] 
temp = [] 

with open("mues_marinas.csv") as archivo:
    for linea in archivo:
        try:
            datos = linea.split(",")
            prof.append(float(datos[0]))
            temp.append(float(datos[1]))
        except ValueError:
            print ("Dato no valido, se omite la linea")
            continue

prof = np.array(prof)
temp = np.array(temp)
print(np.mean(temp))
print(np.array(temp)<20)

ptl.scatter(temp, prof)
ptl.show()
