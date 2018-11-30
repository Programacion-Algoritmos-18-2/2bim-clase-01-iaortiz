#Creación de clase Persona
class Persona(object):
    #Constructor
    def __init__(self, nom, n1, n2, n3):
        self.nombre = nom
        self.nota_1 = int(n1)
        self.nota_2 = int(n2)
        self.nota_3 = int(n3)
        self.promedio = 0.0
    #Creación de metodos agregar y obtener para cada variable
    def agregar_nombre(self, n):
        self.nombre = n

    def obtener_nombre(self):
        return self.nombre

    def agregar_nota1(self, n):
        self.nota_1 = int(n)

    def obtener_nota1(self):
        return self.nota_1
    
    def agregar_nota2(self, n):
        self.nota_2 = int(n)

    def obtener_nota2(self):
        return self.nota_2

    def agregar_nota3(self, n):
        self.nota_3 = int(n)
    
    def obtener_nota3(self):
        return self.nota_3

    #Método para calcular el promedio
    def obtener_promedio(self):
        #Suma de las 3 notas y las dividimos para 3
        self.promedio = (self.nota_1 + self.nota_2 + self.nota_3)/3
        return self.promedio
    #Método str para presentar
    def __str__(self):
        return "%-26s%.2f" % (self.nombre, self.obtener_promedio())
