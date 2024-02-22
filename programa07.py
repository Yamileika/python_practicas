"""
Nombre: Diana Yamileika Tellez Ordoñez
Fecha: 18/01/2023
Descripcion: programa08.py
"""
class Alumno: #Define una clase de nombre Alumno
    matricula=None #Declara la variable matricula
    nombre=None #Declara la variable nombre
    def __init__(self, matricula, nombre): #Define el metodo init
        self.matricula=matricula #Asigna el valor de matricula
        self.nombre=nombre #Asigna el valor de nombre
        print("Objeto Alumno") #Imprime el mensaje
    def estudiar(self): #Define el metodo estudiar
        print(f"{self.nombre} estudia") #Imprime el mensaje recuperando valores que viene de una variable
    def sumar(self, numero1, numero2): #Define el metodo sumar
        suma=numero1+numero2 #Asigna al la variable suma el valor de la suma de numero1 y numero2
        print(str(numero1)+ "+" + str(numero2) + "=" + str(suma)) #Imprime el mensaje recuperando valores que viene de una variable
dejah=Alumno("111", "Dejah") #Crea un objeto de la clase Alumno
dejah.estudiar() #Llama al metodo estudiar
dejah.sumar(10,5) #Llama al metodo sumar
