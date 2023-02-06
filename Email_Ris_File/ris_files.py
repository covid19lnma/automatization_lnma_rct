import io
import os
import rispy
import math

def particion(filepath,n,directorio): # Se le pasa la direccion del archivo ("filepath") y el numero de particiones ("n")
    with open(filepath,"r", encoding="utf-8") as bf: #Apertura de la direccion en modo lectura ("r = read"), codificacion ("utf-8")
        descripcion = bf.read() #Lectura del archivo base ("bf = base file")
        brincos = descripcion.split("\n\n\n\n") # Hacemos el split por el separador que tiene cada cita, se convierte en lista
        brincos.remove(brincos[-1]) #Quitamos  el ultimo atributo de la lista anterior, pues no nos interesa por ser un ""
        n_citas = descripcion.count("\n\n\n\n")
        n_citas_c_archivo = math.floor(descripcion.count("\n\n\n\n")/ n)
    if n_citas % 5 == 0:
        output=[brincos[i:i + n_citas_c_archivo] for i in range(0,len(brincos),n_citas_c_archivo)] #divide en una lista de listas
        #Creamos una lista que guarde cada 1 de las listas pero en formato de strings
        strings = []
        nombres = ["archivo1.ris","archivo2.ris","archivo3.ris","archivo4.ris","archivo5.ris"]
        for i in range(0,len(output)):
            strings.append("".join(output[i]))
            file = open(str(directorio) + "/" + nombres[i],"w", encoding = "utf-8")
            file.write(strings[i] + os.linesep)
            file.close()
        print(" Tamaño archivo grande: %i \n No. citas por achivo: %i \n No. citas ultimo archivo: %i" %(len(brincos),n_citas_c_archivo , len(output[4])))
    elif n_citas % 5 != 0: 
        output=[brincos[i:i + n_citas_c_archivo] for i in range(0,len(brincos),n_citas_c_archivo)] #divide en una lista de listas
        output[4] = sorted(output[4] + output[5])
        #Creamos una lista que guarde cada 1 de las listas pero en formato de strings
        strings = []
        nombres = ["archivo1.ris","archivo2.ris","archivo3.ris","archivo4.ris","archivo5.ris", "archivos6.ris"]
        for i in range(0,len(output)):
            strings.append("".join(output[i]))
            file = open(str(directorio) + "/" + nombres[i],"w", encoding = "utf-8")
            file.write(strings[i] + os.linesep)
            file.close()
        print(" Tamaño archivo grande: %i \n No. citas por achivo: %i \n No. citas ultimo archivo: %i" %(len(brincos),n_citas_c_archivo , len(output[4])))

