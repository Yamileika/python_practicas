"""
Nombre: Diana Yamileika Tellez Ordoñez
Fecha: 18/01/2023
Descripcion: programa04.py
"""
class A: #Define una clase de nombre A
    matricula=None #Declara la variable matricula     
    nombre=None #Declara la variable nombre
    def __init__(self, matricula, nombre): #Define el metodo init
        print("Constructor de la clase A") #Imprime el mensaje
        self.matricula=matricula #Asigna el valor de matricula
        self.nombre=nombre #Asigna el valor de nombre
objetoA = A("111", "Dejah")  #Crea un objeto de la clase A
print(objetoA.nombre) #Imprime el valor de la variable nombre
