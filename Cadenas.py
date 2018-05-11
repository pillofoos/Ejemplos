#Archivo: Cadenas.py
#Descripcion: Ejemplo en el que se muestra la utilizacion de las cadenas de caracteres
#

texto = 'cadena de caracteres'
print('Esto es una ' + texto)
texto: str = 'se pueden colocar con comillas dobles'
print('Y tambien ' + texto)
texto_largo = """
    Puede colocarse un texto en
    comillas triples cuando el texto
    es demasiado largo y abarca varias lineas."""
print(texto_largo)

#Uso de la funcion len
print('La longitud del texto largo es '+str(len(texto_largo))+' caracteres')

#Slice o particionado
print(f'El primer caracter de "{texto}" es "{texto[0]}"')
print(f'Los primeros cinco caracteres de "{texto}" es "{texto[0:5]}"')
print(f'Los ultimos dos caracteres de "{texto}" es "{texto[-2:]}"')

#texto[0]="E" - Es inmutable

#Recorrido como secuencia
print("El texto largo impreso caracter por caracter es el siguiente")
for letra in texto_largo:
    print(letra,end='')
