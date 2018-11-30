#Importación de paquetes y clases
from paquete_archivos.miarchivo import *
from paquete_modelo.mimodelo import Persona

#Creacion de 2 objetos, uno de tipo MiArchivo y otro MiArchivoEscribir
m = MiArchivo() # objeto para leer el archivo
m2 = MiArchivoEscribir() # objeto para escribir el archivo

#Creacion de variable lista para guardar lo que retorna el metodo
lista = m.obtener_informacion()
#Uso de split para eliminar el caracter " | " de la lista
lista = [l.split("|") for l in lista]
# Guardamos en lista todos los elementos a partir de la posición 1
lista = lista[1:]

print("NOMBRE\t\t\t\t\tPROMEDIO")
for d in lista:
    #Creación objeto con los parametros
    p = Persona(d[0],d[1],d[2],d[3])
    # Presentación
    print(p)
    m2.agregar_informacion(p)
#Cerramos los archivos
m.cerrar_archivo()
m2.cerrar_archivo()
