def ordenar_insercion(vector):
    n = len(vector)

    # Recorrer todos los elementos del vector
    for i in range(1, n):
        valor_actual = vector[i]
        posicion = i

        # Desplazar los elementos mayores hacia la derecha
        while posicion > 0 and vector[posicion - 1] > valor_actual:
            vector[posicion] = vector[posicion - 1]
            posicion -= 1

        # Insertar el valor actual en la posición correcta
        vector[posicion] = valor_actual

# Ejemplo de uso
vector = [5, 3, 8, 2, 1]
print("Vector original:", vector)

# Ordenar el vector utilizando el método de inserción
ordenar_insercion(vector)

print("Vector ordenado:", vector)
