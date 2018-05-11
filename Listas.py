#Archivo: Listas.py
#Descripcion: Ejemplo en el que se muestra la utilizacion de la lista
#

#Declaracion de una lista
conjunto = [1,2,3,4]

#Recorrido de una lista como secuencia
i = 0
for elemento in conjunto:
    print(f'conjunto[{i}]={elemento}')
    i+=1

#Modificacion de un elemento de una lista
conjunto[0] = 0
print('Despues de modificar, la lista quedo',conjunto)

#Eliminacion de un elemento de una lista
del(conjunto[0])
print('Despues de eliminar el elemento, la lista quedo',conjunto)

#Agregado de un elemento de una lista
conjunto.append(100)
print('Despues de agregar el elemento al final, la lista quedo',conjunto)