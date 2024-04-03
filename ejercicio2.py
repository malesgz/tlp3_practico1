def ejercicio_dos (n, array):
    # Suma de todos los números de 1 hasta n.
    result = (n * (n + 1)) // 2
    # Suma de los elementos del array.
    total_array = sum(array)
    
    faltante = result - total_array
    # El resultado de esta resta es el número que falta.
    
    return faltante

print("Ejercicio 2: Hecho.")
assert ejercicio_dos(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"
    