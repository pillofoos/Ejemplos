#Archivo: TomaDecisiones.py
#Descripcion: Ejemplo en el que se muestra la utilizacion de la sentencia if, if..else, if..elif..else
#             la funcion input y la utilizacion del depurador (antes y despues de conversion)

antiguedad = (int)(input("Ingrese la antiguedad en años:"))
if antiguedad > 5:
    print("Le corresponden mas de 15 dias")
else:
    print("Le corresponden solo 15 dias de licencia")

if antiguedad <=5:
    dias_licencia = 15
elif 5< antiguedad <=10:
    dias_licencia=20
elif 10< antiguedad <=15:
    dias_licencia = 25
else:
    dias_licencia = 35

print(f"Le corresponden {dias_licencia} dias de licencia")