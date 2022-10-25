import io
import os
import rispy
import math

def particion(filepath,n,directorio): # Se le pasa la direccion del archivo ("filepath") y el numero de particiones ("n")
    with open(filepath ,"r", encoding="utf-8") as bf: #Apertura de la direccion en modo lectura ("r = read"), codificacion ("utf-8")
        descripcion = bf.read() #Lectura del archivo base ("bf = base file")
        brincos = descripcion.split("\n\n\n\n") # Hacemos el split por el separador que tiene cada cita, se convierte en lista
        brincos.remove(brincos[1]) #Quitamos  el ultimo atributo de la lista anterior, pues no nos interesa por ser un ""
        n_citas_c_archivo = math.ceil(descripcion.count("\n\n\n\n\n") / n) #Numero de citas por archivo usando funcion techo
        output=[brincos[i:i + n_citas_c_archivo] for i in range(0, len(brincos), n_citas_c_archivo)] #divide en una lista de listas
        #Creamos una lista que guarde cada 1 de las listas pero en formato de strings
        strings = []
        nombres = ["file1","file2","file3","file4","file5","file6","file7"]
        for i in range(0,len(output)):
            strings.append("".join(output[i]))
            file = open(str(directorio) + "/" + nombres[i] + ".ris" ,"w", encoding = "utf-8")
            file.write(strings[i] + os.linesep)
            file.close()
        print(len(brincos),n_citas_c_archivo, len(output), len(strings))

