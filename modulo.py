def mayusculas(cadena):
    "Funcion que convierte a mayusculas una cadena"
    return cadena.upper()


def parametro_defecto(primero, segundo=10):
    "Funcion que muestra los parametros pasados"
    print(primero, segundo)
    return None

if __name__=='__main__':
    ejemplo = "prueba"
    print(ejemplo, mayusculas(ejemplo))

    parametro_defecto(5)
    parametro_defecto(5, 20)
