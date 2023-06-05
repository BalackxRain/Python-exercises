def ordenar_burbuja(vector):
    n = len(vector)

    # Recorrer todos los elementos del vector
    for i in range(n):
        # Realizar comparaciones y realizar intercambios si es necesario
        for j in range(0, n-i-1):
            if vector[j] < vector[j+1]:
                vector[j], vector[j+1] = vector[j+1], vector[j]

# Ejemplo de uso
vector = [5, 3, 8, 2, 1]
print("Vector original:", vector)

# Ordenar el vector utilizando el método de burbuja
ordenar_burbuja(vector)

print("Vector ordenado:", vector)
n = len(vector)
for i in range(n):
    print(i)