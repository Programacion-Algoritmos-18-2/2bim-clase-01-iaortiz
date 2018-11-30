#Importación de libreria Codec
import codecs

#Creación de clase MiArchivo
class MiArchivo:
    #Constructor
    def __init__(self):
        self.archivo = codecs.open("data/informacion.csv", "r")

    #Método para obtener la información del archivo
    def obtener_informacion(self):
        return self.archivo.readlines()

    #Metodo para cerrar el archivo
    def cerrar_archivo(self):
        self.archivo.close()

#Creacion de clase MiArchivoEscribir
class MiArchivoEscribir:
    #Constructor
    def __init__(self):
        self.archivo = codecs.open("data/new_informacion.csv", "a")

    #Metodo para Escribir en el archivo
    def agregar_informacion(self, p):
        self.archivo.write("%s|%.2f" % (p.nombre, p.promedio))

    #Método para cerrar el archivo
    def cerrar_archivo(self):
        self.archivo.close()
