"""
Nombre: Diana Yamileika Tellez Ordoñez
Fecha: 18/01/2023
Descripcion: programa05.py
"""
class Alumnos: #Define una clase de nombre Alumnos
    matricula=None #Declara la variable matricula
    nombre=None #Declara la variable nombre
    def __init__(self, matricula, nombre): #Define el metodo init
        self.matricula=matricula #Asigna el valor de matricula
        self.nombre=nombre #Asigna el valor de nombre
        print("Objeto Alumnos") #Imprime el mensaje
objetoAlumno = Alumnos("111", "Dejah") #Crea un objeto de la clase Alumnos
objetoAlumno2 =Alumnos(nombre="John",matricula=222) #Crea un objeto de la clase Alumnos
