"""
Programa: eva02.py
Nombre completo (nombre primer_apellido segundo_apellido): Diana Yamileika Tellez Ordoñez
Matricula: 1723110200
Fecha:29/01/2024
"""
class Libro():#Define la clase Libro
    titulo = None #Se crea la categoria
    autor = None #Se crea la categoria
    prestado = None #Se crea la categoria
    anio_publicacion = None #Se crea la categoria
    genero = None #Se crea la categoria
  
    def __init__(self, titulo, autor, anio_publicacion, genero, prestado=False): #Define el metodo init
        self.titulo = titulo #Asigna valores
        self.autor = autor #Asigna valores
        self.prestado = prestado #Asigna valores
        self.anio_publicacion = anio_publicacion #Asigna valores
        self.genero = genero #Asigna valores
      
    def prestar(self):#Define el metodo
        self.prestado = True #Asigna valores
      
    def devolver(self):#Define el metodo
        self.prestado = False #Asigna valores
      
    def mostrar_informacion(self):
        print(f"Título: {self.titulo}\n")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.anio_publicacion}")
        print(f"Género: {self.genero}")
        print(f"Prestado: {'Sí' if self.prestado else 'No'}")


libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943, "Ficción")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, "Ficción",True)
libro1.prestar()
libro1.mostrar_informacion()
libro2.mostrar_informacion()
libro1.devolver()
libro1.mostrar_informacion()
libro2.mostrar_informacion()
