#Archivo: EstructurasIterativas.py
#Descripcion: Ejemplo en el que se muestra la utilizacion de las distintas sentencias iterativas
#

suma_edades = 0
i = 1
while i <= 3:
    edad = (int)(input("Ingrese la edad en años:"))
    suma_edades+=edad
    i+=1

edad_promedio = suma_edades / 3
print('La edad promedio ingresada es %.2f' % (edad_promedio))

suma_edades = 0
for i in range(3):
    edad = (int)(input("Ingrese la edad en años:"))
    suma_edades+=edad
    print(f'Esta es la iteracion numero {i}')

edad_promedio = suma_edades / 3
print('La edad promedio ingresada es %.2f' % (edad_promedio))

while True:
    print('a')