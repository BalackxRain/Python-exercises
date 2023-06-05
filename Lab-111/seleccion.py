def ordenar_seleccion(vector):
    n = len(vector)

    # Recorrer todos los elementos del vector
    for i in range(n):
        # Encontrar el índice del valor mínimo en el subvector no ordenado
        indice_minimo = i
        for j in range(i+1, n):
            if vector[j] < vector[indice_minimo]:
                indice_minimo = j

        # Intercambiar el valor mínimo con el primer elemento del subvector no ordenado
        vector[i], vector[indice_minimo] = vector[indice_minimo], vector[i]

# Ejemplo de uso
vector = [5, 3, 8, 2, 1]
print("Vector original:", vector)

# Ordenar el vector utilizando el método de selección
ordenar_seleccion(vector)

print("Vector ordenado:", vector)
