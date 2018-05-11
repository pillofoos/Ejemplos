def mayusculas(cadena):
    "Funcion que convierte a mayusculas una cadena"
    return cadena.upper()


def parametros(valor):
    "Funcion que modifica el valor y muestra la"
    valor += 5
    return None


def parametro_defecto(primero, segundo=10):
    "Funcion que muestra los parametros pasados"
    print(primero, segundo)
    return None


def parametro_variable(primero, *parametro_variable):
    "Funcion que muestra los parametros pasados"
    print(primero,end=" ")
    for valor in parametro_variable:
        print(valor,end=" ")
    print()
    return None


ejemplo = "prueba"
print(ejemplo, mayusculas(ejemplo))

numero = 2
print(numero, parametros(numero), numero)

parametro_defecto(5)
parametro_defecto(5, 20)

parametro_variable(1)
parametro_variable(1,2,3,4,5)