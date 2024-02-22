"""Nombre del alumno: Diana Yamileika Tellez Ordoñez
Fecha: 15/02/2024
Descripción: Ejercicio de condicionales
"""

cadena = "Hola mundo python" #se declara una cadena de caracteres
a = "a" #se declara la variable a
e = "e" #se declara la variable e
i = "i" #se declara la variable i
o = "o" #se declara la varible o
u = "u" #se declara la variable u
i=0 #se inicializa la variable i en 0
j=0 #se inicializa la variable j en 0
k=0 #se inicializa la variable k en 0
l=0 #se inicializa la variable l en 0
m=0 #se inicializa la variable m en 0
for c in cadena: #cada caracter de la variable "cadena" se guarda en la variable "c"
    if c == a: #se utiliza la condicional if para ver si la variable "c" es igual a "a"
        i=i+1 #si la condicional es verdadera se suma 1 a la variable "i"
    if c == e: #se utiliza la condicional if para ver si la variable "c" es igual a "e"
        j=j+1 #si la condicional es verdadera se suma 1 a la variable "j"
    if c == i: #se utiliza la condicional if para ver si la variable "c" es igual a "i"
        k=k+1 #si la condicional es verdadera se suma 1 a la variable "k"
    if c == o: #se utiliza la condicional if para ver si la variable "c" es igual a "o"
        l=l+1 #s la condicional es verdadera se suma 1 a la variable "l"
    if c == u: #se utiliza la condicional if para ver si la variable "c" es igual a "u"
        m=m+1 #si la condicional es verdadera se suma 1 a la variable "m"
print("El número de letras a es de " + str(i)) #imprime el valor de la variable "i"
print("El número de letras e es de " + str(j)) #imprime el valor de la variable "j"
print("El número de letras i es de " + str(k)) #imprime el valor de la variable "k"
print("El número de letras o es de " + str(l)) #imprime el valor de la variable "l"
print("El número de letras u es de " + str(m)) #imprime el valor de la variable "m"
