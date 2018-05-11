#Archivo: Variables.py
#Descripcion: Ejemplo en el que se muestra la utilizacion de variables, operadores, y las funciones print y type

#Uso de variables enteras
a = 10
b = 5
c = a + b
print("El valor de %d+%d=%d" % (a,b,c))
print("La variable a es de tipo ", type(a))

#Uso de variables flotantes
a = 10.5
b = 6.6
c = a * b
print("El valor de %.2f*%.2f=%.2f" % (a,b,c))

#Uso de variables booleanas
existe = True
print("La variable existe=",existe)
print("La variable existe=%d" % existe)
print("Si no existiera existe=",not existe)