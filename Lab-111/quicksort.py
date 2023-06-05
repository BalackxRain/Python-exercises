def quicksort(vector):
    if len(vector) <= 1:
        return vector
    else:
        pivot = vector[0]
        less = [x for x in vector[1:] if x <= pivot]
        greater = [x for x in vector[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# Ejemplo de uso
vector = [5, 3, 8, 2, 1]
print("Vector original:", vector)

# Ordenar el vector utilizando el método de ordenación rápida (quicksort)
vector_ordenado = quicksort(vector)

print("Vector ordenado:", vector_ordenado)
