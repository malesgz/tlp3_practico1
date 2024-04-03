def ejercicio_uno (n):
    # Variable que almacena el valor inicial de la secuencia.
    valores = [n]
    
    while n != 1:
        if n % 2 == 0:
            # Se reasigna el valor de la variable.
            n = n / 2
            valores.append(n)
        else:
            n = (n * 3) + 1
            # Pero si es impar.
            valores.append(n)
        # append es un método que permite agregar un elemento a una lista.
    return valores

print("Ejercicio 1: Hecho.")
assert ejercicio_uno(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"
