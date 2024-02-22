"""
Programa: eva01.py
Alumno:Diana Yamileika Tellez Ordoñez
Matricula:1723110200
Fecha:29/01/2024
"""
class Profesor(): #Define la clase Profesor
    id = None #Se crea la categoria id
    nombre = None #Se crea la categoria nombre
    materias = None #Se crea la categoria materias
    def __init__(self, profesor, id, nombre): #Se llama al metodo init
      self.id = id #Asigna valores
      self.nombre = nombre #Asigna valores
      self.materias = materias #Asigna valores
      print("Constructor objeto - Profesor") #Imprime el texto
    def califica(self): #Define el metodo califica
      print(f"El profesor {self.nombre} califica evaluaciones de la materia {self.materias[0]}") # Asigna valores
    def pasaAsistencia(self): #Define el metodo pasa Asistencia
      print(f"El profesor {self.nombre} pasa asistencia") #Imprime el texto

profesor1 = Profesor("111","Profesor 1") #Asigna valores a las variables
profesor1 = materias("Materia 1") #Asigna valores a las variables
profesor1 = materias("Materia 2") #Asigna valores a las variables
profesor1 = califica() #Asigna valores a las variables
profesor1 = pasaAsistencia() #Asigna valores a las variables
