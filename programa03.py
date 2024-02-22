"""
Nombre: Diana Yamileika Tellez Ordoñez
Fecha: 18/01/2023
Descripcion: programa03.py
"""
class A: #Define una clase de nombre A
    matricula=None #Declara la variable matricula
    nombre=None #Declara la variable nombre
    def __init__(self): #Define el metodo init
        print("Constructor de la clase A") #Imprime el mensaje

objetoA = A() #Crea un objeto de la clase A
print(objetoA.nombre) #Imprime el valor de la variable nombre
