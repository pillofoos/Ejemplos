#Archivo: Tuplas.py
#Descripcion: Ejemplo en el que se muestra la utilizacion de las tuplas
#

#Declaracion de una tupla
conjunto = (1,2,"tres","cuatro")

#Recorrido de una tupla como secuencia
i = 0
for elemento in conjunto:
    print(f'conjunto[{i}]={elemento}')
    i+=1

#Modificacion de un elemento de una tupla - No inmutable
#conjunto[0] = 0
#print('Despues de modificar, la lista quedo',conjunto)

#Eliminacion de un elemento de una tupla - No inmutable
#del(conjunto[0])

#Agregado de un elemento de una lista
#conjunto.append(100)
#print('Despues de agregar el elemento al final, la lista quedo',conjunto)

#Verificacion de a pertenencia

if 'cuatro' in conjunto:
    print("El cuatro esta en el conjunto")

#Eliminacion de la tupla entera
del conjunto

#Genera una excepcion - Manejo de excepciones
try:
   print('Despues de eliminar la el conjunto quedo',conjunto)
except:
    print('Ya no existe el conjunto')

