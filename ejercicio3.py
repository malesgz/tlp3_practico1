# La función verifica el lugar de la fila y columna
# para obtener el número de la espiral.

def num_espiral(fila, columna):
    
    if fila == columna:
        return fila**2 - fila + 1
    
    if fila > columna:
        if fila % 2 == 0:
            return fila**2 - columna + 1
        else:
            return (fila - 1)**2 + columna
    else:
        if columna % 2 == 0:
            return (columna - 1)**2 + fila
        else:
            return columna**2 + 1 - fila

print("Ejercicio 3: Hecho.")
assert num_espiral(2, 2) == 3, "Error en el caso de prueba" 