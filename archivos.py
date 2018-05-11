#Archivo: archivos.py
#Descripcion: Ejemplo en el que se muestra la utilizacion de archivos de texto
#

def crear_archivo():
   f = open('prueba.txt','w')
   f.write('Primera Cadena\n')
   f.write('Segunda Cadena\n')
   f.write('Tercera Cadena\n')
   f.close()

def leer_archivo():
   f = open('prueba.txt','r')
   contenido = f.readlines();
   print(contenido)
   f.close()

def leer_archivo_con_mejoras():
    f = open('prueba.txt', 'r')
    contenido = f.readlines();
    for linea in contenido:
        print(linea)
    f.close()


if __name__=='__main__':
    leer_archivo_con_mejoras()



