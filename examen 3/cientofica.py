import numpy as np 
import matplotlib.pyplot as plt 
 
prof = [] 
temp = [] 

with open("mues_marias.csv") as archivo:
    for linea in archivo:
        datos = linea.split()
        prof.append(float(datos[0]))
        temp.append(float(datos[1]))
    
prof = np.array(prof)
temp = np.array(temp)
